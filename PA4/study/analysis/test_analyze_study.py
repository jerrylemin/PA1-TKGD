"""Synthetic-only analysis tests; fixtures never enter PA4 evidence folders."""

from __future__ import annotations

import csv
import subprocess
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from analyze_study import (
    INTERVIEW_FIELDS,
    PARTICIPANT_FIELDS,
    QUESTIONNAIRE_FIELDS,
    TASK_FIELDS,
    analyze,
    verify_recording,
)


class AnalysisTests(unittest.TestCase):
    def setUp(self) -> None:
        self.tmp = tempfile.TemporaryDirectory()
        root = Path(self.tmp.name)
        self.data = root / "data"
        self.recordings = root / "recordings"
        self.output = root / "output"
        self.data.mkdir()
        self.recordings.mkdir()

    def tearDown(self) -> None:
        self.tmp.cleanup()

    def write_csv(self, path: Path, headers: list[str], rows: list[dict[str, str]]) -> None:
        with path.open("w", encoding="utf-8", newline="") as handle:
            writer = csv.DictWriter(handle, fieldnames=headers)
            writer.writeheader()
            writer.writerows(rows)

    def write_templates(self) -> None:
        self.write_csv(self.data / "participants.csv", PARTICIPANT_FIELDS, [])
        self.write_csv(self.data / "task-results.csv", TASK_FIELDS, [])
        self.write_csv(self.data / "questionnaire.csv", QUESTIONNAIRE_FIELDS, [])
        self.write_csv(self.data / "interview-coding.csv", INTERVIEW_FIELDS, [])

    def participant_rows(self, count: int = 5, duplicate_first: bool = False, missing_order: bool = False) -> list[dict[str, str]]:
        rows: list[dict[str, str]] = []
        for number in range(1, count + 1):
            pid = "P01" if duplicate_first and number == count else f"P{number:02d}"
            rows.append({
                "participant_id": pid,
                "date": "2026-08-23",
                "target_profile_match": "yes",
                "device": "desktop",
                "prior_fifa_experience": "low",
                "prior_chess_experience": "low",
                "recording_file": f"{pid}-session.mp4",
                "consent_confirmed": "yes",
                "condition_order": "" if missing_order and number == 1 else ("A_FIFA_FIRST" if number % 2 else "B_CHESS_FIRST"),
            })
        return rows

    def write_participants(self, count: int = 5, duplicate_first: bool = False, missing_order: bool = False, text_recordings: bool = False) -> None:
        rows = self.participant_rows(count, duplicate_first, missing_order)
        self.write_csv(self.data / "participants.csv", PARTICIPANT_FIELDS, rows)
        for row in rows:
            path = self.recordings / row["recording_file"]
            if text_recordings:
                path.write_text("not a media file", encoding="utf-8")

    def write_complete_results(self) -> None:
        task_rows: list[dict[str, str]] = []
        for participant in self.participant_rows():
            pid = participant["participant_id"]
            for product, prefix in (("FIFA", "FIFA-T"), ("CHESS", "CHESS-T")):
                for task_number in range(1, 5):
                    task_rows.append({
                        "participant_id": pid,
                        "product": product,
                        "task_id": f"{prefix}{task_number}",
                        "task_start": "",
                        "task_end": "",
                        "duration_seconds": "42",
                        "success_score": "2",
                        "errors": "0",
                        "wrong_paths": "0",
                        "assistance_count": "0",
                        "hesitation_count": "0",
                        "recovery_outcome": "NOT_NEEDED",
                        "notes": "synthetic test fixture",
                        "recording_timestamp_reference": "00:00",
                    })
        self.write_csv(self.data / "task-results.csv", TASK_FIELDS, task_rows)
        questionnaire_rows: list[dict[str, str]] = []
        for participant in self.participant_rows():
            for product in ("FIFA", "CHESS"):
                for question_number in range(1, 6):
                    questionnaire_rows.append({
                        "participant_id": participant["participant_id"],
                        "product": product,
                        "flow": product,
                        "question_id": f"Q{question_number}",
                        "question_text": "synthetic fixture item",
                        "response_1_to_5": "5",
                        "notes": "synthetic test fixture",
                    })
        self.write_csv(self.data / "questionnaire.csv", QUESTIONNAIRE_FIELDS, questionnaire_rows)
        interview_rows = [{
            "participant_id": participant["participant_id"],
            "product": "BOTH",
            "theme": "overall_feedback",
            "observation": "synthetic test fixture feedback",
            "severity": "low",
            "supporting_timestamp": "00:20",
            "design_implication": "synthetic test fixture only",
        } for participant in self.participant_rows()]
        self.write_csv(self.data / "interview-coding.csv", INTERVIEW_FIELDS, interview_rows)

    def verified_recordings(self):
        return patch("analyze_study.verify_recording", return_value={"status": "VERIFIED_RECORDING", "detail": "synthetic test verifier"})

    def test_t01_zero_participants_is_blocked(self) -> None:
        self.write_templates()
        result = analyze(self.data, self.recordings, self.output)
        self.assertEqual(result["status"], "BLOCKED_PARTICIPANT_COUNT")

    def test_t02_four_complete_participants_are_blocked_by_count(self) -> None:
        self.write_participants(4)
        self.write_complete_results()
        with self.verified_recordings():
            result = analyze(self.data, self.recordings, self.output)
        self.assertEqual(result["status"], "BLOCKED_PARTICIPANT_COUNT")

    def test_t03_five_participants_without_task_rows_are_blocked(self) -> None:
        self.write_participants()
        self.write_csv(self.data / "task-results.csv", TASK_FIELDS, [])
        self.write_csv(self.data / "questionnaire.csv", QUESTIONNAIRE_FIELDS, [])
        self.write_csv(self.data / "interview-coding.csv", INTERVIEW_FIELDS, [])
        with self.verified_recordings():
            result = analyze(self.data, self.recordings, self.output)
        self.assertEqual(result["status"], "BLOCKED_TASK_DATA")

    def test_t04_missing_questionnaire_is_blocked(self) -> None:
        self.write_participants()
        self.write_complete_results()
        self.write_csv(self.data / "questionnaire.csv", QUESTIONNAIRE_FIELDS, [])
        with self.verified_recordings():
            result = analyze(self.data, self.recordings, self.output)
        self.assertEqual(result["status"], "BLOCKED_QUESTIONNAIRE")

    def test_t05_missing_interview_data_is_blocked(self) -> None:
        self.write_participants()
        self.write_complete_results()
        self.write_csv(self.data / "interview-coding.csv", INTERVIEW_FIELDS, [])
        with self.verified_recordings():
            result = analyze(self.data, self.recordings, self.output)
        self.assertEqual(result["status"], "BLOCKED_INTERVIEW_DATA")

    def test_t06_fake_text_mp4_is_not_verified_recording(self) -> None:
        fake = self.recordings / "P01-session.mp4"
        fake.write_text("SYNTHETIC TEST DATA - NOT STUDY EVIDENCE", encoding="utf-8")
        result = verify_recording(fake)
        self.assertEqual(result["status"], "RECORDING_INVALID_MEDIA")

    def test_t13_audio_only_mp4_is_rejected_without_video_stream(self) -> None:
        audio = self.recordings / "P01-audio-only.mp4"
        audio.write_bytes(b"0" * 2048)
        probe = subprocess.CompletedProcess(
            args=["ffprobe"],
            returncode=0,
            stdout='{"streams":[{"codec_type":"audio"}],"format":{"duration":"12"}}',
            stderr="",
        )
        with patch("analyze_study.shutil.which", return_value="ffprobe"), patch("analyze_study.subprocess.run", return_value=probe):
            result = verify_recording(audio)
        self.assertEqual(result["status"], "RECORDING_INVALID_NO_VIDEO_STREAM")

    def test_t14_video_stream_and_positive_duration_are_required_for_verified(self) -> None:
        video = self.recordings / "P01-video.mp4"
        video.write_bytes(b"0" * 2048)
        probe = subprocess.CompletedProcess(
            args=["ffprobe"],
            returncode=0,
            stdout='{"streams":[{"codec_type":"video"}],"format":{"duration":"12"}}',
            stderr="",
        )
        with patch("analyze_study.shutil.which", return_value="ffprobe"), patch("analyze_study.subprocess.run", return_value=probe):
            result = verify_recording(video)
        self.assertEqual(result["status"], "VERIFIED_RECORDING")

    def test_t15_missing_probe_never_becomes_verified(self) -> None:
        present = self.recordings / "P01-no-probe.mp4"
        present.write_bytes(b"0" * 2048)
        with patch("analyze_study.shutil.which", return_value=None):
            result = verify_recording(present)
        self.assertEqual(result["status"], "RECORDING_PRESENT_UNVERIFIED")

    def test_t07_duplicate_participant_id_is_validation_error(self) -> None:
        self.write_participants(5, duplicate_first=True)
        self.write_templates()
        self.write_csv(self.data / "participants.csv", PARTICIPANT_FIELDS, self.participant_rows(5, duplicate_first=True))
        result = analyze(self.data, self.recordings, self.output)
        self.assertEqual(result["status"], "BLOCKED_PARTICIPANT_METADATA")
        self.assertTrue(any("Duplicate participant IDs" in issue for issue in result["issues"]))

    def test_t08_duplicate_task_row_is_validation_error(self) -> None:
        self.write_participants()
        self.write_complete_results()
        with (self.data / "task-results.csv").open("r", encoding="utf-8", newline="") as handle:
            rows = list(csv.DictReader(handle))
        rows.append(dict(rows[0]))
        self.write_csv(self.data / "task-results.csv", TASK_FIELDS, rows)
        with self.verified_recordings():
            result = analyze(self.data, self.recordings, self.output)
        self.assertEqual(result["status"], "BLOCKED_TASK_DATA")
        self.assertTrue(any("duplicate task row" in issue for issue in result["issues"]))

    def test_t09_negative_duration_is_validation_error(self) -> None:
        self.write_participants()
        self.write_complete_results()
        with (self.data / "task-results.csv").open("r", encoding="utf-8", newline="") as handle:
            rows = list(csv.DictReader(handle))
        rows[0]["duration_seconds"] = "-1"
        self.write_csv(self.data / "task-results.csv", TASK_FIELDS, rows)
        with self.verified_recordings():
            result = analyze(self.data, self.recordings, self.output)
        self.assertEqual(result["status"], "BLOCKED_TASK_DATA")
        self.assertTrue(any("negative task duration" in issue for issue in result["issues"]))

    def test_t10_invalid_success_score_is_validation_error(self) -> None:
        self.write_participants()
        self.write_complete_results()
        with (self.data / "task-results.csv").open("r", encoding="utf-8", newline="") as handle:
            rows = list(csv.DictReader(handle))
        rows[0]["success_score"] = "3"
        self.write_csv(self.data / "task-results.csv", TASK_FIELDS, rows)
        with self.verified_recordings():
            result = analyze(self.data, self.recordings, self.output)
        self.assertEqual(result["status"], "BLOCKED_TASK_DATA")
        self.assertTrue(any("success_score must be 0, 1, or 2" in issue for issue in result["issues"]))

    def test_t11_missing_assigned_order_is_validation_error(self) -> None:
        self.write_participants(missing_order=True)
        self.write_csv(self.data / "task-results.csv", TASK_FIELDS, [])
        self.write_csv(self.data / "questionnaire.csv", QUESTIONNAIRE_FIELDS, [])
        self.write_csv(self.data / "interview-coding.csv", INTERVIEW_FIELDS, [])
        result = analyze(self.data, self.recordings, self.output)
        self.assertEqual(result["status"], "BLOCKED_PARTICIPANT_METADATA")
        self.assertTrue(any("condition_order" in issue for issue in result["issues"]))

    def test_t12_fully_complete_synthetic_fixture_passes_only_in_test_fixture(self) -> None:
        """A complete synthetic fixture may exercise the pipeline, never final evidence."""

        self.write_participants()
        self.write_complete_results()
        with self.verified_recordings():
            result = analyze(self.data, self.recordings, self.output)
        self.assertEqual(result["status"], "PASS")
        self.assertEqual(result["gates"]["G08"]["status"], "PASS")


if __name__ == "__main__":
    unittest.main()
