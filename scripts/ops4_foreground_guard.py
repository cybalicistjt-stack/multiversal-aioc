#!/usr/bin/env python3
"""OPS4 foreground execution durability and circuit-breaker guard."""
from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

MAX_TOOL_BATCHES = 6
MAX_REMOTE_OPERATIONS = 18
MAX_RECOVERY_READS = 4

TOOL_BUDGET = "OPS4.FOREGROUND_TOOL_BUDGET_EXCEEDED"
REMOTE_BUDGET = "OPS4.FOREGROUND_REMOTE_BUDGET_EXCEEDED"
CI_OBSERVATION_BUDGET = "OPS4.FOREGROUND_CI_OBSERVATION_BUDGET_EXCEEDED"
FAILURE_INSPECTION_BUDGET = "OPS4.FOREGROUND_FAILURE_INSPECTION_BUDGET_EXCEEDED"
SLEEP_WAIT = "OPS4.FOREGROUND_SLEEP_WAIT_FORBIDDEN"
RECOVERY_BUDGET = "OPS4.FOREGROUND_RECOVERY_SCAN_TOO_BROAD"
SAME_BRANCH_SPECULATION = "OPS4.FOREGROUND_SAME_BRANCH_SPECULATION"
LEASE_HELD = "OPS4.FOREGROUND_LEASE_HELD_AT_WAIT"
RESUME_CAPSULE_REQUIRED = "OPS4.FOREGROUND_RESUME_CAPSULE_REQUIRED"
CIRCUIT_OPEN = "OPS4.FOREGROUND_INTERRUPTION_CIRCUIT_OPEN"
DURABLE_EXECUTOR_REQUIRED = "OPS4.DURABLE_EXECUTOR_REQUIRED"
INVALID_TRACE = "OPS4.INVALID_FOREGROUND_TRACE"

_CAPSULE_KEYS = {
    "work_item_id",
    "branch",
    "head",
    "phase",
    "last_material_progress",
    "next_action",
}

def _nonnegative_int(value: Any) -> bool:
    return isinstance(value, int) and not isinstance(value, bool) and value >= 0

def _valid_capsule(value: Any) -> bool:
    if not isinstance(value, dict):
        return False
    for key in _CAPSULE_KEYS:
        field = value.get(key)
        if field is None:
            return False
        if isinstance(field, str) and not field.strip():
            return False
    return True

def validate_foreground_trace(trace: dict[str, Any]) -> list[str]:
    if trace.get("mode") != "foreground_chat":
        return []

    errors: list[str] = []
    numeric_fields = (
        "tool_batches",
        "remote_operations",
        "ci_observations",
        "failed_job_inspections",
        "failure_log_fetches",
        "sleep_wait_calls",
        "same_branch_mutations_while_ci_running",
        "interruptions_this_attempt",
    )
    if any(not _nonnegative_int(trace.get(field, 0)) for field in numeric_fields):
        return [INVALID_TRACE]

    if trace.get("tool_batches", 0) > MAX_TOOL_BATCHES:
        errors.append(TOOL_BUDGET)
    if trace.get("remote_operations", 0) > MAX_REMOTE_OPERATIONS:
        errors.append(REMOTE_BUDGET)
    if trace.get("ci_observations", 0) > 1:
        errors.append(CI_OBSERVATION_BUDGET)
    if trace.get("failed_job_inspections", 0) > 1 or trace.get("failure_log_fetches", 0) > 1:
        errors.append(FAILURE_INSPECTION_BUDGET)
    if trace.get("sleep_wait_calls", 0) > 0:
        errors.append(SLEEP_WAIT)
    if len(trace.get("recovery_reads", [])) > MAX_RECOVERY_READS:
        errors.append(RECOVERY_BUDGET)
    if trace.get("same_branch_mutations_while_ci_running", 0) > 0:
        errors.append(SAME_BRANCH_SPECULATION)

    wait_boundary = bool(
        trace.get("wait_boundary")
        or trace.get("interrupted")
        or trace.get("budget_boundary")
        or trace.get("tool_session_abort")
    )
    interruptions = trace.get("interruptions_this_attempt", 0)
    circuit_open = interruptions >= 2

    if wait_boundary and trace.get("foreground_lease_held") is True:
        errors.append(LEASE_HELD)
    if (wait_boundary or circuit_open) and not _valid_capsule(trace.get("resume_capsule")):
        errors.append(RESUME_CAPSULE_REQUIRED)
    if circuit_open and not trace.get("durable_executor_active") and not trace.get("harness_repair_only"):
        errors.append(CIRCUIT_OPEN)

    if (
        trace.get("must_survive_disconnect")
        or trace.get("multiple_acceptance_gates_remaining")
        or trace.get("planned_remote_operations", 0) > MAX_REMOTE_OPERATIONS
        or trace.get("planned_tool_batches", 0) > MAX_TOOL_BATCHES
    ) and not trace.get("durable_executor_active") and not trace.get("bounded_quantum_only"):
        errors.append(DURABLE_EXECUTOR_REQUIRED)

    return sorted(set(errors))

def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("trace")
    args = parser.parse_args()
    trace = json.loads(Path(args.trace).read_text(encoding="utf-8"))
    errors = validate_foreground_trace(trace)
    print(json.dumps({"status":"FAIL" if errors else "PASS","errors":errors},sort_keys=True))
    return 1 if errors else 0

if __name__ == "__main__":
    raise SystemExit(main())
