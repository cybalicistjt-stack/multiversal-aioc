from __future__ import annotations

import sys
import tempfile
import unittest
import re
import subprocess
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
                "live_workflows": [
                    {"path": ".github/workflows/validate-repository-health.yml"}
                ]
            },
            "cybalicistjt-stack/Multiversal-app": {
                "current_main": "e34d43d669c48d484dbdb9e82b72a00c5d91f00c",
                "family_scope_merge": "e34d43d669c48d484dbdb9e82b72a00c5d91f00c",
                "live_workflows": [
                    {
                        "path": ".github/workflows/_validation-core-profile.yml",
                        "automatic_repository_event_trigger": False,
                    },
                    {
                        "path": ".github/workflows/validate-current-family.yml",
                        "automatic_repository_event_trigger": True,
                    },
                ],
            },
        }
    }


def _validator_registry() -> dict[str, object]:
    return {
        "repositories": {
            "cybalicistjt-stack/multiversal-aioc": {
                "current_validators": [
                    {
                        "path": "scripts/validate_repository_health.py",
                        "runtime_imports_historical_validators": False,
                    }
                ],
                "current_compatible_utilities": [
                    {"path": "scripts/execution_termination_preflight.py"}
                ],
                "current_regression_suites": [
                    {
                        "path": "tests/control_plane/test_control_plane_health.py",
                        "caller": ".github/workflows/validate-repository-health.yml",
                    }
                ],
            }
        }
    }


class TerminationPreflightTests(unittest.TestCase):
    def test_required_async_operation_is_nonterminal(self) -> None:
        state = _base_state()
        state["active_async_operations"] = 1
        result = evaluate(state)
        self.assertEqual("CONTINUE_EXECUTION", result["decision"])
        self.assertEqual("MVTERM-ASYNC-ACTIVE", result["reason_code"])

    def test_completed_verified_with_successor_is_terminal(self) -> None:
        state = _base_state()
        state.update(
            {
                "work_item_status": "completed_verified",
                "successor_selected": True,
                "requested_boundary_completed": True,
            }
        )
        result = evaluate(state)
        self.assertEqual("ALLOW_FINAL_RESPONSE", result["decision"])
        self.assertEqual("MVTERM-COMPLETED-VERIFIED", result["reason_code"])

    def test_unproven_blocker_is_nonterminal(self) -> None:
        state = _base_state()
        state["genuine_blocker"] = {
            "class": "environment_unavailable",
            "evidence": [],
            "recovery_attempted": False,
            "blocks_all_authorized_progress": False,
        }
        result = evaluate(state)
        self.assertEqual("CONTINUE_EXECUTION", result["decision"])
        self.assertEqual(
            "MVTERM-BLOCKER-EVIDENCE-INSUFFICIENT", result["reason_code"]
        )

    def test_verified_usage_ceiling_preserves_pending_closeout_in_handoff(self) -> None:
        state = _base_state()
        state.update(
            {
                "work_item_status": "blocked_environment",
                "pending_authorized_steps": [
                    "record completed_verified evidence",
                    "select the strict successor",
                ],
                "genuine_blocker": {
                    "class": "environment_unavailable",
                    "evidence": [
                        "the execution platform reported that its usage ceiling was reached"
                    ],
                    "recovery_attempted": True,
                    "blocks_all_authorized_progress": True,
                },
            }
        )
        result = evaluate(state)
        self.assertEqual("ALLOW_FINAL_RESPONSE", result["decision"])
        self.assertEqual("MVTERM-GENUINE-BLOCKER", result["reason_code"])


class FlatHealthRegressionTests(unittest.TestCase):
    def test_active_product_convergence_control_is_machine_validated(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            checkpoint_path = root / "checkpoint.json"
            checkpoint_path.write_text(
                """{
                  "work_item_id":"AAI-10",
                  "attempt_id":"AAI-10-attempt-001",
                  "status":"in_progress",
                  "implementation_branch":"codex/aai-10-proof-integrity-repair",
                  "implementation_authority":true,
                  "convergence_control":{
                    "owner_continue_count":2,
                    "execution_cycles":2,
                    "repair_cycles":4,
                    "no_progress_cycles":0,
                    "diagnostic_mode":true,
                    "last_failure_signature":"post-merge state remained stale",
                    "last_failure_class":"test_contract",
                    "diagnostic_hypotheses":["active product convergence was not checked"],
                    "retry_basis":"new repository evidence",
                    "service_objective":{
                      "ordinary_tranche_single_continue_target_percent":80,
                      "ordinary_tranche_two_continue_target_percent":95,
                      "max_execution_cycles_without_genuine_blocker":2,
                      "unrelated_historical_validation_jobs_target":0,
                      "reruns_without_changed_evidence_target":0,
                      "post_merge_stale_pointer_target":0
                    }
                  }
                }""",
                encoding="utf-8",
            )
            pointer = {
                "primary_attempt_id": "AAI-10-attempt-001",
                "active_attempt": {
                    "work_item_id": "AAI-10",
                    "attempt_id": "AAI-10-attempt-001",
                    "checkpoint_path": "checkpoint.json",
                    "status": "in_progress",
                    "implementation_branch": "codex/aai-10-proof-integrity-repair",
                },
            }
            active = {
                "work_item": "AAI-10",
                "attempt_id": "AAI-10-attempt-001",
                "state": "in_progress",
                "implementation_branch": "codex/aai-10-proof-integrity-repair",
                "implementation_authority": True,
            }
            audit = Audit(root)
            _validate_authority_and_pointer(
                audit,
                pointer,
                {"current": [], "active_planning_work": active},
                {"active_work": active},
            )
            codes = {error["code"] for error in audit.errors}
            self.assertIn("MVHEALTH-CONVERGENCE-CLASS", codes)

    def test_scorecard_observation_rejects_noncanonical_failure_class(self) -> None:
        audit = Audit(ROOT)
        _validate_behavior_scorecard_observations(
            audit,
            {
                "post_policy_observations": [
                    {
                        "work_item": "AAI-09",
                        "failure_class": "test_contract",
                    }
                ]
            },
        )
        codes = {error["code"] for error in audit.errors}
        self.assertIn("MVHEALTH-SCORECARD-FAILURE-CLASS", codes)

    def test_current_workflow_requires_control_plane_regressions(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            workflow_dir = root / ".github/workflows"
            workflow_dir.mkdir(parents=True)
            (workflow_dir / "validate-repository-health.yml").write_text(
                "fetch-depth: 0\n"
                "python3 scripts/validate_repository_health.py --expected-head abc\n",
                encoding="utf-8",
            )
            audit = Audit(root)
            _validate_workflows(audit, _workflow_registry())
            codes = {error["code"] for error in audit.errors}
            self.assertIn("MVHEALTH-CONTROL-PLANE-TEST-EXECUTION", codes)

    def test_local_cross_repository_gate_rejects_wrong_application_head(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            app_root = Path(directory)
            workflow_dir = app_root / ".github/workflows"
            workflow_dir.mkdir(parents=True)
            for name in ("_validation-core-profile.yml", "validate-current-family.yml"):
                (workflow_dir / name).write_text("name: fixture\n", encoding="utf-8")
            validator = app_root / "tools/validation_core/validate_repository_health_app.py"
            validator.parent.mkdir(parents=True)
            validator.write_text(
                "import sys\nprint('fixture app health')\nsys.exit(0)\n",
                encoding="utf-8",
            )
            subprocess.run(["git", "init"], cwd=app_root, check=True, capture_output=True)
            subprocess.run(["git", "config", "user.email", "fixture@example.invalid"], cwd=app_root, check=True)
            subprocess.run(["git", "config", "user.name", "Fixture"], cwd=app_root, check=True)
            subprocess.run(["git", "add", "."], cwd=app_root, check=True)
            subprocess.run(["git", "commit", "-m", "fixture"], cwd=app_root, check=True, capture_output=True)
            registry = _workflow_registry()
            registry["repositories"]["cybalicistjt-stack/Multiversal-app"]["current_main"] = "0" * 40
            audit = Audit(ROOT)
            _validate_cross_repository_app(audit, app_root, registry)
            codes = {error["code"] for error in audit.errors}
            self.assertIn("MVHEALTH-APP-EXACT-HEAD", codes)

    def test_current_workflow_rejects_historical_validator_execution(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            workflow_dir = root / ".github/workflows"
            workflow_dir.mkdir(parents=True)
            (workflow_dir / "validate-repository-health.yml").write_text(
                "fetch-depth: 0\n"
                "python3 scripts/validate_repository_health.py --expected-head abc\n"
                "python3 scripts/validate_rsr_01.py\n",
                encoding="utf-8",
            )
            audit = Audit(root)
            _validate_workflows(audit, _workflow_registry())
            codes = {error["code"] for error in audit.errors}
            self.assertIn("MVHEALTH-HISTORICAL-WORKFLOW-EXECUTION", codes)

    def test_current_validator_rejects_version_chain_import(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            scripts = root / "scripts"
            scripts.mkdir(parents=True)
            (scripts / "validate_repository_health.py").write_text(
                "import importlib.util\n"
                "legacy = '_validate_repository_health_v1_14.py'\n",
                encoding="utf-8",
            )
            audit = Audit(root)
            _validate_validators(audit, _validator_registry())
            codes = {error["code"] for error in audit.errors}
            self.assertIn("MVHEALTH-HISTORICAL-RUNTIME-IMPORT", codes)

    def test_runtime_pointer_preload_is_bounded_to_active_or_latest_closeout(self) -> None:
        pointer = __import__("json").loads(
            (ROOT / "governance/ai/runtime/CURRENT_WORK_POINTER.json").read_text(
                encoding="utf-8"
            )
        )
        supplements = pointer.get("roadmap_supplements")
        self.assertIsInstance(supplements, list)
        self.assertLessEqual(
            len(supplements),
            1,
            "runtime pointer must not fan out into historical roadmap supplements",
        )
        if supplements:
            supplement = supplements[0]
            self.assertIsInstance(supplement, str)
            self.assertTrue((ROOT / supplement).is_file())
            filename = Path(supplement).name.upper()
            active = pointer.get("active_attempt", {})
            self.assertIsInstance(active, dict)
            active_status = active.get("status")
            active_item = active.get("work_item_id")
            self.assertIsInstance(active_item, str)
            if active_status == "in_progress":
                self.assertIn("GOVERNED_START", filename)
                self.assertIn(active_item.replace("-", "").upper(), filename)
            else:
                recent = pointer.get("recently_completed_implementation_work", [])
                self.assertIsInstance(recent, list)
                self.assertTrue(recent, "a live closeout supplement requires a recent completion")
                work_item = recent[0].get("work_item_id")
                self.assertIsInstance(work_item, str)
                self.assertIn("CLOSEOUT", filename)
                self.assertIn(work_item.replace("-", "").upper(), filename)

    def test_current_validator_contains_no_mutable_state_constants(self) -> None:
        source = (ROOT / "scripts/validate_repository_health.py").read_text(
            encoding="utf-8"
        )
        self.assertIsNone(
            re.search(r"\b(?:AAI|MV-CONT)-\d+(?:-attempt-\d+)?\b", source)
        )
        self.assertIsNone(re.search(r"['\"][0-9a-f]{40}['\"]", source))


if __name__ == "__main__":
    unittest.main()
