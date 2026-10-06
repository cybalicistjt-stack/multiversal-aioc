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

class MtlcLaneActivationTests(unittest.TestCase):
    def test_mtlc_owns_terminal_fashion_slot_and_selects_mtlc02_after_mtlc01(self)->None:
        lanes=read_json("operations/LANES.json")
        current=read_json("operations/CURRENT.json")
        self.assertEqual(lanes["persistent_implementation_lanes"],["gpr","cwks","mtlc"])
        rows={row["id"]:row for row in lanes["lanes"]}
        self.assertIn("mtlc",rows)
        self.assertEqual(rows["mtlc"]["execution_state_ref"],"ops3-lane-state/mtlc")
        self.assertNotIn("fga",lanes["persistent_implementation_lanes"])
        self.assertEqual(current["lanes"]["fga"]["state"],"completed_verified")
        self.assertFalse(current["lanes"]["fga"]["implementation_authority"])
        self.assertEqual(current["completed_programs"]["FGA"]["state"],"completed_verified")
        self.assertEqual(current["completed_programs"]["FDE"]["state"],"completed_verified")

        mtlc=current["lanes"]["mtlc"]
        self.assertEqual(mtlc["state"],"selected_not_started")
        self.assertEqual(mtlc["selected_work_item"],"MTLC-02")
        self.assertEqual(mtlc["attempt_id"],"MTLC-02-attempt-001")
        self.assertIsNone(mtlc["implementation_branch"])
        self.assertFalse(mtlc["implementation_authority"])
        cp=read_json(mtlc["checkpoint_path"])
        self.assertEqual(cp["lane"],"mtlc")
        self.assertEqual(cp["work_item_id"],"MTLC-02")
        self.assertEqual(cp["status"],"selected_not_started")
        self.assertFalse(cp["implementation_authority"])

        prior=read_json("operations/work-items/MTLC-01.json")
        self.assertEqual(prior["status"],"completed_verified")
        self.assertEqual(prior["completion_evidence"]["authority_matrix_row_count"],70)
        self.assertEqual(prior["completion_evidence"]["successor"],"MTLC-02")

    def test_lane_state_writer_accepts_mtlc_and_rejects_terminal_fga(self)->None:
        lane_state=load_lane_state_module()
        self.assertEqual(lane_state.coordination_branch("mtlc"),"ops3-lane-state/mtlc")
        state=lane_state.initial_state("mtlc",revision=1,selected_work_item="MTLC-02",attempt_id="MTLC-02-attempt-001")
        started=lane_state.start_execution(state,expected_revision=1,lane="mtlc",implementation_branch="work/mtlc-02-private-table-onboarding",evidence="future owner Continue")
        self.assertEqual(started["execution_status"],"in_progress")
        with self.assertRaises(lane_state.LaneStateConflict):
            lane_state.coordination_branch("fga")

if __name__=="__main__":
    unittest.main()
