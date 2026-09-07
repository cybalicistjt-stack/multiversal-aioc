import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


class Vti08ContinueTerminationBoundaryTests(unittest.TestCase):
    def test_continue_boundary_is_explicit_for_active_tranche(self):
        text = (ROOT / "governance/ai/work-state/VTI-08-RED-UNLOCK-BOUNDARY.md").read_text(encoding="utf-8")
        self.assertIn("Continue", text)
        self.assertIn("terminal closeout", text)
        self.assertIn("strict-successor selection", text)
        self.assertIn("Unrelated historical/profile scans are blocked", text)
        self.assertIn("No unchanged rerun", text)
        self.assertIn("no completion response", text)


if __name__ == "__main__":
    unittest.main()
