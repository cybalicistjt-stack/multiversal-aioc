from __future__ import annotations

import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SCRIPTS = ROOT / "scripts"
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))

from execution_termination_preflight import evaluate  # noqa: E402
from execution_transaction_preflight import (  # noqa: E402
    TransactionPreflightError,
    assess_validation_head,
    decide_start,
    prepare_closeout,
    validate_execution_outcome,
    validate_start_projection,
)


def _started_projection() -> tuple[dict, dict, dict, dict, dict]:
    checkpoint = {
        "work_item_id": "ARI-19",
        "attempt_id": "ARI-19-attempt-001",
        "status": "in_progress",
        "implementation_branch": "implementation/ari-19-universal-asset-picker-resource-query-api",
        "implementation_authority": True,
    }
    pointer = {
        "active_attempt": {
            **checkpoint,
            "checkpoint_path": "governance/ai/work-state/ARI-19-attempt-001.json",
        }
    }
    authority = {
        "active_planning_work": {
            "work_item": "ARI-19",
            "attempt_id": "ARI-19-attempt-001",
            "state": "in_progress",
            "implementation_branch": checkpoint["implementation_branch"],
            "implementation_authority": True,
        }
    }
    runtime = {
        "active_work": {
            "work_item": "ARI-19",
            "attempt_id": "ARI-19-attempt-001",
            "state": "in_progress",
            "implementation_branch": checkpoint["implementation_branch"],
            "implementation_authority": True,
        }
    }
    compiled = {
        "current_selection": {
            "work_item_id": "ARI-19",
            "attempt_id": "ARI-19-attempt-001",
            "status": "in_progress",
            "implementation_authority": True,
        }
    }
    return checkpoint, pointer, authority, runtime, compiled


class ExecutionHardeningTests(unittest.TestCase):
    def test_exact_authorized_open_pr_is_resumed_not_duplicated(self) -> None:
        result = decide_start({
            "work_item_id": "ARI-19",
            "authorized_branch": "implementation/ari-19-universal-asset-picker-resource-query-api",
            "proposed_branch": "implementation/ari-19-universal-asset-picker-resource-query-api",
            "observed_branches": ["implementation/ari-19-universal-asset-picker-resource-query-api"],
            "open_pull_requests": [{"number": 470, "work_item_id": "ARI-19", "head": "implementation/ari-19-universal-asset-picker-resource-query-api", "state": "open"}],
        })
        self.assertEqual(result["decision"], "RESUME_OPEN_PR")
        self.assertEqual(result["pull_request"], 470)

    def test_exact_authorized_branch_is_resumed_when_no_pr_exists(self) -> None:
        result = decide_start({
            "work_item_id": "ARI-19",
            "authorized_branch": "implementation/ari-19-universal-asset-picker-resource-query-api",
            "proposed_branch": "implementation/ari-19-universal-asset-picker-resource-query-api",
            "observed_branches": ["implementation/ari-19-universal-asset-picker-resource-query-api"],
            "open_pull_requests": [],
        })
        self.assertEqual(result["decision"], "RESUME_BRANCH")

    def test_clean_start_creates_only_the_authorized_branch(self) -> None:
        result = decide_start({
            "work_item_id": "ARI-19",
            "authorized_branch": "implementation/ari-19-universal-asset-picker-resource-query-api",
            "proposed_branch": "implementation/ari-19-universal-asset-picker-resource-query-api",
            "observed_branches": [],
            "open_pull_requests": [],
        })
        self.assertEqual(result["decision"], "CREATE_AUTHORIZED_BRANCH")

    def test_alternate_branch_or_duplicate_pr_stops_start(self) -> None:
        result = decide_start({
            "work_item_id": "ARI-19",
            "authorized_branch": "implementation/ari-19-universal-asset-picker-resource-query-api",
            "proposed_branch": "implementation/ari-19-picker",
            "observed_branches": ["implementation/ari-19-picker"],
            "open_pull_requests": [{"number": 471, "work_item_id": "ARI-19", "head": "implementation/ari-19-picker", "state": "open"}],
        })
        self.assertEqual(result["decision"], "STOP_DUPLICATE_ATTEMPT")
        self.assertIn(471, result["conflicting_pull_requests"])

    def test_started_projection_must_be_atomic_before_branch_mutation(self) -> None:
        checkpoint, pointer, authority, runtime, compiled = _started_projection()
        validate_start_projection(checkpoint, pointer, authority, runtime, compiled)
        compiled["current_selection"]["status"] = "selected_not_started"
        with self.assertRaises(TransactionPreflightError):
            validate_start_projection(checkpoint, pointer, authority, runtime, compiled)

    def test_only_validation_for_current_exact_head_can_count(self) -> None:
        current = "a" * 40
        self.assertEqual(assess_validation_head(current, current, "success")["state"], "CURRENT_GREEN")
        stale = assess_validation_head(current, "b" * 40, "success")
        self.assertEqual(stale["state"], "SUPERSEDED")
        self.assertFalse(stale["counts_for_closeout"])

    def test_closeout_can_be_precomputed_without_fabricating_evidence(self) -> None:
        prepared = prepare_closeout({
            "work_item_id": "ARI-19",
            "strict_successor": "ARI-20",
            "current_head": "a" * 40,
            "validated_head": None,
            "validation_run": None,
            "deterministic_receipt_sha256": None,
            "merge_sha": None,
        })
        self.assertEqual(prepared["decision"], "PREPARE_CLOSEOUT")
        self.assertEqual(prepared["successor"], "ARI-20")
        self.assertEqual(set(prepared["evidence_placeholders"]), {"validated_head", "validation_run", "deterministic_receipt_sha256", "merge_sha"})
        ready = prepare_closeout({
            "work_item_id": "ARI-19",
            "strict_successor": "ARI-20",
            "current_head": "a" * 40,
            "validated_head": "a" * 40,
            "validation_run": 123,
            "deterministic_receipt_sha256": "c" * 64,
            "merge_sha": "d" * 40,
        })
        self.assertEqual(ready["decision"], "READY_TO_CLOSE")

    def test_one_continue_outcome_is_machine_visible_and_second_continue_is_incident(self) -> None:
        validate_execution_outcome({"owner_continue_turns": 1, "single_continue_achieved": True, "execution_incident": None})
        validate_execution_outcome({"owner_continue_turns": 2, "single_continue_achieved": False, "execution_incident": {"type": "second_continue_required", "reason": "assistant returned before terminal boundary"}})
        with self.assertRaises(TransactionPreflightError):
            validate_execution_outcome({"owner_continue_turns": 2, "single_continue_achieved": True, "execution_incident": None})

    def test_termination_preflight_cannot_forget_open_pr_or_current_ci_or_closeout(self) -> None:
        base = {
            "command_mode": "execution",
            "work_item_status": "in_progress",
            "successor_selection_required": True,
            "successor_selected": False,
            "requested_boundary_completed": False,
            "active_async_operations": 0,
            "pending_authorized_steps": [],
            "genuine_blocker": None,
        }
        pr_open = evaluate({**base, "pull_request_state": "open"})
        self.assertEqual((pr_open["decision"], pr_open["reason_code"]), ("CONTINUE_EXECUTION", "MVTERM-PR-OPEN"))
        ci_active = evaluate({**base, "current_head_validation_state": "queued"})
        self.assertEqual((ci_active["decision"], ci_active["reason_code"]), ("CONTINUE_EXECUTION", "MVTERM-VALIDATION-ACTIVE"))
        closeout = evaluate({**base, "pull_request_state": "merged", "merge_closeout_pending": True})
        self.assertEqual((closeout["decision"], closeout["reason_code"]), ("CONTINUE_EXECUTION", "MVTERM-CLOSEOUT-PENDING"))


if __name__ == "__main__":
    unittest.main()
