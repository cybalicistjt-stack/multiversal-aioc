#!/usr/bin/env python3
from __future__ import annotations
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / "governance/application-planning/parallel-preimplementation"
BACKLOG = BASE / "PPIA_PROGRAM_BACKLOG.json"
P13 = ROOT / "governance/ai/work-state/PPIA-13-attempt-001.json"
P14 = ROOT / "governance/ai/work-state/PPIA-14-attempt-001.json"
P8 = ROOT / "governance/ai/work-state/PPIA-08-attempt-001.json"
POINTER = ROOT / "governance/ai/runtime/CURRENT_WORK_POINTER.json"
STATUS = ROOT / "governance/ai/runtime/CURRENT_IMPLEMENTATION_STATUS.json"
PACKAGE = BASE / "PPIA-13_COMPLETION_PACKAGE_INDEX_v0.1.0.json"
REPORT = BASE / "PPIA-13_COMPLETION_REPORT.md"

P13_FINAL_HEAD = "81e5c75effa1d4f8a8215493ef84b57108e20fae"
P13_COMPLETION_PR = 279
P13_COMPLETION_RUN = "31638609641"
P13_COMPLETION_MERGE = "cbfb6b931b11326afd5b826ad2a500e9b6d2d9c9"
P14_BRANCH = "governance/ppia-14-error-recovery-permission-microcopy"
EXPECTED_ORDER = ["PPIA-01","PPIA-02","PPIA-03","PPIA-04","PPIA-05","PPIA-12","PPIA-07","PPIA-08","PPIA-09","PPIA-10","PPIA-11","PPIA-06","PPIA-13","PPIA-14","PPIA-15","PPIA-16"]
COMPLETE = {"complete","completed","completed_verified"}
ACTIVE = {"started","in_progress","ready_for_review"}

def fail(message: str) -> None:
    raise SystemExit(f"PPIA-13→PPIA-14 TRANSITION: FAIL — {message}")
def require(condition: bool, message: str) -> None:
    if not condition: fail(message)
def load(path: Path) -> dict:
    require(path.exists(), f"missing {path.relative_to(ROOT)}")
    return json.loads(path.read_text(encoding="utf-8"))

def main() -> None:
    backlog=load(BACKLOG); p13=load(P13); p14=load(P14); p8=load(P8); pointer=load(POINTER); status=load(STATUS); package=load(PACKAGE)
    report=REPORT.read_text(encoding="utf-8").lower()
    tranches={x["work_item_id"]:x for x in backlog["tranches"]}
    require(backlog["execution_order"]==EXPECTED_ORDER, "dependency-optimized PPIA order changed")
    require(EXPECTED_ORDER.index("PPIA-13")+1==EXPECTED_ORDER.index("PPIA-14"), "PPIA-14 must directly follow PPIA-13")
    require(tranches["PPIA-13"]["status"]=="completed_verified", "PPIA-13 backlog must be completed_verified")
    require(tranches["PPIA-14"].get("dependencies")==["PPIA-08","PPIA-13"], "PPIA-14 dependencies changed")
    require(tranches["PPIA-08"]["status"] in COMPLETE and p8["status"]=="completed_verified", "PPIA-08 dependency must remain completed_verified")
    for wid in EXPECTED_ORDER[:EXPECTED_ORDER.index("PPIA-14")]: require(tranches[wid]["status"] in COMPLETE, f"{wid} must be complete before PPIA-14")

    require(p13["work_item_id"]=="PPIA-13" and p13["attempt_id"]=="PPIA-13-attempt-001", "PPIA-13 checkpoint identity mismatch")
    require(p13["status"]=="completed_verified" and p13["active_substep"] is None and p13.get("completed_at"), "PPIA-13 checkpoint must be finalized")
    require(p13["latest_pushed_commit"]==P13_FINAL_HEAD, "PPIA-13 exact validated completion head mismatch")
    require(p13["pull_request"]==P13_COMPLETION_PR and p13["merge_commit"]==P13_COMPLETION_MERGE, "PPIA-13 completion PR/merge mismatch")
    require(p13["owner_decision_required"] is False and p13["unresolved_failures"]==[], "PPIA-13 completion has unresolved state")
    require(any(P13_COMPLETION_RUN in x.get("command","") and x.get("status")=="passed" for x in p13.get("validation",[])), "PPIA-13 completion run evidence missing")
    ev=json.dumps(p13.get("evidence",[]),ensure_ascii=False)+p13.get("last_verified_action","")
    for v in (P13_FINAL_HEAD,P13_COMPLETION_MERGE,"PR #279",P13_COMPLETION_RUN): require(v in ev, f"PPIA-13 immutable evidence missing {v}")
    require(package.get("transition_after_completion")=="PPIA-13 -> PPIA-14 separate governed operation", "PPIA-13 completion transition boundary changed")
    for phrase in ("p13-gap-001","ppia-14 retains final","zero-ai parity","no application runtime"): require(phrase in report, f"PPIA-13 completion report lost {phrase!r}")

    require(p14["work_item_id"]=="PPIA-14" and p14["attempt_id"]=="PPIA-14-attempt-001", "PPIA-14 checkpoint identity mismatch")
    require(p14["branch"]==P14_BRANCH and p14["base_commit"]==P13_COMPLETION_MERGE, "PPIA-14 branch/base mismatch")
    require(p14["status"] in ACTIVE | {"completed_verified"}, "PPIA-14 status invalid")
    require(p14["owner_decision_required"] is False and p14["unresolved_failures"]==[], "PPIA-14 transition state must be unblocked")
    scope=json.dumps({"objective":p14.get("objective"),"last_verified_action":p14.get("last_verified_action"),"active_substep":p14.get("active_substep"),"next_action":p14.get("next_action"),"completed_substeps":p14.get("completed_substeps",[]),"notes":p14.get("notes",[])},ensure_ascii=False).lower()
    for phrase in ("error","recovery","permission","hidden-information","validation","stale","conflict","offline","reconnect","status unknown","retry","approval","support","diagnostics","player","gm","creator","mobile","keyboard","screen-reader","nonvisual","localization","f024","ppia-13"):
        require(phrase in scope, f"PPIA-14 governed scope missing {phrase!r}")

    current_id=backlog["current_work_item_id"]
    if current_id=="PPIA-14":
        require(tranches["PPIA-14"]["status"] in ACTIVE, "active PPIA-14 backlog must be started")
        require(p14["status"] in ACTIVE and p14.get("active_substep") and p14.get("next_action"), "active PPIA-14 must be on a bounded step")
        for wid in EXPECTED_ORDER[EXPECTED_ORDER.index("PPIA-14")+1:]: require(tranches[wid]["status"]=="planned", f"{wid} must remain planned during PPIA-14 activation")
        selected=[x for x in pointer["active_attempts"] if x.get("owner_selected")]
        require(len(selected)==1 and pointer["primary_attempt_id"]=="PPIA-14-attempt-001" and selected[0]["work_item_id"]=="PPIA-14", "pointer must select exactly PPIA-14")
        current=selected[0]
        require(current["checkpoint_path"]=="governance/ai/work-state/PPIA-14-attempt-001.json", "pointer must select PPIA-14 checkpoint")
        for field in ("attempt_id","branch","status","updated_at","roadmap_projection_pending"): require(current[field]==p14[field], f"pointer/PPIA-14 mismatch {field}")
        primary=status["primary"]
        for field in ("work_item_id","attempt_id","branch","status","active_substep","next_action","latest_pushed_commit","pull_request","owner_decision_required","unresolved_failures","roadmap_projection_pending"): require(primary[field]==p14.get(field), f"compact status/PPIA-14 mismatch {field}")
        reason=pointer["selection_reason"]
        for v in (P13_FINAL_HEAD,P13_COMPLETION_MERGE,P13_COMPLETION_RUN): require(v in reason, f"pointer must preserve PPIA-13 completion evidence {v}")
        transition_mode="active_ppia14"
    else:
        require(EXPECTED_ORDER.index(current_id)>EXPECTED_ORDER.index("PPIA-14"), "historical transition may only validate after PPIA-14")
        require(tranches["PPIA-14"]["status"] in COMPLETE, "historical PPIA-14 backlog must be complete")
        require(p14["status"]=="completed_verified" and p14["active_substep"] is None and p14.get("completed_at"), "historical PPIA-14 checkpoint must be completed_verified")
        transition_mode="historical_after_ppia14"

    require("roadmap" in pointer["selection_reason"].lower() and "pending" in pointer["selection_reason"].lower(), "pointer must explain batched roadmap projection")
    boundaries=backlog["boundaries"]
    for key in ("application_runtime_mutation_authorized","a2_activation_authorized","release_authorized","deployment_authorized","tester_access_authorized","canonical_promotion_without_source_evidence_authorized"): require(boundaries[key] is False, f"transition may not enable {key}")
    require(boundaries["requires_codex"] is False, "PPIA transition must not require Codex")
    print("PPIA-13→PPIA-14 TRANSITION: PASS")
    print(f"ppia13_final_head={P13_FINAL_HEAD}")
    print(f"ppia13_final_merge={P13_COMPLETION_MERGE}")
    print(f"ppia13_completion_run={P13_COMPLETION_RUN}")
    print("ppia13_status=completed_verified")
    print(f"ppia14_status={p14['status']}")
    print(f"ppia14_branch={P14_BRANCH}")
    print(f"transition_mode={transition_mode}")
    print("roadmap_projection_pending=true runtime_activation=false")

if __name__ == "__main__": main()
