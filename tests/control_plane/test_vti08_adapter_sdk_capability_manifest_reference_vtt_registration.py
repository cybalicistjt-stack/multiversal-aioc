import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def load_json(path):
    return json.loads((ROOT / path).read_text(encoding="utf-8"))


def load_text(path):
    return (ROOT / path).read_text(encoding="utf-8")


class Vti08AdapterSdkCapabilityManifestReferenceVttRegistrationTests(unittest.TestCase):
    def test_vti08_lifecycle_is_registered_without_unlocking_production_early(self):
        baseline = "692da4f4792426b9c62f6be14db60fc63eb09d6b"
        branch = "integration/vti-08-adapter-sdk-capability-manifest-reference-vtt"
        checkpoint = load_json("governance/ai/work-state/VTI-08-attempt-001.json")
        backlog = load_json("governance/application-planning/virtual-tabletop-interoperability/VTI_PROGRAM_BACKLOG.json")
        pointer = load_json("governance/ai/runtime/CURRENT_WORK_POINTER.json")
        registry = load_json("governance/ai/runtime/ACTIVE_AUTHORITY_REGISTRY.json")
        index = load_json("governance/ai/runtime/ROADMAP_INDEX.json")
        runtime = load_json("governance/repository-health/RUNTIME_STATE_LIFECYCLE_REGISTRY.json")

        self.assertEqual(checkpoint["application_baseline_sha"], baseline)
        self.assertEqual(checkpoint["implementation_branch"], branch)
        self.assertIn(checkpoint["status"], {"in_progress", "ready_for_review", "completed_verified"})
        vti08 = next(item for item in backlog["tranches"] if item["id"] == "VTI-08")
        authority = registry["vti_08_authority"]

        if checkpoint["status"] == "completed_verified":
            self.assertTrue(checkpoint["completed"])
            self.assertTrue(checkpoint["authority_retired"])
            self.assertFalse(checkpoint["implementation_authority"])
            self.assertFalse(checkpoint["branch_creation_authorized"])
            self.assertFalse(checkpoint["acceptance_package_authorized"])
            self.assertFalse(checkpoint["production_mutation_authorized"])
            self.assertEqual(vti08["status"], "completed_verified")
            self.assertTrue(authority["retired"])
            self.assertFalse(authority["implementation_authority"])
            self.assertIn(pointer["active_attempt"]["work_item_id"], {"VTI-08", "VTI-09"})
        else:
            self.assertTrue(checkpoint["implementation_authority"])
            self.assertTrue(checkpoint["branch_creation_authorized"])
            self.assertTrue(checkpoint["acceptance_package_authorized"])
            self.assertEqual(vti08["status"], "in_progress")
            self.assertTrue(vti08["implementation_authority"])
            self.assertEqual(pointer["active_attempt"]["work_item_id"], "VTI-08")
            self.assertEqual(index["current"]["work_item_id"], "VTI-08")
            self.assertEqual(runtime["active_work"]["work_item"], "VTI-08")
            if checkpoint["validation"]["acceptance_red"] is None:
                self.assertFalse(checkpoint["production_mutation_authorized"])
                self.assertFalse(vti08["production_mutation_authorized"])
                self.assertFalse(authority["production_mutation_authorized"])
                self.assertFalse(authority["adapter_sdk_capability_manifest_reference_vtt_authorized"])
                self.assertFalse(authority["matching_red_observed"])

        self.assertEqual(runtime["application_repository"]["canonical_main"], baseline)
        for key in (
            "provider_selection_authorized",
            "provider_specific_schema_authorized",
            "credential_or_external_account_mutation_authorized",
            "live_external_or_canonical_mutation_authorized",
            "durable_persistence_or_migration_authorized",
            "provider_activation_authorized",
            "tester_distribution_authorized",
            "release_or_deployment_authorized",
            "vti09_plus_authorized",
            "sgc01_plus_authorized",
        ):
            self.assertFalse(authority[key])

    def test_vti08_scope_reuses_completed_vti_contracts_and_keeps_reference_vtt_derivative(self):
        checkpoint = load_json("governance/ai/work-state/VTI-08-attempt-001.json")
        scope = checkpoint["implementation_scope"]
        for item in (
            "provider-neutral adapter SDK interfaces that consume the completed VTI-02 through VTI-07 projection, identity, action/receipt and permission-preservation contracts without replacing them",
            "deterministic capability manifests that declare supported, unsupported, conditional or unknown adapter fidelity and force safe downgrade when capability is absent",
            "a deterministic fake/reference VTT that implements the provider-neutral adapter surface entirely as a local test double with no commercial provider dependency",
            "end-to-end acceptance fixtures that exercise canonical projection, request/receipt replay, visibility/permission preservation and capability downgrade through the reference adapter",
        ):
            self.assertIn(item, scope["authorized"])
        for item in (
            "commercial provider selection, ranking, provider-specific schemas or VTI-09 first-platform integration",
            "provider credentials, external accounts, provider network access or live external synchronization mutation",
            "new canonical rules, campaign, spatial, identity, permission or adjudication authority inside the adapter or reference VTT",
            "durable VTI persistence or a new migration before separately authorized persistence work",
            "VTI-09+ or SGC-01+ implementation",
        ):
            self.assertIn(item, scope["not_authorized"])

        program = load_text("governance/application-planning/virtual-tabletop-interoperability/VTI_VIRTUAL_TABLETOP_INTEROPERABILITY_PROGRAM.md")
        self.assertIn("VTI-08 — Adapter SDK, Capability Manifest & Deterministic Reference VTT", program)
        self.assertIn("Platform selection remains evidence-driven", program)


if __name__ == "__main__":
    unittest.main()
