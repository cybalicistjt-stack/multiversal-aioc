import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]

def load_json(path):
    return json.loads((ROOT / path).read_text(encoding="utf-8"))

def load_text(path):
    return (ROOT / path).read_text(encoding="utf-8")

class Vti05CharacterSheetItemCompendiumProjectionRegistrationTests(unittest.TestCase):
    def test_vti05_completed_lifecycle_and_vti06_successor_are_consistent(self):
        merge = "6b7e101c08d52362af824b68f43cd983794893c6"
        current_app_main = "e9ddbf9c763faca74689cb3776ad21501c341ba5"
        checkpoint = load_json("governance/ai/work-state/VTI-05-attempt-001.json")
        vti06 = load_json("governance/ai/work-state/VTI-06-attempt-001.json")
        backlog = load_json("governance/application-planning/virtual-tabletop-interoperability/VTI_PROGRAM_BACKLOG.json")
        pointer = load_json("governance/ai/runtime/CURRENT_WORK_POINTER.json")
        registry = load_json("governance/ai/runtime/ACTIVE_AUTHORITY_REGISTRY.json")
        index = load_json("governance/ai/runtime/ROADMAP_INDEX.json")
        runtime = load_json("governance/repository-health/RUNTIME_STATE_LIFECYCLE_REGISTRY.json")
        program = load_text("governance/application-planning/virtual-tabletop-interoperability/VTI_VIRTUAL_TABLETOP_INTEROPERABILITY_PROGRAM.md")

        self.assertEqual(checkpoint["status"], "completed_verified")
        self.assertEqual(checkpoint["application_pr"], 420)
        self.assertEqual(checkpoint["application_merge_sha"], merge)
        self.assertTrue(checkpoint["authority_retired"])
        self.assertFalse(checkpoint["implementation_authority"])
        self.assertFalse(checkpoint["branch_creation_authorized"])
        self.assertFalse(checkpoint["acceptance_package_authorized"])
        self.assertFalse(checkpoint["production_mutation_authorized"])
        self.assertTrue(checkpoint["completed"])

        red = checkpoint["validation"]["acceptance_red"]
        green = checkpoint["validation"]["final_green"]
        self.assertEqual(red["head_sha"], "5ff92aaebc311933a3fa814b22badcb8ee694f76")
        self.assertEqual(red["run_id"], 33997794873)
        self.assertEqual(red["deterministic_receipt_sha256"], "d234d207d409056383670a853e29d6d2748ea5bc59db3892f3c7d9a0133bff7b")
        self.assertTrue(red["matching_red_observed"])
        self.assertEqual(green["head_sha"], "a26f4aa49f76c668d8a28030d52e3b1719cd25ef")
        self.assertEqual(green["run_id"], 33999669961)
        self.assertEqual(green["deterministic_receipt_sha256"], "b093ef2a838a5d76157342f91c54d8fa79b6ab4458aa21f3bac2f762bdcf688b")
        self.assertEqual(green["historical_profile_fanout"], 0)

        vti05 = next(item for item in backlog["tranches"] if item["id"] == "VTI-05")
        self.assertEqual(vti05["status"], "completed_verified")
        self.assertEqual(vti05["application_merge_sha"], merge)
        self.assertFalse(vti05["implementation_authority"])

        authority = registry["vti_05_authority"]
        self.assertTrue(authority["retired"])
        self.assertFalse(authority["implementation_authority"])
        self.assertEqual(authority["application_merge_sha"], merge)
        self.assertTrue(authority["matching_red_observed"])
        for key in ("branch_creation_authorized","acceptance_package_authorized","production_mutation_authorized","character_sheet_projection_authorized","item_projection_authorized","compendium_projection_authorized"):
            self.assertFalse(authority[key])

        current = backlog["current_item"]
        order = backlog["strict_order"]
        self.assertGreater(order.index(current), order.index("VTI-05"))
        self.assertEqual(current, pointer["active_attempt"]["work_item_id"])
        self.assertEqual(current, index["current"]["work_item_id"])
        self.assertEqual(current, runtime["active_work"]["work_item"])

        if current == "VTI-06":
            self.assertIn(vti06["status"], {"selected_not_started", "in_progress"})
            self.assertEqual(pointer["active_attempt"]["status"], vti06["status"])
            self.assertEqual(index["current"]["status"], vti06["status"])
            self.assertEqual(runtime["active_work"]["state"], vti06["status"])
            self.assertEqual(vti06["application_baseline_sha"], current_app_main)
            if vti06["status"] == "selected_not_started":
                self.assertIsNone(vti06["implementation_branch"])
                self.assertFalse(vti06["implementation_authority"])
                self.assertFalse(vti06["branch_creation_authorized"])
                self.assertFalse(vti06["acceptance_package_authorized"])
                self.assertFalse(vti06["production_mutation_authorized"])
                self.assertTrue(registry["vti_06_authority"]["selected_not_started"])
                self.assertFalse(registry["vti_06_authority"]["implementation_authority"])
        else:
            self.assertEqual(vti06["status"], "completed_verified")
            self.assertTrue(vti06["authority_retired"])
            self.assertTrue(registry["vti_06_authority"]["retired"])

        self.assertEqual(runtime["application_repository"]["canonical_main"], pointer["active_attempt"]["application_baseline_sha"])
        for phrase in (
            "VTI-05 — Character Sheet, Item & Compendium Projection",
            "VTI-06 — Scene, Map, Token & MAI Bridge",
            "Platform selection remains evidence-driven",
        ):
            self.assertIn(phrase, program)

    def test_vti05_completed_scope_preserves_projection_and_successor_boundaries(self):
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
