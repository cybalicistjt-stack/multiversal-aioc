from __future__ import annotations

import json
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
TOOL = REPO_ROOT / "tools" / "continuity_state.py"


class ContinuityStateTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        shutil.copytree(REPO_ROOT / "governance" / "ai", self.root / "governance" / "ai")
        shutil.copytree(REPO_ROOT / ".github", self.root / ".github")
        (self.root / "tools").mkdir(parents=True)
        shutil.copy2(TOOL, self.root / "tools" / "continuity_state.py")

    def tearDown(self) -> None:
        self.temp.cleanup()

    def run_tool(self, *args: str, expect: int = 0) -> subprocess.CompletedProcess[str]:
        result = subprocess.run(
            [sys.executable, str(self.root / "tools" / "continuity_state.py"), "--root", str(self.root), *args],
            text=True,
            capture_output=True,
            check=False,
        )
        self.assertEqual(expect, result.returncode, result.stdout + result.stderr)
        return result

    def test_repository_baseline_validates(self) -> None:
        result = self.run_tool("validate")
        self.assertIn("PASS", result.stdout)

    def test_wrong_revision_is_rejected_without_mutation(self) -> None:
        checkpoint = self.root / "governance/ai/work-state/MV-CONT-001-attempt-001.json"
        before = checkpoint.read_bytes()
        result = self.run_tool(
            "update", "--attempt-id", "MV-CONT-001-attempt-001",
            "--expected-revision", "999", "--status", "in_progress", expect=1,
        )
        self.assertIn("revision conflict", result.stderr)
        self.assertEqual(before, checkpoint.read_bytes())

    def test_duplicate_attempt_is_rejected(self) -> None:
        result = self.run_tool(
            "start", "--work-item-id", "MV-CONT-001",
            "--attempt-id", "MV-CONT-001-attempt-001", "--track", "test",
            "--repository", "cybalicistjt-stack/multiversal-aioc", "--branch", "test",
            "--objective", "test", "--active-substep", "test", "--next-action", "test",
            expect=1,
        )
        self.assertIn("attempt already exists", result.stderr)

    def test_false_completion_is_rejected_without_mutation(self) -> None:
        checkpoint = self.root / "governance/ai/work-state/MV-CONT-001-attempt-001.json"
        before = checkpoint.read_bytes()
        result = self.run_tool(
            "update", "--attempt-id", "MV-CONT-001-attempt-001",
            "--expected-revision", "1", "--status", "completed_verified",
            "--active-substep", "-", "--completed-at", "2026-08-05T22:10:00Z",
            expect=1,
        )
        self.assertIn("completion evidence missing", result.stderr)
        self.assertEqual(before, checkpoint.read_bytes())

    def test_checkpoint_update_refreshes_pointer_and_status(self) -> None:
        self.run_tool(
            "update", "--attempt-id", "MV-CONT-001-attempt-001",
            "--expected-revision", "1", "--status", "in_progress",
            "--active-substep", "Test atomic continuation.",
            "--next-action", "Resume the exact test substep.",
        )
        pointer = json.loads((self.root / "governance/ai/runtime/CURRENT_WORK_POINTER.json").read_text())
        status = json.loads((self.root / "governance/ai/runtime/CURRENT_IMPLEMENTATION_STATUS.json").read_text())
        self.assertEqual("in_progress", pointer["active_attempts"][0]["status"])
        self.assertEqual("in_progress", status["primary"]["status"])
        self.run_tool("validate")


if __name__ == "__main__":
    unittest.main()
