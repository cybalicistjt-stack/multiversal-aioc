#!/usr/bin/env python3
from __future__ import annotations
import json
from collections import Counter
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
BASE=ROOT/"governance/application-planning/parallel-preimplementation"
P=lambda n: BASE/n
FILES={
"workflow":P("PPIA-16_INTEGRATED_SCREEN_WORKFLOW_CONTRACT_MATRIX_v0.1.0.json"),
"trace":P("PPIA-16_INTEGRATED_SCREEN_WORKFLOW_TRACEABILITY_MATRIX_v0.1.0.json"),
"cases":P("PPIA-16_INTEGRATED_SCREEN_WORKFLOW_REFERENCE_CASES_v0.1.0.json"),
"index":P("PPIA-16_INTEGRATED_SCREEN_WORKFLOW_PACKAGE_INDEX_v0.1.0.json"),
"screens":P("PPIA-16_SCREEN_STATE_CONTRACTS_v0.1.0.json"),
"actions":P("PPIA-16_ACTION_CONTRACTS_v0.1.0.json"),
"components":P("PPIA-16_COMPONENT_INTERACTION_CONTRACTS_v0.1.0.json"),
"rc":P("PPIA-16_SCREEN_ACTION_REFERENCE_CASES_v0.1.0.json"),
"inventory":P("PPIA-16_FOUNDATION_TOOLBELT_AND_AUTHORITY_INVENTORY_v0.1.0.json"),
"authority":P("PPIA-16_FOUNDATION_AUTHORITY_AND_STATUS_MODEL_v0.1.0.json"),
"coverage":P("PPIA-16_FOUNDATION_SCREEN_WORKFLOW_COVERAGE_MAP_v0.1.0.json"),
"backlog":P("PPIA_PROGRAM_BACKLOG.json")}
CHECKPOINT=ROOT/"governance/ai/work-state/PPIA-16-attempt-001.json"
POINTER=ROOT/"governance/ai/runtime/CURRENT_WORK_POINTER.json"
STATUS=ROOT/"governance/ai/runtime/CURRENT_IMPLEMENTATION_STATUS.json"
NARRATIVE=P("PPIA-16_INTEGRATED_SCREEN_WORKFLOW_CANDIDATE.md")
BRANCH="governance/ppia-16-developer-console-ai-team-control-surface"
PREDECESSOR=("8e0650fb9ab237ec3f1b1fe9152de42ee6f7c889","31685859485","31685859480","67/67","#291","015f200595fd6e8ba5da85a2956ee1c9dc8fb15b","45e7e34b6bf7de0ca2ebff4b2818bdb1007f04c5","31689903909","68/68","#292","be811bd4508954700a83032b285107a8bd0d019a","354e24007d2c453d090a2a6cdb31d3e3333c84c1","mv-dev v0.10.0")
WFS=[f"P16-WF-{i:03d}" for i in range(1,13)]
SCR={f"P16-SCR-{i:03d}" for i in range(1,11)}
ACT={"ACT-OBSERVE","ACT-NAVIGATE","ACT-GENERATE","ACT-RUN-EVIDENCE","ACT-EXTERNAL-ADAPTER","ACT-PROPOSE-GOVERNED-MUTATION","ACT-EXECUTE-GOVERNED-MUTATION","ACT-OWNER-GATED"}
CMP={f"P16-CMP-{i:03d}" for i in range(1,9)}
DT={f"DT-{i:03d}" for i in range(1,11)}
CTL={f"AIOC-CONTROL-{i:03d}" for i in range(1,11)}
HO={f"P16-HO-{i:03d}" for i in range(1,13)}
RC=[f"P16-RC-{i:03d}" for i in range(1,49)]
IW=[f"P16-IW-{i:03d}" for i in range(1,13)]
AUTH={"canonical_repository_authority","active_attempt_repository_state","derived_repository_projection","tool_observation_or_evidence","generated_development_aid"}
REQ={"current work/slice","scope authority","stop conditions","repository health","fixtures","scenarios","privacy scanning","UI evidence","design lint","traceability","recovery/performance","CI/evidence receipts","findings","Codex task capsules","proof exploration","interruption recovery"}
COUNTS={"foundation_workflows":12,"screens":10,"action_classes":8,"components":8,"dt_tools":10,"aioc_control_surfaces":10,"program_requirements":16,"authority_layers":5,"handoffs":12,"predecessor_reference_cases":48,"new_integrated_cases":12,"effective_qa_cases":60}

def fail(m):
    t="PPIA-16 INTEGRATED SCREEN/WORKFLOW TRACEABILITY: FAIL — "+m
    print("::error title=PPIA-16 Integrated Screen Workflow Validator::"+t)
    raise SystemExit(t)
def req(c,m):
    if not c: fail(m)
def load(p):
    req(p.exists(),f"missing {p.relative_to(ROOT)}")
    try:return json.loads(p.read_text(encoding="utf-8"))
    except json.JSONDecodeError as e:fail(f"invalid JSON {p.relative_to(ROOT)}: {e}")
def once(actual,expected,label):
    c=Counter(actual); req(set(c)==set(expected) and all(v==1 for v in c.values()),f"{label} not exact-once")

def main():
    d={k:load(v) for k,v in FILES.items()}
    cp,pointer,status=load(CHECKPOINT),load(POINTER),load(STATUS)
    wf,tr,cases,index=d["workflow"],d["trace"],d["cases"],d["index"]
    narrative=NARRATIVE.read_text(encoding="utf-8").lower()
    tranche={x.get("work_item_id"):x for x in d["backlog"].get("tranches",[])}.get("PPIA-16",{})
    req(d["backlog"].get("current_work_item_id")=="PPIA-16","PPIA-16 not current")
    req(tranche.get("status") in {"started","in_progress","ready_for_review"},"PPIA-16 not unfinished")
    req(cp.get("work_item_id")=="PPIA-16" and cp.get("attempt_id")=="PPIA-16-attempt-001" and cp.get("branch")==BRANCH,"checkpoint identity")
    req(cp.get("status") in {"started","in_progress","ready_for_review"} and cp.get("completed_at") is None,"checkpoint completion boundary")
    sub=(cp.get("active_substep") or "").lower(); req("integrated screen" in sub and "workflow traceability" in sub,"wrong active substep")
    req(cp.get("owner_decision_required") is False and cp.get("unresolved_failures")==[] and cp.get("roadmap_projection_pending") is True,"checkpoint blocker/projection")
    req(pointer.get("primary_attempt_id")=="PPIA-16-attempt-001","pointer primary")
    selected=[x for x in pointer.get("active_attempts",[]) if x.get("owner_selected")]; req(len(selected)==1 and selected[0].get("work_item_id")=="PPIA-16","owner-selected attempt")
    primary=status.get("primary",{})
    for f in ("work_item_id","attempt_id","branch","status","active_substep","next_action","latest_pushed_commit","pull_request","owner_decision_required","unresolved_failures","roadmap_projection_pending"): req(primary.get(f)==cp.get(f),f"compact status mismatch {f}")
    for f in ("attempt_id","branch","status","updated_at","roadmap_projection_pending"): req(selected[0].get(f)==cp.get(f),f"pointer mismatch {f}")
    hist=json.dumps({"completed":cp.get("completed_substeps",[]),"validation":cp.get("validation",[]),"evidence":cp.get("evidence",[]),"selection":pointer.get("selection_reason","")}).lower()
    for token in PREDECESSOR: req(token.lower() in hist,f"predecessor evidence missing {token}")
    req("dt-001" in hist and "dt-010" in hist,"DT identity missing")
    req({x.get("screen_id") for x in d["screens"].get("screens",[])}==SCR,"screen predecessor changed")
    req({x.get("id") for x in d["actions"].get("actions",[])}==ACT,"action predecessor changed")
    req({x.get("id") for x in d["components"].get("components",[])}==CMP,"component predecessor changed")
    rcs=d["rc"].get("cases",[]); req(d["rc"].get("classification")=="synthetic_noncanonical_qa_reference_fixture" and d["rc"].get("canonical") is False,"predecessor RC classification")
    req([x.get("id") for x in rcs]==RC,"predecessor RC IDs"); req(Counter(x.get("workflow_id") for x in rcs)==Counter({w:4 for w in WFS}),"predecessor RC distribution")
    req({x.get("id") for x in d["inventory"].get("toolbelt",[])}==DT,"DT set"); req({x.get("id") for x in d["inventory"].get("aioc_control_surfaces",[])}==CTL,"AIOC controls")
    req({x.get("class") for x in d["authority"].get("authority_precedence",[])}==AUTH,"authority set"); req({x.get("workflow_id") for x in d["coverage"].get("workflows",[])}==set(WFS),"Foundation workflow set")
    req({x.get("requirement") for x in d["coverage"].get("program_requirement_coverage",[])}==REQ,"program requirements")
    for doc in (wf,tr,index): req(doc.get("work_item_id")=="PPIA-16" and doc.get("status")=="integrated-screen-workflow-candidate","integrated identity/status")
    req(wf.get("classification")=="synthetic_noncanonical_qa_integrated_workflow_contracts" and wf.get("canonical") is False,"workflow classification")
    req(wf.get("counts")==COUNTS and tr.get("counts")==COUNTS and index.get("locked_counts")==COUNTS,"locked counts")
    rows=wf.get("workflows",[]); req([x.get("id") for x in rows]==WFS,"workflow IDs/order"); by={x["id"]:x for x in rows}
    used={"screens":set(),"actions":set(),"components":set(),"tools":set(),"controls":set(),"requirements":set(),"authority":set(),"handoffs":set()}; allrc=[]; alliw=[]
    for i,row in enumerate(rows,1):
        wid=f"P16-WF-{i:03d}"; exp=[f"P16-RC-{j:03d}" for j in range((i-1)*4+1,i*4+1)]
        req(row.get("predecessor_cases")==exp and row.get("integrated_case")==f"P16-IW-{i:03d}",f"{wid} case assignment"); req(row.get("candidate_bound") is True and row.get("oracle"),f"{wid} candidate/oracle")
        for k,allowed in (("screens",SCR),("actions",ACT),("components",CMP),("tools",DT),("controls",CTL),("requirements",REQ),("authority",AUTH),("handoffs",HO)):
            req(set(row.get(k,[]))<=allowed,f"{wid} unknown {k}"); used[k]|=set(row.get(k,[]))
        allrc+=row["predecessor_cases"]; alliw.append(row["integrated_case"])
    once(allrc,RC,"predecessor reference cases"); once(alliw,IW,"integrated cases")
    req(used=={"screens":SCR,"actions":ACT,"components":CMP,"tools":DT,"controls":CTL,"requirements":REQ,"authority":AUTH,"handoffs":HO},"orphaned concern")
    handoffs=wf.get("handoffs",[]); req({x.get("id") for x in handoffs}==HO,"handoff set")
    for h in handoffs:
        for f in ("from","to","owner","rule","candidate"): req(h.get(f) not in (None,[],{},""),f"{h.get('id')} missing {f}")
    trace_by={x["workflow_id"]:x for x in tr.get("workflow_rows",[])}; req(set(trace_by)==set(WFS),"trace workflow set")
    translate={"screens":"screen_ids","actions":"action_ids","components":"component_ids","tools":"tool_ids","controls":"aioc_control_surface_ids","requirements":"program_requirements","authority":"authority_classes","handoffs":"handoff_ids","predecessor_cases":"predecessor_reference_case_ids"}
    for wid,row in by.items():
        t=trace_by[wid]
        for source,target in translate.items(): req(row.get(source,[])==t.get(target,[]),f"{wid} trace {source}")
        req([row["integrated_case"]]==t.get("integrated_case_ids",[]),f"{wid} trace integrated case")
    reverse=tr.get("reverse",{}); expected={"screens":SCR,"actions":ACT,"components":CMP,"tools":DT,"controls":CTL,"requirements":REQ,"authority":AUTH,"handoffs":HO}
    for group,ids in expected.items():
        req(set(reverse.get(group,{}))==ids,f"reverse {group} set")
        for ident,wids in reverse[group].items(): req(wids==[w for w in WFS if ident in by[w].get(group,[])],f"reverse {group} {ident}")
    req("no orphan" in tr.get("no_orphan_rule","").lower() and "exactly once" in tr.get("no_orphan_rule","").lower(),"no-orphan rule")
    req(cases.get("classification")=="synthetic_noncanonical_qa_integrated_reference_cases" and cases.get("canonical") is False,"integrated case classification")
    req(cases.get("counts")=={"new_integrated_cases":12,"inherited_screen_action_reference_cases":48,"effective_qa_cases":60},"integrated case counts")
    crows=cases.get("cases",[]); req([x.get("id") for x in crows]==IW,"integrated case IDs")
    for i,c in enumerate(crows,1):
        wid=f"P16-WF-{i:03d}"; req(c.get("workflow")==wid and c.get("predecessor_cases")==by[wid]["predecessor_cases"],f"{c.get('id')} assignment")
        req(c.get("classification")=="synthetic_noncanonical_qa_integrated_reference_case" and c.get("canonical") is False,f"{c.get('id')} class")
        for f in ("scenario","oracle","accessibility","forbidden"): req(c.get(f) not in (None,[],{},""),f"{c.get('id')} missing {f}")
    policy=wf.get("policy",{})
    for k in ("only_completed_verified_is_complete","authority_precedence_before_projection","raw_status_preserved","exact_candidate_binding_for_candidate_evidence","historical_evidence_remains_historical","stop_conditions_before_mutation","confirmation_does_not_create_authority"): req(policy.get(k) is True,f"policy {k}")
    for k in ("ambiguous_mutation_blind_retry","generated_aid_is_governance_authority","tool_pass_is_work_item_completion","proven_is_work_item_completion","synthetic_tool_test_ui_is_product_evidence","reference_probe_is_product_recovery_proof","runtime_activation","stage_a_a2_activation","release","deployment","tester_access","paid_service","production_credentials","canonical_promotion"): req(policy.get(k) is False,f"boundary {k}")
    cr=cases.get("requirements",{})
    for k in ("only_completed_verified_is_complete","authority_precedence_before_projection","exact_candidate_binding","stale_evidence_visible","historical_findings_not_automatic_current_blockers","raw_status_semantics_preserved","stop_conditions_before_governed_action","semantic_nonvisual_parity","mobile_touch_high_zoom_parity","synthetic_noncanonical"): req(cr.get(k) is True,f"case requirement {k}")
    for k in ("blind_ambiguous_mutation_retry","generated_aid_is_authority","runtime_activation","stage_a_a2_activation","release","deployment","tester_access","paid_service","production_credentials","canonical_promotion"): req(cr.get(k) is False,f"case boundary {k}")
    for doc in (wf,tr,cases,index): req(doc.get("nonactivation") and all(v is False for v in doc["nonactivation"].values()),f"{doc.get('title')} nonactivation")
    pred=index.get("immutable_predecessor_evidence",{}); req(pred.get("foundation",{}).get("merge")==PREDECESSOR[5] and pred.get("screen_action_reference",{}).get("merge")==PREDECESSOR[10],"package predecessor evidence")
    req(index.get("next_milestone")=="PPIA-16 Completion Contract / Evidence Closure","next milestone"); req("does not by itself complete ppia-16" in index.get("completion_effect","").lower(),"completion effect")
    for phrase in ("60 effective","12/12","candidate","stale","raw","blind retry","all-green","completion contract","not ppia-16 completion"): req(phrase in narrative,f"narrative {phrase}")
    print("PPIA-16 INTEGRATED SCREEN/WORKFLOW TRACEABILITY: PASS")
    print("workflows=12 screens=10 actions=8 components=8 dt_tools=10 aioc_controls=10 requirements=16 authority_layers=5 handoffs=12")
    print("predecessor_reference_cases=48 exact_once=true new_integrated_cases=12 effective_qa_cases=60 orphans=0")
    print("exact_candidate=true stale_visible=true raw_status=true blind_retry=false runtime_activation=false stage_a_a2=false")
if __name__=="__main__": main()
