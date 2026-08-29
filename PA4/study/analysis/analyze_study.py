"""Analyze PA4 summative evidence without manufacturing participant data.

The analyzer keeps independent evidence gates visible. A complete participant
count or a non-empty filename is never enough to report a complete study.
"""

from __future__ import annotations

import argparse
import csv
import json
import math
import re
import shutil
import statistics
import subprocess
from collections import defaultdict
from datetime import datetime
from pathlib import Path
from typing import Iterable


ROOT = Path(__file__).resolve().parents[2]
DEFAULT_DATA = ROOT / "study" / "data"
DEFAULT_RECORDINGS = ROOT / "evidence" / "recordings"
DEFAULT_OUTPUT = ROOT / "study" / "analysis"

PARTICIPANT_ID_PATTERN = re.compile(r"^P\d{2,}$")
ALLOWED_CONDITION_ORDERS = {"A_FIFA_FIRST", "B_CHESS_FIRST"}
ALLOWED_RECOVERY_OUTCOMES = {
    "NOT_NEEDED",
    "RECOVERED_INDEPENDENTLY",
    "RECOVERED_WITH_ASSISTANCE",
    "NOT_RECOVERED",
}
PRODUCTS = ("FIFA", "CHESS")
TASKS_BY_PRODUCT = {
    "FIFA": ("FIFA-T1", "FIFA-T2", "FIFA-T3", "FIFA-T4"),
    "CHESS": ("CHESS-T1", "CHESS-T2", "CHESS-T3", "CHESS-T4"),
}
QUESTIONNAIRE_ITEMS = {"FIFA": ("Q1", "Q2", "Q3", "Q4", "Q5"), "CHESS": ("Q1", "Q2", "Q3", "Q4", "Q5")}
INTERVIEW_PRODUCTS = {"BOTH", "FIFA", "CHESS"}
MIN_RECORDING_BYTES = 1024

PARTICIPANT_FIELDS = [
    "participant_id", "date", "target_profile_match", "device",
    "prior_fifa_experience", "prior_chess_experience", "recording_file",
    "consent_confirmed", "condition_order",
]
TASK_FIELDS = [
    "participant_id", "product", "task_id", "task_start", "task_end",
    "duration_seconds", "success_score", "errors", "wrong_paths",
    "assistance_count", "hesitation_count", "recovery_outcome", "notes", "recording_timestamp_reference",
]
QUESTIONNAIRE_FIELDS = [
    "participant_id", "product", "flow", "question_id", "question_text",
    "response_1_to_5", "notes",
]
INTERVIEW_FIELDS = [
    "participant_id", "product", "theme", "observation", "severity",
    "supporting_timestamp", "design_implication",
]


def clean(value: object) -> str:
    return str(value or "").strip()


def read_csv(path: Path, required: list[str]) -> tuple[list[dict[str, str]], list[str]]:
    if not path.exists():
        return [], [f"Missing file: {path.name}"]
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(handle)
        fields = reader.fieldnames or []
        missing = [field for field in required if field not in fields]
        rows = list(reader)
    return rows, [f"{path.name} missing columns: {', '.join(missing)}"] if missing else []


def parse_float(value: object, field: str, row_number: int, issues: list[str]) -> float | None:
    raw = clean(value)
    if not raw:
        return None
    try:
        result = float(raw)
    except ValueError:
        issues.append(f"{field} is not numeric at row {row_number}: {raw!r}")
        return None
    if not math.isfinite(result):
        issues.append(f"{field} is not finite at row {row_number}")
        return None
    return result


def parse_nonnegative_int(value: object, field: str, row_number: int, issues: list[str]) -> int | None:
    parsed = parse_float(value, field, row_number, issues)
    if parsed is None:
        issues.append(f"{field} is required at row {row_number}")
        return None
    if parsed < 0 or parsed != int(parsed):
        issues.append(f"{field} must be a non-negative integer at row {row_number}")
        return None
    return int(parsed)


def duration_from_row(row: dict[str, str], row_number: int, issues: list[str]) -> float | None:
    direct = clean(row.get("duration_seconds"))
    if direct:
        result = parse_float(direct, "duration_seconds", row_number, issues)
        if result is not None and result < 0:
            issues.append(f"negative task duration at row {row_number}")
            return None
        return result

    start, end = clean(row.get("task_start")), clean(row.get("task_end"))
    if not start or not end:
        issues.append(f"duration_seconds or task_start/task_end is required at row {row_number}")
        return None
    try:
        seconds = (datetime.fromisoformat(end) - datetime.fromisoformat(start)).total_seconds()
    except ValueError:
        issues.append(f"task_start/task_end are not ISO timestamps at row {row_number}")
        return None
    if seconds < 0:
        issues.append(f"negative task duration at row {row_number}")
        return None
    return seconds


def mean_or_blank(values: Iterable[float]) -> str:
    values = list(values)
    return f"{statistics.mean(values):.2f}" if values else ""


def median_or_blank(values: Iterable[float]) -> str:
    values = list(values)
    return f"{statistics.median(values):.2f}" if values else ""


def write_csv(path: Path, fieldnames: list[str], rows: list[dict[str, str]]) -> None:
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def verify_recording(path: Path) -> dict[str, str]:
    """Return a conservative media status for one expected video recording."""

    if path.suffix.lower() != ".mp4":
        return {"status": "RECORDING_INVALID_MEDIA", "detail": "expected .mp4 extension"}
    if not path.is_file():
        return {"status": "MISSING_RECORDING", "detail": "file does not exist"}
    try:
        size = path.stat().st_size
    except OSError as error:
        return {"status": "RECORDING_INVALID_MEDIA", "detail": f"cannot stat file: {error}"}
    if size < MIN_RECORDING_BYTES:
        return {"status": "RECORDING_INVALID_MEDIA", "detail": "file is too small to be meaningful media"}

    ffprobe = shutil.which("ffprobe")
    if not ffprobe:
        return {"status": "RECORDING_PRESENT_UNVERIFIED", "detail": "no local media probe is available"}

    try:
        probe = subprocess.run(
            [
                ffprobe,
                "-v", "error",
                "-show_entries", "stream=codec_type:format=duration",
                "-of", "json",
                str(path),
            ],
            capture_output=True,
            text=True,
            timeout=15,
            check=False,
        )
    except (OSError, subprocess.SubprocessError) as error:
        return {"status": "RECORDING_PRESENT_UNVERIFIED", "detail": f"media probe failed to run: {error}"}

    if probe.returncode != 0:
        return {"status": "RECORDING_INVALID_MEDIA", "detail": "media probe rejected the file"}
    try:
        payload = json.loads(probe.stdout)
    except (json.JSONDecodeError, TypeError):
        return {"status": "RECORDING_INVALID_MEDIA", "detail": "media probe returned invalid JSON"}
    streams = payload.get("streams", []) if isinstance(payload, dict) else []
    if not any(isinstance(stream, dict) and stream.get("codec_type") == "video" for stream in streams):
        return {"status": "RECORDING_INVALID_NO_VIDEO_STREAM", "detail": "media has no video stream"}
    try:
        duration = float((payload.get("format") or {}).get("duration"))
    except (AttributeError, TypeError, ValueError):
        return {"status": "RECORDING_INVALID_MEDIA", "detail": "media probe returned no readable duration"}
    if not math.isfinite(duration) or duration <= 0:
        return {"status": "RECORDING_INVALID_MEDIA", "detail": "media duration is not positive"}
    return {"status": "VERIFIED_RECORDING", "detail": f"ffprobe video stream and duration {duration:.3f}s"}


def participant_gate(participants: list[dict[str, str]], recordings_dir: Path) -> dict[str, object]:
    participant_ids = [clean(row.get("participant_id")) for row in participants if clean(row.get("participant_id"))]
    duplicate_ids = sorted({pid for pid in participant_ids if participant_ids.count(pid) > 1})
    metadata_issues: list[str] = []
    metadata_valid_ids: list[str] = []
    required_metadata = (
        "date", "target_profile_match", "device", "prior_fifa_experience",
        "prior_chess_experience", "recording_file", "condition_order",
    )
    for number, row in enumerate(participants, start=2):
        pid = clean(row.get("participant_id"))
        row_issues: list[str] = []
        if not pid or not PARTICIPANT_ID_PATTERN.fullmatch(pid):
            row_issues.append(f"participant_id must match P## at row {number}")
        if pid in duplicate_ids:
            row_issues.append(f"duplicate participant ID {pid} at row {number}")
        missing = [field for field in required_metadata if not clean(row.get(field))]
        if missing:
            row_issues.append(f"participant {pid or '<blank>'} missing metadata: {', '.join(missing)}")
        if clean(row.get("condition_order")) not in ALLOWED_CONDITION_ORDERS:
            row_issues.append(f"participant {pid or '<blank>'} has invalid condition_order")
        if clean(row.get("consent_confirmed")).lower() not in {"yes", "true", "1"}:
            row_issues.append(f"participant {pid or '<blank>'} lacks consent confirmation")
        if row_issues:
            metadata_issues.extend(row_issues)
        elif pid:
            metadata_valid_ids.append(pid)

    unique_valid_ids = sorted(set(pid for pid in participant_ids if PARTICIPANT_ID_PATTERN.fullmatch(pid)))
    count_status = "PASS" if len(unique_valid_ids) >= 5 else "BLOCKED_PARTICIPANT_COUNT"
    metadata_status = "PASS" if participants and not metadata_issues else "BLOCKED_PARTICIPANT_METADATA"

    recording_checks: dict[str, dict[str, str]] = {}
    verified: list[str] = []
    missing_recordings: list[str] = []
    for row in participants:
        pid = clean(row.get("participant_id"))
        if pid not in metadata_valid_ids:
            continue
        recording_name = clean(row.get("recording_file"))
        candidate = recordings_dir / Path(recording_name).name
        check = verify_recording(candidate)
        recording_checks[pid] = check
        if check["status"] == "VERIFIED_RECORDING":
            verified.append(pid)
        else:
            missing_recordings.append(pid)
    unique_verified = sorted(set(verified))
    recording_status = "PASS" if len(unique_verified) >= 5 and not missing_recordings else "BLOCKED_RECORDINGS"

    return {
        "participant_rows": len(participants),
        "unique_participant_ids": unique_valid_ids,
        "duplicate_participant_ids": duplicate_ids,
        "metadata_issues": metadata_issues,
        "verified_participant_ids": unique_verified,
        "verified_participant_count": len(unique_verified),
        "missing_recording_participant_ids": sorted(set(missing_recordings)),
        "recording_checks": recording_checks,
        "minimum_five_verified": len(unique_verified) >= 5,
        "gates": {
            "G01": {"name": "participant count", "status": count_status},
            "G02": {"name": "participant metadata completeness", "status": metadata_status, "issues": metadata_issues},
            "G03": {"name": "recording presence and validity", "status": recording_status},
        },
    }


def task_gate(tasks: list[dict[str, str]], verified_ids: set[str]) -> tuple[dict[str, object], list[dict[str, object]]]:
    issues: list[str] = []
    seen: set[tuple[str, str, str]] = set()
    parsed: list[dict[str, object]] = []
    for number, row in enumerate(tasks, start=2):
        pid, product, task_id = clean(row.get("participant_id")), clean(row.get("product")).upper(), clean(row.get("task_id"))
        key = (pid, product, task_id)
        if key in seen:
            issues.append(f"duplicate task row for {pid}/{product}/{task_id}")
        seen.add(key)
        if pid not in verified_ids:
            issues.append(f"task row {number} is not linked to a verified participant: {pid or '<blank>'}")
        if product not in PRODUCTS:
            issues.append(f"invalid product at task row {number}: {product!r}")
        elif task_id not in TASKS_BY_PRODUCT[product]:
            issues.append(f"invalid task_id at row {number}: {task_id!r}")
        duration = duration_from_row(row, number, issues)
        score = parse_float(row.get("success_score"), "success_score", number, issues)
        if score is None:
            issues.append(f"success_score is required at row {number}")
        elif score not in {0, 1, 2} or score != int(score):
            issues.append(f"success_score must be 0, 1, or 2 at row {number}")
        counts = {
            field: parse_nonnegative_int(row.get(field), field, number, issues)
            for field in ("errors", "wrong_paths", "assistance_count", "hesitation_count")
        }
        recovery = clean(row.get("recovery_outcome"))
        if recovery not in ALLOWED_RECOVERY_OUTCOMES:
            issues.append(f"invalid recovery_outcome at row {number}: {recovery!r}")
        parsed.append({
            "participant_id": pid,
            "product": product,
            "task_id": task_id,
            "duration": duration,
            "score": int(score) if score in {0, 1, 2} and score == int(score) else None,
            "errors": counts["errors"],
            "wrong_paths": counts["wrong_paths"],
            "assistance": counts["assistance_count"],
            "hesitations": counts["hesitation_count"],
            "recovery_outcome": recovery,
        })

    missing_tasks: list[str] = []
    for pid in sorted(verified_ids):
        for product in PRODUCTS:
            for task_id in TASKS_BY_PRODUCT[product]:
                if (pid, product, task_id) not in seen:
                    missing_tasks.append(f"{pid}/{product}/{task_id}")
    issues.extend(f"missing task row: {key}" for key in missing_tasks)
    status = "PASS" if verified_ids and not issues else "BLOCKED_TASK_DATA"
    return {
        "status": status,
        "row_count": len(tasks),
        "missing_tasks": missing_tasks,
        "issues": issues,
    }, parsed


def questionnaire_gate(questionnaire: list[dict[str, str]], verified_ids: set[str]) -> tuple[dict[str, object], dict[tuple[str, str], list[float]]]:
    issues: list[str] = []
    seen: set[tuple[str, str, str]] = set()
    groups: dict[tuple[str, str], list[float]] = defaultdict(list)
    for number, row in enumerate(questionnaire, start=2):
        pid, product, question_id = clean(row.get("participant_id")), clean(row.get("product")).upper(), clean(row.get("question_id"))
        key = (pid, product, question_id)
        if key in seen:
            issues.append(f"duplicate questionnaire row for {pid}/{product}/{question_id}")
        seen.add(key)
        if pid not in verified_ids:
            issues.append(f"questionnaire row {number} is not linked to a verified participant: {pid or '<blank>'}")
        if product not in PRODUCTS:
            issues.append(f"invalid questionnaire product at row {number}: {product!r}")
        elif question_id not in QUESTIONNAIRE_ITEMS[product]:
            issues.append(f"invalid question_id at row {number}: {question_id!r}")
        response = parse_float(row.get("response_1_to_5"), "response_1_to_5", number, issues)
        if response is None:
            issues.append(f"questionnaire response is required at row {number}")
        elif response < 1 or response > 5 or response != int(response):
            issues.append(f"questionnaire response must be an integer from 1 to 5 at row {number}")
        else:
            groups[(product, question_id)].append(response)

    missing_items: list[str] = []
    for pid in sorted(verified_ids):
        for product in PRODUCTS:
            for question_id in QUESTIONNAIRE_ITEMS[product]:
                if (pid, product, question_id) not in seen:
                    missing_items.append(f"{pid}/{product}/{question_id}")
    issues.extend(f"missing questionnaire row: {key}" for key in missing_items)
    status = "PASS" if verified_ids and not issues else "BLOCKED_QUESTIONNAIRE"
    return {"status": status, "row_count": len(questionnaire), "missing_items": missing_items, "issues": issues}, groups


def interview_gate(interviews: list[dict[str, str]], verified_ids: set[str]) -> dict[str, object]:
    issues: list[str] = []
    covered: set[str] = set()
    for number, row in enumerate(interviews, start=2):
        pid, product, theme = clean(row.get("participant_id")), clean(row.get("product")).upper(), clean(row.get("theme"))
        if pid not in verified_ids:
            issues.append(f"interview row {number} is not linked to a verified participant: {pid or '<blank>'}")
        if product not in INTERVIEW_PRODUCTS:
            issues.append(f"invalid interview product at row {number}: {product!r}")
        if not theme or not clean(row.get("observation")):
            issues.append(f"interview feedback and theme are required at row {number}")
        if not clean(row.get("supporting_timestamp")):
            issues.append(f"interview supporting_timestamp is required at row {number}")
        if pid in verified_ids and clean(row.get("observation")):
            covered.add(pid)
    missing = sorted(verified_ids - covered)
    issues.extend(f"missing post-test feedback record: {pid}" for pid in missing)
    status = "PASS" if verified_ids and not issues else "BLOCKED_INTERVIEW_DATA"
    return {"status": status, "row_count": len(interviews), "missing_participants": missing, "issues": issues}


def build_task_metrics(parsed_tasks: list[dict[str, object]]) -> list[dict[str, str]]:
    task_groups: dict[tuple[str, str], list[dict[str, object]]] = defaultdict(list)
    for task in parsed_tasks:
        task_groups[(str(task["product"]), str(task["task_id"]))].append(task)
    metrics: list[dict[str, str]] = []
    for (product, task_id), rows in sorted(task_groups.items()):
        scored = [row for row in rows if row["score"] in {0, 1, 2}]
        durations = [float(row["duration"]) for row in rows if row["duration"] is not None]
        error_rows = [row for row in rows if row["errors"] is not None]
        wrong_rows = [row for row in rows if row["wrong_paths"] is not None]
        assisted_rows = [row for row in rows if row["assistance"] is not None]
        hesitation_rows = [row for row in rows if row["hesitations"] is not None]
        metrics.append({
            "product": product,
            "task_id": task_id,
            "participant_rows": str(len(rows)),
            "independent_success_rate": f"{sum(row['score'] == 2 for row in scored) / len(scored):.3f}" if scored else "",
            "any_success_rate": f"{sum(row['score'] in {1, 2} for row in scored) / len(scored):.3f}" if scored else "",
            "median_duration_seconds": median_or_blank(durations),
            "mean_duration_seconds": mean_or_blank(durations),
            "error_rate": f"{sum(float(row['errors']) > 0 for row in error_rows) / len(error_rows):.3f}" if error_rows else "",
            "wrong_path_rate": f"{sum(float(row['wrong_paths']) > 0 for row in wrong_rows) / len(wrong_rows):.3f}" if wrong_rows else "",
            "assistance_rate": f"{sum(float(row['assistance']) > 0 for row in assisted_rows) / len(assisted_rows):.3f}" if assisted_rows else "",
            "hesitation_rate": f"{sum(float(row['hesitations']) > 0 for row in hesitation_rows) / len(hesitation_rows):.3f}" if hesitation_rows else "",
        })
    return metrics


def analyze(data_dir: Path, recordings_dir: Path, output_dir: Path) -> dict[str, object]:
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "charts").mkdir(parents=True, exist_ok=True)
    issues: list[str] = []
    participants, errors = read_csv(data_dir / "participants.csv", PARTICIPANT_FIELDS)
    issues.extend(errors)
    tasks, errors = read_csv(data_dir / "task-results.csv", TASK_FIELDS)
    issues.extend(errors)
    questionnaire, errors = read_csv(data_dir / "questionnaire.csv", QUESTIONNAIRE_FIELDS)
    issues.extend(errors)
    interviews, errors = read_csv(data_dir / "interview-coding.csv", INTERVIEW_FIELDS)
    issues.extend(errors)

    participant = participant_gate(participants, recordings_dir)
    issues.extend(participant["metadata_issues"])
    if participant["duplicate_participant_ids"]:
        issues.append(f"Duplicate participant IDs: {', '.join(participant['duplicate_participant_ids'])}")
    verified_ids = set(participant["verified_participant_ids"])

    task, parsed_tasks = task_gate(tasks, verified_ids)
    questionnaire_result, questionnaire_groups = questionnaire_gate(questionnaire, verified_ids)
    interview = interview_gate(interviews, verified_ids)
    issues.extend(task["issues"])
    issues.extend(questionnaire_result["issues"])
    issues.extend(interview["issues"])

    gates = {
        **participant["gates"],
        "G04": {"name": "task-result completeness", "status": task["status"], "issues": task["issues"]},
        "G05": {"name": "questionnaire completeness", "status": questionnaire_result["status"], "issues": questionnaire_result["issues"]},
        "G06": {"name": "interview/feedback completeness", "status": interview["status"], "issues": interview["issues"]},
    }
    quantitative_status = "PASS" if task["status"] == "PASS" and questionnaire_result["status"] == "PASS" else "BLOCKED_EXTERNAL_EVIDENCE"
    gates["G07"] = {"name": "quantitative-analysis readiness", "status": quantitative_status}
    report_status = "PASS" if all(gates[key]["status"] == "PASS" for key in ("G01", "G02", "G03", "G04", "G05", "G06")) else "BLOCKED_EXTERNAL_EVIDENCE"
    gates["G08"] = {"name": "final summative-report readiness", "status": report_status}

    if gates["G02"]["status"] != "PASS" and participant["participant_rows"] >= 5:
        status = gates["G02"]["status"]
    else:
        status_priority = ("G01", "G02", "G04", "G05", "G06", "G03", "G07", "G08")
        status = "PASS"
        for key in status_priority:
            if gates[key]["status"] != "PASS":
                status = gates[key]["status"]
                break

    task_metrics = build_task_metrics(parsed_tasks)
    questionnaire_summary = [
        {
            "product": product,
            "question_id": question_id,
            "response_count": str(len(values)),
            "mean_response_1_to_5": mean_or_blank(values),
        }
        for (product, question_id), values in sorted(questionnaire_groups.items())
    ]
    summary_rows = [
        {"metric": key, "value": str(gates[key]["status"]), "status": gates[key]["status"], "notes": gates[key]["name"]}
        for key in ("G01", "G02", "G03", "G04", "G05", "G06", "G07", "G08")
    ]
    summary_rows.extend([
        {"metric": "verified_participant_count", "value": str(participant["verified_participant_count"]), "status": gates["G03"]["status"], "notes": "Only consented recordings with positive duration and a video stream count."},
        {"metric": "task_row_count", "value": str(len(tasks)), "status": gates["G04"]["status"], "notes": "Every verified participant must have all assigned FIFA and Chess tasks."},
        {"metric": "questionnaire_response_count", "value": str(len(questionnaire)), "status": gates["G05"]["status"], "notes": "Five raw items are required for each product and verified participant."},
        {"metric": "interview_code_count", "value": str(len(interviews)), "status": gates["G06"]["status"], "notes": "At least one timestamped post-test feedback record is required per participant."},
    ])
    write_csv(output_dir / "summary.csv", ["metric", "value", "status", "notes"], summary_rows)
    write_csv(output_dir / "task-metrics.csv", [
        "product", "task_id", "participant_rows", "independent_success_rate", "any_success_rate",
        "median_duration_seconds", "mean_duration_seconds", "error_rate", "wrong_path_rate", "assistance_rate",
        "hesitation_rate",
    ], task_metrics)
    write_csv(output_dir / "questionnaire-summary.csv", ["product", "question_id", "response_count", "mean_response_1_to_5"], questionnaire_summary)

    report_lines = [
        "# PA4 study analysis report",
        "",
        f"Analysis status: **{status}**",
        "",
        "This report is generated from the current CSV templates. It does not create or infer participant evidence.",
        "",
        "## Independent evidence gates",
        "",
    ]
    for key in ("G01", "G02", "G03", "G04", "G05", "G06", "G07", "G08"):
        report_lines.append(f"- {key} {gates[key]['name']}: **{gates[key]['status']}**")
    report_lines.extend([
        "",
        "## Evidence counts",
        "",
        f"- Participant rows: {participant['participant_rows']}",
        f"- Verified recordings: {participant['verified_participant_count']}",
        f"- Task rows: {len(tasks)}",
        f"- Questionnaire rows: {len(questionnaire)}",
        f"- Interview/feedback rows: {len(interviews)}",
        "",
        "## Validation issues",
        "",
    ])
    report_lines.extend(f"- {issue}" for issue in issues) if issues else report_lines.append("- None detected by the schema and numeric validation pass.")
    report_lines.extend([
        "",
        "## Interpretation guardrail",
        "",
        "Do not report partial or synthetic rows as summative findings. With a small course sample, use descriptive statistics only. Concurrent think-aloud can affect duration; do not treat these task times as natural unmoderated performance or compare them with an unrelated baseline. Hesitation is recorded separately and does not alter success_score by itself.",
    ])
    (output_dir / "analysis-report.md").write_text("\n".join(report_lines) + "\n", encoding="utf-8")

    result = {
        "status": status,
        "participant_row_count": participant["participant_rows"],
        "verified_participant_count": participant["verified_participant_count"],
        "task_row_count": len(tasks),
        "questionnaire_row_count": len(questionnaire),
        "interview_row_count": len(interviews),
        "gate": participant,
        "gates": gates,
        "issues": issues,
        "task_metric_groups": len(task_metrics),
        "questionnaire_rows": len(questionnaire),
        "interview_rows": len(interviews),
    }
    (output_dir / "analysis-result.json").write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    return result


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--data-dir", type=Path, default=DEFAULT_DATA)
    parser.add_argument("--recordings-dir", type=Path, default=DEFAULT_RECORDINGS)
    parser.add_argument("--output-dir", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    result = analyze(args.data_dir, args.recordings_dir, args.output_dir)
    print(json.dumps(result, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
