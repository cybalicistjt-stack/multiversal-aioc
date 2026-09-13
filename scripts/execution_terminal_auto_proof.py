#!/usr/bin/env python3
"""Produce terminal reconciliation evidence inside canonical-main repository health.

A newly completed implementation item is proved in the same main-health run that
validates its closeout projection. If the main push did not introduce a new completed
implementation item, the control emits a deterministic SKIP record.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import subprocess
from pathlib import Path
from typing import Any

from execution_termination_preflight import evaluate

POINTER = Path("governance/ai/runtime/CURRENT_WORK_POINTER.json")


class TerminalAutoProofError(RuntimeError):
    pass


def _require(condition: bool, message: str) -> None:
    if not condition:
        raise TerminalAutoProofError(message)


def _canonical_digest(bundle: dict[str, Any]) -> str:
    material = {key: value for key, value in bundle.items() if key != "reconciliation_digest"}
    return hashlib.sha256(
        json.dumps(material, sort_keys=True, separators=(",", ":"), ensure_ascii=True).encode("utf-8")
    ).hexdigest()


def build_terminal_state(checkpoint: dict[str, Any]) -> dict[str, Any]:
    _require(checkpoint.get("status") == "completed_verified", "checkpoint is not completed_verified")
    successor = checkpoint.get("strict_successor")
    _require(isinstance(successor, str) and bool(successor.strip()), "strict_successor is required")
    completion = checkpoint.get("completion_evidence")
    _require(isinstance(completion, dict), "completion_evidence is required")
    validation_run = completion.get("application_validation_run")
    _require(isinstance(validation_run, int) and not isinstance(validation_run, bool) and validation_run > 0, "application_validation_run is required")
    seed = checkpoint.get("terminal_reconciliation_seed")
    _require(isinstance(seed, dict), "terminal_reconciliation_seed is required")

    cycle_id = seed.get("cycle_id")
    trace_id = seed.get("trace_id")
    _require(isinstance(cycle_id, str) and bool(cycle_id.strip()), "cycle_id is required")
    _require(isinstance(trace_id, str) and bool(trace_id.strip()), "trace_id is required")
    operations = seed.get("operation_ledger")
    effects = seed.get("side_effect_ledger")
    _require(isinstance(operations, list) and bool(operations), "operation_ledger is required")
    _require(isinstance(effects, list), "side_effect_ledger is required")

    reconciliation: dict[str, Any] = {
        "desired_state": "terminal_verified",
        "trace_id": trace_id,
        "resume_generation": seed.get("resume_generation", 0),
        "resumed_from_cycle_id": seed.get("resumed_from_cycle_id"),
        "operation_ledger": operations,
        "next_operation_id": None,
        "side_effect_ledger": effects,
        "progress": {
            "reconciliation_passes": 1,
            "consecutive_no_progress_passes": 0,
            "diagnostic_mode": False,
        },
        "verification_evidence": [
            {
                "evidence_id": f"application-validation-{validation_run}",
                "kind": "ci_run",
                "result": "pass",
                "independent": True,
                "bound_cycle_id": cycle_id,
                "trace_id": trace_id,
            }
        ],
    }
    reconciliation["reconciliation_digest"] = _canonical_digest(reconciliation)

    elapsed = seed.get("elapsed_active_minutes")
    _require(isinstance(elapsed, (int, float)) and not isinstance(elapsed, bool) and elapsed >= 0, "completed checkpoint requires elapsed_active_minutes")
    safe_work = seed.get("safe_same_lane_work_available")
    dynamic_fill = seed.get("dynamic_fill_attempted")
    fill_exit_reason = seed.get("fill_exit_reason")
    _require(isinstance(safe_work, bool), "safe_same_lane_work_available must be boolean")
    _require(isinstance(dynamic_fill, bool), "dynamic_fill_attempted must be boolean")
    _require(fill_exit_reason in {"safe_work_exhausted", "closeout_switch_reached"}, "completed checkpoint requires a terminal fill_exit_reason")

    return {
        "command_mode": "execution",
        "work_item_status": "completed_verified",
        "active_async_operations": 0,
        "pending_authorized_steps": [],
        "successor_selection_required": True,
        "successor_selected": True,
        "requested_boundary_completed": True,
        "pull_request_state": "merged",
        "current_head_validation_state": "passed",
        "merge_closeout_pending": False,
        "execution_envelope": {
            "cycle_id": cycle_id,
            "phase": "closed",
            "elapsed_active_minutes": elapsed,
            "closeout_switch_active_minute": 16.0,
            "target_cycle_minutes": 24.0,
            "safe_same_lane_work_available": safe_work,
            "dynamic_fill_attempted": dynamic_fill,
            "closeout_complete": True,
            "fill_exit_reason": fill_exit_reason,
        },
        "execution_reconciliation": reconciliation,
    }


def _load_pointer(root: Path) -> dict[str, Any]:
    return json.loads((root / POINTER).read_text(encoding="utf-8"))


def _load_parent_pointer(root: Path, parent_head: str) -> dict[str, Any] | None:
    completed = subprocess.run(
        ["git", "show", f"{parent_head}:{POINTER.as_posix()}"],
        cwd=root,
        text=True,
        capture_output=True,
        check=False,
    )
    if completed.returncode != 0:
        return None
    return json.loads(completed.stdout)


def _latest_completed(pointer: dict[str, Any]) -> dict[str, Any] | None:
    rows = pointer.get("recently_completed_implementation_work")
    if not isinstance(rows, list) or not rows or not isinstance(rows[0], dict):
        return None
    return rows[0]


def prove_new_completion(root: Path, parent_head: str) -> dict[str, Any]:
    current = _load_pointer(root)
    parent = _load_parent_pointer(root, parent_head)
    current_row = _latest_completed(current)
    parent_row = _latest_completed(parent or {})
    if current_row is None:
        return {"schema_version": "1.0.0", "status": "SKIP", "reason": "no_completed_implementation_record"}
    if parent_row and parent_row.get("work_item_id") == current_row.get("work_item_id"):
        return {"schema_version": "1.0.0", "status": "SKIP", "reason": "no_new_completed_implementation"}

    work_item = current_row.get("work_item_id")
    _require(isinstance(work_item, str) and bool(work_item.strip()), "completed work_item_id is required")
    checkpoint_path = current_row.get("checkpoint_path") or f"governance/ai/work-state/{work_item}-attempt-001.json"
    checkpoint = json.loads((root / checkpoint_path).read_text(encoding="utf-8"))
    successor = checkpoint.get("strict_successor")
    active = current.get("active_attempt", {})
    _require(active.get("work_item_id") == successor, "strict successor is not the current selected work item")
    _require(active.get("status") == "selected_not_started", "strict successor must remain selected_not_started at terminal proof")
    _require(active.get("implementation_authority") is False, "strict successor must not inherit implementation authority")

    state = build_terminal_state(checkpoint)
    decision = evaluate(state)
    _require(decision.get("decision") == "ALLOW_FINAL_RESPONSE", f"termination preflight rejected completion: {decision}")
    result = {
        "schema_version": "1.0.0",
        "status": "PASS",
        "work_item_id": work_item,
        "checkpoint_path": checkpoint_path,
        "decision": decision.get("decision"),
        "reason_code": decision.get("reason_code"),
        "state_digest_sha256": hashlib.sha256(
            json.dumps(state, sort_keys=True, separators=(",", ":"), ensure_ascii=True).encode("utf-8")
        ).hexdigest(),
    }
    return result


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", default=".")
    parser.add_argument("--head", required=True)
    parser.add_argument("--parent-head", required=True)
    parser.add_argument("--output")
    args = parser.parse_args()
    root = Path(args.root).resolve()
    _require(len(args.head) == 40, "head must be a commit SHA")
    _require(len(args.parent_head) == 40, "parent-head must be a commit SHA")
    result = prove_new_completion(root, args.parent_head)
    payload = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.output:
        Path(args.output).write_text(payload, encoding="utf-8")
    print(payload, end="")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except TerminalAutoProofError as exc:
        print(json.dumps({"schema_version": "1.0.0", "status": "FAIL", "error": str(exc)}, sort_keys=True))
        raise SystemExit(1)
