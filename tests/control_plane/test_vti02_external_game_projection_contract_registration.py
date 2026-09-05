import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def load_json(path):
    return json.loads((ROOT / path).read_text(encoding="utf-8"))


def load_text(path):
    return (ROOT / path).read_text(encoding="utf-8")


class Vti02ExternalGameProjectionContractRegistrationTests(unittest.TestCase):
    def test_vti02_lifecycle_is_consistent_across_current_control_plane(self):
        baseline = "027fad06d0bac3a20d56f0cc2a674581662cd1b9"
        branch = "integration/vti-02-multiversal-external-game-projection-contract"
        checkpoint = load_json("governance/ai/work-state/VTI-02-attempt-001.json")
        backlog = load_json("governance/application-planning/virtual-tabletop-interoperability/VTI_PROGRAM_BACKLOG.json")
        pointer = load_json("governance/ai/runtime/CURRENT_WORK_POINTER.json")
        registry = load_json("governance/ai/runtime/ACTIVE_AUTHORITY_REGISTRY.json")
        index = load_json("governance/ai/runtime/ROADMAP_INDEX.json")
        runtime = load_json("governance/repository-health/RUNTIME_STATE_LIFECYCLE_REGISTRY.json")
        program = load_text("governance/application-planning/virtual-tabletop-interoperability/VTI_VIRTUAL_TABLETOP_INTEROPERABILITY_PROGRAM.md")

        self.assertEqual(checkpoint["work_item_id"], "VTI-02")
        self.assertEqual(checkpoint["status"], "in_progress")
        self.assertEqual(checkpoint["application_baseline_sha"], baseline)
        self.assertEqual(checkpoint["implementation_branch"], branch)
        self.assertTrue(checkpoint["implementation_authority"])
        self.assertTrue(checkpoint["branch_creation_authorized"])
        self.assertTrue(checkpoint["acceptance_package_authorized"])

        production_authorized = checkpoint["production_mutation_authorized"]
        red = checkpoint["validation"]["acceptance_red"]
        if production_authorized:
            self.assertIsNotNone(red)
            self.assertTrue(red["matching_red_observed"])
            self.assertEqual(red["head_sha"], "db4a4c436cb6eeb011afd9614568fb68f070c785")
            self.assertEqual(red["run_id"], 33989074845)
            self.assertEqual(red["deterministic_receipt_sha256"], "7005e6b204a3b24a1e8a6e8e8ac2f80a295540afaf9fc9b3bbfb733a5f39ccc7")
        else:
            self.assertIsNone(red)

        vti02 = next(item for item in backlog["tranches"] if item["id"] == "VTI-02")
        self.assertEqual(vti02["status"], "in_progress")
        self.assertEqual(vti02["implementation_branch"], branch)
        self.assertTrue(vti02["implementation_authority"])
        self.assertEqual(backlog["active_contract"]["work_item"], "VTI-02")
        self.assertEqual(backlog["active_contract"]["production_mutation_authorized"], production_authorized)
        self.assertEqual(backlog["active_contract"]["matching_red_observed"], production_authorized)

        self.assertEqual(pointer["active_attempt"]["work_item_id"], "VTI-02")
        self.assertEqual(pointer["active_attempt"]["status"], "in_progress")
        self.assertEqual(pointer["active_attempt"]["implementation_branch"], branch)
        self.assertTrue(pointer["bounded_authority"]["acceptance_package_authorized"])
        self.assertEqual(pointer["bounded_authority"]["production_mutation_authorized"], production_authorized)

        authority = registry["vti_02_authority"]
        self.assertFalse(authority["selected_not_started"])
        self.assertTrue(authority["implementation_authority"])
        self.assertEqual(authority["implementation_branch"], branch)
        self.assertTrue(authority["branch_creation_authorized"])
        self.assertTrue(authority["acceptance_package_authorized"])
        self.assertEqual(authority["production_mutation_authorized"], production_authorized)
        self.assertEqual(authority["matching_red_observed"], production_authorized)

        self.assertEqual(index["current"]["work_item_id"], "VTI-02")
        self.assertEqual(index["current"]["status"], "in_progress")
        self.assertEqual(index["current"]["implementation_branch"], branch)
        self.assertEqual(index["current"]["production_mutation_authorized"], production_authorized)
        self.assertEqual(runtime["active_work"]["work_item"], "VTI-02")
        self.assertEqual(runtime["active_work"]["state"], "in_progress")
        self.assertEqual(runtime["active_work"]["implementation_branch"], branch)
        self.assertEqual(runtime["active_work"]["production_mutation_authorized"], production_authorized)
        self.assertEqual(runtime["application_repository"]["canonical_main"], baseline)

        for phrase in (
            "VTI-02 — Multiversal External Game Projection Contract",
            "Character, Creature, Item, Action, Condition, Encounter, Scene, Vehicle and RuleReference",
            "present`, `redacted`, `unsupported",
            "VTI-03",
            "VTI-04",
            "Platform selection remains evidence-driven",
        ):
            self.assertIn(phrase, program)

    def test_vti02_scope_preserves_provider_neutral_and_successor_boundaries(self):
        checkpoint = load_json("governance/ai/work-state/VTI-02-attempt-001.json")
        scope = checkpoint["implementation_scope"]
        for item in (
            "provider-neutral projection kinds Character, Creature, Item, Action, Condition, Encounter, Scene, Vehicle and RuleReference",
            "deterministic projection field ordering and deterministic receipts independent of supplied projection or field ordering",
            "explicit projection availability states present, redacted and unsupported so hidden or unavailable information is never manufactured",
        ):
            self.assertIn(item, scope["authorized"])
        for item in (
            "vendor selection, ranking, provider-specific schemas or VTI-09 platform commitment",
            "external-object mapping, fingerprints, version negotiation, stale/conflict handling, reconnect, deduplication or tombstones reserved to VTI-03",
            "rules actions, rolls, attacks, checks, powers, initiative, reactions or resolution bridging reserved to VTI-04",
        ):
            self.assertIn(item, scope["not_authorized"])

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
