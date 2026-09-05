import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]

def load_json(path):
    return json.loads((ROOT / path).read_text(encoding="utf-8"))

class Vti05CharacterSheetItemCompendiumProjectionRegistrationTests(unittest.TestCase):
    def test_vti05_governed_start_is_consistent_across_current_control_plane(self):
        baseline = "295424982135337de80cccfac072764ab35183cc"
        branch = "integration/vti-05-character-sheet-item-compendium-projection"
        checkpoint = load_json("governance/ai/work-state/VTI-05-attempt-001.json")
        backlog = load_json("governance/application-planning/virtual-tabletop-interoperability/VTI_PROGRAM_BACKLOG.json")
        pointer = load_json("governance/ai/runtime/CURRENT_WORK_POINTER.json")
        registry = load_json("governance/ai/runtime/ACTIVE_AUTHORITY_REGISTRY.json")
        index = load_json("governance/ai/runtime/ROADMAP_INDEX.json")
        runtime = load_json("governance/repository-health/RUNTIME_STATE_LIFECYCLE_REGISTRY.json")

        self.assertEqual(checkpoint["status"], "in_progress")
        self.assertEqual(checkpoint["application_baseline_sha"], baseline)
        self.assertEqual(checkpoint["implementation_branch"], branch)
        self.assertTrue(checkpoint["implementation_authority"])
        self.assertTrue(checkpoint["branch_creation_authorized"])
        self.assertTrue(checkpoint["acceptance_package_authorized"])
        self.assertTrue(checkpoint["production_mutation_authorized"])
        red = checkpoint["validation"]["acceptance_red"]
        self.assertEqual(red["head_sha"], "5ff92aaebc311933a3fa814b22badcb8ee694f76")
        self.assertEqual(red["run_id"], 33997794873)
        self.assertEqual(red["deterministic_receipt_sha256"], "d234d207d409056383670a853e29d6d2748ea5bc59db3892f3c7d9a0133bff7b")
        self.assertTrue(red["matching_red_observed"])

        vti05 = next(item for item in backlog["tranches"] if item["id"] == "VTI-05")
        self.assertEqual(vti05["status"], "in_progress")
        self.assertEqual(vti05["implementation_branch"], branch)
        self.assertTrue(vti05["implementation_authority"])
        self.assertEqual(backlog["active_contract"]["work_item"], "VTI-05")
        self.assertTrue(backlog["active_contract"]["production_mutation_authorized"])

        self.assertEqual(pointer["active_attempt"]["work_item_id"], "VTI-05")
        self.assertEqual(pointer["active_attempt"]["status"], "in_progress")
        self.assertEqual(pointer["active_attempt"]["implementation_branch"], branch)
        self.assertTrue(pointer["bounded_authority"]["acceptance_package_authorized"])
        self.assertTrue(pointer["bounded_authority"]["production_mutation_authorized"])

        authority = registry["vti_05_authority"]
        self.assertFalse(authority["selected_not_started"])
        self.assertTrue(authority["implementation_authority"])
        self.assertEqual(authority["implementation_branch"], branch)
        self.assertTrue(authority["branch_creation_authorized"])
        self.assertTrue(authority["acceptance_package_authorized"])
        self.assertTrue(authority["production_mutation_authorized"])
        self.assertTrue(authority["matching_red_observed"])
        for key in ("character_sheet_projection_authorized","item_projection_authorized","compendium_projection_authorized"):
            self.assertTrue(authority[key])

        self.assertEqual(index["current"]["work_item_id"], "VTI-05")
        self.assertEqual(index["current"]["status"], "in_progress")
        self.assertEqual(index["current"]["implementation_branch"], branch)
        self.assertTrue(index["current"]["production_mutation_authorized"])
        self.assertEqual(runtime["active_work"]["work_item"], "VTI-05")
        self.assertEqual(runtime["active_work"]["state"], "in_progress")
        self.assertEqual(runtime["active_work"]["implementation_branch"], branch)
        self.assertTrue(runtime["active_work"]["production_mutation_authorized"])
        self.assertEqual(runtime["application_repository"]["canonical_main"], baseline)

    def test_vti05_scope_preserves_projection_and_successor_boundaries(self):
        checkpoint = load_json("governance/ai/work-state/VTI-05-attempt-001.json")
        scope = checkpoint["implementation_scope"]
        for item in (
            "provider-neutral character-sheet projection for Characters, NPCs and creatures with canonical source references and explicit present/redacted/unsupported fidelity",
            "provider-neutral item projection for equipment, powers and conditions without provider-specific schemas",
            "provider-neutral compendium projection for RuleReference, roll-table and vehicle records where platform capability supports them",
            "deterministic normalization, visibility, ownership, consent, hidden-information filtering and GM-authority preservation across projection envelopes",
        ):
            self.assertIn(item, scope["authorized"])
        for item in (
            "provider-specific schemas, vendor selection/ranking or VTI-09 platform commitment",
            "credentials, external account mutation, adapter implementation, live external synchronization mutation or canonical game-state mutation",
            "durable VTI persistence or a new migration before separately authorized persistence work",
            "VTI-06 scene/map/token/MAI bridge behavior or any VTI-06+ implementation",
        ):
            self.assertIn(item, scope["not_authorized"])

if __name__ == "__main__":
    unittest.main()
