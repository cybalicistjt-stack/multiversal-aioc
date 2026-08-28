#!/usr/bin/env python3
"""Flat deterministic AIOC authority, lifecycle and sealed-proof health audit."""
from __future__ import annotations

import argparse
import hashlib
import json
import subprocess
import sys
from pathlib import Path
from typing import Any

from execution_termination_preflight import PreflightError, self_test as termination_self_test


POINTER_PATH = Path("governance/ai/runtime/CURRENT_WORK_POINTER.json")
AUTHORITY_PATH = Path("governance/ai/runtime/ACTIVE_AUTHORITY_REGISTRY.json")
WORKFLOW_REGISTRY_PATH = Path(
    "governance/repository-health/WORKFLOW_LIFECYCLE_REGISTRY.json"
)
VALIDATOR_REGISTRY_PATH = Path(
    "governance/repository-health/VALIDATOR_LIFECYCLE_REGISTRY.json"
)
RUNTIME_REGISTRY_PATH = Path(
    "governance/repository-health/RUNTIME_STATE_LIFECYCLE_REGISTRY.json"
)
SEALED_PROOFS_PATH = Path("governance/repository-health/SEALED_VALIDATION_PROOFS.json")
SCORECARD_PATH = Path(
    "governance/ai/interaction-system/live/EXECUTION_CONVERGENCE_SCORECARD.json"
)
CURRENT_WORKFLOW = Path(".github/workflows/validate-repository-health.yml")
CURRENT_VALIDATOR = Path("scripts/validate_repository_health.py")
CURRENT_PREFLIGHT = Path("scripts/execution_termination_preflight.py")
CURRENT_CONTROL_TESTS = Path("tests/control_plane/test_control_plane_health.py")
EXPECTED_AIOC_WORKFLOWS = {"validate-repository-health.yml"}
EXPECTED_APP_WORKFLOWS = {
    "_validation-core-profile.yml",
    "validate-current-family.yml",
}
REQUIRED_SERVICE_OBJECTIVE = {
    "ordinary_tranche_single_continue_target_percent": 80,
    "ordinary_tranche_two_continue_target_percent": 95,
    "max_execution_cycles_without_genuine_blocker": 2,
    "unrelated_historical_validation_jobs_target": 0,
    "reruns_without_changed_evidence_target": 0,
    "post_merge_stale_pointer_target": 0,
}
FAILURE_CLASSES = {
    "feature_implementation",
    "validation_contract",
    "validation_infrastructure",
    "runner_environment",
    "repository_state",
    "owner_only",
}


class Audit:
    def __init__(self, root: Path) -> None:
        self.root = root.resolve()
        self.errors: list[dict[str, str]] = []

    def fail(self, code: str, message: str, path: str | Path | None = None) -> None:
        error = {"code": code, "message": message}
        if path is not None:
            error["path"] = str(path).replace("\\", "/")
        self.errors.append(error)

    def require(
        self,
        condition: bool,
        code: str,
        message: str,
        path: str | Path | None = None,
    ) -> bool:
        if not condition:
            self.fail(code, message, path)
            return False
        return True

    def read_json(self, relative: Path) -> dict[str, Any]:
        path = self.root / relative
        try:
            value = json.loads(path.read_text(encoding="utf-8"))
        except FileNotFoundError:
            self.fail("MVHEALTH-FILE-MISSING", "required JSON file is missing", relative)
            return {}
        except json.JSONDecodeError as exc:
            self.fail("MVHEALTH-JSON-INVALID", f"invalid JSON: {exc}", relative)
            return {}
        except OSError as exc:
            self.fail("MVHEALTH-IO", f"could not read JSON: {exc}", relative)
            return {}
        if not isinstance(value, dict):
            self.fail("MVHEALTH-JSON-TYPE", "expected object JSON", relative)
            return {}
        return value

    def read_text(self, relative: Path) -> str:
        path = self.root / relative
        try:
            return path.read_text(encoding="utf-8")
        except OSError as exc:
            self.fail("MVHEALTH-TEXT-READ", f"could not read text: {exc}", relative)
            return ""

    def git(self, *arguments: str, cwd: Path | None = None) -> str | None:
        workdir = cwd or self.root
        process = subprocess.run(
            ["git", *arguments],
            cwd=workdir,
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            check=False,
        )
        if process.returncode:
            self.fail(
                "MVHEALTH-GIT",
                f"git {' '.join(arguments)} failed: {process.stdout.strip()}",
                workdir,
            )
            return None
        return process.stdout.strip()


def _is_sha(value: Any) -> bool:
    return (
        isinstance(value, str)
        and len(value) == 40
        and all(character in "0123456789abcdef" for character in value)
    )


def _validate_convergence_control(
    audit: Audit, control: dict[str, Any], status: str, context: str
) -> None:
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
    missing = sorted(required - set(control))
    audit.require(
        not missing,
        "MVHEALTH-CONVERGENCE-FIELDS",
        f"{context} convergence_control missing {missing}",
    )
    for key in (
        "owner_continue_count",
        "execution_cycles",
        "repair_cycles",
        "no_progress_cycles",
    ):
        value = control.get(key)
        audit.require(
            isinstance(value, int) and value >= 0,
            "MVHEALTH-CONVERGENCE-COUNTER",
            f"{context} {key} must be a non-negative integer",
        )
    audit.require(
        isinstance(control.get("diagnostic_mode"), bool),
        "MVHEALTH-CONVERGENCE-DIAGNOSTIC",
        f"{context} diagnostic_mode must be boolean",
    )
    hypotheses = control.get("diagnostic_hypotheses")
    audit.require(
        isinstance(hypotheses, list),
        "MVHEALTH-CONVERGENCE-HYPOTHESES",
        f"{context} diagnostic_hypotheses must be an array",
    )
    failure_class = control.get("last_failure_class")
    audit.require(
        failure_class is None or failure_class in FAILURE_CLASSES,
        "MVHEALTH-CONVERGENCE-CLASS",
        f"{context} invalid failure class {failure_class!r}",
    )
    objective = control.get("service_objective")
    audit.require(
        objective == REQUIRED_SERVICE_OBJECTIVE,
        "MVHEALTH-CONVERGENCE-OBJECTIVE",
        f"{context} service objective drift",
    )
    repair_cycles = control.get("repair_cycles")
    if isinstance(repair_cycles, int) and repair_cycles >= 2:
        audit.require(
            control.get("diagnostic_mode") is True,
            "MVHEALTH-CONVERGENCE-ESCALATION",
            f"{context} second repair requires diagnostic mode",
        )
        audit.require(
            bool(control.get("last_failure_signature"))
            and failure_class in FAILURE_CLASSES
            and bool(hypotheses),
            "MVHEALTH-CONVERGENCE-DIAGNOSTIC-EVIDENCE",
            f"{context} diagnostic repair lacks classified evidence/hypotheses",
        )
    retry = control.get("retry_basis")
    if retry is not None:
        changed = retry.get("changed_since_previous") if isinstance(retry, dict) else None
        audit.require(
            isinstance(changed, list)
            and any(isinstance(item, str) and item.strip() for item in changed),
            "MVHEALTH-CONVERGENCE-RETRY",
            f"{context} retry lacks changed evidence",
        )
    no_progress = control.get("no_progress_cycles")
    if isinstance(no_progress, int) and no_progress >= 2:
        audit.require(
            status in {"blocked_control_plane", "blocked_environment", "blocked_owner"}
            or control.get("diagnostic_mode") is True,
            "MVHEALTH-CONVERGENCE-NOPROGRESS",
            f"{context} two no-progress cycles require blocked or diagnostic state",
        )


def _validate_authority_and_pointer(
    audit: Audit,
    pointer: dict[str, Any],
    authority: dict[str, Any],
    runtime: dict[str, Any],
) -> dict[str, Any]:
    active = pointer.get("active_attempt", {})
    attempt_id = active.get("attempt_id")
    audit.require(
        isinstance(attempt_id, str)
        and bool(attempt_id)
        and pointer.get("primary_attempt_id") == attempt_id,
        "MVHEALTH-SELECTOR-IDENTITY",
        "pointer primary attempt must identify the selected active attempt",
        POINTER_PATH,
    )
    selected_path = Path(str(active.get("checkpoint_path", "")))
    selected = audit.read_json(selected_path)
    selected_status = active.get("status")
    audit.require(
        selected.get("work_item_id") == active.get("work_item_id")
        and selected.get("attempt_id") == attempt_id
        and selected.get("status") == selected_status
        and selected.get("implementation_branch")
        == active.get("implementation_branch"),
        "MVHEALTH-SELECTED-CHECKPOINT",
        "selected checkpoint identity, status or branch disagrees with the pointer",
        selected_path,
    )
    if selected_status == "selected_not_started":
        audit.require(
            active.get("implementation_branch") is None
            and selected.get("implementation_authority") is False,
            "MVHEALTH-UNAUTHORIZED-FEATURE-START",
            "selected_not_started work must not have a branch or implementation authority",
            selected_path,
        )
    else:
        audit.require(
            selected_status in {"in_progress", "ready_for_review"}
            and isinstance(active.get("implementation_branch"), str)
            and selected.get("implementation_authority") is True,
            "MVHEALTH-ACTIVE-FEATURE-STATE",
            "started product work must be authorized, branch-bound and nonterminal",
            selected_path,
        )

    current_entries = authority.get("current", [])
    paths = [item.get("path") for item in current_entries if isinstance(item, dict)]
    audit.require(
        len(paths) == len(set(paths)),
        "MVHEALTH-AUTHORITY-DUPLICATE",
        "authority registry contains duplicate current paths",
        AUTHORITY_PATH,
    )
    for path in paths:
        if isinstance(path, str):
            audit.require(
                (audit.root / path).is_file(),
                "MVHEALTH-AUTHORITY-MISSING",
                "registered current authority file is missing",
                path,
            )
    mandatory_paths = {
        POINTER_PATH.as_posix(),
        RUNTIME_REGISTRY_PATH.as_posix(),
        WORKFLOW_REGISTRY_PATH.as_posix(),
        VALIDATOR_REGISTRY_PATH.as_posix(),
        SEALED_PROOFS_PATH.as_posix(),
        "governance/ai/interaction-system/EXECUTION_TERMINATION_CONTRACT.json",
        "governance/ai/interaction-system/OWNER_AI_INTERACTION_CONTRACT.md",
    }
    audit.require(
        mandatory_paths <= set(paths),
        "MVHEALTH-AUTHORITY-COVERAGE",
        f"authority registry missing {sorted(mandatory_paths - set(paths))}",
        AUTHORITY_PATH,
    )

    authority_active = authority.get("active_planning_work", {})
    runtime_active = runtime.get("active_work", {})
    audit.require(
        authority_active.get("work_item") == active.get("work_item_id")
        and authority_active.get("attempt_id") == attempt_id
        and authority_active.get("state") == selected_status
        and authority_active.get("implementation_branch")
        == active.get("implementation_branch")
        and authority_active.get("implementation_authority")
        == selected.get("implementation_authority"),
        "MVHEALTH-AUTHORITY-SELECTOR-DRIFT",
        "authority registry active planning work disagrees with the pointer/checkpoint",
        AUTHORITY_PATH,
    )
    audit.require(
        runtime_active.get("work_item") == active.get("work_item_id")
        and runtime_active.get("attempt_id") == attempt_id
        and runtime_active.get("state") == selected_status
        and runtime_active.get("implementation_branch")
        == active.get("implementation_branch")
        and runtime_active.get("implementation_authority")
        == selected.get("implementation_authority"),
        "MVHEALTH-RUNTIME-SELECTOR-DRIFT",
        "runtime registry active work disagrees with the pointer/checkpoint",
        RUNTIME_REGISTRY_PATH,
    )

    maintenance = pointer.get("exclusive_control_plane_maintenance")
    if isinstance(maintenance, dict):
        checkpoint_path = Path(str(maintenance.get("checkpoint_path", "")))
        checkpoint = audit.read_json(checkpoint_path)
        audit.require(
            isinstance(maintenance.get("attempt_id"), str)
            and bool(maintenance.get("attempt_id"))
            and maintenance.get("attempt_id") == checkpoint.get("attempt_id")
            and maintenance.get("work_item_id") == checkpoint.get("work_item_id"),
            "MVHEALTH-MAINTENANCE-IDENTITY",
            "maintenance pointer/checkpoint identity mismatch",
            checkpoint_path,
        )
        audit.require(
            maintenance.get("status") == checkpoint.get("status")
            and checkpoint.get("status") in {"in_progress", "ready_for_review"}
            and maintenance.get("branch") == checkpoint.get("implementation_branch")
            and checkpoint.get("implementation_authority") is True
            and maintenance.get("feature_starts_blocked") is True,
            "MVHEALTH-MAINTENANCE-STATE",
            "active maintenance must be in_progress/ready_for_review, branch-consistent, authorized and feature-blocking",
            checkpoint_path,
        )
        _validate_convergence_control(
            audit,
            checkpoint.get("convergence_control", {}),
            str(checkpoint.get("status")),
            str(checkpoint.get("attempt_id")),
        )
        audit.require(
            checkpoint_path.as_posix() in paths,
            "MVHEALTH-MAINTENANCE-AUTHORITY",
            "active maintenance checkpoint is not registered CURRENT",
            AUTHORITY_PATH,
        )
        authority_maintenance = authority.get("exclusive_control_plane_maintenance", {})
        runtime_maintenance = runtime.get("exclusive_control_plane_maintenance", {})
        audit.require(
            authority_maintenance.get("work_item") == checkpoint.get("work_item_id")
            and authority_maintenance.get("attempt_id") == checkpoint.get("attempt_id")
            and authority_maintenance.get("state") == checkpoint.get("status")
            and authority_maintenance.get("implementation_branch")
            == checkpoint.get("implementation_branch")
            and authority_maintenance.get("implementation_authority") is True
            and authority_maintenance.get("feature_starts_blocked") is True,
            "MVHEALTH-AUTHORITY-MAINTENANCE-DRIFT",
            "authority registry maintenance lease drift",
            AUTHORITY_PATH,
        )
        audit.require(
            runtime_maintenance.get("work_item") == checkpoint.get("work_item_id")
            and runtime_maintenance.get("attempt_id") == checkpoint.get("attempt_id")
            and runtime_maintenance.get("state") == checkpoint.get("status")
            and runtime_maintenance.get("implementation_branch")
            == checkpoint.get("implementation_branch")
            and runtime_maintenance.get("implementation_authority") is True
            and runtime_maintenance.get("feature_starts_blocked") is True,
            "MVHEALTH-RUNTIME-MAINTENANCE-DRIFT",
            "runtime registry maintenance lease drift",
            RUNTIME_REGISTRY_PATH,
        )
    else:
        audit.require(
            "exclusive_control_plane_maintenance" not in authority
            and "exclusive_control_plane_maintenance" not in runtime,
            "MVHEALTH-CLEARED-LEASE-DRIFT",
            "cleared pointer lease remains active in a lifecycle registry",
        )
        completed_records = pointer.get(
            "recently_completed_repository_health_maintenance", []
        )
        audit.require(
            isinstance(completed_records, list),
            "MVHEALTH-MAINTENANCE-HISTORY-TYPE",
            "completed repository-health maintenance must be an array",
            POINTER_PATH,
        )
        for completed in (
            completed_records if isinstance(completed_records, list) else []
        ):
            if not isinstance(completed, dict):
                audit.fail(
                    "MVHEALTH-MAINTENANCE-HISTORY-ROW",
                    "completed maintenance record must be an object",
                    POINTER_PATH,
                )
                continue
            checkpoint_path = Path(str(completed.get("checkpoint_path", "")))
            checkpoint = audit.read_json(checkpoint_path)
            completion = checkpoint.get("completion_evidence", {})
            audit.require(
                checkpoint.get("work_item_id") == completed.get("work_item_id")
                and checkpoint.get("status") == completed.get("status") == "completed_verified"
                and completion.get("application", {}).get("merge_sha")
                == completed.get("application_merge")
                and completion.get("aioc", {}).get("merge_sha")
                == completed.get("aioc_merge")
                and completion.get("aioc", {}).get("repository_health_run")
                == completed.get("aioc_repository_health_run")
                and completion.get("zombie_retirement", {}).get("closed_prs")
                == completed.get("superseded_prs_closed"),
                "MVHEALTH-MAINTENANCE-CLOSEOUT-DRIFT",
                f"{completed.get('work_item_id')} pointer/checkpoint completion evidence drift",
                checkpoint_path,
            )
            authority_completed = next(
                (
                    row
                    for row in authority.get(
                        "recently_completed_repository_health_remediation", []
                    )
                    if isinstance(row, dict)
                    and row.get("work_item") == completed.get("work_item_id")
                ),
                None,
            )
            audit.require(
                isinstance(authority_completed, dict)
                and authority_completed.get("aioc_merge") == completed.get("aioc_merge")
                and authority_completed.get("superseded_prs_closed")
                == completed.get("superseded_prs_closed"),
                "MVHEALTH-AUTHORITY-CLOSEOUT-DRIFT",
                f"authority registry {completed.get('work_item_id')} completion evidence drift",
                AUTHORITY_PATH,
            )
        runtime_completed = runtime.get(
            "recently_completed_control_plane_maintenance", {}
        )
        latest = completed_records[0] if completed_records else None
        if isinstance(latest, dict):
            audit.require(
                runtime_completed.get("work_item") == latest.get("work_item_id")
                and runtime_completed.get("state") == "completed_verified"
                and runtime_completed.get("aioc_merge") == latest.get("aioc_merge")
                and runtime_completed.get("superseded_prs_closed")
                == latest.get("superseded_prs_closed"),
                "MVHEALTH-RUNTIME-CLOSEOUT-DRIFT",
                "runtime registry latest maintenance completion evidence drift",
                RUNTIME_REGISTRY_PATH,
            )
    return {
        "selected_attempt": active.get("attempt_id"),
        "selected_status": active.get("status"),
        "maintenance_attempt": maintenance.get("attempt_id")
        if isinstance(maintenance, dict)
        else None,
        "maintenance_status": maintenance.get("status")
        if isinstance(maintenance, dict)
        else None,
    }


def _validate_workflows(
    audit: Audit, workflow_registry: dict[str, Any]
) -> dict[str, Any]:
    workflow_dir = audit.root / ".github/workflows"
    actual = {
        path.name
        for path in workflow_dir.iterdir()
        if path.is_file() and path.suffix in {".yml", ".yaml"}
    }
    audit.require(
        actual == EXPECTED_AIOC_WORKFLOWS,
        "MVHEALTH-AIOC-WORKFLOW-NAMESPACE",
        f"AIOC workflow namespace drift: {sorted(actual)}",
        workflow_dir,
    )
    source = audit.read_text(CURRENT_WORKFLOW)
    historical_markers = ("validate_" + "rsr_", "_validate_" + "repository_health_v")
    for marker in historical_markers:
        audit.require(
            marker not in source,
            "MVHEALTH-HISTORICAL-WORKFLOW-EXECUTION",
            f"current workflow references historical validator marker {marker}",
            CURRENT_WORKFLOW,
        )
    audit.require(
        source.count("python3 scripts/validate_repository_health.py") == 1,
        "MVHEALTH-WORKFLOW-ENTRYPOINT",
        "current AIOC workflow must invoke the flat health entrypoint exactly once",
        CURRENT_WORKFLOW,
    )
    audit.require(
        "tests/control_plane/**" in source
        and "python3 -m unittest discover -s tests/control_plane" in source,
        "MVHEALTH-CONTROL-PLANE-TEST-EXECUTION",
        "the one AIOC health workflow must trigger and run current control-plane regressions",
        CURRENT_WORKFLOW,
    )
    audit.require(
        "fetch-depth: 0" in source and "--expected-head" in source,
        "MVHEALTH-WORKFLOW-EXACT-HEAD",
        "AIOC workflow must fetch ancestry and bind the exact candidate head",
        CURRENT_WORKFLOW,
    )

    repositories = workflow_registry.get("repositories", {})
    aioc_live = repositories.get("cybalicistjt-stack/multiversal-aioc", {}).get(
        "live_workflows", []
    )
    aioc_paths = {Path(str(item.get("path"))).name for item in aioc_live}
    audit.require(
        aioc_paths == EXPECTED_AIOC_WORKFLOWS and len(aioc_live) == 1,
        "MVHEALTH-AIOC-WORKFLOW-REGISTRY",
        f"AIOC workflow registry drift: {sorted(aioc_paths)}",
        WORKFLOW_REGISTRY_PATH,
    )
    app_registry = repositories.get("cybalicistjt-stack/Multiversal-app", {})
    app_live = app_registry.get("live_workflows", [])
    app_paths = {Path(str(item.get("path"))).name for item in app_live}
    automatic = [
        item for item in app_live if item.get("automatic_repository_event_trigger") is True
    ]
    audit.require(
        app_paths == EXPECTED_APP_WORKFLOWS and len(automatic) == 1,
        "MVHEALTH-APP-WORKFLOW-REGISTRY",
        f"application workflow registry drift: {sorted(app_paths)}, automatic={len(automatic)}",
        WORKFLOW_REGISTRY_PATH,
    )
    audit.require(
        _is_sha(app_registry.get("current_main")),
        "MVHEALTH-APP-MAIN-REGISTRY",
        "workflow registry application main must be a canonical commit SHA",
        WORKFLOW_REGISTRY_PATH,
    )
    return {
        "aioc_live": sorted(actual),
        "application_registered": sorted(app_paths),
        "application_automatic_workflows": len(automatic),
        "historical_validator_executions": 0,
    }


def _validate_validators(
    audit: Audit, validator_registry: dict[str, Any]
) -> dict[str, Any]:
    source = audit.read_text(CURRENT_VALIDATOR)
    forbidden_markers = (
        "import" + "lib.",
        "_validate_" + "repository_health_v",
        "validate_" + "rsr_",
    )
    for marker in forbidden_markers:
        audit.require(
            marker not in source,
            "MVHEALTH-HISTORICAL-RUNTIME-IMPORT",
            f"flat validator contains forbidden historical runtime marker {marker}",
            CURRENT_VALIDATOR,
        )
    repositories = validator_registry.get("repositories", {})
    aioc = repositories.get("cybalicistjt-stack/multiversal-aioc", {})
    current = aioc.get("current_validators", [])
    audit.require(
        len(current) == 1
        and current[0].get("path") == str(CURRENT_VALIDATOR).replace("\\", "/")
        and current[0].get("runtime_imports_historical_validators") is False,
        "MVHEALTH-VALIDATOR-REGISTRY",
        "AIOC must register exactly one flat current validator",
        VALIDATOR_REGISTRY_PATH,
    )
    utilities = aioc.get("current_compatible_utilities", [])
    audit.require(
        len(utilities) == 1
        and utilities[0].get("path") == str(CURRENT_PREFLIGHT).replace("\\", "/"),
        "MVHEALTH-PREFLIGHT-REGISTRY",
        "executable termination preflight must be the sole current-compatible AIOC utility",
        VALIDATOR_REGISTRY_PATH,
    )
    regression_suites = aioc.get("current_regression_suites", [])
    audit.require(
        len(regression_suites) == 1
        and regression_suites[0].get("path")
        == str(CURRENT_CONTROL_TESTS).replace("\\", "/")
        and regression_suites[0].get("caller")
        == str(CURRENT_WORKFLOW).replace("\\", "/"),
        "MVHEALTH-REGRESSION-REGISTRY",
        "the focused control-plane regression suite must be registered to the one health workflow",
        VALIDATOR_REGISTRY_PATH,
    )
    retired_suites = aioc.get("retired_legacy_control_suites", [])
    audit.require(
        isinstance(retired_suites, list) and bool(retired_suites),
        "MVHEALTH-LEGACY-CONTROL-REGISTRY",
        "superseded continuity/interaction control suites must remain explicitly historical inert",
        VALIDATOR_REGISTRY_PATH,
    )
    current_execution_text = source + audit.read_text(CURRENT_WORKFLOW)
    for row in retired_suites if isinstance(retired_suites, list) else []:
        tool = row.get("tool") if isinstance(row, dict) else None
        test = row.get("test") if isinstance(row, dict) else None
        audit.require(
            row.get("lifecycle") == "HISTORICAL_INERT"
            and isinstance(tool, str)
            and isinstance(test, str)
            and (audit.root / tool).is_file()
            and (audit.root / test).is_file(),
            "MVHEALTH-LEGACY-CONTROL-ENTRY",
            f"invalid retired legacy control suite entry: {row!r}",
            VALIDATOR_REGISTRY_PATH,
        )
        if isinstance(tool, str):
            audit.require(
                Path(tool).name not in current_execution_text,
                "MVHEALTH-LEGACY-CONTROL-EXECUTION",
                f"current execution surface references retired control tool {tool}",
                CURRENT_VALIDATOR,
            )
    return {
        "current_validator": str(CURRENT_VALIDATOR).replace("\\", "/"),
        "current_compatible_utility": str(CURRENT_PREFLIGHT).replace("\\", "/"),
        "current_regression_suite": str(CURRENT_CONTROL_TESTS).replace("\\", "/"),
        "historical_runtime_imports": 0,
        "retired_legacy_control_suites": len(retired_suites)
        if isinstance(retired_suites, list)
        else 0,
    }


def _validate_sealed_proofs(
    audit: Audit,
    sealed: dict[str, Any],
    validator_registry: dict[str, Any],
    workflow_registry: dict[str, Any],
    pointer: dict[str, Any],
) -> dict[str, Any]:
    baseline = sealed.get("aioc_baseline", {})
    commit = baseline.get("commit")
    tree = baseline.get("tree")
    audit.require(
        _is_sha(commit) and _is_sha(tree),
        "MVHEALTH-SEALED-IDENTITY",
        "sealed AIOC commit/tree identity is invalid",
        SEALED_PROOFS_PATH,
    )
    if _is_sha(commit) and _is_sha(tree):
        observed_tree = audit.git("rev-parse", f"{commit}^{{tree}}")
        audit.require(
            observed_tree == tree,
            "MVHEALTH-SEALED-TREE",
            f"sealed AIOC tree mismatch: expected {tree}, observed {observed_tree}",
            SEALED_PROOFS_PATH,
        )
        head = audit.git("rev-parse", "HEAD")
        if head:
            process = subprocess.run(
                ["git", "merge-base", "--is-ancestor", commit, head],
                cwd=audit.root,
                text=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,
                check=False,
            )
            audit.require(
                process.returncode == 0,
                "MVHEALTH-SEALED-ANCESTRY",
                f"sealed baseline {commit} is not an ancestor of {head}: {process.stdout.strip()}",
                SEALED_PROOFS_PATH,
            )
    rows = sealed.get("archived_validator_digests", [])
    manifest_paths: set[str] = set()
    for row in rows if isinstance(rows, list) else []:
        relative = row.get("path") if isinstance(row, dict) else None
        expected = row.get("sha256") if isinstance(row, dict) else None
        if not isinstance(relative, str) or not isinstance(expected, str):
            audit.fail(
                "MVHEALTH-SEALED-DIGEST-ROW",
                "invalid archived validator digest record",
                SEALED_PROOFS_PATH,
            )
            continue
        manifest_paths.add(relative)
        path = audit.root / relative
        if not path.is_file():
            audit.fail(
                "MVHEALTH-SEALED-FILE-MISSING",
                "sealed historical validator file is missing",
                relative,
            )
            continue
        blob = subprocess.run(
            ["git", "show", f"HEAD:{relative}"],
            cwd=audit.root,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            check=False,
        )
        if blob.returncode:
            audit.fail(
                "MVHEALTH-SEALED-GIT-BLOB",
                f"could not read canonical Git blob: {blob.stderr.decode('utf-8', errors='replace').strip()}",
                relative,
            )
            continue
        observed = hashlib.sha256(blob.stdout).hexdigest()
        audit.require(
            observed == expected,
            "MVHEALTH-SEALED-DIGEST",
            f"sealed historical validator digest drift: expected {expected}, observed {observed}",
            relative,
        )
    registered = set(
        validator_registry.get("repositories", {})
        .get("cybalicistjt-stack/multiversal-aioc", {})
        .get("historical_inert_exact_paths", [])
    )
    audit.require(
        bool(manifest_paths) and manifest_paths == registered,
        "MVHEALTH-SEALED-REGISTRY-COVERAGE",
        "sealed validator manifest and historical-inert registry differ",
        SEALED_PROOFS_PATH,
    )
    app_proof = sealed.get("application_family_proof", {})
    app_registry = (
        workflow_registry.get("repositories", {})
        .get("cybalicistjt-stack/Multiversal-app", {})
    )
    proof_workflows = set(app_proof.get("live_workflows", []))
    registered_workflows = {
        row.get("path")
        for row in app_registry.get("live_workflows", [])
        if isinstance(row, dict)
    }
    audit.require(
        app_proof.get("repository") == "cybalicistjt-stack/Multiversal-app"
        and isinstance(app_proof.get("active_family"), str)
        and bool(app_proof.get("active_family"))
        and isinstance(app_proof.get("sealed_through"), str)
        and _is_sha(app_proof.get("sealed_baseline"))
        and _is_sha(app_proof.get("family_scope_merge"))
        and app_proof.get("family_scope_merge") == app_registry.get("current_main")
        and proof_workflows == registered_workflows
        and app_proof.get("historical_predecessor_reruns_default") is False,
        "MVHEALTH-APP-SEALED-PROOF",
        "application family proof must agree with the workflow registry and retain sealed predecessor behavior",
        SEALED_PROOFS_PATH,
    )
    maintenance_proofs = sealed.get("control_plane_maintenance_proofs", [])
    audit.require(
        isinstance(maintenance_proofs, list) and bool(maintenance_proofs),
        "MVHEALTH-CONTROL-PLANE-PROOF-TYPE",
        "sealed control-plane maintenance proofs must be a non-empty array",
        SEALED_PROOFS_PATH,
    )
    pointer_records = {
        row.get("work_item_id"): row
        for row in pointer.get("recently_completed_repository_health_maintenance", [])
        if isinstance(row, dict) and isinstance(row.get("work_item_id"), str)
    }
    seen_work_items: set[str] = set()
    for proof in maintenance_proofs if isinstance(maintenance_proofs, list) else []:
        if not isinstance(proof, dict):
            audit.fail(
                "MVHEALTH-CONTROL-PLANE-PROOF-ROW",
                "sealed control-plane maintenance proof must be an object",
                SEALED_PROOFS_PATH,
            )
            continue
        work_item = proof.get("work_item")
        superseded = proof.get("superseded_prs_closed")
        valid = (
            isinstance(work_item, str)
            and bool(work_item)
            and work_item not in seen_work_items
            and proof.get("status") == "completed_verified"
            and isinstance(proof.get("application_pr"), int)
            and proof.get("application_pr") > 0
            and _is_sha(proof.get("application_merge"))
            and isinstance(proof.get("aioc_pr"), int)
            and proof.get("aioc_pr") > 0
            and _is_sha(proof.get("aioc_validated_head"))
            and isinstance(proof.get("aioc_repository_health_run"), int)
            and proof.get("aioc_repository_health_run") > 0
            and _is_sha(proof.get("aioc_merge"))
            and isinstance(proof.get("aioc_main_health_run"), int)
            and proof.get("aioc_main_health_run") > 0
            and isinstance(superseded, list)
            and all(isinstance(number, int) and number > 0 for number in superseded)
        )
        audit.require(
            valid,
            "MVHEALTH-CONTROL-PLANE-PROOF",
            f"invalid or duplicate sealed maintenance proof: {work_item!r}",
            SEALED_PROOFS_PATH,
        )
        if not isinstance(work_item, str):
            continue
        seen_work_items.add(work_item)
        pointer_record = pointer_records.get(work_item)
        audit.require(
            isinstance(pointer_record, dict)
            and pointer_record.get("status") == proof.get("status")
            and pointer_record.get("application_pr") == proof.get("application_pr")
            and pointer_record.get("application_merge")
            == proof.get("application_merge")
            and pointer_record.get("aioc_pr") == proof.get("aioc_pr")
            and pointer_record.get("aioc_validated_head")
            == proof.get("aioc_validated_head")
            and pointer_record.get("aioc_repository_health_run")
            == proof.get("aioc_repository_health_run")
            and pointer_record.get("aioc_merge") == proof.get("aioc_merge")
            and pointer_record.get("aioc_main_health_run")
            == proof.get("aioc_main_health_run")
            and pointer_record.get("superseded_prs_closed") == superseded,
            "MVHEALTH-CONTROL-PLANE-POINTER-PROOF",
            f"sealed maintenance proof disagrees with the pointer: {work_item}",
            SEALED_PROOFS_PATH,
        )
        if _is_sha(proof.get("aioc_merge")):
            process = subprocess.run(
                ["git", "merge-base", "--is-ancestor", proof["aioc_merge"], "HEAD"],
                cwd=audit.root,
                text=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,
                check=False,
            )
            audit.require(
                process.returncode == 0,
                "MVHEALTH-CONTROL-PLANE-ANCESTRY",
                f"maintenance merge is not an ancestor of HEAD: {work_item}",
                SEALED_PROOFS_PATH,
            )
    audit.require(
        seen_work_items == set(pointer_records),
        "MVHEALTH-CONTROL-PLANE-PROOF-COVERAGE",
        "sealed maintenance proof identities and pointer completion history differ",
        SEALED_PROOFS_PATH,
    )
    latest_proof = maintenance_proofs[0] if maintenance_proofs else {}
    return {
        "aioc_baseline": commit,
        "aioc_tree": tree,
        "historical_validator_digests": len(manifest_paths),
        "application_sealed_through": app_proof.get("sealed_through"),
        "application_family_scope_merge": app_proof.get("family_scope_merge"),
        "latest_control_plane_maintenance": latest_proof.get("work_item"),
        "latest_control_plane_maintenance_merge": latest_proof.get("aioc_merge"),
    }


def _validate_behavior_and_scorecard(audit: Audit) -> dict[str, Any]:
    try:
        termination = termination_self_test(audit.root)
    except (OSError, PreflightError) as exc:
        code = exc.code if isinstance(exc, PreflightError) else "MVHEALTH-TERMINATION-IO"
        audit.fail(code, str(exc), CURRENT_PREFLIGHT)
        termination = {"status": "FAIL", "cases_passed": 0}
    bootstrap = audit.read_text(Path("governance/ai/MULTIVERSAL_NEW_CONVERSATION_BOOTSTRAP.md"))
    agents = audit.read_text(Path("AGENTS.md"))
    for relative, text in (("AGENTS.md", agents), ("governance/ai/MULTIVERSAL_NEW_CONVERSATION_BOOTSTRAP.md", bootstrap)):
        for marker in (
            "execution_termination_preflight.py",
            "CONTINUE_EXECUTION",
            "ALLOW_FINAL_RESPONSE",
        ):
            audit.require(
                marker in text,
                "MVHEALTH-TERMINATION-INSTRUCTION",
                f"termination instruction surface missing marker {marker}",
                relative,
            )
    scorecard = audit.read_json(SCORECARD_PATH)
    targets = scorecard.get("targets", {})
    expected_targets = {
        "ordinary_tranche_single_continue_completion_percent_min": 80,
        "ordinary_tranche_completion_within_two_continues_percent_min": 95,
        "unrelated_historical_validation_jobs": 0,
        "reruns_without_changed_evidence": 0,
        "post_merge_stale_pointer_incidents": 0,
        "third_patch_rerun_without_new_diagnostic_evidence": 0,
    }
    audit.require(
        targets == expected_targets,
        "MVHEALTH-SCORECARD-TARGETS",
        "live execution-convergence targets drift",
        SCORECARD_PATH,
    )
    privacy = scorecard.get("privacy", {})
    audit.require(
        privacy.get("aggregation_only") is True
        and privacy.get("raw_private_transcript_text_published") is False,
        "MVHEALTH-SCORECARD-PRIVACY",
        "live scorecard privacy contract drift",
        SCORECARD_PATH,
    )
    return {
        "termination_preflight_status": termination.get("status"),
        "termination_cases_passed": termination.get("cases_passed"),
        "live_same_cycle_baseline_percent": scorecard.get("baseline", {}).get(
            "same_cycle_completion_percent"
        ),
        "single_continue_target_percent": 80,
        "two_continue_target_percent": 95,
    }


def _validate_cross_repository_app(
    audit: Audit, app_root: Path | None, workflow_registry: dict[str, Any]
) -> dict[str, Any] | None:
    if app_root is None:
        return None
    app_root = app_root.resolve()
    expected = (
        workflow_registry.get("repositories", {})
        .get("cybalicistjt-stack/Multiversal-app", {})
        .get("current_main")
    )
    observed = audit.git("rev-parse", "HEAD", cwd=app_root)
    audit.require(
        observed == expected,
        "MVHEALTH-APP-EXACT-HEAD",
        f"application checkout head mismatch: expected {expected}, observed {observed}",
        app_root,
    )
    workflow_dir = app_root / ".github/workflows"
    actual = {
        path.name
        for path in workflow_dir.iterdir()
        if path.is_file() and path.suffix in {".yml", ".yaml"}
    }
    audit.require(
        actual == EXPECTED_APP_WORKFLOWS,
        "MVHEALTH-APP-LIVE-NAMESPACE",
        f"application live workflow namespace drift: {sorted(actual)}",
        workflow_dir,
    )
    app_validator = app_root / "tools/validation_core/validate_repository_health_app.py"
    process = subprocess.run(
        [
            sys.executable,
            str(app_validator),
            "--root",
            str(app_root),
            "--expected-head",
            str(expected),
        ],
        cwd=app_root,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        check=False,
    )
    audit.require(
        process.returncode == 0,
        "MVHEALTH-APP-HEALTH",
        f"application repository health failed: {process.stdout.strip()}",
        app_validator,
    )
    return {
        "repository": "cybalicistjt-stack/Multiversal-app",
        "expected_head": expected,
        "observed_head": observed,
        "workflow_files": sorted(actual),
        "health_exit_code": process.returncode,
    }


def run_audit(
    root: Path, expected_head: str | None = None, app_root: Path | None = None
) -> dict[str, Any]:
    audit = Audit(root)
    observed_head = audit.git("rev-parse", "HEAD")
    if expected_head is not None:
        audit.require(
            _is_sha(expected_head),
            "MVHEALTH-EXPECTED-HEAD-FORMAT",
            f"invalid expected head: {expected_head!r}",
        )
        audit.require(
            observed_head == expected_head,
            "MVHEALTH-EXACT-HEAD",
            f"AIOC exact-head mismatch: expected {expected_head}, observed {observed_head}",
        )

    pointer = audit.read_json(POINTER_PATH)
    authority = audit.read_json(AUTHORITY_PATH)
    workflow_registry = audit.read_json(WORKFLOW_REGISTRY_PATH)
    validator_registry = audit.read_json(VALIDATOR_REGISTRY_PATH)
    runtime = audit.read_json(RUNTIME_REGISTRY_PATH)
    sealed = audit.read_json(SEALED_PROOFS_PATH)
    authority_summary = _validate_authority_and_pointer(
        audit, pointer, authority, runtime
    )
    workflow_summary = _validate_workflows(audit, workflow_registry)
    validator_summary = _validate_validators(audit, validator_registry)
    sealed_summary = _validate_sealed_proofs(
        audit, sealed, validator_registry, workflow_registry, pointer
    )
    behavior_summary = _validate_behavior_and_scorecard(audit)
    app_summary = _validate_cross_repository_app(audit, app_root, workflow_registry)

    return {
        "schema_version": "2.0.0",
        "validator": "scripts/validate_repository_health.py",
        "status": "FAIL" if audit.errors else "PASS",
        "repository": "cybalicistjt-stack/multiversal-aioc",
        "observed_head": observed_head,
        "expected_head": expected_head,
        "authority": authority_summary,
        "workflows": workflow_summary,
        "validators": validator_summary,
        "sealed_proofs": sealed_summary,
        "behavioral_execution": behavior_summary,
        "application": app_summary,
        "errors": audit.errors,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", default=".")
    parser.add_argument("--expected-head")
    parser.add_argument("--app-root")
    parser.add_argument("--output")
    args = parser.parse_args()
    result = run_audit(
        Path(args.root),
        expected_head=args.expected_head,
        app_root=Path(args.app_root) if args.app_root else None,
    )
    payload = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.output:
        Path(args.output).write_text(payload, encoding="utf-8")
    print(payload, end="")
    return 0 if result["status"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
