#!/usr/bin/env python3
"""Validate the Operations V3 single-door control plane and terminal cutover state."""
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
PROJECT_MEMORY = Path("governance/project-memory/PROJECT_MEMORY.json")
LEGACY_CONTROL_MATRIX = Path("governance/ai/interaction-system/enforcement/CONTROL_COVERAGE_MATRIX.json")
MIB17_CHECKPOINT = Path("governance/ai/work-state/MIB-17-attempt-001.json")
LEGACY_EXECUTABLES = (
    Path("scripts/validate-8e009-completion-governance.py"),
    Path("scripts/_validate_repository_health_v1_6.py"),
    Path("tools/validate_stage_a_a10_projection.py"),
    Path("tools/validate_completion_claim_integrity.py"),
    Path("tools/validate_stage_a_a8_supplemental_authority.py"),
)

FORBIDDEN_ENTRYPOINT_MARKERS = (
    "CURRENT_WORK_POINTER",
    "AIOC_CURRENT_STATE",
    "execution_termination_preflight",
    "STAGE-A-A2",
    "MIB-17",
    "exact next",
)
PROJECT_MEMORY_FORBIDDEN = (
    "MULTIVERSAL_NEW_CONVERSATION_BOOTSTRAP.md",
    "CURRENT_WORK_POINTER.json",
    "CURRENT_IMPLEMENTATION_STATUS.json",
    "ROADMAP_INDEX.json",
    "STAGE-A-A2",
    ".ai/current-work-order.md",
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
    try:
        return (root / relative).read_text(encoding="utf-8")
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
    project_memory = _read_json(root, PROJECT_MEMORY, errors)
    control_matrix = _read_json(root, LEGACY_CONTROL_MATRIX, errors)
    checkpoint = _read_json(root, MIB17_CHECKPOINT, errors)

    for relative in (DOOR, CONTRACT, AIOC_AGENTS, LEGACY_BOOTSTRAP, STATIC_RESTART):
        if not (root / relative).is_file():
            errors.append(f"missing required file: {relative.as_posix()}")

    if current.get("schema_version") != "3.0.0":
        errors.append("operations/CURRENT.json schema_version must be 3.0.0")
    for key, expected in {
        "canonical_door": DOOR.as_posix(),
        "operating_contract": CONTRACT.as_posix(),
        "lane_registry": LANES.as_posix(),
        "control_surface_registry": REGISTRY.as_posix(),
    }.items():
        if current.get(key) != expected:
            errors.append(f"CURRENT {key} must equal {expected}")

    state = current.get("status")
    if state not in {"cutover_in_progress", "completed_verified"}:
        errors.append(f"unsupported OPS3 state: {state!r}")

    freeze = current.get("product_start_freeze", {})
    if not isinstance(freeze, dict):
        errors.append("product_start_freeze must be an object")
        freeze = {}
    if freeze.get("preserved_selected_work_item") != "MIB-17":
        errors.append("MIB-17 selection was not preserved through OPS3")
    if freeze.get("preserved_attempt_id") != "MIB-17-attempt-001":
        errors.append("MIB-17 attempt identity was not preserved through OPS3")
    if freeze.get("implementation_authority") is not False:
        errors.append("MIB-17 must remain without implementation authority")

    operations_lane = current.get("lanes", {}).get("operations", {})
    product_lane = current.get("lanes", {}).get("product-development", {})

    if state == "cutover_in_progress":
        if current.get("active_operations_work_item") != "OPS3-01":
            errors.append("OPS3-01 must be active while cutover is in progress")
        if freeze.get("active") is not True:
            errors.append("product_start_freeze must be active while cutover is in progress")
        if work_item.get("status") != "in_progress" or work_item.get("implementation_authority") is not True:
            errors.append("OPS3-01 must be authorized and in_progress during cutover")
        if operations_lane.get("state") != "active" or operations_lane.get("implementation_authority") is not True:
            errors.append("operations lane must be active and authorized during cutover")
        if product_lane.get("state") != "paused_for_operations_cutover" or product_lane.get("implementation_authority") is not False:
            errors.append("product-development must remain paused and unauthorized during cutover")
    elif state == "completed_verified":
        if current.get("active_operations_work_item") is not None:
            errors.append("completed OPS3 state must not retain an active operations work item")
        if freeze.get("active") is not False:
            errors.append("product_start_freeze must be cleared after OPS3 completed_verified")
        if work_item.get("status") != "completed_verified" or work_item.get("implementation_authority") is not False:
            errors.append("OPS3-01 must be completed_verified and non-authoritative after closeout")
        if operations_lane.get("state") != "completed_verified" or operations_lane.get("implementation_authority") is not False:
            errors.append("operations lane must be completed_verified and non-authoritative after closeout")
        if product_lane.get("state") != "selected_not_started":
            errors.append("product-development must return to selected_not_started after OPS3")
        if product_lane.get("selected_work_item") != "MIB-17" or product_lane.get("attempt_id") != "MIB-17-attempt-001":
            errors.append("product-development did not restore the preserved MIB-17 selection")
        if product_lane.get("implementation_authority") is not False:
            errors.append("clearing the OPS3 freeze must not itself grant MIB-17 implementation authority")

    if work_item.get("work_item_id") != "OPS3-01" or work_item.get("lane") != "operations":
        errors.append("OPS3-01 work item identity/lane mismatch")

    if lanes.get("operating_contract") != CONTRACT.as_posix():
        errors.append("all lanes must use the one canonical operating contract")
    if lanes.get("selection_rule") != "User intent selects a lane; lane state never changes the global operating contract.":
        errors.append("lane selection rule drift")
    lane_rows = lanes.get("lanes")
    if not isinstance(lane_rows, list):
        errors.append("LANES lanes must be an array")
        lane_rows = []
    lane_ids = {row.get("id") for row in lane_rows if isinstance(row, dict)}
    required_lanes = {"product-development", "operations", "content-design", "dwc-speech", "research-evaluation", "source-provenance"}
    if not required_lanes <= lane_ids:
        errors.append(f"missing required lanes: {sorted(required_lanes - lane_ids)}")

    surfaces = registry.get("surfaces")
    if not isinstance(surfaces, list):
        errors.append("control surface registry must contain surfaces array")
        surfaces = []
    surface_keys = [(row.get("system"), row.get("path")) for row in surfaces if isinstance(row, dict)]
    if len(surface_keys) != len(set(surface_keys)):
        errors.append("control surface registry contains duplicate (system, path) identifiers")
    canonical_selectors = [row for row in surfaces if isinstance(row, dict) and row.get("can_select_work") is True]
    allowed_selector_pairs = {("AIOC", "operations/BOOTSTRAP.md"), ("AIOC", "operations/CURRENT.json")}
    actual_selector_pairs = {(row.get("system"), row.get("path")) for row in canonical_selectors}
    if actual_selector_pairs != allowed_selector_pairs:
        errors.append(f"unexpected work-selecting surfaces: {sorted(actual_selector_pairs)}")

    required_registry_rows = {
        ("AIOC", PROJECT_MEMORY.as_posix(), "BACKGROUND_ONLY"),
        ("AIOC", LEGACY_CONTROL_MATRIX.as_posix(), "HISTORICAL_INERT"),
    } | {("AIOC", path.as_posix(), "HISTORICAL_INERT") for path in LEGACY_EXECUTABLES}
    actual_registry_rows = {
        (row.get("system"), row.get("path"), row.get("disposition"))
        for row in surfaces if isinstance(row, dict)
    }
    for row in sorted(required_registry_rows):
        if row not in actual_registry_rows:
            errors.append(f"control surface registry missing required disposition row: {row}")

    agents = _read_text(root, AIOC_AGENTS, errors)
    if DOOR.as_posix() not in agents:
        errors.append("AIOC AGENTS.md must redirect to operations/BOOTSTRAP.md")
    for marker in FORBIDDEN_ENTRYPOINT_MARKERS:
        if marker.lower() in agents.lower():
            errors.append(f"AIOC AGENTS.md regained independent operational marker: {marker}")

    legacy_bootstrap = _read_text(root, LEGACY_BOOTSTRAP, errors)
    if "HISTORICAL_INERT" not in legacy_bootstrap or DOOR.as_posix() not in legacy_bootstrap:
        errors.append("legacy bootstrap must be an inert redirect to OPS3")
    for marker in ("CURRENT_WORK_POINTER.json", "execution_termination_preflight.py"):
        if marker in legacy_bootstrap:
            errors.append(f"legacy bootstrap still contains executable legacy instruction: {marker}")

    expected_restart = (
        "Open cybalicistjt-stack/multiversal-aioc/operations/BOOTSTRAP.md from current main and follow it. "
        "Use no other bootstrap or behavior source."
    )
    if _read_text(root, STATIC_RESTART, errors).strip() != expected_restart:
        errors.append("static restart prompt must be the exact OPS3 single-door prompt")

    if project_memory.get("status") != "OPS3_BACKGROUND_ONLY" or project_memory.get("operational_authority") is not False:
        errors.append("PROJECT_MEMORY.json must remain background-only and non-authoritative")
    if project_memory.get("canonical_door") != DOOR.as_posix() or project_memory.get("canonical_current_state") != CURRENT.as_posix():
        errors.append("PROJECT_MEMORY.json must point only to canonical OPS3 live surfaces")
    project_memory_text = json.dumps(project_memory, sort_keys=True)
    for marker in PROJECT_MEMORY_FORBIDDEN:
        if marker in project_memory_text:
            errors.append(f"PROJECT_MEMORY.json still advertises retired live marker: {marker}")

    if control_matrix.get("ops3_disposition") != "HISTORICAL_INERT" or control_matrix.get("can_select_work") is not False:
        errors.append("legacy control coverage matrix must remain HISTORICAL_INERT")
    if control_matrix.get("canonical_door") != DOOR.as_posix():
        errors.append("legacy control coverage matrix must point to the OPS3 door")

    for relative in LEGACY_EXECUTABLES:
        text = _read_text(root, relative, errors)
        if "Operations V2" not in text or "retired" not in text.lower() or DOOR.as_posix() not in text or "SystemExit(2)" not in text:
            errors.append(f"legacy executable is not retired/fail-closed: {relative.as_posix()}")

    if legacy_pointer.get("canonical_source") != CURRENT.as_posix() or legacy_pointer.get("projection_only") is not True:
        errors.append("CURRENT_WORK_POINTER must be an explicit compatibility projection from operations/CURRENT.json")
    active = legacy_pointer.get("active_attempt", {})
    if active.get("work_item_id") != "MIB-17" or active.get("attempt_id") != "MIB-17-attempt-001":
        errors.append("legacy pointer projection lost the MIB-17 selection")
    if active.get("status") != "selected_not_started" or active.get("implementation_authority") is not False or active.get("implementation_branch") is not None:
        errors.append("legacy pointer projection must keep MIB-17 selected_not_started without authority/branch")
    maintenance = legacy_pointer.get("exclusive_control_plane_maintenance", {})
    if maintenance.get("work_item_id") != "OPS3-01":
        errors.append("legacy pointer must retain OPS3-01 maintenance provenance")
    if state == "cutover_in_progress":
        if maintenance.get("status") != "in_progress" or maintenance.get("feature_starts_blocked") is not True:
            errors.append("legacy pointer must expose active OPS3 freeze during cutover")
    elif state == "completed_verified":
        if maintenance.get("status") != "completed_verified" or maintenance.get("feature_starts_blocked") is not False:
            errors.append("legacy pointer must project completed OPS3 maintenance without blocking feature starts")

    if legacy_authority.get("canonical_source") != CURRENT.as_posix() or legacy_authority.get("projection_only") is not True:
        errors.append("ACTIVE_AUTHORITY_REGISTRY must be an explicit compatibility projection from operations/CURRENT.json")
    if legacy_authority.get("canonical_door") != DOOR.as_posix():
        errors.append("legacy authority projection must identify the OPS3 canonical door")
    authority_ops = legacy_authority.get("active_operations_work", {})
    preserved_product = legacy_authority.get("preserved_product_selection", {})
    if state == "completed_verified":
        if authority_ops.get("state") != "completed_verified" or authority_ops.get("implementation_authority") is not False:
            errors.append("legacy authority projection must show OPS3 completed and non-authoritative")
        if preserved_product.get("state") != "selected_not_started" or preserved_product.get("implementation_authority") is not False:
            errors.append("legacy authority projection must preserve unauthorized MIB-17 selection")
        if preserved_product.get("feature_starts_blocked") is not False:
            errors.append("legacy authority projection must show OPS3 freeze cleared")

    if checkpoint.get("work_item_id") != "MIB-17" or checkpoint.get("status") != "selected_not_started":
        errors.append("canonical MIB-17 checkpoint must remain selected_not_started")
    if checkpoint.get("implementation_authority") is not False or checkpoint.get("implementation_branch") is not None:
        errors.append("MIB-17 checkpoint gained implementation authority or branch during OPS3")

    observed_head = _git_head(root, errors) if expected_head else None
    if expected_head and observed_head != expected_head:
        errors.append(f"exact-head mismatch: expected {expected_head}, observed {observed_head}")

    return {
        "schema_version": "3.0.0",
        "validator": "scripts/validate_operations_v3.py",
        "status": "FAIL" if errors else "PASS",
        "ops3_state": state,
        "canonical_door": DOOR.as_posix(),
        "canonical_current_state": CURRENT.as_posix(),
        "active_operations_work_item": current.get("active_operations_work_item"),
        "product_start_freeze": freeze.get("active"),
        "preserved_product_work_item": freeze.get("preserved_selected_work_item"),
        "product_implementation_authority": product_lane.get("implementation_authority"),
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
