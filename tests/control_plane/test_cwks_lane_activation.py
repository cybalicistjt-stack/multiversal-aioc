from __future__ import annotations

import importlib.util
import json
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[2]


def read_json(path: str) -> dict:
    return json.loads((ROOT / path).read_text(encoding="utf-8"))


def load_lane_state_module():
    path = ROOT / "scripts/ops3_lane_state.py"
    spec = importlib.util.spec_from_file_location("ops3_lane_state", path)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class CwksLaneActivationTests(unittest.TestCase):
    def test_cwks_replaces_terminal_mrcs_persistent_slot_without_erasing_history(self) -> None:
        lanes = read_json("operations/LANES.json")
        current = read_json("operations/CURRENT.json")

        self.assertEqual(lanes["persistent_implementation_lanes"], ["gpr", "cwks", "oarc"])
        lane_rows = {row["id"]: row for row in lanes["lanes"]}
        self.assertIn("cwks", lane_rows)
        self.assertEqual(lane_rows["cwks"]["execution_state_ref"], "ops3-lane-state/cwks")
        self.assertIn("mrcs", lane_rows)
        self.assertNotIn("mrcs", lanes["persistent_implementation_lanes"])

        self.assertEqual(current["lanes"]["mrcs"]["state"], "completed_verified")
        self.assertFalse(current["lanes"]["mrcs"]["implementation_authority"])
        self.assertEqual(current["completed_programs"]["MRCS"]["state"], "completed_verified")

        cwks = current["lanes"]["cwks"]
        self.assertEqual(cwks["state"], "in_progress")
        self.assertEqual(cwks["selected_work_item"], "CWKS-01")
        self.assertEqual(cwks["attempt_id"], "CWKS-01-attempt-001")
        self.assertEqual(cwks["implementation_branch"], "work/cwks-01-document-schema")
        self.assertTrue(cwks["implementation_authority"])
        self.assertEqual(cwks["execution_state_ref"], "ops3-lane-state/cwks")

        checkpoint = read_json(cwks["checkpoint_path"])
        self.assertEqual(checkpoint["lane"], "cwks")
        self.assertEqual(checkpoint["work_item_id"], "CWKS-01")
        self.assertEqual(checkpoint["status"], "in_progress")
        self.assertTrue(checkpoint["implementation_authority"])
        self.assertEqual(checkpoint["implementation_branch"], "work/cwks-01-document-schema")

    def test_lane_state_writer_accepts_cwks_and_rejects_retired_mrcs(self) -> None:
        lane_state = load_lane_state_module()
        self.assertEqual(lane_state.coordination_branch("cwks"), "ops3-lane-state/cwks")
        state = lane_state.initial_state(
            "cwks",
            revision=1,
            selected_work_item="CWKS-01",
            attempt_id="CWKS-01-attempt-001",
        )
        started = lane_state.start_execution(
            state,
            expected_revision=1,
            lane="cwks",
            implementation_branch="work/cwks-01-document-schema",
            evidence="owner approved, execute",
        )
        self.assertEqual(started["execution_status"], "in_progress")

        with self.assertRaises(lane_state.LaneStateConflict):
            lane_state.coordination_branch("mrcs")


if __name__ == "__main__":
    unittest.main()
