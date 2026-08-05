from __future__ import annotations

import json
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
TOOL = REPO_ROOT / "tools/interaction_pilot.py"


class InteractionPilotTests(unittest.TestCase):
    def run_tool(self, root: Path, *args: str, expect: int = 0):
        result = subprocess.run(
            [sys.executable, str(root / "tools/interaction_pilot.py"), "--root", str(root), *args],
            text=True,
            capture_output=True,
            check=False,
        )
        self.assertEqual(expect, result.returncode, result.stdout + result.stderr)
        return result

    def fixture(self) -> tuple[tempfile.TemporaryDirectory, Path]:
        temp = tempfile.TemporaryDirectory()
        root = Path(temp.name)
        shutil.copytree(REPO_ROOT / "governance/ai", root / "governance/ai")
        shutil.copytree(REPO_ROOT / "governance/development-bible", root / "governance/development-bible")
        (root / "tools").mkdir(parents=True)
        for name in ("continuity_state.py", "correction_regression.py", "interaction_enforcement.py", "interaction_pilot.py"):
            shutil.copy2(REPO_ROOT / "tools" / name, root / "tools" / name)
        shutil.copytree(REPO_ROOT / "tools/correction_regression_lib", root / "tools/correction_regression_lib")
        return temp, root

    def test_repository_pilot_validates(self):
        result = self.run_tool(REPO_ROOT, "validate")
        self.assertIn("PASS", result.stdout)
        scorecard = json.loads((REPO_ROOT / "governance/ai/interaction-system/pilot/OPERATIONAL_PILOT_SCORECARD.json").read_text())
        self.assertEqual(17, scorecard["metrics"]["scenario_passed"])
        self.assertEqual(0, scorecard["metrics"]["scenario_failed"])
        self.assertIsNone(scorecard["metrics"]["live_longitudinal_owner_intervention_reduction"])

    def test_run_reproduces_the_committed_scorecard(self):
        temp, root = self.fixture()
        try:
            source = json.loads((root / "governance/ai/interaction-system/pilot/OPERATIONAL_PILOT_SCORECARD.json").read_text())
            result = self.run_tool(root, "run", "--generated-at", source["generated_at"])
            self.assertIn("17/17 PASS", result.stdout)
            regenerated = json.loads((root / "governance/ai/interaction-system/pilot/OPERATIONAL_PILOT_SCORECARD.json").read_text())
            self.assertEqual(source, regenerated)
            self.run_tool(root, "validate")
        finally:
            temp.cleanup()

    def test_stale_runtime_projection_is_rejected(self):
        temp, root = self.fixture()
        try:
            path = root / "governance/ai/runtime/INTERACTION_OPERATIONAL_SCORECARD.json"
            data = json.loads(path.read_text())
            data["scenario_passed"] = 16
            path.write_text(json.dumps(data, indent=2) + "\n")
            result = self.run_tool(root, "validate", expect=1)
            self.assertIn("runtime scorecard projection is stale", result.stderr)
        finally:
            temp.cleanup()

    def test_tampered_pilot_result_is_rejected(self):
        temp, root = self.fixture()
        try:
            path = root / "governance/ai/interaction-system/pilot/OPERATIONAL_PILOT_SCORECARD.json"
            data = json.loads(path.read_text())
            data["results"][0]["status"] = "fail"
            path.write_text(json.dumps(data, indent=2) + "\n")
            result = self.run_tool(root, "validate", expect=1)
            self.assertIn("stored pilot scorecard differs", result.stderr)
        finally:
            temp.cleanup()


if __name__ == "__main__":
    unittest.main()
