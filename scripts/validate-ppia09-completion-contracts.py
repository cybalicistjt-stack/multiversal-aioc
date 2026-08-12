#!/usr/bin/env python3
from __future__ import annotations

import json
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / "governance/application-planning/parallel-preimplementation"
SPEC = BASE / "PPIA-09_INVESTIGATION_MYSTERY_AUTHORING_EXPERIENCE_SPEC_v1.0.0.md"
ACCEPTANCE = BASE / "PPIA-09_ACCEPTANCE_TRACEABILITY_MATRIX_v1.0.0.json"
REPORT = BASE / "PPIA-09_COMPLETION_REPORT.md"
SOURCE = BASE / "PPIA-09_SOURCE_MANIFEST_v0.1.0.json"
TAXONOMY = BASE / "PPIA-09_INVESTIGATION_MYSTERY_TAXONOMY_v0.1.0.json"
AUTHORITY = BASE / "PPIA-09_AUTHORITY_AND_BOUNDARY_MATRIX_v0.1.0.json"
INSPECTOR = BASE / "PPIA-09_INSPECTOR_ACTION_CONTRACT_MATRIX_v0.1.0.json"
SOLVABILITY = BASE / "PPIA-09_SOLVABILITY_UNCERTAINTY_AUTHORING_CONTRACT_v0.1.0.json"
CASES = BASE / "PPIA-09_REFERENCE_CASES_v0.1.0.json"
WORKFLOWS = BASE / "PPIA-09_WORKFLOW_AUTHORING_CONTRACT_MATRIX_v0.1.0.json"
TRACE = BASE / "PPIA-09_WORKFLOW_TRACEABILITY_MATRIX_v0.1.0.json"
BACKLOG = BASE / "PPIA_PROGRAM_BACKLOG.json"
CHECKPOINT = ROOT / "governance/ai/work-state/PPIA-09-attempt-001.json"
POINTER = ROOT / "governance/ai/runtime/CURRENT_WORK_POINTER.json"
STATUS = ROOT / "governance/ai/runtime/CURRENT_IMPLEMENTATION_STATUS.json"
F011_MATRIX = ROOT / "governance/application-planning/internal-alpha/feature-packets/MV-IA-F011_INVESTIGATION_CLUE_MATRIX.json"

FOUNDATION_HEAD = "e4999c40e1fe92852c142789b3d70596dfad52a8"
FOUNDATION_MERGE = "511b7b3edc0b88ff8ea5683fd093d2853b50ccf1"
INSPECTOR_HEAD = "844b9e100ea3fe9bbf009ef29764967173a331f5"
INSPECTOR_MERGE = "5768ce7864cac4e03e12a610c22d126797583599"
WORKFLOW_HEAD = "32e4d6ff560966eed9aab4fca57236ae6f992e79"
WORKFLOW_MERGE = "02e359606087d88f19b3dd4cfe504a934cc8ede0"


def fail(message: str) -> None:
    raise SystemExit(f"PPIA-09 COMPLETION CONTRACT: FAIL — {message}")


def require(condition: bool, message: str) -> None:
    if not condition:
        fail(message)


def load(path: Path) -> dict:
    require(path.exists(), f"missing {path.relative_to(ROOT)}")
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> None:
    for path in (SPEC, REPORT):
        require(path.exists(), f"missing {path.relative_to(ROOT)}")
    spec = SPEC.read_text(encoding="utf-8")
    report = REPORT.read_text(encoding="utf-8")
    acceptance = load(ACCEPTANCE)
    source = load(SOURCE)
    taxonomy = load(TAXONOMY)
    authority = load(AUTHORITY)
    inspector = load(INSPECTOR)
    solvability = load(SOLVABILITY)
    cases_doc = load(CASES)
    workflows_doc = load(WORKFLOWS)
    trace = load(TRACE)
    backlog = load(BACKLOG)
    checkpoint = load(CHECKPOINT)
    pointer = load(POINTER)
    status = load(STATUS)
    f011 = load(F011_MATRIX)

    # Retained source boundary.
    require(source.get("work_item_id") == "PPIA-09", "source manifest work item changed")
    require(source.get("direct_pdf_totals") == {"files": 3, "pages": 53}, "direct PDF boundary must remain 3 files / 53 pages")
    require(all(x.get("visual_review_complete") is True for x in source.get("direct_pdf_sources", [])), "direct PDFs must remain visually reviewed")
    require(source.get("structured_support_totals") == {"files": 4, "rows": 4936, "bounded_keyword_hit_rows": 1570}, "structured source totals changed")
    abilities = next(x for x in source.get("structured_support_sources", []) if x.get("path", "").endswith("Abilities_Core.csv"))
    require(abilities.get("explicit_investigation_knowledge_tree_rows") == 109, "explicit Investigation/Knowledge row count changed")
    require(len(source.get("source_backed_findings", [])) == 14, "source-backed finding count changed")
    require(len(source.get("explicit_source_gaps", [])) == 10, "explicit source-gap count changed")
    require(all(v is False for v in source.get("non_assumptions", {}).values()), "source non-assumptions must remain false")

    # F011 and semantic model.
    require(f011.get("featureId") == "MV-IA-F011", "wrong F011 matrix")
    require(len(f011.get("records", [])) == 10, "F011 record-family count changed")
    require(len(f011.get("connectionTypes", [])) == 15, "F011 connection predicate count changed")
    require(len(f011.get("fixtures", [])) == 24, "F011 fixture count changed")
    layers = taxonomy.get("identity_state_layers", [])
    profiles = taxonomy.get("presentation_profiles", [])
    require(len(layers) == 16 and len({x.get("id") for x in layers}) == 16, "expected sixteen unique semantic layers")
    require(len(profiles) == 12 and len(set(profiles)) == 12, "expected twelve presentation profiles")
    require(all(v is False for v in taxonomy.get("foundation_non_assumptions", {}).values()), "foundation non-assumptions must remain false")

    # Ownership and inspector/action contract.
    handoffs = authority.get("domain_handoffs", [])
    require(len(handoffs) == 12, "expected twelve domain handoffs")
    require([x.get("id") for x in handoffs] == [f"P9-HO-{n:03d}" for n in range(1, 13)], "handoff IDs changed")
    groups = inspector.get("projection_groups", [])
    actions = inspector.get("action_contracts", [])
    require([x.get("projection_group_id") for x in groups] == [f"P9-PG-{n:03d}" for n in range(1, 17)], "projection groups changed")
    require([x.get("action_id") for x in actions] == [f"P9-ACT-{n:03d}" for n in range(1, 31)], "action IDs changed")
    writes = [a for a in actions if a.get("mutation") == "write"]
    reads = [a for a in actions if a.get("mutation") == "read"]
    require(len(writes) == 22 and len(reads) == 8, "expected 22 authoritative mutations / 8 reads")
    for action in writes:
        require("expected_version" in action.get("inputs", []), f"{action['action_id']} missing expected_version")
        require("operation_id" in action.get("inputs", []), f"{action['action_id']} missing operation_id")
    projection_policy = inspector.get("projection_policy", {})
    require(projection_policy.get("server_side_filter_before_resolution_and_aggregation") is True, "permission filtering must precede derivatives")
    for key in ("confidence_is_truth_probability", "contradiction_auto_adjudicates_truth", "graph_layout_authoritative", "evidence_reference_transfers_ownership", "research_success_bypasses_permissions"):
        require(projection_policy.get(key) is False, f"projection boundary changed: {key}")

    # Solvability/uncertainty boundaries.
    require(solvability.get("work_item") == "PPIA-09", "wrong solvability work item")
    require(solvability.get("revelation_contract", {}).get("requirement_classes") == ["required", "optional", "bonus"], "revelation classes changed")
    source_boundary = " ".join(solvability.get("source_boundary", {}).get("source_backed", [])).lower()
    require("at least two places" in source_boundary, "source-grounded redundancy guidance missing")
    gap_boundary = " ".join(solvability.get("source_boundary", {}).get("not_source_defined", [])).lower()
    require("universal required clue count" in gap_boundary, "universal clue-count gap missing")
    require(any("never resolves" in x.lower() or "never resolve" in x.lower() for x in solvability.get("solvability_diagnostic", {}).get("deterministic_rules", [])), "read-only non-resolution diagnostic boundary missing")

    # Reference cases and workflows.
    cases = cases_doc.get("cases", [])
    expected_cases = [f"PPIA09-RC-{n:03d}" for n in range(1, 37)]
    require(cases_doc.get("case_count") == 36 and [x.get("case_id") for x in cases] == expected_cases, "reference cases must remain PPIA09-RC-001..036")
    require(cases_doc.get("preserved_f011_fixture_count") == 24, "preserved F011 fixture count changed")
    workflows = workflows_doc.get("workflows", [])
    require(len(workflows) == 18 and [x.get("workflow_id") for x in workflows] == [f"P9-WF-{n:03d}" for n in range(1, 19)], "workflows must remain P9-WF-001..018")
    require(trace.get("workflow_count") == 18 and trace.get("authoritative_mutation_workflow_count") == 15 and trace.get("read_only_workflow_count") == 3, "workflow trace counts changed")
    coverage_summary = trace.get("coverage_summary", {})
    expected_trace_counts = {"projection_groups": 16, "presentation_profiles": 12, "actions": 30, "reference_cases": 36, "handoffs": 12}
    for key, count in expected_trace_counts.items():
        require(coverage_summary.get(key, {}).get("expected") == count and coverage_summary.get(key, {}).get("covered") == count and coverage_summary.get(key, {}).get("gaps") == 0, f"workflow trace gap/count changed: {key}")
    require(len(trace.get("end_to_end_assertions", [])) == 12, "expected twelve end-to-end workflow assertions")

    # Final 48/16 acceptance contract.
    require(acceptance.get("format") == "multiversal-ppia09-investigation-mystery-authoring-acceptance-traceability-matrix", "wrong acceptance format")
    reqs = acceptance.get("requirements", [])
    require(len(reqs) == 48, "final acceptance matrix must contain 48 requirements")
    require([r.get("requirement_id") for r in reqs] == [f"PPIA09-AC-{n:03d}" for n in range(1, 49)], "acceptance IDs must be contiguous 001..048")
    categories = Counter(r.get("category") for r in reqs)
    require(len(categories) == 16 and all(v == 3 for v in categories.values()), "expected sixteen acceptance categories with three requirements each")
    require(set(categories) == {x.get("id") for x in layers}, "acceptance categories must map one-to-one to semantic layers")
    require(all(r.get("blocking") is True and r.get("traces") and r.get("reference_cases") for r in reqs), "every final requirement must be blocking and traced")
    require({c for r in reqs for c in r.get("reference_cases", [])} == set(expected_cases), "acceptance requirements must collectively exercise all 36 reference cases")
    coverage = acceptance.get("coverage", {})
    require(coverage.get("traceability_gap_count") == 0, "final traceability gap count must be zero")
    sets = coverage.get("sets", {})
    expected_counts = {"semantic_layers":16,"presentation_profiles":12,"projection_groups":16,"actions":30,"reference_cases":36,"workflows":18,"handoffs":12}
    for key, count in expected_counts.items():
        require(sets.get(key, {}).get("count") == count, f"final acceptance count changed: {key}")
    require(sets.get("actions", {}).get("authoritative_mutations") == 22 and sets.get("actions", {}).get("read_actions") == 8, "final action split changed")
    require(sets.get("workflows", {}).get("authoritative_mutations") == 15 and sets.get("workflows", {}).get("read_only") == 3, "final workflow split changed")
    require(coverage.get("source_boundary") == {"direct_pdfs":3,"direct_pdf_pages":53,"structured_support_files":4,"structured_rows":4936,"explicit_investigation_knowledge_tree_rows":109}, "final source coverage summary changed")
    diag = coverage.get("diagnostic_contract", {})
    require(diag == {"solvability_read_only":True,"redundancy_warning_source_grounded":True,"universal_clue_count":False,"automatic_truth_adjudication":False,"false_lead_fairness_threshold":False}, "final diagnostic summary changed")
    policy = acceptance.get("blocking_policy", {})
    require(policy.get("permission_filter_before_resolution_and_aggregation") is True, "final permission policy changed")
    for key, value in policy.items():
        if key != "permission_filter_before_resolution_and_aggregation":
            require(value is False, f"blocking policy must keep {key}=false")

    # Human-readable final specification/report.
    for phrase in (
        "3 directly relevant PDFs / 53 visually reviewed pages", "4 structured support CSVs / 4,936 rows", "109 explicit Investigation/Knowledge ability-tree rows",
        "10 record families, 15 typed connection predicates, and 24 deterministic fixtures", "The Vanishing of Dr. Wen", "16 semantic identity/state layers", "12 presentation profiles",
        "30 governed actions", "22 authoritative mutations", "8 read actions", "36 contiguous reference cases", "18 end-to-end Investigation/Mystery workflows",
        "15 perform authoritative mutation", "3 are read-only", "at least two places", "expected_version", "operation_id", "permission filtering",
        "PPIA-12-owned", "semantic nonvisual", "proposal-only", "48 requirements across 16 categories", "STAGE-A-A2 activation authorized: **No**"
    ):
        require(phrase.lower() in spec.lower(), f"final spec missing {phrase!r}")
    for phrase in (
        "COMPLETION CANDIDATE — NOT COMPLETE UNTIL THIS EXACT HEAD PASSES REQUIRED VALIDATION AND MERGES",
        FOUNDATION_HEAD, FOUNDATION_MERGE, INSPECTOR_HEAD, INSPECTOR_MERGE, WORKFLOW_HEAD, WORKFLOW_MERGE,
        "48 blocking acceptance requirements across 16 categories", "PPIA-09→PPIA-10 transition"
    ):
        require(phrase in report, f"completion report missing {phrase!r}")

    # Dual-mode continuity: strict candidate while active; immutable evidence after verified completion.
    tranches = {x.get("work_item_id"): x for x in backlog.get("tranches", [])}
    require("PPIA-09" in tranches, "PPIA-09 missing from backlog")
    cp_status = checkpoint.get("status")
    require(cp_status in {"started", "completed_verified"}, f"unexpected PPIA-09 checkpoint status {cp_status!r}")
    require(checkpoint.get("attempt_id") == "PPIA-09-attempt-001" and checkpoint.get("branch") == "governance/ppia-09-investigation-mystery-authoring", "checkpoint identity changed")
    require(checkpoint.get("unresolved_failures") == [] and checkpoint.get("owner_decision_required") is False, "checkpoint has unresolved state")
    history = json.dumps({"last_verified_action": checkpoint.get("last_verified_action"), "completed_substeps": checkpoint.get("completed_substeps", []), "validation": checkpoint.get("validation", []), "evidence": checkpoint.get("evidence", [])}, ensure_ascii=False)
    for value in (FOUNDATION_HEAD, FOUNDATION_MERGE, INSPECTOR_HEAD, INSPECTOR_MERGE, WORKFLOW_HEAD, WORKFLOW_MERGE):
        require(value in history, f"immutable milestone evidence missing {value}")
    if cp_status == "started":
        require(backlog.get("current_work_item_id") == "PPIA-09" and tranches["PPIA-09"].get("status") == "started", "active completion candidate must keep PPIA-09 selected/started")
        require(pointer.get("primary_attempt_id") == "PPIA-09-attempt-001", "active pointer must select PPIA-09")
        require(status.get("primary", {}).get("work_item_id") == "PPIA-09" and status.get("primary", {}).get("status") == "started", "compact status must select started PPIA-09")
        require(status.get("primary", {}).get("active_substep") == checkpoint.get("active_substep"), "compact active_substep must exactly project checkpoint")
        combined = ((checkpoint.get("active_substep") or "") + " " + (checkpoint.get("next_action") or "")).lower()
        require("completion" in combined and "v1.0.0" in combined and "acceptance" in combined, "active checkpoint must identify final completion package")
    else:
        require(tranches["PPIA-09"].get("status") == "completed_verified", "completed checkpoint requires completed_verified backlog tranche")
        require(checkpoint.get("completed_at"), "completed checkpoint requires completed_at")
        require(isinstance(checkpoint.get("pull_request"), int) and checkpoint.get("pull_request") > 0, "completed checkpoint requires completion PR")
        require(isinstance(checkpoint.get("merge_commit"), str) and len(checkpoint.get("merge_commit")) == 40, "completed checkpoint requires completion merge SHA")
        require(isinstance(checkpoint.get("latest_pushed_commit"), str) and len(checkpoint.get("latest_pushed_commit")) == 40, "completed checkpoint requires final validated head")
        require("Validate PPIA-09 Completion Contract" in history, "completed checkpoint must retain completion-gate evidence")
        require(str(checkpoint.get("pull_request")) in history and checkpoint.get("merge_commit") in history and checkpoint.get("latest_pushed_commit") in history, "completed checkpoint must retain final head/PR/merge evidence")

    print("PPIA-09 COMPLETION CONTRACT: PASS")
    print("source_pdfs=3 source_pages=53 structured_files=4 structured_rows=4936 investigation_knowledge_rows=109")
    print("semantic_layers=16 presentation_profiles=12 projection_groups=16 handoffs=12")
    print("actions=30 authoritative_mutations=22 reads=8 reference_cases=36 f011_preserved=24")
    print("workflows=18 mutation_workflows=15 read_only_workflows=3")
    print("acceptance_requirements=48 acceptance_categories=16 traceability_gaps=0")
    print("universal_clue_count=false auto_truth_adjudication=false diagnostic_mutation=false ai_proposal_only=true")
    print(f"checkpoint_status={cp_status} runtime_activation=false")


if __name__ == "__main__":
    main()
