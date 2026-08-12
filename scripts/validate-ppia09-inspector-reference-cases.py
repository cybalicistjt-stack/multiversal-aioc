#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / "governance/application-planning/parallel-preimplementation"
MATRIX = BASE / "PPIA-09_INSPECTOR_ACTION_CONTRACT_MATRIX_v0.1.0.json"
SOLV = BASE / "PPIA-09_SOLVABILITY_UNCERTAINTY_AUTHORING_CONTRACT_v0.1.0.json"
CASES = BASE / "PPIA-09_REFERENCE_CASES_v0.1.0.json"
CANDIDATE = BASE / "PPIA-09_INSPECTOR_ACTION_REFERENCE_CANDIDATE.md"
TAXONOMY = BASE / "PPIA-09_INVESTIGATION_MYSTERY_TAXONOMY_v0.1.0.json"
AUTHORITY = BASE / "PPIA-09_AUTHORITY_AND_BOUNDARY_MATRIX_v0.1.0.json"
CHECKPOINT = ROOT / "governance/ai/work-state/PPIA-09-attempt-001.json"
POINTER = ROOT / "governance/ai/runtime/CURRENT_WORK_POINTER.json"
STATUS = ROOT / "governance/ai/runtime/CURRENT_IMPLEMENTATION_STATUS.json"
F011 = ROOT / "governance/application-planning/internal-alpha/feature-packets/MV-IA-F011_INVESTIGATION_AND_CLUE_BOARD.md"
F011_MATRIX = ROOT / "governance/application-planning/internal-alpha/feature-packets/MV-IA-F011_INVESTIGATION_CLUE_MATRIX.json"

FOUNDATION_MERGE = "511b7b3edc0b88ff8ea5683fd093d2853b50ccf1"
INSPECTOR_FINAL_HEAD = "844b9e100ea3fe9bbf009ef29764967173a331f5"
INSPECTOR_PR = 254
INSPECTOR_MERGE = "5768ce7864cac4e03e12a610c22d126797583599"
P9_COMPLETION_HEAD = "7393eac19d88eb5b2c58e44b51c1c3a2f3e2b968"
P9_COMPLETION_PR = 256
P9_COMPLETION_MERGE = "3996ca97a2e31fa89ce5c9d4101c96affb83ea71"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    for path in (MATRIX, SOLV, CASES, CANDIDATE, TAXONOMY, AUTHORITY, CHECKPOINT, POINTER, STATUS, F011, F011_MATRIX):
        require(path.exists(), f"missing {path.relative_to(ROOT)}")

    matrix = load(MATRIX)
    solv = load(SOLV)
    cases = load(CASES)
    taxonomy = load(TAXONOMY)
    authority = load(AUTHORITY)
    checkpoint = load(CHECKPOINT)
    pointer = load(POINTER)
    status = load(STATUS)
    f011_matrix = load(F011_MATRIX)
    candidate = CANDIDATE.read_text(encoding="utf-8").lower()
    f011 = F011.read_text(encoding="utf-8").lower()

    require(matrix["work_item"] == "PPIA-09" and matrix["version"] == "0.1.0", "wrong matrix identity/version")
    require(matrix["foundation_merge"] == FOUNDATION_MERGE, "foundation merge drifted")

    layers = [x["id"] for x in taxonomy["identity_state_layers"]]
    groups = matrix["projection_groups"]
    require(len(layers) == 16, "foundation taxonomy must retain sixteen semantic layers")
    require(len(groups) == 16, "inspector must contain sixteen projection groups")
    require([g["projection_group_id"] for g in groups] == [f"P9-PG-{i:03d}" for i in range(1, 17)], "projection group IDs must be contiguous")
    require([g["layer_id"] for g in groups] == layers, "projection groups must map one-to-one and in order to foundation layers")
    require(all(g["fields"] for g in groups), "every projection group needs fields")

    pp = matrix["projection_policy"]
    require(pp["server_side_filter_before_resolution_and_aggregation"] is True, "permission filtering must precede resolution/aggregation")
    require(pp["hidden_content_in_unauthorized_counts_search_or_diagnostics"] is False, "hidden content may not leak through counts/search/diagnostics")
    for key in ("confidence_is_truth_probability", "contradiction_auto_adjudicates_truth", "graph_layout_authoritative", "evidence_reference_transfers_ownership", "research_success_bypasses_permissions"):
        require(pp[key] is False, f"projection boundary drifted: {key}")

    annotation = matrix["annotation_contract"]
    require(annotation["status"] == "governed_ppia09_design_not_recovered_source_canon", "annotation authority label changed")
    require(annotation["dimensions"] == ["confidence", "relevance", "authenticity", "source-reliability"], "annotation dimensions changed")
    require(any("not objective truth probabilities" in x for x in annotation["rules"]), "confidence/truth separation missing")
    require(any("no universal numeric scale" in x.lower() for x in annotation["rules"]), "no-universal-scale guardrail missing")

    timeline = matrix["timeline_alibi_contract"]
    require(timeline["time_forms"] == ["exact", "bounded-window", "relative-before", "relative-after", "unknown"], "timeline forms changed")
    require("contradicted-by-record" in timeline["alibi_review_states"] and "unresolved" in timeline["alibi_review_states"], "alibi review states incomplete")

    contradiction = matrix["contradiction_contract"]
    require(len(contradiction["classifications"]) == 8, "expected eight contradiction classifications")
    require(len(contradiction["review_states"]) == 6, "expected six contradiction review states")
    require(any("never decide which source is true" in x.lower() for x in contradiction["rules"]), "contradiction truth guardrail missing")

    actions = matrix["action_contracts"]
    require(len(actions) == 30, "expected thirty governed actions")
    require([a["action_id"] for a in actions] == [f"P9-ACT-{i:03d}" for i in range(1, 31)], "action IDs must be contiguous")
    require(len({a["name"] for a in actions}) == 30, "action names must be unique")
    writes = [a for a in actions if a["mutation"] == "write"]
    reads = [a for a in actions if a["mutation"] == "read"]
    require(len(writes) == matrix["action_policy"]["authoritative_mutation_count"] == 22, "expected twenty-two authoritative mutations")
    require(len(reads) == matrix["action_policy"]["read_action_count"] == 8, "expected eight read actions")
    for action in writes:
        require("expected_version" in action["inputs"], f"{action['action_id']} missing expected_version")
        require("operation_id" in action["inputs"], f"{action['action_id']} missing operation_id")
    for key in ("player_hypothesis_mutates_truth", "contradiction_mutates_truth_automatically", "diagnostic_mutates_truth_or_reveal_state", "evidence_reference_transfers_source_ownership", "offline_authoritative_investigation_mutation_allowed"):
        require(matrix["action_policy"][key] is False, f"action boundary drifted: {key}")

    required_action_names = {
        "inspect_truth_solution", "run_solvability_diagnostics", "preview_reveal_audience", "author_truth_statement",
        "record_discovery_analysis", "record_observation", "record_claim", "attach_evidence_reference",
        "annotate_evidence_or_source_quality", "create_or_edit_hypothesis", "create_or_edit_connection",
        "author_timeline_entry", "author_alibi_claim", "author_contradiction_review",
        "set_false_lead_or_corruption_metadata", "author_revelation_dependency", "author_stall_recovery_clue",
        "reveal_withhold_or_revoke", "resolve_investigation_conclusion", "accept_generated_investigation_proposal"
    }
    require(required_action_names <= {a["name"] for a in actions}, "required Investigation action surface incomplete")

    require(solv["work_item"] == "PPIA-09", "wrong solvability contract work item")
    require(solv["solvability_diagnostic"]["status"] == "governed_ppia09_design_not_recovered_source_canon", "solvability design authority label changed")
    require(solv["uncertainty_contract"]["status"] == "governed_ppia09_design_not_recovered_source_canon", "uncertainty design authority label changed")
    require(solv["false_lead_and_corruption_diagnostic"]["status"] == "governed_ppia09_design_not_recovered_source_canon", "false-lead diagnostic authority label changed")
    require(solv["revelation_contract"]["requirement_classes"] == ["required", "optional", "bonus"], "revelation requirement classes changed")
    require("all-of" in solv["revelation_contract"]["dependency_kinds"] and "any-of" in solv["revelation_contract"]["dependency_kinds"], "revelation dependency kinds incomplete")
    require(any("at least two places" in x.lower() for x in solv["source_boundary"]["source_backed"]), "source redundancy guidance missing")
    require(any("universal required clue count" in x.lower() for x in solv["source_boundary"]["not_source_defined"]), "universal clue-count gap missing")
    require(any("fewer than two distinct routes produces an authoring warning" in x.lower() for x in solv["redundancy_contract"]["governed_interpretation"]), "redundancy warning rule missing")
    require(any("does not guarantee" in x.lower() for x in solv["redundancy_contract"]["governed_interpretation"]), "redundancy guarantee guardrail missing")
    require(any("never resolves" in x.lower() or "never resolve" in x.lower() for x in solv["solvability_diagnostic"]["deterministic_rules"]), "diagnostic non-resolution rule missing")
    require(any("not a universal fairness verdict" in x.lower() for x in solv["false_lead_and_corruption_diagnostic"]["rules"]), "false-lead fairness guardrail missing")

    require(f011_matrix["featureId"] == "MV-IA-F011", "wrong F011 fixture source")
    require(len(f011_matrix["records"]) == 10, "F011 ten-record model changed")
    require(len(f011_matrix["connectionTypes"]) == 15, "F011 fifteen connection predicates changed")
    require(len(f011_matrix["fixtures"]) == 24, "F011 fixture count changed")

    corpus = cases["cases"]
    require(cases["case_count"] == len(corpus) == 36, "reference corpus must contain thirty-six cases")
    require(cases["preserved_f011_fixture_count"] == 24, "preserved F011 fixture count changed")
    require([c["case_id"] for c in corpus] == [f"PPIA09-RC-{i:03d}" for i in range(1, 37)], "reference case IDs must be contiguous")
    require([c.get("preserved_f011_fixture_id") for c in corpus[:24]] == [f"INV-FX-{i:03d}" for i in range(1, 25)], "first twenty-four cases must preserve F011 fixtures one-to-one")
    require(all("preserved_f011_fixture_id" not in c for c in corpus[24:]), "new PPIA-09 cases may not masquerade as F011 fixtures")

    action_ids = {a["action_id"] for a in actions}
    group_ids = {g["projection_group_id"] for g in groups}
    covered_actions, covered_groups = set(), set()
    for case in corpus:
        require(case["scenario"] and case["expected"], f"{case['case_id']} missing scenario/expected")
        require(set(case["actions"]) <= action_ids, f"{case['case_id']} references unknown action")
        require(set(case["projection_groups"]) <= group_ids, f"{case['case_id']} references unknown projection group")
        covered_actions.update(case["actions"])
        covered_groups.update(case["projection_groups"])
    require(covered_actions == action_ids, f"action coverage gap: {sorted(action_ids - covered_actions)}")
    require(covered_groups == group_ids, f"projection coverage gap: {sorted(group_ids - covered_groups)}")

    case_titles = {c["title"] for c in corpus}
    for title in (
        "Private clue discovery", "Player hypothesis remains theory", "False lead without truth corruption",
        "Witness observation and claim", "Dr. Wen dossier projection integrity",
        "Important revelation single-route warning", "Important revelation has two independent routes",
        "Circular revelation dependency", "False lead with authored recovery route",
        "Misleading material is sole required route", "Timeline alibi contradiction review",
        "Research success cannot bypass reveal permission", "Hidden world timeline fact does not leak",
        "Dynamic extra clue retains provenance", "Cross-case correlation creates a lead, not truth"
    ):
        require(title in case_titles, f"missing required reference case: {title}")

    require(all(v is False for v in cases["policy"].values()), "reference-case policy guardrail drifted")

    for phrase in ("player deductions are not auto-promoted to fact", "spatial placement is presentation state", "false lead", "private clue", "idempotency", "nonvisual"):
        require(phrase in f011, f"F011 invariant missing {phrase!r}")
    require(len(authority["domain_handoffs"]) == 12, "foundation must retain twelve ownership handoffs")

    # Milestone continuity supports active inspector-candidate mode and immutable historical mode after merge/completion.
    require(checkpoint["work_item_id"] == "PPIA-09", "PPIA-09 checkpoint identity mismatch")
    require(checkpoint["branch"] == "governance/ppia-09-investigation-mystery-authoring", "PPIA-09 branch mismatch")
    require(checkpoint["owner_decision_required"] is False and checkpoint["unresolved_failures"] == [], "PPIA-09 checkpoint has unresolved state")
    require(checkpoint["status"] in {"started", "completed_verified"}, f"unexpected PPIA-09 checkpoint status {checkpoint['status']!r}")
    history = json.dumps({
        "last_verified_action": checkpoint.get("last_verified_action"),
        "completed_substeps": checkpoint.get("completed_substeps", []),
        "validation": checkpoint.get("validation", []),
        "evidence": checkpoint.get("evidence", []),
    }, ensure_ascii=False).lower()
    inspector_historical = all(value in history for value in (INSPECTOR_FINAL_HEAD.lower(), f"pr #{INSPECTOR_PR}", INSPECTOR_MERGE.lower()))
    if checkpoint["status"] == "started":
        if not inspector_historical:
            milestone_text = ((checkpoint.get("active_substep") or "") + " " + (checkpoint.get("next_action") or "")).lower()
            require("inspector" in milestone_text and "reference" in milestone_text and "solvability" in milestone_text, "checkpoint must remain on detailed inspector/reference milestone")
        require(pointer["primary_attempt_id"] == "PPIA-09-attempt-001", "active pointer must select PPIA-09")
        require(status["primary"]["work_item_id"] == "PPIA-09" and status["primary"]["status"] == "started", "active compact status must select started PPIA-09")
        continuity_mode = "active_ppia09"
    else:
        require(inspector_historical, "completed PPIA-09 must retain inspector head/PR/merge evidence")
        require(checkpoint.get("active_substep") is None and checkpoint.get("completed_at"), "completed PPIA-09 state invalid")
        require(checkpoint.get("latest_pushed_commit") == P9_COMPLETION_HEAD, "PPIA-09 completion head changed")
        require(checkpoint.get("pull_request") == P9_COMPLETION_PR and checkpoint.get("merge_commit") == P9_COMPLETION_MERGE, "PPIA-09 completion PR/merge changed")
        require(pointer.get("primary_attempt_id") != "PPIA-09-attempt-001" or status["primary"]["work_item_id"] == "PPIA-09", "historical pointer/status mismatch")
        continuity_mode = "historical_after_ppia09"

    for phrase in (
        "16 projection groups", "30 actions", "22 authoritative mutations", "36 deterministic cases",
        "24 f011 deterministic fixtures", "the vanishing of dr. wen", "at least two places",
        "no mandatory universal numeric probability scale", "contradiction", "stall recovery",
        "not ppia-09 complete", "no application runtime"
    ):
        require(phrase.lower() in candidate, f"candidate note missing phrase: {phrase}")

    print("PPIA-09 INSPECTOR / ACTION / REFERENCE CASES: PASS")
    print("projection_groups=16 actions=30 authoritative_mutations=22 read_actions=8")
    print("reference_cases=36 preserved_f011_fixtures=24 added_ppia09_cases=12")
    print("annotation_dimensions=4 contradiction_classes=8 revelation_classes=3")
    print("solvability=read_only redundancy_warning=source_grounded universal_clue_count=false")
    print("truth_auto_adjudication=false hidden_diagnostic_leak=false graph_layout_authority=false")
    print(f"continuity_mode={continuity_mode} runtime_activation=false")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
