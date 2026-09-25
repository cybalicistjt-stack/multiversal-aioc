#!/usr/bin/env python3
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
A=ROOT/"governance"/"project-archaeology"
P=ROOT/"governance"/"application-planning"/"product-convergence"
I=ROOT/"governance"/"project-integrity"
def load(path): return json.loads(path.read_text(encoding="utf-8"))
reg=load(A/"PROJECT_CANON_REGISTER.json")
fam=load(A/"PROJECT_FAMILY_TRANCHE_INVENTORY.json")
canon=load(A/"PROJECT_CURRENT_CANON_INDEX.json")
matrix=load(A/"PROJECT_WIRING_DEPENDENCY_MATRIX.json")
defects=load(A/"PROJECT_WIRING_DEFECT_REGISTER.json")
orphans=load(A/"PROJECT_ORPHANED_INTENT_REGISTER.json")
repairs=load(A/"PROJECT_REPAIR_ROUTING_PLAN.json")
allowed={"current_canon","current_intent_not_yet_implemented","implemented_and_current","implemented_but_superseded","design_complete_consumed_by_later_owner","completed_parallel_content_or_governance","owner_approved_planned","deferred_future","superseded_provenance_only","rejected_or_retired","unresolved_archaeology","missing_orphaned_intent"}
assert reg["status"].endswith("_candidate") or reg["status"] in {"completed_verified","completed_verified_canon_reconstruction_with_pcv_wiring_reaudit"}
assert reg.get("canon_reconstruction_gate_complete") is True
assert all(x.get("status","").startswith("accounted") for x in reg["required_eras"])
phase_ids={x["id"] for x in reg["chronology"]}
assert {f"PHASE-{i}" for i in range(1,10)} <= phase_ids
dirs=fam["application_planning_directories"]
assert len(dirs)==83, len(dirs)
assert all(d["disposition"] in allowed and d["disposition"]!="unresolved_archaeology" for d in dirs)
families=fam["work_state_families"]
assert fam["work_state_attempt_file_count"]==667
assert fam["unique_work_item_count"]==662
assert sum(x["work_item_count"] for x in families)==662
assert sum(len(v)-1 for v in fam["duplicate_attempt_series"].values())==5
for f in families:
    assert f["disposition"] in allowed and f["disposition"]!="unresolved_archaeology"
    assert len(f["item_dispositions"])==f["work_item_count"]
    assert {x["work_item_id"] for x in f["item_dispositions"]}==set(f["work_items"])
    assert all(x["disposition"] in allowed and x["disposition"]!="unresolved_archaeology" for x in f["item_dispositions"])
canon_ids={x["id"] for x in canon["entries"]}
matrix_ids={x["canon_entry_id"] for x in matrix["entries"]}
assert canon_ids==matrix_ids
assert defects["summary"]["unowned"]==0
assert defects["summary"].get("silent_duplicate_owners",0)==0
assert repairs["unowned_repairs"]==[]
assert orphans["unowned_orphaned_intent"]==[]
if reg.get("internal_wiring_dependency_interconnectivity_gate_complete") is True:
    assert defects["summary"]["unresolved_required_bindings"]==0
    assert all(x.get("repair_destination") and x.get("status","").startswith("owned_") for x in defects["findings"])
else:
    pcv=reg.get("pcv_candidate_specific_wiring_gate") or {}
    assert pcv.get("status")=="in_progress"
    gap=load(P/"PCV_PREIMPLEMENTATION_GAP_REGISTER.json")
    assert gap["status"] in {"in_progress","blocked_by_project_integrity_map"}
    assert gap["finding_count"]==len(gap["findings"]) and gap["finding_count"]>=100
    assert all(x.get("primary_interstitial") and x.get("disposition") for x in gap["findings"])
    pim=reg.get("project_integrity_map_gate") or {}
    if pim:
        assert pim.get("status")=="in_progress"
        assert (I/"PROJECT_WORK_HISTORY_REGISTRY.json").exists()
assert any(x["id"]=="CANON-PCV03" for x in canon["entries"])
for n in range(4,11):
    e=next(x for x in canon["entries"] if x["id"]==f"INTENT-PCV-{n:02d}")
    assert e["disposition"]=="current_intent_not_yet_implemented"
print(json.dumps({"status":"PASS","planning_directories":len(dirs),"attempt_files":fam["work_state_attempt_file_count"],"unique_work_items":fam["unique_work_item_count"],"current_canon_intent_entries":len(canon_ids),"wiring_findings":len(defects["findings"]),"wiring_gate_complete":reg.get("internal_wiring_dependency_interconnectivity_gate_complete"),"unowned_repairs":0},sort_keys=True))
