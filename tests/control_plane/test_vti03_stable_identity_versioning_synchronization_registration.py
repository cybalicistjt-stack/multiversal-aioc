import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def load_json(path):
    return json.loads((ROOT / path).read_text(encoding="utf-8"))


class Vti03StableIdentityVersioningSynchronizationRegistrationTests(unittest.TestCase):
    def test_vti03_is_selected_only_from_exact_vti02_merge(self):
        baseline = "01aa25d60ad71e5ed318b9680f859c6927a90541"
        checkpoint = load_json("governance/ai/work-state/VTI-03-attempt-001.json")
        backlog = load_json("governance/application-planning/virtual-tabletop-interoperability/VTI_PROGRAM_BACKLOG.json")
        pointer = load_json("governance/ai/runtime/CURRENT_WORK_POINTER.json")
        registry = load_json("governance/ai/runtime/ACTIVE_AUTHORITY_REGISTRY.json")
        index = load_json("governance/ai/runtime/ROADMAP_INDEX.json")
        runtime = load_json("governance/repository-health/RUNTIME_STATE_LIFECYCLE_REGISTRY.json")

        self.assertEqual(checkpoint["work_item_id"], "VTI-03")
        self.assertEqual(checkpoint["status"], "selected_not_started")
        self.assertEqual(checkpoint["application_baseline_sha"], baseline)
        self.assertIsNone(checkpoint["implementation_branch"])
        self.assertFalse(checkpoint["implementation_authority"])
        self.assertFalse(checkpoint["branch_creation_authorized"])
        self.assertFalse(checkpoint["acceptance_package_authorized"])
        self.assertFalse(checkpoint["production_mutation_authorized"])

        self.assertEqual(backlog["completed_through"], "VTI-02")
        self.assertEqual(backlog["current_item"], "VTI-03")
        self.assertEqual(backlog["active_contract"]["status"], "selected_not_started")
        self.assertFalse(backlog["active_contract"]["implementation_authority"])

        self.assertEqual(pointer["active_attempt"]["work_item_id"], "VTI-03")
        self.assertEqual(pointer["active_attempt"]["status"], "selected_not_started")
        self.assertFalse(pointer["bounded_authority"]["vti_implementation"])
        self.assertEqual(index["current"]["work_item_id"], "VTI-03")
        self.assertEqual(runtime["active_work"]["work_item"], "VTI-03")
        self.assertEqual(runtime["application_repository"]["canonical_main"], baseline)

        authority = registry["vti_03_authority"]
        self.assertTrue(authority["selected_not_started"])
        for key in (
            "implementation_authority",
            "branch_creation_authorized",
            "acceptance_package_authorized",
            "production_mutation_authorized",
            "external_object_mapping_authorized",
            "versioning_authorized",
            "external_sync_mutation_authorized",
            "conflict_resolution_authorized",
            "reconnect_authorized",
            "deduplication_authorized",
            "tombstone_authorized",
            "rules_action_bridge_authorized",
            "provider_specific_schema_authorized",
            "credential_use_authorized",
            "external_account_mutation_authorized",
            "adapter_implementation_authorized",
            "canonical_game_state_mutation_authorized",
            "hidden_information_bypass_authorized",
            "durable_vti_persistence_authorized",
            "new_migration_authorized",
            "provider_activation_authorized",
            "tester_distribution_authorized",
            "release_or_deployment_authorized",
            "vti04_plus_authorized",
            "sgc01_plus_authorized",
        ):
            self.assertFalse(authority[key])


if __name__ == "__main__":
    unittest.main()
