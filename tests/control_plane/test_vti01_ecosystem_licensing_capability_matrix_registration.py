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
        baseline = "e61109affe9d662e6da6eb214c1acc870079c1a7"
        merge = "027fad06d0bac3a20d56f0cc2a674581662cd1b9"
        checkpoint = load_json("governance/ai/work-state/VTI-01-attempt-001.json")
        backlog = load_json("governance/application-planning/virtual-tabletop-interoperability/VTI_PROGRAM_BACKLOG.json")
        pointer = load_json("governance/ai/runtime/CURRENT_WORK_POINTER.json")
        registry = load_json("governance/ai/runtime/ACTIVE_AUTHORITY_REGISTRY.json")
        index = load_json("governance/ai/runtime/ROADMAP_INDEX.json")
        runtime = load_json("governance/repository-health/RUNTIME_STATE_LIFECYCLE_REGISTRY.json")
        program = load_text("governance/application-planning/virtual-tabletop-interoperability/VTI_VIRTUAL_TABLETOP_INTEROPERABILITY_PROGRAM.md")

        self.assertEqual(checkpoint["work_item_id"], "VTI-01")
        self.assertEqual(checkpoint["status"], "completed_verified")
        self.assertEqual(checkpoint["application_baseline_sha"], baseline)
        self.assertEqual(checkpoint["application_merge_sha"], merge)
        self.assertFalse(checkpoint["implementation_authority"])
        self.assertTrue(checkpoint["authority_retired"])
        self.assertTrue(checkpoint["completed"])
        self.assertEqual(checkpoint["application_pr"], 415)
        self.assertEqual(checkpoint["validation"]["final_green"]["head_sha"], "7c377f1add2e00bbadb4007a043fee69709bd923")
        self.assertEqual(checkpoint["validation"]["final_green"]["deterministic_receipt_sha256"], "be8c090d2482898fbcdc8ffc93b93a31b7cb2eae3c8c0e238a221a990f8ce761")

        vti01 = next(item for item in backlog["tranches"] if item["id"] == "VTI-01")
        self.assertEqual(vti01["status"], "completed_verified")
        self.assertFalse(vti01["implementation_authority"])
        self.assertTrue(registry["vti_01_authority"]["retired"])
        self.assertFalse(registry["vti_01_authority"]["implementation_authority"])

        # The frozen VTI-01 regression follows the registered active successor rather than pinning the program to VTI-02 forever.
        current = backlog["current_item"]
        self.assertEqual(current, pointer["active_attempt"]["work_item_id"])
        self.assertEqual(current, registry["active_planning_work"]["work_item"])
        self.assertEqual(current, index["current"]["work_item_id"])
        self.assertEqual(current, runtime["active_work"]["work_item"])
        self.assertEqual(runtime["application_repository"]["canonical_main"], pointer["active_attempt"]["application_baseline_sha"])
        self.assertIn(current, {"VTI-02", "VTI-03"})

        if current == "VTI-02":
            vti02 = load_json("governance/ai/work-state/VTI-02-attempt-001.json")
            self.assertIn(vti02["status"], {"selected_not_started", "in_progress"})
            self.assertEqual(vti02["application_baseline_sha"], merge)
        else:
            vti02 = load_json("governance/ai/work-state/VTI-02-attempt-001.json")
            vti03 = load_json("governance/ai/work-state/VTI-03-attempt-001.json")
            self.assertEqual(vti02["status"], "completed_verified")
            self.assertTrue(vti02["authority_retired"])
            self.assertEqual(vti03["status"], "selected_not_started")
            self.assertFalse(vti03["implementation_authority"])
            self.assertIsNone(vti03["implementation_branch"])
            self.assertTrue(registry["vti_02_authority"]["retired"])
            self.assertTrue(registry["vti_03_authority"]["selected_not_started"])

        for phrase in (
            "VTI-01 — VTT Ecosystem, Licensing & Capability Matrix",
            "supported, unsupported, conditional or unknown",
            "VTI-02 — Multiversal External Game Projection Contract",
            "VTI-03 — Stable Identity, Versioning & Synchronization",
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

        authority = load_json("governance/ai/runtime/ACTIVE_AUTHORITY_REGISTRY.json")["vti_01_authority"]
        for key in (
            "vendor_selection_authorized",
            "external_account_mutation_authorized",
            "credential_use_authorized",
            "adapter_implementation_authorized",
            "external_sync_mutation_authorized",
            "canonical_game_state_mutation_authorized",
            "hidden_information_bypass_authorized",
            "provider_activation_authorized",
            "tester_distribution_authorized",
            "release_or_deployment_authorized",
            "vti02_plus_authorized",
            "sgc01_plus_authorized",
        ):
            self.assertFalse(authority[key])


if __name__ == "__main__":
    unittest.main()
