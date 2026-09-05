import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]

def load_json(path):
    return json.loads((ROOT / path).read_text(encoding="utf-8"))

def load_text(path):
    return (ROOT / path).read_text(encoding="utf-8")

class Vti04RulesActionRollBridgeRegistrationTests(unittest.TestCase):
    def test_vti04_completed_lifecycle_and_vti05_selection_are_consistent(self):
        merge = "295424982135337de80cccfac072764ab35183cc"
        checkpoint = load_json("governance/ai/work-state/VTI-04-attempt-001.json")
        successor = load_json("governance/ai/work-state/VTI-05-attempt-001.json")
        backlog = load_json("governance/application-planning/virtual-tabletop-interoperability/VTI_PROGRAM_BACKLOG.json")
        pointer = load_json("governance/ai/runtime/CURRENT_WORK_POINTER.json")
        registry = load_json("governance/ai/runtime/ACTIVE_AUTHORITY_REGISTRY.json")
        index = load_json("governance/ai/runtime/ROADMAP_INDEX.json")
        runtime = load_json("governance/repository-health/RUNTIME_STATE_LIFECYCLE_REGISTRY.json")
        program = load_text("governance/application-planning/virtual-tabletop-interoperability/VTI_VIRTUAL_TABLETOP_INTEROPERABILITY_PROGRAM.md")

        self.assertEqual(checkpoint["status"], "completed_verified")
        self.assertEqual(checkpoint["application_pr"], 418)
        self.assertEqual(checkpoint["application_merge_sha"], merge)
        self.assertTrue(checkpoint["authority_retired"])
        self.assertFalse(checkpoint["implementation_authority"])
        self.assertFalse(checkpoint["branch_creation_authorized"])
        self.assertFalse(checkpoint["acceptance_package_authorized"])
        self.assertFalse(checkpoint["production_mutation_authorized"])
        self.assertTrue(checkpoint["completed"])

        red = checkpoint["validation"]["acceptance_red"]
        green = checkpoint["validation"]["final_green"]
        self.assertEqual(red["head_sha"], "c9a3cc09aa9ce6ce2ca55c35df7ba7032ffb7126")
        self.assertEqual(red["run_id"], 33993535896)
        self.assertTrue(red["matching_red_observed"])
        self.assertEqual(red["deterministic_receipt_sha256"], "ee79438a64ccaccabe8acd2953df5f911d1e0ee8b92352952b3026ede1d0e028")
        self.assertEqual(green["head_sha"], "8806fce4a0143281942dd2d68a23301c70501999")
        self.assertEqual(green["run_id"], 33994055604)
        self.assertEqual(green["deterministic_receipt_sha256"], "766e06c3f2de74e4cbee599fa56c3d88e4a49fe98481b7f65f70d30a5970050c")
        self.assertEqual(green["historical_profile_fanout"], 0)

        self.assertEqual(backlog["completed_through"], "VTI-04")
        self.assertEqual(backlog["current_item"], "VTI-05")
        self.assertIn(successor["status"], {"selected_not_started", "in_progress"})
        self.assertEqual(successor["application_baseline_sha"], merge)
        if successor["status"] == "selected_not_started":
            self.assertIsNone(successor["implementation_branch"])
            self.assertFalse(successor["implementation_authority"])
            self.assertFalse(successor["branch_creation_authorized"])
            self.assertFalse(successor["acceptance_package_authorized"])
            self.assertFalse(successor["production_mutation_authorized"])
        else:
            self.assertEqual(successor["implementation_branch"], branch)
            self.assertTrue(successor["implementation_authority"])
            self.assertTrue(successor["branch_creation_authorized"])
            self.assertTrue(successor["acceptance_package_authorized"])

        self.assertEqual(pointer["active_attempt"]["work_item_id"], "VTI-05")
        self.assertEqual(pointer["active_attempt"]["status"], successor["status"])
        self.assertEqual(index["current"]["work_item_id"], "VTI-05")
        self.assertEqual(index["current"]["status"], successor["status"])
        self.assertEqual(runtime["active_work"]["work_item"], "VTI-05")
        self.assertEqual(runtime["active_work"]["state"], successor["status"])
        self.assertEqual(runtime["application_repository"]["canonical_main"], merge)

        vti04_authority = registry["vti_04_authority"]
        self.assertTrue(vti04_authority["retired"])
        for key in ("implementation_authority","branch_creation_authorized","acceptance_package_authorized","production_mutation_authorized","rules_action_bridge_authorized","roll_bridge_authorized"):
            self.assertFalse(vti04_authority[key])
        self.assertTrue(vti04_authority["matching_red_observed"])
        self.assertEqual(vti04_authority["application_merge_sha"], merge)

        vti05_authority = registry["vti_05_authority"]
        self.assertTrue(vti05_authority["selected_not_started"])
        self.assertFalse(vti05_authority["implementation_authority"])
        self.assertIsNone(vti05_authority["implementation_branch"])

        for phrase in (
            "VTI-04 — Rules Action & Roll Bridge",
            "COMPLETED_VERIFIED",
            "VTI-05 — Character Sheet, Item & Compendium Projection",
            "SELECTED_NOT_STARTED",
            "Platform selection remains evidence-driven",
        ):
            self.assertIn(phrase, program)

    def test_vti04_completed_scope_keeps_deferred_authorities_closed(self):
        authority = load_json("governance/ai/runtime/ACTIVE_AUTHORITY_REGISTRY.json")["vti_04_authority"]
        for key in (
            "implementation_authority",
            "branch_creation_authorized",
            "acceptance_package_authorized",
            "production_mutation_authorized",
            "rules_action_bridge_authorized",
            "roll_bridge_authorized",
            "external_rules_authority_authorized",
            "external_rng_authority_authorized",
            "autonomous_gm_adjudication_authorized",
            "provider_specific_schema_authorized",
            "credential_use_authorized",
            "external_account_mutation_authorized",
            "adapter_implementation_authorized",
            "external_sync_mutation_authorized",
            "canonical_game_state_mutation_authorized",
            "hidden_information_bypass_authorized",
            "durable_vti_persistence_authorized",
            "new_migration_authorized",
            "provider_activation_authorized",
            "tester_distribution_authorized",
            "release_or_deployment_authorized",
            "vti05_plus_authorized",
            "sgc01_plus_authorized",
        ):
            self.assertFalse(authority[key])

if __name__ == "__main__":
    unittest.main()
