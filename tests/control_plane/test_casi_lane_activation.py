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

class CasiLaneActivationTests(unittest.TestCase):
    def test_casi_replaces_terminal_oarc_slot_without_erasing_oarc_history(self) -> None:
        lanes=read_json("operations/LANES.json")
        current=read_json("operations/CURRENT.json")
        self.assertEqual(lanes["persistent_implementation_lanes"],["gpr","cwks","casi"])
        rows={row["id"]:row for row in lanes["lanes"]}
        self.assertIn("casi",rows)
        self.assertEqual(rows["casi"]["execution_state_ref"],"ops3-lane-state/casi")
        self.assertIn("oarc",rows)
        self.assertNotIn("oarc",lanes["persistent_implementation_lanes"])
        self.assertEqual(current["lanes"]["oarc"]["state"],"completed_verified")
        self.assertFalse(current["lanes"]["oarc"]["implementation_authority"])
        self.assertEqual(current["completed_programs"]["OARC"]["state"],"completed_verified")
        casi=current["lanes"]["casi"]
        self.assertEqual(casi["state"],"in_progress")
        self.assertEqual(casi["selected_work_item"],"CASI-01")
        self.assertEqual(casi["attempt_id"],"CASI-01-attempt-001")
        self.assertEqual(casi["implementation_branch"],"work/casi-01-semantic-parameter-transport")
        self.assertTrue(casi["implementation_authority"])
        cp=read_json(casi["checkpoint_path"])
        self.assertEqual(cp["lane"],"casi")
        self.assertEqual(cp["work_item_id"],"CASI-01")
        self.assertEqual(cp["status"],"in_progress")
        self.assertTrue(cp["implementation_authority"])

    def test_lane_state_writer_accepts_casi_and_rejects_terminal_oarc(self) -> None:
        lane_state=load_lane_state_module()
        self.assertEqual(lane_state.coordination_branch("casi"),"ops3-lane-state/casi")
        state=lane_state.initial_state("casi",revision=1,selected_work_item="CASI-01",attempt_id="CASI-01-attempt-001")
        started=lane_state.start_execution(state,expected_revision=1,lane="casi",implementation_branch="work/casi-01-semantic-parameter-transport",evidence="owner Continue after CAS design closure")
        self.assertEqual(started["execution_status"],"in_progress")
        with self.assertRaises(lane_state.LaneStateConflict):
            lane_state.coordination_branch("oarc")

if __name__ == "__main__":
    unittest.main()
