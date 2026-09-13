#!/usr/bin/env python3
from __future__ import annotations

from typing import Any, Mapping


def materialize_selector_rows(record: Mapping[str, Any]) -> dict[str, dict[str, Any]]:
    row = {
        "work_item_id": record.get("work_item_id"),
        "attempt_id": record.get("attempt_id"),
        "status": record.get("status"),
        "implementation_authority": record.get("implementation_authority"),
        "implementation_branch": record.get("implementation_branch"),
    }
    return {label: dict(row) for label in ("checkpoint", "pointer", "authority", "runtime", "compiled")}


def reconcile_execution_state(record: Mapping[str, Any], observed: Mapping[str, Any]) -> dict[str, Any]:
    status = str(record.get("status") or "")
    start_pr_state = str(observed.get("start_pr_state") or "absent")
    branch_exists = bool(observed.get("implementation_branch_exists"))
    focused_test_exists = bool(observed.get("focused_test_exists"))
    application_pr_state = str(observed.get("application_pr_state") or "absent")
    validation_state = str(observed.get("validation_state") or "not_dispatched")
    merge_sha = observed.get("application_merge_sha")
    closeout_state = str(observed.get("closeout_state") or "not_started")

    if status == "completed_verified":
        return {"phase": "closed", "next_action": "strict_successor_selected"}
    if start_pr_state != "merged":
        return {"phase": "governed_start", "next_action": "validate_and_merge_governed_start"}
    if not branch_exists:
        return {"phase": "implementation_branch", "next_action": "create_or_resume_authorized_branch"}
    if merge_sha:
        if closeout_state == "completed_verified":
            return {"phase": "closed", "next_action": "strict_successor_selected"}
        return {"phase": "closeout", "next_action": "complete_governance_closeout"}
    if application_pr_state == "merged":
        return {"phase": "closeout", "next_action": "complete_governance_closeout"}
    if focused_test_exists and validation_state in {"not_dispatched", "absent"}:
        return {"phase": "implementation_red", "next_action": "dispatch_focused_red_validation"}
    if validation_state in {"queued", "in_progress", "dispatched"}:
        return {"phase": "implementation_red", "next_action": "wait_for_focused_red_result"}
    if validation_state in {"red_observed", "expected_failure"}:
        return {"phase": "implementation_green", "next_action": "implement_from_observed_red"}
    if validation_state in {"green", "success"}:
        return {"phase": "integration", "next_action": "merge_exact_validated_head"}
    if not focused_test_exists:
        return {"phase": "implementation_test", "next_action": "create_focused_behavior_test"}
    return {"phase": "implementation", "next_action": "reconcile_observed_execution_state"}
