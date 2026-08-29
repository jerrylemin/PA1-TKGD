"""Synthetic-only checks for the shared DOCX/PDF report data model."""

from __future__ import annotations

import json
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from build_pa4_reports import ANALYSIS_RESULT, build_summative_report_data  # noqa: E402


class SummativeReportModelTests(unittest.TestCase):
    def test_real_empty_state_is_dynamic_and_blocked(self) -> None:
        data = build_summative_report_data(ANALYSIS_RESULT)
        self.assertEqual(data["verified_count"], 0)
        self.assertEqual(data["analysis_status"], "BLOCKED_PARTICIPANT_COUNT")
        self.assertIn("No verified participant sessions", data["participant_state"])
        self.assertIn("header-only", data["task_state"])

    def test_isolated_complete_fixture_changes_shared_model(self) -> None:
        gates = {key: {"name": key, "status": "PASS"} for key in ("G01", "G02", "G03", "G04", "G05", "G06", "G07", "G08")}
        fixture = {
            "status": "PASS",
            "gate": {"participant_rows": 5, "verified_participant_count": 5},
            "gates": gates,
            "task_row_count": 40,
            "questionnaire_row_count": 50,
            "interview_row_count": 5,
        }
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "analysis-result.json"
            path.write_text(json.dumps(fixture), encoding="utf-8")
            data = build_summative_report_data(path)
        self.assertEqual(data["verified_count"], 5)
        self.assertEqual(data["task_state"], "40 task rows")
        self.assertEqual(data["questionnaire_state"], "50 questionnaire rows")
        self.assertEqual(data["interview_state"], "5 interview/feedback rows")
        self.assertEqual(data["analysis_status"], "PASS")

    def test_return_to_real_state_does_not_retain_fixture(self) -> None:
        data = build_summative_report_data(ANALYSIS_RESULT)
        self.assertEqual(data["verified_count"], 0)
        self.assertNotIn("40 task rows", data["task_state"])


if __name__ == "__main__":
    unittest.main()
