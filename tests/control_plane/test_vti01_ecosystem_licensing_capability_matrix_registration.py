import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]

def load_json(path):
    return json.loads((ROOT / path).read_text(encoding="utf-8"))

def load_text(path):
    return (ROOT / path).read_text(encoding="utf-8")

class Vti01EcosystemLicensingCapabilityMatrixRegistrationTests(unittest.TestCase):
    def test_vti01_completed_lifecycle_and_current_successor_chain_are_consistent(self):
        checkpoint = load_json("governance/ai/work-state/VTI-01-attempt-001.json")
        backlog = load_json("governance/application-planning/virtual-tabletop-interoperability/VTI_PROGRAM_BACKLOG.json")
        pointer = load_json("governance/ai/runtime/CURRENT_WORK_POINTER.json")
        registry = load_json("governance/ai/runtime/ACTIVE_AUTHORITY_REGISTRY.json")
        index = load_json("governance/ai/runtime/ROADMAP_INDEX.json")
        runtime = load_json("governance/repository-health/RUNTIME_STATE_LIFECYCLE_REGISTRY.json")
        program = load_text("governance/application-planning/virtual-tabletop-interoperability/VTI_VIRTUAL_TABLETOP_INTEROPERABILITY_PROGRAM.md")
        self.assertEqual(checkpoint["status"], "completed_verified")
        self.assertTrue(checkpoint["authority_retired"])
        self.assertFalse(checkpoint["implementation_authority"])
        self.assertEqual(checkpoint["application_merge_sha"], "027fad06d0bac3a20d56f0cc2a674581662cd1b9")
        self.assertTrue(registry["vti_01_authority"]["retired"])
        current = backlog["current_item"]
        order = backlog["strict_order"]
        self.assertGreater(order.index(current), order.index("VTI-01"))
        self.assertEqual(current, pointer["active_attempt"]["work_item_id"])
        self.assertEqual(current, registry["active_planning_work"]["work_item"])
        self.assertEqual(current, index["current"]["work_item_id"])
        self.assertEqual(current, runtime["active_work"]["work_item"])
        self.assertEqual(runtime["application_repository"]["canonical_main"], pointer["active_attempt"]["application_baseline_sha"])
        for phrase in ("VTI-01 — VTT Ecosystem, Licensing & Capability Matrix","VTI-02 — Multiversal External Game Projection Contract","VTI-03 — Stable Identity, Versioning & Synchronization","VTI-04 — Rules Action & Roll Bridge","VTI-05 — Character Sheet, Item & Compendium Projection","Platform selection remains evidence-driven"):
            self.assertIn(phrase, program)

    def test_vti01_scope_keeps_external_mutation_and_vendor_selection_closed(self):
        authority = load_json("governance/ai/runtime/ACTIVE_AUTHORITY_REGISTRY.json")["vti_01_authority"]
        for key in ("vendor_selection_authorized","external_account_mutation_authorized","credential_use_authorized","adapter_implementation_authorized","external_sync_mutation_authorized","canonical_game_state_mutation_authorized","hidden_information_bypass_authorized","provider_activation_authorized","tester_distribution_authorized","release_or_deployment_authorized","vti02_plus_authorized","sgc01_plus_authorized"):
            self.assertFalse(authority[key])

if __name__ == "__main__":
    unittest.main()
