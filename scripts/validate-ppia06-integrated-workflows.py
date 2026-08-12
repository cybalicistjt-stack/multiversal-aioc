#!/usr/bin/env python3
from __future__ import annotations
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
B=ROOT/"governance/application-planning/parallel-preimplementation"

def load(name):
    p=B/name
    if not p.exists(): raise AssertionError(f"missing {name}")
    return json.loads(p.read_text(encoding="utf-8"))

def req(v,m):
    if not v: raise AssertionError(m)

def union(rows,key):
    out=set()
    for row in rows: out.update(row.get(key,[]))
    return out

def main():
    wf=load("PPIA-06_APPEARANCE_WORKFLOW_CONTRACT_MATRIX_v0.2.0.json")
    tr=load("PPIA-06_APPEARANCE_WORKFLOW_TRACEABILITY_MATRIX_v0.1.0.json")
    cov=load("PPIA-06_SPECIES_WORKFLOW_COVERAGE_MATRIX_v0.1.0.json")
    iw=load("PPIA-06_INTEGRATED_WORKFLOW_REFERENCE_CASES_v0.1.0.json")
    inspector=load("PPIA-06_APPEARANCE_INSPECTOR_ACTION_CONTRACT_MATRIX_v0.1.0.json")
    iar=load("PPIA-06_APPEARANCE_INSPECTOR_REFERENCE_CASES_v0.1.0.json")
    sv=load("PPIA-06_SPECIES_VISUAL_REFERENCE_CASES_v0.1.0.json")
    profiles=load("PPIA-06_SPECIES_MORPHOLOGY_PROFILES_v0.1.0.json")
    owner=load("PPIA-06_OWNER_VISUAL_CANON_DECISIONS_v0.1.0.json")
    manifest=load("PPIA-06_SPECIES_VISUAL_AUTHORITY_MANIFEST_v0.1.0.json")
    candidate=(B/"PPIA-06_APPEARANCE_WORKFLOW_TRACEABILITY_CANDIDATE.md").read_text(encoding="utf-8").lower()

    req(wf["schema_version"]=="0.2.0" and wf["work_item"]=="PPIA-06","workflow contract version/work item mismatch")
    counts=wf["counts"]
    expected_counts={"workflows":16,"mutation_workflows":14,"read_analysis_workflows":2,"species_profiles":25,"projection_groups":20,"actions":30,"iar_cases":48,"species_visual_cases":36,"integrated_cases":32,"effective_cases":116,"semantic_layers":18,"compatibility_dimensions":5,"handoffs":9}
    req(counts==expected_counts,"workflow counts changed")
    rows=wf["workflows"]
    req(len(rows)==16 and {x["id"] for x in rows}=={f"P06-WF-{i:03d}" for i in range(1,17)},"workflow IDs incomplete")
    req(sum(1 for x in rows if x["mutation"])==14 and sum(1 for x in rows if not x["mutation"])==2,"mutation/read workflow split changed")
    req(all(x.get("protocol")=="P06-MUT-001" for x in rows if x["mutation"]),"mutation workflow missing P06-MUT-001")

    expected_species={x["species"] for x in profiles["profiles"]}
    req(profiles["profile_count"]==25 and len(expected_species)==25,"expected 25 Species profiles")
    req(union(rows,"species")==expected_species,"integrated workflows must exercise all 25 Species")
    req(cov["profile_count"]==25 and len(cov["rows"])==25 and {x["species"] for x in cov["rows"]}==expected_species,"Species workflow coverage matrix incomplete")
    req(cov["coverage"]=="25/25","Species coverage declaration changed")
    req(all(x.get("integrated_cases") for x in cov["rows"]),"every Species must have integrated case coverage")

    expected_actions={f"P06-ACT-{i:03d}" for i in range(1,31)}
    expected_groups={f"P06-PG-{i:03d}" for i in range(1,21)}
    inspector_actions={x["id"]:x for x in inspector["actions"]}
    req(set(inspector_actions)==expected_actions,"Inspector actions changed")
    req({x["id"] for x in inspector["projection_groups"]}==expected_groups,"Inspector projection groups changed")
    wf_actions=union(rows,"actions")
    req(wf_actions==expected_actions,"workflow action coverage incomplete")
    derived_groups=set()
    for action in wf_actions: derived_groups.update(inspector_actions[action].get("groups",[]))
    req(derived_groups==expected_groups,"workflow projection-group coverage incomplete")
    expected_handoffs={f"P06-HO-{i:03d}" for i in range(1,10)}
    req({x["id"] for x in wf["handoffs"]}==expected_handoffs and union(rows,"handoffs")==expected_handoffs,"handoff coverage incomplete")

    expected_iar={f"P06-IAR-{i:03d}" for i in range(1,49)}
    iar_assigned=[c for row in rows for c in row["iar_case_ids"]]
    req(len(iar_assigned)==48 and set(iar_assigned)==expected_iar and len(set(iar_assigned))==48,"48 IAR cases must be assigned exactly once")
    req(iar["counts"]["new_inspector_action_reference_cases"]==48,"IAR corpus count changed")
    expected_sv={f"P06-SV-{i:02d}" for i in range(1,37)}
    sv_assigned=[c for row in rows for c in row["species_visual_case_ids"]]
    req(len(sv_assigned)==36 and set(sv_assigned)==expected_sv and len(set(sv_assigned))==36,"36 Species Visual cases must be assigned exactly once")
    req(sv["case_count"]==36,"Species Visual corpus count changed")
    expected_iw={f"P06-IW-{i:03d}" for i in range(1,33)}
    iw_assigned=[c for row in rows for c in row["integrated_case_ids"]]
    req(len(iw_assigned)==32 and set(iw_assigned)==expected_iw and len(set(iw_assigned))==32,"32 integrated cases must be assigned exactly once")
    req(iw["counts"]=={"integrated_cases":32,"species_profiles_covered":25,"inherited_iar_cases":48,"inherited_species_visual_cases":36,"effective_case_surface":116},"integrated case counts changed")
    req({x["id"] for x in iw["cases"]}==expected_iw,"integrated case IDs incomplete")
    req({s for x in iw["cases"] for s in x["species"]}==expected_species,"integrated cases must explicitly exercise all 25 Species")

    trace_rows=tr["rows"]
    req(len(trace_rows)==16 and {x["id"] for x in trace_rows}=={x["id"] for x in rows},"trace workflow rows mismatch")
    by={x["id"]:x for x in rows}
    for row in trace_rows:
        w=by[row["id"]]
        req(row["mutation"]==w["mutation"],f"trace mutation mismatch {row['id']}")
        req(row["iar_cases"]==w["iar_case_ids"],f"trace IAR mismatch {row['id']}")
        req(row["species_visual_cases"]==w["species_visual_case_ids"],f"trace Species Visual mismatch {row['id']}")
        req(row["integrated_cases"]==w["integrated_case_ids"],f"trace integrated mismatch {row['id']}")
    req(tr["coverage"]["species_profiles"]=="25/25" and tr["coverage"]["actions"]=="30/30" and tr["coverage"]["iar_cases"]=="48/48 exactly once" and tr["coverage"]["species_visual_cases"]=="36/36 exactly once" and tr["coverage"]["integrated_cases"]=="32/32 exactly once","trace coverage declaration incomplete")

    mut=inspector["mutation_protocols"]["P06-MUT-001"]
    req(mut["required"]==["authorization","expected_version","operation_id"],"P06-MUT-001 required fields changed")
    req(mut["version_field"]=="appearance_state_version","appearance version field changed")
    req(mut["ambiguous_result"]==["query_operation_status","query_current_version","compare_committed_receipt","retry_only_if_safe"],"ambiguous recovery changed")
    for key in ["source_biology_mutation","current_form_or_transition_mutation","persistent_history_mutation","equipment_mutation","renderer_coverage_mutation","ai_authoritative_mutation"]:
        req(mut[key] is False,f"mutation boundary weakened: {key}")

    policy=wf["workflow_policy"]
    for key in ["all_species_profiles_exercised","permission_filter_before_reference_resolution","permission_filter_before_derivatives","permission_filter_before_renderer_asset_selection","mutation_requires_P06_MUT_001","expected_version_required_for_write","operation_id_required_for_write","ambiguous_result_recovery_before_retry","semantic_nonvisual_parity_required"]:
        req(policy[key] is True,f"required policy missing: {key}")
    for key in ["hidden_derivative_leak","renderer_output_authoritative","view_output_authoritative","filename_prompt_species_inference","species_form_biology_mutation","equipment_state_mutation","presentation_wardrobe_grants_mechanics","silent_preset_substitution","arbitrary_rotation","pseudo_3d","runtime_activation"]:
        req(policy[key] is False,f"workflow policy weakened: {key}")

    # OVC-027: all rat-humanoid Arthold art is Furashin, while Ratman remains a Species.
    req(any(x.get("id")=="OVC-027" and "all rat-humanoid" in x.get("decision","").lower() and "Furashin" in x.get("decision","") for x in owner["decisions"]),"OVC-027 missing")
    assets=[]
    for name in manifest["art_manifest_parts"]: assets.extend(load(name)["assets"])
    rat_art=[x for x in assets if "ratman" in x["filename"].lower()]
    req(len(rat_art)>=9,"rat-humanoid Arthold reference set unexpectedly small")
    req(all(x.get("species_binding")=="Furashin" and x.get("binding_authority")=="owner_identification_OVC-027" for x in rat_art),"every rat-humanoid Arthold image must bind to Furashin under OVC-027")
    req("Ratman" in expected_species and "Furashin" in expected_species,"Ratman and Furashin must remain distinct Species profiles")
    fur_wf=by["P06-WF-008"]
    req(set(fur_wf["species"])=={"Furashin","Ratman"},"Furashin/Ratman separation workflow changed")

    # Special all-species assertions.
    iw_text=json.dumps(iw,ensure_ascii=False).lower()
    for phrase in ["four legs","four arms","four arborae seasonal","hybrid recomputes","one upstream ascension","persistent markers remain nonerasable","three simultaneous fur colors","one constituent identity","functional/vestigial","humanoid mechanical grammar","rakuuta feathers/ears","kola-ha fins/tail"]:
        req(phrase in iw_text,f"integrated case surface missing {phrase}")

    for phrase in ["all 25 species profiles","16 end-to-end workflows","25 / 25","20 / 20","30 / 30","48 / 48","36 / 36","32 / 32","116","ovc-027","ratman continues","p06-mut-001","fixed 3/4 full-body","no application runtime","ppia-06 remains `started`"]:
        req(phrase in candidate,f"candidate narrative missing {phrase}")

    checkpoint=json.loads((ROOT/"governance/ai/work-state/PPIA-06-attempt-001.json").read_text(encoding="utf-8"))
    req(checkpoint["work_item_id"]=="PPIA-06" and checkpoint["status"]=="started","PPIA-06 must remain started")
    scope=((checkpoint.get("active_substep") or "")+" "+(checkpoint.get("next_action") or "")).lower()
    req("workflow" in scope and "traceability" in scope,"checkpoint no longer selects workflow/traceability")
    req(checkpoint["owner_decision_required"] is False and checkpoint["unresolved_failures"]==[],"unexpected PPIA-06 block")

    print("PPIA-06 INTEGRATED WORKFLOW/TRACEABILITY: PASS")
    print("workflows=16 mutation=14 read_analysis=2 species=25")
    print("coverage=20 projection groups / 30 actions / 9 handoffs")
    print("cases=48 IAR + 36 SpeciesVisual + 32 integrated = 116; inherited cases assigned exactly once")
    print(f"arthold_rat_humanoid_art={len(rat_art)} all=Furashin OVC-027=true Ratman_species_preserved=true")
    print("biology_mutation=false equipment_mutation=false hidden_leak=false arbitrary_rotation=false runtime_activation=false")
    return 0

if __name__=="__main__":
    raise SystemExit(main())
