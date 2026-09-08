from __future__ import annotations

import json
import re
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SCRIPTS = ROOT / "scripts"
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))

from execution_termination_preflight import evaluate  # noqa: E402
from validate_repository_health import (  # noqa: E402
    Audit,
    _validate_authority_and_pointer,
    _validate_behavior_scorecard_observations,
    _validate_cross_repository_app,
    _validate_validators,
    _validate_workflows,
)


def _load_json(path: str) -> dict[str, object]:
    return json.loads((ROOT / path).read_text(encoding="utf-8"))


def _base_state() -> dict[str, object]:
    return {
        "command_mode": "execution",
        "work_item_status": "in_progress",
        "successor_selection_required": True,
        "successor_selected": False,
        "requested_boundary_completed": False,
        "active_async_operations": 0,
        "pending_authorized_steps": [],
        "genuine_blocker": None,
    }


def _workflow_registry() -> dict[str, object]:
    return {
        "repositories": {
            "cybalicistjt-stack/multiversal-aioc": {
                "live_workflows": [{"path": ".github/workflows/validate-repository-health.yml"}]
            },
            "cybalicistjt-stack/Multiversal-app": {
                "current_main": "e34d43d669c48d484dbdb9e82b72a00c5d91f00c",
                "family_scope_merge": "e34d43d669c48d484dbdb9e82b72a00c5d91f00c",
                "live_workflows": [
                    {"path": ".github/workflows/_validation-core-profile.yml", "automatic_repository_event_trigger": False},
                    {"path": ".github/workflows/validate-current-family.yml", "automatic_repository_event_trigger": True},
                ],
            },
        }
    }


def _validator_registry() -> dict[str, object]:
    return {
        "repositories": {
            "cybalicistjt-stack/multiversal-aioc": {
                "current_validators": [{"path": "scripts/validate_repository_health.py", "runtime_imports_historical_validators": False}],
                "current_compatible_utilities": [{"path": "scripts/execution_termination_preflight.py"}],
                "current_regression_suites": [{"path": "tests/control_plane/test_control_plane_health.py", "caller": ".github/workflows/validate-repository-health.yml"}],
                "retired_legacy_control_suites": [{"lifecycle": "HISTORICAL_INERT"}],
            }
        }
    }


class TerminationPreflightTests(unittest.TestCase):
    def test_required_async_operation_is_nonterminal(self) -> None:
        state = _base_state(); state["active_async_operations"] = 1
        result = evaluate(state)
        self.assertEqual("CONTINUE_EXECUTION", result["decision"])
        self.assertEqual("MVTERM-ASYNC-ACTIVE", result["reason_code"])

    def test_completed_verified_with_successor_is_terminal(self) -> None:
        state = _base_state(); state.update({"work_item_status": "completed_verified", "successor_selected": True, "requested_boundary_completed": True})
        result = evaluate(state)
        self.assertEqual("ALLOW_FINAL_RESPONSE", result["decision"])
        self.assertEqual("MVTERM-COMPLETED-VERIFIED", result["reason_code"])

    def test_unproven_blocker_is_nonterminal(self) -> None:
        state = _base_state(); state["genuine_blocker"] = {"class": "environment_unavailable", "evidence": [], "recovery_attempted": False, "blocks_all_authorized_progress": False}
        result = evaluate(state)
        self.assertEqual("CONTINUE_EXECUTION", result["decision"])
        self.assertEqual("MVTERM-BLOCKER-EVIDENCE-INSUFFICIENT", result["reason_code"])

    def test_verified_usage_ceiling_preserves_pending_closeout_in_handoff(self) -> None:
        state = _base_state(); state.update({
            "work_item_status": "blocked_environment",
            "pending_authorized_steps": ["record completed_verified evidence", "select the strict successor"],
            "genuine_blocker": {"class": "environment_unavailable", "evidence": ["the execution platform reported that its usage ceiling was reached"], "recovery_attempted": True, "blocks_all_authorized_progress": True},
        })
        result = evaluate(state)
        self.assertEqual("ALLOW_FINAL_RESPONSE", result["decision"])
        self.assertEqual("MVTERM-GENUINE-BLOCKER", result["reason_code"])


class FlatHealthRegressionTests(unittest.TestCase):
    def test_active_product_convergence_control_is_machine_validated(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory); checkpoint_path = root / "checkpoint.json"
            checkpoint_path.write_text(json.dumps({
                "work_item_id":"AAI-10","attempt_id":"AAI-10-attempt-001","status":"in_progress",
                "implementation_branch":"codex/aai-10-proof-integrity-repair","implementation_authority":True,
                "convergence_control":{"owner_continue_count":2,"execution_cycles":2,"repair_cycles":4,"no_progress_cycles":0,"diagnostic_mode":True,"last_failure_signature":"post-merge state remained stale","last_failure_class":"test_contract","diagnostic_hypotheses":["active product convergence was not checked"],"retry_basis":{"changed_since_previous":["new repository evidence"]},"service_objective":{"ordinary_tranche_single_continue_target_percent":80,"ordinary_tranche_two_continue_target_percent":95,"max_execution_cycles_without_genuine_blocker":2,"unrelated_historical_validation_jobs_target":0,"reruns_without_changed_evidence_target":0,"post_merge_stale_pointer_target":0}}
            }), encoding="utf-8")
            pointer={"primary_attempt_id":"AAI-10-attempt-001","active_attempt":{"work_item_id":"AAI-10","attempt_id":"AAI-10-attempt-001","checkpoint_path":"checkpoint.json","status":"in_progress","implementation_branch":"codex/aai-10-proof-integrity-repair"}}
            active={"work_item":"AAI-10","attempt_id":"AAI-10-attempt-001","state":"in_progress","implementation_branch":"codex/aai-10-proof-integrity-repair","implementation_authority":True}
            audit=Audit(root); _validate_authority_and_pointer(audit,pointer,{"current":[],"active_planning_work":active},{"active_work":active})
            self.assertIn("MVHEALTH-CONVERGENCE-CLASS", {e["code"] for e in audit.errors})

    def test_scorecard_observation_rejects_noncanonical_failure_class(self) -> None:
        audit=Audit(ROOT); _validate_behavior_scorecard_observations(audit,{"post_policy_observations":[{"work_item":"AAI-09","failure_class":"test_contract"}]})
        self.assertIn("MVHEALTH-SCORECARD-FAILURE-CLASS", {e["code"] for e in audit.errors})

    def test_current_workflow_requires_control_plane_regressions(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root=Path(directory); d=root/".github/workflows"; d.mkdir(parents=True)
            (d/"validate-repository-health.yml").write_text("fetch-depth: 0\npython3 scripts/validate_repository_health.py --expected-head abc\n",encoding="utf-8")
            audit=Audit(root); _validate_workflows(audit,_workflow_registry())
            self.assertIn("MVHEALTH-CONTROL-PLANE-TEST-EXECUTION", {e["code"] for e in audit.errors})

    def test_local_cross_repository_gate_rejects_wrong_application_head(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            app_root=Path(directory); d=app_root/".github/workflows"; d.mkdir(parents=True)
            for name in ("_validation-core-profile.yml","validate-current-family.yml"): (d/name).write_text("name: fixture\n",encoding="utf-8")
            validator=app_root/"tools/validation_core/validate_repository_health_app.py"; validator.parent.mkdir(parents=True); validator.write_text("import sys\nprint('fixture app health')\nsys.exit(0)\n",encoding="utf-8")
            subprocess.run(["git","init"],cwd=app_root,check=True,capture_output=True); subprocess.run(["git","config","user.email","fixture@example.invalid"],cwd=app_root,check=True); subprocess.run(["git","config","user.name","Fixture"],cwd=app_root,check=True); subprocess.run(["git","add","."],cwd=app_root,check=True); subprocess.run(["git","commit","-m","fixture"],cwd=app_root,check=True,capture_output=True)
            registry=_workflow_registry(); registry["repositories"]["cybalicistjt-stack/Multiversal-app"]["current_main"]="0"*40
            audit=Audit(ROOT); _validate_cross_repository_app(audit,app_root,registry)
            self.assertIn("MVHEALTH-APP-EXACT-HEAD", {e["code"] for e in audit.errors})

    def test_current_workflow_rejects_historical_validator_execution(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root=Path(directory); d=root/".github/workflows"; d.mkdir(parents=True)
            (d/"validate-repository-health.yml").write_text("fetch-depth: 0\npython3 scripts/validate_repository_health.py --expected-head abc\npython3 scripts/validate_rsr_01.py\n",encoding="utf-8")
            audit=Audit(root); _validate_workflows(audit,_workflow_registry())
            self.assertIn("MVHEALTH-HISTORICAL-WORKFLOW-EXECUTION", {e["code"] for e in audit.errors})

    def test_current_validator_rejects_version_chain_import(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root=Path(directory); scripts=root/"scripts"; scripts.mkdir(parents=True)
            (scripts/"validate_repository_health.py").write_text("import importlib.util\nlegacy = '_validate_repository_health_v1_14.py'\n",encoding="utf-8")
            audit=Audit(root); _validate_validators(audit,_validator_registry())
            self.assertIn("MVHEALTH-HISTORICAL-RUNTIME-IMPORT", {e["code"] for e in audit.errors})

    def test_runtime_pointer_preload_is_bounded_to_active_or_latest_closeout(self) -> None:
        pointer=_load_json("governance/ai/runtime/CURRENT_WORK_POINTER.json"); supplements=pointer.get("roadmap_supplements")
        self.assertIsInstance(supplements,list); self.assertLessEqual(len(supplements),1)
        if supplements:
            supplement=supplements[0]; self.assertIsInstance(supplement,str); self.assertTrue((ROOT/supplement).is_file())
            filename=Path(supplement).name.upper(); active=pointer.get("active_attempt",{}); active_status=active.get("status"); active_item=active.get("work_item_id")
            if active_status == "in_progress":
                self.assertIn("GOVERNED_START",filename); self.assertIn(active_item.replace("-","").upper(),filename)
            else:
                recent=pointer.get("recently_completed_implementation_work",[]); self.assertTrue(recent)
                work_item=recent[0].get("work_item_id"); self.assertIn("CLOSEOUT",filename); self.assertIn(work_item.replace("-","").upper(),filename)

    def test_current_validator_contains_no_mutable_state_constants(self) -> None:
        source=(ROOT/"scripts/validate_repository_health.py").read_text(encoding="utf-8")
        self.assertIsNone(re.search(r"\b(?:AAI|MV-CONT)-\d+(?:-attempt-\d+)?\b",source)); self.assertIsNone(re.search(r"['\"][0-9a-f]{40}['\"]",source))


class FamilyExecutionPreflightTests(unittest.TestCase):
    def test_vti12_closeout_and_sgc_selection_are_atomic(self) -> None:
        vti=_load_json("governance/ai/work-state/VTI-12-attempt-001.json")
        pointer=_load_json("governance/ai/runtime/CURRENT_WORK_POINTER.json")
        authority=_load_json("governance/ai/runtime/ACTIVE_AUTHORITY_REGISTRY.json")
        runtime=_load_json("governance/repository-health/RUNTIME_STATE_LIFECYCLE_REGISTRY.json")
        index=_load_json("governance/ai/runtime/ROADMAP_INDEX.json")
        self.assertEqual(vti["status"],"completed_verified"); self.assertTrue(vti["authority_retired"]); self.assertEqual(vti["application_pr"],441); self.assertEqual(vti["application_merge_sha"],"7e93bc4bb1c3b8ecc9bc4424dd7422ea328e2765")
        green=vti["validation"]["final_green"]; self.assertEqual(green["head_sha"],"712f7096118ae065d3d17492e2cc5effa1d83034"); self.assertEqual(green["run_id"],34221889244); self.assertEqual(green["deterministic_receipt_sha256"],"77536c1214f37374ca8ea1b2f1f627b30e209f52bb141133d690cdfc9b0544a4")
        for selected in (pointer["active_attempt"],authority["active_planning_work"],runtime["active_work"],index["current"]): self.assertEqual(selected.get("work_item_id",selected.get("work_item")),"SGC-01A")
        self.assertEqual(pointer["active_attempt"]["status"],"selected_not_started"); self.assertFalse(pointer["active_attempt"]["implementation_authority"]); self.assertIsNone(pointer["active_attempt"]["implementation_branch"])

    def test_sgc_execution_units_are_pre_sized_for_one_continue(self) -> None:
        pf=_load_json("governance/ai/runtime/FAMILY_EXECUTION_PREFLIGHT.json"); backlog=_load_json("governance/application-planning/source-gameplay-coverage-closure/SGC_PROGRAM_BACKLOG.json")
        self.assertEqual(pf["status"],"sealed"); self.assertEqual(pf["family_id"],"SGC"); self.assertEqual(pf["execution_target"]["ordinary_tranche_single_continue_completion_percent"],100); self.assertEqual(pf["execution_target"]["max_execution_cycles_without_genuine_blocker"],1); self.assertEqual(pf["execution_target"]["target_active_minutes_per_unit"],24); self.assertGreaterEqual(pf["execution_target"]["minimum_closeout_reserve_minutes"],8)
        units=pf["execution_units"]; self.assertEqual(len(units),22); self.assertTrue(all(0 < row["estimated_active_minutes"] <= 24 for row in units)); self.assertEqual(backlog["strict_order"],[row["id"] for row in units]); self.assertEqual(backlog["current_item"],"SGC-01A")

    def test_prefamily_context_is_blocked_by_default(self) -> None:
        pf=_load_json("governance/ai/runtime/FAMILY_EXECUTION_PREFLIGHT.json"); blocked=" ".join(pf["context_seal"]["blocked_by_default"]).lower()
        for phrase in ("historical tranche tests","unrelated completed-program","drive","airtable","sheets","docs"): self.assertIn(phrase,blocked)

    def test_live_workflow_executes_only_single_current_regression_suite(self) -> None:
        workflow=(ROOT/".github/workflows/validate-repository-health.yml").read_text(encoding="utf-8")
        registry=_load_json("governance/repository-health/VALIDATOR_LIFECYCLE_REGISTRY.json")
        suites=registry["repositories"]["cybalicistjt-stack/multiversal-aioc"]["current_regression_suites"]
        self.assertEqual([row["path"] for row in suites],["tests/control_plane/test_control_plane_health.py"])
        self.assertIn("-p 'test_control_plane_health.py'",workflow)
        self.assertNotIn("-p 'test_*.py'",workflow)


if __name__ == "__main__":
    unittest.main()
