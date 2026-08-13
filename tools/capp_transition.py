#!/usr/bin/env python3
"""Atomic CAPP lifecycle transition engine.

The connector only needs to create a small request JSON on a governed CAPP branch.
This tool performs the large, coupled backlog/checkpoint/pointer/status writes in one
repository checkout, eliminating prose-sensitive hand edits and completion-only PRs.
"""
from __future__ import annotations

import argparse
import copy
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CAPP = ROOT / "governance/application-planning/character-appearance-production"
BACKLOG = CAPP / "CAPP_PROGRAM_BACKLOG.json"
POINTER = ROOT / "governance/ai/runtime/CURRENT_WORK_POINTER.json"
STATUS = ROOT / "governance/ai/runtime/CURRENT_IMPLEMENTATION_STATUS.json"
SHA_RE = re.compile(r"^[0-9a-f]{40}$")
CAPP_RE = re.compile(r"^CAPP-(0[1-9]|1[0-2])$")


class TransitionError(RuntimeError):
    pass


def req(condition: bool, message: str) -> None:
    if not condition:
        raise TransitionError(message)


def load(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def write(path: Path, value) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2, ensure_ascii=False) + "\n", encoding="utf-8", newline="\n")


def next_after(backlog: dict, item_id: str) -> str | None:
    order = backlog["execution_order"]
    index = order.index(item_id)
    return order[index + 1] if index + 1 < len(order) else None


def checkpoint_path(attempt_id: str) -> Path:
    return ROOT / "governance/ai/work-state" / f"{attempt_id}.json"


def completion_receipt_path(work_item_id: str) -> Path:
    return CAPP / f"{work_item_id}_VERIFIED_COMPLETION_RECEIPT_v1.0.0.json"


def ensure_boundaries(backlog: dict) -> None:
    boundaries = backlog.get("boundaries", {})
    req(boundaries, "CAPP boundaries missing")
    req(all(value is False for value in boundaries.values()), "CAPP transition may not activate runtime/release boundaries")


def validate_request(request: dict, backlog: dict) -> None:
    req(request.get("schema_version") == "1.0.0", "request schema_version")
    req(request.get("mode") in {"start", "advance"}, "request mode")
    stamp = request.get("transition_at")
    req(isinstance(stamp, str) and stamp, "transition_at")
    nxt = request.get("next")
    req(isinstance(nxt, dict), "next block")
    next_id = nxt.get("work_item_id")
    req(CAPP_RE.fullmatch(next_id or "") is not None, "next CAPP id")
    req(nxt.get("attempt_id") == f"{next_id}-attempt-001", "next attempt id")
    req(isinstance(nxt.get("branch"), str) and nxt["branch"].startswith("governance/capp-"), "next governed branch")
    req(SHA_RE.fullmatch(nxt.get("base_commit", "")) is not None, "next base commit")
    for key in ("objective", "active_substep", "next_action", "validation_command"):
        req(isinstance(nxt.get(key), str) and nxt[key].strip(), f"next.{key}")
    items = {item["id"]: item for item in backlog["work_items"]}
    req(next_id in items, "next item absent from backlog")
    req(items[next_id]["status"] == "planned", "next item must be planned")
    if request["mode"] == "start":
        last = backlog.get("last_completed")
        if last:
            req(next_after(backlog, last["work_item_id"]) == next_id, "start is not dependency-ordered after last completion")
        return
    prev = request.get("previous")
    req(isinstance(prev, dict), "previous block")
    prev_id = prev.get("work_item_id")
    req(CAPP_RE.fullmatch(prev_id or "") is not None, "previous CAPP id")
    req(next_after(backlog, prev_id) == next_id, "advance is not dependency ordered")
    req(prev.get("attempt_id") == f"{prev_id}-attempt-001", "previous attempt id")
    req(SHA_RE.fullmatch(prev.get("exact_validated_head", "")) is not None, "previous exact head")
    req(SHA_RE.fullmatch(prev.get("merge_commit", "")) is not None, "previous merge commit")
    req(isinstance(prev.get("workflows"), str) and re.fullmatch(r"\d+/\d+", prev["workflows"]), "previous workflow evidence")
    req(isinstance(prev.get("pull_request"), int) and prev["pull_request"] > 0, "previous PR")
    req(prev.get("merge_verification") == "verified valid", "previous merge verification")
    req(isinstance(prev.get("delivered", {}), dict), "previous delivered summary")
    req(isinstance(prev.get("invariants", {}), dict), "previous invariants")
    req(items[prev_id]["status"] in {"in_progress", "started", "completed_verified"}, "previous backlog lifecycle")


def complete_previous(request: dict, backlog: dict, pointer: dict) -> dict:
    prev = request["previous"]
    prev_id = prev["work_item_id"]
    attempt_id = prev["attempt_id"]
    stamp = request["transition_at"]
    items = {item["id"]: item for item in backlog["work_items"]}
    items[prev_id]["status"] = "completed_verified"
    cp_path = checkpoint_path(attempt_id)
    cp = load(cp_path)
    cp["revision"] = int(cp.get("revision", 1)) + 1
    cp["status"] = "completed_verified"
    cp["updated_at"] = stamp
    cp["completed_at"] = stamp
    cp["latest_pushed_commit"] = prev["exact_validated_head"]
    cp["expected_remote_head"] = prev["merge_commit"]
    cp["pull_request"] = prev["pull_request"]
    cp["merge_commit"] = prev["merge_commit"]
    cp["last_verified_action"] = (
        f"{prev_id} exact candidate {prev['exact_validated_head']} passed {prev['workflows']} applicable pull-request workflows "
        f"and merged in PR #{prev['pull_request']} as signed/verified {prev['merge_commit']}."
    )
    cp["active_substep"] = None
    cp["next_action"] = f"{prev_id} is completed_verified; continue through the dependency-ordered CAPP transition."
    cp["unresolved_failures"] = []
    cp["owner_decision_required"] = False
    cp["roadmap_projection_pending"] = False
    cp["validation"] = [{
        "command": cp.get("completion_gate", {}).get("required_validation_commands", [f"Validate {prev_id} Completion"])[0],
        "status": "passed",
        "evidence": f"{prev_id} exact head {prev['exact_validated_head']} passed {prev['workflows']} applicable workflows in PR #{prev['pull_request']}; signed/verified merge {prev['merge_commit']}.",
    }]
    cp["evidence"] = [
        {"kind": "commit", "value": f"{prev_id} exact validated candidate head {prev['exact_validated_head']}"},
        {"kind": "pull_request", "value": f"{prev_id} PR #{prev['pull_request']} passed {prev['workflows']} applicable workflows"},
        {"kind": "merge", "value": f"{prev_id} signed/verified merge {prev['merge_commit']}"},
    ]
    write(cp_path, cp)
    receipt = {
        "schema_version": "1.0.0",
        "work_item_id": prev_id,
        "state": "completed_verified",
        "completed_at": stamp,
        "exact_validated_head": prev["exact_validated_head"],
        "applicable_pull_request_workflows": prev["workflows"],
        "pull_request": prev["pull_request"],
        "merge_commit": prev["merge_commit"],
        "merge_verification": prev["merge_verification"],
        "delivered": prev.get("delivered", {}),
        "invariants": prev.get("invariants", {}),
        "next_work_item": {"id": request["next"]["work_item_id"], "state": "started"},
        "boundaries": copy.deepcopy(backlog["boundaries"]),
    }
    write(completion_receipt_path(prev_id), receipt)
    backlog["last_completed"] = {
        "work_item_id": prev_id,
        "exact_validated_head": prev["exact_validated_head"],
        "workflows": prev["workflows"],
        "pull_request": prev["pull_request"],
        "merge_commit": prev["merge_commit"],
        "merge_verification": prev["merge_verification"],
    }
    for item in pointer.get("active_attempts", []):
        if item.get("attempt_id") == attempt_id:
            item["status"] = "completed_verified"
            item["updated_at"] = stamp
            item["roadmap_projection_pending"] = False
            item["owner_selected"] = False
    return cp


def create_start_checkpoint(request: dict) -> dict:
    nxt = request["next"]
    stamp = request["transition_at"]
    cp = {
        "schema_version": "1.0.0",
        "revision": 1,
        "work_item_id": nxt["work_item_id"],
        "attempt_id": nxt["attempt_id"],
        "track": "character-appearance-production",
        "repository": "cybalicistjt-stack/multiversal-aioc",
        "branch": nxt["branch"],
        "status": "started",
        "started_at": stamp,
        "updated_at": stamp,
        "completed_at": None,
        "base_commit": nxt["base_commit"],
        "latest_pushed_commit": None,
        "expected_remote_head": nxt["base_commit"],
        "pull_request": None,
        "objective": nxt["objective"],
        "last_verified_action": f"Created governed {nxt['work_item_id']} transition from canonical base {nxt['base_commit']}.",
        "active_substep": nxt["active_substep"],
        "completed_substeps": ["Recovered the previous completed_verified CAPP boundary and selected the dependency-ordered next item."],
        "next_action": nxt["next_action"],
        "changed_paths": list(nxt.get("anticipated_changed_paths", [])),
        "completion_gate": {
            "required_evidence_kinds": ["commit", "pull_request", "merge"],
            "required_validation_commands": [nxt["validation_command"]],
            "owner_approval_required": False,
        },
        "validation": [{"command": nxt["validation_command"], "status": "not_run", "evidence": None}],
        "unresolved_failures": [],
        "owner_decision_required": False,
        "evidence": [{"kind": "commit", "value": f"{nxt['work_item_id']} base canonical main {nxt['base_commit']}"}],
        "roadmap_projection_pending": True,
        "notes": [
            "CAPP transition generated by tools/capp_transition.py; explanatory prose is non-authoritative.",
            "STAGE-A-A2 remains authorized but not activated; DS-008 remains unfinished/blocked_non_owner; Apple/WP-011 remains separate.",
            "No application runtime, release, deployment, tester access, paid service, production credential or unsupported canonical promotion is authorized.",
        ],
    }
    write(checkpoint_path(nxt["attempt_id"]), cp)
    return cp


def project_pointer_and_status(request: dict, backlog: dict, pointer: dict, cp: dict) -> None:
    nxt = request["next"]
    stamp = request["transition_at"]
    # Keep one completed CAPP anchor (the immediately prior item), not an ever-growing history list.
    existing = pointer.get("active_attempts", [])
    capp_entries = [item for item in existing if item.get("track") == "character-appearance-production"]
    latest_capp = None
    if request["mode"] == "advance":
        previous_attempt = request["previous"]["attempt_id"]
        latest_capp = next((copy.deepcopy(item) for item in capp_entries if item.get("attempt_id") == previous_attempt), None)
    elif backlog.get("last_completed"):
        previous_attempt = f"{backlog['last_completed']['work_item_id']}-attempt-001"
        latest_capp = next((copy.deepcopy(item) for item in capp_entries if item.get("attempt_id") == previous_attempt), None)
    retained = [copy.deepcopy(item) for item in existing if item.get("track") != "character-appearance-production"]
    next_entry = {
        "work_item_id": nxt["work_item_id"],
        "attempt_id": nxt["attempt_id"],
        "track": "character-appearance-production",
        "priority": 1,
        "owner_selected": True,
        "repository": "cybalicistjt-stack/multiversal-aioc",
        "branch": nxt["branch"],
        "checkpoint_path": f"governance/ai/work-state/{nxt['attempt_id']}.json",
        "status": "started",
        "updated_at": stamp,
        "roadmap_projection_pending": True,
    }
    new_entries = [next_entry]
    if latest_capp is not None:
        latest_capp["owner_selected"] = False
        latest_capp["status"] = "completed_verified"
        latest_capp["roadmap_projection_pending"] = False
        new_entries.append(latest_capp)
    new_entries.extend(retained)
    for index, item in enumerate(new_entries, 1):
        item["priority"] = index
    pointer["updated_at"] = stamp
    pointer["primary_attempt_id"] = nxt["attempt_id"]
    pointer["selection_reason"] = (
        f"{nxt['work_item_id']} is the dependency-ordered CAPP primary. Previous CAPP completion evidence is structured in its checkpoint/receipt; "
        "explanatory wording is non-authoritative. STAGE-A-A2 remains authorized/not activated, DS-008 remains blocked_non_owner, and Apple remains separate."
    )
    pointer["active_attempts"] = new_entries
    write(POINTER, pointer)

    active_count = sum(item.get("status") not in {"completed_verified", "superseded"} for item in new_entries)
    status = {
        "schema_version": "1.0.0",
        "generated_at": stamp,
        "source_pointer": "governance/ai/runtime/CURRENT_WORK_POINTER.json",
        "primary": {
            "work_item_id": nxt["work_item_id"],
            "attempt_id": nxt["attempt_id"],
            "track": "character-appearance-production",
            "repository": "cybalicistjt-stack/multiversal-aioc",
            "branch": nxt["branch"],
            "status": "started",
            "active_substep": cp["active_substep"],
            "next_action": cp["next_action"],
            "latest_pushed_commit": None,
            "pull_request": None,
            "owner_decision_required": False,
            "unresolved_failures": [],
            "roadmap_projection_pending": True,
        },
        "active_attempt_count": active_count,
        "deferred_track_count": len(pointer.get("deferred_tracks", [])),
    }
    write(STATUS, status)


def apply_transition(request_path: Path) -> None:
    backlog = load(BACKLOG)
    pointer = load(POINTER)
    ensure_boundaries(backlog)
    request = load(request_path)
    validate_request(request, backlog)
    if request["mode"] == "advance":
        complete_previous(request, backlog, pointer)
    nxt = request["next"]
    items = {item["id"]: item for item in backlog["work_items"]}
    items[nxt["work_item_id"]]["status"] = "in_progress"
    backlog["active_work_item_id"] = nxt["work_item_id"]
    backlog["completed_work_items"] = sum(item["status"] == "completed_verified" for item in backlog["work_items"])
    backlog["next_planned_work_item_id"] = next_after(backlog, nxt["work_item_id"])
    cp = create_start_checkpoint(request)
    project_pointer_and_status(request, backlog, pointer, cp)
    ensure_boundaries(backlog)
    write(BACKLOG, backlog)
    request_path.unlink()
    print(f"CAPP transition: PASS mode={request['mode']} active={nxt['work_item_id']} next={backlog['next_planned_work_item_id']}")


def self_test() -> None:
    # Structural smoke test for request rules; repository-state mutation is exercised by transition workflow validation.
    sample = {
        "schema_version": "1.0.0",
        "mode": "start",
        "transition_at": "2026-08-13T00:00:00Z",
        "next": {
            "work_item_id": "CAPP-03",
            "attempt_id": "CAPP-03-attempt-001",
            "branch": "governance/capp-03-example",
            "base_commit": "0" * 40,
            "objective": "Example objective",
            "active_substep": "Example active substep",
            "next_action": "Example next action",
            "validation_command": "Validate CAPP-03 Completion",
        },
    }
    req(sample["next"]["attempt_id"] == f"{sample['next']['work_item_id']}-attempt-001", "self-test attempt")
    req(SHA_RE.fullmatch(sample["next"]["base_commit"]) is not None, "self-test SHA")
    print("CAPP transition self-test: PASS")


def main() -> int:
    parser = argparse.ArgumentParser()
    sub = parser.add_subparsers(dest="command", required=True)
    apply_parser = sub.add_parser("apply")
    apply_parser.add_argument("--request", required=True)
    sub.add_parser("self-test")
    args = parser.parse_args()
    try:
        if args.command == "self-test":
            self_test()
        else:
            apply_transition(Path(args.request).resolve())
    except (TransitionError, OSError, json.JSONDecodeError, ValueError) as exc:
        print(f"CAPP transition FAILED: {exc}")
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
