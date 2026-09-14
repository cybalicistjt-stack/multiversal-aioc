#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any, Mapping, Sequence


class TransactionPreflightError(RuntimeError):
    pass


def _branch_mentions_work_item(branch: str, work_item_id: str) -> bool:
    token = work_item_id.lower().replace("_", "-")
    return token in branch.lower().replace("_", "-")


def decide_start(snapshot: Mapping[str, Any]) -> dict[str, Any]:
    work_item_id = str(snapshot.get("work_item_id") or "")
    authorized_branch = str(snapshot.get("authorized_branch") or "")
    proposed_branch = str(snapshot.get("proposed_branch") or authorized_branch)
    observed_branches = [str(x) for x in snapshot.get("observed_branches", [])]
    open_prs = [x for x in snapshot.get("open_pull_requests", []) if isinstance(x, Mapping) and x.get("state") == "open"]
    if not work_item_id or not authorized_branch:
        raise TransactionPreflightError("work_item_id and authorized_branch are required")

    conflicting_prs = [
        int(pr["number"])
        for pr in open_prs
        if str(pr.get("work_item_id") or "") == work_item_id
        and str(pr.get("head") or "") != authorized_branch
        and isinstance(pr.get("number"), int)
    ]
    alternate_branches = sorted({
        branch for branch in observed_branches
        if branch != authorized_branch and _branch_mentions_work_item(branch, work_item_id)
    })
    if proposed_branch != authorized_branch or conflicting_prs or alternate_branches:
        return {
            "decision": "STOP_DUPLICATE_ATTEMPT",
            "authorized_branch": authorized_branch,
            "conflicting_pull_requests": conflicting_prs,
            "conflicting_branches": alternate_branches,
        }

    exact_prs = [pr for pr in open_prs if str(pr.get("head") or "") == authorized_branch]
    if len(exact_prs) > 1:
        return {
            "decision": "STOP_DUPLICATE_ATTEMPT",
            "authorized_branch": authorized_branch,
            "conflicting_pull_requests": [int(pr["number"]) for pr in exact_prs if isinstance(pr.get("number"), int)],
            "conflicting_branches": [],
        }
    if exact_prs:
        return {
            "decision": "RESUME_OPEN_PR",
            "authorized_branch": authorized_branch,
            "pull_request": exact_prs[0].get("number"),
        }
    if authorized_branch in observed_branches:
        return {"decision": "RESUME_BRANCH", "authorized_branch": authorized_branch}
    return {"decision": "CREATE_AUTHORIZED_BRANCH", "authorized_branch": authorized_branch}


def decide_execution_route(snapshot: Mapping[str, Any]) -> dict[str, Any]:
    capsule_ready = snapshot.get("capsule_ready") is True
    focused_test_exists = snapshot.get("focused_test_exists") is True
    context_resolved = snapshot.get("required_context_resolved") is True
    red_dispatched = snapshot.get("red_validation_dispatched") is True
    red_observed = snapshot.get("red_result_observed") is True
    diagnostic_mode = snapshot.get("diagnostic_mode") is True
    failure_signature = str(snapshot.get("failure_signature") or "").strip()

    if diagnostic_mode:
        if not failure_signature:
            return {
                "decision": "CONTINUE_CONTEXT_RESOLUTION",
                "repository_search_authorized": False,
                "reason": "diagnostic mode requires a concrete failure signature",
            }
        return {
            "decision": "DIAGNOSTIC_EXPANSION_ALLOWED",
            "repository_search_authorized": True,
            "failure_signature": failure_signature,
        }
    if not capsule_ready:
        return {
            "decision": "COMPILE_EXECUTION_CAPSULE",
            "repository_search_authorized": False,
            "reason": "ordinary execution requires a compiled capsule before RED dispatch",
        }
    if focused_test_exists and context_resolved and not red_dispatched:
        return {"decision": "DISPATCH_RED_NOW", "repository_search_authorized": False}
    if red_dispatched and not red_observed:
        return {"decision": "WAIT_FOR_RED_RESULT", "repository_search_authorized": False}
    if red_observed:
        return {"decision": "IMPLEMENT_FROM_RED", "repository_search_authorized": False}
    return {"decision": "CONTINUE_CONTEXT_RESOLUTION", "repository_search_authorized": False}


def select_merge_method(capabilities: Mapping[str, Any], requested_method: str | None = None) -> dict[str, Any]:
    """Choose a repository-supported PR merge method before issuing a merge side effect.

    Repository metadata is intentionally passed in rather than fetched here so this
    deterministic control can be tested and so the caller must supply a fresh capability
    snapshot from the repository being mutated.
    """
    capability_keys = (
        ("squash", "allow_squash_merge"),
        ("merge", "allow_merge_commit"),
        ("rebase", "allow_rebase_merge"),
    )
    supported = [method for method, key in capability_keys if capabilities.get(key) is True]
    if not supported:
        raise TransactionPreflightError("repository exposes no supported merge method")
    if requested_method is not None:
        normalized = str(requested_method).strip().lower()
        if normalized not in {"merge", "squash", "rebase"}:
            raise TransactionPreflightError("requested_method must be merge, squash, or rebase")
        if normalized not in supported:
            return {
                "schema_version": "1.0.0",
                "decision": "STOP_UNSUPPORTED_MERGE_METHOD",
                "requested_method": normalized,
                "supported_methods": supported,
            }
        selected = normalized
    else:
        selected = supported[0]
    return {
        "schema_version": "1.0.0",
        "decision": "USE_MERGE_METHOD",
        "merge_method": selected,
        "supported_methods": supported,
    }


def assess_precloseout_readiness(snapshot: Mapping[str, Any]) -> dict[str, Any]:
    """Decide closeout from terminal invariants; elapsed time is SLO telemetry only."""
    elapsed = snapshot.get("elapsed_active_minutes")
    target = snapshot.get("target_cycle_minutes")
    if not isinstance(elapsed, (int, float)) or isinstance(elapsed, bool) or elapsed < 0:
        raise TransactionPreflightError("elapsed_active_minutes must be a non-negative number")
    if not isinstance(target, (int, float)) or isinstance(target, bool) or target <= 0:
        raise TransactionPreflightError("target_cycle_minutes must be a positive number")

    elapsed_f = float(elapsed)
    target_f = float(target)
    overrun = max(elapsed_f - target_f, 0.0)
    telemetry = {
        "latency_slo_minutes": target_f,
        "latency_slo_status": "within_slo" if elapsed_f <= target_f else "missed",
        "latency_slo_overrun_minutes": overrun,
    }

    if "terminal_invariants_satisfied" in snapshot:
        terminal = snapshot.get("terminal_invariants_satisfied")
        if not isinstance(terminal, bool):
            raise TransactionPreflightError("terminal_invariants_satisfied must be boolean")
        if terminal:
            return {
                "schema_version": "1.1.0",
                "decision": "READY_FOR_CLOSEOUT",
                "reason_code": "MVEXEC-TERMINAL-INVARIANTS-SATISFIED",
                **telemetry,
            }
        return {
            "schema_version": "1.1.0",
            "decision": "CONTINUE_SAME_CYCLE",
            "reason_code": "MVEXEC-TERMINAL-INVARIANTS-PENDING",
            **telemetry,
        }

    safe_work = snapshot.get("safe_same_lane_work_available")
    dynamic_fill = snapshot.get("dynamic_fill_attempted")
    fill_exit_reason = snapshot.get("fill_exit_reason")
    if not isinstance(safe_work, bool):
        raise TransactionPreflightError("safe_same_lane_work_available must be boolean")
    if not isinstance(dynamic_fill, bool):
        raise TransactionPreflightError("dynamic_fill_attempted must be boolean")
    if fill_exit_reason not in {None, "safe_work_exhausted", "closeout_switch_reached"}:
        raise TransactionPreflightError("fill_exit_reason is invalid")

    remaining = max(target_f - elapsed_f, 0.0)
    if safe_work is False and dynamic_fill is True and fill_exit_reason in {"safe_work_exhausted", "closeout_switch_reached"}:
        reason = (
            "MVEXEC-ENVELOPE-SAFE-WORK-EXHAUSTED"
            if fill_exit_reason == "safe_work_exhausted"
            else "MVEXEC-LEGACY-STATE-READY"
        )
        return {
            "schema_version": "1.1.0",
            "decision": "READY_FOR_CLOSEOUT",
            "reason_code": reason,
            "remaining_active_minutes": remaining,
            **telemetry,
        }
    return {
        "schema_version": "1.1.0",
        "decision": "CONTINUE_SAME_CYCLE",
        "reason_code": "MVEXEC-LEGACY-TERMINAL-INVARIANTS-PENDING",
        "remaining_active_minutes": remaining,
        **telemetry,
    }


def _selection(source: Mapping[str, Any], key: str | None = None) -> Mapping[str, Any]:
    if key is None:
        return source
    value = source.get(key)
    if not isinstance(value, Mapping):
        raise TransactionPreflightError(f"missing selection object: {key}")
    return value


def _work_item(row: Mapping[str, Any]) -> Any:
    return row.get("work_item_id", row.get("work_item"))


def _state(row: Mapping[str, Any]) -> Any:
    return row.get("status", row.get("state"))


def validate_start_projection(
    checkpoint: Mapping[str, Any],
    pointer: Mapping[str, Any],
    authority: Mapping[str, Any],
    runtime: Mapping[str, Any],
    compiled: Mapping[str, Any],
    *,
    capsule: Mapping[str, Any] | None = None,
) -> dict[str, Any]:
    rows = [
        ("checkpoint", checkpoint),
        ("pointer", _selection(pointer, "active_attempt")),
        ("authority", _selection(authority, "active_planning_work")),
        ("runtime", _selection(runtime, "active_work")),
        ("compiled", _selection(compiled, "current_selection")),
    ]
    expected = {
        "work_item_id": _work_item(checkpoint),
        "attempt_id": checkpoint.get("attempt_id"),
        "status": _state(checkpoint),
        "implementation_authority": checkpoint.get("implementation_authority"),
        "implementation_branch": checkpoint.get("implementation_branch"),
    }
    if expected["status"] != "in_progress" or expected["implementation_authority"] is not True or not expected["implementation_branch"]:
        raise TransactionPreflightError("checkpoint is not an authorized governed-start state")

    errors: list[str] = []
    for label, row in rows:
        if _work_item(row) != expected["work_item_id"]:
            errors.append(f"{label}:work-item")
        if row.get("attempt_id") not in (None, expected["attempt_id"]):
            errors.append(f"{label}:attempt")
        if _state(row) != expected["status"]:
            errors.append(f"{label}:status")
        if row.get("implementation_authority") is not expected["implementation_authority"]:
            errors.append(f"{label}:implementation-authority")
        if "implementation_branch" in row and row.get("implementation_branch") != expected["implementation_branch"]:
            errors.append(f"{label}:implementation-branch")
    if errors:
        raise TransactionPreflightError("start projection mismatch: " + ",".join(errors))

    if not isinstance(capsule, Mapping):
        raise TransactionPreflightError("governed start requires a compiled execution capsule")
    capsule_application = capsule.get("application")
    if not isinstance(capsule_application, Mapping):
        raise TransactionPreflightError("execution capsule is missing application binding")
    capsule_digest = str(capsule.get("capsule_digest") or "")
    if len(capsule_digest) != 64:
        raise TransactionPreflightError("execution capsule digest must be 64 hex characters")
    capsule_errors: list[str] = []
    if capsule.get("work_item_id") != expected["work_item_id"]:
        capsule_errors.append("work-item")
    if capsule.get("attempt_id") != expected["attempt_id"]:
        capsule_errors.append("attempt")
    if capsule_application.get("implementation_branch") != expected["implementation_branch"]:
        capsule_errors.append("implementation-branch")
    if capsule_errors:
        raise TransactionPreflightError("execution capsule mismatch: " + ",".join(capsule_errors))
    return {
        "status": "PASS",
        "authorized_branch": expected["implementation_branch"],
        "work_item_id": expected["work_item_id"],
        "capsule_digest": capsule_digest,
    }


def assess_validation_head(current_head: str, validation_head: str | None, validation_status: str | None) -> dict[str, Any]:
    if validation_head and validation_head != current_head:
        return {"state": "SUPERSEDED", "counts_for_closeout": False, "current_head": current_head, "validation_head": validation_head}
    normalized = str(validation_status or "").lower()
    green = validation_head == current_head and normalized in {"success", "passed", "pass", "completed_success"}
    return {
        "state": "CURRENT_GREEN" if green else "CURRENT_NOT_GREEN",
        "counts_for_closeout": green,
        "current_head": current_head,
        "validation_head": validation_head,
    }


def prepare_closeout(snapshot: Mapping[str, Any]) -> dict[str, Any]:
    v2_envelope_keys = {
        "terminal_invariants_satisfied",
        "elapsed_active_minutes",
        "target_cycle_minutes",
    }
    legacy_envelope_keys = {
        "elapsed_active_minutes",
        "target_cycle_minutes",
        "safe_same_lane_work_available",
        "dynamic_fill_attempted",
        "fill_exit_reason",
    }
    if "terminal_invariants_satisfied" in snapshot:
        if not v2_envelope_keys.issubset(snapshot.keys()):
            missing = sorted(v2_envelope_keys.difference(snapshot.keys()))
            raise TransactionPreflightError("closeout terminal snapshot incomplete: " + ",".join(missing))
        readiness = assess_precloseout_readiness(snapshot)
        if readiness["decision"] != "READY_FOR_CLOSEOUT":
            return {
                **readiness,
                "successor": snapshot.get("strict_successor"),
                "evidence_placeholders": [],
            }
    elif legacy_envelope_keys.intersection(snapshot.keys()):
        if not legacy_envelope_keys.issubset(snapshot.keys()):
            missing = sorted(legacy_envelope_keys.difference(snapshot.keys()))
            raise TransactionPreflightError("closeout envelope snapshot incomplete: " + ",".join(missing))
        readiness = assess_precloseout_readiness(snapshot)
        if readiness["decision"] != "READY_FOR_CLOSEOUT":
            return {
                **readiness,
                "successor": snapshot.get("strict_successor"),
                "evidence_placeholders": [],
            }

    required = ("validated_head", "validation_run", "deterministic_receipt_sha256", "merge_sha")
    placeholders = [key for key in required if not snapshot.get(key)]
    current_head = str(snapshot.get("current_head") or "")
    validated_head = snapshot.get("validated_head")
    if validated_head and validated_head != current_head:
        return {
            "decision": "WAIT_CURRENT_HEAD_VALIDATION",
            "successor": snapshot.get("strict_successor"),
            "evidence_placeholders": placeholders,
            "superseded_validated_head": validated_head,
        }
    if placeholders:
        return {
            "decision": "PREPARE_CLOSEOUT",
            "successor": snapshot.get("strict_successor"),
            "evidence_placeholders": placeholders,
            "precomputable": ["terminal_checkpoint_shape", "successor_checkpoint_shape", "pointer_projection", "authority_projection", "runtime_projection", "compiled_projection", "backlog_projection"],
        }
    receipt = str(snapshot.get("deterministic_receipt_sha256") or "")
    merge_sha = str(snapshot.get("merge_sha") or "")
    if len(current_head) != 40 or len(str(validated_head)) != 40 or len(merge_sha) != 40 or len(receipt) != 64:
        raise TransactionPreflightError("closeout evidence has invalid digest/SHA shape")
    return {"decision": "READY_TO_CLOSE", "successor": snapshot.get("strict_successor"), "evidence_placeholders": []}


def _structured_terminal_reason(value: Any, *, require_reason: bool = False) -> bool:
    if not isinstance(value, Mapping) or not value.get("type"):
        return False
    return not require_reason or bool(value.get("reason"))


def validate_execution_outcome(outcome: Mapping[str, Any]) -> dict[str, Any]:
    turns = outcome.get("owner_continue_turns")
    achieved = outcome.get("single_continue_achieved")
    incident = outcome.get("execution_incident")
    blocker = outcome.get("genuine_blocker")
    if not isinstance(turns, int) or isinstance(turns, bool) or turns < 1:
        raise TransactionPreflightError("owner_continue_turns must be a positive integer")
    if not isinstance(achieved, bool):
        raise TransactionPreflightError("single_continue_achieved must be boolean")

    has_incident = _structured_terminal_reason(incident, require_reason=True)
    has_blocker = _structured_terminal_reason(blocker, require_reason=True)
    if achieved:
        if turns != 1 or incident is not None or blocker is not None:
            raise TransactionPreflightError("single-Continue success requires exactly one Continue with no incident or blocker")
        outcome_class = "single_continue"
    else:
        if has_incident == has_blocker:
            raise TransactionPreflightError("unsuccessful single-Continue outcome requires exactly one structured execution_incident or genuine_blocker")
        outcome_class = "execution_incident" if has_incident else "genuine_blocker_exception"
    return {
        "status": "PASS",
        "owner_continue_turns": turns,
        "single_continue_achieved": achieved,
        "outcome_class": outcome_class,
    }


def _load(path: str) -> dict[str, Any]:
    return json.loads(Path(path).read_text(encoding="utf-8"))


def main() -> int:
    parser = argparse.ArgumentParser(description="Deterministic bounded-execution transaction preflight")
    parser.add_argument("mode", choices=["start", "outcome", "validation", "closeout", "route", "merge-method", "precloseout"])
    parser.add_argument("snapshot", help="JSON snapshot path")
    args = parser.parse_args()
    data = _load(args.snapshot)
    if args.mode == "start":
        result = decide_start(data)
    elif args.mode == "outcome":
        result = validate_execution_outcome(data)
    elif args.mode == "validation":
        result = assess_validation_head(str(data.get("current_head") or ""), data.get("validation_head"), data.get("validation_status"))
    elif args.mode == "route":
        result = decide_execution_route(data)
    elif args.mode == "merge-method":
        result = select_merge_method(data, data.get("requested_method"))
    elif args.mode == "precloseout":
        result = assess_precloseout_readiness(data)
    else:
        result = prepare_closeout(data)
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
