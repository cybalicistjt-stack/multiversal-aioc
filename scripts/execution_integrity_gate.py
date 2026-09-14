#!/usr/bin/env python3
from __future__ import annotations

import argparse
import copy
import json
from datetime import datetime
from pathlib import Path
from typing import Any, Mapping

import execution_environment_admission as environment
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


def measure_owner_visible_timing(checkpoint: Mapping[str, Any]) -> dict[str, Any]:
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
) -> dict[str, Any]:
    _require(checkpoint.get("status") == "completed_verified", f"{context}: expected completed_verified")
    control = checkpoint.get("convergence_control")
    observation = checkpoint.get("owner_interaction_observation")
    conformance = checkpoint.get("execution_conformance")
    _require(isinstance(control, Mapping), f"{context}: convergence_control missing")
    _require(isinstance(observation, Mapping), f"{context}: owner_interaction_observation missing")
    _require(isinstance(conformance, Mapping), f"{context}: execution_conformance missing")

    turns = observation.get("continue_turns")
    stall_nudges = observation.get("stall_nudges")
    _require(isinstance(turns, int) and not isinstance(turns, bool) and turns >= 1, f"{context}: continue_turns invalid")
    _require(isinstance(stall_nudges, int) and not isinstance(stall_nudges, bool) and stall_nudges >= 0, f"{context}: stall_nudges invalid")
    _require(control.get("owner_continue_count") == turns, f"{context}: owner Continue count contradicts owner observation")
    achieved = control.get("single_continue_achieved")
    _require(isinstance(achieved, bool), f"{context}: single_continue_achieved missing")
    if turns > 1:
        _require(achieved is False, f"{context}: multi-Continue attempt cannot certify single-Continue success")
    if stall_nudges > 0:
        _require(int(control.get("no_progress_cycles", 0)) >= 1, f"{context}: stall nudge requires no-progress accounting")

    timing = measure_owner_visible_timing(checkpoint)
    status = conformance.get("status")
    violations = set(conformance.get("policy_violations", [])) if isinstance(conformance.get("policy_violations"), list) else set()

    if status == "conforming":
        _require(not violations, f"{context}: conforming attempt cannot carry policy violations")
        _require(stall_nudges == 0, f"{context}: owner stall intervention makes execution nonconforming")
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
        if timing["target_met"] is False:
            _require("owner_visible_timing_target_missed" in violations, f"{context}: owner-visible timing miss not recorded")
    else:
        raise ExecutionIntegrityError(f"{context}: unsupported execution_conformance status {status!r}")

    return {
        "status": "PASS",
        "attempt_id": checkpoint.get("attempt_id"),
        "execution_conformance": status,
        "owner_continue_turns": turns,
        "stall_nudges": stall_nudges,
        "owner_visible_timing": timing,
        "policy_violations": sorted(violations),
    }


def _validate_active_attempt(root: Path, pointer: Mapping[str, Any]) -> dict[str, Any]:
    active = pointer.get("active_attempt")
    _require(isinstance(active, Mapping), "current pointer active_attempt missing")
    checkpoint_path = active.get("checkpoint_path")
    _require(isinstance(checkpoint_path, str) and checkpoint_path, "active checkpoint path missing")
    checkpoint = _load_json(root / checkpoint_path)
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
    return {"attempt_id": checkpoint.get("attempt_id"), "status": status, "integrity": "enforced"}


def check(root: Path) -> dict[str, Any]:
    root = root.resolve()
    pointer = _load_json(root / POINTER_PATH)
    profile = _load_json(root / PROFILE_PATH)
    service = profile.get("service_objective")
    _require(isinstance(service, Mapping), "execution profile service objective missing")

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
            )
        )

    active = _validate_active_attempt(root, pointer)
    return {
        "schema_version": "1.0.0",
        "status": "PASS",
        "gate": "execution_integrity",
        "active_attempt": active,
        "recent_completed": recent_results,
        "correction_registry": str(CORRECTION_PATH),
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="Audit current and recently completed Multiversal execution integrity")
    parser.add_argument("--root", default=".")
    args = parser.parse_args()
    try:
        result = check(Path(args.root))
    except (OSError, json.JSONDecodeError, ExecutionIntegrityError, environment.EnvironmentAdmissionError, merge_authorization.MergeAuthorizationError, convergence.ConvergenceError) as exc:
        result = {"schema_version": "1.0.0", "status": "FAIL", "gate": "execution_integrity", "error": str(exc)}
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0 if result["status"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
