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
OPS3_01_WORK_ITEM = Path("operations/work-items/OPS3-01.json")
LEGACY_POINTER = Path("governance/ai/runtime/CURRENT_WORK_POINTER.json")
LEGACY_AUTHORITY = Path("governance/ai/runtime/ACTIVE_AUTHORITY_REGISTRY.json")
AIOC_AGENTS = Path("AGENTS.md")
LEGACY_BOOTSTRAP = Path("governance/ai/MULTIVERSAL_NEW_CONVERSATION_BOOTSTRAP.md")
STATIC_RESTART = Path("governance/ai/MULTIVERSAL_STATIC_RESTART_PROMPT.txt")
PROJECT_MEMORY = Path("governance/project-memory/PROJECT_MEMORY.json")
LEGACY_CONTROL_MATRIX = Path("governance/ai/interaction-system/enforcement/CONTROL_COVERAGE_MATRIX.json")
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
DEEP_LEGACY_ROUTE_MARKERS = (
    "governance/ai/MULTIVERSAL_NEW_CONVERSATION_BOOTSTRAP.md",
    "governance/ai/runtime/CURRENT_WORK_POINTER.json",
    "governance/ai/runtime/ACTIVE_AUTHORITY_REGISTRY.json",
    "governance/ai/runtime/CURRENT_IMPLEMENTATION_STATUS.json",
    "governance/ai/runtime/ROADMAP_INDEX.json",
    "governance/current-state/AIOC_CURRENT_STATE.md",
    "governance/current-state/SESSION_HANDOFF.md",
    "governance/current-state/AIOC_OPERATIONAL_HANDOFF.md",
    "governance/ai/interaction-system/OWNER_AI_INTERACTION_CONTRACT.md",
    "governance/ai/interaction-system/EXECUTION_TERMINATION_CONTRACT.json",
    "execution_transaction_preflight.py",
    "execution_termination_preflight.py",
    "execution_state_reconciler.py",
    "execution_context_guard.py",
    "execution_event_ledger.py",
    "execution_atomic_projection.py",
    "execution_terminal_auto_proof.py",
    "tools/continuity_state.py",
    "tools/interaction_pilot.py",
)
DEEP_SCAN_PREFIXES = (
    "scripts/",
    "tools/",
    ".github/",
    ".codex/",
    "bridge/",
    "operations/",
    "governance/ai/runtime/",
    "governance/project-memory/",
    "governance/ai/interaction-system/",
    "governance/application-planning/dwc-speech/",
)
DEEP_SCAN_EXACT = {
    "AGENTS.md",
    "README.md",
    "governance/application-planning/APPLICATION_IMPLEMENTATION_ROADMAP.md",
}
DEEP_SCAN_EXEMPT_EXACT = {
    "scripts/validate_operations_v3.py",
    "operations/CONTROL_SURFACE_REGISTRY.json",
    "docs/plans/2026-09-15-operations-v3-single-door.md",
}
HISTORICAL_BANNER = "OPS3 HISTORICAL REFERENCE / NO OPERATIONAL AUTHORITY"
BACKGROUND_BANNER = "OPS3 BACKGROUND ONLY / NO OPERATIONAL AUTHORITY"
TEXT_SUFFIXES = {".md", ".txt", ".json", ".py", ".sh", ".yml", ".yaml", ".toml", ".js", ".ts", ".csv"}


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
        ["git", "rev-parse", "HEAD"], cwd=root, text=True,
        stdout=subprocess.PIPE, stderr=subprocess.STDOUT, check=False,
    )
    if process.returncode:
        errors.append(f"git rev-parse HEAD failed: {process.stdout.strip()}")
        return None
    return process.stdout.strip()


def _deep_legacy_scan(root: Path, errors: list[str]) -> None:
    for path in root.rglob("*"):
        if not path.is_file() or path.suffix.lower() not in TEXT_SUFFIXES:
            continue
        relative = path.relative_to(root).as_posix()
        if relative in DEEP_SCAN_EXEMPT_EXACT:
            continue
        if not (relative.startswith(DEEP_SCAN_PREFIXES) or relative in DEEP_SCAN_EXACT):
            continue
        try:
            text = path.read_text(encoding="utf-8")
        except (OSError, UnicodeDecodeError):
            continue
        hits = [marker for marker in DEEP_LEGACY_ROUTE_MARKERS if marker.lower() in text.lower()]
        if not hits:
            continue
        if relative in {LEGACY_POINTER.as_posix(), LEGACY_AUTHORITY.as_posix()}:
            continue
        if "Operations V2" in text and "retired" in text.lower() and DOOR.as_posix() in text:
            continue
        if HISTORICAL_BANNER in text or BACKGROUND_BANNER in text:
            continue
        errors.append(f"deep legacy route contamination: {relative}: {hits}")


def _validate_product_lane_projection(
    current: dict[str, Any],
    legacy_pointer: dict[str, Any],
    legacy_authority: dict[str, Any],
    checkpoint: dict[str, Any],
    errors: list[str],
) -> None:
    lanes = current.get("lanes", {})
    product = lanes.get("product-development", {}) if isinstance(lanes, dict) else {}
    if not isinstance(product, dict):
        errors.append("CURRENT product-development lane must be an object")
        return

    work_item = product.get("selected_work_item")
    attempt_id = product.get("attempt_id")
    state = product.get("state")
    branch = product.get("implementation_branch")
    authority = product.get("implementation_authority")

    if not isinstance(work_item, str) or not work_item:
        errors.append("CURRENT product-development selected_work_item is required")
    if not isinstance(attempt_id, str) or not attempt_id:
        errors.append("CURRENT product-development attempt_id is required")
    if state not in {"selected_not_started", "in_progress", "completed_verified"}:
        errors.append(f"unsupported product-development state: {state}")
    if state == "selected_not_started" and (authority is not False or branch is not None):
        errors.append("selected_not_started product work must have no implementation authority or branch")
    if state == "in_progress" and (authority is not True or not isinstance(branch, str) or not branch):
        errors.append("in_progress product work requires implementation authority and a branch")
    if state == "completed_verified" and authority is not False:
        errors.append("completed_verified product work must retire implementation authority")

    active = legacy_pointer.get("active_attempt", {})
    if not isinstance(active, dict):
        errors.append("legacy pointer active_attempt must be an object")
        active = {}
    pointer_expected = {
        "work_item_id": work_item,
        "attempt_id": attempt_id,
        "status": state,
        "implementation_branch": branch,
        "implementation_authority": authority,
    }
    for key, expected in pointer_expected.items():
        if active.get(key) != expected:
            errors.append(f"legacy pointer projection drift for {key}: expected {expected!r}, observed {active.get(key)!r}")

    preserved = legacy_authority.get("preserved_product_selection", {})
    if not isinstance(preserved, dict):
        errors.append("legacy authority preserved_product_selection must be an object")
        preserved = {}
    authority_expected = {
        "work_item": work_item,
        "attempt_id": attempt_id,
        "state": state,
        "implementation_branch": branch,
        "implementation_authority": authority,
    }
    for key, expected in authority_expected.items():
        if preserved.get(key) != expected:
            errors.append(f"legacy authority projection drift for {key}: expected {expected!r}, observed {preserved.get(key)!r}")

    checkpoint_expected = {
        "work_item_id": work_item,
        "attempt_id": attempt_id,
        "status": state,
        "implementation_branch": branch,
        "implementation_authority": authority,
    }
    for key, expected in checkpoint_expected.items():
        if checkpoint.get(key) != expected:
            errors.append(f"product checkpoint drift for {key}: expected {expected!r}, observed {checkpoint.get(key)!r}")


def validate(root: Path, expected_head: str | None = None) -> dict[str, Any]:
    root = root.resolve()
    errors: list[str] = []
    current = _read_json(root, CURRENT, errors)
    lanes = _read_json(root, LANES, errors)
    registry = _read_json(root, REGISTRY, errors)
    ops3_01 = _read_json(root, OPS3_01_WORK_ITEM, errors)
    current_lanes = current.get("lanes", {}) if isinstance(current.get("lanes", {}), dict) else {}
    operations_lane = current_lanes.get("operations", {}) if isinstance(current_lanes, dict) else {}
    active_operations_id = current.get("active_operations_work_item")
    active_operations_path = current.get("active_operations_work_item_path")
    if active_operations_id is not None:
        if not isinstance(active_operations_path, str) or not active_operations_path:
            errors.append("active_operations_work_item_path is required while operations work is active")
            operations_work_item = {}
        else:
            operations_work_item = _read_json(root, Path(active_operations_path), errors)
    else:
        operations_work_item = ops3_01
    legacy_pointer = _read_json(root, LEGACY_POINTER, errors)
    legacy_authority = _read_json(root, LEGACY_AUTHORITY, errors)
    project_memory = _read_json(root, PROJECT_MEMORY, errors)
    control_matrix = _read_json(root, LEGACY_CONTROL_MATRIX, errors)

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

    if current.get("status") != "completed_verified":
        errors.append("OPS3 system status must remain completed_verified")
    if ops3_01.get("work_item_id") != "OPS3-01" or ops3_01.get("status") != "completed_verified":
        errors.append("OPS3-01 historical work item must remain completed_verified")
    if ops3_01.get("implementation_authority") is not False:
        errors.append("completed OPS3-01 must not retain implementation authority")

    freeze = current.get("product_start_freeze", {})
    if not isinstance(freeze, dict):
        errors.append("product_start_freeze must be an object")
        freeze = {}
    if freeze.get("implementation_authority") is not False:
        errors.append("product_start_freeze may preserve selection only; it cannot grant implementation authority")

    product_for_freeze = current_lanes.get("product-development", {}) if isinstance(current_lanes, dict) else {}
    if active_operations_id is not None:
        if not isinstance(operations_lane, dict):
            errors.append("CURRENT operations lane must be an object")
        else:
            if operations_lane.get("work_item_id") != active_operations_id:
                errors.append("active operations id must match CURRENT operations lane")
            if operations_lane.get("work_item_path") != active_operations_path:
                errors.append("active operations path must match CURRENT operations lane")
            if operations_lane.get("state") != "in_progress" or operations_lane.get("implementation_authority") is not True:
                errors.append("active operations work requires in_progress state and implementation authority")
        if operations_work_item.get("work_item_id") != active_operations_id or operations_work_item.get("status") != "in_progress":
            errors.append("CURRENT-referenced active operations work item must exist and be in_progress")
        if freeze.get("active") is not True:
            errors.append("active operations repair requires product_start_freeze.active=true")
        if isinstance(product_for_freeze, dict):
            if freeze.get("preserved_selected_work_item") != product_for_freeze.get("selected_work_item"):
                errors.append("operations freeze must preserve the CURRENT product selection")
            if freeze.get("preserved_attempt_id") != product_for_freeze.get("attempt_id"):
                errors.append("operations freeze must preserve the CURRENT product attempt")
    else:
        if current.get("active_operations_work_item_path") is not None:
            errors.append("inactive operations must not retain active_operations_work_item_path")
        if not isinstance(operations_lane, dict) or operations_lane.get("state") != "completed_verified" or operations_lane.get("implementation_authority") is not False:
            errors.append("inactive operations lane must be completed_verified with no implementation authority")
        if freeze.get("active") is not False:
            errors.append("product_start_freeze must be cleared when no operations work is active")

    if lanes.get("operating_contract") != CONTRACT.as_posix():
        errors.append("all lanes must use the one canonical operating contract")
    if lanes.get("selection_rule") != "User intent selects a lane; lane state never changes the global operating contract.":
        errors.append("lane selection rule drift")
    lane_rows = lanes.get("lanes")
    if not isinstance(lane_rows, list):
        errors.append("LANES lanes must be an array")
        lane_rows = []
    lane_ids = {row.get("id") for row in lane_rows if isinstance(row, dict)}
    required_lanes = {"product-development", "ui-implementation", "player-species", "operations", "content-design", "dwc-speech", "research-evaluation", "source-provenance"}
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
    expected_restart = "Open cybalicistjt-stack/multiversal-aioc/operations/BOOTSTRAP.md from current main and follow it. Use no other bootstrap or behavior source."
    if restart != expected_restart:
        errors.append("static restart prompt must be the exact OPS3 single-door prompt")

    if project_memory.get("status") != "OPS3_BACKGROUND_ONLY":
        errors.append("PROJECT_MEMORY.json must be background-only under OPS3")
    if project_memory.get("operational_authority") is not False:
        errors.append("PROJECT_MEMORY.json must explicitly deny operational authority")
    if project_memory.get("canonical_door") != DOOR.as_posix():
        errors.append("PROJECT_MEMORY.json must point only to the OPS3 door")
    if project_memory.get("canonical_current_state") != CURRENT.as_posix():
        errors.append("PROJECT_MEMORY.json must point to operations/CURRENT.json for live state")
    project_memory_text = json.dumps(project_memory, sort_keys=True)
    for marker in PROJECT_MEMORY_FORBIDDEN:
        if marker in project_memory_text:
            errors.append(f"PROJECT_MEMORY.json still advertises retired live marker: {marker}")

    if control_matrix.get("ops3_disposition") != "HISTORICAL_INERT":
        errors.append("legacy control coverage matrix must be explicitly HISTORICAL_INERT")
    if control_matrix.get("canonical_door") != DOOR.as_posix():
        errors.append("legacy control coverage matrix must point to the OPS3 door")
    if control_matrix.get("can_select_work") is not False:
        errors.append("legacy control coverage matrix must not select work")

    for relative in LEGACY_EXECUTABLES:
        text = _read_text(root, relative, errors)
        if "Operations V2" not in text or "retired" not in text.lower():
            errors.append(f"legacy executable is not explicitly retired: {relative.as_posix()}")
        if DOOR.as_posix() not in text:
            errors.append(f"legacy executable does not redirect to OPS3: {relative.as_posix()}")
        if "SystemExit(2)" not in text:
            errors.append(f"legacy executable does not fail closed: {relative.as_posix()}")

    _deep_legacy_scan(root, errors)

    if legacy_pointer.get("canonical_source") != CURRENT.as_posix() or legacy_pointer.get("projection_only") is not True:
        errors.append("CURRENT_WORK_POINTER must be an explicit compatibility projection from operations/CURRENT.json")
    maintenance = legacy_pointer.get("exclusive_control_plane_maintenance", {})
    if maintenance.get("work_item_id") != operations_lane.get("work_item_id"):
        errors.append("legacy pointer operations work-item drift")
    if maintenance.get("status") != operations_lane.get("state"):
        errors.append("legacy pointer operations status drift")
    if maintenance.get("work_item_path") != operations_lane.get("work_item_path"):
        errors.append("legacy pointer operations path drift")
    if maintenance.get("feature_starts_blocked") is not bool(freeze.get("active")):
        errors.append("legacy pointer freeze projection drift")

    if legacy_authority.get("canonical_source") != CURRENT.as_posix() or legacy_authority.get("projection_only") is not True:
        errors.append("ACTIVE_AUTHORITY_REGISTRY must be an explicit compatibility projection from operations/CURRENT.json")
    if legacy_authority.get("canonical_door") != DOOR.as_posix():
        errors.append("legacy authority projection must identify the OPS3 canonical door")
    active_operations = legacy_authority.get("active_operations_work", {})
    if active_operations.get("work_item") != operations_lane.get("work_item_id"):
        errors.append("legacy authority operations work-item drift")
    if active_operations.get("state") != operations_lane.get("state"):
        errors.append("legacy authority operations state drift")
    if active_operations.get("implementation_authority") is not operations_lane.get("implementation_authority"):
        errors.append("legacy authority operations authority drift")
    if active_operations.get("path") != operations_lane.get("work_item_path"):
        errors.append("legacy authority operations path drift")

    product_lanes = current.get("lanes", {})
    product = product_lanes.get("product-development", {}) if isinstance(product_lanes, dict) else {}
    checkpoint_path_value = product.get("checkpoint_path") or product.get("legacy_checkpoint_path") if isinstance(product, dict) else None
    if not isinstance(checkpoint_path_value, str) or not checkpoint_path_value:
        errors.append("CURRENT product-development checkpoint path is required")
        checkpoint = {}
    else:
        checkpoint = _read_json(root, Path(checkpoint_path_value), errors)
    _validate_product_lane_projection(current, legacy_pointer, legacy_authority, checkpoint, errors)

    ui_lane = product_lanes.get("ui-implementation", {}) if isinstance(product_lanes, dict) else {}
    if not isinstance(ui_lane, dict):
        errors.append("CURRENT ui-implementation lane must be an object")
    else:
        ui_state = ui_lane.get("state")
        if ui_state not in {"selected_not_started", "in_progress", "completed_verified"}:
            errors.append(f"invalid ui-implementation state: {ui_state!r}")
        ui_checkpoint_value = ui_lane.get("checkpoint_path") or ui_lane.get("legacy_checkpoint_path")
        if not isinstance(ui_checkpoint_value, str) or not ui_checkpoint_value:
            errors.append("CURRENT ui-implementation checkpoint path is required")
        else:
            ui_checkpoint = _read_json(root, Path(ui_checkpoint_value), errors)
            expected_ui = {
                "work_item_id": ui_lane.get("selected_work_item"),
                "attempt_id": ui_lane.get("attempt_id"),
                "status": ui_state,
                "implementation_branch": ui_lane.get("implementation_branch"),
                "implementation_authority": ui_lane.get("implementation_authority"),
            }
            for key, value in expected_ui.items():
                if ui_checkpoint.get(key) != value:
                    errors.append(f"CURRENT/ui checkpoint drift for {key}: {value!r} != {ui_checkpoint.get(key)!r}")
        if ui_state == "in_progress":
            if not ui_lane.get("implementation_branch") or ui_lane.get("implementation_authority") is not True:
                errors.append("in_progress ui-implementation lane requires branch and implementation authority")

    mvps_lane = product_lanes.get("player-species", {}) if isinstance(product_lanes, dict) else {}
    if not isinstance(mvps_lane, dict):
        errors.append("CURRENT player-species lane must be an object")
    else:
        mvps_state = mvps_lane.get("state")
        if mvps_state not in {"selected_not_started", "in_progress", "completed_verified"}:
            errors.append(f"invalid player-species state: {mvps_state!r}")
        mvps_checkpoint_value = mvps_lane.get("checkpoint_path") or mvps_lane.get("legacy_checkpoint_path")
        if not isinstance(mvps_checkpoint_value, str) or not mvps_checkpoint_value:
            errors.append("CURRENT player-species checkpoint path is required")
        else:
            mvps_checkpoint = _read_json(root, Path(mvps_checkpoint_value), errors)
            expected_mvps = {
                "work_item_id": mvps_lane.get("selected_work_item"),
                "attempt_id": mvps_lane.get("attempt_id"),
                "status": mvps_state,
                "implementation_branch": mvps_lane.get("implementation_branch"),
                "implementation_authority": mvps_lane.get("implementation_authority"),
            }
            for key, value in expected_mvps.items():
                if mvps_checkpoint.get(key) != value:
                    errors.append(f"CURRENT/MVPS checkpoint drift for {key}: {value!r} != {mvps_checkpoint.get(key)!r}")
        if mvps_state == "selected_not_started":
            if mvps_lane.get("implementation_branch") is not None or mvps_lane.get("implementation_authority") is not False:
                errors.append("selected_not_started player-species lane must have no branch or implementation authority")
        if mvps_state == "in_progress":
            if not mvps_lane.get("implementation_branch") or mvps_lane.get("implementation_authority") is not True:
                errors.append("in_progress player-species lane requires branch and implementation authority")
        if mvps_state == "completed_verified" and mvps_lane.get("implementation_authority") is not False:
            errors.append("completed_verified player-species work must retire implementation authority")

    observed_head = _git_head(root, errors) if expected_head else None
    if expected_head and observed_head != expected_head:
        errors.append(f"exact-head mismatch: expected {expected_head}, observed {observed_head}")

    return {
        "schema_version": "3.2.0",
        "validator": "scripts/validate_operations_v3.py",
        "status": "FAIL" if errors else "PASS",
        "canonical_door": DOOR.as_posix(),
        "canonical_current_state": CURRENT.as_posix(),
        "active_operations_work_item": current.get("active_operations_work_item"),
        "product_start_freeze": bool(freeze.get("active")) if isinstance(freeze, dict) else None,
        "preserved_product_work_item": freeze.get("preserved_selected_work_item") if isinstance(freeze, dict) else None,
        "deep_legacy_route_scan": True,
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
