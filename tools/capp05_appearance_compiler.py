#!/usr/bin/env python3
"""CAPP-05 deterministic appearance compiler/reference engine.

Repository-side reference/validation tool only. It never mutates Character truth,
actual equipment, biology, renderer assets, or application runtime state.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import sys
from pathlib import Path
from typing import Any

SCHEMA_VERSION = "0.1.0"
WORK_ITEM_ID = "CAPP-05"


def canonical_bytes(value: Any) -> bytes:
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode("utf-8")


def stable_hash(value: Any) -> str:
    return hashlib.sha256(canonical_bytes(value)).hexdigest()


def _visible(asset: dict[str, Any], permissions: set[str]) -> bool:
    required = set(asset.get("permission_tags", []))
    return required.issubset(permissions)


def _matches(asset: dict[str, Any], request: dict[str, Any]) -> bool:
    def allows(field: str, value: str | None) -> bool:
        allowed = asset.get(field, [])
        return not allowed or value in allowed

    if not allows("profile_ids", request.get("profile_id")):
        return False
    if not allows("view_ids", request.get("view_id")):
        return False
    if not allows("pose_ids", request.get("pose_id")):
        return False
    if not allows("topology_template_ids", request.get("topology_template_id")):
        return False
    if not allows("fit_classes", request.get("fit_class")):
        return False
    requested_choices = set(request.get("semantic_choice_ids", []))
    asset_choices = set(asset.get("semantic_choice_ids", []))
    if asset_choices and not asset_choices.intersection(requested_choices):
        return False
    return True


def compile_render_plan(request: dict[str, Any], manifest: dict[str, Any]) -> dict[str, Any]:
    diagnostics: list[dict[str, Any]] = []
    permissions = set(request.get("permission_projection", []))
    assets = manifest.get("assets", [])
    if not isinstance(assets, list):
        raise ValueError("manifest.assets must be a list")

    eligible: list[dict[str, Any]] = []
    for asset in assets:
        if not isinstance(asset, dict):
            diagnostics.append({"code": "invalid_manifest_entry", "severity": "error"})
            continue
        if not _visible(asset, permissions):
            continue
        if _matches(asset, request):
            eligible.append(asset)

    eligible.sort(key=lambda a: (
        str(a.get("semantic_band", "")),
        int(a.get("layer_order", 0)),
        str(a.get("asset_id", "")),
        str(a.get("asset_version", "")),
    ))

    layers = []
    support_states = []
    for asset in eligible:
        support = asset.get("support_state", "unknown")
        support_states.append(support)
        layers.append({
            "asset_id": asset.get("asset_id"),
            "asset_version": asset.get("asset_version"),
            "semantic_band": asset.get("semantic_band"),
            "layer_order": int(asset.get("layer_order", 0)),
            "anchor_map": asset.get("anchor_map", {}),
            "mask_ids": sorted(asset.get("mask_ids", [])),
            "palette_zone_ids": sorted(asset.get("palette_zone_ids", [])),
            "occlusion": asset.get("occlusion", {}),
            "support_state": support,
        })

    if not eligible:
        coverage_state = "unknown"
        fallback_state = "no_authorized_asset_match"
        diagnostics.append({"code": "no_authorized_asset_match", "severity": "warning"})
    elif any(s == "unsupported" for s in support_states):
        coverage_state = "unsupported"
        fallback_state = "renderer_fallback_required"
    elif any(s in {"partial", "unknown"} for s in support_states):
        coverage_state = "partial"
        fallback_state = "partial_renderer_plan"
    else:
        coverage_state = "supported"
        fallback_state = "none"

    plan_core = {
        "schema_version": SCHEMA_VERSION,
        "work_item_id": WORK_ITEM_ID,
        "renderer_id": request.get("renderer_id"),
        "renderer_version": request.get("renderer_version"),
        "asset_pack_id": manifest.get("asset_pack_id"),
        "asset_pack_version": manifest.get("asset_pack_version"),
        "profile_id": request.get("profile_id"),
        "biology_snapshot_id": request.get("biology_snapshot_id"),
        "appearance_state_id": request.get("appearance_state_id"),
        "view_id": request.get("view_id"),
        "pose_id": request.get("pose_id"),
        "topology_template_id": request.get("topology_template_id"),
        "semantic_choice_ids": sorted(request.get("semantic_choice_ids", [])),
        "fit_class": request.get("fit_class"),
        "asset_lock": sorted(request.get("asset_lock", [])),
        "layers": layers,
        "coverage_state": coverage_state,
        "fallback_state": fallback_state,
        "diagnostics": diagnostics,
        "permission_filter_applied": True,
        "character_truth_changed": False,
        "actual_equipment_changed": False,
        "biology_changed": False,
    }
    plan_core["render_plan_sha256"] = stable_hash(plan_core)
    return plan_core


def self_test() -> None:
    manifest = {
        "asset_pack_id": "synthetic",
        "asset_pack_version": "0",
        "assets": [
            {"asset_id": "b", "asset_version": "1", "semantic_band": "body", "layer_order": 2,
             "profile_ids": ["P"], "view_ids": ["full_body_three_quarter"], "support_state": "supported"},
            {"asset_id": "a", "asset_version": "1", "semantic_band": "body", "layer_order": 1,
             "profile_ids": ["P"], "view_ids": ["full_body_three_quarter"], "support_state": "supported"},
            {"asset_id": "secret", "asset_version": "1", "semantic_band": "body", "layer_order": 0,
             "profile_ids": ["P"], "view_ids": ["full_body_three_quarter"], "support_state": "supported",
             "permission_tags": ["gm_only"]},
        ],
    }
    request = {"renderer_id": "pixel-art-v1", "renderer_version": "1", "profile_id": "P",
               "view_id": "full_body_three_quarter", "permission_projection": []}
    one = compile_render_plan(request, manifest)
    two = compile_render_plan(request, manifest)
    assert one == two
    assert [x["asset_id"] for x in one["layers"]] == ["a", "b"]
    assert one["permission_filter_applied"] is True and "hidden_asset_count" not in one
    assert one["character_truth_changed"] is False
    altered = dict(request)
    altered["view_id"] = "portrait"
    miss = compile_render_plan(altered, manifest)
    assert miss["coverage_state"] == "unknown"
    assert miss["fallback_state"] == "no_authorized_asset_match"


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--request", type=Path)
    parser.add_argument("--manifest", type=Path)
    parser.add_argument("--output", type=Path)
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args()
    if args.self_test:
        self_test()
        print("CAPP-05 self-test: PASS")
        return 0
    if not args.request or not args.manifest:
        parser.error("--request and --manifest are required unless --self-test is used")
    request = json.loads(args.request.read_text(encoding="utf-8"))
    manifest = json.loads(args.manifest.read_text(encoding="utf-8"))
    result = compile_render_plan(request, manifest)
    text = json.dumps(result, ensure_ascii=False, sort_keys=True, indent=2) + "\n"
    if args.output:
        args.output.write_text(text, encoding="utf-8")
    else:
        sys.stdout.write(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
