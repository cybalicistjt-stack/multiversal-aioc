import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def load_json(path):
    return json.loads((ROOT / path).read_text(encoding="utf-8"))


def load_text(path):
    return (ROOT / path).read_text(encoding="utf-8")


class Vti03StableIdentityVersioningSynchronizationRegistrationTests(unittest.TestCase):
    def test_vti03_lifecycle_is_consistent_across_current_control_plane(self):
        baseline = "01aa25d60ad71e5ed318b9680f859c6927a90541"
        branch = "integration/vti-03-stable-identity-versioning-synchronization"
        checkpoint = load_json("governance/ai/work-state/VTI-03-attempt-001.json")
        backlog = load_json("governance/application-planning/virtual-tabletop-interoperability/VTI_PROGRAM_BACKLOG.json")
        pointer = load_json("governance/ai/runtime/CURRENT_WORK_POINTER.json")
        registry = load_json("governance/ai/runtime/ACTIVE_AUTHORITY_REGISTRY.json")
        index = load_json("governance/ai/runtime/ROADMAP_INDEX.json")
        runtime = load_json("governance/repository-health/RUNTIME_STATE_LIFECYCLE_REGISTRY.json")
        program = load_text("governance/application-planning/virtual-tabletop-interoperability/VTI_VIRTUAL_TABLETOP_INTEROPERABILITY_PROGRAM.md")

        self.assertEqual(checkpoint["work_item_id"], "VTI-03")
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

        vti03 = next(item for item in backlog["tranches"] if item["id"] == "VTI-03")
        self.assertEqual(vti03["status"], "in_progress")
        self.assertEqual(vti03["implementation_branch"], branch)
        self.assertTrue(vti03["implementation_authority"])
        self.assertEqual(backlog["active_contract"]["work_item"], "VTI-03")
        self.assertEqual(backlog["active_contract"]["production_mutation_authorized"], production_authorized)

        self.assertEqual(pointer["active_attempt"]["work_item_id"], "VTI-03")
        self.assertEqual(pointer["active_attempt"]["status"], "in_progress")
        self.assertEqual(pointer["active_attempt"]["implementation_branch"], branch)
        self.assertTrue(pointer["bounded_authority"]["acceptance_package_authorized"])
        self.assertEqual(pointer["bounded_authority"]["production_mutation_authorized"], production_authorized)

        authority = registry["vti_03_authority"]
        self.assertFalse(authority["selected_not_started"])
        self.assertTrue(authority["implementation_authority"])
        self.assertEqual(authority["implementation_branch"], branch)
        self.assertTrue(authority["branch_creation_authorized"])
        self.assertTrue(authority["acceptance_package_authorized"])
        self.assertEqual(authority["production_mutation_authorized"], production_authorized)

        self.assertEqual(index["current"]["work_item_id"], "VTI-03")
        self.assertEqual(index["current"]["status"], "in_progress")
        self.assertEqual(index["current"]["implementation_branch"], branch)
        self.assertEqual(index["current"]["production_mutation_authorized"], production_authorized)
        self.assertEqual(runtime["active_work"]["work_item"], "VTI-03")
        self.assertEqual(runtime["active_work"]["state"], "in_progress")
        self.assertEqual(runtime["active_work"]["implementation_branch"], branch)
        self.assertEqual(runtime["active_work"]["production_mutation_authorized"], production_authorized)
        self.assertEqual(runtime["application_repository"]["canonical_main"], baseline)

        for phrase in (
            "VTI-03 — Stable Identity, Versioning & Synchronization",
            "external-object mappings",
            "fingerprints",
            "version negotiation",
            "stale/conflict handling",
            "reconnect",
            "deduplication",
            "tombstones",
            "MIB-03",
            "VTI-04",
        ):
            self.assertIn(phrase, program)

    def test_vti03_scope_preserves_authority_and_successor_boundaries(self):
        checkpoint = load_json("governance/ai/work-state/VTI-03-attempt-001.json")
        scope = checkpoint["implementation_scope"]
        for item in (
            "provider-neutral stable external-object mappings between Multiversal canonical source references and derivative external-object identities",
            "deterministic fingerprints and version negotiation for synchronization decisions",
            "stale and conflict detection, reconnect, deduplication, tombstones and MIB-03 retry/recovery semantics",
            "visibility, ownership, consent, hidden-information filtering and GM-authority constraints preserved in synchronization metadata",
        ):
            self.assertIn(item, scope["authorized"])
        for item in (
            "rules actions, rolls, attacks, checks, powers, initiative, reactions or resolution bridging reserved to VTI-04",
            "provider-specific schemas, vendor selection or VTI-09 platform commitment",
            "credentials, external account mutation, adapter implementation or canonical game-state mutation",
            "durable VTI persistence or a new migration before separately authorized persistence work",
        ):
            self.assertIn(item, scope["not_authorized"])

        authority = load_json("governance/ai/runtime/ACTIVE_AUTHORITY_REGISTRY.json")["vti_03_authority"]
        for key in (
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
