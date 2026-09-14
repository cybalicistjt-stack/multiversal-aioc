#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
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


def _execution_state(phase: str, next_action: str) -> dict[str, Any]:
    return {
        "phase": phase,
        "next_action": next_action,
        "response_gate": "TERMINATION_PREFLIGHT_REQUIRED" if phase == "closed" else "CONTINUE_EXECUTION",
    }


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
        return _execution_state("closed", "strict_successor_selected")
    if start_pr_state != "merged":
        return _execution_state("governed_start", "validate_and_merge_governed_start")
    if not branch_exists:
        return _execution_state("implementation_branch", "create_or_resume_authorized_branch")
    if merge_sha:
        if closeout_state == "completed_verified":
            return _execution_state("closed", "strict_successor_selected")
        return _execution_state("closeout", "complete_governance_closeout")
    if application_pr_state == "merged":
        return _execution_state("closeout", "complete_governance_closeout")
    if focused_test_exists and validation_state in {"not_dispatched", "absent"}:
        return _execution_state("implementation_red", "dispatch_focused_red_validation")
    if validation_state in {"queued", "in_progress", "dispatched"}:
        return _execution_state("implementation_red", "wait_for_focused_red_result")
    if validation_state in {"red_observed", "expected_failure"}:
        return _execution_state("implementation_green", "implement_from_observed_red")
    if validation_state in {"green", "success"}:
        return _execution_state("integration", "merge_exact_validated_head")
    if not focused_test_exists:
        return _execution_state("implementation_test", "create_focused_behavior_test")
    return _execution_state("implementation", "reconcile_observed_execution_state")


def _required_text(spec: Mapping[str, Any], key: str) -> str:
    value = str(spec.get(key) or "").strip()
    if not value:
        raise ValueError(f"execution capsule missing required field: {key}")
    return value


def _string_list(spec: Mapping[str, Any], key: str) -> list[str]:
    value = spec.get(key)
    if not isinstance(value, list) or not value or not all(isinstance(row, str) and row.strip() for row in value):
        raise ValueError(f"execution capsule field {key} must be a non-empty string list")
    return [row.strip() for row in value]


def compile_execution_capsule(spec: Mapping[str, Any]) -> dict[str, Any]:
    """Compile all ordinary tranche execution facts into one deterministic packet.

    The capsule is the bridge from selection to governed start. Once compiled, ordinary
    execution consumes declared inputs and may not reopen repository-wide discovery unless
    diagnostic mode carries a concrete materially-new failure signature.
    """
    from execution_transaction_preflight import select_merge_method

    work_item_id = _required_text(spec, "work_item_id")
    attempt_id = _required_text(spec, "attempt_id")
    repository = _required_text(spec, "application_repository")
    base_sha = _required_text(spec, "application_base_sha")
    branch = _required_text(spec, "implementation_branch")
    profile_id = _required_text(spec, "validation_profile_id")
    focused_test = _required_text(spec, "focused_test_path")
    if len(base_sha) != 40:
        raise ValueError("application_base_sha must be a 40-character commit SHA")

    successor = spec.get("strict_successor")
    if not isinstance(successor, Mapping):
        raise ValueError("strict_successor must be a mapping")
    successor_row = {
        "work_item_id": _required_text(successor, "work_item_id"),
        "attempt_id": _required_text(successor, "attempt_id"),
        "selection_state": str(successor.get("selection_state") or ""),
        "implementation_authority": successor.get("implementation_authority"),
        "implementation_branch": successor.get("implementation_branch"),
    }
    if successor_row["selection_state"] != "selected_not_started":
        raise ValueError("strict successor must be selected_not_started")
    if successor_row["implementation_authority"] is not False or successor_row["implementation_branch"] is not None:
        raise ValueError("strict successor must not have implementation authority or a branch")

    merge = select_merge_method(spec.get("repository_capabilities", {}))
    if merge.get("decision") != "USE_MERGE_METHOD":
        raise ValueError("repository exposes no usable merge plan")

    capsule: dict[str, Any] = {
        "schema_version": "1.0.0",
        "capsule_id": f"{attempt_id}:capsule:v1",
        "work_item_id": work_item_id,
        "attempt_id": attempt_id,
        "application": {
            "repository": repository,
            "base_sha": base_sha,
            "implementation_branch": branch,
            "mutation_allowlist": _string_list(spec, "application_mutation_allowlist"),
        },
        "context": {
            "allowed_paths": _string_list(spec, "allowed_context_paths"),
            "repository_search_authorized": False,
        },
        "validation": {
            "profile_id": profile_id,
            "focused_test_path": focused_test,
        },
        "merge_plan": {
            "method": merge["merge_method"],
            "supported_methods": list(merge["supported_methods"]),
            "bind_to_exact_validated_head": True,
        },
        "closeout": {
            "projection_paths": _string_list(spec, "closeout_projection_paths"),
            "evidence_fields": [
                "application_pr",
                "validated_head",
                "validation_run",
                "deterministic_receipt_sha256",
                "merge_sha",
            ],
            "derive_from_one_canonical_transition_record": True,
        },
        "strict_successor": successor_row,
        "post_start_discovery_policy": "DENY_UNLESS_DIAGNOSTIC_FAILURE_SIGNATURE",
        "terminal_boundary": "completed_verified_with_strict_successor_selected_or_genuine_blocker",
    }
    canonical = json.dumps(capsule, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode("utf-8")
    capsule["capsule_digest"] = hashlib.sha256(canonical).hexdigest()
    return capsule


def materialize_transition_bundle(record: Mapping[str, Any]) -> dict[str, Any]:
    """Derive terminal and successor projections from one canonical closeout record."""
    if str(record.get("status") or "") != "completed_verified":
        raise ValueError("transition record must be completed_verified")
    successor = str(record.get("strict_successor") or "").strip()
    successor_attempt = str(record.get("successor_attempt_id") or "").strip()
    if not successor or not successor_attempt:
        raise ValueError("transition record requires strict successor identity")

    completed = {
        "work_item_id": record.get("work_item_id"),
        "attempt_id": record.get("attempt_id"),
        "status": "completed_verified",
        "implementation_authority": False,
        "implementation_branch": None,
        "strict_successor": successor,
    }
    successor_row = {
        "work_item_id": successor,
        "attempt_id": successor_attempt,
        "title": record.get("successor_title"),
        "status": "selected_not_started",
        "implementation_authority": False,
        "implementation_branch": None,
    }
    evidence = {
        "application_pr": record.get("application_pr"),
        "validated_head": record.get("validated_head"),
        "validation_run": record.get("validation_run"),
        "deterministic_receipt_sha256": record.get("deterministic_receipt_sha256"),
        "merge_sha": record.get("merge_sha"),
    }
    if any(value in (None, "") for value in evidence.values()):
        raise ValueError("transition record has incomplete completion evidence")
    return {
        "schema_version": "1.0.0",
        "completed": completed,
        "successor": successor_row,
        "evidence": evidence,
    }
