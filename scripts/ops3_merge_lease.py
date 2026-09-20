#!/usr/bin/env python3
"""Operations V3 ready-candidate publication queue.

This module serializes only integration-ready immutable candidates. It does not
reserve future work, create active holders, freeze main during implementation,
or require a post-merge release step.
"""
from __future__ import annotations

from typing import Any

DIRECT_MAIN_MUTATION = "OPS3.DIRECT_MAIN_MUTATION"
HEAD_MISMATCH = "OPS3.HEAD_MISMATCH"
INTEGRATION_NOT_BOUND = "OPS3.INTEGRATION_NOT_BOUND"
QUEUE_ORDER = "OPS3.QUEUE_ORDER"
STALE_INTEGRATION = "OPS3.STALE_INTEGRATION"
CANDIDATE_NOT_READY = "OPS3.CANDIDATE_NOT_READY"

PROTECTED_REPOSITORIES = frozenset({
    "cybalicistjt-stack/Multiversal-app",
    "cybalicistjt-stack/multiversal-aioc",
})

NO_PUBLICATION = "none"
SINGLE_LANE_DIRECT = "single_lane_direct"
READY_QUEUE = "ready_queue"

class PublicationConflict(RuntimeError):
    pass

def publication_mode(nonterminal_persistent_lanes: list[str] | tuple[str, ...] | set[str]) -> str:
    """Choose publication coordination once from canonical lane state."""
    lanes = {str(lane).strip() for lane in nonterminal_persistent_lanes if str(lane).strip()}
    if not lanes:
        return NO_PUBLICATION
    if len(lanes) == 1:
        return SINGLE_LANE_DIRECT
    return READY_QUEUE

def coordination_branch(target_repo: str) -> str:
    slug = target_repo.lower().replace("/", "-").replace("_", "-")
    return f"ops3-publication-queue/{slug}"

def free_publication_queue(target_repo: str, *, generation: int = 0, last_merge_sha: str | None = None) -> dict[str, Any]:
    return {
        "schema_version": "3.0.0",
        "target_repo": target_repo,
        "generation": generation,
        "ready": [],
        "history": [],
        "last_merge_sha": last_merge_sha,
    }

def _generation(state: dict[str, Any], expected_generation: int) -> None:
    if state.get("generation") != expected_generation:
        raise PublicationConflict("publication queue generation changed")

def _ready(state: dict[str, Any]) -> list[dict[str, Any]]:
    value = state.get("ready", [])
    if not isinstance(value, list):
        raise PublicationConflict("ready queue must be a list")
    return [dict(x) for x in value]

def _candidate(candidate: dict[str, Any]) -> dict[str, Any]:
    required = ("candidate_id", "lane", "work_item_id", "pr_number", "head_sha", "prequeue_validation")
    if any(not candidate.get(k) for k in required):
        raise PublicationConflict(CANDIDATE_NOT_READY)
    validation = candidate.get("prequeue_validation")
    if not isinstance(validation, dict):
        raise PublicationConflict(CANDIDATE_NOT_READY)
    if validation.get("status") != "green":
        raise PublicationConflict(CANDIDATE_NOT_READY)
    if validation.get("head_sha") != candidate.get("head_sha") or not validation.get("run_id"):
        raise PublicationConflict(CANDIDATE_NOT_READY)
    normalized = {
        "candidate_id": str(candidate["candidate_id"]),
        "lane": str(candidate["lane"]),
        "work_item_id": str(candidate["work_item_id"]),
        "pr_number": int(candidate["pr_number"]),
        "head_sha": str(candidate["head_sha"]),
        "prequeue_validation": {
            "status": "green",
            "head_sha": str(validation["head_sha"]),
            "run_id": str(validation["run_id"]),
        },
    }
    if candidate.get("write_set") is not None:
        normalized["write_set"] = candidate["write_set"]
    if candidate.get("dependency_fingerprint") is not None:
        normalized["dependency_fingerprint"] = candidate["dependency_fingerprint"]
    return normalized

def submit_ready_candidate(state: dict[str, Any], *, expected_generation: int, candidate: dict[str, Any]) -> dict[str, Any]:
    _generation(state, expected_generation)
    item = _candidate(candidate)
    ready = _ready(state)
    ids = {x.get("candidate_id") for x in ready}
    heads = {x.get("head_sha") for x in ready}
    if item["candidate_id"] in ids or item["head_sha"] in heads:
        raise PublicationConflict("candidate already queued")
    return {**state, "generation": expected_generation + 1, "ready": ready + [item]}

def withdraw_ready_candidate(state: dict[str, Any], *, expected_generation: int, candidate_id: str, reason: str) -> dict[str, Any]:
    _generation(state, expected_generation)
    ready = _ready(state)
    match = next((x for x in ready if x.get("candidate_id") == candidate_id), None)
    if match is None:
        raise PublicationConflict("candidate not queued")
    if not reason.strip():
        raise PublicationConflict("withdraw reason is required")
    remaining = [x for x in ready if x.get("candidate_id") != candidate_id]
    history = list(state.get("history", []))
    history.append({**match, "status": "withdrawn", "reason": reason})
    return {**state, "generation": expected_generation + 1, "ready": remaining, "history": history}

def fail_ready_candidate(state: dict[str, Any], *, expected_generation: int, candidate_id: str, reason: str) -> dict[str, Any]:
    _generation(state, expected_generation)
    ready = _ready(state)
    if not ready or ready[0].get("candidate_id") != candidate_id:
        raise PublicationConflict(QUEUE_ORDER)
    if not reason.strip():
        raise PublicationConflict("failure reason is required")
    failed = ready[0]
    history = list(state.get("history", []))
    history.append({**failed, "status": "failed", "reason": reason})
    return {**state, "generation": expected_generation + 1, "ready": ready[1:], "history": history}

def validate_integration_authorization(
    state: dict[str, Any],
    *,
    candidate_id: str,
    fresh_main_sha: str,
    pr_head_sha: str,
    integration_receipt: dict[str, Any],
) -> list[str]:
    errors: list[str] = []
    ready = _ready(state)
    if not ready or ready[0].get("candidate_id") != candidate_id:
        errors.append(QUEUE_ORDER)
        return errors
    candidate = ready[0]
    if candidate.get("head_sha") != pr_head_sha:
        errors.append(HEAD_MISMATCH)
    if not isinstance(integration_receipt, dict):
        errors.append(INTEGRATION_NOT_BOUND)
        return sorted(set(errors))
    if integration_receipt.get("candidate_id") != candidate_id:
        errors.append(INTEGRATION_NOT_BOUND)
    if integration_receipt.get("candidate_head") != candidate.get("head_sha"):
        errors.append(HEAD_MISMATCH)
    if integration_receipt.get("status") != "green" or not integration_receipt.get("run_id"):
        errors.append(INTEGRATION_NOT_BOUND)
    if integration_receipt.get("base_sha") != fresh_main_sha:
        errors.append(STALE_INTEGRATION)
    return sorted(set(errors))

def validate_single_lane_protected_main_write(
    *,
    target_repo: str,
    fresh_main_sha: str,
    mutation_kind: str,
    expected_head_sha: str,
    pr_head_sha: str,
    integration_receipt: dict[str, Any],
) -> list[str]:
    """Fail-closed protected-main gate without multi-lane queue coordination."""
    if target_repo not in PROTECTED_REPOSITORIES:
        return []
    if mutation_kind != "pull_request_merge":
        return [DIRECT_MAIN_MUTATION]
    errors: list[str] = []
    if not expected_head_sha or pr_head_sha != expected_head_sha:
        errors.append(HEAD_MISMATCH)
    if not isinstance(integration_receipt, dict):
        errors.append(INTEGRATION_NOT_BOUND)
        return sorted(set(errors))
    if integration_receipt.get("candidate_head") != expected_head_sha:
        errors.append(HEAD_MISMATCH)
    if integration_receipt.get("status") != "green" or not integration_receipt.get("run_id"):
        errors.append(INTEGRATION_NOT_BOUND)
    if integration_receipt.get("base_sha") != fresh_main_sha:
        errors.append(STALE_INTEGRATION)
    return sorted(set(errors))

def validate_protected_main_write(
    state: dict[str, Any],
    *,
    target_repo: str,
    fresh_main_sha: str,
    mutation_kind: str,
    candidate_id: str | None = None,
    pr_head_sha: str | None = None,
    integration_receipt: dict[str, Any] | None = None,
) -> list[str]:
    if target_repo not in PROTECTED_REPOSITORIES:
        return []
    if mutation_kind != "pull_request_merge":
        return [DIRECT_MAIN_MUTATION]
    return validate_integration_authorization(
        state,
        candidate_id=candidate_id or "",
        fresh_main_sha=fresh_main_sha,
        pr_head_sha=pr_head_sha or "",
        integration_receipt=integration_receipt or {},
    )

def reconcile_durable_publication(
    state: dict[str, Any],
    *,
    expected_generation: int,
    candidate_id: str,
    observed_head_sha: str,
    merge_sha: str,
) -> dict[str, Any]:
    _generation(state, expected_generation)
    ready = _ready(state)
    if not ready or ready[0].get("candidate_id") != candidate_id:
        raise PublicationConflict(QUEUE_ORDER)
    candidate = ready[0]
    if candidate.get("head_sha") != observed_head_sha:
        raise PublicationConflict(HEAD_MISMATCH)
    if not merge_sha:
        raise PublicationConflict("durable merge SHA is required")
    history = list(state.get("history", []))
    history.append({**candidate, "status": "published", "merge_sha": merge_sha})
    return {
        **state,
        "generation": expected_generation + 1,
        "ready": ready[1:],
        "history": history,
        "last_merge_sha": merge_sha,
    }
