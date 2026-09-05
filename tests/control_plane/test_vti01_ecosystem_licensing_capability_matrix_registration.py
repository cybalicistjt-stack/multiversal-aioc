import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def load_json(path):
    return json.loads((ROOT / path).read_text(encoding="utf-8"))


def load_text(path):
    return (ROOT / path).read_text(encoding="utf-8")


class Vti01EcosystemLicensingCapabilityMatrixRegistrationTests(unittest.TestCase):
    def test_vti01_governed_start_is_consistent(self):
        baseline = "e61109affe9d662e6da6eb214c1acc870079c1a7"
        branch = "integration/vti-01-vtt-ecosystem-licensing-capability-matrix"
        checkpoint = load_json("governance/ai/work-state/VTI-01-attempt-001.json")
        backlog = load_json("governance/application-planning/virtual-tabletop-interoperability/VTI_PROGRAM_BACKLOG.json")
        pointer = load_json("governance/ai/runtime/CURRENT_WORK_POINTER.json")
        registry = load_json("governance/ai/runtime/ACTIVE_AUTHORITY_REGISTRY.json")
        index = load_json("governance/ai/runtime/ROADMAP_INDEX.json")
        runtime = load_json("governance/repository-health/RUNTIME_STATE_LIFECYCLE_REGISTRY.json")
        program = load_text("governance/application-planning/virtual-tabletop-interoperability/VTI_VIRTUAL_TABLETOP_INTEROPERABILITY_PROGRAM.md")

        self.assertEqual(checkpoint["work_item_id"], "VTI-01")
        self.assertEqual(checkpoint["application_baseline_sha"], baseline)
        self.assertEqual(checkpoint["status"], "in_progress")
        self.assertTrue(checkpoint["implementation_authority"])
        self.assertEqual(checkpoint["implementation_branch"], branch)
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
            self.assertEqual(backlog["active_contract"]["matching_red_head"], red["head_sha"])
            self.assertEqual(backlog["active_contract"]["matching_red_run"], red["run_id"])
            self.assertEqual(backlog["active_contract"]["matching_red_receipt_sha256"], red["deterministic_receipt_sha256"])
            self.assertEqual(registry["vti_01_authority"]["matching_red_head"], red["head_sha"])
            self.assertEqual(registry["vti_01_authority"]["matching_red_run"], red["run_id"])
            self.assertEqual(registry["vti_01_authority"]["matching_red_receipt_sha256"], red["deterministic_receipt_sha256"])
        else:
            self.assertIsNone(checkpoint["validation"]["acceptance_red"])
            self.assertFalse(backlog["active_contract"]["matching_red_observed"])
            self.assertFalse(registry["vti_01_authority"]["matching_red_observed"])

        vti01 = next(item for item in backlog["tranches"] if item["id"] == "VTI-01")
        self.assertEqual(vti01["status"], "in_progress")
        self.assertEqual(vti01["implementation_branch"], branch)
        self.assertEqual(backlog["current_item"], "VTI-01")

        self.assertEqual(pointer["active_attempt"]["work_item_id"], "VTI-01")
        self.assertEqual(pointer["active_attempt"]["status"], "in_progress")
        self.assertEqual(pointer["active_attempt"]["implementation_branch"], branch)
        self.assertTrue(pointer["active_attempt"]["implementation_authority"])

        self.assertEqual(registry["active_planning_work"]["work_item"], "VTI-01")
        self.assertEqual(registry["active_planning_work"]["state"], "in_progress")
        self.assertTrue(registry["vti_01_authority"]["implementation_authority"])

        self.assertEqual(index["current"]["work_item_id"], "VTI-01")
        self.assertEqual(index["current"]["status"], "in_progress")
        self.assertEqual(runtime["active_work"]["work_item"], "VTI-01")
        self.assertEqual(runtime["active_work"]["state"], "in_progress")
        self.assertEqual(runtime["application_repository"]["active_validation_family_state"], "VTI01_in_progress_acceptance_only")

        for phrase in (
            "VTI-01 — VTT Ecosystem, Licensing & Capability Matrix",
            "evidence-backed",
            "supported, unsupported, conditional or unknown",
            "Platform selection remains evidence-driven and is deferred to VTI-09",
            "No vendor selection",
            "VTI-02+ and SGC-01+ remain unauthorized",
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
