from __future__ import annotations

import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SCRIPTS = ROOT / "scripts"
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))

import execution_transaction_preflight as preflight


class ExecutionRoutingGateTests(unittest.TestCase):
    def test_execution_routing_controls_exist_before_ari_resume(self) -> None:
        self.assertTrue((SCRIPTS / "execution_state_reconciler.py").exists(), "missing execution state reconciler")
        self.assertTrue((SCRIPTS / "execution_context_guard.py").exists(), "missing hermetic context guard")
        self.assertTrue((SCRIPTS / "generate_focused_validation_profile.py").exists(), "missing focused validation generator")
        self.assertTrue(hasattr(preflight, "decide_execution_route"), "missing immediate RED routing decision")


if __name__ == "__main__":
    unittest.main()
