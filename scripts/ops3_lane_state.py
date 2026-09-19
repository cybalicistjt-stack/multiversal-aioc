#!/usr/bin/env python3
"""Independent Operations V3 lane execution-state journal."""
from __future__ import annotations

from typing import Any

LANES = frozenset({"msas", "mrcs", "mvps"})

class LaneStateConflict(RuntimeError):
    pass

def coordination_branch(lane: str) -> str:
    if lane not in LANES:
        raise LaneStateConflict(f"unsupported lane: {lane}")
    return f"ops3-lane-state/{lane}"

def initial_state(lane: str, *, revision: int, selected_work_item: str, attempt_id: str) -> dict[str, Any]:
    if lane not in LANES:
        raise LaneStateConflict(f"unsupported lane: {lane}")
    return {
        "schema_version": "1.0.0",
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

def start_execution(state: dict[str, Any], *, expected_revision: int, lane: str, implementation_branch: str, evidence: str) -> dict[str, Any]:
    _check(state, expected_revision=expected_revision, lane=lane)
    if state.get("execution_status") != "selected_not_started":
        raise LaneStateConflict("lane attempt is not startable")
    if not implementation_branch.strip() or not evidence.strip():
        raise LaneStateConflict("implementation branch and evidence are required")
    return {
        **state,
        "revision": expected_revision + 1,
        "execution_status": "in_progress",
        "implementation_branch": implementation_branch,
        "progress_seq": int(state.get("progress_seq", 0)) + 1,
        "last_progress": {"kind": "started", "evidence": evidence},
    }

def record_progress(state: dict[str, Any], *, expected_revision: int, lane: str, kind: str, evidence: str) -> dict[str, Any]:
    _check(state, expected_revision=expected_revision, lane=lane)
    if state.get("terminal"):
        raise LaneStateConflict("terminal lane attempt cannot record progress")
    if not kind.strip() or not evidence.strip():
        raise LaneStateConflict("progress kind and evidence are required")
    return {
        **state,
        "revision": expected_revision + 1,
        "progress_seq": int(state.get("progress_seq", 0)) + 1,
        "last_progress": {"kind": kind, "evidence": evidence},
    }

def complete_execution(state: dict[str, Any], *, expected_revision: int, lane: str, evidence: str) -> dict[str, Any]:
    _check(state, expected_revision=expected_revision, lane=lane)
    if not evidence.strip():
        raise LaneStateConflict("completion evidence is required")
    return {
        **state,
        "revision": expected_revision + 1,
        "execution_status": "completed_verified",
        "progress_seq": int(state.get("progress_seq", 0)) + 1,
        "last_progress": {"kind": "completed_verified", "evidence": evidence},
        "terminal": True,
    }
