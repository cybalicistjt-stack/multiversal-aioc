import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def load_json(path):
    return json.loads((ROOT / path).read_text(encoding="utf-8"))


def load_text(path):
    return (ROOT / path).read_text(encoding="utf-8")


class Vti01EcosystemLicensingCapabilityMatrixRegistrationTests(unittest.TestCase):
    def test_vti01_lifecycle_and_successor_are_consistent(self):
        baseline = "e61109affe9d662e6da6eb214c1acc870079c1a7"
        branch = "integration/vti-01-vtt-ecosystem-licensing-capability-matrix"
        merge = "027fad06d0bac3a20d56f0cc2a674581662cd1b9"
        vti02_branch = "integration/vti-02-multiversal-external-game-projection-contract"
        checkpoint = load_json("governance/ai/work-state/VTI-01-attempt-001.json")
        backlog = load_json("governance/application-planning/virtual-tabletop-interoperability/VTI_PROGRAM_BACKLOG.json")
        pointer = load_json("governance/ai/runtime/CURRENT_WORK_POINTER.json")
        registry = load_json("governance/ai/runtime/ACTIVE_AUTHORITY_REGISTRY.json")
        index = load_json("governance/ai/runtime/ROADMAP_INDEX.json")
        runtime = load_json("governance/repository-health/RUNTIME_STATE_LIFECYCLE_REGISTRY.json")
        program = load_text("governance/application-planning/virtual-tabletop-interoperability/VTI_VIRTUAL_TABLETOP_INTEROPERABILITY_PROGRAM.md")

        self.assertEqual(checkpoint["work_item_id"], "VTI-01")
        self.assertEqual(checkpoint["application_baseline_sha"], baseline)
        self.assertIn(checkpoint["status"], {"in_progress", "completed_verified"})
        self.assertEqual(checkpoint["implementation_branch"], branch)

        vti01 = next(item for item in backlog["tranches"] if item["id"] == "VTI-01")
        self.assertEqual(vti01["status"], checkpoint["status"])

        if checkpoint["status"] == "in_progress":
            self.assertTrue(checkpoint["implementation_authority"])
            self.assertTrue(checkpoint["branch_creation_authorized"])
            self.assertTrue(checkpoint["acceptance_package_authorized"])
            production_authorized = checkpoint["production_mutation_authorized"]
            self.assertEqual(backlog["active_contract"]["production_mutation_authorized"], production_authorized)
            self.assertEqual(pointer["bounded_authority"]["production_mutation_authorized"], production_authorized)
            self.assertEqual(registry["vti_01_authority"]["production_mutation_authorized"], production_authorized)
            if production_authorized:
                red = checkpoint["validation"]["acceptance_red"]
                self.assertIsNotNone(red)
                self.assertTrue(red["matching_red_observed"])
                self.assertTrue(backlog["active_contract"]["matching_red_observed"])
                self.assertTrue(registry["vti_01_authority"]["matching_red_observed"])
            else:
                self.assertIsNone(checkpoint["validation"]["acceptance_red"])
            self.assertEqual(backlog["current_item"], "VTI-01")
            self.assertEqual(pointer["active_attempt"]["work_item_id"], "VTI-01")
            self.assertEqual(pointer["active_attempt"]["status"], "in_progress")
            self.assertEqual(registry["active_planning_work"]["work_item"], "VTI-01")
            self.assertEqual(index["current"]["work_item_id"], "VTI-01")
            self.assertEqual(runtime["active_work"]["work_item"], "VTI-01")
        else:
            self.assertFalse(checkpoint["implementation_authority"])
            self.assertTrue(checkpoint["authority_retired"])
            self.assertTrue(checkpoint["completed"])
            self.assertEqual(checkpoint["application_pr"], 415)
            self.assertEqual(checkpoint["application_merge_sha"], merge)
            self.assertEqual(checkpoint["validation"]["final_green"]["head_sha"], "7c377f1add2e00bbadb4007a043fee69709bd923")
            self.assertEqual(checkpoint["validation"]["final_green"]["deterministic_receipt_sha256"], "be8c090d2482898fbcdc8ffc93b93a31b7cb2eae3c8c0e238a221a990f8ce761")
            self.assertEqual(backlog["completed_through"], "VTI-01")
            vti02 = load_json("governance/ai/work-state/VTI-02-attempt-001.json")
            self.assertIn(vti02["status"], {"selected_not_started", "in_progress"})
            self.assertEqual(vti02["application_baseline_sha"], merge)
            self.assertEqual(pointer["active_attempt"]["work_item_id"], "VTI-02")
            self.assertEqual(pointer["active_attempt"]["status"], vti02["status"])
            self.assertEqual(registry["active_planning_work"]["work_item"], "VTI-02")
            self.assertTrue(registry["vti_01_authority"]["retired"])
            self.assertFalse(registry["vti_01_authority"]["implementation_authority"])
            self.assertEqual(index["current"]["work_item_id"], "VTI-02")
            self.assertEqual(runtime["active_work"]["work_item"], "VTI-02")
            self.assertEqual(runtime["application_repository"]["canonical_main"], merge)
            if vti02["status"] == "selected_not_started":
                self.assertIsNone(vti02["implementation_branch"])
                self.assertFalse(vti02["implementation_authority"])
                self.assertFalse(vti02["acceptance_package_authorized"])
                self.assertFalse(vti02["production_mutation_authorized"])
                self.assertTrue(registry["vti_02_authority"]["selected_not_started"])
                self.assertFalse(registry["vti_02_authority"]["implementation_authority"])
            else:
                self.assertEqual(vti02["implementation_branch"], vti02_branch)
                self.assertTrue(vti02["implementation_authority"])
                self.assertTrue(vti02["acceptance_package_authorized"])
                self.assertFalse(vti02["production_mutation_authorized"])
                self.assertFalse(registry["vti_02_authority"]["selected_not_started"])
                self.assertTrue(registry["vti_02_authority"]["implementation_authority"])
                self.assertEqual(registry["vti_02_authority"]["implementation_branch"], vti02_branch)
                self.assertFalse(registry["vti_02_authority"]["production_mutation_authorized"])

        for phrase in (
            "VTI-01 — VTT Ecosystem, Licensing & Capability Matrix",
            "supported, unsupported, conditional or unknown",
            "VTI-02 — Multiversal External Game Projection Contract",
            "Platform selection remains evidence-driven",
        ):
            self.assertIn(phrase, program)

    def test_vti01_scope_keeps_external_mutation_and_vendor_selection_closed(self):
        checkpoint = load_json("governance/ai/work-state/VTI-01-attempt-001.json")
        scope = checkpoint["implementation_scope"]
        for item in (
            "evidence-backed platform identity, hosting, licensing and distribution classification with source provenance",
            "explicit capability states supported, unsupported, conditional or unknown across rules packages, modules/plugins, sheets, compendiums, maps/scenes, automation, APIs/live communication and import/export",
            "deterministic capability-matrix ordering and deterministic receipts independent of supplied platform or evidence ordering",
        ):
            self.assertIn(item, scope["authorized"])
        for item in (
            "vendor selection, ranking, winner recommendation or VTI-09 platform commitment",
            "credential use, external account mutation, provider activation or external synchronization mutation",
            "adapter implementation, canonical game-state mutation, package publication, tester distribution, release or deployment",
        ):
            self.assertIn(item, scope["not_authorized"])

        authority = load_json("governance/ai/runtime/ACTIVE_AUTHORITY_REGISTRY.json")["vti_01_authority"]
        self.assertFalse(authority["vendor_selection_authorized"])
        self.assertFalse(authority["external_account_mutation_authorized"])
        self.assertFalse(authority["credential_use_authorized"])
        self.assertFalse(authority["adapter_implementation_authorized"])
        self.assertFalse(authority["external_sync_mutation_authorized"])
        self.assertFalse(authority["canonical_game_state_mutation_authorized"])
        self.assertFalse(authority["hidden_information_bypass_authorized"])
        self.assertFalse(authority["provider_activation_authorized"])
        self.assertFalse(authority["tester_distribution_authorized"])
        self.assertFalse(authority["release_or_deployment_authorized"])
        self.assertFalse(authority["vti02_plus_authorized"])
        self.assertFalse(authority["sgc01_plus_authorized"])


if __name__ == "__main__":
    unittest.main()
