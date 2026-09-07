import json
import unittest
from pathlib import Path

ROOT=Path(__file__).resolve().parents[2]
def load_json(path): return json.loads((ROOT/path).read_text(encoding="utf-8"))

class Vti08RedUnlockTests(unittest.TestCase):
    def test_matching_red_is_sealed_and_only_bounded_production_is_unlocked(self):
        cp=load_json("governance/ai/work-state/VTI-08-attempt-001.json")
        backlog=load_json("governance/application-planning/virtual-tabletop-interoperability/VTI_PROGRAM_BACKLOG.json")
        pointer=load_json("governance/ai/runtime/CURRENT_WORK_POINTER.json")
        registry=load_json("governance/ai/runtime/ACTIVE_AUTHORITY_REGISTRY.json")
        index=load_json("governance/ai/runtime/ROADMAP_INDEX.json")
        runtime=load_json("governance/repository-health/RUNTIME_STATE_LIFECYCLE_REGISTRY.json")
        red=cp["validation"]["acceptance_red"]
        self.assertEqual(red["head_sha"],"420dced5ba3daf982d80a5b6cf141d2bdb4376bd")
        self.assertEqual(red["run_id"],34066821411)
        self.assertEqual(red["repository_health_job"],101576932682)
        self.assertEqual(red["linux_job"],101576947365)
        self.assertEqual(red["windows_job"],101576947375)
        self.assertEqual(red["deterministic_compare_job"],101576996334)
        self.assertEqual(red["deterministic_receipt_sha256"],"45e107c94e4cf57ae3e360cf1e89b043c8dc79d60f95362afed9a52458fb0bc2")
        self.assertTrue(red["matching_red_observed"])
        self.assertEqual(red["failure_stage"],"vti08-invariants")
        auth=registry["vti_08_authority"]
        self.assertTrue(auth["matching_red_observed"])
        if cp["status"] == "completed_verified":
            self.assertTrue(cp["authority_retired"])
            self.assertFalse(cp["production_mutation_authorized"])
            self.assertFalse(auth["production_mutation_authorized"])
            self.assertFalse(auth["adapter_sdk_capability_manifest_reference_vtt_authorized"])
            self.assertEqual(pointer["active_attempt"]["work_item_id"], "VTI-09")
        else:
            self.assertTrue(cp["production_mutation_authorized"])
            self.assertTrue(backlog["active_contract"]["production_mutation_authorized"])
            self.assertTrue(pointer["bounded_authority"]["production_mutation_authorized"])
            self.assertTrue(index["current"]["production_mutation_authorized"])
            self.assertTrue(runtime["active_work"]["production_mutation_authorized"])
            self.assertTrue(auth["production_mutation_authorized"])
            self.assertTrue(auth["adapter_sdk_capability_manifest_reference_vtt_authorized"])
        for key in ("provider_selection_authorized","provider_specific_schema_authorized","credential_or_external_account_mutation_authorized","live_external_or_canonical_mutation_authorized","durable_persistence_or_migration_authorized","provider_activation_authorized","tester_distribution_authorized","release_or_deployment_authorized","vti09_plus_authorized","sgc01_plus_authorized"):
            self.assertFalse(auth[key])

if __name__=="__main__": unittest.main()
