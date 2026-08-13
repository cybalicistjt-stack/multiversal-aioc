#!/usr/bin/env python3
"""CAPP-09 deterministic appearance migration reference engine.

The engine classifies and transforms portable appearance state only when the
migration map explicitly authorizes the transformation. Missing/removed values
are never silently substituted.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import sys
from pathlib import Path
from typing import Any

SCHEMA_VERSION = "0.1.0"


def canonical(value: Any) -> bytes:
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode("utf-8")


def digest(value: Any) -> str:
    return hashlib.sha256(canonical(value)).hexdigest()


def migrate(payload: dict[str, Any], migration: dict[str, Any]) -> dict[str, Any]:
    option_map = migration.get("option_id_map", {})
    removed = set(migration.get("removed_option_ids", []))
    valid_target_ids = set(migration.get("valid_target_option_ids", []))
    choices = payload.get("authored_choices", {})
    locks = payload.get("locks", [])

    migrated: dict[str, Any] = {}
    review: list[dict[str, Any]] = []
    exact = 0
    mapped = 0

    for old_id in sorted(choices):
        value = choices[old_id]
        if old_id in option_map:
            new_id = option_map[old_id]
            migrated[new_id] = value
            mapped += 1
            continue
        if old_id in removed:
            review.append({"code": "removed_option", "old_id": old_id, "value": value})
            continue
        if not valid_target_ids or old_id in valid_target_ids:
            migrated[old_id] = value
            exact += 1
        else:
            review.append({"code": "unknown_target_option", "old_id": old_id, "value": value})

    migrated_locks = []
    for lock_id in sorted(set(locks)):
        if lock_id in option_map:
            migrated_locks.append(option_map[lock_id])
        elif lock_id in removed:
            review.append({"code": "removed_lock", "old_id": lock_id})
        elif not valid_target_ids or lock_id in valid_target_ids:
            migrated_locks.append(lock_id)
        else:
            review.append({"code": "unknown_target_lock", "old_id": lock_id})

    source_pack = payload.get("asset_pack_version")
    target_pack = migration.get("target_asset_pack_version", source_pack)
    source_renderer = payload.get("renderer_version")
    target_renderer = migration.get("target_renderer_version", source_renderer)

    if migration.get("asset_pack_available") is False:
        review.append({"code": "missing_asset_pack", "source": source_pack, "target": target_pack})
    if migration.get("renderer_supported") is False:
        review.append({"code": "renderer_capability_changed", "source": source_renderer, "target": target_renderer})

    if review:
        classification = "review_required"
    elif mapped:
        classification = "recoverable_mapped"
    else:
        classification = "recoverable_exact"

    result = {
        "schema_version": SCHEMA_VERSION,
        "work_item_id": "CAPP-09",
        "classification": classification,
        "source_schema_version": payload.get("schema_version"),
        "target_schema_version": migration.get("target_schema_version", payload.get("schema_version")),
        "source_profile_id": payload.get("source_profile_id"),
        "authored_choices": dict(sorted(migrated.items())),
        "locks": sorted(set(migrated_locks)),
        "asset_pack_version": target_pack,
        "renderer_version": target_renderer,
        "exact_choice_count": exact,
        "mapped_choice_count": mapped,
        "review_items": review,
        "silent_substitution": False,
        "character_truth_changed": False,
        "biology_changed": False,
        "equipment_changed": False,
    }
    result["migration_sha256"] = digest(result)
    return result


def self_test() -> None:
    payload = {
        "schema_version": "0.1.0",
        "source_profile_id": "P",
        "authored_choices": {"A": "x", "B": "y", "C": "z"},
        "locks": ["A", "B"],
        "asset_pack_version": "1",
        "renderer_version": "1",
    }
    migration = {
        "target_schema_version": "0.2.0",
        "option_id_map": {"A": "A2"},
        "removed_option_ids": ["B"],
        "valid_target_option_ids": ["A2", "C"],
        "target_asset_pack_version": "2",
        "target_renderer_version": "2",
        "asset_pack_available": True,
        "renderer_supported": True,
    }
    one = migrate(payload, migration)
    two = migrate(payload, migration)
    assert one == two
    assert one["classification"] == "review_required"
    assert one["authored_choices"] == {"A2": "x", "C": "z"}
    assert one["silent_substitution"] is False
    clean = dict(payload)
    clean["authored_choices"] = {"C": "z"}
    clean["locks"] = []
    exact = migrate(clean, {"valid_target_option_ids": ["C"]})
    assert exact["classification"] == "recoverable_exact"


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--payload", type=Path)
    parser.add_argument("--migration", type=Path)
    parser.add_argument("--output", type=Path)
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args()
    if args.self_test:
        self_test()
        print("CAPP-09 self-test: PASS")
        return 0
    if not args.payload or not args.migration:
        parser.error("--payload and --migration are required unless --self-test is used")
    payload = json.loads(args.payload.read_text(encoding="utf-8"))
    migration_map = json.loads(args.migration.read_text(encoding="utf-8"))
    result = migrate(payload, migration_map)
    text = json.dumps(result, ensure_ascii=False, sort_keys=True, indent=2) + "\n"
    if args.output:
        args.output.write_text(text, encoding="utf-8")
    else:
        sys.stdout.write(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
