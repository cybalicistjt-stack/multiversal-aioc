import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def load_json(path):
    return json.loads((ROOT / path).read_text(encoding="utf-8"))


def load_text(path):
    return (ROOT / path).read_text(encoding="utf-8")


class Alp06RehearsalRetrySafeFailureTrainingProjectRegistrationTests(unittest.TestCase):
    def test_alp06_remains_completed_while_successor_may_advance(self):
        baseline = "402aa6d91795d6e75be64c106aa122b0b79cb872"
        merge_sha = "b59e47dfe5754ad22cfdbe2082585d265335da51"
        checkpoint = load_json("governance/ai/work-state/ALP-06-attempt-001.json")
        alp07 = load_json("governance/ai/work-state/ALP-07-attempt-001.json")
        backlog = load_json("governance/application-planning/achievements-learning-practice/ALP_PROGRAM_BACKLOG.json")
        pointer = load_json("governance/ai/runtime/CURRENT_WORK_POINTER.json")
        registry = load_json("governance/ai/runtime/ACTIVE_AUTHORITY_REGISTRY.json")
        index = load_json("governance/ai/runtime/ROADMAP_INDEX.json")
        runtime = load_json("governance/repository-health/RUNTIME_STATE_LIFECYCLE_REGISTRY.json")
        program = load_text("governance/application-planning/achievements-learning-practice/ALP_ACHIEVEMENTS_LEARNING_PRACTICE_PROGRAM.md")

        self.assertEqual(checkpoint["work_item_id"], "ALP-06")
        self.assertEqual(checkpoint["status"], "completed_verified")
        self.assertEqual(checkpoint["application_baseline_sha"], baseline)
        self.assertEqual(checkpoint["application_pr"], 412)
        self.assertEqual(checkpoint["application_merge_sha"], merge_sha)
        self.assertFalse(checkpoint["implementation_authority"])
        self.assertTrue(checkpoint["authority_retired"])
        self.assertTrue(checkpoint["completed"])
        self.assertEqual(checkpoint["validation"]["acceptance_red"]["head_sha"], "7e9078a8f1d6a2a906b3f30842259ebbc7ff7ea2")
        self.assertEqual(checkpoint["validation"]["acceptance_red"]["run_id"], 33906923458)
        self.assertEqual(checkpoint["validation"]["acceptance_red"]["deterministic_receipt_sha256"], "d8d9d18a26fd83567b4e17cc02df777accdd9247222864cbbfa696d28e1d2338")
        self.assertEqual(checkpoint["validation"]["final_green"]["head_sha"], "0b895ee21ea7585527b3acdb309bd11b05b5bea3")
        self.assertEqual(checkpoint["validation"]["final_green"]["run_id"], 33907481266)
        self.assertEqual(checkpoint["validation"]["final_green"]["deterministic_receipt_sha256"], "5d28a9e9ca42ee65bb9c37f7c1425242b3f2ce56f24cdec0d89c5161c401cde3")
        self.assertEqual(checkpoint["convergence_control"]["application_feature_repair_cycles"], 0)
        self.assertEqual(checkpoint["convergence_control"]["unrelated_historical_validation_jobs_observed"], 0)
        self.assertEqual(checkpoint["convergence_control"]["reruns_without_changed_evidence"], 0)
        self.assertEqual(checkpoint["convergence_control"]["post_merge_stale_pointer_incidents"], 0)

        alp06 = next(item for item in backlog["tranches"] if item["id"] == "ALP-06")
        self.assertEqual(alp06["status"], "completed_verified")
        self.assertFalse(alp06["implementation_authority"])
        self.assertEqual(alp06["application_merge_sha"], merge_sha)
        self.assertEqual(backlog["completed_alp06"]["application_merge_sha"], merge_sha)
        self.assertEqual(backlog["completed_alp06"]["historical_profile_fanout"], 0)

        self.assertIn(alp07["status"], {"selected_not_started", "in_progress", "completed_verified"})
        self.assertEqual(alp07["application_baseline_sha"], merge_sha)
        if alp07["status"] != "completed_verified":
            self.assertEqual(backlog["completed_through"], "ALP-06")
            self.assertEqual(backlog["current_item"], "ALP-07")
            self.assertEqual(pointer["active_attempt"]["work_item_id"], "ALP-07")
            self.assertEqual(pointer["active_attempt"]["status"], alp07["status"])
            self.assertEqual(registry["active_planning_work"]["work_item"], "ALP-07")
            self.assertEqual(registry["active_planning_work"]["state"], alp07["status"])
            self.assertEqual(index["current"]["work_item_id"], "ALP-07")
            self.assertEqual(index["current"]["status"], alp07["status"])
            self.assertEqual(runtime["active_work"]["work_item"], "ALP-07")
            self.assertEqual(runtime["active_work"]["state"], alp07["status"])
            self.assertEqual(runtime["application_repository"]["canonical_main"], merge_sha)
        else:
            self.assertEqual(backlog["completed_through"], "ALP-07")
            self.assertEqual(backlog["current_item"], "ALP-08")
            self.assertEqual(pointer["active_attempt"]["work_item_id"], "ALP-08")
            self.assertEqual(pointer["active_attempt"]["status"], "selected_not_started")
            self.assertEqual(registry["active_planning_work"]["work_item"], "ALP-08")
            self.assertEqual(registry["active_planning_work"]["state"], "selected_not_started")
            self.assertEqual(index["current"]["work_item_id"], "ALP-08")
            self.assertEqual(runtime["active_work"]["work_item"], "ALP-08")

        self.assertFalse(registry["alp_06_authority"]["implementation_authority"])
        self.assertTrue(registry["alp_06_authority"]["retired"])
        self.assertEqual(registry["alp_06_authority"]["application_merge_sha"], merge_sha)

        for phrase in (
            "ALP-06 — Rehearsal, Retry, Safe Failure & Training/Project Integration",
            "rehearsal attempts",
            "retry lineage",
            "Safe failure",
            "practice_training_marker",
            "project_learning_evidence",
            "Character Progression",
            "Projects",
            "World/Scene",
            "GCL",
            "ISE",
            "MAL",
            "migration `0022`",
        ):
            self.assertIn(phrase, program)

    def test_alp06_closeout_supplement_seals_exact_evidence(self):
        supplement = load_text("governance/application-planning/APPLICATION_IMPLEMENTATION_ROADMAP_ALP06_CLOSEOUT_2026-09-04.md")
        for marker in (
            "ALP-06 Closeout Supplement",
            "7e9078a8f1d6a2a906b3f30842259ebbc7ff7ea2",
            "33906923458",
            "d8d9d18a26fd83567b4e17cc02df777accdd9247222864cbbfa696d28e1d2338",
            "0b895ee21ea7585527b3acdb309bd11b05b5bea3",
            "33907481266",
            "5d28a9e9ca42ee65bb9c37f7c1425242b3f2ce56f24cdec0d89c5161c401cde3",
            "b59e47dfe5754ad22cfdbe2082585d265335da51",
            "ALP-07",
            "selected_not_started",
            "Historical predecessor profile fanout: **0**",
            "Application feature repair cycles: **0**",
        ):
            self.assertIn(marker, supplement)

    def test_alp06_scope_preserves_safe_failure_and_owner_authority(self):
        checkpoint = load_json("governance/ai/work-state/ALP-06-attempt-001.json")
        scope = checkpoint["implementation_scope"]
        boundary = checkpoint["authority_boundary"]
        self.assertIn("retry lineage with stable attempt identity and deterministic attempt ordering", scope["authorized"])
        self.assertIn("safe-failure projection in which rehearsal failure does not itself mutate canonical character, project, scene, achievement or reward state", scope["authorized"])
        self.assertIn("explicit training marker and project learning evidence references tied to frozen ALP taxonomy families", scope["authorized"])
        self.assertIn("automatic XP, advancement, capability, achievement completion or reward grants from rehearsal, retry or failure", scope["not_authorized"])
        self.assertIn("canonical penalties, injuries, resource loss, project mutation or world/scene mutation caused solely by safe-failure rehearsal outcomes", scope["not_authorized"])
        self.assertIn("hidden or unauthorized evidence inference", scope["not_authorized"])
        self.assertIn("durable ALP persistence or migration 0022", scope["not_authorized"])
        self.assertFalse(boundary["alp07_plus_authorized"])
        self.assertFalse(boundary["provider_activation_authorized"])
        self.assertFalse(boundary["tester_distribution_authorized"])
        self.assertFalse(boundary["release_or_deployment_authorized"])


if __name__ == "__main__":
    unittest.main()
