from __future__ import annotations

import hashlib
import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SCRIPTS = ROOT / "scripts"
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))

from execution_termination_preflight import evaluate  # noqa: E402


def _valid_reconciliation(cycle_id: str) -> dict:
    trace_id = f"TRACE-{cycle_id}"
    bundle = {
        "desired_state": "terminal_verified",
        "trace_id": trace_id,
        "resume_generation": 0,
        "resumed_from_cycle_id": None,
        "operation_ledger": [{
            "operation_id": "terminal-operation",
            "idempotency_key": f"{cycle_id}:terminal-operation",
            "status": "completed",
            "attempts": 1,
            "trace_id": trace_id,
        }],
        "next_operation_id": None,
        "side_effect_ledger": [],
        "progress": {"reconciliation_passes": 1, "consecutive_no_progress_passes": 0, "diagnostic_mode": False},
        "verification_evidence": [{
            "evidence_id": "evidence-001",
            "kind": "deterministic_test",
            "result": "pass",
            "independent": True,
            "bound_cycle_id": cycle_id,
            "trace_id": trace_id,
        }],
    }
    payload = json.dumps(bundle, sort_keys=True, separators=(",", ":"), ensure_ascii=True).encode("utf-8")
    bundle["reconciliation_digest"] = hashlib.sha256(payload).hexdigest()
    return bundle


def _envelope(*, phase: str = "closed", elapsed: float = 11.0, closeout_complete: bool = True, target: float = 24.0, switch: float = 16.0) -> dict:
    return {
        "cycle_id": "HAI-CYCLE-004",
        "phase": phase,
        "elapsed_active_minutes": elapsed,
        "closeout_switch_active_minute": switch,
        "target_cycle_minutes": target,
        "safe_same_lane_work_available": False,
        "dynamic_fill_attempted": True,
        "closeout_complete": closeout_complete,
        "fill_exit_reason": "terminal_invariants_satisfied" if phase == "closed" else ("closeout_switch_reached" if phase == "closeout" else None),
    }


class ExecutionEnvelopeGateTests(unittest.TestCase):
    def _completed_state(self) -> dict:
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
        }

    def test_nonterminal_fill_state_cannot_return(self) -> None:
        state = {**self._completed_state(), "execution_envelope": _envelope(phase="fill", elapsed=5.42, closeout_complete=False)}
        result = evaluate(state)
        self.assertEqual((result["decision"], result["reason_code"]), ("CONTINUE_EXECUTION", "MVTERM-ENVELOPE-FILL"))

    def test_incomplete_closeout_cannot_return(self) -> None:
        state = {**self._completed_state(), "execution_envelope": _envelope(phase="closeout", elapsed=16.1, closeout_complete=False)}
        result = evaluate(state)
        self.assertEqual((result["decision"], result["reason_code"]), ("CONTINUE_EXECUTION", "MVTERM-ENVELOPE-CLOSEOUT"))

    def test_terminal_state_before_latency_slo_returns_immediately(self) -> None:
        state = {**self._completed_state(), "execution_envelope": _envelope(elapsed=11.0), "execution_reconciliation": _valid_reconciliation("HAI-CYCLE-004")}
        result = evaluate(state)
        self.assertEqual((result["decision"], result["reason_code"]), ("ALLOW_FINAL_RESPONSE", "MVTERM-COMPLETED-VERIFIED"))
        self.assertEqual(result["telemetry"]["latency_slo_status"], "within_slo")

    def test_terminal_state_after_latency_slo_returns_and_records_miss(self) -> None:
        state = {**self._completed_state(), "execution_envelope": _envelope(elapsed=31.0), "execution_reconciliation": _valid_reconciliation("HAI-CYCLE-004")}
        result = evaluate(state)
        self.assertEqual((result["decision"], result["reason_code"]), ("ALLOW_FINAL_RESPONSE", "MVTERM-COMPLETED-VERIFIED"))
        self.assertEqual(result["telemetry"]["latency_slo_status"], "missed")
        self.assertEqual(result["telemetry"]["latency_slo_overrun_minutes"], 7.0)

    def test_custom_timing_values_are_telemetry_not_terminal_authority(self) -> None:
        state = {**self._completed_state(), "execution_envelope": _envelope(elapsed=6.0, target=6.0, switch=4.0), "execution_reconciliation": _valid_reconciliation("HAI-CYCLE-004")}
        result = evaluate(state)
        self.assertEqual(result["decision"], "ALLOW_FINAL_RESPONSE")

    def test_terminal_state_still_requires_reconciliation(self) -> None:
        state = {**self._completed_state(), "execution_envelope": _envelope(elapsed=11.0)}
        result = evaluate(state)
        self.assertEqual((result["decision"], result["reason_code"]), ("CONTINUE_EXECUTION", "MVTERM-RECONCILIATION-MISSING"))

    def test_missing_envelope_blocks_execution_mode_final_response(self) -> None:
        result = evaluate(self._completed_state())
        self.assertEqual((result["decision"], result["reason_code"]), ("CONTINUE_EXECUTION", "MVTERM-ENVELOPE-MISSING"))

    def test_execution_profile_defines_latency_slo_without_minimum_runtime(self) -> None:
        profile = json.loads((ROOT / "governance/ai/runtime/EXECUTION_PROFILE.json").read_text(encoding="utf-8"))
        timing = profile["timing"]
        envelope = profile["execution_envelope"]
        self.assertEqual(timing["latency_slo_minutes"], 24)
        self.assertFalse(timing["minimum_runtime_gate"])
        self.assertIn("latency SLO", envelope["latency_rule"])
        self.assertIn("Elapsed time never", envelope["terminal_rule"])
        self.assertIn("Conversation change", envelope["interruption_rule"])

    def test_bootstrap_treats_time_as_slo_not_permission_to_stop(self) -> None:
        bootstrap = (ROOT / "governance/ai/MULTIVERSAL_NEW_CONVERSATION_BOOTSTRAP.md").read_text(encoding="utf-8")
        self.assertIn("latency SLO", bootstrap)
        self.assertIn("minimum runtime", bootstrap)
        self.assertIn("terminal invariants", bootstrap)

    def test_efficiency_policy_treats_elapsed_time_as_telemetry(self) -> None:
        policy = (ROOT / "governance/ai/MULTIVERSAL_CHECKPOINT_AND_VALIDATION_EFFICIENCY_POLICY.md").read_text(encoding="utf-8")
        self.assertIn("latency SLO", policy)
        self.assertIn("minimum runtime", policy)
        self.assertIn("terminal invariants", policy)


if __name__ == "__main__":
    unittest.main()
