#!/usr/bin/env python3
"""Deterministic Multiversal canonical-state health validator.

Historical material may remain in Git, but it must not occupy a current selector,
automatic workflow, or operational active/ready namespace.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

AIOC_RUNTIME_ALLOWED = {
    "ACTIVE_AUTHORITY_REGISTRY.json",
    "CURRENT_WORK_POINTER.json",
    "INTERACTION_OPERATIONAL_SCORECARD.json",
    "ROADMAP_INDEX.json",
}
AIOC_WORKFLOWS_ALLOWED = {"validate-repository-health.yml"}
APP_WORKFLOWS_ALLOWED = {
    "_validation-core-profile.yml",
    "self-hosted-windows-runner-smoke.yml",
}
APP_SELECTOR_PATHS = [
    ".ai/current-phase.md",
    ".ai/current-work-order.md",
    ".ai/next-task.md",
    ".ai/task-queue.md",
    ".ai/agent-handoff.md",
    ".ai/owner-control-center.md",
    ".ai/owner-decisions-needed.md",
    ".ai/project-context.md",
]


def read_json(path: Path) -> dict[str, Any]:
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except Exception as exc:
        raise AssertionError(f"invalid JSON {path}: {exc}") from exc
    assert isinstance(value, dict), f"expected object JSON: {path}"
    return value


def require(path: Path) -> None:
    assert path.exists(), f"required path missing: {path}"


def workflow_names(root: Path) -> set[str]:
    path = root / ".github" / "workflows"
    if not path.exists():
        return set()
    return {p.name for p in path.iterdir() if p.is_file() and p.suffix in {".yml", ".yaml"}}


def check_aioc(root: Path, errors: list[str]) -> dict[str, Any]:
    result: dict[str, Any] = {}
    try:
        bootstrap = root / "governance/ai/MULTIVERSAL_NEW_CONVERSATION_BOOTSTRAP.md"
        authority_path = root / "governance/ai/runtime/ACTIVE_AUTHORITY_REGISTRY.json"
        pointer_path = root / "governance/ai/runtime/CURRENT_WORK_POINTER.json"
        backlog_path = root / "governance/repository-health/CRS_BACKLOG.json"
        runtime_registry_path = root / "governance/repository-health/RUNTIME_STATE_LIFECYCLE_REGISTRY.json"
        workflow_registry_path = root / "governance/repository-health/WORKFLOW_LIFECYCLE_REGISTRY.json"
        validator_registry_path = root / "governance/repository-health/VALIDATOR_LIFECYCLE_REGISTRY.json"
        audit_path = root / "governance/repository-health/CANONICAL_STATE_AUDIT.json"
        for path in [bootstrap, authority_path, pointer_path, backlog_path, runtime_registry_path, workflow_registry_path, validator_registry_path, audit_path]:
            require(path)

        bootstrap_text = bootstrap.read_text(encoding="utf-8")
        assert "stable recovery protocol" in bootstrap_text
        assert "not a current-status document" in bootstrap_text
        assert "CURRENT_WORK_POINTER.json" in bootstrap_text
        assert "ACTIVE_AUTHORITY_REGISTRY.json" in bootstrap_text

        authority = read_json(authority_path)
        pointer = read_json(pointer_path)
        backlog = read_json(backlog_path)
        runtime_registry = read_json(runtime_registry_path)
        workflow_registry = read_json(workflow_registry_path)
        validator_registry = read_json(validator_registry_path)
        audit = read_json(audit_path)

        checkpoint_rel = pointer["active_attempt"]["checkpoint_path"]
        checkpoint_path = root / checkpoint_rel
        require(checkpoint_path)
        checkpoint = read_json(checkpoint_path)
        assert pointer["primary_attempt_id"] == checkpoint["attempt_id"]
        assert pointer["active_attempt"]["attempt_id"] == checkpoint["attempt_id"]
        assert pointer["active_attempt"]["work_item_id"] == checkpoint["work_item_id"]

        if backlog["status"] == "in_progress":
            assert pointer["active_attempt"]["active_item"] == checkpoint["active_substep"]
            assert backlog["active_item"] == pointer["active_attempt"]["active_item"]
            assert audit["production_resume_authorized"] is False
        elif backlog["status"] == "completed_verified":
            assert backlog["active_item"] is None
            assert audit["production_resume_authorized"] is True
        else:
            raise AssertionError(f"unexpected CRS backlog status: {backlog['status']}")

        for rel in [pointer["canonical_bootstrap"], pointer["authority_registry"], pointer["roadmap_index"], pointer["canonical_application_roadmap"]]:
            require(root / rel)
        for rel in pointer.get("roadmap_supplements", []):
            require(root / rel)
        for rel in pointer.get("mandatory_operating_policies", []):
            require(root / rel)

        runtime_dir = root / "governance/ai/runtime"
        live_runtime = {p.name for p in runtime_dir.iterdir() if p.is_file()}
        assert live_runtime == AIOC_RUNTIME_ALLOWED, f"AIOC runtime namespace drift: {sorted(live_runtime)}"
        assert not list(runtime_dir.glob("BOOTSTRAP_CURRENT_STATE_AMENDMENT_*"))
        assert not (runtime_dir / "CURRENT_IMPLEMENTATION_STATUS.json").exists()
        assert not list(runtime_dir.glob("ROADMAP_INDEX_*_SUPPLEMENT.json"))

        current_entries = authority.get("current", [])
        kinds = [entry.get("kind") for entry in current_entries]
        for singular in ["bootstrap", "work_pointer", "checkpoint", "program", "backlog", "roadmap"]:
            assert kinds.count(singular) == 1, f"authority registry must contain exactly one CURRENT {singular}"
        current_checkpoint = next(entry for entry in current_entries if entry.get("kind") == "checkpoint")
        assert current_checkpoint["path"] == checkpoint_rel
        assert authority.get("rule", "").startswith("Anything not explicitly CURRENT")

        assert runtime_registry["canonical_selector"]["path"] == "governance/ai/runtime/CURRENT_WORK_POINTER.json"
        assert runtime_registry["work_state"]["selected_checkpoint"] == checkpoint_rel
        assert runtime_registry["application_repository"]["local_selector_lifecycle"] == "HISTORICAL_INERT_COMPATIBILITY_REDIRECT"

        aioc_workflows = workflow_names(root)
        assert aioc_workflows == AIOC_WORKFLOWS_ALLOWED, f"unexpected AIOC workflows: {sorted(aioc_workflows)}"
        workflow_text = (root / ".github/workflows/validate-repository-health.yml").read_text(encoding="utf-8")
        assert "runs-on: ubuntu-latest" in workflow_text
        assert "governance-only check is an explicit exception" in workflow_text
        assert "actions/setup-python" not in workflow_text
        assert "scripts/validate_repository_health.py" in workflow_text

        aioc_registry = workflow_registry["repositories"]["cybalicistjt-stack/multiversal-aioc"]
        registered_aioc = {Path(item["path"]).name for item in aioc_registry["live_workflows"]}
        assert registered_aioc == aioc_workflows
        health_entry = aioc_registry["live_workflows"][0]
        assert health_entry["execution"] == "github_hosted_linux_governance_exception"
        assert health_entry["timeout_minutes"] <= 5

        assert validator_registry["default_rule"].startswith("A validator or validation-like script is not a current gate")
        registered_aioc_validators = {item["path"] for item in validator_registry["repositories"]["cybalicistjt-stack/multiversal-aioc"]["current_validators"]}
        assert "scripts/validate_repository_health.py" in registered_aioc_validators
        assert audit["result"] == "zero_known_conflicting_authority"
        assert audit["known_conflicts"] == []

        result.update({
            "pointer_attempt": checkpoint["attempt_id"],
            "active_item": pointer["active_attempt"].get("active_item"),
            "crs_status": backlog["status"],
            "runtime_files": sorted(live_runtime),
            "workflow_files": sorted(aioc_workflows),
        })
    except Exception as exc:
        errors.append(f"AIOC: {exc}")
    return result


def check_app(root: Path, audit: dict[str, Any], errors: list[str]) -> dict[str, Any]:
    result: dict[str, Any] = {}
    try:
        live_workflows = workflow_names(root)
        assert live_workflows == APP_WORKFLOWS_ALLOWED, f"App workflow namespace drift: {sorted(live_workflows)}"
        reusable = (root / ".github/workflows/_validation-core-profile.yml").read_text(encoding="utf-8")
        assert "workflow_call" in reusable
        assert "self-hosted" in reusable
        assert "ubuntu-latest" not in reusable
        assert "compare_receipts.py" in reusable
        smoke = (root / ".github/workflows/self-hosted-windows-runner-smoke.yml").read_text(encoding="utf-8")
        assert "workflow_dispatch" in smoke
        assert "ubuntu-latest" not in smoke

        assert not (root / ".agent/active-work-orders").exists()
        assert not (root / ".ai/ready-work-orders").exists()
        for rel in APP_SELECTOR_PATHS:
            path = root / rel
            require(path)
            text = path.read_text(encoding="utf-8")
            assert "HISTORICAL_INERT / COMPATIBILITY PATH ONLY" in text, f"selector not inert: {rel}"
            assert "CURRENT_WORK_POINTER.json" in text, f"selector does not redirect to AIOC: {rel}"

        evidence = audit["repositories"]["cybalicistjt-stack/Multiversal-app"]
        assert len(evidence["main_head"]) == 40
        preserved = evidence["preserved_open_prs"]
        numbers = [item["number"] for item in preserved]
        assert sorted(numbers) == [61, 191, 201]
        assert all(item["state"] == "open" and item["draft"] is True and item["merge_authority"] is False for item in preserved)

        result.update({
            "workflow_files": sorted(live_workflows),
            "compatibility_selectors": len(APP_SELECTOR_PATHS),
            "preserved_open_prs": numbers,
        })
    except Exception as exc:
        errors.append(f"App: {exc}")
    return result


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", default=".")
    parser.add_argument("--app-root")
    parser.add_argument("--output")
    args = parser.parse_args()

    root = Path(args.root).resolve()
    errors: list[str] = []
    aioc = check_aioc(root, errors)
    audit = read_json(root / "governance/repository-health/CANONICAL_STATE_AUDIT.json")
    app: dict[str, Any] | None = None
    if args.app_root:
        app = check_app(Path(args.app_root).resolve(), audit, errors)

    result = {
        "schema_version": "1.2.0",
        "validator": "scripts/validate_repository_health.py",
        "status": "FAIL" if errors else "PASS",
        "aioc": aioc,
        "application": app,
        "errors": errors,
    }
    payload = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.output:
        Path(args.output).write_text(payload, encoding="utf-8")
    print(payload, end="")
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
