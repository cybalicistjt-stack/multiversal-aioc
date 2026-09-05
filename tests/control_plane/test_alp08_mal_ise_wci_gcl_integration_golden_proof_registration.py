import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def load_json(path):
    return json.loads((ROOT / path).read_text(encoding="utf-8"))


def load_text(path):
    return (ROOT / path).read_text(encoding="utf-8")


class Alp08MalIseWciGclIntegrationGoldenProofRegistrationTests(unittest.TestCase):
    def test_alp08_governed_start_or_closeout_is_consistent(self):
        baseline = "773b9bcfbdc549e53e51dcedaae83b450a74c8fc"
        branch = "integration/alp-08-mal-ise-wci-gcl-integration-golden-learning-recognition-proof"
        checkpoint = load_json("governance/ai/work-state/ALP-08-attempt-001.json")
        backlog = load_json("governance/application-planning/achievements-learning-practice/ALP_PROGRAM_BACKLOG.json")
        pointer = load_json("governance/ai/runtime/CURRENT_WORK_POINTER.json")
        registry = load_json("governance/ai/runtime/ACTIVE_AUTHORITY_REGISTRY.json")
        index = load_json("governance/ai/runtime/ROADMAP_INDEX.json")
        runtime = load_json("governance/repository-health/RUNTIME_STATE_LIFECYCLE_REGISTRY.json")
        program = load_text("governance/application-planning/achievements-learning-practice/ALP_ACHIEVEMENTS_LEARNING_PRACTICE_PROGRAM.md")

        self.assertEqual(checkpoint["work_item_id"], "ALP-08")
        self.assertEqual(checkpoint["application_baseline_sha"], baseline)
        self.assertIn(checkpoint["status"], {"in_progress", "completed_verified"})
        alp08 = next(item for item in backlog["tranches"] if item["id"] == "ALP-08")
        self.assertEqual(alp08["status"], checkpoint["status"])

        if checkpoint["status"] == "in_progress":
            production_authorized = checkpoint["production_mutation_authorized"]
            self.assertTrue(checkpoint["implementation_authority"])
            self.assertEqual(checkpoint["implementation_branch"], branch)
            self.assertTrue(checkpoint["branch_creation_authorized"])
            self.assertTrue(checkpoint["acceptance_package_authorized"])
            self.assertEqual(backlog["completed_through"], "ALP-07")
            self.assertEqual(backlog["current_item"], "ALP-08")
            self.assertEqual(pointer["active_attempt"]["work_item_id"], "ALP-08")
            self.assertEqual(pointer["active_attempt"]["status"], "in_progress")
            self.assertEqual(pointer["active_attempt"]["implementation_branch"], branch)
            self.assertTrue(pointer["active_attempt"]["implementation_authority"])
            self.assertEqual(pointer["bounded_authority"]["production_mutation_authorized"], production_authorized)
            self.assertEqual(registry["active_planning_work"]["work_item"], "ALP-08")
            self.assertEqual(registry["active_planning_work"]["state"], "in_progress")
            self.assertEqual(registry["alp_08_authority"]["production_mutation_authorized"], production_authorized)
            self.assertEqual(index["current"]["work_item_id"], "ALP-08")
            self.assertEqual(index["current"]["status"], "in_progress")
            self.assertEqual(runtime["active_work"]["work_item"], "ALP-08")
            self.assertEqual(runtime["active_work"]["state"], "in_progress")
            if production_authorized:
                self.assertIsNotNone(checkpoint["validation"]["acceptance_red"])
                self.assertTrue(backlog["active_contract"]["matching_red_observed"])
                self.assertTrue(registry["alp_08_authority"]["matching_red_observed"])
            else:
                self.assertIsNone(checkpoint["validation"]["acceptance_red"])
                self.assertFalse(backlog["active_contract"]["matching_red_observed"])
                self.assertFalse(registry["alp_08_authority"]["matching_red_observed"])
        else:
            self.assertFalse(checkpoint["implementation_authority"])
            self.assertTrue(checkpoint["authority_retired"])
            self.assertTrue(checkpoint["completed"])
            self.assertEqual(backlog["completed_through"], "ALP-08")
            vti01 = load_json("governance/ai/work-state/VTI-01-attempt-001.json")
            self.assertEqual(pointer["active_attempt"]["work_item_id"], "VTI-01")
            self.assertIn(vti01["status"], {"selected_not_started", "in_progress"})
            self.assertEqual(pointer["active_attempt"]["status"], vti01["status"])
            if vti01["status"] == "selected_not_started":
                self.assertIsNone(pointer["active_attempt"]["implementation_branch"])
                self.assertFalse(pointer["active_attempt"]["implementation_authority"])
            else:
                self.assertEqual(pointer["active_attempt"]["implementation_branch"], "integration/vti-01-vtt-ecosystem-licensing-capability-matrix")
                self.assertTrue(pointer["active_attempt"]["implementation_authority"])
                production_authorized = vti01["production_mutation_authorized"]
                self.assertEqual(pointer["bounded_authority"]["production_mutation_authorized"], production_authorized)
                self.assertEqual(registry["vti_01_authority"]["production_mutation_authorized"], production_authorized)
                if production_authorized:
                    self.assertIsNotNone(vti01["validation"]["acceptance_red"])
                    self.assertTrue(registry["vti_01_authority"]["matching_red_observed"])
                else:
                    self.assertIsNone(vti01["validation"]["acceptance_red"])

        for phrase in (
            "ALP-08 — MAL/ISE/WCI/GCL Integration & Golden Learning/Recognition Proof",
            "MAL, ISE, WCI and GCL",
            "golden learning proof",
            "golden recognition proof",
            "hidden inventory and hidden cardinality are never inferred",
            "migration `0022`",
            "VTI-01+",
        ):
            self.assertIn(phrase, program)

    def test_alp08_scope_preserves_owner_system_boundaries(self):
        checkpoint = load_json("governance/ai/work-state/ALP-08-attempt-001.json")
        scope = checkpoint["implementation_scope"]
        for item in (
            "explicit MAL, ISE, WCI and GCL integration references with stable owner-system identity, source work-item identity, source object identity and provenance",
            "golden learning-proof assembly from explicit authorized learning, practice, rehearsal or project-evidence references with satisfied, unsatisfied or unknown state preserved",
            "golden recognition-proof assembly from explicit authorized achievement or recognition references with stable identity, subject, provenance and supplied order metadata preserved",
            "deterministic ordering and deterministic receipts independent of supplied integration-reference ordering",
        ):
            self.assertIn(item, scope["authorized"])
        for item in (
            "direct MAL, ISE, WCI or GCL mutation, command execution, content acquisition or owner-state creation",
            "achievement awarding, completion mutation, recognition creation by implication or mechanical reward commit",
            "hidden or unauthorized evidence, event, recognition, owner-state or cardinality inference",
            "durable ALP persistence or migration 0022",
            "GCL-13+ implementation, VTI-01+ implementation, provider activation, tester distribution, release or deployment",
        ):
            self.assertIn(item, scope["not_authorized"])

    def test_alp08_registry_keeps_mutating_authorities_closed(self):
        authority = load_json("governance/ai/runtime/ACTIVE_AUTHORITY_REGISTRY.json")["alp_08_authority"]
        self.assertFalse(authority["owner_mutation_authorized"])
        self.assertFalse(authority["mal_mutation_authorized"])
        self.assertFalse(authority["ise_mutation_authorized"])
        self.assertFalse(authority["wci_mutation_authorized"])
        self.assertFalse(authority["gcl_mutation_authorized"])
        self.assertFalse(authority["golden_proof_owner_mutation_authorized"])
        self.assertFalse(authority["achievement_award_authorized"])
        self.assertFalse(authority["reward_commit_authorized"])
        self.assertFalse(authority["xp_or_advancement_grant_authorized"])
        self.assertFalse(authority["title_or_reputation_grant_authorized"])
        self.assertFalse(authority["hidden_evidence_inference_authorized"])
        self.assertFalse(authority["durable_persistence_authorized"])
        self.assertFalse(authority["migration_0022_authorized"])
        self.assertFalse(authority["vti01_plus_authorized"])


if __name__ == "__main__":
    unittest.main()
