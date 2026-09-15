#!/usr/bin/env python3
"""Render the two Operations V3 generated-compatibility projections.

OPS3 BACKGROUND ONLY / NO OPERATIONAL AUTHORITY

This tool is one-way: operations/CURRENT.json and its CURRENT-referenced
checkpoint are inputs. The legacy compatibility projections are outputs only.
The tool has no path that mutates CURRENT.json, selects work, or grants authority.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

CURRENT = Path("operations/CURRENT.json")
POINTER = Path("governance/ai/runtime/CURRENT_WORK_POINTER.json")
AUTHORITY = Path("governance/ai/runtime/ACTIVE_AUTHORITY_REGISTRY.json")
MANIFEST = Path("operations/GENERATED_COMPATIBILITY_PROJECTIONS.json")
ALLOWED_OUTPUTS = (POINTER, AUTHORITY)


def _load_json(path: Path) -> dict[str, Any]:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ValueError(f"expected object JSON: {path}")
    return value


def _canonical_context(root: Path) -> tuple[dict[str, Any], dict[str, Any], dict[str, Any], dict[str, Any]]:
    current = _load_json(root / CURRENT)
    lanes = current.get("lanes")
    if not isinstance(lanes, dict):
        raise ValueError("CURRENT lanes must be an object")
    product = lanes.get("product-development")
    operations = lanes.get("operations")
    if not isinstance(product, dict) or not isinstance(operations, dict):
        raise ValueError("CURRENT product-development and operations lanes must be objects")

    checkpoint_value = product.get("checkpoint_path") or product.get("legacy_checkpoint_path")
    if not isinstance(checkpoint_value, str) or not checkpoint_value:
        raise ValueError("CURRENT product-development checkpoint path is required")
    checkpoint_path = Path(checkpoint_value)
    checkpoint = _load_json(root / checkpoint_path)

    expected = {
        "work_item_id": product.get("selected_work_item"),
        "attempt_id": product.get("attempt_id"),
        "status": product.get("state"),
        "implementation_branch": product.get("implementation_branch"),
        "implementation_authority": product.get("implementation_authority"),
    }
    for key, value in expected.items():
        if checkpoint.get(key) != value:
            raise ValueError(f"CURRENT/checkpoint drift for {key}: {value!r} != {checkpoint.get(key)!r}")

    context = {
        "checkpoint_path": checkpoint_path.as_posix(),
        "freeze": current.get("product_start_freeze", {}),
    }
    return current, product, operations, {"checkpoint": checkpoint, **context}


def render_pointer(current: dict[str, Any], product: dict[str, Any], operations: dict[str, Any], context: dict[str, Any]) -> dict[str, Any]:
    checkpoint = context["checkpoint"]
    freeze = context.get("freeze") if isinstance(context.get("freeze"), dict) else {}
    blocked = bool(freeze.get("active"))
    reason = freeze.get("reason") if blocked else "Operations V3 single-door cutover completed and freeze cleared"
    work_item = product["selected_work_item"]
    return {
        "schema_version": "3.0.0-compat",
        "projection_only": True,
        "canonical_source": CURRENT.as_posix(),
        "canonical_door": current["canonical_door"],
        "rule": "Compatibility projection only. This file cannot select work or grant authority.",
        "primary_attempt_id": product["attempt_id"],
        "active_attempt": {
            "work_item_id": work_item,
            "attempt_id": product["attempt_id"],
            "track": checkpoint["track"],
            "repository": checkpoint["repository"],
            "checkpoint_path": context["checkpoint_path"],
            "status": product["state"],
            "implementation_branch": product["implementation_branch"],
            "implementation_authority": product["implementation_authority"],
            "active_item": f"{work_item} — {checkpoint['title']}",
        },
        "exclusive_control_plane_maintenance": {
            "work_item_id": operations["work_item_id"],
            "lane": "operations",
            "status": operations["state"],
            "work_item_path": operations["work_item_path"],
            "feature_starts_blocked": blocked,
            "reason": reason,
        },
        "exact_next_action": "Read operations/CURRENT.json; this projection has no independent next-action authority.",
    }


def render_authority(current: dict[str, Any], product: dict[str, Any], operations: dict[str, Any], context: dict[str, Any]) -> dict[str, Any]:
    freeze = context.get("freeze") if isinstance(context.get("freeze"), dict) else {}
    return {
        "schema_version": "3.0.0-compat",
        "projection_only": True,
        "canonical_source": CURRENT.as_posix(),
        "canonical_door": current["canonical_door"],
        "canonical_contract": current["operating_contract"],
        "canonical_lane_registry": current["lane_registry"],
        "rule": "Compatibility projection only. Operational authority is defined exclusively by Operations V3.",
        "current": [
            {"kind": "canonical_door", "lifecycle": "CURRENT", "path": current["canonical_door"]},
            {"kind": "operating_contract", "lifecycle": "CURRENT", "path": current["operating_contract"]},
            {"kind": "current_state", "lifecycle": "CURRENT", "path": CURRENT.as_posix()},
            {"kind": "lane_registry", "lifecycle": "CURRENT", "path": current["lane_registry"]},
            {"kind": "control_surface_registry", "lifecycle": "CURRENT", "path": current["control_surface_registry"]},
        ],
        "active_operations_work": {
            "work_item": operations["work_item_id"],
            "state": operations["state"],
            "implementation_authority": operations["implementation_authority"],
            "path": operations["work_item_path"],
        },
        "preserved_product_selection": {
            "work_item": product["selected_work_item"],
            "attempt_id": product["attempt_id"],
            "state": product["state"],
            "implementation_branch": product["implementation_branch"],
            "implementation_authority": product["implementation_authority"],
            "feature_starts_blocked": bool(freeze.get("active")),
            "rule": "Compatibility projection of the canonical product-development lane; this file does not independently grant authority.",
        },
    }


def render_projections(root: Path) -> dict[Path, dict[str, Any]]:
    current, product, operations, context = _canonical_context(root.resolve())
    return {
        POINTER: render_pointer(current, product, operations, context),
        AUTHORITY: render_authority(current, product, operations, context),
    }


def _serialized(value: dict[str, Any]) -> str:
    return json.dumps(value, indent=2, ensure_ascii=False) + "\n"


def check(root: Path) -> list[str]:
    errors: list[str] = []
    rendered = render_projections(root)
    for relative, expected in rendered.items():
        path = root / relative
        try:
            actual = _load_json(path)
        except (OSError, ValueError, json.JSONDecodeError) as exc:
            errors.append(f"unable to read generated compatibility projection {relative}: {exc}")
            continue
        if actual != expected:
            errors.append(f"generated compatibility projection drift: {relative}")
    return errors


def write(root: Path) -> None:
    rendered = render_projections(root)
    unexpected = set(rendered) - set(ALLOWED_OUTPUTS)
    if unexpected:
        raise RuntimeError(f"refusing unexpected projection outputs: {sorted(map(str, unexpected))}")
    for relative, value in rendered.items():
        path = root / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(_serialized(value), encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path("."))
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--check", action="store_true", help="fail if generated projections differ from canonical inputs")
    mode.add_argument("--write", action="store_true", help="rewrite only the two declared compatibility outputs")
    args = parser.parse_args()

    root = args.root.resolve()
    if args.write:
        write(root)
        return 0
    errors = check(root)
    if errors:
        for error in errors:
            print(error)
        return 1
    print("OPS3 generated compatibility projections: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
