import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]

def load_json(path):
    return json.loads((ROOT / path).read_text(encoding="utf-8"))

def load_text(path):
    return (ROOT / path).read_text(encoding="utf-8")

class Vti03StableIdentityVersioningSynchronizationRegistrationTests(unittest.TestCase):
    def test_vti03_completed_lifecycle_and_vti04_successor_are_consistent(self):
        merge = "56ab87c2be214d4d7edb15e0e8d02429a07ee2d4"
        checkpoint = load_json("governance/ai/work-state/VTI-03-attempt-001.json")
        successor = load_json("governance/ai/work-state/VTI-04-attempt-001.json")
        backlog = load_json("governance/application-planning/virtual-tabletop-interoperability/VTI_PROGRAM_BACKLOG.json")
        pointer = load_json("governance/ai/runtime/CURRENT_WORK_POINTER.json")
        registry = load_json("governance/ai/runtime/ACTIVE_AUTHORITY_REGISTRY.json")
        index = load_json("governance/ai/runtime/ROADMAP_INDEX.json")
        runtime = load_json("governance/repository-health/RUNTIME_STATE_LIFECYCLE_REGISTRY.json")
        program = load_text("governance/application-planning/virtual-tabletop-interoperability/VTI_VIRTUAL_TABLETOP_INTEROPERABILITY_PROGRAM.md")
        self.assertEqual(checkpoint["status"], "completed_verified")
        self.assertEqual(checkpoint["application_pr"], 417)
        self.assertEqual(checkpoint["application_merge_sha"], merge)
        self.assertTrue(checkpoint["authority_retired"])
        self.assertFalse(checkpoint["implementation_authority"])
        self.assertFalse(checkpoint["branch_creation_authorized"])
        self.assertFalse(checkpoint["acceptance_package_authorized"])
        self.assertFalse(checkpoint["production_mutation_authorized"])
        self.assertTrue(checkpoint["completed"])
        red = checkpoint["validation"]["acceptance_red"]
        green = checkpoint["validation"]["final_green"]
        self.assertEqual(red["head_sha"], "fdb9139a5c75e30b03af16dec9815287eebcc763")
        self.assertTrue(red["matching_red_observed"])
        self.assertEqual(green["head_sha"], "47d08c706fcafdfb7cb602e3e19a43eef85b6896")
        self.assertEqual(green["run_id"], 33992208512)
        self.assertEqual(green["deterministic_receipt_sha256"], "af6bf644b06ea1e9ac28f60226f939195d67c89bf88fb622c66dfc8544d54e25")
        self.assertEqual(green["historical_profile_fanout"], 0)
        self.assertEqual(backlog["completed_through"], "VTI-03")
        self.assertEqual(backlog["current_item"], "VTI-04")
        self.assertIn(successor["status"], {"selected_not_started", "in_progress"})
        self.assertEqual(successor["application_baseline_sha"], merge)
        self.assertEqual(pointer["active_attempt"]["work_item_id"], "VTI-04")
        self.assertEqual(pointer["active_attempt"]["status"], successor["status"])
        self.assertEqual(index["current"]["work_item_id"], "VTI-04")
        self.assertEqual(index["current"]["status"], successor["status"])
        self.assertEqual(runtime["active_work"]["work_item"], "VTI-04")
        self.assertEqual(runtime["active_work"]["state"], successor["status"])
        self.assertEqual(runtime["application_repository"]["canonical_main"], merge)
        self.assertTrue(registry["vti_03_authority"]["retired"])
        self.assertFalse(registry["vti_03_authority"]["implementation_authority"])
        if successor["status"] == "selected_not_started":
            self.assertIsNone(successor["implementation_branch"])
            self.assertFalse(successor["implementation_authority"])
            self.assertFalse(successor["branch_creation_authorized"])
            self.assertFalse(successor["acceptance_package_authorized"])
            self.assertFalse(successor["production_mutation_authorized"])
            self.assertTrue(registry["vti_04_authority"]["selected_not_started"])
            self.assertFalse(registry["vti_04_authority"]["implementation_authority"])
        else:
            self.assertEqual(successor["implementation_branch"], "integration/vti-04-rules-action-roll-bridge")
            self.assertTrue(successor["implementation_authority"])
            self.assertTrue(successor["branch_creation_authorized"])
            self.assertTrue(successor["acceptance_package_authorized"])
            production_authorized = successor["production_mutation_authorized"]
            self.assertEqual(pointer["bounded_authority"]["production_mutation_authorized"], production_authorized)
            self.assertFalse(registry["vti_04_authority"]["selected_not_started"])
            self.assertTrue(registry["vti_04_authority"]["implementation_authority"])
            self.assertTrue(registry["vti_04_authority"]["acceptance_package_authorized"])
            self.assertEqual(registry["vti_04_authority"]["production_mutation_authorized"], production_authorized)
            if production_authorized:
                self.assertIsNotNone(successor["validation"]["acceptance_red"])
                self.assertTrue(successor["validation"]["acceptance_red"]["matching_red_observed"])
                self.assertTrue(registry["vti_04_authority"]["matching_red_observed"])
            else:
                self.assertIsNone(successor["validation"]["acceptance_red"])
        for phrase in ("VTI-03 — Stable Identity, Versioning & Synchronization","COMPLETED_VERIFIED","VTI-04 — Rules Action & Roll Bridge","MIB-03","Platform selection remains evidence-driven"):
            self.assertIn(phrase, program)

    def test_vti03_completed_scope_keeps_deferred_authorities_closed(self):
        authority = load_json("governance/ai/runtime/ACTIVE_AUTHORITY_REGISTRY.json")["vti_03_authority"]
        for key in ("implementation_authority","branch_creation_authorized","acceptance_package_authorized","production_mutation_authorized","external_object_mapping_authorized","versioning_authorized","external_sync_mutation_authorized","conflict_resolution_authorized","reconnect_authorized","deduplication_authorized","tombstone_authorized","rules_action_bridge_authorized","provider_specific_schema_authorized","credential_use_authorized","external_account_mutation_authorized","adapter_implementation_authorized","canonical_game_state_mutation_authorized","hidden_information_bypass_authorized","durable_vti_persistence_authorized","new_migration_authorized","provider_activation_authorized","tester_distribution_authorized","release_or_deployment_authorized","vti04_plus_authorized","sgc01_plus_authorized"):
            self.assertFalse(authority[key])

if __name__ == "__main__":
    unittest.main()
