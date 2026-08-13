#!/usr/bin/env python3
from __future__ import annotations

import json
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / "governance/application-planning/parallel-preimplementation"
P = lambda name: BASE / name
FILES = {
    "workflow": P("PPIA-16_INTEGRATED_SCREEN_WORKFLOW_CONTRACT_MATRIX_v0.1.0.json"),
    "trace": P("PPIA-16_INTEGRATED_SCREEN_WORKFLOW_TRACEABILITY_MATRIX_v0.1.0.json"),
    "cases": P("PPIA-16_INTEGRATED_SCREEN_WORKFLOW_REFERENCE_CASES_v0.1.0.json"),
    "index": P("PPIA-16_INTEGRATED_SCREEN_WORKFLOW_PACKAGE_INDEX_v0.1.0.json"),
    "candidate": P("PPIA-16_INTEGRATED_SCREEN_WORKFLOW_CANDIDATE.md"),
    "screens": P("PPIA-16_SCREEN_STATE_CONTRACTS_v0.1.0.json"),
    "actions": P("PPIA-16_ACTION_CONTRACTS_v0.1.0.json"),
    "components": P("PPIA-16_COMPONENT_INTERACTION_CONTRACTS_v0.1.0.json"),
    "predecessor_cases": P("PPIA-16_SCREEN_ACTION_REFERENCE_CASES_v0.1.0.json"),
    "foundation_inventory": P("PPIA-16_FOUNDATION_TOOLBELT_AND_AUTHORITY_INVENTORY_v0.1.0.json"),
    "foundation_authority": P("PPIA-16_FOUNDATION_AUTHORITY_AND_STATUS_MODEL_v0.1.0.json"),
    "foundation_coverage": P("PPIA-16_FOUNDATION_SCREEN_WORKFLOW_COVERAGE_MAP_v0.1.0.json"),
    "backlog": P("PPIA_PROGRAM_BACKLOG.json"),
}
CHECKPOINT = ROOT / "governance/ai/work-state/PPIA-16-attempt-001.json"
POINTER = ROOT / "governance/ai/runtime/CURRENT_WORK_POINTER.json"
STATUS = ROOT / "governance/ai/runtime/CURRENT_IMPLEMENTATION_STATUS.json"
BRANCH = "governance/ppia-16-developer-console-ai-team-control-surface"
APP_ANCHOR = "354e24007d2c453d090a2a6cdb31d3e3333c84c1"
FOUNDATION = ("8e0650fb9ab237ec3f1b1fe9152de42ee6f7c889", "31685859485", "31685859480", "67/67", "#291", "015f200595fd6e8ba5da85a2956ee1c9dc8fb15b")
SCREEN_ACTION = ("45e7e34b6bf7de0ca2ebff4b2818bdb1007f04c5", "31689903909", "68/68", "#292", "be811bd4508954700a83032b285107a8bd0d019a")
WORKFLOWS = [f"P16-WF-{i:03d}" for i in range(1, 13)]
SCREENS = {f"P16-SCR-{i:03d}" for i in range(1, 11)}
ACTIONS = {"ACT-OBSERVE","ACT-NAVIGATE","ACT-GENERATE","ACT-RUN-EVIDENCE","ACT-EXTERNAL-ADAPTER","ACT-PROPOSE-GOVERNED-MUTATION","ACT-EXECUTE-GOVERNED-MUTATION","ACT-OWNER-GATED"}
COMPONENTS = {f"P16-CMP-{i:03d}" for i in range(1, 9)}
TOOLS = {f"DT-{i:03d}" for i in range(1, 11)}
CONTROLS = {f"AIOC-CONTROL-{i:03d}" for i in range(1, 11)}
HANDOFFS = {f"P16-HO-{i:03d}" for i in range(1, 13)}
REFERENCE_CASES = [f"P16-RC-{i:03d}" for i in range(1, 49)]
INTEGRATED_CASES = [f"P16-IW-{i:03d}" for i in range(1, 13)]
AUTHORITY = {"canonical_repository_authority","active_attempt_repository_state","derived_repository_projection","tool_observation_or_evidence","generated_development_aid"}
REQUIREMENTS = {"current work/slice","scope authority","stop conditions","repository health","fixtures","scenarios","privacy scanning","UI evidence","design lint","traceability","recovery/performance","CI/evidence receipts","findings","Codex task capsules","proof exploration","interruption recovery"}
COUNTS = {"foundation_workflows":12,"screens":10,"action_classes":8,"components":8,"dt_tools":10,"aioc_control_surfaces":10,"program_requirements":16,"authority_layers":5,"handoffs":12,"predecessor_reference_cases":48,"new_integrated_cases":12,"effective_qa_cases":60}


def fail(message: str) -> None:
    text = "PPIA-16 INTEGRATED SCREEN/WORKFLOW TRACEABILITY: FAIL — " + message
    print("::error title=PPIA-16 Integrated Screen Workflow Validator::" + text.replace("\n", "%0A"))
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


def exact_once(actual: list[str], expected: list[str], label: str) -> None:
    counts = Counter(actual)
    req(set(counts) == set(expected) and all(v == 1 for v in counts.values()), f"{label} must cover the exact set once")


def main() -> None:
    d = {k: load(v) for k, v in FILES.items() if k != "candidate"}
    checkpoint, pointer, status = load(CHECKPOINT), load(POINTER), load(STATUS)
    workflow, trace, cases, index = d["workflow"], d["trace"], d["cases"], d["index"]
    candidate = FILES["candidate"].read_text(encoding="utf-8").lower()

    backlog = d["backlog"]
    req(backlog.get("current_work_item_id") == "PPIA-16", "PPIA-16 is not current")
    tranche = {x.get("work_item_id"): x for x in backlog.get("tranches", [])}.get("PPIA-16", {})
    req(tranche.get("status") in {"started","in_progress","ready_for_review"}, "PPIA-16 must remain unfinished")
    req(checkpoint.get("work_item_id") == "PPIA-16" and checkpoint.get("attempt_id") == "PPIA-16-attempt-001", "checkpoint identity changed")
    req(checkpoint.get("branch") == BRANCH and checkpoint.get("status") in {"started","in_progress","ready_for_review"}, "checkpoint branch/status changed")
    substep = (checkpoint.get("active_substep") or "").lower()
    req("integrated screen" in substep and "workflow traceability" in substep, "checkpoint does not select integrated traceability")
    req(checkpoint.get("owner_decision_required") is False and checkpoint.get("unresolved_failures") == [], "unexpected checkpoint blocker")
    req(checkpoint.get("roadmap_projection_pending") is True, "roadmap projection must remain pending")
    req(pointer.get("primary_attempt_id") == "PPIA-16-attempt-001", "pointer does not select PPIA-16")
    primary = status.get("primary", {})
    for field in ("work_item_id","attempt_id","branch","status","active_substep","next_action","latest_pushed_commit","pull_request","owner_decision_required","unresolved_failures","roadmap_projection_pending"):
        req(primary.get(field) == checkpoint.get(field), f"compact status mismatch: {field}")
    selected = [x for x in pointer.get("active_attempts", []) if x.get("owner_selected")]
    req(len(selected) == 1 and selected[0].get("work_item_id") == "PPIA-16", "owner-selected attempt changed")
    for field in ("attempt_id","branch","status","updated_at","roadmap_projection_pending"):
        req(selected[0].get(field) == checkpoint.get(field), f"pointer mismatch: {field}")

    history = json.dumps({"completed":checkpoint.get("completed_substeps",[]),"validation":checkpoint.get("validation",[]),"evidence":checkpoint.get("evidence",[]),"selection":pointer.get("selection_reason","")}, ensure_ascii=False).lower()
    for token in FOUNDATION + SCREEN_ACTION:
        req(token.lower() in history, f"immutable predecessor evidence missing {token}")
    for token in (APP_ANCHOR,"mv-dev v0.10.0","dt-001","dt-010"):
        req(token.lower() in history, f"toolbelt predecessor missing {token}")

    req({x.get("screen_id") for x in d["screens"].get("screens", [])} == SCREENS, "screen predecessor set changed")
    req({x.get("id") for x in d["actions"].get("actions", [])} == ACTIONS, "action predecessor set changed")
    req({x.get("id") for x in d["components"].get("components", [])} == COMPONENTS, "component predecessor set changed")
    predecessor = d["predecessor_cases"]
    rc_rows = predecessor.get("cases", [])
    req(predecessor.get("classification") == "synthetic_noncanonical_qa_reference_fixture" and predecessor.get("canonical") is False, "predecessor case class changed")
    req([x.get("id") for x in rc_rows] == REFERENCE_CASES, "predecessor reference IDs changed")
    req(Counter(x.get("workflow_id") for x in rc_rows) == Counter({wid:4 for wid in WORKFLOWS}), "predecessor reference distribution changed")
    req({x.get("id") for x in d["foundation_inventory"].get("toolbelt", [])} == TOOLS, "DT tool set changed")
    req({x.get("id") for x in d["foundation_inventory"].get("aioc_control_surfaces", [])} == CONTROLS, "AIOC control set changed")
    req({x.get("class") for x in d["foundation_authority"].get("authority_precedence", [])} == AUTHORITY, "authority classes changed")
    req({x.get("workflow_id") for x in d["foundation_coverage"].get("workflows", [])} == set(WORKFLOWS), "Foundation workflow set changed")
    req({x.get("requirement") for x in d["foundation_coverage"].get("program_requirement_coverage", [])} == REQUIREMENTS, "program requirement set changed")

    for doc in (workflow, trace, index):
        req(doc.get("work_item_id") == "PPIA-16" and doc.get("status") == "integrated-screen-workflow-candidate", "integrated artifact identity/status changed")
    req(workflow.get("classification") == "synthetic_noncanonical_qa_integrated_workflow_contracts" and workflow.get("canonical") is False, "workflow class changed")
    req(workflow.get("counts") == COUNTS and trace.get("counts") == COUNTS and index.get("locked_counts") == COUNTS, "locked counts changed")

    rows = workflow.get("workflows", [])
    req([x.get("workflow_id") for x in rows] == WORKFLOWS, "workflow IDs/order changed")
    by_wf = {x["workflow_id"]: x for x in rows}
    used = {"screens":set(),"actions":set(),"components":set(),"tools":set(),"controls":set(),"requirements":set(),"authority":set(),"handoffs":set()}
    all_rc, all_iw = [], []
    for i, row in enumerate(rows, 1):
        wid = f"P16-WF-{i:03d}"
        expected_rc = [f"P16-RC-{j:03d}" for j in range((i-1)*4+1, i*4+1)]
        req(row.get("predecessor_reference_case_ids") == expected_rc, f"{wid} predecessor cases changed")
        req(row.get("integrated_case_ids") == [f"P16-IW-{i:03d}"], f"{wid} integrated case changed")
        req(row.get("candidate_binding_required") is True, f"{wid} lost candidate binding")
        for field in ("screen_ids","action_ids","component_ids","aioc_control_surface_ids","program_requirements","authority_classes","handoff_ids","stop_condition_rule","recovery_rule","success_oracle","forbidden"):
            req(row.get(field) not in (None,[],{},""), f"{wid} missing {field}")
        req(set(row["screen_ids"]) <= SCREENS and set(row["action_ids"]) <= ACTIONS and set(row["component_ids"]) <= COMPONENTS, f"{wid} references unknown interaction contract")
        req(set(row.get("tool_ids", [])) <= TOOLS and set(row["aioc_control_surface_ids"]) <= CONTROLS, f"{wid} references unknown tool/control")
        req(set(row["program_requirements"]) <= REQUIREMENTS and set(row["authority_classes"]) <= AUTHORITY and set(row["handoff_ids"]) <= HANDOFFS, f"{wid} references unknown governed concern")
        all_rc += row["predecessor_reference_case_ids"]; all_iw += row["integrated_case_ids"]
        used["screens"] |= set(row["screen_ids"]); used["actions"] |= set(row["action_ids"]); used["components"] |= set(row["component_ids"])
        used["tools"] |= set(row.get("tool_ids", [])); used["controls"] |= set(row["aioc_control_surface_ids"]); used["requirements"] |= set(row["program_requirements"]); used["authority"] |= set(row["authority_classes"]); used["handoffs"] |= set(row["handoff_ids"])
    exact_once(all_rc, REFERENCE_CASES, "predecessor reference cases")
    exact_once(all_iw, INTEGRATED_CASES, "integrated cases")
    req(used == {"screens":SCREENS,"actions":ACTIONS,"components":COMPONENTS,"tools":TOOLS,"controls":CONTROLS,"requirements":REQUIREMENTS,"authority":AUTHORITY,"handoffs":HANDOFFS}, "integrated package contains orphaned concerns")

    handoffs = workflow.get("handoffs", [])
    req({x.get("id") for x in handoffs} == HANDOFFS, "handoff IDs changed")
    for row in handoffs:
        for field in ("name","from","to","owner","boundary","candidate_rule"):
            req(row.get(field) not in (None,[],{},""), f"{row.get('id')} missing {field}")

    trace_by = {x["workflow_id"]: x for x in trace.get("workflow_rows", [])}
    req(set(trace_by) == set(WORKFLOWS), "trace workflow set changed")
    fields = ("screen_ids","action_ids","component_ids","tool_ids","aioc_control_surface_ids","program_requirements","authority_classes","handoff_ids","predecessor_reference_case_ids","integrated_case_ids")
    for wid in WORKFLOWS:
        for field in fields:
            req(trace_by[wid].get(field, []) == by_wf[wid].get(field, []), f"{wid} trace mismatch {field}")
    reverse = [("screen_rows","screen_id",SCREENS,"screen_ids"),("action_rows","action_id",ACTIONS,"action_ids"),("component_rows","component_id",COMPONENTS,"component_ids"),("tool_rows","tool_id",TOOLS,"tool_ids"),("aioc_control_surface_rows","control_id",CONTROLS,"aioc_control_surface_ids"),("program_requirement_rows","requirement",REQUIREMENTS,"program_requirements"),("authority_rows","authority_class",AUTHORITY,"authority_classes"),("handoff_rows","handoff_id",HANDOFFS,"handoff_ids")]
    for rows_name, key, expected, wf_field in reverse:
        rrows = trace.get(rows_name, [])
        req({x.get(key) for x in rrows} == expected, f"{rows_name} set changed")
        for r in rrows:
            req(r.get("workflow_ids") == [wid for wid in WORKFLOWS if r[key] in by_wf[wid].get(wf_field, [])], f"{rows_name} reciprocal mapping changed for {r[key]}")
    req("no orphan" in trace.get("no_orphan_rule", "").lower() and "exactly once" in trace.get("no_orphan_rule", "").lower(), "no-orphan rule weakened")

    req(cases.get("classification") == "synthetic_noncanonical_qa_integrated_reference_cases" and cases.get("canonical") is False, "integrated cases lost synthetic noncanonical class")
    req(cases.get("counts") == {"new_integrated_cases":12,"inherited_screen_action_reference_cases":48,"effective_qa_cases":60}, "integrated case counts changed")
    iw_rows = cases.get("cases", [])
    req([x.get("id") for x in iw_rows] == INTEGRATED_CASES, "integrated case IDs changed")
    for i, case in enumerate(iw_rows, 1):
        wid = f"P16-WF-{i:03d}"
        req(case.get("workflow_id") == wid and case.get("predecessor_reference_case_ids") == by_wf[wid]["predecessor_reference_case_ids"], f"{case.get('id')} assignment changed")
        req(case.get("classification") == "synthetic_noncanonical_qa_integrated_reference_case" and case.get("canonical") is False, f"{case.get('id')} classification changed")
        for field in ("setup","sequence","authoritative_oracle","candidate_provenance_oracle","stop_recovery_oracle","accessibility_responsive_oracle","forbidden"):
            req(case.get(field) not in (None,[],{},""), f"{case.get('id')} missing {field}")

    policy = workflow.get("workflow_policy", {})
    for key in ("only_completed_verified_is_complete","authority_precedence_before_projection","raw_status_preserved","exact_candidate_binding_for_candidate_evidence","historical_evidence_remains_historical","stop_conditions_before_mutation","confirmation_does_not_create_authority"):
        req(policy.get(key) is True, f"policy weakened {key}")
    for key in ("ambiguous_mutation_blind_retry","generated_aid_is_governance_authority","tool_pass_is_work_item_completion","proven_is_work_item_completion","synthetic_tool_test_ui_is_product_evidence","reference_probe_is_product_recovery_proof","runtime_activation","stage_a_a2_activation","release","deployment","tester_access","paid_service","production_credentials","canonical_promotion"):
        req(policy.get(key) is False, f"boundary changed {key}")
    for doc in (workflow, trace, cases, index):
        req(doc.get("nonactivation") and all(v is False for v in doc["nonactivation"].values()), f"{doc.get('title')} nonactivation changed")

    predecessor_evidence = index.get("immutable_predecessor_evidence", {})
    req(predecessor_evidence.get("foundation", {}).get("merge") == FOUNDATION[-1] and predecessor_evidence.get("screen_action_reference", {}).get("merge") == SCREEN_ACTION[-1], "package predecessor merge evidence changed")
    req(index.get("next_milestone") == "PPIA-16 Completion Contract / Evidence Closure", "next milestone changed")
    req("does not by itself complete ppia-16" in index.get("completion_effect", "").lower(), "completion effect weakened")
    for phrase in ("60 effective","12/12","candidate","stale","raw","blind retry","all-green","completion contract","not ppia-16 completion"):
        req(phrase in candidate, f"narrative missing {phrase}")

    print("PPIA-16 INTEGRATED SCREEN/WORKFLOW TRACEABILITY: PASS")
    print("workflows=12 screens=10 actions=8 components=8 dt_tools=10 aioc_controls=10 requirements=16 authority_layers=5 handoffs=12")
    print("predecessor_reference_cases=48 assigned_exactly_once new_integrated_cases=12 effective_qa_cases=60 orphans=0")
    print("exact_candidate_binding=true stale_visible=true raw_status_preserved=true blind_retry=false")
    print("runtime_activation=false stage_a_a2=false release=false deployment=false tester_access=false owner_autoexecute=false")

if __name__ == "__main__":
    main()
