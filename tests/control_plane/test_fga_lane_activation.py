from __future__ import annotations

import importlib.util
import json
from pathlib import Path
import unittest

ROOT=Path(__file__).resolve().parents[2]

def read_json(path:str)->dict:
    return json.loads((ROOT/path).read_text(encoding="utf-8"))

def load_lane_state_module():
    path=ROOT/"scripts/ops3_lane_state.py"
    spec=importlib.util.spec_from_file_location("ops3_lane_state",path)
    assert spec and spec.loader
    module=importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module

class FgaLaneActivationTests(unittest.TestCase):
    def test_fga_replaces_terminal_casi_slot_without_erasing_history(self)->None:
        lanes=read_json("operations/LANES.json")
        current=read_json("operations/CURRENT.json")
        self.assertEqual(lanes["persistent_implementation_lanes"],["gpr","cwks","fga"])
        rows={row["id"]:row for row in lanes["lanes"]}
        self.assertIn("fga",rows)
        self.assertEqual(rows["fga"]["execution_state_ref"],"ops3-lane-state/fga")
        self.assertNotIn("casi",lanes["persistent_implementation_lanes"])
        self.assertEqual(current["lanes"]["casi"]["state"],"completed_verified")
        self.assertFalse(current["lanes"]["casi"]["implementation_authority"])
        self.assertEqual(current["completed_programs"]["CASI"]["state"],"completed_verified")
        fga=current["lanes"]["fga"]
        self.assertEqual(fga["state"],"in_progress")
        self.assertEqual(fga["selected_work_item"],"FGA-01")
        self.assertEqual(fga["attempt_id"],"FGA-01-attempt-001")
        self.assertEqual(fga["implementation_branch"],"work/fga-01-garment-semantic-authority")
        self.assertTrue(fga["implementation_authority"])
        cp=read_json(fga["checkpoint_path"])
        self.assertEqual(cp["lane"],"fga")
        self.assertEqual(cp["work_item_id"],"FGA-01")
        self.assertEqual(cp["status"],"in_progress")
        self.assertTrue(cp["implementation_authority"])

    def test_lane_state_writer_accepts_fga_and_rejects_terminal_casi(self)->None:
        lane_state=load_lane_state_module()
        self.assertEqual(lane_state.coordination_branch("fga"),"ops3-lane-state/fga")
        state=lane_state.initial_state("fga",revision=1,selected_work_item="FGA-01",attempt_id="FGA-01-attempt-001")
        started=lane_state.start_execution(state,expected_revision=1,lane="fga",implementation_branch="work/fga-01-garment-semantic-authority",evidence="owner directed first Fashion step after CASI closure")
        self.assertEqual(started["execution_status"],"in_progress")
        with self.assertRaises(lane_state.LaneStateConflict):
            lane_state.coordination_branch("casi")

if __name__=="__main__":
    unittest.main()
