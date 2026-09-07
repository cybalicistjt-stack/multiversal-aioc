import json
import unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
def load_json(path): return json.loads((ROOT/path).read_text(encoding="utf-8"))
class Vti09GovernedStartTests(unittest.TestCase):
    def test_foundry_selection_and_red_gated_authority(self):
        cp=load_json("governance/ai/work-state/VTI-09-attempt-001.json")
        backlog=load_json("governance/application-planning/virtual-tabletop-interoperability/VTI_PROGRAM_BACKLOG.json")
        pointer=load_json("governance/ai/runtime/CURRENT_WORK_POINTER.json")
        registry=load_json("governance/ai/runtime/ACTIVE_AUTHORITY_REGISTRY.json")
        index=load_json("governance/ai/runtime/ROADMAP_INDEX.json")
        runtime=load_json("governance/repository-health/RUNTIME_STATE_LIFECYCLE_REGISTRY.json")
        self.assertEqual(cp["status"],"in_progress"); self.assertEqual(cp["application_baseline_sha"],"69bc17bf5999e5cd704d7ec4d8aaa7b168db740c")
        self.assertEqual(cp["implementation_branch"],"integration/vti-09-foundry-vtt-first-full-platform-integration")
        self.assertTrue(cp["implementation_authority"]); self.assertTrue(cp["branch_creation_authorized"]); self.assertTrue(cp["acceptance_package_authorized"])
        self.assertEqual(cp["selected_platform"]["platform_id"],"foundry-vtt"); self.assertEqual(cp["selected_platform"]["integration_level"],3); self.assertFalse(cp["selected_platform"]["provider_activation_authorized"])
        self.assertEqual(backlog["current_item"],"VTI-09"); self.assertEqual(backlog["active_contract"]["selected_platform"],"foundry-vtt")
        self.assertEqual(pointer["active_attempt"]["work_item_id"],"VTI-09"); self.assertTrue(pointer["bounded_authority"]["vti_implementation"])
        self.assertEqual(index["current"]["selected_platform"],"foundry-vtt"); self.assertEqual(runtime["active_work"]["selected_platform"],"foundry-vtt")
        red=cp["validation"]["acceptance_red"]
        red_open=red is not None and red.get("matching_red_observed") is True
        self.assertEqual(cp["production_mutation_authorized"],red_open)
        self.assertEqual(pointer["bounded_authority"]["production_mutation_authorized"],red_open)
        self.assertEqual(backlog["active_contract"]["production_mutation_authorized"],red_open)
        self.assertEqual(index["current"]["production_mutation_authorized"],red_open)
        self.assertEqual(runtime["active_work"]["production_mutation_authorized"],red_open)
        auth=registry["vti_09_authority"]; self.assertTrue(auth["in_progress"]); self.assertTrue(auth["provider_selection_authorized"]); self.assertEqual(auth["selected_platform"],"foundry-vtt"); self.assertEqual(auth["production_mutation_authorized"],red_open)
        for key in ("credential_use_authorized","external_account_use_authorized","provider_network_access_authorized","live_external_mutation_authorized","canonical_mutation_authorized","durable_persistence_authorized","new_migration_authorized","provider_activation_authorized","tester_distribution_authorized","package_publication_authorized","release_or_deployment_authorized","vti10_plus_authorized","sgc01_plus_authorized"):
            self.assertFalse(auth[key], key)
if __name__=="__main__": unittest.main()
