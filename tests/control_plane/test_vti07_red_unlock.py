import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def load_json(path):
    return json.loads((ROOT / path).read_text(encoding="utf-8"))


class Vti07RedUnlockTests(unittest.TestCase):
    def test_matching_application_red_is_sealed_and_production_authority_is_open(self):
        head = "5cb646cd4ea49e4ef82cc13d695c6450336c73ff"
        run = 34064038245
        receipt = "3c405551b32804277945d4047a99786a2cf5a2dd6d513e0852aae48e8ea94f71"
        checkpoint = load_json("governance/ai/work-state/VTI-07-attempt-001.json")
        backlog = load_json("governance/application-planning/virtual-tabletop-interoperability/VTI_PROGRAM_BACKLOG.json")
        pointer = load_json("governance/ai/runtime/CURRENT_WORK_POINTER.json")
        registry = load_json("governance/ai/runtime/ACTIVE_AUTHORITY_REGISTRY.json")
        index = load_json("governance/ai/runtime/ROADMAP_INDEX.json")
        runtime = load_json("governance/repository-health/RUNTIME_STATE_LIFECYCLE_REGISTRY.json")

        red = checkpoint["validation"]["acceptance_red"]
        self.assertEqual(red["head_sha"], head)
        self.assertEqual(red["run_id"], run)
        self.assertEqual(red["repository_health_job"], 101569552203)
        self.assertEqual(red["linux_job"], 101569566705)
        self.assertEqual(red["windows_job"], 101569566565)
        self.assertEqual(red["deterministic_compare_job"], 101569630517)
        self.assertEqual(red["deterministic_receipt_sha256"], receipt)
        self.assertTrue(red["matching_red_observed"])
        self.assertEqual(red["failure_stage"], "vti07-invariants")
        self.assertEqual(red["failure_reason"], "production contract intentionally absent")

        self.assertTrue(checkpoint["production_mutation_authorized"])
        self.assertTrue(checkpoint["implementation_authority"])
        self.assertEqual(checkpoint["status"], "in_progress")
        self.assertTrue(backlog["active_contract"]["production_mutation_authorized"])
        self.assertTrue(backlog["active_contract"]["matching_red_observed"])
        self.assertTrue(pointer["bounded_authority"]["production_mutation_authorized"])
        self.assertTrue(pointer["bounded_authority"]["matching_red_observed"])
        self.assertTrue(index["current"]["production_mutation_authorized"])
        self.assertTrue(index["current"]["matching_red_observed"])
        self.assertTrue(runtime["active_work"]["production_mutation_authorized"])
        self.assertTrue(runtime["active_work"]["matching_red_observed"])

        authority = registry["vti_07_authority"]
        self.assertTrue(authority["production_mutation_authorized"])
        self.assertTrue(authority["permissions_hidden_gm_authority_authorized"])
        self.assertTrue(authority["matching_red_observed"])
        for key in (
            "provider_specific_schema_authorized",
            "credential_or_external_account_mutation_authorized",
            "adapter_implementation_authorized",
            "live_external_or_canonical_mutation_authorized",
            "durable_persistence_or_migration_authorized",
            "provider_activation_authorized",
            "tester_distribution_authorized",
            "release_or_deployment_authorized",
            "vti08_plus_authorized",
            "sgc01_plus_authorized",
        ):
            self.assertFalse(authority[key])


if __name__ == "__main__":
    unittest.main()
