#!/usr/bin/env python3
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
A=ROOT/"governance"/"project-archaeology"
I=ROOT/"governance"/"project-integrity"
P=ROOT/"governance"/"application-planning"/"product-convergence"
def load(p): return json.loads(p.read_text(encoding="utf-8"))
fam=load(A/"PROJECT_FAMILY_TRANCHE_INVENTORY.json")
canon=load(A/"PROJECT_CURRENT_CANON_INDEX.json")
reg=load(I/"PROJECT_WORK_HISTORY_REGISTRY.json")
dep=load(I/"PROJECT_FEATURE_FAMILY_APP_DEPENDENCY_MAP.json")
gaps=load(I/"PROJECT_INTEGRITY_GAP_REGISTER.json")
pcv=load(P/"PCV_PREIMPLEMENTATION_GAP_REGISTER.json")
backlog=load(I/"PROJECT_INTEGRITY_PROGRAM_BACKLOG.json")
assert reg["status"] in {"completion_candidate","completed_verified"}
assert dep["status"] in {"completion_candidate","completed_verified"}
assert reg["mutation_policy"]["identity_fields_immutable"] is True
assert reg["mutation_policy"]["silent_rename_forbidden"] is True
assert reg["mutation_policy"]["silent_delete_forbidden"] is True
assert reg["counts"]["application_planning_groups"]==83
assert reg["counts"]["work_state_families"]==73
assert reg["counts"]["unique_work_items"]==662
assert reg["counts"]["attempt_files"]==667
assert reg["counts"]["duplicate_attempt_extra_files"]==5
assert reg["counts"]["pdcp_reductions"]==10
assert len(reg["planning_groups"])==83
assert len(reg["work_state_families"])==73
assert len(reg["work_items"])==662
assert len({x["group_id"] for x in reg["planning_groups"]})==83
assert len({x["family_id"] for x in reg["work_state_families"]})==73
assert len({x["work_item_id"] for x in reg["work_items"]})==662
source_paths={x["path"] for x in fam["application_planning_directories"]}
registry_paths={x["source_path"] for x in reg["planning_groups"]}
assert source_paths==registry_paths
source_families={x["family"] for x in fam["work_state_families"]}
registry_families={x["family_id"] for x in reg["work_state_families"]}
assert source_families==registry_families
source_items={i for f in fam["work_state_families"] for i in f["work_items"]}
registry_items={x["work_item_id"] for x in reg["work_items"]}
assert source_items==registry_items
for item in reg["work_items"]:
    assert item["family_id"] in registry_families
family_parent={x["family_id"]:x["parent_group_ids"] for x in reg["work_state_families"]}
# Standalone historical family is allowed only when explicitly preserved as such.
for family,parents in family_parent.items():
    if not parents:
        rec=next(x for x in reg["work_state_families"] if x["family_id"]==family)
        assert rec["lineage_mapping"]=="standalone_unmapped"
        assert rec["disposition"] in {"superseded_provenance_only","completed_parallel_content_or_governance"}
nodes={x["node_id"] for x in dep["nodes"]}
assert "APP::MULTIVERSAL" in nodes
member_edges=[e for e in dep["edges"] if e["edge_type"]=="member_of"]
assert len(member_edges)==662
assert {e["from"].removeprefix("WORK::") for e in member_edges}==source_items
assert dep["counts"]["planning_groups"]==83
assert dep["counts"]["work_state_families"]==73
assert dep["counts"]["work_items"]==662
assert dep["counts"]["canon_intent_nodes"]==len(canon["entries"])==71
assert dep["counts"]["capability_ledger_rows"]==56
assert dep["counts"]["current_overlay_work_items"]==len(reg["current_overlay"]["work_items"])
# Every edge endpoint must exist; overlay work may not create dangling graph references.
for edge in dep["edges"]:
    assert edge["from"] in nodes, edge
    assert edge["to"] in nodes, edge
# Every planning group contributes structurally to the app.
contrib={e["from"] for e in dep["edges"] if e["edge_type"]=="contributes_to_app" and e["to"]=="APP::MULTIVERSAL"}
assert contrib=={x["group_id"] for x in reg["planning_groups"]}
# All scoped gaps have owners and routes.
assert gaps["child_registers"][0]["known_findings"]==pcv["finding_count"]==len(pcv["findings"])
assert all(x.get("owner") and x.get("repair") and x.get("status") for x in gaps["findings"])
assert all(x.get("primary_interstitial") and x.get("disposition") for x in pcv["findings"])
assert backlog["strict_order"]==["PIM-01","PIM-02","PIM-03"]
overlay_ids={x["work_item_id"] for x in reg["current_overlay"]["work_items"]}
assert {"PIM-01","PIM-02","PIM-03","PCV-I01A","PCV-I01B","PCV-I01C","PCV-I06","PCV-03A","PCV-03F","PCV-10"} <= overlay_ids
# Project Source hashes are frozen integrity anchors, not authority.
sources={x["name"]:x["sha256"] for x in reg["live_project_source_surface"]["files"]}
assert sources["PROJECT_SOURCE_MANIFEST.md"]=="15ba1bc42c12920c245d1611ac5b95c8614a87520644230ca64c3cd43892bb2c"
assert sources["PROJECT_BIBLE_OPS3_REFERENCE.md"]=="8de341b25a51af106387c3516bbe4983a30274efb423fdca460350bb92b1748e"
print(json.dumps({"status":"PASS","planning_groups":83,"work_state_families":73,"unique_work_items":662,"attempt_files":667,"canon_nodes":71,"capability_rows":56,"map_nodes":dep["counts"]["nodes"],"map_edges":dep["counts"]["edges"],"master_integrity_findings":len(gaps["findings"]),"pcv_child_findings":pcv["finding_count"]},sort_keys=True))
