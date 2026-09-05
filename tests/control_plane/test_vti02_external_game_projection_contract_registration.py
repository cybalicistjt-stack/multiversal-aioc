import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def load_json(path):
    return json.loads((ROOT / path).read_text(encoding="utf-8"))


def load_text(path):
    return (ROOT / path).read_text(encoding="utf-8")


class Vti02ExternalGameProjectionContractRegistrationTests(unittest.TestCase):
    def test_vti02_completed_lifecycle_and_vti03_successor_are_consistent(self):
        baseline = "027fad06d0bac3a20d56f0cc2a674581662cd1b9"
        merge = "01aa25d60ad71e5ed318b9680f859c6927a90541"
        branch = "integration/vti-02-multiversal-external-game-projection-contract"
        vti03_branch = "integration/vti-03-stable-identity-versioning-synchronization"
        checkpoint = load_json("governance/ai/work-state/VTI-02-attempt-001.json")
        successor = load_json("governance/ai/work-state/VTI-03-attempt-001.json")
        backlog = load_json("governance/application-planning/virtual-tabletop-interoperability/VTI_PROGRAM_BACKLOG.json")
        pointer = load_json("governance/ai/runtime/CURRENT_WORK_POINTER.json")
        registry = load_json("governance/ai/runtime/ACTIVE_AUTHORITY_REGISTRY.json")
        index = load_json("governance/ai/runtime/ROADMAP_INDEX.json")
        runtime = load_json("governance/repository-health/RUNTIME_STATE_LIFECYCLE_REGISTRY.json")
        program = load_text("governance/application-planning/virtual-tabletop-interoperability/VTI_VIRTUAL_TABLETOP_INTEROPERABILITY_PROGRAM.md")

        self.assertEqual(checkpoint["work_item_id"], "VTI-02")
        self.assertEqual(checkpoint["status"], "completed_verified")
        self.assertEqual(checkpoint["application_baseline_sha"], baseline)
        self.assertEqual(checkpoint["implementation_branch"], branch)
        self.assertEqual(checkpoint["application_pr"], 416)
        self.assertEqual(checkpoint["application_merge_sha"], merge)
        self.assertFalse(checkpoint["implementation_authority"])
        self.assertTrue(checkpoint["authority_retired"])
        self.assertFalse(checkpoint["branch_creation_authorized"])
        self.assertFalse(checkpoint["acceptance_package_authorized"])
        self.assertFalse(checkpoint["production_mutation_authorized"])
        self.assertTrue(checkpoint["completed"])

        red = checkpoint["validation"]["acceptance_red"]
        green = checkpoint["validation"]["final_green"]
        self.assertEqual(red["head_sha"], "db4a4c436cb6eeb011afd9614568fb68f070c785")
        self.assertEqual(red["run_id"], 33989074845)
        self.assertTrue(red["matching_red_observed"])
        self.assertEqual(red["deterministic_receipt_sha256"], "7005e6b204a3b24a1e8a6e8e8ac2f80a295540afaf9fc9b3bbfb733a5f39ccc7")
        self.assertEqual(green["head_sha"], "e24f1e045d6dd5c6f332ebc4392acf2ba9f6e281")
        self.assertEqual(green["run_id"], 33989626004)
        self.assertEqual(green["deterministic_receipt_sha256"], "a66e9f4557713aa2807c960cb3c018a222c4316cadeb4afbfd8e5be4199ff7bd")
        self.assertEqual(green["historical_profile_fanout"], 0)

        vti02 = next(item for item in backlog["tranches"] if item["id"] == "VTI-02")
        self.assertEqual(vti02["status"], "completed_verified")
        self.assertFalse(vti02["implementation_authority"])
        self.assertEqual(vti02["application_merge_sha"], merge)
        self.assertEqual(backlog["completed_through"], "VTI-02")
        self.assertEqual(backlog["current_item"], "VTI-03")

        self.assertEqual(successor["work_item_id"], "VTI-03")
        self.assertIn(successor["status"], {"selected_not_started", "in_progress"})
        self.assertEqual(successor["application_baseline_sha"], merge)

        self.assertEqual(pointer["active_attempt"]["work_item_id"], "VTI-03")
        self.assertEqual(pointer["active_attempt"]["status"], successor["status"])
        self.assertEqual(index["current"]["work_item_id"], "VTI-03")
        self.assertEqual(index["current"]["status"], successor["status"])
        self.assertEqual(runtime["active_work"]["work_item"], "VTI-03")
        self.assertEqual(runtime["active_work"]["state"], successor["status"])
        self.assertEqual(runtime["application_repository"]["canonical_main"], merge)

        vti02_authority = registry["vti_02_authority"]
        self.assertTrue(vti02_authority["retired"])
        self.assertFalse(vti02_authority["implementation_authority"])
        self.assertEqual(vti02_authority["application_merge_sha"], merge)
        vti03_authority = registry["vti_03_authority"]

        if successor["status"] == "selected_not_started":
            self.assertIsNone(successor["implementation_branch"])
            self.assertFalse(successor["implementation_authority"])
            self.assertFalse(successor["branch_creation_authorized"])
            self.assertFalse(successor["acceptance_package_authorized"])
            self.assertFalse(successor["production_mutation_authorized"])
            self.assertTrue(vti03_authority["selected_not_started"])
            self.assertFalse(vti03_authority["implementation_authority"])
            self.assertIsNone(vti03_authority["implementation_branch"])
            self.assertFalse(pointer["bounded_authority"]["vti_implementation"])
        else:
            self.assertEqual(successor["implementation_branch"], vti03_branch)
            self.assertTrue(successor["implementation_authority"])
            self.assertTrue(successor["branch_creation_authorized"])
            self.assertTrue(successor["acceptance_package_authorized"])
            self.assertFalse(vti03_authority["selected_not_started"])
            self.assertTrue(vti03_authority["implementation_authority"])
            self.assertEqual(vti03_authority["implementation_branch"], vti03_branch)
            self.assertTrue(pointer["bounded_authority"]["vti_implementation"])
            self.assertTrue(pointer["bounded_authority"]["acceptance_package_authorized"])
            self.assertEqual(pointer["bounded_authority"]["production_mutation_authorized"], successor["production_mutation_authorized"])

        for phrase in (
            "VTI-02 — Multiversal External Game Projection Contract",
            "COMPLETED_VERIFIED",
            "Character, Creature, Item, Action, Condition, Encounter, Scene, Vehicle and RuleReference",
            "present`, `redacted` or `unsupported",
            "VTI-03 — Stable Identity, Versioning & Synchronization",
            "Platform selection remains evidence-driven",
        ):
            self.assertIn(phrase, program)

    def test_vti02_completed_scope_keeps_deferred_authorities_closed(self):
        checkpoint = load_json("governance/ai/work-state/VTI-02-attempt-001.json")
        completed = checkpoint["completed_contract"]
        self.assertTrue(completed["provider_neutral"])
        self.assertEqual(completed["availability_states"], ["present", "redacted", "unsupported"])
        self.assertTrue(completed["deterministic_ordering"])
        self.assertTrue(completed["deterministic_receipts"])
        self.assertTrue(completed["redacted_values_stripped"])
        self.assertTrue(completed["unsupported_values_not_manufactured"])

        authority = load_json("governance/ai/runtime/ACTIVE_AUTHORITY_REGISTRY.json")["vti_02_authority"]
        for key in (
            "vendor_selection_authorized",
            "provider_specific_schema_authorized",
            "external_account_mutation_authorized",
            "credential_use_authorized",
            "adapter_implementation_authorized",
            "external_sync_mutation_authorized",
            "canonical_game_state_mutation_authorized",
            "hidden_information_bypass_authorized",
            "external_object_mapping_authorized",
            "versioning_authorized",
            "conflict_resolution_authorized",
            "rules_action_bridge_authorized",
            "durable_vti_persistence_authorized",
            "new_migration_authorized",
            "provider_activation_authorized",
            "tester_distribution_authorized",
            "release_or_deployment_authorized",
            "vti03_plus_authorized",
            "sgc01_plus_authorized",
        ):
            self.assertFalse(authority[key])


if __name__ == "__main__":
    unittest.main()
