import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def load_json(path):
    return json.loads((ROOT / path).read_text(encoding="utf-8"))


class Vti07PermissionsHiddenGmRegistrationTests(unittest.TestCase):
    def test_vti07_lifecycle_preserves_governed_start_and_terminal_handoff(self):
        baseline = "1e325045b2fc65d067a5e587f8cde78dcba9f766"
        branch = "integration/vti-07-permissions-hidden-information-gm-authority"
        merge = "692da4f4792426b9c62f6be14db60fc63eb09d6b"
        checkpoint = load_json("governance/ai/work-state/VTI-07-attempt-001.json")
        backlog = load_json("governance/application-planning/virtual-tabletop-interoperability/VTI_PROGRAM_BACKLOG.json")
        pointer = load_json("governance/ai/runtime/CURRENT_WORK_POINTER.json")
        registry = load_json("governance/ai/runtime/ACTIVE_AUTHORITY_REGISTRY.json")
        index = load_json("governance/ai/runtime/ROADMAP_INDEX.json")
        runtime = load_json("governance/repository-health/RUNTIME_STATE_LIFECYCLE_REGISTRY.json")

        self.assertEqual(checkpoint["application_baseline_sha"], baseline)
        self.assertEqual(checkpoint["implementation_branch"], branch)
        self.assertIn(checkpoint["status"], {"in_progress", "ready_for_review", "completed_verified"})
        vti07 = next(item for item in backlog["tranches"] if item["id"] == "VTI-07")
        authority = registry["vti_07_authority"]

        if checkpoint["status"] == "completed_verified":
            self.assertTrue(checkpoint["completed"])
            self.assertTrue(checkpoint["authority_retired"])
            self.assertEqual(checkpoint["application_merge_sha"], merge)
            self.assertFalse(checkpoint["implementation_authority"])
            self.assertFalse(checkpoint["branch_creation_authorized"])
            self.assertFalse(checkpoint["acceptance_package_authorized"])
            self.assertFalse(checkpoint["production_mutation_authorized"])
            self.assertEqual(vti07["status"], "completed_verified")
            self.assertEqual(vti07["application_merge_sha"], merge)
            self.assertFalse(vti07["implementation_authority"])
            self.assertTrue(authority["retired"])
            for key in ("implementation_authority", "branch_creation_authorized", "acceptance_package_authorized", "production_mutation_authorized", "permissions_hidden_gm_authority_authorized"):
                self.assertFalse(authority[key])
            self.assertEqual(pointer["active_attempt"]["work_item_id"], "VTI-08")
            self.assertEqual(pointer["active_attempt"]["status"], "selected_not_started")
            self.assertEqual(index["current"]["work_item_id"], "VTI-08")
            self.assertEqual(runtime["active_work"]["work_item"], "VTI-08")
            self.assertEqual(runtime["application_repository"]["canonical_main"], merge)
        else:
            self.assertTrue(checkpoint["implementation_authority"])
            self.assertTrue(checkpoint["branch_creation_authorized"])
            self.assertTrue(checkpoint["acceptance_package_authorized"])
            self.assertEqual(vti07["status"], "in_progress")
            self.assertTrue(vti07["implementation_authority"])
            self.assertEqual(pointer["active_attempt"]["work_item_id"], "VTI-07")
            self.assertEqual(index["current"]["work_item_id"], "VTI-07")
            self.assertEqual(runtime["active_work"]["work_item"], "VTI-07")

        for key in (
            "provider_specific_schema_authorized",
            "credential_or_external_account_mutation_authorized",
            "adapter_implementation_authorized",
            "live_external_or_canonical_mutation_authorized",
            "durable_persistence_or_migration_authorized",
            "provider_activation_authorized",
            "tester_distribution_authorized",
            "release_or_deployment_authorized",
            "vti08_plus_authorized",
            "sgc01_plus_authorized",
        ):
            self.assertFalse(authority[key])

    def test_vti07_scope_consumes_canonical_authorization_and_fails_closed(self):
        checkpoint = load_json("governance/ai/work-state/VTI-07-attempt-001.json")
        scope = checkpoint["implementation_scope"]
        for item in (
            "provider-neutral preservation of canonical Multiversal ownership, consent, visibility and GM-authority decisions across derivative external VTT clients",
            "fail-closed projection of hidden counts, hidden content, redacted identities and GM-only material with no inference channel",
            "deterministic authorization-presentation envelopes that consume canonical Multiversal authorization decisions without creating a parallel permission engine",
            "capability-aware downgrade to redacted or unsupported presentation when a target cannot safely preserve canonical hidden-information semantics",
        ):
            self.assertIn(item, scope["authorized"])
        for item in (
            "a new or parallel permission, ownership, consent, visibility, adjudication or hidden-state authority engine",
            "provider-specific schemas, vendor selection/ranking or VTI-09 platform commitment",
            "credentials, external account mutation, adapter implementation, live external synchronization mutation or canonical game-state mutation",
            "durable VTI persistence or a new migration before separately authorized persistence work",
            "VTI-08 adapter-SDK behavior or any VTI-08+ implementation",
        ):
            self.assertIn(item, scope["not_authorized"])


if __name__ == "__main__":
    unittest.main()
