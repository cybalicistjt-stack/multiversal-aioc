#!/usr/bin/env python3
"""Decide whether a governed owner-AI execution turn may emit a final response."""
from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any


CONTRACT_PATH = Path(
    "governance/ai/interaction-system/EXECUTION_TERMINATION_CONTRACT.json"
)
CASES_PATH = Path(
    "governance/ai/interaction-system/evaluation/EXECUTION_TERMINATION_CASES.json"
)
EXECUTION_MODES = {"execution", "status_and_continue", "keep_going"}
NON_EXECUTION_MODES = {"get_ready", "status_only", "analysis_only"}
BLOCKER_CLASSES = {
    "owner_only",
    "environment_unavailable",
    "source_unavailable",
    "safety",
    "irrecoverable_external",
}


class PreflightError(RuntimeError):
    def __init__(self, code: str, message: str) -> None:
        super().__init__(message)
        self.code = code


def _require(condition: bool, code: str, message: str) -> None:
    if not condition:
        raise PreflightError(code, message)


def _load_json(path: Path) -> dict[str, Any]:
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError as exc:
        raise PreflightError("MVTERM-INPUT-MISSING", f"missing JSON input: {path}") from exc
    except json.JSONDecodeError as exc:
        raise PreflightError(
            "MVTERM-INPUT-INVALID", f"invalid JSON input {path}: {exc}"
        ) from exc
    _require(
        isinstance(value, dict),
        "MVTERM-INPUT-TYPE",
        f"expected object JSON: {path}",
    )
    return value


def _decision(decision: str, reason_code: str, reason: str) -> dict[str, Any]:
    return {
        "schema_version": "1.0.0",
        "status": "PASS",
        "decision": decision,
        "reason_code": reason_code,
        "reason": reason,
    }


def evaluate(state: dict[str, Any]) -> dict[str, Any]:
    """Evaluate one ephemeral turn state against the termination contract."""
    mode = state.get("command_mode")
    _require(
        mode in EXECUTION_MODES | NON_EXECUTION_MODES,
        "MVTERM-MODE-INVALID",
        f"unsupported command_mode: {mode!r}",
    )
    status = state.get("work_item_status")
    _require(
        isinstance(status, str) and bool(status.strip()),
        "MVTERM-STATUS-MISSING",
        "work_item_status must be a non-empty string",
    )
    active_async = state.get("active_async_operations")
    _require(
        isinstance(active_async, int) and active_async >= 0,
        "MVTERM-ASYNC-INVALID",
        "active_async_operations must be a non-negative integer",
    )
    pending = state.get("pending_authorized_steps")
    _require(
        isinstance(pending, list) and all(isinstance(item, str) for item in pending),
        "MVTERM-PENDING-INVALID",
        "pending_authorized_steps must be an array of strings",
    )
    successor_required = state.get("successor_selection_required")
    successor_selected = state.get("successor_selected")
    boundary_completed = state.get("requested_boundary_completed")
    for key, value in (
        ("successor_selection_required", successor_required),
        ("successor_selected", successor_selected),
        ("requested_boundary_completed", boundary_completed),
    ):
        _require(
            isinstance(value, bool),
            "MVTERM-BOOLEAN-INVALID",
            f"{key} must be boolean",
        )

    if mode in NON_EXECUTION_MODES:
        return _decision(
            "ALLOW_FINAL_RESPONSE",
            "MVTERM-EXPLICIT-NONEXECUTION",
            f"owner selected explicit non-execution mode {mode}",
        )

    if active_async:
        return _decision(
            "CONTINUE_EXECUTION",
            "MVTERM-ASYNC-ACTIVE",
            f"{active_async} required asynchronous operation(s) remain active",
        )

    if status == "completed_verified":
        if successor_required and not successor_selected:
            return _decision(
                "CONTINUE_EXECUTION",
                "MVTERM-SUCCESSOR-PENDING",
                "completed work still requires canonical strict-successor selection",
            )
        if mode == "keep_going" and not boundary_completed:
            return _decision(
                "CONTINUE_EXECUTION",
                "MVTERM-BOUNDARY-PENDING",
                "the owner-requested keep-going boundary is not complete",
            )
        if pending:
            return _decision(
                "CONTINUE_EXECUTION",
                "MVTERM-AUTHORIZED-WORK-PENDING",
                "authorized closeout work remains after completion evidence",
            )
        return _decision(
            "ALLOW_FINAL_RESPONSE",
            "MVTERM-COMPLETED-VERIFIED",
            "the bounded unit is completed_verified at its requested boundary",
        )

    blocker = state.get("genuine_blocker")
    if isinstance(blocker, dict):
        blocker_class = blocker.get("class")
        evidence = blocker.get("evidence")
        recovery_attempted = blocker.get("recovery_attempted")
        blocks_all = blocker.get("blocks_all_authorized_progress")
        if (
            blocker_class in BLOCKER_CLASSES
            and isinstance(evidence, list)
            and any(isinstance(item, str) and item.strip() for item in evidence)
            and recovery_attempted is True
            and blocks_all is True
        ):
            return _decision(
                "ALLOW_FINAL_RESPONSE",
                "MVTERM-GENUINE-BLOCKER",
                f"verified {blocker_class} blocker prevents all further authorized progress; {len(pending)} authorized step(s) remain durably resumable",
            )
        return _decision(
            "CONTINUE_EXECUTION",
            "MVTERM-BLOCKER-EVIDENCE-INSUFFICIENT",
            "claimed blocker lacks the required class, evidence, recovery, or all-progress proof",
        )

    if pending:
        return _decision(
            "CONTINUE_EXECUTION",
            "MVTERM-AUTHORIZED-WORK-PENDING",
            f"{len(pending)} authorized step(s) remain",
        )

    return _decision(
        "CONTINUE_EXECUTION",
        "MVTERM-NONTERMINAL-STATE",
        f"work item remains {status!r} without a verified terminal condition",
    )


def self_test(root: Path) -> dict[str, Any]:
    contract = _load_json(root / CONTRACT_PATH)
    _require(
        contract.get("schema_version") == "1.2.0",
        "MVTERM-CONTRACT-SCHEMA",
        "termination contract schema mismatch",
    )
    _require(
        contract.get("control_id") == "C-EXECUTION-TERMINATION-GATE",
        "MVTERM-CONTRACT-ID",
        "termination contract control identity mismatch",
    )
    cases = _load_json(root / CASES_PATH)
    rows = cases.get("cases")
    _require(
        isinstance(rows, list) and len(rows) >= 8,
        "MVTERM-CASES-MISSING",
        "termination preflight requires at least eight regression cases",
    )
    seen: set[str] = set()
    for row in rows:
        _require(
            isinstance(row, dict),
            "MVTERM-CASE-TYPE",
            "termination case must be an object",
        )
        case_id = row.get("case_id")
        _require(
            isinstance(case_id, str) and case_id not in seen,
            "MVTERM-CASE-ID",
            f"invalid or duplicate termination case id: {case_id!r}",
        )
        seen.add(case_id)
        observed = evaluate(row.get("state", {}))
        _require(
            observed["decision"] == row.get("expected_decision"),
            "MVTERM-CASE-DECISION",
            f"{case_id}: expected {row.get('expected_decision')}, observed {observed['decision']}",
        )
        _require(
            observed["reason_code"] == row.get("expected_reason_code"),
            "MVTERM-CASE-REASON",
            f"{case_id}: expected {row.get('expected_reason_code')}, observed {observed['reason_code']}",
        )
    return {
        "schema_version": "1.0.0",
        "status": "PASS",
        "control_id": "C-EXECUTION-TERMINATION-GATE",
        "cases_passed": len(rows),
        "case_ids": sorted(seen),
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--state")
    parser.add_argument("--self-test", action="store_true")
    parser.add_argument("--root", default=".")
    parser.add_argument("--output")
    args = parser.parse_args()
    try:
        _require(
            bool(args.state) ^ bool(args.self_test),
            "MVTERM-INVOCATION",
            "choose exactly one of --state or --self-test",
        )
        if args.self_test:
            result = self_test(Path(args.root).resolve())
        else:
            result = evaluate(_load_json(Path(args.state).resolve()))
    except (OSError, PreflightError) as exc:
        code = exc.code if isinstance(exc, PreflightError) else "MVTERM-IO"
        result = {
            "schema_version": "1.0.0",
            "status": "FAIL",
            "decision": "CONTINUE_EXECUTION",
            "reason_code": code,
            "reason": str(exc),
        }
    payload = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.output:
        Path(args.output).write_text(payload, encoding="utf-8")
    print(payload, end="")
    return 0 if result["status"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
