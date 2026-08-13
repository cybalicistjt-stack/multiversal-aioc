#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / "governance/application-planning/parallel-preimplementation"
INVENTORY = BASE / "PPIA-16_FOUNDATION_TOOLBELT_AND_AUTHORITY_INVENTORY_v0.1.0.json"
AUTHORITY = BASE / "PPIA-16_FOUNDATION_AUTHORITY_AND_STATUS_MODEL_v0.1.0.json"
IA = BASE / "PPIA-16_FOUNDATION_INFORMATION_ARCHITECTURE_v0.1.0.json"
COVERAGE = BASE / "PPIA-16_FOUNDATION_SCREEN_WORKFLOW_COVERAGE_MAP_v0.1.0.json"
NARRATIVE = BASE / "PPIA-16_FOUNDATION_EXISTING_TOOLBELT_AND_CONTROL_SURFACE_AUTHORITY_INVENTORY.md"
PACKAGE = BASE / "PPIA-16_FOUNDATION_PACKAGE_INDEX_v0.1.0.json"
BACKLOG = BASE / "PPIA_PROGRAM_BACKLOG.json"
PROGRAM = BASE / "PPIA_PARALLEL_PREIMPLEMENTATION_ADVANCEMENT_PROGRAM.md"
CHECKPOINT = ROOT / "governance/ai/work-state/PPIA-16-attempt-001.json"
POINTER = ROOT / "governance/ai/runtime/CURRENT_WORK_POINTER.json"
STATUS = ROOT / "governance/ai/runtime/CURRENT_IMPLEMENTATION_STATUS.json"

APP_ANCHOR = "354e24007d2c453d090a2a6cdb31d3e3333c84c1"
P16_BRANCH = "governance/ppia-16-developer-console-ai-team-control-surface"
DT_DOC_SHA = {
    "DT-001": ("docs/development/DT-001-developer-toolbelt.md", "ad015a00efdb594c9c1ae6599ab84b459faafed5"),
    "DT-002": ("docs/development/DT-002-a2-preflight.md", "82c29470c47806871f534f37b752e084a33a4ce9"),
    "DT-003": ("docs/development/DT-003-task-capsules.md", "b70060272998f7bc856ce997523ba6bd410cec95"),
    "DT-004": ("docs/development/DT-004-fixture-gateway.md", "fc63e79941ac3a353e40c8fb26a492c064f45ce2"),
    "DT-005": ("docs/development/DT-005-scenario-runner.md", "79c962daaff107f830f672826afc84b56441e754"),
    "DT-006": ("docs/development/DT-006-permission-leak-scanner.md", "c32d1674491b66a87390783eecc243f54e30efe4"),
    "DT-007": ("docs/development/DT-007-ui-evidence-harvester.md", "fd52662a3148a01670ef155791e7f37fd23f2ec9"),
    "DT-008": ("docs/development/DT-008-design-system-linter.md", "8e6329c59eade15c3faa34326aa90f544e455b79"),
    "DT-009": ("docs/development/DT-009-traceability-compiler.md", "a5d66b2ab75b0b00d5b8046c720a0a2a8b21da7f"),
    "DT-010": ("docs/development/DT-010-recovery-performance-harness.md", "29bb61ee85e60151570dc0a73bdeecff25eea7b6"),
}
PROGRAM_REQUIREMENTS = {
    "current work/slice",
    "scope authority",
    "stop conditions",
    "repository health",
    "fixtures",
    "scenarios",
    "privacy scanning",
    "UI evidence",
    "design lint",
    "traceability",
    "recovery/performance",
    "CI/evidence receipts",
    "findings",
    "Codex task capsules",
    "proof exploration",
    "interruption recovery",
}
ACTION_IDS = {
    "ACT-OBSERVE", "ACT-NAVIGATE", "ACT-GENERATE", "ACT-RUN-EVIDENCE",
    "ACT-EXTERNAL-ADAPTER", "ACT-PROPOSE-GOVERNED-MUTATION",
    "ACT-EXECUTE-GOVERNED-MUTATION", "ACT-OWNER-GATED",
}
RAW_STATES = {"PASS", "WARN", "FAIL", "BLOCK", "PREPARED", "READY_TO_EXECUTE", "UNDECLARED", "DECLARED", "PROVEN"}
PACKAGE_PATHS = {
    "governance/application-planning/parallel-preimplementation/PPIA-16_FOUNDATION_TOOLBELT_AND_AUTHORITY_INVENTORY_v0.1.0.json",
    "governance/application-planning/parallel-preimplementation/PPIA-16_FOUNDATION_AUTHORITY_AND_STATUS_MODEL_v0.1.0.json",
    "governance/application-planning/parallel-preimplementation/PPIA-16_FOUNDATION_INFORMATION_ARCHITECTURE_v0.1.0.json",
    "governance/application-planning/parallel-preimplementation/PPIA-16_FOUNDATION_SCREEN_WORKFLOW_COVERAGE_MAP_v0.1.0.json",
    "governance/application-planning/parallel-preimplementation/PPIA-16_FOUNDATION_EXISTING_TOOLBELT_AND_CONTROL_SURFACE_AUTHORITY_INVENTORY.md",
    "scripts/validate-ppia16-foundation.py",
    ".github/workflows/validate-ppia-16-foundation.yml",
}


def fail(message: str) -> None:
    text = "PPIA-16 FOUNDATION: FAIL — " + message
    print("::error title=PPIA-16 Foundation Validator::" + text.replace("\n", "%0A").replace("\r", "%0D"))
    raise SystemExit(text)


def req(condition: bool, message: str) -> None:
    if not condition:
        fail(message)


def load(path: Path) -> dict:
    req(path.exists(), f"missing {path.relative_to(ROOT)}")
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        fail(f"invalid JSON in {path.relative_to(ROOT)}: {exc}")


def text(path: Path) -> str:
    req(path.exists(), f"missing {path.relative_to(ROOT)}")
    return path.read_text(encoding="utf-8")


def main() -> None:
    inv = load(INVENTORY)
    authority = load(AUTHORITY)
    ia = load(IA)
    coverage = load(COVERAGE)
    package = load(PACKAGE)
    backlog = load(BACKLOG)
    checkpoint = load(CHECKPOINT)
    pointer = load(POINTER)
    status = load(STATUS)
    narrative = text(NARRATIVE).lower()
    program = text(PROGRAM).lower()

    # Current governed state.
    req(backlog.get("current_work_item_id") == "PPIA-16", "PPIA-16 is not current in backlog")
    tranches = {x.get("work_item_id"): x for x in backlog.get("tranches", [])}
    req(tranches.get("PPIA-16", {}).get("status") in {"started", "in_progress", "ready_for_review"}, "PPIA-16 backlog is not active")
    req(tranches.get("PPIA-16", {}).get("dependencies") == [], "PPIA-16 explicit dependencies changed")
    req("developer console / ai-team control surface" in tranches["PPIA-16"].get("title", "").lower(), "PPIA-16 title changed")
    req(checkpoint.get("work_item_id") == "PPIA-16" and checkpoint.get("attempt_id") == "PPIA-16-attempt-001", "checkpoint identity changed")
    req(checkpoint.get("branch") == P16_BRANCH, "checkpoint branch changed")
    req(checkpoint.get("status") in {"started", "in_progress", "ready_for_review"}, "checkpoint is not active")
    req("foundation" in (checkpoint.get("active_substep") or "").lower(), "checkpoint no longer points at Foundation")
    req(checkpoint.get("owner_decision_required") is False and checkpoint.get("unresolved_failures") == [], "Foundation has unresolved checkpoint state")
    req(pointer.get("primary_attempt_id") == "PPIA-16-attempt-001", "pointer does not select PPIA-16")
    primary = status.get("primary", {})
    req(primary.get("work_item_id") == "PPIA-16" and primary.get("attempt_id") == "PPIA-16-attempt-001", "compact status does not select PPIA-16")

    # Source inventory and immutable cross-repo provenance.
    req(inv.get("schema_version") == "1.0.0" and inv.get("work_item_id") == "PPIA-16", "inventory identity invalid")
    anchor = inv.get("application_source_anchor", {})
    req(anchor.get("repository") == "cybalicistjt-stack/Multiversal-app", "application source repository changed")
    req(anchor.get("commit") == APP_ANCHOR, "application source anchor changed")
    req(anchor.get("toolbelt_version") == "mv-dev v0.10.0", "toolbelt version changed")
    req(anchor.get("runtime_impact") == "none" and anchor.get("a2_activation") is False and anchor.get("release_deployment_authority") is False, "toolbelt anchor gained authority")
    tools = inv.get("toolbelt", [])
    req(len(tools) == 10, "expected exactly 10 DT tool entries")
    by_id = {x.get("id"): x for x in tools}
    req(set(by_id) == set(DT_DOC_SHA), "DT-001..DT-010 set changed")
    for dt, (doc_path, doc_sha) in DT_DOC_SHA.items():
        row = by_id[dt]
        req(row.get("doc_path") == doc_path and row.get("doc_blob_sha") == doc_sha, f"{dt} immutable documentation provenance changed")
        req(row.get("command_family"), f"{dt} missing command family")
        req(row.get("primary_outputs"), f"{dt} missing primary outputs")
        req(row.get("authority_class"), f"{dt} missing authority class")
        req(row.get("console_rule"), f"{dt} missing console rule")
    controls = inv.get("aioc_control_surfaces", [])
    req(len(controls) == 10, "expected exactly 10 AIOC control surfaces")
    req({x.get("id") for x in controls} == {f"AIOC-CONTROL-{i:03d}" for i in range(1, 11)}, "AIOC control-surface IDs changed")
    app_work = inv.get("application_work_authority", {})
    req(app_work.get("current_work_order_path") == ".ai/current-work-order.md", "application current-work authority path changed")
    req(app_work.get("ready_work_order_path") == ".ai/ready-work-orders/STAGE-A-A2-universal-object-experience.md", "A2 ready work-order path changed")
    req("implementation not yet started" in app_work.get("current_state", "").lower(), "Foundation must preserve A2 not-started state")
    req(app_work.get("release_deployment_authority") is False, "Foundation may not grant A2 release/deployment authority")
    staleness = inv.get("known_staleness", [])
    req(len(staleness) == 1 and "ppia-03" in json.dumps(staleness).lower(), "stale program current-tranche condition not recorded")
    req("ppia-16 — developer console / ai-team control surface" in program, "governing program missing PPIA-16 tranche definition")
    req("current tranche" in program and "ppia-03" in program, "expected stale historical current-tranche condition is no longer detectable; update Foundation disposition intentionally")
    nonauth_blob = json.dumps(inv.get("global_non_authorizations", [])).lower()
    for term in ("runtime", "a2", "release", "deployment", "tester", "paid", "credentials", "canonical"):
        req(term in nonauth_blob, f"global nonauthorization missing {term}")

    # Authority/status/action model.
    req(authority.get("work_item_id") == "PPIA-16", "authority model identity invalid")
    precedence = authority.get("authority_precedence", [])
    req([x.get("rank") for x in precedence] == [1, 2, 3, 4, 5], "authority precedence must contain ordered ranks 1..5")
    lifecycle = authority.get("work_lifecycle_states", {})
    req(lifecycle.get("complete_state") == "completed_verified", "only completed_verified may be complete")
    for unfinished in ("started", "in_progress", "validation_failed", "blocked_non_owner", "blocked_owner", "ready_for_review"):
        req(unfinished in lifecycle.get("unfinished_states", []), f"missing unfinished lifecycle state {unfinished}")
    raw = {x.get("raw") for x in authority.get("tool_result_semantics", [])}
    req(RAW_STATES <= raw, f"raw tool-result semantics incomplete: missing {sorted(RAW_STATES - raw)}")
    actions = authority.get("action_classes", [])
    req({x.get("id") for x in actions} == ACTION_IDS, "action-class set changed")
    receipt_fields = set(authority.get("evidence_receipt_minimum", {}).get("required_fields", []))
    for field in ("source_tool_or_workflow", "source_repository", "candidate_or_source_ref", "raw_result", "authoritative_mutation_performed", "authority_limitations"):
        req(field in receipt_fields, f"evidence receipt minimum missing {field}")
    finding = authority.get("finding_model", {})
    req(finding.get("raw_preservation") is True, "finding model must preserve raw severity/state")
    req("current blocker" in finding.get("current_blocker_rule", "").lower(), "finding model lost current-blocker binding rule")
    recovery_blob = json.dumps(authority.get("interruption_recovery_model", {})).lower()
    for term in ("current_work_pointer", "checkpoint", "branch", "open pr", "completion gate", "conversation"):
        req(term in recovery_blob, f"interruption recovery model missing {term}")

    # Information architecture.
    req(ia.get("work_item_id") == "PPIA-16", "IA identity invalid")
    screens = ia.get("screens", [])
    req(len(screens) == 10, "expected exactly 10 Foundation screens")
    req({x.get("screen_id") for x in screens} == {f"P16-SCR-{i:03d}" for i in range(1, 11)}, "Foundation screen IDs changed")
    screen_blob = json.dumps(screens).lower()
    for phrase in ("developer cockpit overview", "current work & scope authority", "repository health & preflight", "fixtures & scenario laboratory", "privacy & design quality", "ui evidence workspace", "traceability & proof explorer", "ci, evidence receipts & findings", "recovery & performance harness", "interruption recovery & ai-team handoff"):
        req(phrase in screen_blob, f"Foundation IA missing screen {phrase}")
    components = ia.get("cross_screen_components", [])
    req(len(components) == 8, "expected 8 cross-screen components")
    req({x.get("id") for x in components} == {f"P16-CMP-{i:03d}" for i in range(1, 9)}, "cross-screen component IDs changed")
    context_blob = json.dumps(ia.get("navigation", {})).lower()
    for term in ("repository", "branch/ref", "candidate sha", "work item", "authority badge", "nonactivation"):
        req(term in context_blob, f"persistent context/safety model missing {term}")
    req(len(ia.get("responsive_and_accessibility_foundation", {}).get("requirements", [])) >= 5, "responsive/accessibility Foundation is too thin")
    ia_nonauth = ia.get("nonactivation_boundary", "").lower()
    for term in ("runtime", "a2", "release", "deployment", "tester", "credentials", "paid", "canonical"):
        req(term in ia_nonauth, f"IA nonactivation boundary missing {term}")

    # Coverage and workflow completeness.
    req(coverage.get("work_item_id") == "PPIA-16", "coverage identity invalid")
    reqs = coverage.get("program_requirement_coverage", [])
    req(len(reqs) == 16, "expected 16 PPIA-16 program requirement rows")
    req({x.get("requirement") for x in reqs} == PROGRAM_REQUIREMENTS, "PPIA-16 program requirement coverage set changed")
    req(all(x.get("status") == "foundation-covered" and x.get("screens") and x.get("workflow_ids") for x in reqs), "every PPIA-16 program requirement must be screen/workflow covered")
    tool_cov = coverage.get("tool_coverage", [])
    req(len(tool_cov) == 10 and {x.get("tool_id") for x in tool_cov} == set(DT_DOC_SHA), "DT tool screen/workflow coverage incomplete")
    req(all(x.get("screens") and x.get("workflow_ids") for x in tool_cov), "every DT tool needs screen and workflow coverage")
    workflows = coverage.get("workflows", [])
    req(len(workflows) == 12, "expected exactly 12 Foundation workflows")
    req({x.get("workflow_id") for x in workflows} == {f"P16-WF-{i:03d}" for i in range(1, 13)}, "Foundation workflow IDs changed")
    req(all(x.get("steps") and x.get("success_oracle") and "mutation" in x for x in workflows), "workflow contract incomplete")
    counts = coverage.get("foundation_counts", {})
    req(counts == {"program_requirements": 16, "tool_ids": 10, "screens": 10, "workflows": 12, "cross_screen_components": 8}, "Foundation coverage counts changed")

    # Package and human-readable contract.
    req(package.get("work_item_id") == "PPIA-16", "package identity invalid")
    req(package.get("application_source_anchor") == f"cybalicistjt-stack/Multiversal-app@{APP_ANCHOR}", "package app anchor changed")
    artifact_paths = {x.get("path") for x in package.get("artifacts", [])}
    req(artifact_paths == PACKAGE_PATHS, "Foundation package path set changed")
    for path in PACKAGE_PATHS:
        req((ROOT / path).exists(), f"package artifact missing {path}")
    expected_counts = package.get("expected_counts", {})
    req(expected_counts.get("toolbelt_entries") == 10 and expected_counts.get("aioc_control_surfaces") == 10, "package source counts invalid")
    req(expected_counts.get("program_requirements") == 16 and expected_counts.get("screens") == 10 and expected_counts.get("workflows") == 12, "package design counts invalid")
    boundary_blob = json.dumps(package.get("required_boundaries", [])).lower()
    for phrase in ("only completed_verified is complete", "mentions are not proof", "synthetic ci images", "historical ci failures", "does not activate runtime"):
        req(phrase in boundary_blob, f"package boundary missing {phrase!r}")
    for phrase in ("dt-001 through dt-010", "ten semantic screens", "twelve end-to-end operator workflows", "only `completed_verified` is complete", "historical ci failures", "ppia-03", "screen states / action contracts / reference cases"):
        req(phrase in narrative, f"Foundation narrative missing {phrase!r}")

    print("PPIA-16 FOUNDATION: PASS")
    print(f"app_anchor={APP_ANCHOR} toolbelt=DT-001..DT-010 tool_entries={len(tools)} aioc_surfaces={len(controls)}")
    print(f"program_requirements={len(reqs)} screens={len(screens)} workflows={len(workflows)} components={len(components)}")
    print("authority_layers=5 action_classes=8 only_complete=completed_verified stale_program_current_tranche=recorded")
    print("runtime_activation=false a2_activation=false tester_access=false release=false deployment=false paid_services=false production_credentials=false")


if __name__ == "__main__":
    main()
