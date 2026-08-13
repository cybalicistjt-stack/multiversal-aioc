from __future__ import annotations

import json
import re
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
TOOL = REPO_ROOT / "tools/correction_regression.py"
EXAMPLE = REPO_ROOT / "governance/ai/interaction-system/corrections/CORRECTION_INTAKE.examples.json"


class CorrectionRegressionTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        shutil.copytree(REPO_ROOT / "governance", self.root / "governance")
        shutil.copytree(REPO_ROOT / ".github", self.root / ".github")
        (self.root / "tools").mkdir()
        shutil.copy2(TOOL, self.root / "tools/correction_regression.py")
        shutil.copytree(REPO_ROOT / "tools/correction_regression_lib", self.root / "tools/correction_regression_lib")

    def tearDown(self) -> None:
        self.temp.cleanup()

    def run_tool(self, *args: str, expect: int = 0):
        result = subprocess.run(
            [sys.executable, str(self.root / "tools/correction_regression.py"), "--root", str(self.root), *args],
            text=True, capture_output=True, check=False,
        )
        self.assertEqual(expect, result.returncode, result.stdout + result.stderr)
        return result

    def write_input(self, mutate=None) -> Path:
        data = json.loads(EXAMPLE.read_text())["intakes"][0]
        if mutate:
            mutate(data)
        path = self.root / "input.json"
        path.write_text(json.dumps(data, indent=2) + "\n")
        return path

    def ledger(self):
        return json.loads((self.root / "governance/ai/interaction-system/corrections/CORRECTION_REGRESSION_LEDGER.json").read_text())

    def promoted(self):
        return json.loads((self.root / "governance/ai/interaction-system/evaluation/PROMOTED_EVALUATION_CASES.json").read_text())

    def captured_candidate_id(self, result) -> str:
        match = re.search(r"candidate=(\S+)", result.stdout)
        self.assertIsNotNone(match, result.stdout)
        return match.group(1)

    def candidate(self, candidate_id: str):
        return next(item for item in self.ledger()["candidates"] if item["candidate_id"] == candidate_id)

    def test_repository_baseline_validates(self):
        self.assertIn("PASS", self.run_tool("validate").stdout)

    def test_capture_is_deterministic_and_idempotent(self):
        before = self.ledger()
        input_path = self.write_input()
        first = self.run_tool("capture", "--input", str(input_path))
        second = self.run_tool("capture", "--input", str(input_path))
        self.assertIn("created correction=", first.stdout)
        self.assertIn("existing correction=", second.stdout)
        candidate_id = self.captured_candidate_id(first)
        ledger = self.ledger()
        self.assertEqual(len(before["corrections"]) + 1, len(ledger["corrections"]))
        self.assertEqual(len(before["candidates"]) + 1, len(ledger["candidates"]))
        self.assertEqual("proposed", self.candidate(candidate_id)["status"])
        self.run_tool("validate")

    def test_capture_rejects_raw_transcript_field_without_mutation(self):
        before = self.ledger()
        path = self.write_input(lambda data: data.update(raw_transcript="private content"))
        result = self.run_tool("capture", "--input", str(path), expect=1)
        self.assertIn("fields mismatch", result.stderr)
        self.assertEqual(before, self.ledger())

    def test_capture_rejects_unknown_pattern_without_mutation(self):
        before = self.ledger()
        path = self.write_input(lambda data: data.__setitem__("pattern_ids", ["MV-SUCC-NOTREAL-999"]))
        result = self.run_tool("capture", "--input", str(path), expect=1)
        self.assertIn("unknown pattern ID", result.stderr)
        self.assertEqual(before, self.ledger())

    def test_review_requires_owner_authority(self):
        path = self.write_input()
        capture = self.run_tool("capture", "--input", str(path))
        candidate_id = self.captured_candidate_id(capture)
        result = self.run_tool(
            "review", "--candidate-id", candidate_id, "--decision", "approved",
            "--reviewer", "other-reviewer", "--evidence", "review evidence", expect=1,
        )
        self.assertIn("only the owner", result.stderr)
        self.assertEqual("proposed", self.candidate(candidate_id)["status"])

    def test_promotion_requires_approved_candidate(self):
        path = self.write_input()
        capture = self.run_tool("capture", "--input", str(path))
        candidate_id = self.captured_candidate_id(capture)
        promoted_before = self.promoted()
        result = self.run_tool(
            "promote", "--candidate-id", candidate_id, "--case-id", "MV-EVAL-016",
            "--evidence", "promotion evidence", expect=1,
        )
        self.assertIn("must be owner-approved", result.stderr)
        self.assertEqual(promoted_before, self.promoted())

    def test_owner_review_and_promotion_materialize_extension_case(self):
        path = self.write_input()
        capture = self.run_tool("capture", "--input", str(path))
        candidate_id = self.captured_candidate_id(capture)
        self.run_tool(
            "review", "--candidate-id", candidate_id, "--decision", "approved",
            "--reviewer", "john-brandon-turner", "--evidence", "owner decision ref",
            "--decided-at", "2026-08-05T23:30:00Z",
        )
        self.run_tool(
            "promote", "--candidate-id", candidate_id, "--case-id", "MV-EVAL-016",
            "--evidence", "promotion PR ref", "--promoted-at", "2026-08-05T23:31:00Z",
        )
        self.assertEqual("promoted", self.candidate(candidate_id)["status"])
        promoted = self.promoted()
        new_case = next(item for item in promoted["cases"] if item["case_id"] == "MV-EVAL-016")
        self.assertEqual(candidate_id, new_case["source_candidate_id"])
        mapping = json.loads((self.root / "governance/ai/interaction-system/corrections/EVALUATION_CONTROL_EXTENSION.json").read_text())
        new_map = next(item for item in mapping["cases"] if item["case_id"] == "MV-EVAL-016")
        self.assertIn("C-CORRECTION-REGRESSION-INTAKE", new_map["control_ids"])
        self.run_tool("validate")


if __name__ == "__main__":
    unittest.main()
