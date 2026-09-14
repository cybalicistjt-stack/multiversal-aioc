from __future__ import annotations

import json
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SCRIPTS = ROOT / "scripts"
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))

import execution_event_ledger as ledger
import execution_integrity_gate as integrity
import execution_transaction_preflight as preflight
from execution_termination_preflight import evaluate


def _event(events: list[dict], *, run_id: str, event_type: str, timestamp: str, source: str, payload: dict | None = None) -> None:
    events.append(
        ledger.build_event(
            run_id=run_id,
            sequence=len(events) + 1,
            event_type=event_type,
            timestamp=timestamp,
            source=source,
            payload=payload or {},
            previous_digest=events[-1]["event_digest"] if events else None,
        )
    )


def _ledger_backed_checkpoint(root: Path, *, continue_turns: int = 1, stall_nudges: int = 0) -> tuple[dict, list[dict]]:
    run_id = "ARI-LEDGER-001-attempt-001"
    events: list[dict] = []
    _event(events, run_id=run_id, event_type="run_started", timestamp="2026-09-14T10:00:00-05:00", source="supervisor")
    for offset in range(continue_turns):
        _event(
            events,
            run_id=run_id,
            event_type="owner_continue",
            timestamp=f"2026-09-14T10:00:{offset + 1:02d}-05:00",
            source="owner",
        )
    for offset in range(stall_nudges):
        _event(
            events,
            run_id=run_id,
            event_type="owner_stall_nudge",
            timestamp=f"2026-09-14T10:01:{offset:02d}-05:00",
            source="owner",
        )
    _event(events, run_id=run_id, event_type="run_completed", timestamp="2026-09-14T10:10:00-05:00", source="supervisor")
    chain = ledger.validate_chain(events)
    ledger_path = Path("governance/ai/execution-events") / f"{run_id}.json"
    target = root / ledger_path
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(json.dumps({"events": events}), encoding="utf-8")
    checkpoint = {
        "attempt_id": run_id,
        "status": "completed_verified",
        # Deliberately contradictory wall-clock checkpoint timestamps prove that
        # ledger-backed timing is event-derived rather than checkpoint-authored.
        "started_at": "2026-09-14T08:00:00-05:00",
        "completed_at": "2026-09-14T12:00:00-05:00",
        "execution_target_minutes": 24,
        "execution_event_ledger": {
            "path": ledger_path.as_posix(),
            "run_id": run_id,
            "head_digest": chain["head_digest"],
        },
        "owner_interaction_observation": {
            "continue_turns": continue_turns,
            "stall_nudges": stall_nudges,
        },
        "convergence_control": {
            "owner_continue_count": continue_turns,
            "single_continue_achieved": continue_turns == 1 and stall_nudges == 0,
        },
    }
    return checkpoint, events


class ExecutionSystemV2Tests(unittest.TestCase):
    def _completed_state(self, elapsed: float) -> dict:
        cycle_id = "MV-CONT-016-CYCLE"
        trace_id = "MV-CONT-016-TRACE"
        reconciliation = {
            "desired_state": "terminal_verified",
            "trace_id": trace_id,
            "resume_generation": 0,
            "resumed_from_cycle_id": None,
            "operation_ledger": [{
                "operation_id": "terminal-op",
                "idempotency_key": "terminal-op-key",
                "status": "completed",
                "attempts": 1,
                "trace_id": trace_id,
            }],
            "next_operation_id": None,
            "side_effect_ledger": [],
            "progress": {
                "reconciliation_passes": 1,
                "consecutive_no_progress_passes": 0,
                "diagnostic_mode": False,
            },
            "verification_evidence": [{
                "evidence_id": "independent-acceptance",
                "kind": "deterministic_test",
                "result": "pass",
                "independent": True,
                "bound_cycle_id": cycle_id,
                "trace_id": trace_id,
            }],
        }
        import hashlib
        material = json.dumps(reconciliation, sort_keys=True, separators=(",", ":"), ensure_ascii=True).encode("utf-8")
        reconciliation["reconciliation_digest"] = hashlib.sha256(material).hexdigest()
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
                "cycle_id": cycle_id,
                "phase": "closed",
                "elapsed_active_minutes": elapsed,
                "closeout_switch_active_minute": 16,
                "target_cycle_minutes": 24,
                "safe_same_lane_work_available": False,
                "dynamic_fill_attempted": True,
                "closeout_complete": True,
                "fill_exit_reason": "terminal_invariants_satisfied",
            },
            "execution_reconciliation": reconciliation,
        }

    def test_terminal_invariants_allow_completion_before_latency_slo(self) -> None:
        result = evaluate(self._completed_state(11.0))
        self.assertEqual(result["decision"], "ALLOW_FINAL_RESPONSE")
        self.assertEqual(result["reason_code"], "MVTERM-COMPLETED-VERIFIED")

    def test_latency_slo_miss_does_not_block_correct_terminal_state(self) -> None:
        result = evaluate(self._completed_state(31.0))
        self.assertEqual(result["decision"], "ALLOW_FINAL_RESPONSE")
        decision = preflight.assess_precloseout_readiness({
            "terminal_invariants_satisfied": True,
            "elapsed_active_minutes": 31.0,
            "target_cycle_minutes": 24.0,
        })
        self.assertEqual(decision["decision"], "READY_FOR_CLOSEOUT")
        self.assertEqual(decision["latency_slo_status"], "missed")
        self.assertEqual(decision["latency_slo_overrun_minutes"], 7.0)

    def test_nonterminal_state_continues_even_after_latency_slo(self) -> None:
        decision = preflight.assess_precloseout_readiness({
            "terminal_invariants_satisfied": False,
            "elapsed_active_minutes": 31.0,
            "target_cycle_minutes": 24.0,
        })
        self.assertEqual(decision["decision"], "CONTINUE_SAME_CYCLE")
        self.assertEqual(decision["reason_code"], "MVEXEC-TERMINAL-INVARIANTS-PENDING")
        self.assertEqual(decision["latency_slo_status"], "missed")

    def test_event_ledger_derives_owner_interaction_truth(self) -> None:
        events: list[dict] = []
        _event(events, run_id="ARI-22B", event_type="run_started", timestamp="2026-09-14T09:12:06-05:00", source="supervisor")
        _event(events, run_id="ARI-22B", event_type="owner_continue", timestamp="2026-09-14T09:12:07-05:00", source="owner")
        _event(events, run_id="ARI-22B", event_type="owner_stall_nudge", timestamp="2026-09-14T09:40:00-05:00", source="owner")
        _event(events, run_id="ARI-22B", event_type="owner_continue", timestamp="2026-09-14T09:40:01-05:00", source="owner")
        _event(events, run_id="ARI-22B", event_type="run_completed", timestamp="2026-09-14T10:10:13-05:00", source="supervisor")
        self.assertEqual(ledger.validate_chain(events)["status"], "PASS")
        metrics = ledger.derive_metrics(events, latency_slo_minutes=24.0)
        self.assertEqual(metrics["owner_continue_count"], 2)
        self.assertEqual(metrics["owner_stall_nudge_count"], 1)
        self.assertFalse(metrics["single_continue_achieved"])
        self.assertAlmostEqual(metrics["owner_visible_wall_minutes"], 58.1167, places=3)
        self.assertEqual(metrics["latency_slo_status"], "missed")

    def test_event_ledger_detects_tampering(self) -> None:
        events: list[dict] = []
        _event(events, run_id="RUN-1", event_type="run_started", timestamp="2026-09-14T10:00:00-05:00", source="supervisor")
        _event(events, run_id="RUN-1", event_type="owner_continue", timestamp="2026-09-14T10:00:01-05:00", source="owner")
        events[0]["event_type"] = "rewritten_after_the_fact"
        with self.assertRaises(ledger.EventLedgerError):
            ledger.validate_chain(events)

    def test_execution_profile_makes_time_an_slo_not_terminal_gate(self) -> None:
        profile = json.loads((ROOT / "governance/ai/runtime/EXECUTION_PROFILE.json").read_text(encoding="utf-8"))
        timing = profile["timing"]
        self.assertEqual(timing["latency_slo_minutes"], 24)
        self.assertFalse(timing["minimum_runtime_gate"])
        self.assertEqual(profile["execution_hardening"]["event_ledger"], "scripts/execution_event_ledger.py")

    def test_integrity_gate_uses_event_ledger_as_source_of_truth(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            checkpoint, _ = _ledger_backed_checkpoint(root)
            truth = integrity.resolve_execution_truth(root, checkpoint, latency_slo_minutes=24.0)
            self.assertEqual(truth["source"], "event_ledger")
            self.assertEqual(truth["owner_continue_count"], 1)
            self.assertEqual(truth["owner_stall_nudge_count"], 0)
            self.assertTrue(truth["single_continue_achieved"])
            self.assertEqual(truth["owner_visible_timing"]["measurement_basis"], "execution_event_ledger")
            self.assertAlmostEqual(truth["owner_visible_timing"]["wall_elapsed_minutes"], 10.0)
            self.assertEqual(truth["owner_visible_timing"]["latency_slo_status"], "within_slo")

    def test_integrity_gate_rejects_checkpoint_projection_disagreement(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            checkpoint, _ = _ledger_backed_checkpoint(root)
            checkpoint["owner_interaction_observation"]["continue_turns"] = 2
            checkpoint["convergence_control"]["owner_continue_count"] = 2
            checkpoint["convergence_control"]["single_continue_achieved"] = False
            with self.assertRaises(integrity.ExecutionIntegrityError):
                integrity.resolve_execution_truth(root, checkpoint, latency_slo_minutes=24.0)

    def test_integrity_gate_rejects_tampered_or_rebound_ledger(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            checkpoint, events = _ledger_backed_checkpoint(root)
            checkpoint["execution_event_ledger"]["run_id"] = "OTHER-RUN"
            with self.assertRaises(integrity.ExecutionIntegrityError):
                integrity.resolve_execution_truth(root, checkpoint, latency_slo_minutes=24.0)

            checkpoint, events = _ledger_backed_checkpoint(root)
            ledger_path = root / checkpoint["execution_event_ledger"]["path"]
            events[0]["event_type"] = "tampered"
            ledger_path.write_text(json.dumps({"events": events}), encoding="utf-8")
            with self.assertRaises((integrity.ExecutionIntegrityError, ledger.EventLedgerError)):
                integrity.resolve_execution_truth(root, checkpoint, latency_slo_minutes=24.0)


if __name__ == "__main__":
    unittest.main()
