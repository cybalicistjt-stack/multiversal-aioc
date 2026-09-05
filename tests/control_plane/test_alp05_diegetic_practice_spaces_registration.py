import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def load_json(path):
    return json.loads((ROOT / path).read_text(encoding="utf-8"))


def load_text(path):
    return (ROOT / path).read_text(encoding="utf-8")


class Alp05DiegeticPracticeSpacesRegistrationTests(unittest.TestCase):
    def test_alp05_governed_start_or_closeout_is_consistent(self):
        baseline = "788a8025caf8046edfeddcbf238cce972a4c5378"
        merge = "402aa6d91795d6e75be64c106aa122b0b79cb872"
        validated_head = "359ee958759d4be86cc347e463c28a3ff565d150"
        green_receipt = "fedc7e7a6a824acf582b64a095b64a42b7bae19d1a4590f3a4ee4e4b02c81288"
        checkpoint = load_json("governance/ai/work-state/ALP-05-attempt-001.json")
        alp06_checkpoint = load_json("governance/ai/work-state/ALP-06-attempt-001.json")
        backlog = load_json("governance/application-planning/achievements-learning-practice/ALP_PROGRAM_BACKLOG.json")
        pointer = load_json("governance/ai/runtime/CURRENT_WORK_POINTER.json")
        registry = load_json("governance/ai/runtime/ACTIVE_AUTHORITY_REGISTRY.json")
        index = load_json("governance/ai/runtime/ROADMAP_INDEX.json")
        runtime = load_json("governance/repository-health/RUNTIME_STATE_LIFECYCLE_REGISTRY.json")
        program = load_text("governance/application-planning/achievements-learning-practice/ALP_ACHIEVEMENTS_LEARNING_PRACTICE_PROGRAM.md")

        self.assertEqual(checkpoint["work_item_id"], "ALP-05")
        self.assertEqual(checkpoint["application_baseline_sha"], baseline)
        self.assertIn(checkpoint["status"], {"in_progress", "completed_verified"})
        alp05 = next(item for item in backlog["tranches"] if item["id"] == "ALP-05")
        self.assertEqual(alp05["status"], checkpoint["status"])

        if checkpoint["status"] == "in_progress":
            branch = "integration/alp-05-diegetic-practice-spaces-training-scenes-simulations"
            production_authorized = checkpoint["production_mutation_authorized"]
            self.assertTrue(checkpoint["implementation_authority"])
            self.assertEqual(checkpoint["implementation_branch"], branch)
            self.assertTrue(checkpoint["branch_creation_authorized"])
            self.assertTrue(checkpoint["acceptance_package_authorized"])
            self.assertEqual(backlog["active_contract"]["production_mutation_authorized"], production_authorized)
            self.assertEqual(pointer["bounded_authority"]["production_mutation_authorized"], production_authorized)
            self.assertEqual(registry["alp_05_authority"]["production_mutation_authorized"], production_authorized)
            if production_authorized:
                self.assertIsNotNone(checkpoint["validation"]["acceptance_red"])
                self.assertTrue(backlog["active_contract"]["matching_red_observed"])
                self.assertEqual(backlog["active_contract"]["matching_red_receipt_sha256"], checkpoint["validation"]["acceptance_red"]["deterministic_receipt_sha256"])
            else:
                self.assertIsNone(checkpoint["validation"]["acceptance_red"])
            self.assertEqual(backlog["completed_through"], "ALP-04")
            self.assertEqual(backlog["current_item"], "ALP-05")
            self.assertEqual(pointer["active_attempt"]["work_item_id"], "ALP-05")
            self.assertEqual(pointer["active_attempt"]["status"], "in_progress")
            self.assertEqual(pointer["active_attempt"]["implementation_branch"], branch)
            self.assertTrue(pointer["active_attempt"]["implementation_authority"])
            self.assertEqual(registry["active_planning_work"]["state"], "in_progress")
            self.assertEqual(index["current"]["status"], "in_progress")
            self.assertEqual(runtime["active_work"]["state"], "in_progress")
        else:
            self.assertFalse(checkpoint["implementation_authority"])
            self.assertTrue(checkpoint["authority_retired"])
            self.assertEqual(checkpoint["application_pr"], 411)
            self.assertEqual(checkpoint["application_merge_sha"], merge)
            self.assertEqual(checkpoint["validation"]["final_green"]["head_sha"], validated_head)
            self.assertEqual(checkpoint["validation"]["final_green"]["deterministic_receipt_sha256"], green_receipt)
            self.assertIn(alp06_checkpoint["status"], {"selected_not_started", "in_progress", "completed_verified"})
            if alp06_checkpoint["status"] in {"selected_not_started", "in_progress"}:
                self.assertEqual(backlog["completed_through"], "ALP-05")
                self.assertEqual(backlog["current_item"], "ALP-06")
                self.assertEqual(pointer["active_attempt"]["work_item_id"], "ALP-06")
                self.assertEqual(pointer["active_attempt"]["status"], alp06_checkpoint["status"])
                self.assertEqual(registry["active_planning_work"]["work_item"], "ALP-06")
                self.assertEqual(registry["active_planning_work"]["state"], alp06_checkpoint["status"])
                self.assertEqual(index["current"]["work_item_id"], "ALP-06")
                self.assertEqual(runtime["active_work"]["work_item"], "ALP-06")
            else:
                alp07 = load_json("governance/ai/work-state/ALP-07-attempt-001.json")
                self.assertEqual(alp07["application_baseline_sha"], alp06_checkpoint["application_merge_sha"])
                if alp07["status"] != "completed_verified":
                    self.assertEqual(backlog["completed_through"], "ALP-06")
                    self.assertEqual(backlog["current_item"], "ALP-07")
                    self.assertEqual(pointer["active_attempt"]["work_item_id"], "ALP-07")
                    self.assertEqual(pointer["active_attempt"]["status"], alp07["status"])
                    self.assertEqual(registry["active_planning_work"]["work_item"], "ALP-07")
                    self.assertEqual(index["current"]["work_item_id"], "ALP-07")
                    self.assertEqual(runtime["active_work"]["work_item"], "ALP-07")
                else:
                    alp08 = load_json("governance/ai/work-state/ALP-08-attempt-001.json")
                    self.assertEqual(alp08["application_baseline_sha"], alp07["application_merge_sha"])
                    if alp08["status"] != "completed_verified":
                        self.assertEqual(backlog["completed_through"], "ALP-07")
                        self.assertEqual(backlog["current_item"], "ALP-08")
                        self.assertEqual(pointer["active_attempt"]["work_item_id"], "ALP-08")
                        self.assertEqual(pointer["active_attempt"]["status"], alp08["status"])
                        self.assertEqual(registry["active_planning_work"]["work_item"], "ALP-08")
                        self.assertEqual(index["current"]["work_item_id"], "ALP-08")
                        self.assertEqual(runtime["active_work"]["work_item"], "ALP-08")
                    else:
                        vti01 = load_json("governance/ai/work-state/VTI-01-attempt-001.json")
                        self.assertEqual(alp08["application_merge_sha"], "e61109affe9d662e6da6eb214c1acc870079c1a7")
                        self.assertEqual(vti01["application_baseline_sha"], alp08["application_merge_sha"])
                        self.assertEqual(backlog["completed_through"], "ALP-08")
                        self.assertIsNone(backlog["current_item"])
                        self.assertEqual(pointer["active_attempt"]["work_item_id"], "VTI-01")
                        self.assertEqual(pointer["active_attempt"]["status"], "selected_not_started")
                        self.assertEqual(registry["active_planning_work"]["work_item"], "VTI-01")
                        self.assertEqual(index["current"]["work_item_id"], "VTI-01")
                        self.assertEqual(runtime["active_work"]["work_item"], "VTI-01")

        for phrase in (
            "ALP-05 — Diegetic Practice Spaces, Training Scenes & Simulations",
            "optional practice-space contracts",
            "training scenes",
            "simulations",
            "Practice participation remains optional",
            "Character Progression",
            "Projects",
            "World/Scene",
            "GCL",
            "ISE",
            "MAL",
            "migration `0022`",
        ):
            self.assertIn(phrase, program)

    def test_alp05_scope_keeps_practice_non_mutating_and_optional(self):
        checkpoint = load_json("governance/ai/work-state/ALP-05-attempt-001.json")
        scope = checkpoint["implementation_scope"]
        boundary = checkpoint["authority_boundary"]
        self.assertIn("explicit practice-space identity, kind, scope, author and provenance", scope["authorized"])
        self.assertIn("optional participation policy with no universal gating", scope["authorized"])
        self.assertIn("read-only links to Character Progression, Projects, World/Scene, GCL, ISE and MAL owner objects", scope["authorized"])
        self.assertIn("automatic XP, advancement, capability or reward grants from practice participation", scope["not_authorized"])
        self.assertIn("hidden or unauthorized evidence inference", scope["not_authorized"])
        self.assertIn("durable ALP persistence or migration 0022", scope["not_authorized"])
        self.assertFalse(boundary["alp06_plus_authorized"])
        self.assertFalse(boundary["tester_distribution_authorized"])
        self.assertFalse(boundary["release_or_deployment_authorized"])

    def test_alp05_closeout_evidence_and_successor_boundary_are_sealed(self):
        checkpoint = load_json("governance/ai/work-state/ALP-05-attempt-001.json")
        alp06 = load_json("governance/ai/work-state/ALP-06-attempt-001.json")
        supplement = load_text("governance/application-planning/APPLICATION_IMPLEMENTATION_ROADMAP_ALP05_CLOSEOUT_2026-09-04.md")

        if checkpoint["status"] != "completed_verified":
            self.skipTest("ALP-05 closeout assertions apply after verified application merge")

        self.assertIn(alp06["status"], {"selected_not_started", "in_progress", "completed_verified"})
        if alp06["status"] == "selected_not_started":
            self.assertIsNone(alp06["implementation_branch"])
            self.assertFalse(alp06["implementation_authority"])
            self.assertFalse(alp06["branch_creation_authorized"])
            self.assertFalse(alp06["acceptance_package_authorized"])
            self.assertFalse(alp06["production_mutation_authorized"])
        elif alp06["status"] == "in_progress":
            self.assertEqual(alp06["implementation_branch"], "integration/alp-06-rehearsal-retry-safe-failure-training-project-integration")
            self.assertTrue(alp06["implementation_authority"])
            self.assertTrue(alp06["branch_creation_authorized"])
            self.assertTrue(alp06["acceptance_package_authorized"])
        else:
            self.assertFalse(alp06["implementation_authority"])
            self.assertTrue(alp06["authority_retired"])
        for token in (
            "11cc4da854fe11f90cd95f8b6cc0b2f5eb91077c",
            "33899883790",
            "e6c47a4c749d8caa4b3a22dafec5e52acb2c6c66876ac8b94e7a1ad8fb291ba2",
            "359ee958759d4be86cc347e463c28a3ff565d150",
            "33900659543",
            "fedc7e7a6a824acf582b64a095b64a42b7bae19d1a4590f3a4ee4e4b02c81288",
            "402aa6d91795d6e75be64c106aa122b0b79cb872",
            "ALP-06",
            "selected_not_started",
        ):
            self.assertIn(token, supplement)


if __name__ == "__main__":
    unittest.main()
