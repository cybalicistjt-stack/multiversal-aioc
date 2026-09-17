#!/usr/bin/env python3
"""Operations V3 compare-and-swap merge lease model.

The lease is executor coordination only. It never selects work or grants product
scope. A real publisher stores the lease on a dedicated coordination branch and
advances that branch with a non-forced compare-and-swap ref update.
"""
from __future__ import annotations

import argparse
import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any

STALE_MAIN = "OPS3.STALE_MAIN"
HEAD_MISMATCH = "OPS3.HEAD_MISMATCH"
HOLDER_MISMATCH = "OPS3.HOLDER_MISMATCH"
LEASE_NOT_HELD = "OPS3.LEASE_NOT_HELD"


class LeaseConflict(RuntimeError):
    pass


def coordination_branch(target_repo: str) -> str:
    slug = target_repo.lower().replace("/", "-").replace("_", "-")
    return f"ops3-merge-lease/{slug}"


def free_lease(target_repo: str, *, generation: int = 0) -> dict[str, Any]:
    return {
        "schema_version": "1.0.0",
        "target_repo": target_repo,
        "status": "free",
        "generation": generation,
        "holder": None,
        "validated_head": None,
        "validated_base": None,
        "last_merge_sha": None,
    }


def acquire_lease(
    current: dict[str, Any],
    *,
    expected_generation: int,
    holder: str,
    validated_head: str,
    validated_base: str,
) -> dict[str, Any]:
    if current.get("status") != "free":
        raise LeaseConflict("lease already held")
    if current.get("generation") != expected_generation:
        raise LeaseConflict("lease generation changed")
    if not holder or not validated_head or not validated_base:
        raise LeaseConflict("holder, validated_head and validated_base are required")
    return {
        **current,
        "status": "held",
        "generation": expected_generation + 1,
        "holder": holder,
        "validated_head": validated_head,
        "validated_base": validated_base,
    }


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
    if lease.get("validated_head") != pr_head_sha:
        errors.append(HEAD_MISMATCH)
    if lease.get("validated_base") != fresh_main_sha:
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
        "validated_head": None,
        "validated_base": None,
        "last_merge_sha": merged_sha,
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
            lease,
            fresh_main_sha=args.fresh_main,
            pr_head_sha=args.pr_head,
            holder=args.holder,
        )
        print(json.dumps({"status": "FAIL" if errors else "PASS", "errors": errors}, sort_keys=True))
        return 1 if errors else 0
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
