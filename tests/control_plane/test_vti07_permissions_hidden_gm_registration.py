import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def load_json(path):
    return json.loads((ROOT / path).read_text(encoding="utf-8"))


class Vti07PermissionsHiddenGmRegistrationTests(unittest.TestCase):
    def test_vti07_governed_start_is_consistent_across_current_control_plane(self):
        baseline = "1e325045b2fc65d067a5e587f8cde78dcba9f766"
        branch = "integration/vti-07-permissions-hidden-information-gm-authority"
        red_head = "5cb646cd4ea49e4ef82cc13d695c6450336c73ff"
        red_run = 34064038245
        red_receipt = "3c405551b32804277945d4047a99786a2cf5a2dd6d513e0852aae48e8ea94f71"
        checkpoint = load_json("governance/ai/work-state/VTI-07-attempt-001.json")
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

        vti07 = next(item for item in backlog["tranches"] if item["id"] == "VTI-07")
        self.assertEqual(vti07["status"], "in_progress")
        self.assertEqual(vti07["implementation_branch"], branch)
        self.assertTrue(vti07["implementation_authority"])
        self.assertEqual(backlog["active_contract"]["work_item"], "VTI-07")
        self.assertTrue(backlog["active_contract"]["acceptance_package_authorized"])

        self.assertEqual(pointer["active_attempt"]["work_item_id"], "VTI-07")
        self.assertEqual(pointer["active_attempt"]["status"], "in_progress")
        self.assertEqual(pointer["active_attempt"]["implementation_branch"], branch)
        self.assertTrue(pointer["bounded_authority"]["acceptance_package_authorized"])

        authority = registry["vti_07_authority"]
        self.assertFalse(authority["selected_not_started"])
        self.assertTrue(authority["implementation_authority"])
        self.assertEqual(authority["implementation_branch"], branch)
        self.assertTrue(authority["branch_creation_authorized"])
        self.assertTrue(authority["acceptance_package_authorized"])

        self.assertEqual(index["current"]["work_item_id"], "VTI-07")
        self.assertEqual(index["current"]["status"], "in_progress")
        self.assertEqual(index["current"]["implementation_branch"], branch)
        self.assertEqual(runtime["active_work"]["work_item"], "VTI-07")
        self.assertEqual(runtime["active_work"]["state"], "in_progress")
        self.assertEqual(runtime["active_work"]["implementation_branch"], branch)
        self.assertEqual(runtime["application_repository"]["canonical_main"], baseline)

        red = checkpoint["validation"]["acceptance_red"]
        if red is None:
            self.assertFalse(checkpoint["production_mutation_authorized"])
            self.assertFalse(backlog["active_contract"]["production_mutation_authorized"])
            self.assertFalse(pointer["bounded_authority"]["production_mutation_authorized"])
            self.assertFalse(authority["production_mutation_authorized"])
            self.assertFalse(authority["permissions_hidden_gm_authority_authorized"])
            self.assertFalse(index["current"]["production_mutation_authorized"])
            self.assertFalse(runtime["active_work"]["production_mutation_authorized"])
        else:
            self.assertEqual(red["head_sha"], red_head)
            self.assertEqual(red["run_id"], red_run)
            self.assertEqual(red["deterministic_receipt_sha256"], red_receipt)
            self.assertTrue(red["matching_red_observed"])
            self.assertTrue(checkpoint["production_mutation_authorized"])
            self.assertTrue(backlog["active_contract"]["production_mutation_authorized"])
            self.assertTrue(backlog["active_contract"]["matching_red_observed"])
            self.assertTrue(pointer["bounded_authority"]["production_mutation_authorized"])
            self.assertTrue(pointer["bounded_authority"]["matching_red_observed"])
            self.assertTrue(authority["production_mutation_authorized"])
            self.assertTrue(authority["permissions_hidden_gm_authority_authorized"])
            self.assertTrue(authority["matching_red_observed"])
            self.assertTrue(index["current"]["production_mutation_authorized"])
            self.assertTrue(index["current"]["matching_red_observed"])
            self.assertTrue(runtime["active_work"]["production_mutation_authorized"])
            self.assertTrue(runtime["active_work"]["matching_red_observed"])

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
