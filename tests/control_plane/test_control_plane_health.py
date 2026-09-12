from __future__ import annotations

import importlib.util
from pathlib import Path

_BASE = Path(__file__).with_name("_control_plane_health_regression_base.py")
_spec = importlib.util.spec_from_file_location("_control_plane_health_regression_base", _BASE)
if _spec is None or _spec.loader is None:
    raise RuntimeError(f"unable to load current regression base: {_BASE}")
_legacy = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_legacy)

from validate_execution_convergence import ConvergenceError, validate_convergence_control
from validate_repository_health import REQUIRED_SERVICE_OBJECTIVE, _maintenance_proof_has_required_shape

TerminationPreflightTests = _legacy.TerminationPreflightTests
FlatHealthRegressionTests = _legacy.FlatHealthRegressionTests


class FamilyExecutionPreflightTests(_legacy.FamilyExecutionPreflightTests):
    def test_vti12_closeout_and_current_sgc_selection_are_atomic(self) -> None:
        sgc = _legacy._load_json("governance/ai/work-state/SGC-08C-attempt-001.json")
        sgc_backlog = _legacy._load_json("governance/application-planning/source-gameplay-coverage-closure/SGC_PROGRAM_BACKLOG.json")
        ari_backlog = _legacy._load_json("governance/application-planning/asset-resource-ingestion-reuse/ARI_PROGRAM_BACKLOG.json")
        pointer = _legacy._load_json("governance/ai/runtime/CURRENT_WORK_POINTER.json")
        authority = _legacy._load_json("governance/ai/runtime/ACTIVE_AUTHORITY_REGISTRY.json")
        runtime = _legacy._load_json("governance/repository-health/RUNTIME_STATE_LIFECYCLE_REGISTRY.json")
        compiled = _legacy._load_json("governance/ai/runtime/ROADMAP_COMPILED_PROJECTION.json")
        checkpoint = _legacy._load_json(pointer["active_attempt"]["checkpoint_path"])
        self.assertEqual(sgc["status"], "completed_verified")
        self.assertEqual(sgc_backlog["status"], "completed_verified")
        self.assertEqual(sgc_backlog["completed_through"], "SGC-08C")
        selected_item = pointer["active_attempt"]["work_item_id"]
        self.assertEqual(selected_item, ari_backlog["current_item"])
        self.assertEqual(pointer["active_attempt"]["attempt_id"], ari_backlog["current_attempt"])
        selected_index = ari_backlog["strict_order"].index(selected_item)
        self.assertGreater(selected_index, 0)
        self.assertEqual(ari_backlog["completed_through"], ari_backlog["strict_order"][selected_index - 1])
        self.assertEqual(checkpoint["work_item_id"], selected_item)
        self.assertEqual(checkpoint["attempt_id"], pointer["active_attempt"]["attempt_id"])
        self.assertEqual(pointer["active_attempt"]["status"], checkpoint["status"])
        self.assertEqual(pointer["active_attempt"]["implementation_authority"], checkpoint["implementation_authority"])
        self.assertEqual(pointer["active_attempt"]["implementation_branch"], checkpoint["implementation_branch"])
        for selected in (authority["active_planning_work"], runtime["active_work"]):
            self.assertEqual(selected.get("work_item_id", selected.get("work_item")), selected_item)
            self.assertEqual(selected.get("state", selected.get("status")), checkpoint["status"])
            self.assertEqual(selected["implementation_authority"], checkpoint["implementation_authority"])
            self.assertEqual(selected["implementation_branch"], checkpoint["implementation_branch"])
        compiled_selection = compiled["current_selection"]
        self.assertEqual(compiled_selection["work_item_id"], selected_item)
        self.assertEqual(compiled_selection["attempt_id"], checkpoint["attempt_id"])
        self.assertEqual(compiled_selection["status"], checkpoint["status"])
        self.assertEqual(compiled_selection["implementation_authority"], checkpoint["implementation_authority"])

    def test_sgc_execution_units_are_pre_sized_for_one_continue(self) -> None:
        pf = _legacy._load_json("governance/ai/runtime/FAMILY_EXECUTION_PREFLIGHT.json")
        pointer = _legacy._load_json("governance/ai/runtime/CURRENT_WORK_POINTER.json")
        self.assertEqual(pf["status"], "sealed")
        self.assertEqual(pf["family_id"], pointer["active_program"]["program_id"])
        self.assertEqual(pf["execution_target"]["ordinary_tranche_single_continue_completion_percent"], 100)
        self.assertEqual(pf["execution_target"]["max_execution_cycles_without_genuine_blocker"], 1)
        self.assertEqual(pf["execution_target"]["target_active_minutes_per_unit"], 24)
        self.assertGreaterEqual(pf["execution_target"]["minimum_closeout_reserve_minutes"], 8)
        units = pf["execution_units"]
        self.assertTrue(units)
        self.assertTrue(all(0 < row["estimated_active_minutes"] <= 24 for row in units))
        self.assertEqual(len({row["id"] for row in units}), len(units))
        self.assertIn(pointer["active_attempt"]["work_item_id"], [row["id"] for row in units])


class TrancheExecutionFastPathGovernanceTests(_legacy.unittest.TestCase):
    def test_convergence_validators_enforce_one_continue_policy(self) -> None:
        self.assertEqual(
            REQUIRED_SERVICE_OBJECTIVE,
            {
                "ordinary_tranche_single_continue_target_percent": 100,
                "max_execution_cycles_without_genuine_blocker": 1,
                "unrelated_historical_validation_jobs_target": 0,
                "reruns_without_changed_evidence_target": 0,
                "post_merge_stale_pointer_target": 0,
            },
        )
        control = {
            "owner_continue_count": 1,
            "execution_cycles": 1,
            "repair_cycles": 0,
            "no_progress_cycles": 0,
            "diagnostic_mode": False,
            "last_failure_signature": None,
            "last_failure_class": None,
            "diagnostic_hypotheses": [],
            "retry_basis": None,
            "service_objective": REQUIRED_SERVICE_OBJECTIVE,
        }
        validate_convergence_control(control, status="in_progress", context="test")
        control["service_objective"] = {
            **REQUIRED_SERVICE_OBJECTIVE,
            "ordinary_tranche_single_continue_target_percent": 80,
            "ordinary_tranche_two_continue_target_percent": 95,
            "max_execution_cycles_without_genuine_blocker": 2,
        }
        with self.assertRaises(ConvergenceError):
            validate_convergence_control(control, status="in_progress", context="test")

    def test_maintenance_proof_scope_allows_aioc_only_without_fake_application_evidence(self) -> None:
        aioc_only = {
            "work_item": "MV-CONT-009",
            "status": "completed_verified",
            "maintenance_scope": "aioc_only",
            "aioc_pr": 1136,
            "aioc_validated_head": "f1d4738df210b7defa2ef9342b93874bfe835f40",
            "aioc_repository_health_run": 34702688466,
            "aioc_merge": "32f96ba6e9728fb785f2d4eaa0655a705996e8e8",
            "aioc_main_health_run": 34702781559,
            "superseded_prs_closed": [],
        }
        self.assertTrue(_maintenance_proof_has_required_shape(aioc_only, seen_work_items=set()))
        historical = {
            **aioc_only,
            "work_item": "MV-CONT-008",
            "maintenance_scope": "cross_repository",
            "application_pr": 337,
            "application_merge": "d007dc980c63a7beab4ab9a4ddbc67525f8d7003",
        }
        self.assertTrue(_maintenance_proof_has_required_shape(historical, seen_work_items=set()))
        fabricated = {**aioc_only, "application_pr": 999, "application_merge": "d007dc980c63a7beab4ab9a4ddbc67525f8d7003"}
        self.assertFalse(_maintenance_proof_has_required_shape(fabricated, seen_work_items=set()))

    def test_lane_maintenance_projection_matches_live_pointer(self) -> None:
        pointer = _legacy._load_json("governance/ai/runtime/CURRENT_WORK_POINTER.json")
        lanes = _legacy._load_json("governance/ai/runtime/PRODUCT_EXECUTION_LANES.json")
        maintenance = lanes["maintenance_mode"]
        self.assertNotIn("exclusive_control_plane_maintenance", pointer)
        self.assertFalse(maintenance["active"])
        self.assertIsNone(maintenance["work_item"])
        self.assertFalse(maintenance["feature_starts_blocked"])
        self.assertEqual(lanes["active_product_attempts"], [])
        self.assertFalse(lanes["legacy_primary_selection"]["implementation_authority"])

    @staticmethod
    def _read(path: str) -> str:
        return (_legacy.ROOT / path).read_text(encoding="utf-8")

    def test_bootstrap_makes_fast_path_survive_conversation_boundaries(self) -> None:
        bootstrap = self._read("governance/ai/MULTIVERSAL_NEW_CONVERSATION_BOOTSTRAP.md")
        required = [
            "## Tranche execution fast path",
            "closeout-switch point",
            "Do not rediscover an already-loaded tool schema",
            "atomic tree/commit",
            "compact evidence artifact",
            "initial `mergeable: false`",
            "unrelated parallel work",
            "control-plane efficiency incident",
        ]
        for phrase in required:
            with self.subTest(phrase=phrase):
                self.assertIn(phrase, bootstrap)

    def test_efficiency_policy_blocks_operational_noise_regressions(self) -> None:
        policy = self._read("governance/ai/MULTIVERSAL_CHECKPOINT_AND_VALIDATION_EFFICIENCY_POLICY.md")
        required = [
            "## 11. Tranche execution fast path",
            "Operational overhead counts against the tranche target.",
            "target_active_minutes_per_unit - minimum_closeout_reserve_minutes",
            "atomic multi-file closeout",
            "Full successful workflow logs are prohibited by default.",
            "one bounded recomputation check",
            "fixed sleep/poll loops",
            "control-plane efficiency incident",
            "one-Continue completion objective",
        ]
        for phrase in required:
            with self.subTest(phrase=phrase):
                self.assertIn(phrase, policy)

    def test_fast_path_retains_declared_closeout_reserve_math(self) -> None:
        pf = _legacy._load_json("governance/ai/runtime/FAMILY_EXECUTION_PREFLIGHT.json")
        target = pf["execution_target"]["target_active_minutes_per_unit"]
        reserve = pf["execution_target"]["minimum_closeout_reserve_minutes"]
        self.assertGreater(target, reserve)
        self.assertEqual(target, 24)
        self.assertGreaterEqual(reserve, 8)
        self.assertLessEqual(target - reserve, 16)


if __name__ == "__main__":
    _legacy.unittest.main()
