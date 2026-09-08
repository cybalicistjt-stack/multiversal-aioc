import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]

def load_json(path):
    return json.loads((ROOT / path).read_text(encoding="utf-8"))

class Vti10RedUnlockTests(unittest.TestCase):
    def test_matching_red_is_sealed_before_production_authority(self):
        cp = load_json("governance/ai/work-state/VTI-10-attempt-001.json")
        pointer = load_json("governance/ai/runtime/CURRENT_WORK_POINTER.json")
        backlog = load_json("governance/application-planning/virtual-tabletop-interoperability/VTI_PROGRAM_BACKLOG.json")
        index = load_json("governance/ai/runtime/ROADMAP_INDEX.json")
        runtime = load_json("governance/repository-health/RUNTIME_STATE_LIFECYCLE_REGISTRY.json")
        authority = load_json("governance/ai/runtime/ACTIVE_AUTHORITY_REGISTRY.json")

        red = cp["validation"]["acceptance_red"]
        self.assertIsNotNone(red)
        self.assertEqual(red["head_sha"], "8f6b95ed0479069c4a3904f25c2f5a17f00de016")
        self.assertEqual(red["run_id"], 34171468253)
        self.assertEqual(red["repository_health_job"], 101892440021)
        self.assertEqual(red["linux_job"], 101892476523)
        self.assertEqual(red["windows_job"], 101892476478)
        self.assertEqual(red["deterministic_compare_job"], 101892589252)
        self.assertEqual(red["deterministic_receipt_sha256"], "24c4c44bdeafd3acdba878552f3547ad2a5389586dc92383a754862fc78d007d")
        self.assertEqual(red["failure_stage"], "vti10-invariants")
        self.assertEqual(red["failure_reason"], "production contract intentionally absent")
        self.assertTrue(red["matching_red_observed"])
        self.assertTrue(red["raw_evidence_confirmed"])
        self.assertEqual(red["historical_profile_fanout"], 0)

        if cp["status"] == "completed_verified":
            self.assertTrue(cp["authority_retired"])
            self.assertFalse(cp["production_mutation_authorized"])
            self.assertFalse(authority["vti_10_authority"]["production_mutation_authorized"])
            self.assertTrue(authority["vti_10_authority"]["matching_red_observed"])
        else:
            self.assertTrue(cp["production_mutation_authorized"])
            self.assertTrue(pointer["bounded_authority"]["production_mutation_authorized"])
            self.assertTrue(backlog["active_contract"]["production_mutation_authorized"])
            self.assertTrue(index["current"]["production_mutation_authorized"])
            self.assertTrue(runtime["active_work"]["production_mutation_authorized"])
            self.assertTrue(authority["vti_10_authority"]["production_mutation_authorized"])
            self.assertTrue(pointer["bounded_authority"]["matching_red_observed"])
            self.assertTrue(backlog["active_contract"]["matching_red_observed"])
            self.assertTrue(index["current"]["matching_red_observed"])
            self.assertTrue(runtime["active_work"]["matching_red_observed"])

        for key in ("provider_activation_authorized", "tester_distribution_authorized", "release_or_deployment_authorized", "vti11_plus_authorized", "sgc01_plus_authorized"):
            self.assertFalse(cp["authority_boundary"][key])

if __name__ == "__main__":
    unittest.main()
