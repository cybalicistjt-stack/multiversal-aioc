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
    if focused_test_exists and context_resolved and not red_dispatched:
        return {"decision": "DISPATCH_RED_NOW", "repository_search_authorized": False}
    if red_dispatched and not red_observed:
        return {"decision": "WAIT_FOR_RED_RESULT", "repository_search_authorized": False}
    if red_observed:
        return {"decision": "IMPLEMENT_FROM_RED", "repository_search_authorized": False}
    return {"decision": "CONTINUE_CONTEXT_RESOLUTION", "repository_search_authorized": False}


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
    return {"status": "PASS", "authorized_branch": expected["implementation_branch"], "work_item_id": expected["work_item_id"]}


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
    if turns == 1:
        if not achieved or incident is not None or blocker is not None:
            raise TransactionPreflightError("single-Continue outcome must be achieved=true with no incident or blocker")
        outcome_class = "single_continue"
    else:
        if achieved:
            raise TransactionPreflightError("second-or-later Continue cannot be reported as single-Continue success")
        has_incident = _structured_terminal_reason(incident)
        has_blocker = _structured_terminal_reason(blocker, require_reason=True)
        if has_incident == has_blocker:
            raise TransactionPreflightError("second-or-later Continue requires exactly one structured execution_incident or genuine_blocker")
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
    parser.add_argument("mode", choices=["start", "outcome", "validation", "closeout", "route"])
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
    else:
        result = prepare_closeout(data)
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
