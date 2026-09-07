import json
import unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
def load_json(path): return json.loads((ROOT/path).read_text(encoding="utf-8"))
class Vti08TerminalCloseoutTests(unittest.TestCase):
    def test_vti08_terminal_evidence_and_vti09_successor_lifecycle(self):
        cp=load_json("governance/ai/work-state/VTI-08-attempt-001.json")
        nxt=load_json("governance/ai/work-state/VTI-09-attempt-001.json")
        backlog=load_json("governance/application-planning/virtual-tabletop-interoperability/VTI_PROGRAM_BACKLOG.json")
        pointer=load_json("governance/ai/runtime/CURRENT_WORK_POINTER.json")
        registry=load_json("governance/ai/runtime/ACTIVE_AUTHORITY_REGISTRY.json")
        runtime=load_json("governance/repository-health/RUNTIME_STATE_LIFECYCLE_REGISTRY.json")
        self.assertEqual(cp["status"],"completed_verified"); self.assertTrue(cp["completed"]); self.assertTrue(cp["authority_retired"])
        self.assertEqual(cp["application_pr"],437); self.assertEqual(cp["application_merge_sha"],"69bc17bf5999e5cd704d7ec4d8aaa7b168db740c")
        green=cp["validation"]["final_green"]
        self.assertEqual(green["head_sha"],"2cb7e2797e7a5c8b251ea4ac7e3980e124ff9d7e"); self.assertEqual(green["run_id"],34138095971)
        self.assertEqual(green["deterministic_receipt_sha256"],"c85ce8390efeac8ecc3442e0b1b435f1ea86dc3433220ff0fbb8ada1ca0bbddb"); self.assertEqual(green["historical_profile_fanout"],0)
        self.assertIn(nxt["status"],{"selected_not_started","in_progress","ready_for_review","completed_verified"}); self.assertEqual(nxt["application_baseline_sha"],"69bc17bf5999e5cd704d7ec4d8aaa7b168db740c")
        self.assertEqual(backlog["completed_through"],"VTI-08") if nxt["status"]!="completed_verified" else None
        old=registry["vti_08_authority"]; self.assertTrue(old["retired"]); self.assertTrue(old["matching_red_observed"])
        if nxt["status"]=="selected_not_started":
            self.assertIsNone(nxt["implementation_branch"]); self.assertFalse(nxt["implementation_authority"])
        elif nxt["status"] in {"in_progress","ready_for_review"}:
            self.assertEqual(nxt["implementation_branch"],"integration/vti-09-foundry-vtt-first-full-platform-integration"); self.assertTrue(nxt["implementation_authority"])
            self.assertEqual(pointer["active_attempt"]["work_item_id"],"VTI-09"); self.assertEqual(runtime["active_work"]["work_item"],"VTI-09")
if __name__=="__main__": unittest.main()
