#!/usr/bin/env python3
from __future__ import annotations
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
BASE=ROOT/"governance/application-planning/parallel-preimplementation"
BACKLOG=BASE/"PPIA_PROGRAM_BACKLOG.json"; P6=ROOT/"governance/ai/work-state/PPIA-06-attempt-001.json"; P13=ROOT/"governance/ai/work-state/PPIA-13-attempt-001.json"; P8=ROOT/"governance/ai/work-state/PPIA-08-attempt-001.json"; POINTER=ROOT/"governance/ai/runtime/CURRENT_WORK_POINTER.json"; STATUS=ROOT/"governance/ai/runtime/CURRENT_IMPLEMENTATION_STATUS.json"
P6_HEAD="6d2da6fb5a7c2d62492de895c6a9c7a1fe970a06"; P6_MERGE="ffce4859a8912813021776c4f5825c3d219bb0f2"; P6_RUN="31622184027"
P13_HEAD="81e5c75effa1d4f8a8215493ef84b57108e20fae"; P13_MERGE="cbfb6b931b11326afd5b826ad2a500e9b6d2d9c9"; P13_RUN="31638609641"
ORDER=["PPIA-01","PPIA-02","PPIA-03","PPIA-04","PPIA-05","PPIA-12","PPIA-07","PPIA-08","PPIA-09","PPIA-10","PPIA-11","PPIA-06","PPIA-13","PPIA-14","PPIA-15","PPIA-16"]
COMPLETE={"complete","completed","completed_verified"}
def load(p): return json.loads(p.read_text(encoding="utf-8"))
def req(c,m):
    if not c: raise SystemExit("PPIA-06→PPIA-13 TRANSITION: FAIL — "+m)
def main():
    b=load(BACKLOG); p6=load(P6); p13=load(P13); p8=load(P8); pointer=load(POINTER); status=load(STATUS); t={x["work_item_id"]:x for x in b["tranches"]}
    req(b["execution_order"]==ORDER,"execution order changed"); req(t["PPIA-06"]["status"]=="completed_verified","PPIA-06 not complete"); req(t["PPIA-08"]["status"]=="completed_verified" and p8["status"]=="completed_verified","PPIA-08 dependency changed")
    req(p6["status"]=="completed_verified" and p6["latest_pushed_commit"]==P6_HEAD and p6["merge_commit"]==P6_MERGE and p6["pull_request"]==273,"PPIA-06 immutable completion evidence changed")
    req(any(P6_RUN in x.get("command","") and x.get("status")=="passed" for x in p6.get("validation",[])),"PPIA-06 completion run missing")
    req(p13["work_item_id"]=="PPIA-13" and p13["branch"]=="governance/ppia-13-onboarding-help-teaching-content" and p13["base_commit"]==P6_MERGE,"PPIA-13 identity/base changed")
    current=b["current_work_item_id"]
    if current=="PPIA-13":
        req(t["PPIA-13"]["status"]=="started" and p13["status"] in {"started","ready_for_review"},"current PPIA-13 must remain active")
        req(pointer["primary_attempt_id"]=="PPIA-13-attempt-001" and status["primary"]["work_item_id"]=="PPIA-13","runtime continuity must select current PPIA-13")
        mode="current"
    else:
        req(ORDER.index(current)>ORDER.index("PPIA-13"),"current item cannot precede historical PPIA-13")
        req(t["PPIA-13"]["status"]=="completed_verified" and p13["status"]=="completed_verified" and p13["active_substep"] is None,"historical PPIA-13 must be completed_verified")
        req(p13["latest_pushed_commit"]==P13_HEAD and p13["merge_commit"]==P13_MERGE and p13["pull_request"]==279,"PPIA-13 completion evidence changed")
        req(any(P13_RUN in x.get("command","") and x.get("status")=="passed" for x in p13.get("validation",[])),"PPIA-13 completion run missing")
        mode="historical"
    for k in ("application_runtime_mutation_authorized","a2_activation_authorized","release_authorized","deployment_authorized","tester_access_authorized","canonical_promotion_without_source_evidence_authorized"): req(b["boundaries"][k] is False,f"boundary enabled {k}")
    print("PPIA-06→PPIA-13 TRANSITION: PASS"); print("continuity_mode="+mode); print("runtime_activation=false")
if __name__=="__main__": main()
