#!/usr/bin/env python3
"""Operations V3 FIFO publication reservation queue.

The queue is executor coordination only. It never selects work or grants product
scope. Reservation order is stable. Publication preparation/reconciliation and
validation occur only after a reservation activates at the queue head.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

STALE_MAIN = "OPS3.STALE_MAIN"
HEAD_MISMATCH = "OPS3.HEAD_MISMATCH"
HOLDER_MISMATCH = "OPS3.HOLDER_MISMATCH"
LEASE_NOT_HELD = "OPS3.LEASE_NOT_HELD"
QUEUE_ORDER = "OPS3.QUEUE_ORDER"
VALIDATION_NOT_BOUND = "OPS3.VALIDATION_NOT_BOUND"
RECOVERY_MAIN_MISMATCH = "OPS3.RECOVERY_MAIN_MISMATCH"
RECOVERY_LOCATION_REQUIRED = "OPS3.RECOVERY_LOCATION_REQUIRED"

class LeaseConflict(RuntimeError):
    pass

def coordination_branch(target_repo: str) -> str:
    slug = target_repo.lower().replace("/", "-").replace("_", "-")
    return f"ops3-merge-lease/{slug}"

def free_lease(target_repo: str, *, generation: int = 0, last_merge_sha: str | None = None) -> dict[str, Any]:
    return {
        "schema_version": "2.0.0",
        "target_repo": target_repo,
        "status": "free",
        "generation": generation,
        "holder": None,
        "active_reservation_id": None,
        "turn_base": None,
        "validated_head": None,
        "validated_base": None,
        "queue": [],
        "last_merge_sha": last_merge_sha,
    }

def _generation(current: dict[str, Any], expected_generation: int) -> None:
    if current.get("generation") != expected_generation:
        raise LeaseConflict("lease generation changed")

def _queue(current: dict[str, Any]) -> list[dict[str, str]]:
    raw = current.get("queue", [])
    if not isinstance(raw, list):
        raise LeaseConflict("invalid queue")
    result: list[dict[str, str]] = []
    for entry in raw:
        if not isinstance(entry, dict) or not entry.get("reservation_id") or not entry.get("holder"):
            raise LeaseConflict("invalid queue entry")
        result.append({"reservation_id": str(entry["reservation_id"]), "holder": str(entry["holder"])})
    return result

def reserve_turn(current: dict[str, Any], *, expected_generation: int, holder: str, reservation_id: str) -> dict[str, Any]:
    _generation(current, expected_generation)
    if not holder or not reservation_id:
        raise LeaseConflict("holder and reservation_id are required")
    q = _queue(current)
    if current.get("holder") == holder or any(e["holder"] == holder or e["reservation_id"] == reservation_id for e in q):
        raise LeaseConflict("holder/reservation already active or queued")
    q.append({"reservation_id": reservation_id, "holder": holder})
    return {**current, "schema_version": "2.0.0", "generation": expected_generation + 1, "queue": q}

def cancel_reservation(current: dict[str, Any], *, expected_generation: int, holder: str, reservation_id: str) -> dict[str, Any]:
    _generation(current, expected_generation)
    q = _queue(current)
    target = {"reservation_id": reservation_id, "holder": holder}
    if target not in q:
        raise LeaseConflict("reservation not queued")
    q.remove(target)
    return {**current, "generation": expected_generation + 1, "queue": q}

def activate_next_turn(current: dict[str, Any], *, expected_generation: int, holder: str, fresh_main_sha: str) -> dict[str, Any]:
    _generation(current, expected_generation)
    if current.get("status") != "free":
        raise LeaseConflict("publication turn already held")
    if not fresh_main_sha:
        raise LeaseConflict("fresh_main_sha is required")
    q = _queue(current)
    if not q:
        raise LeaseConflict("publication queue is empty")
    first = q[0]
    if first["holder"] != holder:
        raise LeaseConflict(QUEUE_ORDER)
    return {
        **current,
        "status": "held",
        "generation": expected_generation + 1,
        "holder": holder,
        "active_reservation_id": first["reservation_id"],
        "turn_base": fresh_main_sha,
        "validated_head": None,
        "validated_base": None,
        "queue": q[1:],
    }

def bind_validated_candidate(
    current: dict[str, Any],
    *,
    expected_generation: int,
    holder: str,
    validated_head: str,
    validated_base: str,
) -> dict[str, Any]:
    _generation(current, expected_generation)
    if current.get("status") != "held" or current.get("holder") != holder:
        raise LeaseConflict("active publication turn holder mismatch")
    if not validated_head or not validated_base:
        raise LeaseConflict("validated_head and validated_base are required")
    if validated_base != current.get("turn_base"):
        raise LeaseConflict(STALE_MAIN)
    return {
        **current,
        "generation": expected_generation + 1,
        "validated_head": validated_head,
        "validated_base": validated_base,
    }

def acquire_lease(*args: Any, **kwargs: Any) -> dict[str, Any]:
    raise LeaseConflict("direct acquire is retired in schema 2; reserve_turn then activate_next_turn")

def validate_merge_authorization(
    lease: dict[str, Any],
    *,
    fresh_main_sha: str,
    pr_head_sha: str,
    holder: str,
) -> list[str]:
    errors: list[str] = []
    if lease.get("status") != "held":
        errors.append(LEASE_NOT_HELD)
    if lease.get("holder") != holder:
        errors.append(HOLDER_MISMATCH)
    if not lease.get("validated_head") or not lease.get("validated_base"):
        errors.append(VALIDATION_NOT_BOUND)
    if lease.get("validated_head") != pr_head_sha:
        errors.append(HEAD_MISMATCH)
    if lease.get("turn_base") != fresh_main_sha or lease.get("validated_base") != fresh_main_sha:
        errors.append(STALE_MAIN)
    return sorted(set(errors))

def release_lease(lease: dict[str, Any], *, holder: str, merged_sha: str) -> dict[str, Any]:
    if lease.get("status") != "held":
        raise LeaseConflict("lease is not held")
    if lease.get("holder") != holder:
        raise LeaseConflict("lease holder changed")
    if not merged_sha:
        raise LeaseConflict("verified merged_sha is required")
    generation = lease.get("generation")
    if not isinstance(generation, int):
        raise LeaseConflict("invalid lease generation")
    return {
        **lease,
        "status": "free",
        "generation": generation + 1,
        "holder": None,
        "active_reservation_id": None,
        "turn_base": None,
        "validated_head": None,
        "validated_base": None,
        "last_merge_sha": merged_sha,
    }


def recover_completed_turn(
    lease: dict[str, Any],
    *,
    expected_generation: int,
    stalled_holder: str,
    fresh_main_sha: str,
    merged_sha: str,
    recovery_location: str,
    recovery_executor: str,
) -> dict[str, Any]:
    """Release a stranded completed turn after durable merge verification.

    This transition does not grant scope or complete product work. It exists only
    so a replacement executor can preserve a recovery pointer and free FIFO
    publication capacity when the originating conversation disappears after the
    merge has already landed.
    """
    _generation(lease, expected_generation)
    if lease.get("status") != "held" or lease.get("holder") != stalled_holder:
        raise LeaseConflict("active publication turn holder mismatch")
    if not merged_sha or fresh_main_sha != merged_sha:
        raise LeaseConflict(RECOVERY_MAIN_MISMATCH)
    if not recovery_location.strip():
        raise LeaseConflict(RECOVERY_LOCATION_REQUIRED)
    if not recovery_executor.strip():
        raise LeaseConflict("recovery_executor is required")
    generation = lease.get("generation")
    if not isinstance(generation, int):
        raise LeaseConflict("invalid lease generation")
    return {
        **lease,
        "status": "free",
        "generation": generation + 1,
        "holder": None,
        "active_reservation_id": None,
        "turn_base": None,
        "validated_head": None,
        "validated_base": None,
        "last_merge_sha": merged_sha,
        "last_recovery_handoff": {
            "stalled_holder": stalled_holder,
            "merged_sha": merged_sha,
            "recovery_location": recovery_location,
            "recovery_executor": recovery_executor,
        },
    }

def yield_turn(lease: dict[str, Any], *, holder: str, reason: str) -> dict[str, Any]:
    if lease.get("status") != "held" or lease.get("holder") != holder:
        raise LeaseConflict("active publication turn holder mismatch")
    if not reason.strip():
        raise LeaseConflict("yield reason is required")
    generation = lease.get("generation")
    if not isinstance(generation, int):
        raise LeaseConflict("invalid lease generation")
    return {
        **lease,
        "status": "free",
        "generation": generation + 1,
        "holder": None,
        "active_reservation_id": None,
        "turn_base": None,
        "validated_head": None,
        "validated_base": None,
        "last_yield_reason": reason,
    }

def main() -> int:
    parser = argparse.ArgumentParser()
    sub = parser.add_subparsers(dest="command", required=True)
    validate = sub.add_parser("validate")
    validate.add_argument("lease")
    validate.add_argument("--fresh-main", required=True)
    validate.add_argument("--pr-head", required=True)
    validate.add_argument("--holder", required=True)
    args = parser.parse_args()
    if args.command == "validate":
        lease = json.loads(Path(args.lease).read_text(encoding="utf-8"))
        errors = validate_merge_authorization(
            lease, fresh_main_sha=args.fresh_main, pr_head_sha=args.pr_head, holder=args.holder
        )
        print(json.dumps({"status": "FAIL" if errors else "PASS", "errors": errors}, sort_keys=True))
        return 1 if errors else 0
    return 2

if __name__ == "__main__":
    raise SystemExit(main())
