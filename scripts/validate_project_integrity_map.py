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
wire=load(A/"PROJECT_WIRING_DEFECT_REGISTER.json")
pcv_backlog=load(P/"PCV_PROGRAM_BACKLOG.json")
pcv_pre=load(P/"PCV_PREIMPLEMENTATION_INTEGRITY_BACKLOG.json")
roadmap=load(ROOT/"governance"/"application-planning"/"ROADMAP_DEPENDENCY_GRAPH.json")
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
assert reg["counts"]["live_project_source_files"]==12
assert reg["coverage_invariants"]["frozen_work_items_have_attempt_evidence"] is True
assert reg["coverage_invariants"]["frozen_attempt_record_count"]==667
assert sorted(reg["coverage_invariants"]["frozen_work_items_with_multiple_attempts"])==["CCTI-12","DS-008-working-series","P9-06-008"]
assert len(reg["planning_groups"])==83
assert len(reg["work_state_families"])==73
assert len(reg["work_items"])==662
assert len({x["group_id"] for x in reg["planning_groups"]})==83
assert all(x.get("wider_app_role") for x in reg["planning_groups"])
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
pcv_child=next(x for x in gaps["child_registers"] if x["register_id"]==pcv["register_id"])
assert pcv_child["known_findings"]==pcv["finding_count"]==len(pcv["findings"])
assert {x["scope"] for x in gaps["child_registers"]}=={"PCV preimplementation","project wiring defects","orphaned/live intent","repair routes"}
assert all(x.get("owner") and x.get("repair") and x.get("status") for x in gaps["findings"])
assert all(x.get("primary_interstitial") and x.get("disposition") for x in pcv["findings"])
assert backlog["strict_order"]==["PIM-01","PIM-02","PIM-03"]
overlay_ids={x["work_item_id"] for x in reg["current_overlay"]["work_items"]}
assert {"PIM-01","PIM-02","PIM-03","PCV-I01A","PCV-I01B","PCV-I01C","PCV-I06","PCV-03A","PCV-03F","PCV-10"} <= overlay_ids
registry_overlay_status={x["work_item_id"]:x["status"] for x in reg["current_overlay"]["work_items"]}
dep_overlay_status={x["work_item_id"]:x["status"] for x in dep["current_overlay_work_items"]}
assert dep_overlay_status==registry_overlay_status
dep_node_status={x["node_id"].removeprefix("WORK::"):x.get("status") for x in dep["nodes"] if x.get("node_type")=="current_overlay_work_item"}
for work_item,status in registry_overlay_status.items():
    assert dep_node_status.get(work_item)==status, (work_item, dep_node_status.get(work_item), status)
if pcv_pre["status"]=="in_progress":
    assert pcv_backlog["current_item"]==pcv_pre["current_item"]
    assert pcv_backlog["current_attempt"]==pcv_pre["current_attempt"]
if pcv_pre["status"]=="in_progress":
    current_attempt_path=ROOT/"governance"/"ai"/"work-state"/f'{pcv_pre["current_attempt"]}.json'
    current_checkpoint=load(current_attempt_path)
    assert current_checkpoint["work_item_id"]==pcv_pre["current_item"]
    current_tranche=next(x for x in pcv_pre["tranches"] if x["id"]==pcv_pre["current_item"])
    assert current_checkpoint["status"]==current_tranche["status"]
assert wire["summary"]["preimplementation_integrity_findings"]==pcv["finding_count"]
open_pcv_findings=[x for x in pcv["findings"] if x["disposition"]=="open_preimplementation"]
assert wire["summary"]["open_pcv_preimplementation_findings"]==len(open_pcv_findings)
for finding_id in {"WIRE-PCV03-PHYSICAL-001","WIRE-PCV-PRE-003"}:
    finding=next(x for x in wire["findings"] if x["finding_id"]==finding_id)
    assert str(len(open_pcv_findings)) in finding["missing_or_stale_binding"]
# Project Source hashes are frozen integrity anchors, not authority.
sources={x["name"]:x["sha256"] for x in reg["live_project_source_surface"]["files"]}
assert sources["PROJECT_SOURCE_MANIFEST.md"]=="15ba1bc42c12920c245d1611ac5b95c8614a87520644230ca64c3cd43892bb2c"
assert sources["PROJECT_BIBLE_OPS3_REFERENCE.md"]=="8de341b25a51af106387c3516bbe4983a30274efb423fdca460350bb92b1748e"
assert sources["SHA256SUMS.txt"]=="4e98b1c18ee3596b0f92efa48213e8faa4bb3f80bbc4af73da09923264e52f36"
# New owner-selected programs/interstitials must not fall out of the cross-program DAG.
assert {"BIP","PCV","PIM"} <= set(roadmap["nodes"])
assert "SMB18" in roadmap["program_edges"]["BIP"]["hard_requires"]
assert "BIP" in roadmap["program_edges"]["PCV"]["hard_requires"]
assert "PCV-02" in roadmap["program_edges"]["PIM"]["start_requires"]
assert "PIM-03" in roadmap["milestone_gates"]["PCV"]["PCV-I01A"]
assert "PCV-I06" in roadmap["milestone_gates"]["PCV"]["PCV-03A"]
# Any preimplementation closure contract is data-driven by its tranche record.
documented_edges={(e["from"],e["to"]) for e in dep["edges"] if e["edge_type"]=="documented_downstream_consumer"}
for tranche in pcv_pre["tranches"]:
    contract_path=tranche.get("closure_contract")
    if not contract_path:
        continue
    closure=load(ROOT/contract_path)
    assert closure["work_item_id"]==tranche["id"]
    assert closure["status"] in {"completion_candidate","completed_verified"}
    assert closure["runtime_boundary"]["runtime_product_implementation_authorized"] is False
    assert closure.get("acceptance_checks") and all(closure["acceptance_checks"].values())
    owned={x["finding_id"] for x in pcv["findings"] if x["primary_interstitial"]==tranche["id"]}
    assert set(closure["gap_closure"])==owned
    for finding in (x for x in pcv["findings"] if x["finding_id"] in owned):
        assert finding.get("candidate_closure_artifact")==contract_path
        if closure["status"]=="completion_candidate":
            assert finding["disposition"]=="open_preimplementation"
        else:
            assert finding["disposition"]=="closed_preimplementation_contract"
            assert finding["blocks_pcv03_implementation"] is False
    required_edges={(x["from"],x["to"]) for x in closure.get("dependency_edges",[])}
    assert required_edges <= documented_edges
print(json.dumps({"status":"PASS","planning_groups":83,"work_state_families":73,"unique_work_items":662,"attempt_files":667,"canon_nodes":71,"capability_rows":56,"map_nodes":dep["counts"]["nodes"],"map_edges":dep["counts"]["edges"],"master_integrity_findings":len(gaps["findings"]),"pcv_child_findings":pcv["finding_count"]},sort_keys=True))
