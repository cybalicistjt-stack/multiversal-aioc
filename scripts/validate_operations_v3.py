#!/usr/bin/env python3
"""Validate the Operations V3 single-door control plane."""
from __future__ import annotations

import argparse
import json
import subprocess
from pathlib import Path
from typing import Any

DOOR = Path("operations/BOOTSTRAP.md")
CONTRACT = Path("operations/OPERATING_CONTRACT.md")
CURRENT = Path("operations/CURRENT.json")
LANES = Path("operations/LANES.json")
REGISTRY = Path("operations/CONTROL_SURFACE_REGISTRY.json")
OPS_WORK_ITEM = Path("operations/work-items/OPS3-01.json")
LEGACY_POINTER = Path("governance/ai/runtime/CURRENT_WORK_POINTER.json")
LEGACY_AUTHORITY = Path("governance/ai/runtime/ACTIVE_AUTHORITY_REGISTRY.json")
AIOC_AGENTS = Path("AGENTS.md")
LEGACY_BOOTSTRAP = Path("governance/ai/MULTIVERSAL_NEW_CONVERSATION_BOOTSTRAP.md")
STATIC_RESTART = Path("governance/ai/MULTIVERSAL_STATIC_RESTART_PROMPT.txt")

FORBIDDEN_ENTRYPOINT_MARKERS = (
    "CURRENT_WORK_POINTER",
    "AIOC_CURRENT_STATE",
    "execution_termination_preflight",
    "STAGE-A-A2",
    "MIB-17",
    "exact next",
)


def _read_json(root: Path, relative: Path, errors: list[str]) -> dict[str, Any]:
    path = root / relative
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError:
        errors.append(f"missing required JSON: {relative.as_posix()}")
        return {}
    except json.JSONDecodeError as exc:
        errors.append(f"invalid JSON {relative.as_posix()}: {exc}")
        return {}
    if not isinstance(value, dict):
        errors.append(f"expected object JSON: {relative.as_posix()}")
        return {}
    return value


def _read_text(root: Path, relative: Path, errors: list[str]) -> str:
    path = root / relative
    try:
        return path.read_text(encoding="utf-8")
    except OSError as exc:
        errors.append(f"unable to read {relative.as_posix()}: {exc}")
        return ""


def _git_head(root: Path, errors: list[str]) -> str | None:
    process = subprocess.run(
        ["git", "rev-parse", "HEAD"],
        cwd=root,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        check=False,
    )
    if process.returncode:
        errors.append(f"git rev-parse HEAD failed: {process.stdout.strip()}")
        return None
    return process.stdout.strip()


def validate(root: Path, expected_head: str | None = None) -> dict[str, Any]:
    root = root.resolve()
    errors: list[str] = []

    current = _read_json(root, CURRENT, errors)
    lanes = _read_json(root, LANES, errors)
    registry = _read_json(root, REGISTRY, errors)
    work_item = _read_json(root, OPS_WORK_ITEM, errors)
    legacy_pointer = _read_json(root, LEGACY_POINTER, errors)
    legacy_authority = _read_json(root, LEGACY_AUTHORITY, errors)

    for relative in (DOOR, CONTRACT, AIOC_AGENTS, LEGACY_BOOTSTRAP, STATIC_RESTART):
        if not (root / relative).is_file():
            errors.append(f"missing required file: {relative.as_posix()}")

    if current.get("schema_version") != "3.0.0":
        errors.append("operations/CURRENT.json schema_version must be 3.0.0")
    expected_refs = {
        "canonical_door": DOOR.as_posix(),
        "operating_contract": CONTRACT.as_posix(),
        "lane_registry": LANES.as_posix(),
        "control_surface_registry": REGISTRY.as_posix(),
    }
    for key, expected in expected_refs.items():
        if current.get(key) != expected:
            errors.append(f"CURRENT {key} must equal {expected}")

    if current.get("active_operations_work_item") != "OPS3-01":
        errors.append("OPS3-01 must be the active operations work item during cutover")
    freeze = current.get("product_start_freeze", {})
    if not isinstance(freeze, dict) or freeze.get("active") is not True:
        errors.append("product_start_freeze must remain active during OPS3 cutover")
    if freeze.get("preserved_selected_work_item") != "MIB-17":
        errors.append("MIB-17 selection was not preserved through the operations freeze")
    if freeze.get("implementation_authority") is not False:
        errors.append("MIB-17 must remain without implementation authority")

    if work_item.get("work_item_id") != "OPS3-01" or work_item.get("status") != "in_progress":
        errors.append("OPS3-01 work item must exist and remain in_progress until cutover closes")
    if work_item.get("lane") != "operations" or work_item.get("implementation_authority") is not True:
        errors.append("OPS3-01 must be an authorized operations-lane work item")

    if lanes.get("operating_contract") != CONTRACT.as_posix():
        errors.append("all lanes must use the one canonical operating contract")
    if lanes.get("selection_rule") != "User intent selects a lane; lane state never changes the global operating contract.":
        errors.append("lane selection rule drift")
    lane_rows = lanes.get("lanes")
    if not isinstance(lane_rows, list):
        errors.append("LANES lanes must be an array")
        lane_rows = []
    lane_ids = {row.get("id") for row in lane_rows if isinstance(row, dict)}
    required_lanes = {
        "product-development",
        "operations",
        "content-design",
        "dwc-speech",
        "research-evaluation",
        "source-provenance",
    }
    if not required_lanes <= lane_ids:
        errors.append(f"missing required lanes: {sorted(required_lanes - lane_ids)}")

    surfaces = registry.get("surfaces")
    if not isinstance(surfaces, list):
        errors.append("control surface registry must contain surfaces array")
        surfaces = []
    surface_keys = [
        (row.get("system"), row.get("path"))
        for row in surfaces
        if isinstance(row, dict)
    ]
    if len(surface_keys) != len(set(surface_keys)):
        errors.append("control surface registry contains duplicate (system, path) identifiers")
    canonical_selectors = [
        row for row in surfaces
        if isinstance(row, dict) and row.get("can_select_work") is True
    ]
    allowed_selector_pairs = {
        ("AIOC", "operations/BOOTSTRAP.md"),
        ("AIOC", "operations/CURRENT.json"),
    }
    actual_selector_pairs = {(row.get("system"), row.get("path")) for row in canonical_selectors}
    if actual_selector_pairs != allowed_selector_pairs:
        errors.append(f"unexpected work-selecting surfaces: {sorted(actual_selector_pairs)}")

    agents = _read_text(root, AIOC_AGENTS, errors)
    if DOOR.as_posix() not in agents:
        errors.append("AIOC AGENTS.md must redirect to operations/BOOTSTRAP.md")
    agents_lower = agents.lower()
    for marker in FORBIDDEN_ENTRYPOINT_MARKERS:
        if marker.lower() in agents_lower:
            errors.append(f"AIOC AGENTS.md regained independent operational marker: {marker}")

    legacy_bootstrap = _read_text(root, LEGACY_BOOTSTRAP, errors)
    if "HISTORICAL_INERT" not in legacy_bootstrap or DOOR.as_posix() not in legacy_bootstrap:
        errors.append("legacy bootstrap must be an inert redirect to OPS3")
    for marker in ("CURRENT_WORK_POINTER.json", "execution_termination_preflight.py"):
        if marker in legacy_bootstrap:
            errors.append(f"legacy bootstrap still contains executable legacy instruction: {marker}")

    restart = _read_text(root, STATIC_RESTART, errors).strip()
    expected_restart = (
        "Open cybalicistjt-stack/multiversal-aioc/operations/BOOTSTRAP.md from current main and follow it. "
        "Use no other bootstrap or behavior source."
    )
    if restart != expected_restart:
        errors.append("static restart prompt must be the exact OPS3 single-door prompt")

    if legacy_pointer.get("canonical_source") != CURRENT.as_posix() or legacy_pointer.get("projection_only") is not True:
        errors.append("CURRENT_WORK_POINTER must be an explicit compatibility projection from operations/CURRENT.json")
    active = legacy_pointer.get("active_attempt", {})
    if active.get("work_item_id") != "MIB-17" or active.get("implementation_authority") is not False:
        errors.append("legacy pointer projection must preserve MIB-17 as unauthorized selected work")
    maintenance = legacy_pointer.get("exclusive_control_plane_maintenance", {})
    if maintenance.get("work_item_id") != "OPS3-01" or maintenance.get("feature_starts_blocked") is not True:
        errors.append("legacy pointer projection must expose the OPS3 product-start freeze")

    if legacy_authority.get("canonical_source") != CURRENT.as_posix() or legacy_authority.get("projection_only") is not True:
        errors.append("ACTIVE_AUTHORITY_REGISTRY must be an explicit compatibility projection from operations/CURRENT.json")
    if legacy_authority.get("canonical_door") != DOOR.as_posix():
        errors.append("legacy authority projection must identify the OPS3 canonical door")

    checkpoint = _read_json(root, Path("governance/ai/work-state/MIB-17-attempt-001.json"), errors)
    if checkpoint.get("work_item_id") != "MIB-17" or checkpoint.get("status") != "selected_not_started":
        errors.append("canonical historical MIB-17 checkpoint must remain selected_not_started during OPS3")
    if checkpoint.get("implementation_authority") is not False or checkpoint.get("implementation_branch") is not None:
        errors.append("MIB-17 checkpoint gained implementation authority during OPS3 freeze")

    observed_head = _git_head(root, errors) if expected_head else None
    if expected_head and observed_head != expected_head:
        errors.append(f"exact-head mismatch: expected {expected_head}, observed {observed_head}")

    return {
        "schema_version": "3.0.0",
        "validator": "scripts/validate_operations_v3.py",
        "status": "FAIL" if errors else "PASS",
        "canonical_door": DOOR.as_posix(),
        "canonical_current_state": CURRENT.as_posix(),
        "active_operations_work_item": current.get("active_operations_work_item"),
        "product_start_freeze": bool(freeze.get("active")) if isinstance(freeze, dict) else None,
        "preserved_product_work_item": freeze.get("preserved_selected_work_item") if isinstance(freeze, dict) else None,
        "observed_head": observed_head,
        "errors": errors,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", default=".")
    parser.add_argument("--expected-head")
    parser.add_argument("--output")
    args = parser.parse_args()
    result = validate(Path(args.root), args.expected_head)
    payload = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.output:
        Path(args.output).write_text(payload, encoding="utf-8")
    print(payload, end="")
    return 1 if result["errors"] else 0


if __name__ == "__main__":
    raise SystemExit(main())
