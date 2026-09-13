#!/usr/bin/env python3
"""Plan an atomic multi-file execution projection using Git object primitives.

The planner is intentionally side-effect free. The caller materializes each path as a
blob, creates one tree from one validated base tree, creates one commit, and moves one
ref. This keeps start/closeout projections from becoming transiently inconsistent and
removes per-tranche workflow plumbing from the critical path.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any


class AtomicProjectionError(ValueError):
    pass


def _require(condition: bool, message: str) -> None:
    if not condition:
        raise AtomicProjectionError(message)


def _sha40(value: Any) -> bool:
    return (
        isinstance(value, str)
        and len(value) == 40
        and all(ch in "0123456789abcdef" for ch in value)
    )


def build_projection_plan(record: dict[str, Any]) -> dict[str, Any]:
    operation_id = record.get("operation_id")
    idempotency_key = record.get("idempotency_key")
    base_sha = record.get("base_sha")
    branch = record.get("branch")
    paths = record.get("paths")

    _require(isinstance(operation_id, str) and bool(operation_id.strip()), "operation_id is required")
    _require(isinstance(idempotency_key, str) and bool(idempotency_key.strip()), "idempotency_key is required")
    _require(_sha40(base_sha), "base_sha must be a lowercase 40-character commit SHA")
    _require(isinstance(branch, str) and bool(branch.strip()), "branch is required")
    _require(isinstance(paths, list) and bool(paths), "paths must be a non-empty array")
    _require(all(isinstance(path, str) and path.strip() for path in paths), "paths must contain non-empty strings")

    normalized_paths = sorted(set(paths))
    _require(len(normalized_paths) == len(paths), "paths must be unique")
    if record.get("temporary_workflow_projection") is True:
        _require(
            not any(path.startswith(".github/workflows/") for path in normalized_paths),
            "temporary per-tranche workflow projections are prohibited when direct Git-object mutation is available",
        )

    material = {
        "operation_id": operation_id,
        "idempotency_key": idempotency_key,
        "base_sha": base_sha,
        "branch": branch,
        "paths": normalized_paths,
        "mutation_sequence": ["create_blob", "create_tree", "create_commit", "update_ref"],
    }
    digest = hashlib.sha256(
        json.dumps(material, sort_keys=True, separators=(",", ":"), ensure_ascii=True).encode("utf-8")
    ).hexdigest()
    return {
        "schema_version": "1.0.0",
        "decision": "ATOMIC_GIT_OBJECT_PROJECTION",
        **material,
        "projection_digest_sha256": digest,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--manifest", required=True)
    parser.add_argument("--output")
    args = parser.parse_args()
    record = json.loads(Path(args.manifest).read_text(encoding="utf-8"))
    result = build_projection_plan(record)
    payload = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.output:
        Path(args.output).write_text(payload, encoding="utf-8")
    print(payload, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
