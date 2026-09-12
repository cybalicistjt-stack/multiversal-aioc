from __future__ import annotations

import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SCRIPTS = ROOT / "scripts"
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))

from execution_termination_preflight import evaluate  # noqa: E402


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

    def test_completed_logical_operation_cannot_end_cycle_while_fill_budget_and_safe_work_remain(self) -> None:
        state = {
            **self._completed_state(),
            "execution_envelope": {
                "cycle_id": "HAI-CYCLE-004",
                "phase": "fill",
                "elapsed_active_minutes": 5.42,
                "closeout_switch_active_minute": 16,
                "target_cycle_minutes": 24,
                "safe_same_lane_work_available": True,
                "dynamic_fill_attempted": False,
                "closeout_complete": False,
                "fill_exit_reason": None,
            },
        }
        result = evaluate(state)
        self.assertEqual(result["decision"], "CONTINUE_EXECUTION")
        self.assertEqual(result["reason_code"], "MVTERM-ENVELOPE-FILL")

    def test_operation_completion_must_dynamic_fill_instead_of_incrementing_cycle(self) -> None:
        state = {
            **self._completed_state(),
            "execution_envelope": {
                "cycle_id": "HAI-CYCLE-004",
                "phase": "fill",
                "elapsed_active_minutes": 9.22,
                "closeout_switch_active_minute": 16,
                "target_cycle_minutes": 24,
                "safe_same_lane_work_available": True,
                "dynamic_fill_attempted": True,
                "closeout_complete": False,
                "fill_exit_reason": None,
            },
        }
        result = evaluate(state)
        self.assertEqual((result["decision"], result["reason_code"]), ("CONTINUE_EXECUTION", "MVTERM-ENVELOPE-FILL"))

    def test_closeout_may_start_at_switch_but_final_response_waits_for_shared_closeout(self) -> None:
        state = {
            **self._completed_state(),
            "execution_envelope": {
                "cycle_id": "HAI-CYCLE-004",
                "phase": "closeout",
                "elapsed_active_minutes": 16.1,
                "closeout_switch_active_minute": 16,
                "target_cycle_minutes": 24,
                "safe_same_lane_work_available": True,
                "dynamic_fill_attempted": True,
                "closeout_complete": False,
                "fill_exit_reason": "closeout_switch_reached",
            },
        }
        result = evaluate(state)
        self.assertEqual((result["decision"], result["reason_code"]), ("CONTINUE_EXECUTION", "MVTERM-ENVELOPE-CLOSEOUT"))

    def test_closed_envelope_still_cannot_return_before_target_when_work_was_not_exhausted(self) -> None:
        state = {
            **self._completed_state(),
            "execution_envelope": {
                "cycle_id": "HAI-CYCLE-004",
                "phase": "closed",
                "elapsed_active_minutes": 23.4,
                "closeout_switch_active_minute": 16,
                "target_cycle_minutes": 24,
                "safe_same_lane_work_available": False,
                "dynamic_fill_attempted": True,
                "closeout_complete": True,
                "fill_exit_reason": "closeout_switch_reached",
            },
        }
        result = evaluate(state)
        self.assertEqual((result["decision"], result["reason_code"]), ("CONTINUE_EXECUTION", "MVTERM-ENVELOPE-TARGET-PENDING"))

    def test_final_response_allowed_after_target_and_shared_closeout(self) -> None:
        state = {
            **self._completed_state(),
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
        result = evaluate(state)
        self.assertEqual((result["decision"], result["reason_code"]), ("ALLOW_FINAL_RESPONSE", "MVTERM-COMPLETED-VERIFIED"))

    def test_early_exhaustion_requires_explicit_no_safe_work_evidence(self) -> None:
        state = {
            **self._completed_state(),
            "execution_envelope": {
                "cycle_id": "HAI-CYCLE-004",
                "phase": "closed",
                "elapsed_active_minutes": 11.0,
                "closeout_switch_active_minute": 16,
                "target_cycle_minutes": 24,
                "safe_same_lane_work_available": False,
                "dynamic_fill_attempted": True,
                "closeout_complete": True,
                "fill_exit_reason": "safe_work_exhausted",
            },
        }
        result = evaluate(state)
        self.assertEqual((result["decision"], result["reason_code"]), ("ALLOW_FINAL_RESPONSE", "MVTERM-COMPLETED-VERIFIED"))

    def test_early_exhaustion_without_dynamic_fill_attempt_is_rejected(self) -> None:
        state = {
            **self._completed_state(),
            "execution_envelope": {
                "cycle_id": "HAI-CYCLE-004",
                "phase": "closed",
                "elapsed_active_minutes": 7.0,
                "closeout_switch_active_minute": 16,
                "target_cycle_minutes": 24,
                "safe_same_lane_work_available": False,
                "dynamic_fill_attempted": False,
                "closeout_complete": True,
                "fill_exit_reason": "safe_work_exhausted",
            },
        }
        result = evaluate(state)
        self.assertEqual((result["decision"], result["reason_code"]), ("CONTINUE_EXECUTION", "MVTERM-ENVELOPE-EARLY-EXIT-UNPROVEN"))

    def test_executor_cannot_shrink_the_canonical_envelope_target(self) -> None:
        state = {
            **self._completed_state(),
            "execution_envelope": {
                "cycle_id": "HAI-CYCLE-004",
                "phase": "closed",
                "elapsed_active_minutes": 6.0,
                "closeout_switch_active_minute": 4,
                "target_cycle_minutes": 6,
                "safe_same_lane_work_available": False,
                "dynamic_fill_attempted": True,
                "closeout_complete": True,
                "fill_exit_reason": "closeout_switch_reached",
            },
        }
        result = evaluate(state)
        self.assertEqual((result["decision"], result["reason_code"]), ("CONTINUE_EXECUTION", "MVTERM-ENVELOPE-POLICY-MISMATCH"))

    def test_missing_envelope_blocks_execution_mode_final_response(self) -> None:
        result = evaluate(self._completed_state())
        self.assertEqual((result["decision"], result["reason_code"]), ("CONTINUE_EXECUTION", "MVTERM-ENVELOPE-MISSING"))

    def test_execution_profile_persists_cycle_identity_and_dynamic_fill(self) -> None:
        profile = json.loads((ROOT / "governance/ai/runtime/EXECUTION_PROFILE.json").read_text(encoding="utf-8"))
        envelope = profile["execution_envelope"]
        self.assertTrue(envelope["terminal_gate_required"])
        self.assertIn("remains stable across logical operations", envelope["cycle_identity_rule"])
        self.assertIn("immediately selects the next safe same-lane operation", envelope["dynamic_fill_rule"])
        self.assertIn("Conversation change", envelope["interruption_rule"])

    def test_bootstrap_requires_envelope_recovery_and_forbids_operation_boundary_stop(self) -> None:
        bootstrap = (ROOT / "governance/ai/MULTIVERSAL_NEW_CONVERSATION_BOOTSTRAP.md").read_text(encoding="utf-8")
        required = [
            "execution envelope",
            "logical operation is not a cycle boundary",
            "resume the same `cycle_id`",
            "dynamic fill",
            "safe same-lane work",
            "24-minute",
        ]
        for phrase in required:
            with self.subTest(phrase=phrase):
                self.assertIn(phrase, bootstrap)

    def test_efficiency_policy_defines_capacity_based_cycle_boundary(self) -> None:
        policy = (ROOT / "governance/ai/MULTIVERSAL_CHECKPOINT_AND_VALIDATION_EFFICIENCY_POLICY.md").read_text(encoding="utf-8")
        required = [
            "execution envelope",
            "logical-operation completion",
            "dynamic fill",
            "safe same-lane work",
            "cycle identity",
            "24-minute",
        ]
        for phrase in required:
            with self.subTest(phrase=phrase):
                self.assertIn(phrase, policy)


if __name__ == "__main__":
    unittest.main()
