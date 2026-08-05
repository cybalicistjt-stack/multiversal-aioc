from __future__ import annotations

import json
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
TOOL = REPO_ROOT / "tools" / "interaction_enforcement.py"


class InteractionEnforcementTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)

        for directory in (
            "governance/ai",
            "governance/access",
            "governance/object-system",
            ".github/workflows",
        ):
            source = REPO_ROOT / directory
            target = self.root / directory
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copytree(source, target)

        (self.root / "tools").mkdir(parents=True)
        for name in ("continuity_state.py", "interaction_audit.py", "interaction_enforcement.py"):
            shutil.copy2(REPO_ROOT / "tools" / name, self.root / "tools" / name)
        shutil.copy2(
            REPO_ROOT / "MULTIVERSAL_PROJECT_BIBLE_v2.0_CANONICAL_RELEASE.md",
            self.root / "MULTIVERSAL_PROJECT_BIBLE_v2.0_CANONICAL_RELEASE.md",
        )

    def tearDown(self) -> None:
        self.temp.cleanup()

    def run_tool(self, expect: int = 0) -> subprocess.CompletedProcess[str]:
        result = subprocess.run(
            [sys.executable, str(self.root / "tools" / "interaction_enforcement.py"), "validate", "--root", str(self.root)],
            text=True,
            capture_output=True,
            check=False,
        )
        self.assertEqual(expect, result.returncode, result.stdout + result.stderr)
        return result

    def load(self, relative: str) -> tuple[Path, dict]:
        path = self.root / relative
        return path, json.loads(path.read_text())

    def save(self, path: Path, data: dict) -> None:
        path.write_text(json.dumps(data, indent=2) + "\n")

    def test_repository_baseline_validates(self) -> None:
        self.assertIn("PASS", self.run_tool().stdout)

    def test_missing_pattern_coverage_is_rejected(self) -> None:
        path, data = self.load("governance/ai/interaction-system/enforcement/CONTROL_COVERAGE_MATRIX.json")
        data["pattern_coverage"].pop()
        self.save(path, data)
        self.assertIn("pattern coverage mismatch", self.run_tool(expect=1).stderr)

    def test_unknown_authority_is_rejected(self) -> None:
        path, data = self.load("governance/ai/interaction-system/enforcement/CONTROL_COVERAGE_MATRIX.json")
        data["pattern_coverage"][0]["authority_ids"] = ["UNKNOWN"]
        self.save(path, data)
        self.assertIn("unknown authority", self.run_tool(expect=1).stderr)

    def test_inaccessible_deliverable_is_rejected(self) -> None:
        path, data = self.load("governance/ai/interaction-system/enforcement/CONTROL_RECEIPT.examples.json")
        receipt = next(item for item in data["receipts"] if item["control_type"] == "deliverable")
        receipt["details"]["user_accessible_verified"] = False
        self.save(path, data)
        self.assertIn("not owner-accessible", self.run_tool(expect=1).stderr)

    def test_duplicate_notification_send_is_rejected(self) -> None:
        path, data = self.load("governance/ai/interaction-system/enforcement/CONTROL_RECEIPT.examples.json")
        receipt = next(item for item in data["receipts"] if item["control_type"] == "notification")
        receipt["status"] = "send"
        receipt["details"]["decision"] = "send"
        self.save(path, data)
        self.assertIn("unchanged notification was not suppressed", self.run_tool(expect=1).stderr)

    def test_unanswered_decision_request_is_rejected(self) -> None:
        path, data = self.load("governance/ai/interaction-system/enforcement/CONTROL_RECEIPT.examples.json")
        receipt = next(item for item in data["receipts"] if item["control_type"] == "request_alignment")
        receipt["details"]["direct_answer_status"] = "omitted"
        self.save(path, data)
        self.assertIn("immediate question was not answered", self.run_tool(expect=1).stderr)

    def test_evaluation_mapping_gap_is_rejected(self) -> None:
        path, data = self.load("governance/ai/interaction-system/enforcement/EVALUATION_CONTROL_MAP.json")
        data["cases"].pop()
        self.save(path, data)
        self.assertIn("evaluation mapping mismatch", self.run_tool(expect=1).stderr)


if __name__ == "__main__":
    unittest.main()
