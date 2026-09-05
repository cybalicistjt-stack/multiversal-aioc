import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]

def load_json(path):
    return json.loads((ROOT / path).read_text(encoding="utf-8"))

def load_text(path):
    return (ROOT / path).read_text(encoding="utf-8")

class Vti04RulesActionRollBridgeRegistrationTests(unittest.TestCase):
    def test_vti04_governed_start_is_consistent_across_current_control_plane(self):
        baseline = "56ab87c2be214d4d7edb15e0e8d02429a07ee2d4"
        branch = "integration/vti-04-rules-action-roll-bridge"
        checkpoint = load_json("governance/ai/work-state/VTI-04-attempt-001.json")
        backlog = load_json("governance/application-planning/virtual-tabletop-interoperability/VTI_PROGRAM_BACKLOG.json")
        pointer = load_json("governance/ai/runtime/CURRENT_WORK_POINTER.json")
        registry = load_json("governance/ai/runtime/ACTIVE_AUTHORITY_REGISTRY.json")
        index = load_json("governance/ai/runtime/ROADMAP_INDEX.json")
        runtime = load_json("governance/repository-health/RUNTIME_STATE_LIFECYCLE_REGISTRY.json")
        program = load_text("governance/application-planning/virtual-tabletop-interoperability/VTI_VIRTUAL_TABLETOP_INTEROPERABILITY_PROGRAM.md")

        self.assertEqual(checkpoint["work_item_id"], "VTI-04")
        self.assertEqual(checkpoint["status"], "in_progress")
        self.assertEqual(checkpoint["application_baseline_sha"], baseline)
        self.assertEqual(checkpoint["implementation_branch"], branch)
        self.assertTrue(checkpoint["implementation_authority"])
        self.assertTrue(checkpoint["branch_creation_authorized"])
        self.assertTrue(checkpoint["acceptance_package_authorized"])

        production_authorized = checkpoint["production_mutation_authorized"]
        red = checkpoint.get("validation", {}).get("acceptance_red")
        if production_authorized:
            self.assertIsNotNone(red)
            self.assertTrue(red["matching_red_observed"])
        else:
            self.assertIsNone(red)

        vti04 = next(item for item in backlog["tranches"] if item["id"] == "VTI-04")
        self.assertEqual(vti04["status"], "in_progress")
        self.assertEqual(vti04["implementation_branch"], branch)
        self.assertTrue(vti04["implementation_authority"])
        self.assertEqual(backlog["active_contract"]["work_item"], "VTI-04")
        self.assertEqual(backlog["active_contract"]["production_mutation_authorized"], production_authorized)

        self.assertEqual(pointer["active_attempt"]["work_item_id"], "VTI-04")
        self.assertEqual(pointer["active_attempt"]["status"], "in_progress")
        self.assertEqual(pointer["active_attempt"]["implementation_branch"], branch)
        self.assertTrue(pointer["bounded_authority"]["acceptance_package_authorized"])
        self.assertEqual(pointer["bounded_authority"]["production_mutation_authorized"], production_authorized)

        authority = registry["vti_04_authority"]
        self.assertFalse(authority["selected_not_started"])
        self.assertTrue(authority["implementation_authority"])
        self.assertEqual(authority["implementation_branch"], branch)
        self.assertTrue(authority["branch_creation_authorized"])
        self.assertTrue(authority["acceptance_package_authorized"])
        self.assertEqual(authority["production_mutation_authorized"], production_authorized)

        self.assertEqual(index["current"]["work_item_id"], "VTI-04")
        self.assertEqual(index["current"]["status"], "in_progress")
        self.assertEqual(index["current"]["implementation_branch"], branch)
        self.assertEqual(index["current"]["production_mutation_authorized"], production_authorized)
        self.assertEqual(runtime["active_work"]["work_item"], "VTI-04")
        self.assertEqual(runtime["active_work"]["state"], "in_progress")
        self.assertEqual(runtime["active_work"]["implementation_branch"], branch)
        self.assertEqual(runtime["active_work"]["production_mutation_authorized"], production_authorized)
        self.assertEqual(runtime["application_repository"]["canonical_main"], baseline)

        for phrase in (
            "VTI-04 — Rules Action & Roll Bridge",
            "roll",
            "attack",
            "check",
            "power",
            "resource",
            "condition",
            "initiative",
            "reaction",
            "gm-adjudication",
            "rules or RNG authorities",
            "VTI-03/MIB-03",
            "VTI-05",
        ):
            self.assertIn(phrase, program)

    def test_vti04_scope_preserves_authority_and_successor_boundaries(self):
        checkpoint = load_json("governance/ai/work-state/VTI-04-attempt-001.json")
        scope = checkpoint["implementation_scope"]
        for item in (
            "provider-neutral action-request envelopes for rolls, attacks, checks, powers, resources, conditions, initiative, reactions and GM adjudication",
            "deterministic Multiversal validation/resolution handoff semantics that keep external VTTs as requesting clients rather than rules authorities",
            "authoritative result and receipt envelopes preserving canonical source references, visibility, ownership, consent and GM-authority metadata",
            "duplicate/idempotent request handling, authoritative receipt replay and status-before-retry semantics compatible with the completed VTI-03 and MIB-03 recovery contracts",
        ):
            self.assertIn(item, scope["authorized"])
        for item in (
            "provider-specific schemas, vendor selection/ranking or VTI-09 platform commitment",
            "re-authoring or bypassing native Multiversal rules resolution, external-VTT rules authority, external-VTT RNG authority or autonomous GM adjudication",
            "credentials, external account mutation, adapter implementation, live external synchronization mutation or canonical game-state mutation",
            "durable VTI persistence or a new migration before separately authorized persistence work",
            "VTI-05 character-sheet/item/compendium projection, VTI-06 scene/map/token/MAI behavior or any VTI-05+ implementation",
        ):
            self.assertIn(item, scope["not_authorized"])

        authority = load_json("governance/ai/runtime/ACTIVE_AUTHORITY_REGISTRY.json")["vti_04_authority"]
        production_authorized = checkpoint["production_mutation_authorized"]
        self.assertEqual(authority["rules_action_bridge_authorized"], production_authorized)
        self.assertEqual(authority["roll_bridge_authorized"], production_authorized)
        if production_authorized:
            self.assertTrue(authority["matching_red_observed"])
            self.assertIsNotNone(checkpoint["validation"]["acceptance_red"])
            self.assertTrue(checkpoint["validation"]["acceptance_red"]["matching_red_observed"])

        for key in (
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
