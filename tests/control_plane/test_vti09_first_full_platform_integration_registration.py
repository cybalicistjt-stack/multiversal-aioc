import json
import unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
def load_json(p): return json.loads((ROOT/p).read_text(encoding="utf-8"))
class Vti09LifecycleTests(unittest.TestCase):
    def test_vti09_terminal_evidence_and_vti10_selection(self):
        cp=load_json("governance/ai/work-state/VTI-09-attempt-001.json")
        nxt=load_json("governance/ai/work-state/VTI-10-attempt-001.json")
        b=load_json("governance/application-planning/virtual-tabletop-interoperability/VTI_PROGRAM_BACKLOG.json")
        p=load_json("governance/ai/runtime/CURRENT_WORK_POINTER.json")
        a=load_json("governance/ai/runtime/ACTIVE_AUTHORITY_REGISTRY.json")
        r=load_json("governance/repository-health/RUNTIME_STATE_LIFECYCLE_REGISTRY.json")
        self.assertEqual(cp["status"],"completed_verified")
        self.assertTrue(cp["authority_retired"])
        self.assertFalse(cp["implementation_authority"])
        self.assertFalse(cp["production_mutation_authorized"])
        self.assertEqual(cp["application_merge_sha"],"9bed9b190b1d78bbbce9e208c2daa792c9109466")
        self.assertEqual(cp["validation"]["final_green"]["head_sha"],"60646de3d4f05888a9ea32a6bd1b8937b6c4a591")
        self.assertEqual(cp["validation"]["final_green"]["deterministic_receipt_sha256"],"58b65117b86f4844472f997e9e13d497e7cf47def10f8e602627d5b4c39d6f40")
        self.assertEqual(nxt["status"],"selected_not_started")
        self.assertIsNone(nxt["implementation_branch"])
        self.assertFalse(nxt["implementation_authority"])
        self.assertEqual(nxt["application_baseline_sha"],"9bed9b190b1d78bbbce9e208c2daa792c9109466")
        self.assertEqual(b["completed_through"],"VTI-09")
        self.assertEqual(b["current_item"],"VTI-10")
        self.assertEqual(p["active_attempt"]["work_item_id"],"VTI-10")
        self.assertEqual(r["active_work"]["work_item"],"VTI-10")
        self.assertTrue(a["vti_09_authority"]["retired"])
        self.assertFalse(a["vti_09_authority"]["implementation_authority"])
        self.assertTrue(a["vti_10_authority"]["selected_not_started"])
        self.assertFalse(a["vti_10_authority"]["implementation_authority"])
if __name__=="__main__": unittest.main()
