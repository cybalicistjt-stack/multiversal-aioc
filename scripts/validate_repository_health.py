#!/usr/bin/env python3
"""Deterministic Multiversal canonical-state health validator."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

AIOC_RUNTIME_ALLOWED = {
    "ACTIVE_AUTHORITY_REGISTRY.json",
    "CURRENT_WORK_POINTER.json",
    "INTERACTION_OPERATIONAL_SCORECARD.json",
    "OWNER_DECISION_2026-08-18_DEFER_CCTI12_T04_TO_SEPTEMBER.md",
    "ROADMAP_INDEX.json",
}
AIOC_WORKFLOWS_ALLOWED = {"validate-repository-health.yml"}
APP_WORKFLOWS_ALLOWED = {
    "_validation-core-profile.yml",
    "self-hosted-windows-runner-smoke.yml",
    "validate-repository-health.yml",
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


def check_gcl_foundation(root: Path) -> dict[str, Any]:
    gcl_dir = root / "governance/application-planning/gm-construction-library"
    backlog_path = gcl_dir / "GCL_PROGRAM_BACKLOG.json"
    taxonomy_path = gcl_dir / "GCL-01_CONSTRUCTION_TAXONOMY_v0.1.0.json"
    schema_path = gcl_dir / "GCL-01_TEMPLATE_GRAMMAR_SCHEMA_v0.1.0.json"
    composition_path = gcl_dir / "GCL-01_COMPOSITION_AND_INTERCHANGE_CONTRACT_v0.1.0.json"
    projection_path = gcl_dir / "GCL-01_PROJECTION_AND_AUTHORITY_CONTRACT_v0.1.0.json"
    fixtures_path = gcl_dir / "GCL-01_SYNTHETIC_GRAMMAR_FIXTURES_v0.1.0.json"
    inventory_path = gcl_dir / "GCL-01_SOURCE_AND_AUTHORITY_INVENTORY.md"
    checkpoint_path = root / "governance/ai/work-state/GCL-01-attempt-001.json"

    for path in [backlog_path, taxonomy_path, schema_path, composition_path, projection_path, fixtures_path, inventory_path, checkpoint_path]:
        require(path)

    backlog = read_json(backlog_path)
    taxonomy = read_json(taxonomy_path)
    schema = read_json(schema_path)
    composition = read_json(composition_path)
    projection = read_json(projection_path)
    fixtures = read_json(fixtures_path)
    checkpoint = read_json(checkpoint_path)

    assert backlog["program_id"] == "GCL"
    assert backlog["current_item"] == "GCL-01"
    assert backlog["current_item_status"] in {"in_progress", "completed_verified"}
    gcl01 = next(item for item in backlog["tranches"] if item["id"] == "GCL-01")
    assert gcl01["status"] in {"in_progress", "completed_verified"}
    assert checkpoint["work_item_id"] == "GCL-01"
    assert checkpoint["attempt_id"] == "GCL-01-attempt-001"
    assert checkpoint["status"] in {"in_progress", "completed_verified"}
    assert checkpoint["repository"] == "cybalicistjt-stack/multiversal-aioc"
    assert checkpoint["nonauthorization"], "GCL-01 must preserve explicit nonauthorization"

    expected_families = {
        "GCL-FAM-HOOK",
        "GCL-FAM-SITUATION",
        "GCL-FAM-ENCOUNTER",
        "GCL-FAM-OBJECTIVE",
        "GCL-FAM-COMPLICATION",
        "GCL-FAM-DIFFICULTY",
        "GCL-FAM-ADVERSARY",
        "GCL-FAM-MYSTERY",
        "GCL-FAM-ADVENTURE",
        "GCL-FAM-SESSION",
        "GCL-FAM-CAMPAIGN",
        "GCL-FAM-NPC",
        "GCL-FAM-CONSEQUENCE",
        "GCL-FAM-TRANSFORM",
        "GCL-FAM-DISCOVERY",
        "GCL-FAM-COMPOSITION",
    }
    family_ids = [item["id"] for item in taxonomy["template_families"]]
    assert len(family_ids) == len(set(family_ids)), "GCL family IDs must be unique"
    assert set(family_ids) == expected_families, "GCL taxonomy family coverage drift"
    assert set(schema["properties"]["family_id"]["enum"]) == expected_families

    required_template_fields = {
        "schema_version",
        "template_id",
        "template_version",
        "family_id",
        "lifecycle",
        "title",
        "summary",
        "authority",
        "discovery",
        "compatibility",
        "provenance",
        "slots",
        "structure",
        "projections",
        "composition",
    }
    assert required_template_fields.issubset(set(schema["required"]))
    authority_schema = schema["$defs"]["authority"]["properties"]
    assert authority_schema["runtime_authority"]["const"] == "none"
    assert authority_schema["requires_owning_domain_acceptance"]["const"] is True
    pressure_schema = schema["$defs"]["pressureLever"]["properties"]
    assert pressure_schema["guarantee"]["const"] is False

    manual_path = composition["composition_contract"]["deterministic_manual_path"]
    assert manual_path["required"] is True
    assert composition["composition_contract"]["ai_boundary"]["core_requires_ai"] is False
    interchange = composition["interchange_contract"]
    assert interchange["authority_declaration"]["default_import_authority"] == "proposal_only"
    assert interchange["conflict_policy"]["default"] == "preserve_and_surface"
    assert interchange["digest"]["algorithm"] == "sha256"
    assert "automatic canon promotion" in composition["composition_contract"]["operation_model"]["forbidden_implicit_operations"]

    projection_ids = {item["id"] for item in projection["projection_contracts"]}
    assert projection_ids == {"ready_to_use", "construction_material"}
    assert projection["single_record_rule"].startswith("Ready-to-use and construction-material views are projections of one versioned reusable template record")
    assert projection["projection_consistency"]["same_source_record_required"] is True
    assert projection["projection_consistency"]["authority_label_preserved"] is True
    assert projection["save_as_derived_record"]["automatic_promotion"] is False
    assert projection["ai_projection_boundary"]["proposal_only"] is True

    fixture_records = fixtures["fixtures"]
    assert fixtures["production_library_content"] is False
    assert len(fixture_records) >= 3
    fixture_ids: set[str] = set()
    fixture_families: set[str] = set()
    for fixture in fixture_records:
        assert required_template_fields.issubset(set(fixture)), f"fixture missing shared grammar fields: {fixture.get('template_id')}"
        assert fixture["lifecycle"] == "synthetic_fixture"
        assert fixture["provenance"]["record_origin"] == "synthetic_fixture"
        assert fixture["authority"]["runtime_authority"] == "none"
        assert fixture["authority"]["requires_owning_domain_acceptance"] is True
        assert fixture["family_id"] in expected_families
        assert fixture["template_id"] not in fixture_ids
        fixture_ids.add(fixture["template_id"])
        fixture_families.add(fixture["family_id"])
        assert fixture["projections"]["ready_to_use"]["include_unresolved_required_slots"] is True
        assert fixture["projections"]["construction_material"]["include_unresolved_required_slots"] is True
        assert fixture["composition"]["deterministic_manual_path"] is True
        assert fixture["composition"]["result_authority"] == "proposal_requires_owning_domain_acceptance"
        for lever in fixture["structure"]["difficulty_pressure_levers"]:
            assert lever["guarantee"] is False
            assert lever["factor_ref"].startswith("P11-F-")

    assert {"GCL-FAM-HOOK", "GCL-FAM-ENCOUNTER", "GCL-FAM-NPC"}.issubset(fixture_families)
    inventory_text = inventory_path.read_text(encoding="utf-8")
    for required_text in ["MV-IA-F005", "MV-IA-F012", "PPIA-11", "runtime/canon authority", "GCL-01 nonauthorization"]:
        assert required_text in inventory_text

    return {
        "gcl01_status": gcl01["status"],
        "families": len(family_ids),
        "fixture_records": len(fixture_records),
        "fixture_families": sorted(fixture_families),
        "manual_composition": True,
        "runtime_authority": "none",
        "universal_balance_guarantee": False,
    }


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
        selected_entries = [entry for entry in current_entries if entry.get("lifecycle") == "CURRENT"]
        kinds = [entry.get("kind") for entry in selected_entries]
        for singular in ["bootstrap", "work_pointer", "checkpoint", "program", "backlog", "roadmap"]:
            assert kinds.count(singular) == 1, f"authority registry must contain exactly one CURRENT {singular}"
        current_checkpoint = next(entry for entry in selected_entries if entry.get("kind") == "checkpoint")
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
        assert "repository: cybalicistjt-stack/Multiversal-app" not in workflow_text

        aioc_registry = workflow_registry["repositories"]["cybalicistjt-stack/multiversal-aioc"]
        registered_aioc = {Path(item["path"]).name for item in aioc_registry["live_workflows"]}
        assert registered_aioc == aioc_workflows
        health_entry = aioc_registry["live_workflows"][0]
        assert health_entry["execution"] == "github_hosted_linux_governance_exception"
        assert health_entry["timeout_minutes"] <= 5

        registered_aioc_validators = {item["path"] for item in validator_registry["repositories"]["cybalicistjt-stack/multiversal-aioc"]["current_validators"]}
        assert "scripts/validate_repository_health.py" in registered_aioc_validators
        assert audit["result"] == "zero_known_conflicting_authority"
        assert audit["known_conflicts"] == []

        gcl = check_gcl_foundation(root)
        result.update({
            "pointer_attempt": checkpoint["attempt_id"],
            "active_item": pointer["active_attempt"].get("active_item"),
            "crs_status": backlog["status"],
            "runtime_files": sorted(live_runtime),
            "workflow_files": sorted(aioc_workflows),
            "gcl": gcl,
        })
    except Exception as exc:
        errors.append(f"AIOC: {exc}")
    return result


def check_app(root: Path, audit: dict[str, Any], errors: list[str]) -> dict[str, Any]:
    result: dict[str, Any] = {}
    try:
        live_workflows = workflow_names(root)
        assert live_workflows == APP_WORKFLOWS_ALLOWED, f"App workflow namespace drift: {sorted(live_workflows)}"
        shared = (root / ".github/workflows/_validation-core-profile.yml").read_text(encoding="utf-8")
        assert "workflow_call" in shared and "self-hosted" in shared and "compare_receipts.py" in shared
        assert "ubuntu-latest" not in shared
        smoke = (root / ".github/workflows/self-hosted-windows-runner-smoke.yml").read_text(encoding="utf-8")
        assert "workflow_dispatch" in smoke and "ubuntu-latest" not in smoke
        health = (root / ".github/workflows/validate-repository-health.yml").read_text(encoding="utf-8")
        assert "multiversal-validation-linux" in health and "validate_repository_health_app.py" in health
        assert "ubuntu-latest" not in health

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
        "schema_version": "1.4.0",
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
