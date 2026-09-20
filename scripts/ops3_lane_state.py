#!/usr/bin/env python3
"""Operations V3 milestone-only persistent-lane execution state.

Lane state is a recovery state machine, not an activity log. Ordinary attempts
have exactly three execution milestones before successor reseed:
start -> prequeue_green -> published. Repository, PR, CI and publication-queue
systems own the intermediate evidence and must not be mirrored here.
"""
from __future__ import annotations

from typing import Any

LANES = frozenset({"msas", "mrcs", "oarc"})
SCHEMA_VERSION = "1.1.0"


class LaneStateConflict(RuntimeError):
    pass


def coordination_branch(lane: str) -> str:
    if lane not in LANES:
        raise LaneStateConflict(f"unsupported lane: {lane}")
    return f"ops3-lane-state/{lane}"


def initial_state(lane: str, *, revision: int, selected_work_item: str, attempt_id: str) -> dict[str, Any]:
    if lane not in LANES:
        raise LaneStateConflict(f"unsupported lane: {lane}")
    if not selected_work_item.strip() or not attempt_id.strip():
        raise LaneStateConflict("selected work item and attempt are required")
    return {
        "schema_version": SCHEMA_VERSION,
        "lane": lane,
        "revision": revision,
        "selected_work_item": selected_work_item,
        "attempt_id": attempt_id,
        "execution_status": "selected_not_started",
        "implementation_branch": None,
        "progress_seq": 0,
        "last_progress": None,
        "terminal": False,
    }


def _check(state: dict[str, Any], *, expected_revision: int, lane: str) -> None:
    if lane not in LANES or state.get("lane") != lane:
        raise LaneStateConflict("lane mismatch")
    if state.get("revision") != expected_revision:
        raise LaneStateConflict("lane-state revision changed")


def _evidence(value: str, label: str) -> str:
    cleaned = value.strip()
    if not cleaned:
        raise LaneStateConflict(f"{label} is required")
    return cleaned


def start_execution(
    state: dict[str, Any],
    *,
    expected_revision: int,
    lane: str,
    implementation_branch: str,
    evidence: str,
) -> dict[str, Any]:
    _check(state, expected_revision=expected_revision, lane=lane)
    if state.get("execution_status") != "selected_not_started":
        raise LaneStateConflict("lane attempt is not startable")
    branch = _evidence(implementation_branch, "implementation branch")
    start_evidence = _evidence(evidence, "start evidence")
    return {
        **state,
        "schema_version": SCHEMA_VERSION,
        "revision": expected_revision + 1,
        "execution_status": "in_progress",
        "implementation_branch": branch,
        "progress_seq": 1,
        "last_progress": {"kind": "started", "evidence": start_evidence},
        "terminal": False,
    }


def mark_prequeue_green(
    state: dict[str, Any],
    *,
    expected_revision: int,
    lane: str,
    candidate_head: str,
    validation_run: str,
) -> dict[str, Any]:
    _check(state, expected_revision=expected_revision, lane=lane)
    if state.get("execution_status") != "in_progress":
        raise LaneStateConflict("prequeue green requires in-progress execution")
    head = _evidence(candidate_head, "candidate head")
    run = _evidence(validation_run, "validation run")
    return {
        **state,
        "schema_version": SCHEMA_VERSION,
        "revision": expected_revision + 1,
        "execution_status": "prequeue_green",
        "progress_seq": 2,
        "last_progress": {
            "kind": "prequeue_green",
            "evidence": f"exact head {head} passed prequeue validation run {run}",
        },
        "prequeue_green": {"candidate_head": head, "validation_run": run},
    }


def invalidate_prequeue_candidate(
    state: dict[str, Any],
    *,
    expected_revision: int,
    lane: str,
    reason: str,
) -> dict[str, Any]:
    """Exceptional repair transition when a previously green exact head is no longer publishable."""
    _check(state, expected_revision=expected_revision, lane=lane)
    if state.get("execution_status") != "prequeue_green":
        raise LaneStateConflict("only a prequeue-green candidate can be invalidated")
    why = _evidence(reason, "invalidation reason")
    result = {
        **state,
        "schema_version": SCHEMA_VERSION,
        "revision": expected_revision + 1,
        "execution_status": "in_progress",
        "last_progress": {
            "kind": "candidate_invalidated",
            "evidence": why,
        },
    }
    result.pop("prequeue_green", None)
    return result


def mark_published(
    state: dict[str, Any],
    *,
    expected_revision: int,
    lane: str,
    candidate_head: str,
    merge_sha: str,
    ready_candidate_id: str,
) -> dict[str, Any]:
    _check(state, expected_revision=expected_revision, lane=lane)
    if state.get("execution_status") != "prequeue_green":
        raise LaneStateConflict("publication requires prequeue-green state")
    head = _evidence(candidate_head, "candidate head")
    green = state.get("prequeue_green", {})
    if green.get("candidate_head") != head:
        raise LaneStateConflict("published head differs from prequeue-green head")
    merge = _evidence(merge_sha, "merge sha")
    candidate = _evidence(ready_candidate_id, "ready candidate id")
    return {
        **state,
        "schema_version": SCHEMA_VERSION,
        "revision": expected_revision + 1,
        "execution_status": "published",
        "progress_seq": 3,
        "last_progress": {
            "kind": "published",
            "evidence": f"{candidate} published exact head {head} as {merge}",
        },
        "publication": {
            "candidate_head": head,
            "merge_sha": merge,
            "ready_candidate_id": candidate,
        },
    }


def reseed_successor(
    state: dict[str, Any],
    *,
    expected_revision: int,
    lane: str,
    successor_work_item: str,
    successor_attempt_id: str,
    closeout_merge_sha: str,
    closeout_validation_run: str,
    closeout_ready_candidate_id: str,
) -> dict[str, Any]:
    """Finish the prior attempt and deterministically reset the lane for its selected successor."""
    _check(state, expected_revision=expected_revision, lane=lane)
    if state.get("execution_status") != "published":
        raise LaneStateConflict("successor reseed requires durable application publication")
    successor = _evidence(successor_work_item, "successor work item")
    successor_attempt = _evidence(successor_attempt_id, "successor attempt id")
    closeout_merge = _evidence(closeout_merge_sha, "closeout merge sha")
    closeout_run = _evidence(closeout_validation_run, "closeout validation run")
    closeout_candidate = _evidence(closeout_ready_candidate_id, "closeout ready candidate id")
    publication = state.get("publication", {})
    if not publication.get("merge_sha") or not publication.get("ready_candidate_id"):
        raise LaneStateConflict("application publication receipt is incomplete")
    last_completed = {
        "work_item_id": state.get("selected_work_item"),
        "attempt_id": state.get("attempt_id"),
        "application_merge_sha": publication["merge_sha"],
        "application_validation_run": state.get("prequeue_green", {}).get("validation_run"),
        "application_ready_candidate": publication["ready_candidate_id"],
        "closeout_merge_sha": closeout_merge,
        "closeout_validation_run": closeout_run,
        "closeout_ready_candidate": closeout_candidate,
    }
    return {
        "schema_version": SCHEMA_VERSION,
        "lane": lane,
        "revision": expected_revision + 1,
        "selected_work_item": successor,
        "attempt_id": successor_attempt,
        "execution_status": "selected_not_started",
        "implementation_branch": None,
        "progress_seq": 0,
        "last_progress": None,
        "terminal": False,
        "last_completed": last_completed,
    }
