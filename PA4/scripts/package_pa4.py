"""Build the PA4 working archive and guard official package generation.

The working archive is allowed while participant-dependent evidence is absent.
The official archive is created only when every mandatory submission gate is
pass. A blocked run returns explicit blockers and preserves any prior official
archive without replacing it.
"""

from __future__ import annotations

import csv
import json
import re
import zipfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
FINAL = ROOT / "final"
WORKING_OUTPUT = FINAL / "Group10-PA4-WorkingEvidence.zip"
SUBMISSION_OUTPUT = FINAL / "Group10-PA4.zip"
ANALYSIS_RESULT = ROOT / "study" / "analysis" / "analysis-result.json"
QA_RESULT = ROOT / "qa" / "prototype-browser-qa.json"
CHESS_VALIDATION = ROOT / "qa" / "chess-scenario-validation.md"
ACCEPTANCE_MATRIX = ROOT / "qa" / "remediation-round2-acceptance-matrix.md"


WORKING_FILES = [
    "README.md",
    "demo/DEMO-SCRIPT.md",
    "evidence/pa3-pa4-traceability.csv",
    "evidence/recordings/README.md",
    "prototype/index.html",
    "prototype/styles.css",
    "prototype/app.js",
    "prototype/README.md",
    "qa/acceptance-matrix.md",
    "qa/remediation-acceptance-matrix.md",
    "qa/remediation-round2-acceptance-matrix.md",
    "qa/prototype-browser-qa.json",
    "qa/chess-scenario-validation.md",
    "qa/validate_chess_scenario.py",
    "study/study-plan.md",
    "study/facilitator-script.md",
    "study/post-test-interview.md",
    "study/data/participants.csv",
    "study/data/task-results.csv",
    "study/data/questionnaire.csv",
    "study/data/interview-coding.csv",
    "study/analysis/analyze_study.py",
    "study/analysis/test_analyze_study.py",
    "study/analysis/analysis-report.md",
    "study/analysis/analysis-result.json",
    "study/analysis/summary.csv",
    "study/analysis/task-metrics.csv",
    "study/analysis/questionnaire-summary.csv",
    "work/context-audit.md",
    "work/decision-log.md",
    "work/pa1-continuity.md",
    "work/pa2-continuity.md",
    "work/pa3-continuity.md",
    "work/pa4-requirements.md",
    "work/remediation-context.md",
    "work/remediation-decision-log.md",
    "work/remediation-audit.md",
    "work/remediation-round2-memory-aware-audit.md",
    "work/remediation-round2-decision-log.md",
    "work/external-blockers.md",
    "scripts/build_pa4_reports.py",
    "scripts/test_build_pa4_reports.py",
    "scripts/capture-prototype-qa.mjs",
    "scripts/package_pa4.py",
    "scripts/render_pdf_browser.mjs",
    "source/Group10-PA4-HifiProtype.docx",
    "source/Group10-PA4-SummativeUserStudy.docx",
    "source/Group10-PA4-WeeklyReport.docx",
    "final/Group10-PA4-HifiProtype.pdf",
    "final/Group10-PA4-SummativeUserStudy.pdf",
    "final/Group10-PA4-WeeklyReport.pdf",
]

SUBMISSION_FILES = [
    "final/Group10-PA4-HifiProtype.pdf",
    "final/Group10-PA4-SummativeUserStudy.pdf",
    "final/Group10-PA4-WeeklyReport.pdf",
]


def resolve(relative_path: str) -> Path:
    return ROOT / Path(relative_path)


def require_files(relative_paths: list[str]) -> list[Path]:
    missing = [relative for relative in relative_paths if not resolve(relative).is_file()]
    if missing:
        raise SystemExit("Missing required PA4 artifacts:\n- " + "\n- ".join(missing))
    return [resolve(relative) for relative in relative_paths]


def screenshot_files() -> list[Path]:
    files = sorted((ROOT / "evidence" / "prototype-screenshots").glob("*.png"))
    if not files:
        raise SystemExit("No prototype screenshots are available for the working-evidence archive")
    return files


def reject_synthetic_rows() -> None:
    evidence_paths = [
        *sorted((ROOT / "study" / "data").glob("*.csv")),
        ROOT / "evidence" / "recordings" / "README.md",
    ]
    markers = ("SYNTHETIC TEST DATA", "dummy recording", "fake participant")
    violations: list[str] = []
    for path in evidence_paths:
        content = path.read_text(encoding="utf-8", errors="replace").lower()
        for marker in markers:
            if marker.lower() in content:
                violations.append(f"{path.relative_to(ROOT)} contains {marker!r}")
    if violations:
        raise SystemExit("Synthetic evidence marker detected:\n- " + "\n- ".join(violations))


def validate_templates() -> None:
    expected = {
        "study/data/participants.csv": {
            "participant_id", "date", "target_profile_match", "device",
            "prior_fifa_experience", "prior_chess_experience", "recording_file",
            "consent_confirmed", "condition_order",
        },
        "study/data/task-results.csv": {
            "participant_id", "product", "task_id", "task_start", "task_end",
            "duration_seconds", "success_score", "errors", "wrong_paths",
            "assistance_count", "hesitation_count", "recovery_outcome", "notes",
            "recording_timestamp_reference",
        },
    }
    for relative, expected_fields in expected.items():
        with resolve(relative).open("r", encoding="utf-8-sig", newline="") as handle:
            actual = set(csv.DictReader(handle).fieldnames or [])
        if actual != expected_fields:
            raise SystemExit(
                f"Unexpected CSV schema in {relative}: expected {sorted(expected_fields)}, got {sorted(actual)}"
            )


def read_json(path: Path) -> dict[str, object]:
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return {}
    return value if isinstance(value, dict) else {}


def hifi_gate_text() -> str:
    try:
        from pypdf import PdfReader
    except ImportError:
        return ""
    reader = PdfReader(str(resolve(SUBMISSION_FILES[0])))
    return "\n".join(page.extract_text() or "" for page in reader.pages)


def validate_hifi_link_gate() -> None:
    text = hifi_gate_text()
    if text and "youtube.com" not in text.lower() and "required external evidence" not in text.lower():
        raise SystemExit("Hi-fi PDF must contain a genuine YouTube URL or the explicit external-evidence gate")


def acceptance_matrix_statuses(text: str) -> dict[str, str]:
    statuses: dict[str, str] = {}
    for line in text.splitlines():
        fields = [field.strip() for field in line.split("|")]
        if len(fields) < 4 or not re.fullmatch(r"R2AC\d+", fields[1]):
            continue
        statuses[fields[1]] = fields[3]
    return statuses


def validate_participant_readiness_matrix(text: str) -> list[str]:
    heading = "## Participant-readiness hard gate"
    if heading not in text:
        return ["participant-readiness hard gate is missing from the acceptance matrix"]

    gate_text = text.split(heading, 1)[1]
    range_match = re.search(
        r"R2AC(\d+)\s*[-\u2010\u2011\u2012\u2013\u2014\u2015]\s*R2AC(\d+)",
        gate_text,
    )
    if not range_match:
        return ["participant-readiness hard-gate range is missing from the acceptance matrix"]

    start, end = (int(value) for value in range_match.groups())
    if start > end:
        return ["participant-readiness hard-gate range is invalid in the acceptance matrix"]

    statuses = acceptance_matrix_statuses(text)
    blockers: list[str] = []
    for number in range(start, end + 1):
        criterion = f"R2AC{number:02d}"
        status = statuses.get(criterion)
        if status is None:
            blockers.append(f"{criterion} is missing from the acceptance matrix")
        elif status != "PASS":
            blockers.append(f"{criterion} is {status}")
    return blockers


def acceptance_matrix_blockers() -> list[str]:
    try:
        text = ACCEPTANCE_MATRIX.read_text(encoding="utf-8")
    except OSError:
        return ["participant-readiness acceptance matrix is missing or unreadable"]
    return validate_participant_readiness_matrix(text)


def validate_local_readiness() -> tuple[str, list[str]]:
    blockers: list[str] = []
    qa = read_json(QA_RESULT)
    checks = qa.get("checks", [])
    if qa.get("status") != "PASS" or not isinstance(checks, list) or any(not isinstance(check, dict) or not check.get("passed") for check in checks):
        blockers.append("local browser QA is not fully PASS")
    if "Status: **PASS**" not in CHESS_VALIDATION.read_text(encoding="utf-8", errors="replace"):
        blockers.append("Chess scenario validation is not PASS")
    analysis = read_json(ANALYSIS_RESULT)
    if not analysis:
        blockers.append("canonical analysis-result.json is missing or invalid")
    blockers.extend(acceptance_matrix_blockers())
    return ("READY_FOR_REAL_PARTICIPANTS" if not blockers else "NOT_READY", blockers)


def submission_blockers() -> list[str]:
    blockers: list[str] = []
    analysis = read_json(ANALYSIS_RESULT)
    gate = analysis.get("gate", {}) if isinstance(analysis.get("gate"), dict) else {}
    gates = analysis.get("gates", {}) if isinstance(analysis.get("gates"), dict) else {}
    verified = int(gate.get("verified_participant_count", analysis.get("verified_participant_count", 0)) or 0)
    if "youtube.com" not in hifi_gate_text().lower():
        blockers.append("real YouTube demo URL")
    if verified < 5:
        blockers.append(f"minimum 5 verified participants (current: {verified})")
    recording_checks = gate.get("recording_checks", {})
    if not isinstance(recording_checks, dict) or not recording_checks or any(check.get("status") != "VERIFIED_RECORDING" for check in recording_checks.values() if isinstance(check, dict)):
        blockers.append("required real video recordings")
    for key, label in (("G04", "complete task evidence"), ("G05", "complete questionnaire evidence"), ("G06", "complete interview evidence"), ("G07", "final analysis"), ("G08", "final summative-report readiness")):
        status = (gates.get(key) or {}).get("status") if isinstance(gates.get(key), dict) else None
        if status != "PASS":
            blockers.append(label)
    template_candidates = [ROOT / "final" / "Official-Weekly-Report-Template.docx", ROOT / "final" / "Weekly-Report-Template.docx"]
    if not any(path.is_file() for path in template_candidates):
        blockers.append("official Weekly Report template")
    local_state, local_blockers = validate_local_readiness()
    if local_state != "READY_FOR_REAL_PARTICIPANTS":
        blockers.extend(local_blockers)
    return blockers


def archive_files(relative_paths: list[str], screenshots: list[Path]) -> list[tuple[Path, str]]:
    entries: list[tuple[Path, str]] = []
    for relative in relative_paths:
        entries.append((resolve(relative), "PA4/" + relative.replace("\\", "/")))
    entries.extend((path, f"PA4/evidence/prototype-screenshots/{path.name}") for path in screenshots)
    return entries


def build_working_zip(files: list[tuple[Path, str]]) -> None:
    WORKING_OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(WORKING_OUTPUT, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as archive:
        for path, arcname in sorted(files, key=lambda item: item[1]):
            archive.write(path, arcname=arcname)
    with zipfile.ZipFile(WORKING_OUTPUT, "r") as archive:
        names = set(archive.namelist())
        forbidden = sorted(name for name in names if name.endswith(".zip") or "__pycache__/" in name or "/pdf-renders/" in name)
        if forbidden:
            raise SystemExit("Working ZIP validation failed; forbidden entries:\n- " + "\n- ".join(forbidden))


def build_submission_zip(files: list[Path]) -> None:
    with zipfile.ZipFile(SUBMISSION_OUTPUT, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as archive:
        for path in sorted(files, key=lambda item: item.name):
            archive.write(path, arcname=path.name)
    with zipfile.ZipFile(SUBMISSION_OUTPUT, "r") as archive:
        names = set(archive.namelist())
        expected = {Path(relative).name for relative in SUBMISSION_FILES}
        if names != expected:
            raise SystemExit(f"Submission ZIP validation failed; expected exactly {sorted(expected)}, got {sorted(names)}")


def main() -> int:
    working = require_files(WORKING_FILES)
    submission = require_files(SUBMISSION_FILES)
    screenshots = screenshot_files()
    reject_synthetic_rows()
    validate_templates()
    validate_hifi_link_gate()
    build_working_zip(archive_files(WORKING_FILES, screenshots))
    print(f"PASS: working package {len(working) + len(screenshots)} artifacts -> {WORKING_OUTPUT}")
    local_state, local_blockers = validate_local_readiness()
    print(f"READINESS: {local_state}")
    if local_blockers:
        for blocker in local_blockers:
            print(f"- {blocker}")
    blockers = submission_blockers()
    if blockers:
        print("REFUSED: official package not ready")
        for blocker in blockers:
            print(f"- {blocker}")
        if SUBMISSION_OUTPUT.exists():
            print(f"PRESERVED: existing official package was not replaced -> {SUBMISSION_OUTPUT}")
        return 2
    build_submission_zip(submission)
    print(f"PASS: official package {len(submission)} PDFs -> {SUBMISSION_OUTPUT}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
