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

    def primary_entry(self) -> tuple[Path, dict, dict]:
        pointer_path = self.root / "governance/ai/runtime/CURRENT_WORK_POINTER.json"
        pointer = json.loads(pointer_path.read_text())
        attempt_id = pointer["primary_attempt_id"]
        entry = next(item for item in pointer["active_attempts"] if item["attempt_id"] == attempt_id)
        checkpoint_path = self.root / entry["checkpoint_path"]
        return pointer_path, pointer, entry

    def make_primary_unfinished(self, *, strip_completion_evidence: bool = False) -> tuple[Path, int, str]:
        pointer_path, pointer, entry = self.primary_entry()
        checkpoint_path = self.root / entry["checkpoint_path"]
        checkpoint = json.loads(checkpoint_path.read_text())
        checkpoint["status"] = "in_progress"
        checkpoint["completed_at"] = None
        checkpoint["active_substep"] = "Synthetic unfinished regression fixture."
        checkpoint["next_action"] = "Exercise the requested checkpoint transition."
        checkpoint["updated_at"] = "2026-08-05T22:40:00+00:00"
        checkpoint["roadmap_projection_pending"] = True
        if strip_completion_evidence:
            tokens = (checkpoint["work_item_id"], checkpoint["attempt_id"])
            checkpoint["evidence"] = [
                item for item in checkpoint["evidence"]
                if not any(token in item["value"] for token in tokens)
            ]
        checkpoint_path.write_text(json.dumps(checkpoint, indent=2) + "\n")

        pointer["updated_at"] = checkpoint["updated_at"]
        entry["status"] = checkpoint["status"]
        entry["updated_at"] = checkpoint["updated_at"]
        entry["roadmap_projection_pending"] = True
        pointer_path.write_text(json.dumps(pointer, indent=2) + "\n")
        self.run_tool("refresh-status")
        return checkpoint_path, checkpoint["revision"], checkpoint["attempt_id"]

    def test_repository_baseline_validates(self) -> None:
        result = self.run_tool("validate")
        self.assertIn("PASS", result.stdout)

    def test_wrong_revision_is_rejected_without_mutation(self) -> None:
        _, _, entry = self.primary_entry()
        checkpoint = self.root / entry["checkpoint_path"]
        before = checkpoint.read_bytes()
        result = self.run_tool(
            "update", "--attempt-id", entry["attempt_id"],
            "--expected-revision", "999", "--status", "in_progress", expect=1,
        )
        self.assertIn("revision conflict", result.stderr)
        self.assertEqual(before, checkpoint.read_bytes())

    def test_duplicate_attempt_is_rejected(self) -> None:
        _, _, entry = self.primary_entry()
        result = self.run_tool(
            "start", "--work-item-id", entry["work_item_id"],
            "--attempt-id", entry["attempt_id"], "--track", "test",
            "--repository", "cybalicistjt-stack/multiversal-aioc", "--branch", "test",
            "--objective", "test", "--active-substep", "test", "--next-action", "test",
            expect=1,
        )
        self.assertIn("attempt already exists", result.stderr)

    def test_false_completion_is_rejected_without_mutation(self) -> None:
        checkpoint, revision, attempt_id = self.make_primary_unfinished(strip_completion_evidence=True)
        before = checkpoint.read_bytes()
        result = self.run_tool(
            "update", "--attempt-id", attempt_id,
            "--expected-revision", str(revision), "--status", "completed_verified",
            "--active-substep", "-", "--completed-at", "2026-08-05T22:41:00Z",
            expect=1,
        )
        self.assertIn("completion evidence missing", result.stderr)
        self.assertEqual(before, checkpoint.read_bytes())

    def test_checkpoint_update_refreshes_pointer_and_status(self) -> None:
        _, revision, attempt_id = self.make_primary_unfinished()
        self.run_tool(
            "update", "--attempt-id", attempt_id,
            "--expected-revision", str(revision), "--status", "in_progress",
            "--active-substep", "Test atomic continuation.",
            "--next-action", "Resume the exact test substep.",
        )
        pointer = json.loads((self.root / "governance/ai/runtime/CURRENT_WORK_POINTER.json").read_text())
        status = json.loads((self.root / "governance/ai/runtime/CURRENT_IMPLEMENTATION_STATUS.json").read_text())
        entry = next(item for item in pointer["active_attempts"] if item["attempt_id"] == attempt_id)
        self.assertEqual("in_progress", entry["status"])
        self.assertEqual(attempt_id, status["primary"]["attempt_id"])
        self.assertEqual("in_progress", status["primary"]["status"])
        self.run_tool("validate")


if __name__ == "__main__":
    unittest.main()
