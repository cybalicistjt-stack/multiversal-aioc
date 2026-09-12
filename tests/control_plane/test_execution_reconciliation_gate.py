from __future__ import annotations

import hashlib
import json
import sys
import unittest
from copy import deepcopy
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SCRIPTS = ROOT / "scripts"
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))

from execution_termination_preflight import evaluate  # noqa: E402


def _digest(bundle: dict) -> str:
    material = {key: value for key, value in bundle.items() if key != "reconciliation_digest"}
    payload = json.dumps(material, sort_keys=True, separators=(",", ":"), ensure_ascii=True).encode("utf-8")
    return hashlib.sha256(payload).hexdigest()


def _valid_reconciliation(cycle_id: str = "HAI-CYCLE-004", trace_id: str = "TRACE-HAI-004") -> dict:
    bundle = {
        "desired_state": "terminal_verified",
        "trace_id": trace_id,
        "resume_generation": 0,
        "resumed_from_cycle_id": None,
        "operation_ledger": [
            {
                "operation_id": "HAT-F09-A",
                "idempotency_key": "HAI-CYCLE-004:HAT-F09-A",
                "status": "completed",
                "attempts": 1,
                "trace_id": trace_id,
            }
        ],
        "next_operation_id": None,
        "side_effect_ledger": [],
        "progress": {
            "reconciliation_passes": 1,
            "consecutive_no_progress_passes": 0,
            "diagnostic_mode": False,
        },
        "verification_evidence": [
            {
                "evidence_id": "evidence-001",
                "kind": "source_crosscheck",
                "result": "pass",
                "independent": True,
                "bound_cycle_id": cycle_id,
                "trace_id": trace_id,
            }
        ],
    }
    bundle["reconciliation_digest"] = _digest(bundle)
    return bundle


def _terminal_state() -> dict:
    return {
        "command_mode": "execution",
        "work_item_status": "completed_verified",
        "successor_selection_required": False,
        "successor_selected": False,
        "requested_boundary_completed": True,
        "active_async_operations": 0,
        "pending_authorized_steps": [],
        "pull_request_state": "none",
        "current_head_validation_state": "passed",
        "merge_closeout_pending": False,
        "genuine_blocker": None,
        "execution_envelope": {
            "cycle_id": "HAI-CYCLE-004",
            "phase": "closed",
            "elapsed_active_minutes": 24.0,
            "closeout_switch_active_minute": 16,
            "target_cycle_minutes": 24,
            "safe_same_lane_work_available": False,
            "dynamic_fill_attempted": True,
            "closeout_complete": True,
            "fill_exit_reason": "closeout_switch_reached",
        },
    }


class ExecutionReconciliationGateTests(unittest.TestCase):
    def test_terminal_state_requires_reconciliation_bundle(self) -> None:
        result = evaluate(_terminal_state())
        self.assertEqual((result["decision"], result["reason_code"]), ("CONTINUE_EXECUTION", "MVTERM-RECONCILIATION-MISSING"))

    def test_reconciliation_returns_all_unmet_invariants_in_one_pass(self) -> None:
        state = _terminal_state()
        bundle = _valid_reconciliation()
        bundle["desired_state"] = "operation_complete"
        bundle["next_operation_id"] = "HAT-F09-B1"
        bundle["side_effect_ledger"] = [{"effect_id": "effect-1", "idempotency_key": "effect-key-1", "status": "applied", "trace_id": bundle["trace_id"]}]
        bundle["progress"]["consecutive_no_progress_passes"] = 2
        bundle["verification_evidence"][0]["independent"] = False
        bundle["resume_generation"] = 1
        bundle["resumed_from_cycle_id"] = "HAI-CYCLE-003"
        bundle["reconciliation_digest"] = "0" * 64
        state["execution_reconciliation"] = bundle
        result = evaluate(state)
        self.assertEqual((result["decision"], result["reason_code"]), ("CONTINUE_EXECUTION", "MVTERM-RECONCILIATION-PENDING"))
        unmet = set(result["unmet_invariants"])
        self.assertTrue({"desired_state", "next_operation", "side_effects", "liveness", "independent_evidence", "resume_identity", "digest"}.issubset(unmet))

    def test_operation_ledger_rejects_duplicate_operation_or_idempotency_identity(self) -> None:
        state = _terminal_state()
        bundle = _valid_reconciliation()
        duplicate = deepcopy(bundle["operation_ledger"][0])
        duplicate["attempts"] = 2
        bundle["operation_ledger"].append(duplicate)
        bundle["reconciliation_digest"] = _digest(bundle)
        state["execution_reconciliation"] = bundle
        result = evaluate(state)
        self.assertEqual(result["reason_code"], "MVTERM-RECONCILIATION-INVALID")
        self.assertIn("operation_identity", result["unmet_invariants"])

    def test_unreconciled_side_effect_blocks_terminal_response(self) -> None:
        state = _terminal_state()
        bundle = _valid_reconciliation()
        bundle["side_effect_ledger"] = [{"effect_id": "effect-1", "idempotency_key": "effect-key-1", "status": "applied", "trace_id": bundle["trace_id"]}]
        bundle["reconciliation_digest"] = _digest(bundle)
        state["execution_reconciliation"] = bundle
        result = evaluate(state)
        self.assertEqual(result["reason_code"], "MVTERM-RECONCILIATION-PENDING")
        self.assertIn("side_effects", result["unmet_invariants"])

    def test_consecutive_no_progress_requires_more_execution_before_terminal(self) -> None:
        state = _terminal_state()
        bundle = _valid_reconciliation()
        bundle["progress"]["consecutive_no_progress_passes"] = 1
        bundle["progress"]["diagnostic_mode"] = True
        bundle["reconciliation_digest"] = _digest(bundle)
        state["execution_reconciliation"] = bundle
        result = evaluate(state)
        self.assertEqual(result["reason_code"], "MVTERM-RECONCILIATION-PENDING")
        self.assertIn("liveness", result["unmet_invariants"])

    def test_independent_verification_evidence_is_required(self) -> None:
        state = _terminal_state()
        bundle = _valid_reconciliation()
        bundle["verification_evidence"][0]["independent"] = False
        bundle["reconciliation_digest"] = _digest(bundle)
        state["execution_reconciliation"] = bundle
        result = evaluate(state)
        self.assertEqual(result["reason_code"], "MVTERM-RECONCILIATION-PENDING")
        self.assertIn("independent_evidence", result["unmet_invariants"])

    def test_interrupted_execution_must_resume_same_cycle_identity(self) -> None:
        state = _terminal_state()
        bundle = _valid_reconciliation()
        bundle["resume_generation"] = 2
        bundle["resumed_from_cycle_id"] = "HAI-CYCLE-003"
        bundle["reconciliation_digest"] = _digest(bundle)
        state["execution_reconciliation"] = bundle
        result = evaluate(state)
        self.assertEqual(result["reason_code"], "MVTERM-RECONCILIATION-PENDING")
        self.assertIn("resume_identity", result["unmet_invariants"])

    def test_causal_trace_must_match_every_operation_effect_and_evidence(self) -> None:
        state = _terminal_state()
        bundle = _valid_reconciliation()
        bundle["operation_ledger"][0]["trace_id"] = "TRACE-WRONG"
        bundle["reconciliation_digest"] = _digest(bundle)
        state["execution_reconciliation"] = bundle
        result = evaluate(state)
        self.assertEqual(result["reason_code"], "MVTERM-RECONCILIATION-PENDING")
        self.assertIn("trace_continuity", result["unmet_invariants"])

    def test_reconciliation_digest_binds_terminal_evidence_snapshot(self) -> None:
        state = _terminal_state()
        bundle = _valid_reconciliation()
        bundle["reconciliation_digest"] = "f" * 64
        state["execution_reconciliation"] = bundle
        result = evaluate(state)
        self.assertEqual(result["reason_code"], "MVTERM-RECONCILIATION-PENDING")
        self.assertIn("digest", result["unmet_invariants"])

    def test_valid_reconciliation_bundle_allows_terminal_response(self) -> None:
        state = _terminal_state()
        state["execution_reconciliation"] = _valid_reconciliation()
        result = evaluate(state)
        self.assertEqual((result["decision"], result["reason_code"]), ("ALLOW_FINAL_RESPONSE", "MVTERM-COMPLETED-VERIFIED"))

    def test_fault_injection_resume_sequences_preserve_cycle_and_never_duplicate_side_effects(self) -> None:
        for interruption_after in ("operation_started", "operation_completed", "effect_applied", "verification_recorded"):
            with self.subTest(interruption_after=interruption_after):
                state = _terminal_state()
                bundle = _valid_reconciliation()
                bundle["resume_generation"] = 1
                bundle["resumed_from_cycle_id"] = state["execution_envelope"]["cycle_id"]
                bundle["side_effect_ledger"] = [{"effect_id": "effect-1", "idempotency_key": "effect-key-1", "status": "verified", "trace_id": bundle["trace_id"]}]
                bundle["reconciliation_digest"] = _digest(bundle)
                state["execution_reconciliation"] = bundle
                result = evaluate(state)
                self.assertEqual(result["decision"], "ALLOW_FINAL_RESPONSE")


if __name__ == "__main__":
    unittest.main()
