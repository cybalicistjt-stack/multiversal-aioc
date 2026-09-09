from __future__ import annotations

import importlib.util
from pathlib import Path

_BASE = Path(__file__).with_name("_control_plane_health_regression_base.py")
_spec = importlib.util.spec_from_file_location("_control_plane_health_regression_base", _BASE)
if _spec is None or _spec.loader is None:
    raise RuntimeError(f"unable to load current regression base: {_BASE}")
_legacy = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_legacy)

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
        index = _legacy._load_json("governance/ai/runtime/ROADMAP_INDEX.json")
        checkpoint = _legacy._load_json(pointer["active_attempt"]["checkpoint_path"])
        self.assertEqual(sgc["status"], "completed_verified")
        self.assertEqual(sgc_backlog["status"], "completed_verified")
        self.assertEqual(sgc_backlog["completed_through"], "SGC-08C")
        self.assertEqual(ari_backlog["completed_through"], "ARI-01")
        selected_item = pointer["active_attempt"]["work_item_id"]
        self.assertEqual(selected_item, ari_backlog["current_item"])
        self.assertEqual(pointer["active_attempt"]["attempt_id"], ari_backlog["current_attempt"])
        self.assertEqual(checkpoint["work_item_id"], selected_item)
        self.assertEqual(checkpoint["attempt_id"], pointer["active_attempt"]["attempt_id"])
        self.assertEqual(pointer["active_attempt"]["status"], checkpoint["status"])
        self.assertEqual(pointer["active_attempt"]["implementation_authority"], checkpoint["implementation_authority"])
        self.assertEqual(pointer["active_attempt"]["implementation_branch"], checkpoint["implementation_branch"])
        for selected in (authority["active_planning_work"], runtime["active_work"], index["current"]):
            self.assertEqual(selected.get("work_item_id", selected.get("work_item")), selected_item)
            self.assertEqual(selected.get("state", selected.get("status")), checkpoint["status"])
            self.assertEqual(selected["implementation_authority"], checkpoint["implementation_authority"])
            self.assertEqual(selected["implementation_branch"], checkpoint["implementation_branch"])

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


if __name__ == "__main__":
    _legacy.unittest.main()
