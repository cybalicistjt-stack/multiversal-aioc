#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path
from collections import Counter

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / "governance/application-planning/parallel-preimplementation"
FILES = {
    "foundation_cases": BASE / "PPIA-15_FOUNDATION_REFERENCE_CASES_v0.1.0.json",
    "foundation_gaps": BASE / "PPIA-15_COVERAGE_GAP_MATRIX_v0.1.0.json",
    "foundation_oracle": BASE / "PPIA-15_ORACLE_AND_FIXTURE_RULES_v0.1.0.json",
    "scenarios": BASE / "PPIA-15_EXPANDED_REGRESSION_SCENARIO_LIBRARY_v0.1.0.json",
    "projections": BASE / "PPIA-15_INSPECTOR_PROJECTION_CONTRACTS_v0.1.0.json",
    "actions": BASE / "PPIA-15_ACTION_AND_REFERENCE_CONTRACTS_v0.1.0.json",
    "cases": BASE / "PPIA-15_IAR_REFERENCE_CASES_v0.1.0.json",
    "trace": BASE / "PPIA-15_IAR_TRACEABILITY_MATRIX_v0.1.0.json",
    "package": BASE / "PPIA-15_IAR_PACKAGE_INDEX_v0.1.0.json",
}
README = BASE / "PPIA-15_EXPANDED_REGRESSION_IAR_README.md"
BACKLOG = BASE / "PPIA_PROGRAM_BACKLOG.json"
CHECKPOINT = ROOT / "governance/ai/work-state/PPIA-15-attempt-001.json"
POINTER = ROOT / "governance/ai/runtime/CURRENT_WORK_POINTER.json"
STATUS = ROOT / "governance/ai/runtime/CURRENT_IMPLEMENTATION_STATUS.json"
WORKFLOW = ROOT / ".github/workflows/validate-ppia-15-expanded-regression-iar.yml"


def fail(message: str) -> None:
    text = "PPIA-15 EXPANDED REGRESSION IAR: FAIL — " + message
    print("::error title=PPIA-15 Expanded Regression IAR Validator::" + text.replace("\n", "%0A").replace("\r", "%0D"))
    raise SystemExit(text)


def req(condition: bool, message: str) -> None:
    if not condition:
        fail(message)


def load(path: Path):
    req(path.exists(), f"missing {path.relative_to(ROOT)}")
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> None:
    docs = {k: load(v) for k, v in FILES.items()}
    backlog, checkpoint, pointer, status = map(load, (BACKLOG, CHECKPOINT, POINTER, STATUS))
    for path in (README, WORKFLOW):
        req(path.exists(), f"missing {path.relative_to(ROOT)}")

    for name in ("scenarios", "projections", "actions", "cases", "trace", "package"):
        doc = docs[name]
        req(doc.get("work_item_id") == "PPIA-15", f"{name} work item changed")
        req(doc.get("artifact_version") == "0.1.0", f"{name} artifact version changed")

    foundation = docs["foundation_cases"]
    req(foundation.get("case_count") == 32 and len(foundation.get("cases", [])) == 32, "Foundation 32-case baseline changed")
    req([x.get("id") for x in foundation.get("cases", [])] == [f"PPIA15-FC-{i:03d}" for i in range(1, 33)], "Foundation case IDs changed")
    req(foundation.get("classification") == "synthetic_noncanonical_qa_foundation_fixture" and foundation.get("canonical") is False, "Foundation fixture classification changed")

    gapdoc = docs["foundation_gaps"]
    rows = gapdoc.get("rows", [])
    req([x.get("awkward_id") for x in rows] == [f"P15-AWK-{i:03d}" for i in range(1, 19)], "Foundation awkward-family rows changed")
    counts = Counter(x.get("status") for x in rows)
    req(counts == Counter({"gap_direct": 7, "partial_awkward_variant": 10, "baseline_covered_no_clone": 1}), "Foundation 7/10/1 gap classification changed")
    gm_gap = next(x for x in rows if x.get("awkward_id") == "P15-AWK-004")
    req(gm_gap.get("status") == "baseline_covered_no_clone" and "do not clone" in gm_gap.get("foundation_disposition", "").lower(), "ordinary GM modification no-clone baseline changed")

    oracle = docs["foundation_oracle"]
    oracle_text = json.dumps(oracle, ensure_ascii=False).lower()
    for phrase in ("status-unknown is not failure", "offline/local state is not authoritative mutation", "silent last-write-wins is forbidden", "no balanced/fair/safe/winnable/optimal/guaranteed oracle"):
        req(phrase in oracle_text, f"Foundation oracle invariant missing {phrase!r}")
    req(all(v is False for v in oracle.get("nonactivation", {}).values()), "Foundation nonactivation boundary changed")

    scenarios = docs["scenarios"]
    scenario_rows = scenarios.get("scenario_contracts", [])
    req(scenarios.get("scenario_count") == 24 and len(scenario_rows) == 24, "24 stable scenario contracts changed")
    req([x.get("id") for x in scenario_rows] == [f"P15-SCN-{i:03d}" for i in range(1, 25)], "scenario IDs changed")
    allowed_awkward = {f"P15-AWK-{i:03d}" for i in range(1, 19)}
    scenario_ids = {x.get("id") for x in scenario_rows}
    covered = set()
    for row in scenario_rows:
        awk = set(row.get("awkward_family_ids", []))
        req(awk and awk <= allowed_awkward, f"invalid awkward-family binding in {row.get('id')}")
        covered |= awk
        for field in ("nearest_inherited_anchors", "foundation_case_ids", "material_differential", "governing_domains", "actor_role", "context", "channel", "device_profile", "interaction_mode", "accessibility_modes", "connection_state", "fixture_id", "operation", "expected_authoritative_outcome", "projection_group_id", "action_ids", "expected_recovery_or_conflict", "provenance", "forbidden_outcomes"):
            req(row.get(field), f"{row.get('id')} missing {field}")
    req(covered == allowed_awkward, "scenario library does not cover all 18 required awkward families")
    guard = scenarios.get("protected_nonclone_baseline", {})
    req(guard.get("awkward_family_id") == "P15-AWK-004" and "not cloned" in guard.get("rule", "").lower(), "GM modification protected no-clone guard missing")
    sg = scenarios.get("source_gap_guard", {})
    req(sg.get("foundation_case_id") == "PPIA15-FC-032" and sg.get("provenance") == "P15-PV-004" and "F024" in sg.get("source_gap", ""), "F024 source-gap guard changed")
    req("invented" not in sg.get("expected", "").lower(), "source-gap expected result improperly invents behavior")
    req(all(v is False for v in scenarios.get("nonactivation", {}).values()), "scenario library activation boundary changed")

    projections = docs["projections"]
    pg_rows = projections.get("projection_groups", [])
    req(projections.get("projection_group_count") == 12 and len(pg_rows) == 12, "12 Inspector projection groups changed")
    req([x.get("id") for x in pg_rows] == [f"P15-PG-{i:03d}" for i in range(1, 13)], "projection-group IDs changed")
    projection_ids = {x.get("id") for x in pg_rows}
    req(all(x.get("semantic_nonvisual_parity") is True for x in pg_rows), "Inspector semantic nonvisual parity changed")
    pg_text = json.dumps(projections, ensure_ascii=False).lower()
    for phrase in ("hidden and missing remain externally equivalent", "case-local scale fixture sizes", "never create mutation"):
        req(phrase in pg_text, f"Inspector global rule missing {phrase!r}")

    actions = docs["actions"]
    action_rows = actions.get("actions", [])
    req(actions.get("action_count") == 20 and len(action_rows) == 20, "20 action/reference contracts changed")
    req([x.get("id") for x in action_rows] == [f"P15-ACT-{i:03d}" for i in range(1, 21)], "action IDs changed")
    action_ids = {x.get("id") for x in action_rows}
    req(all(x.get("ppia15_mutates_authoritative_state") is False for x in action_rows), "PPIA-15 action contract gained mutation authority")
    action_text = json.dumps(actions, ensure_ascii=False).lower()
    for phrase in ("not new application commands or mutation authority", "status-unknown never becomes permission to retry blindly", "f024 as unsupported"):
        req(phrase in action_text, f"action safety rule missing {phrase!r}")
    req(all(v is False for v in actions.get("nonactivation", {}).values()), "action nonactivation boundary changed")

    for row in scenario_rows:
        req(row.get("projection_group_id") in projection_ids, f"{row.get('id')} references unknown projection")
        req(set(row.get("action_ids", [])) <= action_ids, f"{row.get('id')} references unknown action")

    trace = docs["trace"]
    family_rows = trace.get("family_rows", [])
    req([x.get("awkward_id") for x in family_rows] == [f"P15-AWK-{i:03d}" for i in range(1, 19)], "traceability family IDs changed")
    for row in family_rows:
        req(set(row.get("scenario_ids", [])) <= scenario_ids and row.get("scenario_ids"), f"trace row {row.get('awkward_id')} missing scenario")
        req(set(row.get("projection_groups", [])) <= projection_ids and row.get("projection_groups"), f"trace row {row.get('awkward_id')} missing projection")
        req(set(row.get("actions", [])) <= action_ids and row.get("actions"), f"trace row {row.get('awkward_id')} missing actions")
    summary = trace.get("coverage_summary", {})
    req((summary.get("required_awkward_families"), summary.get("stable_scenario_contracts"), summary.get("projection_groups"), summary.get("action_contracts"), summary.get("ordinary_gm_modification_clone_count")) == (18, 24, 12, 20, 0), "traceability locked counts changed")
    source_gap_row = trace.get("source_gap_row", {})
    req(source_gap_row.get("gap_id") == "P15-GAP-001" and source_gap_row.get("foundation_case_id") == "PPIA15-FC-032" and source_gap_row.get("closure") == "open-not-invented", "traceability F024 gap changed")

    cases = docs["cases"]
    case_rows = cases.get("cases", [])
    req(cases.get("case_count") == 40 and cases.get("effective_case_count_with_foundation") == 72 and len(case_rows) == 40, "40 IAR / 72 effective case accounting changed")
    req([x.get("id") for x in case_rows] == [f"P15-IAR-{i:03d}" for i in range(1, 41)], "IAR case IDs changed")
    for row in case_rows:
        req(row.get("scenario_id") in scenario_ids, f"{row.get('id')} references unknown scenario")
        req(row.get("projection_group_id") in projection_ids, f"{row.get('id')} references unknown projection")
        req(set(row.get("action_ids", [])) <= action_ids and row.get("action_ids"), f"{row.get('id')} references unknown action")
        for field in ("variant", "authoritative_class", "projection_class", "recovery_class", "forbidden"):
            req(row.get(field), f"{row.get('id')} missing {field}")
    f024_case = next(x for x in case_rows if x.get("id") == "P15-IAR-040")
    req(f024_case.get("provenance") == "P15-PV-004" and "F024" in f024_case.get("source_gap", "") and f024_case.get("authoritative_class") == "indeterminate-blocked-source-gap", "IAR F024 source-gap case changed")
    req(all(v is True for k, v in cases.get("global_requirements", {}).items() if k in {"permission_filter_before_derivatives","hidden_missing_equivalence_when_existence_protected","status_unknown_not_failure","accepted_event_distinct_from_projection","offline_local_not_authoritative","semantic_nonvisual_parity","synthetic_noncanonical"}), "IAR safety requirements changed")
    req(all(cases.get("global_requirements", {}).get(k) is False for k in ("runtime_activation", "tester_access", "release", "deployment", "canonical_promotion")), "IAR activation boundary changed")

    package = docs["package"]
    req([x.get("id") for x in package.get("package_artifacts", [])] == [f"P15-IAR-PKG-{i:03d}" for i in range(1, 9)], "eight IAR package-index IDs changed")
    locked = package.get("locked_counts", {})
    req((locked.get("foundation_cases"), locked.get("stable_scenario_contracts"), locked.get("required_awkward_families"), locked.get("projection_groups"), locked.get("action_contracts"), locked.get("new_iar_cases"), locked.get("effective_cases"), locked.get("ordinary_gm_modification_clones"), locked.get("open_f024_source_gaps")) == (32, 24, 18, 12, 20, 40, 72, 0, 1), "package locked counts changed")
    immutable = package.get("immutable_foundation_evidence", {})
    req((immutable.get("exact_validated_head"), immutable.get("hosted_workflows"), immutable.get("dedicated_run"), immutable.get("pull_request"), immutable.get("merge"), immutable.get("merge_signature")) == ("d876093989e656d3cf8366c19755295ef0f785e8", "62/62", "31652241636", 286, "a1f6b7380a07e65469ba8072e8aa4135d7b1e42f", "verified valid"), "immutable Foundation evidence changed")
    acceptance = package.get("acceptance", {})
    for k in ("all_18_awkward_families_traced", "ordinary_gm_modification_not_cloned", "every_scenario_has_material_differential", "every_scenario_has_foundation_or_inherited_anchor", "every_scenario_binds_projection_and_action_contracts", "source_gap_f024_remains_open", "synthetic_noncanonical_only", "foundation_only_not_ppia15_completion"):
        req(acceptance.get(k) is True, f"package acceptance changed: {k}")
    for k in ("application_runtime_activation", "stage_a_a2_activation", "tester_access_activation", "release_activation", "deployment_activation", "paid_service_activation", "production_credentials_activation", "canonical_promotion"):
        req(acceptance.get(k) is False, f"package activation changed: {k}")
    req(package.get("next_milestone") == "PPIA-15 Integrated Expanded Regression Workflows / Traceability", "next milestone changed")

    readme = README.read_text(encoding="utf-8").lower()
    for phrase in ("24 stable expanded regression scenario contracts", "12 inspector projection groups", "20 action/reference contracts", "40 new synthetic noncanonical iar cases", "72 effective ppia-15 cases", "ordinary gm modification remains a protected inherited baseline", "p15-gap-001", "not ppia-15 completion", "integrated expanded regression workflows / traceability"):
        req(phrase in readme, f"IAR README missing {phrase!r}")

    tranches = {x.get("work_item_id"): x for x in backlog.get("tranches", [])}
    for dep in ("PPIA-09", "PPIA-10", "PPIA-11", "PPIA-14"):
        req(tranches.get(dep, {}).get("status") == "completed_verified", f"{dep} dependency not completed_verified")
    req(backlog.get("current_work_item_id") == "PPIA-15" and tranches.get("PPIA-15", {}).get("status") in {"started", "ready_for_review"}, "PPIA-15 current backlog state changed")
    req(checkpoint.get("attempt_id") == "PPIA-15-attempt-001" and checkpoint.get("branch") == "governance/ppia-15-internal-alpha-test-content-expansion", "PPIA-15 checkpoint identity changed")
    req(checkpoint.get("status") in {"started", "ready_for_review"} and checkpoint.get("completed_at") is None, "IAR milestone cannot complete PPIA-15")
    req("Expanded Regression Scenario Library" in (checkpoint.get("active_substep") or ""), "checkpoint active substep does not select IAR milestone")
    req(pointer.get("primary_attempt_id") == "PPIA-15-attempt-001", "current pointer does not select PPIA-15")
    req(status.get("primary", {}).get("work_item_id") == "PPIA-15" and status.get("primary", {}).get("status") in {"started", "ready_for_review"}, "compact status does not select active PPIA-15")
    req(checkpoint.get("unresolved_failures") == [] and checkpoint.get("owner_decision_required") is False, "PPIA-15 unresolved state changed")

    boundaries = backlog.get("boundaries", {})
    for k in ("application_runtime_mutation_authorized", "a2_activation_authorized", "release_authorized", "deployment_authorized", "tester_access_authorized", "canonical_promotion_without_source_evidence_authorized"):
        req(boundaries.get(k) is False, f"program boundary changed: {k}")

    print("PPIA-15 EXPANDED REGRESSION IAR: PASS")
    print("scenarios=24 awkward_families=18 projections=12 actions=20 new_iar_cases=40 effective_cases=72")
    print("gm_baseline_clones=0 f024_gap=open-not-invented synthetic_noncanonical=true")
    print("permission_filter=true hidden_missing_equivalence=true status_unknown_not_failure=true")
    print("runtime_activation=false a2_activation=false tester_access=false release=false deployment=false")


if __name__ == "__main__":
    main()
