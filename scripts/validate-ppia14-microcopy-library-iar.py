#!/usr/bin/env python3
from __future__ import annotations
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
BASE=ROOT/"governance/application-planning/parallel-preimplementation"
P=lambda n: BASE/n
FILES={
 "library":P("PPIA-14_MICROCOPY_LIBRARY_v0.1.0.json"),
 "inspector":P("PPIA-14_MICROCOPY_INSPECTOR_CONTRACT_v0.1.0.json"),
 "actions":P("PPIA-14_MICROCOPY_ACTION_CONTRACT_MATRIX_v0.1.0.json"),
 "cases":P("PPIA-14_MICROCOPY_REFERENCE_CASES_v0.1.0.json"),
 "index":P("PPIA-14_MICROCOPY_LIBRARY_PACKAGE_INDEX_v0.1.0.json"),
 "candidate":P("PPIA-14_MICROCOPY_LIBRARY_INSPECTOR_ACTION_REFERENCE_CANDIDATE.md"),
 "taxonomy":P("PPIA-14_MESSAGE_STATE_TAXONOMY_v0.1.0.json"),
 "affordances":P("PPIA-14_SAFE_AFFORDANCE_CLASSES_v0.1.0.json"),
 "actors":P("PPIA-14_ACTOR_CONTEXT_AND_DELIVERY_MATRIX_v0.1.0.json"),
 "a11y":P("PPIA-14_ACCESSIBILITY_MOBILE_NONVISUAL_LOCALIZATION_REQUIREMENTS_v0.1.0.json"),
 "gaps":P("PPIA-14_SOURCE_GAPS_v0.1.0.json"),
 "foundation_cases":P("PPIA-14_FOUNDATION_REFERENCE_CASES_v0.1.0.json"),
}
CHECKPOINT=ROOT/"governance/ai/work-state/PPIA-14-attempt-001.json"
POINTER=ROOT/"governance/ai/runtime/CURRENT_WORK_POINTER.json"
STATUS=ROOT/"governance/ai/runtime/CURRENT_IMPLEMENTATION_STATUS.json"
BACKLOG=P("PPIA_PROGRAM_BACKLOG.json")

def fail(msg): raise SystemExit("PPIA-14 MICROCOPY LIBRARY IAR: FAIL — "+msg)
def require(c,msg):
    if not c: fail(msg)
def load(p):
    require(p.exists(),f"missing {p.relative_to(ROOT)}")
    return json.loads(p.read_text(encoding="utf-8"))

def main():
    library=load(FILES["library"]); inspector=load(FILES["inspector"]); actions=load(FILES["actions"]); cases=load(FILES["cases"]); index=load(FILES["index"])
    taxonomy=load(FILES["taxonomy"]); affordances=load(FILES["affordances"]); actors=load(FILES["actors"]); a11y=load(FILES["a11y"]); gaps=load(FILES["gaps"]); foundation_cases=load(FILES["foundation_cases"])
    checkpoint=load(CHECKPOINT); pointer=load(POINTER); status=load(STATUS); backlog=load(BACKLOG); candidate=FILES["candidate"].read_text(encoding="utf-8")

    require(len(taxonomy["message_states"])==18,"Foundation message-state count changed")
    require([x["id"] for x in taxonomy["message_states"]]==[f"P14-MS-{i:03d}" for i in range(1,19)],"Foundation message-state IDs changed")
    require(len(affordances["affordance_classes"])==13,"Foundation affordance count changed")
    require(len(actors["role_profiles"])==9 and len(actors["help_contexts"])==20,"Foundation role/context counts changed")
    for k,v in a11y["accessibility_requirements"].items(): require(v is True,f"Foundation accessibility requirement {k} changed")

    msgs=library["message_objects"]
    require(len(msgs)==18,"message object count mismatch")
    require([x["id"] for x in msgs]==[f"P14-MSG-{i:03d}" for i in range(1,19)],"message IDs unstable")
    require([x["message_state_id"] for x in msgs]==[f"P14-MS-{i:03d}" for i in range(1,19)],"message/state mapping must be one-to-one")
    required={"semantic_intent_key","title_key","body_key","default_en","severity_semantic","disclosure_class","allowed_interpolation_keys","primary_action_class","secondary_action_classes","nonvisual_status_key","default_en_nonvisual","pluralization_policy","support_reference_policy"}
    for m in msgs:
        require(required.issubset(m),f"{m['id']} missing required fields")
        require(bool(m["default_en"]["title"]) and bool(m["default_en"]["body"]) and bool(m["default_en_nonvisual"]),f"{m['id']} copy incomplete")
        require(set(m["allowed_interpolation_keys"]).issubset({"visible_field_label","safe_reason"}),f"{m['id']} unsafe interpolation key")
    m2,m3=msgs[1],msgs[2]
    require(m2["default_en"]==m3["default_en"] and m2["default_en_nonvisual"]==m3["default_en_nonvisual"],"hidden and safe-unavailable must be externally equivalent")
    require("collapse" in m3.get("render_rule","").lower(),"hidden state must explicitly collapse to safe-unavailable")
    require(msgs[8]["semantic_intent_key"].endswith("status-unknown"),"status-unknown message identity changed")
    require("check its status" in msgs[8]["default_en"]["body"].lower(),"status-unknown must direct status lookup")
    require("recorded" in msgs[9]["default_en"]["body"].lower() and "caught up" in msgs[9]["default_en"]["body"].lower(),"accepted Event/projection lag copy changed")
    require("source-gap fact" in msgs[17].get("render_rule","").lower() and "p14-msg-002" in msgs[17].get("render_rule","").lower(),"source-gap disclosure/fallback rule changed")
    gp=library["global_copy_rules"]
    for k in ("hidden_missing_equivalence","status_unknown_is_not_failure","accepted_event_is_distinct_from_projection","offline_local_state_is_not_authoritative_mutation","blind_ambiguous_mutation_retry_forbidden"):
        require(gp[k] is True,f"global copy invariant {k} changed")
    for k in ("copy_grants_authority","copy_changes_gameplay_or_canonical_truth","f024_behavior_invented","required_recovery_transient_only"):
        require(gp[k] is False,f"global copy boundary {k} changed")

    require(len(inspector["projection_groups"])==12,"projection group count mismatch")
    require([x["id"] for x in inspector["projection_groups"]]==[f"P14-PG-{i:03d}" for i in range(1,13)],"projection group IDs unstable")
    ip=inspector["projection_policy"]
    for k in ("permission_filter_before_message_discovery","permission_filter_before_actions","permission_filter_before_interpolation","permission_filter_before_diagnostics_support","hidden_missing_equivalence_required","nonvisual_semantic_parity_required"):
        require(ip[k] is True,f"Inspector policy {k} changed")
    for k in ("raw_internal_diagnostics_visible","hidden_counts_visible","copy_can_override_authority","ai_decision_authority"):
        require(ip[k] is False,f"Inspector may not enable {k}")

    require(actions["counts"]=={"actions":20,"mutating_presentations":2,"nonmutating_presentations":18},"action counts changed")
    require([x["id"] for x in actions["actions"]]==[f"P14-ACT-{i:03d}" for i in range(1,21)],"action IDs unstable")
    muts=[x for x in actions["actions"] if x["may_mutate_upstream"]]
    require([x["key"] for x in muts]==["retry-idempotent-operation","report-issue-redacted"],"mutating presentation set changed")
    proto=actions["upstream_mutation_protocol"]
    require(proto["authority"]=="upstream-only","PPIA-14 must not own mutation authority")
    for x in ("operation_id","governing_operation_contract"): require(x in proto["required_for_mutating_presentations"],f"mutation protocol missing {x}")
    for phrase in ("status lookup","idempotent","offline","f025"):
        require(phrase in json.dumps(actions).lower(),f"action contract missing {phrase!r}")

    require(cases["counts"]=={"new_cases":40,"inherited_foundation_cases":32,"effective_cases":72},"case counts changed")
    require(len(cases["cases"])==40 and len(foundation_cases["cases"])==32,"actual case counts changed")
    require([x["id"] for x in cases["cases"]]==[f"P14-IAR-{i:03d}" for i in range(1,41)],"case IDs unstable")
    require({x["message_state_id"] for x in cases["cases"]}=={f"P14-MS-{i:03d}" for i in range(1,19)},"all 18 message states require deterministic coverage")
    require(all(x["permissionFilterRequired"] and x["nonvisualRequired"] for x in cases["cases"]),"every case requires permission filtering/nonvisual parity")
    case_text=json.dumps(cases).lower()
    for phrase in ("hidden deep link","blind retry","accepted event","f024 gap","screen-reader","mobile single-focus","keyboard conflict"):
        require(phrase in case_text,f"case corpus missing {phrase!r}")

    require(index["counts"]=={"message_objects":18,"projection_groups":12,"actions":20,"new_reference_cases":40,"effective_reference_cases":72},"package index counts changed")
    low=candidate.lower()
    for phrase in ("18 stable message objects","12 permission-safe projection groups","20 action presentations","72 effective deterministic cases","hidden-vs-missing","status-unknown","accepted durable event","p14-gap-001","f024","ppia-14 integrated error recovery permission workflows / traceability","application runtime"):
        require(phrase in low,f"candidate narrative missing {phrase!r}")

    require(checkpoint["work_item_id"]=="PPIA-14","PPIA-14 checkpoint identity changed")
    require(checkpoint["owner_decision_required"] is False and checkpoint["unresolved_failures"]==[],"PPIA-14 unresolved state changed")
    current_id=backlog["current_work_item_id"]
    if current_id=="PPIA-14":
        require(checkpoint["status"] in {"started","ready_for_review"},"active PPIA-14 checkpoint must remain active")
        selected=[x for x in pointer["active_attempts"] if x.get("owner_selected")]
        require(len(selected)==1 and selected[0]["work_item_id"]=="PPIA-14" and status["primary"]["work_item_id"]=="PPIA-14","runtime continuity must select PPIA-14")
        continuity_mode="active_ppia14"
    else:
        order=backlog["execution_order"]
        require(current_id in order and order.index(current_id)>order.index("PPIA-14"),"historical Microcopy IAR validation may only occur after PPIA-14")
        tranches={x["work_item_id"]:x for x in backlog["tranches"]}
        require(tranches["PPIA-14"]["status"]=="completed_verified","historical PPIA-14 backlog must be completed_verified")
        require(checkpoint["status"]=="completed_verified" and checkpoint.get("active_substep") is None and checkpoint.get("completed_at"),"historical PPIA-14 checkpoint must be completed_verified")
        continuity_mode="historical_after_ppia14"

    gap_by_id={x["id"]:x for x in gaps["gaps"]}
    require(gap_by_id["P14-GAP-001"].get("status")=="open" and "f024" in json.dumps(gap_by_id["P14-GAP-001"]).lower(),"F024 source gap must remain explicit/open")
    require(gap_by_id["P14-GAP-002"].get("status")=="resolved_by_candidate" and "microcopy_library" in json.dumps(gap_by_id["P14-GAP-002"]).lower(),"wording-library gap must be resolved by this candidate only")
    all_text=(json.dumps(library)+json.dumps(inspector)+json.dumps(actions)+json.dumps(cases)+candidate).lower()
    for prohibited in ("runtime_activation=true","a2_activation_authorized=true","release_authorized=true","deployment_authorized=true","tester_access_authorized=true","canonical_promotion_without_source_evidence_authorized=true"):
        require(prohibited not in all_text,f"prohibited authorization {prohibited!r}")
    print("PPIA-14 MICROCOPY LIBRARY IAR: PASS")
    print("library=18 message objects / 12 projection groups / 20 action presentations")
    print("cases=40 new + 32 Foundation = 72 effective")
    print("hidden_missing_equivalence=true status_unknown_not_failure=true f024_gap_preserved=true")
    print(f"continuity_mode={continuity_mode} runtime_activation=false")

if __name__=="__main__": main()