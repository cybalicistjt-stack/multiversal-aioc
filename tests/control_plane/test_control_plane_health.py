from __future__ import annotations

import sys
import tempfile
import unittest
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
SCRIPTS = ROOT / "scripts"
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))

from execution_termination_preflight import evaluate  # noqa: E402
from validate_repository_health import (  # noqa: E402
    Audit,
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


class FlatHealthRegressionTests(unittest.TestCase):
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
