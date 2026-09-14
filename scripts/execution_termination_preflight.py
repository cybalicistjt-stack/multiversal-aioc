#!/usr/bin/env python3
"""State-driven final-response gate for governed Multiversal execution."""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any, Mapping

CONTRACT_PATH = Path("governance/ai/interaction-system/EXECUTION_TERMINATION_CONTRACT.json")
CASES_PATH = Path("governance/ai/interaction-system/evaluation/EXECUTION_TERMINATION_CASES_V2.json")
PROFILE_PATH = Path("governance/ai/runtime/EXECUTION_PROFILE.json")
EXECUTION_MODES = {"execution", "status_and_continue", "keep_going"}
NON_EXECUTION_MODES = {"get_ready", "status_only", "analysis_only"}
BLOCKER_CLASSES = {"owner_only", "environment_unavailable", "source_unavailable", "safety", "irrecoverable_external"}
SELF_IMPOSED_PRESSURE_MARKERS = {
    "response budget", "tool budget", "token pressure", "context pressure",
    "partial closeout", "too many tool calls", "conversation length", "tool execution cut off",
}
PULL_REQUEST_STATES = {None, "none", "open", "merged", "closed_unmerged"}
VALIDATION_STATES = {None, "none", "queued", "in_progress", "failed", "passed", "superseded"}
ENVELOPE_PHASES = {"fill", "closeout", "closed"}
ENVELOPE_FILL_EXIT_REASONS = {None, "closeout_switch_reached", "safe_work_exhausted", "terminal_invariants_satisfied"}
OPERATION_STATUSES = {"planned", "in_progress", "completed", "skipped"}
TERMINAL_OPERATION_STATUSES = {"completed", "skipped"}
SIDE_EFFECT_STATUSES = {"planned", "applied", "verified", "compensated"}
TERMINAL_SIDE_EFFECT_STATUSES = {"verified", "compensated"}
EVIDENCE_KINDS = {"ci_run", "deterministic_test", "source_crosscheck", "human_owner", "external_system"}


class PreflightError(RuntimeError):
    def __init__(self, code: str, message: str) -> None:
        super().__init__(message)
        self.code = code


def _require(condition: bool, code: str, message: str) -> None:
    if not condition:
        raise PreflightError(code, message)


def _load_json(path: Path) -> dict[str, Any]:
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError as exc:
        raise PreflightError("MVTERM-INPUT-MISSING", f"missing JSON input: {path}") from exc
    except json.JSONDecodeError as exc:
        raise PreflightError("MVTERM-INPUT-INVALID", f"invalid JSON input {path}: {exc}") from exc
    _require(isinstance(value, dict), "MVTERM-INPUT-TYPE", f"expected object JSON: {path}")
    return value


def _decision(decision: str, reason_code: str, reason: str, *, unmet_invariants: list[str] | None = None, telemetry: dict[str, Any] | None = None) -> dict[str, Any]:
    result: dict[str, Any] = {
        "schema_version": "2.0.0",
        "status": "PASS",
        "decision": decision,
        "reason_code": reason_code,
        "reason": reason,
    }
    if unmet_invariants is not None:
        result["unmet_invariants"] = sorted(set(unmet_invariants))
    if telemetry:
        result["telemetry"] = telemetry
    return result


def _contains_self_imposed_pressure(evidence: Any) -> bool:
    if not isinstance(evidence, list):
        return False
    text = " ".join(item for item in evidence if isinstance(item, str)).lower()
    return any(marker in text for marker in SELF_IMPOSED_PRESSURE_MARKERS)


def _is_number(value: Any) -> bool:
    return isinstance(value, (int, float)) and not isinstance(value, bool)


def _canonical_reconciliation_digest(bundle: Mapping[str, Any]) -> str:
    material = {key: value for key, value in bundle.items() if key != "reconciliation_digest"}
    payload = json.dumps(material, sort_keys=True, separators=(",", ":"), ensure_ascii=True).encode("utf-8")
    return hashlib.sha256(payload).hexdigest()


def _evaluate_execution_envelope(state: Mapping[str, Any]) -> dict[str, Any] | None:
    """Require lifecycle closure; timing is telemetry, never terminal authority."""
    envelope = state.get("execution_envelope")
    if not isinstance(envelope, Mapping):
        return _decision(
            "CONTINUE_EXECUTION", "MVTERM-ENVELOPE-MISSING",
            "execution-mode terminal response requires an explicit durable execution envelope",
        )

    cycle_id = envelope.get("cycle_id")
    phase = envelope.get("phase")
    elapsed = envelope.get("elapsed_active_minutes")
    target = envelope.get("target_cycle_minutes")
    switch = envelope.get("closeout_switch_active_minute")
    safe_work = envelope.get("safe_same_lane_work_available")
    dynamic_fill = envelope.get("dynamic_fill_attempted")
    closeout_complete = envelope.get("closeout_complete")
    fill_exit_reason = envelope.get("fill_exit_reason")

    if not isinstance(cycle_id, str) or not cycle_id.strip():
        return _decision("CONTINUE_EXECUTION", "MVTERM-ENVELOPE-INVALID", "execution envelope requires a stable non-empty cycle_id")
    if phase not in ENVELOPE_PHASES:
        return _decision("CONTINUE_EXECUTION", "MVTERM-ENVELOPE-INVALID", f"unsupported execution-envelope phase: {phase!r}")
    if not _is_number(elapsed) or float(elapsed) < 0:
        return _decision("CONTINUE_EXECUTION", "MVTERM-ENVELOPE-INVALID", "elapsed_active_minutes must be a non-negative number")
    if not _is_number(target) or float(target) <= 0 or not _is_number(switch) or float(switch) < 0:
        return _decision("CONTINUE_EXECUTION", "MVTERM-ENVELOPE-INVALID", "execution envelope timing telemetry must use non-negative numeric values")
    if not isinstance(safe_work, bool) or not isinstance(dynamic_fill, bool) or not isinstance(closeout_complete, bool):
        return _decision("CONTINUE_EXECUTION", "MVTERM-ENVELOPE-INVALID", "execution envelope requires boolean safe-work, dynamic-fill and closeout-complete fields")
    if fill_exit_reason not in ENVELOPE_FILL_EXIT_REASONS:
        return _decision("CONTINUE_EXECUTION", "MVTERM-ENVELOPE-INVALID", f"unsupported fill_exit_reason: {fill_exit_reason!r}")

    target_f = float(target)
    elapsed_f = float(elapsed)
    telemetry = {
        "elapsed_active_minutes": elapsed_f,
        "latency_slo_minutes": target_f,
        "latency_slo_status": "within_slo" if elapsed_f <= target_f else "missed",
        "latency_slo_overrun_minutes": max(elapsed_f - target_f, 0.0),
    }

    if phase == "fill":
        return _decision(
            "CONTINUE_EXECUTION", "MVTERM-ENVELOPE-FILL",
            f"cycle {cycle_id} remains in nonterminal fill execution",
            telemetry=telemetry,
        )
    if phase == "closeout" or not closeout_complete:
        return _decision(
            "CONTINUE_EXECUTION", "MVTERM-ENVELOPE-CLOSEOUT",
            f"cycle {cycle_id} has not completed terminal closeout",
            telemetry=telemetry,
        )
    if phase != "closed":
        return _decision("CONTINUE_EXECUTION", "MVTERM-ENVELOPE-INVALID", "terminal execution requires phase=closed")
    return None


def _evaluate_execution_reconciliation(state: Mapping[str, Any]) -> dict[str, Any] | None:
    """Reconcile all terminal invariants in one pass."""
    bundle = state.get("execution_reconciliation")
    if not isinstance(bundle, Mapping):
        return _decision(
            "CONTINUE_EXECUTION", "MVTERM-RECONCILIATION-MISSING",
            "terminal execution requires an independent reconciliation bundle",
            unmet_invariants=["reconciliation_bundle"],
        )

    envelope = state.get("execution_envelope", {})
    cycle_id = envelope.get("cycle_id") if isinstance(envelope, Mapping) else None
    structural: list[str] = []
    unmet: list[str] = []

    desired_state = bundle.get("desired_state")
    trace_id = bundle.get("trace_id")
    resume_generation = bundle.get("resume_generation")
    resumed_from_cycle_id = bundle.get("resumed_from_cycle_id")
    operation_ledger = bundle.get("operation_ledger")
    next_operation_id = bundle.get("next_operation_id")
    side_effect_ledger = bundle.get("side_effect_ledger")
    progress = bundle.get("progress")
    evidence = bundle.get("verification_evidence")
    digest = bundle.get("reconciliation_digest")

    if desired_state != "terminal_verified":
        unmet.append("desired_state")
    if not isinstance(trace_id, str) or not trace_id.strip():
        structural.append("trace_identity")
    if not isinstance(resume_generation, int) or isinstance(resume_generation, bool) or resume_generation < 0:
        structural.append("resume_identity")
    else:
        if resume_generation == 0 and resumed_from_cycle_id is not None:
            unmet.append("resume_identity")
        if resume_generation > 0 and resumed_from_cycle_id != cycle_id:
            unmet.append("resume_identity")

    if not isinstance(operation_ledger, list) or not operation_ledger:
        structural.append("operation_ledger")
    else:
        operation_ids: set[str] = set()
        operation_keys: set[str] = set()
        for row in operation_ledger:
            if not isinstance(row, Mapping):
                structural.append("operation_ledger")
                continue
            operation_id = row.get("operation_id")
            idempotency_key = row.get("idempotency_key")
            status = row.get("status")
            attempts = row.get("attempts")
            row_trace = row.get("trace_id")
            if not isinstance(operation_id, str) or not operation_id.strip() or operation_id in operation_ids:
                structural.append("operation_identity")
            else:
                operation_ids.add(operation_id)
            if not isinstance(idempotency_key, str) or not idempotency_key.strip() or idempotency_key in operation_keys:
                structural.append("operation_identity")
            else:
                operation_keys.add(idempotency_key)
            if status not in OPERATION_STATUSES:
                structural.append("operation_status")
            elif status not in TERMINAL_OPERATION_STATUSES:
                unmet.append("operations_terminal")
            if not isinstance(attempts, int) or isinstance(attempts, bool) or attempts < 1:
                structural.append("operation_attempts")
            if isinstance(trace_id, str) and row_trace != trace_id:
                unmet.append("trace_continuity")

    if next_operation_id is not None:
        unmet.append("next_operation")

    if not isinstance(side_effect_ledger, list):
        structural.append("side_effect_ledger")
    else:
        effect_ids: set[str] = set()
        effect_keys: set[str] = set()
        for row in side_effect_ledger:
            if not isinstance(row, Mapping):
                structural.append("side_effect_ledger")
                continue
            effect_id = row.get("effect_id")
            idempotency_key = row.get("idempotency_key")
            status = row.get("status")
            row_trace = row.get("trace_id")
            if not isinstance(effect_id, str) or not effect_id.strip() or effect_id in effect_ids:
                structural.append("side_effect_identity")
            else:
                effect_ids.add(effect_id)
            if not isinstance(idempotency_key, str) or not idempotency_key.strip() or idempotency_key in effect_keys:
                structural.append("side_effect_identity")
            else:
                effect_keys.add(idempotency_key)
            if status not in SIDE_EFFECT_STATUSES:
                structural.append("side_effect_status")
            elif status not in TERMINAL_SIDE_EFFECT_STATUSES:
                unmet.append("side_effects")
            if isinstance(trace_id, str) and row_trace != trace_id:
                unmet.append("trace_continuity")

    if not isinstance(progress, Mapping):
        structural.append("progress")
    else:
        passes = progress.get("reconciliation_passes")
        no_progress = progress.get("consecutive_no_progress_passes")
        diagnostic = progress.get("diagnostic_mode")
        if not isinstance(passes, int) or isinstance(passes, bool) or passes < 1:
            structural.append("progress")
        if not isinstance(no_progress, int) or isinstance(no_progress, bool) or no_progress < 0:
            structural.append("progress")
        elif no_progress != 0:
            unmet.append("liveness")
        if not isinstance(diagnostic, bool):
            structural.append("progress")

    if not isinstance(evidence, list) or not evidence:
        unmet.append("independent_evidence")
    else:
        independent_pass = False
        seen_evidence: set[str] = set()
        for row in evidence:
            if not isinstance(row, Mapping):
                structural.append("verification_evidence")
                continue
            evidence_id = row.get("evidence_id")
            kind = row.get("kind")
            result = row.get("result")
            independent = row.get("independent")
            bound_cycle_id = row.get("bound_cycle_id")
            row_trace = row.get("trace_id")
            if not isinstance(evidence_id, str) or not evidence_id.strip() or evidence_id in seen_evidence:
                structural.append("verification_evidence")
            else:
                seen_evidence.add(evidence_id)
            if kind not in EVIDENCE_KINDS or result not in {"pass", "fail"} or not isinstance(independent, bool):
                structural.append("verification_evidence")
            if bound_cycle_id != cycle_id:
                unmet.append("evidence_cycle_binding")
            if isinstance(trace_id, str) and row_trace != trace_id:
                unmet.append("trace_continuity")
            if result == "pass" and independent is True and bound_cycle_id == cycle_id and row_trace == trace_id:
                independent_pass = True
        if not independent_pass:
            unmet.append("independent_evidence")

    if not isinstance(digest, str) or len(digest) != 64 or any(ch not in "0123456789abcdef" for ch in digest):
        structural.append("digest")
    elif digest != _canonical_reconciliation_digest(bundle):
        unmet.append("digest")

    if structural:
        return _decision(
            "CONTINUE_EXECUTION", "MVTERM-RECONCILIATION-INVALID",
            "execution reconciliation has structurally invalid or duplicate durable identities",
            unmet_invariants=structural + unmet,
        )
    if unmet:
        return _decision(
            "CONTINUE_EXECUTION", "MVTERM-RECONCILIATION-PENDING",
            "terminal invariants remain unsatisfied; repair the returned set before another terminal attempt",
            unmet_invariants=unmet,
        )
    return None


def evaluate(state: Mapping[str, Any]) -> dict[str, Any]:
    mode = state.get("command_mode")
    _require(mode in EXECUTION_MODES | NON_EXECUTION_MODES, "MVTERM-MODE-INVALID", f"unsupported command_mode: {mode!r}")
    status = state.get("work_item_status")
    _require(isinstance(status, str) and bool(status.strip()), "MVTERM-STATUS-MISSING", "work_item_status must be a non-empty string")
    active_async = state.get("active_async_operations")
    _require(isinstance(active_async, int) and not isinstance(active_async, bool) and active_async >= 0, "MVTERM-ASYNC-INVALID", "active_async_operations must be a non-negative integer")
    pending = state.get("pending_authorized_steps")
    _require(isinstance(pending, list) and all(isinstance(item, str) for item in pending), "MVTERM-PENDING-INVALID", "pending_authorized_steps must be an array of strings")

    successor_required = state.get("successor_selection_required")
    successor_selected = state.get("successor_selected")
    boundary_completed = state.get("requested_boundary_completed")
    for key, value in (
        ("successor_selection_required", successor_required),
        ("successor_selected", successor_selected),
        ("requested_boundary_completed", boundary_completed),
    ):
        _require(isinstance(value, bool), "MVTERM-BOOLEAN-INVALID", f"{key} must be boolean")

    pull_request_state = state.get("pull_request_state")
    validation_state = state.get("current_head_validation_state")
    closeout_pending = state.get("merge_closeout_pending", False)
    _require(pull_request_state in PULL_REQUEST_STATES, "MVTERM-PR-STATE-INVALID", f"unsupported pull_request_state: {pull_request_state!r}")
    _require(validation_state in VALIDATION_STATES, "MVTERM-VALIDATION-STATE-INVALID", f"unsupported current_head_validation_state: {validation_state!r}")
    _require(isinstance(closeout_pending, bool), "MVTERM-CLOSEOUT-STATE-INVALID", "merge_closeout_pending must be boolean")

    if mode in NON_EXECUTION_MODES:
        return _decision("ALLOW_FINAL_RESPONSE", "MVTERM-EXPLICIT-NONEXECUTION", f"owner selected explicit non-execution mode {mode}")
    if pull_request_state == "open":
        return _decision("CONTINUE_EXECUTION", "MVTERM-PR-OPEN", "the current governed pull request remains open")
    if validation_state in {"queued", "in_progress"}:
        return _decision("CONTINUE_EXECUTION", "MVTERM-VALIDATION-ACTIVE", f"current exact-head validation remains {validation_state}")
    if pull_request_state == "merged" and closeout_pending:
        return _decision("CONTINUE_EXECUTION", "MVTERM-CLOSEOUT-PENDING", "merge succeeded but canonical closeout remains pending")
    if active_async:
        return _decision("CONTINUE_EXECUTION", "MVTERM-ASYNC-ACTIVE", f"{active_async} required asynchronous operation(s) remain active")

    if status == "completed_verified":
        if successor_required and not successor_selected:
            return _decision("CONTINUE_EXECUTION", "MVTERM-SUCCESSOR-PENDING", "completed work still requires canonical strict-successor selection")
        if mode == "keep_going" and not boundary_completed:
            return _decision("CONTINUE_EXECUTION", "MVTERM-BOUNDARY-PENDING", "the owner-requested keep-going boundary is not complete")
        if pending:
            return _decision("CONTINUE_EXECUTION", "MVTERM-AUTHORIZED-WORK-PENDING", "authorized closeout work remains after completion evidence")
        envelope_decision = _evaluate_execution_envelope(state)
        if envelope_decision is not None:
            return envelope_decision
        reconciliation_decision = _evaluate_execution_reconciliation(state)
        if reconciliation_decision is not None:
            return reconciliation_decision
        envelope = state.get("execution_envelope", {})
        elapsed = float(envelope.get("elapsed_active_minutes", 0.0)) if isinstance(envelope, Mapping) else 0.0
        target = float(envelope.get("target_cycle_minutes", 24.0)) if isinstance(envelope, Mapping) else 24.0
        return _decision(
            "ALLOW_FINAL_RESPONSE", "MVTERM-COMPLETED-VERIFIED",
            "the bounded unit is completed_verified and all terminal invariants are reconciled",
            telemetry={
                "elapsed_active_minutes": elapsed,
                "latency_slo_minutes": target,
                "latency_slo_status": "within_slo" if elapsed <= target else "missed",
                "latency_slo_overrun_minutes": max(elapsed - target, 0.0),
            },
        )

    blocker = state.get("genuine_blocker")
    if isinstance(blocker, Mapping):
        blocker_class = blocker.get("class")
        evidence = blocker.get("evidence")
        recovery_attempted = blocker.get("recovery_attempted")
        blocks_all = blocker.get("blocks_all_authorized_progress")
        if blocker_class == "environment_unavailable" and _contains_self_imposed_pressure(evidence):
            return _decision("CONTINUE_EXECUTION", "MVTERM-SELF-IMPOSED-PRESSURE", "self-imposed response/tool/context pressure is not external blocker evidence")
        if (
            blocker_class in BLOCKER_CLASSES
            and isinstance(evidence, list)
            and any(isinstance(item, str) and item.strip() for item in evidence)
            and recovery_attempted is True
            and blocks_all is True
        ):
            return _decision("ALLOW_FINAL_RESPONSE", "MVTERM-GENUINE-BLOCKER", f"verified {blocker_class} blocker prevents all further authorized progress")
        return _decision("CONTINUE_EXECUTION", "MVTERM-BLOCKER-EVIDENCE-INSUFFICIENT", "claimed blocker lacks required class, evidence, recovery, or all-progress proof")

    if pending:
        return _decision("CONTINUE_EXECUTION", "MVTERM-AUTHORIZED-WORK-PENDING", f"{len(pending)} authorized step(s) remain")
    return _decision("CONTINUE_EXECUTION", "MVTERM-NONTERMINAL-STATE", f"work item remains {status!r} without a verified terminal condition")


def self_test(root: Path) -> dict[str, Any]:
    contract = _load_json(root / CONTRACT_PATH)
    _require(contract.get("schema_version") == "1.7.0", "MVTERM-CONTRACT-SCHEMA", "termination contract schema mismatch")
    _require(contract.get("control_id") == "C-EXECUTION-TERMINATION-GATE", "MVTERM-CONTRACT-ID", "termination contract control identity mismatch")
    profile = _load_json(root / PROFILE_PATH)
    timing = profile.get("timing", {})
    envelope_policy = profile.get("execution_envelope", {})
    reconciliation_policy = profile.get("execution_reconciliation", {})
    hardening = profile.get("execution_hardening", {})
    _require(timing.get("latency_slo_minutes") == 24, "MVTERM-LATENCY-SLO", "execution profile latency SLO must be 24 minutes")
    _require(timing.get("minimum_runtime_gate") is False, "MVTERM-MINIMUM-RUNTIME", "execution profile must not impose a minimum runtime gate")
    _require(envelope_policy.get("terminal_gate_required") is True, "MVTERM-ENVELOPE-PROFILE-GATE", "execution profile must require lifecycle terminal gating")
    _require(reconciliation_policy.get("terminal_gate_required") is True and reconciliation_policy.get("reconcile_all_invariants_in_one_pass") is True, "MVTERM-RECONCILIATION-PROFILE-GATE", "execution profile must require one-pass terminal reconciliation")
    _require(hardening.get("event_ledger") == "scripts/execution_event_ledger.py", "MVTERM-EVENT-LEDGER", "execution profile must register the event-ledger primitive")

    cases = _load_json(root / CASES_PATH)
    rows = cases.get("cases")
    _require(isinstance(rows, list) and len(rows) >= 18, "MVTERM-CASES-MISSING", "termination preflight requires at least eighteen v2 regression cases")
    seen: set[str] = set()
    for row in rows:
        _require(isinstance(row, Mapping), "MVTERM-CASE-TYPE", "termination case must be an object")
        case_id = row.get("case_id")
        _require(isinstance(case_id, str) and case_id not in seen, "MVTERM-CASE-ID", f"invalid or duplicate termination case id: {case_id!r}")
        seen.add(case_id)
        observed = evaluate(row.get("state", {}))
        _require(observed["decision"] == row.get("expected_decision"), "MVTERM-CASE-DECISION", f"{case_id}: expected {row.get('expected_decision')}, observed {observed['decision']}")
        _require(observed["reason_code"] == row.get("expected_reason_code"), "MVTERM-CASE-REASON", f"{case_id}: expected {row.get('expected_reason_code')}, observed {observed['reason_code']}")
    return {
        "schema_version": "2.0.0",
        "status": "PASS",
        "control_id": "C-EXECUTION-TERMINATION-GATE",
        "cases_passed": len(rows),
        "case_ids": sorted(seen),
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--state")
    parser.add_argument("--self-test", action="store_true")
    parser.add_argument("--root", default=".")
    parser.add_argument("--output")
    args = parser.parse_args()
    try:
        _require(bool(args.state) ^ bool(args.self_test), "MVTERM-INVOCATION", "choose exactly one of --state or --self-test")
        result = self_test(Path(args.root).resolve()) if args.self_test else evaluate(_load_json(Path(args.state).resolve()))
    except (OSError, PreflightError) as exc:
        code = exc.code if isinstance(exc, PreflightError) else "MVTERM-IO"
        result = {"schema_version": "2.0.0", "status": "FAIL", "decision": "CONTINUE_EXECUTION", "reason_code": code, "reason": str(exc)}
    payload = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.output:
        Path(args.output).write_text(payload, encoding="utf-8")
    print(payload, end="")
    return 0 if result["status"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
