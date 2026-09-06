import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]

def load_json(path):
    return json.loads((ROOT / path).read_text(encoding="utf-8"))

class Vti07TerminalCloseoutTests(unittest.TestCase):
    def test_vti07_terminal_evidence_and_vti08_successor_lifecycle(self):
        cp=load_json("governance/ai/work-state/VTI-07-attempt-001.json")
        nxt=load_json("governance/ai/work-state/VTI-08-attempt-001.json")
        backlog=load_json("governance/application-planning/virtual-tabletop-interoperability/VTI_PROGRAM_BACKLOG.json")
        pointer=load_json("governance/ai/runtime/CURRENT_WORK_POINTER.json")
        registry=load_json("governance/ai/runtime/ACTIVE_AUTHORITY_REGISTRY.json")
        index=load_json("governance/ai/runtime/ROADMAP_INDEX.json")
        runtime=load_json("governance/repository-health/RUNTIME_STATE_LIFECYCLE_REGISTRY.json")
        self.assertEqual(cp["status"],"completed_verified")
        self.assertTrue(cp["authority_retired"]); self.assertTrue(cp["completed"])
        self.assertEqual(cp["application_pr"],436); self.assertEqual(cp["application_merge_sha"],"692da4f4792426b9c62f6be14db60fc63eb09d6b")
        green=cp["validation"]["final_green"]
        self.assertEqual(green["head_sha"],"63e3194792375bb3abf8955f2448fbea282e859f"); self.assertEqual(green["run_id"],34064468595)
        self.assertEqual(green["repository_health_job"],101570690097); self.assertEqual(green["linux_job"],101570706227); self.assertEqual(green["windows_job"],101570706229); self.assertEqual(green["deterministic_compare_job"],101570780675)
        self.assertEqual(green["deterministic_receipt_sha256"],"8e2b1cab0247a40829f155a360f4a0576d3b3ca625713cd5d5ac7847fabb9ac4"); self.assertEqual(green["historical_profile_fanout"],0)
        self.assertEqual(cp["convergence_control"]["application_feature_repair_cycles"],0)
        self.assertEqual(cp["convergence_control"]["validation_contract_repair_cycles"],2)
        self.assertTrue(cp["convergence_control"]["diagnostic_mode"])

        self.assertEqual(nxt["application_baseline_sha"],"692da4f4792426b9c62f6be14db60fc63eb09d6b")
        self.assertIn(nxt["status"],{"selected_not_started","in_progress","ready_for_review","completed_verified"})
        if nxt["status"] == "selected_not_started":
            self.assertIsNone(nxt["implementation_branch"])
            self.assertFalse(nxt["implementation_authority"])
            self.assertFalse(nxt["acceptance_package_authorized"])
            self.assertFalse(nxt["production_mutation_authorized"])
        elif nxt["status"] in {"in_progress","ready_for_review"}:
            self.assertEqual(nxt["implementation_branch"],"integration/vti-08-adapter-sdk-capability-manifest-reference-vtt")
            self.assertTrue(nxt["implementation_authority"])
            self.assertTrue(nxt["acceptance_package_authorized"])
        else:
            self.assertFalse(nxt["implementation_authority"])
            self.assertFalse(nxt["acceptance_package_authorized"])
            self.assertFalse(nxt["production_mutation_authorized"])

        self.assertEqual(backlog["completed_through"],"VTI-07")
        if nxt["status"] != "completed_verified":
            self.assertEqual(backlog["current_item"],"VTI-08")
            self.assertEqual(pointer["active_attempt"]["work_item_id"],"VTI-08")
            self.assertEqual(index["current"]["work_item_id"],"VTI-08")
            self.assertEqual(runtime["active_work"]["work_item"],"VTI-08")
        else:
            self.assertIn(pointer["active_attempt"]["work_item_id"],{"VTI-08","VTI-09"})
        self.assertEqual(runtime["application_repository"]["canonical_main"],"692da4f4792426b9c62f6be14db60fc63eb09d6b")

        old=registry["vti_07_authority"]; self.assertTrue(old["retired"]); self.assertTrue(old["matching_red_observed"])
        for key in ("implementation_authority","branch_creation_authorized","acceptance_package_authorized","production_mutation_authorized","permissions_hidden_gm_authority_authorized"):
            self.assertFalse(old[key])
        new=registry["vti_08_authority"]
        if nxt["status"] == "selected_not_started":
            self.assertTrue(new["selected_not_started"])
            self.assertFalse(new["implementation_authority"])
            self.assertFalse(new["branch_creation_authorized"])
            self.assertFalse(new["acceptance_package_authorized"])
        elif nxt["status"] in {"in_progress","ready_for_review"}:
            self.assertFalse(new["selected_not_started"])
            self.assertTrue(new["implementation_authority"])
            self.assertTrue(new["branch_creation_authorized"])
            self.assertTrue(new["acceptance_package_authorized"])
        else:
            self.assertTrue(new["retired"])
            self.assertFalse(new["implementation_authority"])
        for key in ("adapter_sdk_capability_manifest_reference_vtt_authorized","provider_selection_authorized","vti09_plus_authorized","sgc01_plus_authorized"):
            if nxt["validation"]["acceptance_red"] is None:
                self.assertFalse(new[key])

if __name__ == "__main__": unittest.main()
