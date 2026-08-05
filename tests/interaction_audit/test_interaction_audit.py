from __future__ import annotations

import json
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
TOOL = REPO_ROOT / "tools" / "interaction_audit.py"


class InteractionAuditTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        analysis = self.root / "governance/ai/interaction-system/analysis"
        evaluation = self.root / "governance/ai/interaction-system/evaluation"
        analysis.parent.mkdir(parents=True, exist_ok=True)
        shutil.copytree(REPO_ROOT / "governance/ai/interaction-system/analysis", analysis)
        shutil.copytree(REPO_ROOT / "governance/ai/interaction-system/evaluation", evaluation)
        (self.root / "tools").mkdir(parents=True)
        shutil.copy2(TOOL, self.root / "tools" / "interaction_audit.py")

    def tearDown(self) -> None:
        self.temp.cleanup()

    def run_tool(self, expect: int = 0) -> subprocess.CompletedProcess[str]:
        result = subprocess.run(
            [sys.executable, str(self.root / "tools" / "interaction_audit.py"), "validate", "--root", str(self.root)],
            text=True,
            capture_output=True,
            check=False,
        )
        self.assertEqual(expect, result.returncode, result.stdout + result.stderr)
        return result

    def test_repository_baseline_validates(self) -> None:
        self.assertIn("PASS", self.run_tool().stdout)

    def test_forbidden_raw_field_is_rejected(self) -> None:
        path = self.root / "governance/ai/interaction-system/analysis/PRIVACY_REVIEW.json"
        data = json.loads(path.read_text())
        data["raw_text"] = "private transcript material"
        path.write_text(json.dumps(data, indent=2) + "\n")
        self.assertIn("forbidden key", self.run_tool(expect=1).stderr)

    def test_unknown_pattern_reference_is_rejected(self) -> None:
        path = self.root / "governance/ai/interaction-system/analysis/REDACTED_EPISODE_INDEX.jsonl"
        records = [json.loads(line) for line in path.read_text().splitlines() if line.strip()]
        records[0]["pattern_ids"] = ["MV-FRIC-UNKNOWN-999"]
        path.write_text("\n".join(json.dumps(item) for item in records) + "\n")
        self.assertIn("unknown pattern", self.run_tool(expect=1).stderr)

    def test_pattern_episode_count_mismatch_is_rejected(self) -> None:
        path = self.root / "governance/ai/interaction-system/analysis/FAILURE_FRICTION_TAXONOMY.json"
        data = json.loads(path.read_text())
        data["patterns"][0]["episode_count"] += 1
        path.write_text(json.dumps(data, indent=2) + "\n")
        self.assertIn("episode count mismatch", self.run_tool(expect=1).stderr)

    def test_privacy_overlap_match_is_rejected(self) -> None:
        path = self.root / "governance/ai/interaction-system/analysis/PRIVACY_REVIEW.json"
        data = json.loads(path.read_text())
        data["checks"]["exact_contiguous_token_overlap"]["matches_found"] = 1
        path.write_text(json.dumps(data, indent=2) + "\n")
        self.assertIn("privacy overlap matches found", self.run_tool(expect=1).stderr)


if __name__ == "__main__":
    unittest.main()
