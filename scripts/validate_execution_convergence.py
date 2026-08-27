#!/usr/bin/env python3
"""Validate Multiversal execution-convergence and bounded-CI controls."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

POLICY_PATH = "governance/ai/MULTIVERSAL_EXECUTION_CONVERGENCE_POLICY.md"
TAXONOMY_PATH = "governance/ai/interaction-system/analysis/EXECUTION_CONVERGENCE_FAILURE_TAXONOMY.json"
SCORECARD_PATH = "governance/ai/interaction-system/live/EXECUTION_CONVERGENCE_SCORECARD.json"
REMEDIATION_CHECKPOINT = "governance/ai/work-state/MV-CONT-006-attempt-001.json"
LEGACY_WORKFLOW = ".github/workflows/self-hosted-windows-runner-smoke.yml"
CURRENT_SELECTOR = ".github/workflows/validate-current-tranche.yml"
SHARED_CORE = ".github/workflows/_validation-core-profile.yml"
APP_HEALTH = ".github/workflows/validate-repository-health.yml"
FAILURE_CLASSES = {
    "feature_implementation",
    "validation_contract",
    "validation_infrastructure",
    "runner_environment",
    "repository_state",
    "owner_only",
}
BLOCKED_STATES = {"blocked_control_plane", "blocked_environment", "blocked_owner"}


class ConvergenceError(RuntimeError):
    pass


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ConvergenceError(message)


def load_json(root: Path, rel: str) -> dict[str, Any]:
    path = root / rel
    require(path.is_file(), f"missing required file: {rel}")
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise ConvergenceError(f"invalid JSON {rel}: {exc}") from exc
    require(isinstance(value, dict), f"expected object JSON: {rel}")
    return value


def validate_convergence_control(control: dict[str, Any], *, status: str, context: str) -> None:
    required = {
        "owner_continue_count",
        "execution_cycles",
        "repair_cycles",
        "no_progress_cycles",
        "diagnostic_mode",
        "last_failure_signature",
        "last_failure_class",
        "diagnostic_hypotheses",
        "retry_basis",
        "service_objective",
    }
    require(required <= set(control), f"{context}: convergence_control missing {sorted(required - set(control))}")
    for key in ("owner_continue_count", "execution_cycles", "repair_cycles", "no_progress_cycles"):
        require(isinstance(control[key], int) and control[key] >= 0, f"{context}: {key} must be a non-negative integer")
    require(isinstance(control["diagnostic_mode"], bool), f"{context}: diagnostic_mode must be boolean")
    require(isinstance(control["diagnostic_hypotheses"], list), f"{context}: diagnostic_hypotheses must be an array")

    failure_class = control["last_failure_class"]
    require(failure_class is None or failure_class in FAILURE_CLASSES, f"{context}: invalid last_failure_class {failure_class!r}")

    objective = control["service_objective"]
    require(isinstance(objective, dict), f"{context}: service_objective must be an object")
    require(objective.get("ordinary_tranche_single_continue_target_percent") == 80, f"{context}: single-continue target must remain 80")
    require(objective.get("ordinary_tranche_two_continue_target_percent") == 95, f"{context}: two-continue target must remain 95")
    require(objective.get("max_execution_cycles_without_genuine_blocker") == 2, f"{context}: max cycles without genuine blocker must remain 2")
    require(objective.get("unrelated_historical_validation_jobs_target") == 0, f"{context}: unrelated validation target must remain zero")
    require(objective.get("reruns_without_changed_evidence_target") == 0, f"{context}: retry-without-change target must remain zero")
    require(objective.get("post_merge_stale_pointer_target") == 0, f"{context}: stale-pointer target must remain zero")

    if control["repair_cycles"] >= 2:
        require(control["diagnostic_mode"] is True, f"{context}: second repair requires diagnostic_mode")
        require(bool(control["last_failure_signature"]), f"{context}: diagnostic repair requires last_failure_signature")
        require(failure_class in FAILURE_CLASSES, f"{context}: diagnostic repair requires classified failure")
        require(bool(control["diagnostic_hypotheses"]), f"{context}: diagnostic repair requires hypotheses")

    retry = control["retry_basis"]
    if retry is not None:
        require(isinstance(retry, dict), f"{context}: retry_basis must be null or object")
        changed = retry.get("changed_since_previous")
        require(isinstance(changed, list) and any(str(item).strip() for item in changed), f"{context}: retry requires changed_since_previous evidence")

    if control["no_progress_cycles"] >= 2:
        require(status in BLOCKED_STATES or control["diagnostic_mode"] is True, f"{context}: two no-progress cycles require blocked or diagnostic state")


def check(root: Path) -> dict[str, Any]:
    root = root.resolve()
    require((root / POLICY_PATH).is_file(), f"missing convergence policy: {POLICY_PATH}")
    taxonomy = load_json(root, TAXONOMY_PATH)
    scorecard = load_json(root, SCORECARD_PATH)
    remediation = load_json(root, REMEDIATION_CHECKPOINT)
    pointer = load_json(root, "governance/ai/runtime/CURRENT_WORK_POINTER.json")
    authority = load_json(root, "governance/ai/runtime/ACTIVE_AUTHORITY_REGISTRY.json")
    workflow_registry = load_json(root, "governance/repository-health/WORKFLOW_LIFECYCLE_REGISTRY.json")

    require(taxonomy.get("work_item_id") == "MV-CONT-006", "convergence taxonomy work item mismatch")
    class_ids = {item.get("id") for item in taxonomy.get("failure_classes", [])}
    required_ids = {
        "MV-CONV-RETRY-001",
        "MV-CONV-DIAG-001",
        "MV-CONV-CI-001",
        "MV-CONV-STATE-001",
        "MV-CONV-INTERRUPT-001",
        "MV-CONV-NOPROGRESS-001",
    }
    require(class_ids == required_ids, "convergence failure taxonomy coverage drift")

    targets = scorecard.get("targets", {})
    require(targets.get("ordinary_tranche_single_continue_completion_percent_min") == 80, "live scorecard single-continue target drift")
    require(targets.get("ordinary_tranche_completion_within_two_continues_percent_min") == 95, "live scorecard two-continue target drift")
    require(targets.get("unrelated_historical_validation_jobs") == 0, "live scorecard unrelated-validation target drift")
    require(targets.get("reruns_without_changed_evidence") == 0, "live scorecard retry target drift")
    require(targets.get("post_merge_stale_pointer_incidents") == 0, "live scorecard stale-pointer target drift")
    privacy = scorecard.get("privacy", {})
    require(privacy.get("aggregation_only") is True, "live scorecard must remain aggregate-only")
    require(privacy.get("raw_private_transcript_text_published") is False, "raw private transcript publication forbidden")

    require(remediation.get("work_item_id") == "MV-CONT-006", "remediation checkpoint work item mismatch")
    require(remediation.get("attempt_id") == "MV-CONT-006-attempt-001", "remediation checkpoint attempt mismatch")
    validate_convergence_control(remediation.get("convergence_control", {}), status=str(remediation.get("status")), context="MV-CONT-006")

    active = pointer.get("active_attempt", {})
    checkpoint_rel = active.get("checkpoint_path")
    if checkpoint_rel:
        checkpoint = load_json(root, checkpoint_rel)
        require(checkpoint.get("attempt_id") == active.get("attempt_id"), "current pointer/checkpoint attempt mismatch")
        require(checkpoint.get("status") == active.get("status"), "current pointer/checkpoint status mismatch")
        if active.get("implementation_authority") is True:
            validate_convergence_control(checkpoint.get("convergence_control", {}), status=str(checkpoint.get("status")), context=str(active.get("attempt_id")))

    current_authorities = authority.get("current", [])
    policy_entries = [item for item in current_authorities if item.get("path") == POLICY_PATH]
    require(len(policy_entries) == 1 and policy_entries[0].get("lifecycle") == "CURRENT", "convergence policy must be registered CURRENT")

    app_registry = workflow_registry.get("repositories", {}).get("cybalicistjt-stack/Multiversal-app", {})
    live = app_registry.get("live_workflows", [])
    paths = {item.get("path") for item in live}
    require(LEGACY_WORKFLOW not in paths, "legacy all-profile workflow remains registered live")
    require(paths == {SHARED_CORE, CURRENT_SELECTOR, APP_HEALTH}, f"application workflow registry drift: {sorted(paths)}")
    selector = next(item for item in live if item.get("path") == CURRENT_SELECTOR)
    require(selector.get("lifecycle") == "CURRENT", "bounded current-tranche selector must be CURRENT")
    require(selector.get("validation_scope") == "single_governed_profile", "bounded selector validation_scope mismatch")
    require(selector.get("automatic_repository_event_trigger") is True, "bounded selector must validate matching PR changes")

    observed_main = scorecard.get("remediation_evidence", {}).get("application_main_after_merge")
    require(app_registry.get("current_main") == observed_main, "workflow registry current_main must equal observed post-cleanup application main")

    return {
        "schema_version": "1.0.0",
        "validator": "scripts/validate_execution_convergence.py",
        "status": "PASS",
        "current_attempt": active.get("attempt_id"),
        "current_attempt_status": active.get("status"),
        "registered_application_workflows": sorted(paths),
        "legacy_fanout_registered": False,
        "single_continue_target_percent": 80,
        "two_continue_target_percent": 95,
        "live_same_cycle_baseline_percent": scorecard.get("baseline", {}).get("same_cycle_completion_percent"),
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", default=".")
    parser.add_argument("--output")
    args = parser.parse_args()
    try:
        result = check(Path(args.root))
    except (ConvergenceError, OSError) as exc:
        result = {
            "schema_version": "1.0.0",
            "validator": "scripts/validate_execution_convergence.py",
            "status": "FAIL",
            "error": str(exc),
        }
    payload = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.output:
        Path(args.output).write_text(payload, encoding="utf-8")
    print(payload, end="")
    return 0 if result["status"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
