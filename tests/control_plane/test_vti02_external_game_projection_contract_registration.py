import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]

def load_json(path):
    return json.loads((ROOT / path).read_text(encoding="utf-8"))

def load_text(path):
    return (ROOT / path).read_text(encoding="utf-8")

class Vti02ExternalGameProjectionContractRegistrationTests(unittest.TestCase):
    def test_vti02_completed_lifecycle_and_current_successor_are_consistent(self):
        checkpoint = load_json("governance/ai/work-state/VTI-02-attempt-001.json")
        vti03 = load_json("governance/ai/work-state/VTI-03-attempt-001.json")
        backlog = load_json("governance/application-planning/virtual-tabletop-interoperability/VTI_PROGRAM_BACKLOG.json")
        pointer = load_json("governance/ai/runtime/CURRENT_WORK_POINTER.json")
        registry = load_json("governance/ai/runtime/ACTIVE_AUTHORITY_REGISTRY.json")
        index = load_json("governance/ai/runtime/ROADMAP_INDEX.json")
        runtime = load_json("governance/repository-health/RUNTIME_STATE_LIFECYCLE_REGISTRY.json")
        program = load_text("governance/application-planning/virtual-tabletop-interoperability/VTI_VIRTUAL_TABLETOP_INTEROPERABILITY_PROGRAM.md")
        self.assertEqual(checkpoint["status"], "completed_verified")
        self.assertEqual(checkpoint["application_merge_sha"], "01aa25d60ad71e5ed318b9680f859c6927a90541")
        self.assertTrue(checkpoint["authority_retired"])
        self.assertFalse(checkpoint["implementation_authority"])
        self.assertTrue(registry["vti_02_authority"]["retired"])
        current = backlog["current_item"]
        self.assertIn(current, {"VTI-03", "VTI-04"})
        self.assertEqual(current, pointer["active_attempt"]["work_item_id"])
        self.assertEqual(current, index["current"]["work_item_id"])
        self.assertEqual(current, runtime["active_work"]["work_item"])
        if current == "VTI-04":
            vti04 = load_json("governance/ai/work-state/VTI-04-attempt-001.json")
            self.assertEqual(vti03["status"], "completed_verified")
            self.assertTrue(vti03["authority_retired"])
            self.assertEqual(vti03["application_merge_sha"], "56ab87c2be214d4d7edb15e0e8d02429a07ee2d4")
            self.assertEqual(vti04["status"], "selected_not_started")
            self.assertEqual(vti04["application_baseline_sha"], vti03["application_merge_sha"])
            self.assertFalse(vti04["implementation_authority"])
            self.assertTrue(registry["vti_04_authority"]["selected_not_started"])
        for phrase in ("VTI-02 — Multiversal External Game Projection Contract","COMPLETED_VERIFIED","VTI-03 — Stable Identity, Versioning & Synchronization","VTI-04 — Rules Action & Roll Bridge","Platform selection remains evidence-driven"):
            self.assertIn(phrase, program)

    def test_vti02_completed_scope_keeps_deferred_authorities_closed(self):
        authority = load_json("governance/ai/runtime/ACTIVE_AUTHORITY_REGISTRY.json")["vti_02_authority"]
        for key in ("vendor_selection_authorized","provider_specific_schema_authorized","external_account_mutation_authorized","credential_use_authorized","adapter_implementation_authorized","external_sync_mutation_authorized","canonical_game_state_mutation_authorized","hidden_information_bypass_authorized","external_object_mapping_authorized","versioning_authorized","conflict_resolution_authorized","rules_action_bridge_authorized","durable_vti_persistence_authorized","new_migration_authorized","provider_activation_authorized","tester_distribution_authorized","release_or_deployment_authorized","vti03_plus_authorized","sgc01_plus_authorized"):
            self.assertFalse(authority[key])

if __name__ == "__main__":
    unittest.main()
