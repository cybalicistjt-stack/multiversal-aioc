#!/usr/bin/env python3
from __future__ import annotations

import argparse
import copy
import json
from datetime import datetime
from pathlib import Path
from typing import Any, Mapping

import execution_environment_admission as environment
import execution_event_ledger as event_ledger
import execution_merge_authorization as merge_authorization
import validate_execution_convergence as convergence

POINTER_PATH = Path("governance/ai/runtime/CURRENT_WORK_POINTER.json")
PROFILE_PATH = Path("governance/ai/runtime/EXECUTION_PROFILE.json")
CORRECTION_PATH = Path("governance/ai/execution-audits/ARI-22B_EXECUTION_CORRECTION_2026-09-14.json")


class ExecutionIntegrityError(RuntimeError):
    pass


def _require(condition: bool, message: str) -> None:
    if not condition:
        raise ExecutionIntegrityError(message)


def _load_json(path: Path) -> dict[str, Any]:
    value = json.loads(path.read_text(encoding="utf-8"))
    _require(isinstance(value, dict), f"expected object JSON: {path}")
    return value


def _valid_digest(value: Any) -> bool:
    return (
        isinstance(value, str)
        and len(value) == 64
        and all(ch in "0123456789abcdef" for ch in value)
    )


def measure_owner_visible_timing(checkpoint: Mapping[str, Any]) -> dict[str, Any]:
    """Legacy compatibility timing for attempts completed before event-ledger enforcement."""
    try:
        started = datetime.fromisoformat(str(checkpoint["started_at"]))
        completed = datetime.fromisoformat(str(checkpoint["completed_at"]))
    except (KeyError, TypeError, ValueError) as exc:
        raise ExecutionIntegrityError("completed attempt requires parseable started_at and completed_at") from exc
    wall = (completed - started).total_seconds() / 60.0
    _require(wall >= 0, "completed_at precedes started_at")
    target_raw = checkpoint.get("execution_target_minutes", checkpoint.get("estimated_active_minutes"))
    _require(isinstance(target_raw, (int, float)) and not isinstance(target_raw, bool) and target_raw > 0, "execution target minutes missing")
    target = float(target_raw)
    return {
        "measurement_basis": "checkpoint_started_at_to_completed_at",
        "wall_elapsed_minutes": round(wall, 4),
        "target_minutes": target,
        "target_met": wall <= target,
        "synthetic_active_minutes_substitute": False,
    }


def _load_execution_events(root: Path, relative_path: str) -> list[dict[str, Any]]:
    rel = Path(relative_path)
    _require(not rel.is_absolute() and ".." not in rel.parts, "execution event ledger path must be repository-relative")
    target = root.resolve() / rel
    try:
        value = json.loads(target.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise ExecutionIntegrityError(f"unable to load execution event ledger {relative_path}: {exc}") from exc
    if isinstance(value, dict):
        value = value.get("events")
    _require(isinstance(value, list), "execution event ledger must be an event array or object containing events")
    _require(all(isinstance(row, dict) for row in value), "execution event ledger contains a non-object event")
    return value


def resolve_execution_truth(
    root: Path,
    checkpoint: Mapping[str, Any],
    *,
    latency_slo_minutes: float,
) -> dict[str, Any]:
    """Resolve owner-interaction and latency truth from events when a ledger is declared.

    Legacy attempts without a ledger retain checkpoint/correction compatibility so
    pre-v2 history such as ARI-22B remains inspectable rather than rewritten.
    """
    _require(
        isinstance(latency_slo_minutes, (int, float))
        and not isinstance(latency_slo_minutes, bool)
        and float(latency_slo_minutes) > 0,
        "latency_slo_minutes must be a positive number",
    )
    reference = checkpoint.get("execution_event_ledger")
    observation = checkpoint.get("owner_interaction_observation")
    control = checkpoint.get("convergence_control")

    if reference is None:
        _require(isinstance(observation, Mapping), "legacy checkpoint owner_interaction_observation missing")
        _require(isinstance(control, Mapping), "legacy checkpoint convergence_control missing")
        turns = observation.get("continue_turns")
        stall_nudges = observation.get("stall_nudges")
        _require(isinstance(turns, int) and not isinstance(turns, bool) and turns >= 1, "legacy continue_turns invalid")
        _require(isinstance(stall_nudges, int) and not isinstance(stall_nudges, bool) and stall_nudges >= 0, "legacy stall_nudges invalid")
        _require(control.get("owner_continue_count") == turns, "legacy owner Continue count contradicts owner observation")
        achieved = control.get("single_continue_achieved")
        _require(isinstance(achieved, bool), "legacy single_continue_achieved missing")
        if turns > 1:
            _require(achieved is False, "legacy multi-Continue attempt cannot certify single-Continue success")
        return {
            "source": "legacy_checkpoint",
            "owner_continue_count": turns,
            "owner_stall_nudge_count": stall_nudges,
            "single_continue_achieved": achieved,
            "owner_visible_timing": measure_owner_visible_timing(checkpoint),
        }

    _require(isinstance(reference, Mapping), "execution_event_ledger reference must be an object")
    path = reference.get("path")
    run_id = reference.get("run_id")
    expected_head = reference.get("head_digest")
    attempt_id = checkpoint.get("attempt_id")
    _require(isinstance(path, str) and bool(path.strip()), "execution event ledger path missing")
    _require(isinstance(run_id, str) and bool(run_id.strip()), "execution event ledger run_id missing")
    _require(isinstance(attempt_id, str) and bool(attempt_id.strip()), "ledger-backed checkpoint attempt_id missing")
    _require(run_id == attempt_id, "execution event ledger run_id must equal checkpoint attempt_id")
    _require(_valid_digest(expected_head), "execution event ledger head_digest invalid")

    events = _load_execution_events(root, path)
    try:
        metrics = event_ledger.derive_metrics(events, latency_slo_minutes=float(latency_slo_minutes))
    except event_ledger.EventLedgerError as exc:
        raise ExecutionIntegrityError(f"execution event ledger invalid: {exc}") from exc

    _require(metrics.get("run_id") == run_id, "execution event ledger run identity mismatch")
    _require(metrics.get("ledger_head_digest") == expected_head, "execution event ledger head digest mismatch")

    # Checkpoint fields are compatibility projections only. If present, they must
    # exactly agree with ledger-derived truth and may never override it.
    if isinstance(observation, Mapping):
        _require(
            observation.get("continue_turns") == metrics["owner_continue_count"],
            "checkpoint Continue projection contradicts execution event ledger",
        )
        _require(
            observation.get("stall_nudges") == metrics["owner_stall_nudge_count"],
            "checkpoint stall-nudge projection contradicts execution event ledger",
        )
    if isinstance(control, Mapping):
        _require(
            control.get("owner_continue_count") == metrics["owner_continue_count"],
            "convergence Continue projection contradicts execution event ledger",
        )
        _require(
            control.get("single_continue_achieved") == metrics["single_continue_achieved"],
            "single-Continue projection contradicts execution event ledger",
        )

    timing = {
        "measurement_basis": "execution_event_ledger",
        "wall_elapsed_minutes": round(float(metrics["owner_visible_wall_minutes"]), 4),
        "target_minutes": float(metrics["latency_slo_minutes"]),
        "target_met": metrics["latency_slo_status"] == "within_slo",
        "latency_slo_status": metrics["latency_slo_status"],
        "latency_slo_overrun_minutes": round(float(metrics["latency_slo_overrun_minutes"]), 4),
        "synthetic_active_minutes_substitute": False,
        "ledger_head_digest": metrics["ledger_head_digest"],
    }
    return {
        "source": "event_ledger",
        "owner_continue_count": metrics["owner_continue_count"],
        "owner_stall_nudge_count": metrics["owner_stall_nudge_count"],
        "single_continue_achieved": metrics["single_continue_achieved"],
        "owner_visible_timing": timing,
    }


def _load_correction(root: Path, checkpoint: Mapping[str, Any]) -> dict[str, Any] | None:
    path = root / CORRECTION_PATH
    if not path.is_file():
        return None
    correction = _load_json(path)
    if correction.get("target_attempt_id") == checkpoint.get("attempt_id"):
        return correction
    return None


def load_effective_checkpoint(root: Path, relative_path: str) -> dict[str, Any]:
    checkpoint = _load_json(root / relative_path)
    correction = _load_correction(root, checkpoint)
    if correction is None:
        return checkpoint
    effective = copy.deepcopy(checkpoint)
    view = correction.get("corrected_execution_view")
    _require(isinstance(view, Mapping), "execution correction missing corrected_execution_view")
    effective["owner_interaction_observation"] = copy.deepcopy(correction["owner_interaction_observation"])
    effective["execution_conformance"] = copy.deepcopy(correction["execution_conformance"])
    control = copy.deepcopy(effective.get("convergence_control", {}))
    control["owner_continue_count"] = view["owner_continue_count"]
    control["single_continue_achieved"] = view["single_continue_achieved"]
    effective["convergence_control"] = control
    effective["execution_correction_id"] = correction.get("correction_id")
    return effective


def validate_completed_attempt_integrity(
    checkpoint: Mapping[str, Any],
    *,
    context: str,
    service_objective: Mapping[str, Any],
    root: Path | None = None,
    latency_slo_minutes: float = 24.0,
) -> dict[str, Any]:
    _require(checkpoint.get("status") == "completed_verified", f"{context}: expected completed_verified")
    control = checkpoint.get("convergence_control")
    observation = checkpoint.get("owner_interaction_observation")
    conformance = checkpoint.get("execution_conformance")
    _require(isinstance(control, Mapping), f"{context}: convergence_control missing")
    _require(isinstance(observation, Mapping), f"{context}: owner_interaction_observation missing")
    _require(isinstance(conformance, Mapping), f"{context}: execution_conformance missing")

    truth = resolve_execution_truth(
        (root or Path(".")).resolve(),
        checkpoint,
        latency_slo_minutes=latency_slo_minutes,
    )
    turns = truth["owner_continue_count"]
    stall_nudges = truth["owner_stall_nudge_count"]
    achieved = truth["single_continue_achieved"]
    if turns > 1:
        _require(achieved is False, f"{context}: multi-Continue attempt cannot certify single-Continue success")
    if stall_nudges > 0:
        _require(int(control.get("no_progress_cycles", 0)) >= 1, f"{context}: stall nudge requires no-progress accounting")

    timing = truth["owner_visible_timing"]
    status = conformance.get("status")
    violations = set(conformance.get("policy_violations", [])) if isinstance(conformance.get("policy_violations"), list) else set()

    if status == "conforming":
        _require(not violations, f"{context}: conforming attempt cannot carry policy violations")
        _require(stall_nudges == 0, f"{context}: owner stall intervention makes execution nonconforming")
        # Pre-v2 history treated the old target as a conformance gate. V2 event-backed
        # runs record latency-SLO misses as telemetry; time never invalidates terminal state.
        if truth["source"] == "legacy_checkpoint":
            _require(timing["target_met"] is True, f"{context}: owner-visible timing target missed")
        convergence.validate_convergence_control(
            dict(control),
            status="completed_verified",
            context=context,
            service_objective=dict(service_objective),
        )
    elif status == "historical_nonconforming":
        _require(bool(violations), f"{context}: historical nonconformance must name policy violations")
        if int(control.get("repair_cycles", 0)) >= 2 and control.get("diagnostic_mode") is not True:
            _require("diagnostic_threshold_missed" in violations, f"{context}: missed diagnostic threshold not recorded")
        if turns > 1:
            _require("single_continue_misreported" in violations, f"{context}: prior single-Continue miscertification not recorded")
        if stall_nudges > 0:
            _require("owner_stall_intervention_required" in violations, f"{context}: owner stall intervention not recorded")
        if truth["source"] == "legacy_checkpoint" and timing["target_met"] is False:
            _require("owner_visible_timing_target_missed" in violations, f"{context}: owner-visible timing miss not recorded")
    else:
        raise ExecutionIntegrityError(f"{context}: unsupported execution_conformance status {status!r}")

    return {
        "status": "PASS",
        "attempt_id": checkpoint.get("attempt_id"),
        "execution_conformance": status,
        "truth_source": truth["source"],
        "owner_continue_turns": turns,
        "stall_nudges": stall_nudges,
        "single_continue_achieved": achieved,
        "owner_visible_timing": timing,
        "policy_violations": sorted(violations),
    }


def _validate_active_attempt(
    root: Path,
    pointer: Mapping[str, Any],
    *,
    service_objective: Mapping[str, Any],
    latency_slo_minutes: float,
) -> dict[str, Any]:
    active = pointer.get("active_attempt")
    _require(isinstance(active, Mapping), "current pointer active_attempt missing")
    checkpoint_path = active.get("checkpoint_path")
    _require(isinstance(checkpoint_path, str) and checkpoint_path, "active checkpoint path missing")
    checkpoint = load_effective_checkpoint(root, checkpoint_path)
    _require(checkpoint.get("attempt_id") == active.get("attempt_id"), "active pointer/checkpoint attempt mismatch")
    status = checkpoint.get("status")
    if status == "selected_not_started":
        return {"attempt_id": checkpoint.get("attempt_id"), "status": status, "integrity": "prestart"}
    if status in {"in_progress", "completed_verified"}:
        admission = checkpoint.get("environment_admission")
        _require(isinstance(admission, Mapping), f"{checkpoint.get('attempt_id')}: environment admission missing")
        environment.validate_admission_receipt(admission)
    if status == "completed_verified":
        receipt = checkpoint.get("merge_authorization")
        _require(isinstance(receipt, Mapping), f"{checkpoint.get('attempt_id')}: merge authorization missing")
        evidence = checkpoint.get("completion_evidence")
        _require(isinstance(evidence, Mapping), f"{checkpoint.get('attempt_id')}: completion evidence missing")
        expected_head = evidence.get("application_validated_head")
        merge_authorization.validate_merge_invocation(
            receipt,
            {
                "repository": receipt.get("repository"),
                "expected_head_sha": expected_head,
                "merge_method": receipt.get("merge_method"),
            },
        )
        completed_integrity = validate_completed_attempt_integrity(
            checkpoint,
            context=str(checkpoint.get("attempt_id") or checkpoint_path),
            service_objective=service_objective,
            root=root,
            latency_slo_minutes=latency_slo_minutes,
        )
        return {
            "attempt_id": checkpoint.get("attempt_id"),
            "status": status,
            "integrity": "enforced",
            "completed_integrity": completed_integrity,
        }
    return {"attempt_id": checkpoint.get("attempt_id"), "status": status, "integrity": "enforced"}


def check(root: Path) -> dict[str, Any]:
    root = root.resolve()
    pointer = _load_json(root / POINTER_PATH)
    profile = _load_json(root / PROFILE_PATH)
    service = profile.get("service_objective")
    timing_policy = profile.get("timing")
    _require(isinstance(service, Mapping), "execution profile service objective missing")
    _require(isinstance(timing_policy, Mapping), "execution profile timing policy missing")
    latency_slo = timing_policy.get("latency_slo_minutes")
    _require(
        isinstance(latency_slo, (int, float)) and not isinstance(latency_slo, bool) and latency_slo > 0,
        "execution profile latency_slo_minutes invalid",
    )

    recent_results: list[dict[str, Any]] = []
    rows = pointer.get("recently_completed_implementation_work", [])
    _require(isinstance(rows, list), "recently_completed_implementation_work must be an array")
    for row in rows:
        _require(isinstance(row, Mapping), "recent completion row must be an object")
        rel = row.get("checkpoint_path")
        _require(isinstance(rel, str) and rel, "recent completion checkpoint_path missing")
        effective = load_effective_checkpoint(root, rel)
        recent_results.append(
            validate_completed_attempt_integrity(
                effective,
                context=str(effective.get("attempt_id") or rel),
                service_objective=service,
                root=root,
                latency_slo_minutes=float(latency_slo),
            )
        )

    active = _validate_active_attempt(
        root,
        pointer,
        service_objective=service,
        latency_slo_minutes=float(latency_slo),
    )
    return {
        "schema_version": "1.1.0",
        "status": "PASS",
        "gate": "execution_integrity",
        "active_attempt": active,
        "recent_completed": recent_results,
        "event_ledger_authority": "enforced_when_checkpoint_declares_execution_event_ledger",
        "legacy_correction_registry": str(CORRECTION_PATH),
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="Audit current and recently completed Multiversal execution integrity")
    parser.add_argument("--root", default=".")
    args = parser.parse_args()
    try:
        result = check(Path(args.root))
    except (
        OSError,
        json.JSONDecodeError,
        ExecutionIntegrityError,
        event_ledger.EventLedgerError,
        environment.EnvironmentAdmissionError,
        merge_authorization.MergeAuthorizationError,
        convergence.ConvergenceError,
    ) as exc:
        result = {"schema_version": "1.1.0", "status": "FAIL", "gate": "execution_integrity", "error": str(exc)}
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0 if result["status"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
