#!/usr/bin/env python3
from __future__ import annotations
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
B=ROOT/"governance/application-planning/parallel-preimplementation"
CHECKPOINT=ROOT/"governance/ai/work-state/PPIA-06-attempt-001.json"

FILES={
 "owner":B/"PPIA-06_OWNER_VISUAL_CANON_DECISIONS_v0.1.0.json",
 "authority":B/"PPIA-06_SPECIES_VISUAL_AUTHORITY_MANIFEST_v0.1.0.json",
 "art4":B/"PPIA-06_SPECIES_VISUAL_ART_FILES_PART_04_v0.1.0.json",
 "taxonomy":B/"PPIA-06_APPEARANCE_SEMANTIC_TAXONOMY_v0.2.0.json",
 "profiles":B/"PPIA-06_SPECIES_MORPHOLOGY_PROFILES_v0.1.0.json",
 "species_cases":B/"PPIA-06_SPECIES_VISUAL_REFERENCE_CASES_v0.1.0.json",
 "surface":B/"PPIA-06_APPEARANCE_STUDIO_CONTROL_SURFACE_v0.1.0.json",
 "contract":B/"PPIA-06_APPEARANCE_INSPECTOR_ACTION_CONTRACT_MATRIX_v0.1.0.json",
 "preset":B/"PPIA-06_PRESET_RANDOMIZATION_IMPORT_EXPORT_CONTRACT_v0.1.0.json",
 "cases":B/"PPIA-06_APPEARANCE_INSPECTOR_REFERENCE_CASES_v0.1.0.json",
 "candidate":B/"PPIA-06_INSPECTOR_ACTION_REFERENCE_CANDIDATE.md",
}

def fail(m:str)->None:
    raise SystemExit("PPIA-06 INSPECTOR/ACTION/REFERENCE: FAIL — "+m)

def need(c:bool,m:str)->None:
    if not c: fail(m)

def load(path:Path):
    need(path.exists(),"missing "+str(path.relative_to(ROOT)))
    return json.loads(path.read_text(encoding="utf-8")) if path.suffix==".json" else path.read_text(encoding="utf-8")

def main()->None:
    d={k:load(v) for k,v in FILES.items()}
    cp=load(CHECKPOINT)

    owner=d["owner"]
    need(any(x.get("id")=="OVC-026" and "Furashin" in x.get("decision","") for x in owner["decisions"]),"OVC-026 Furashin rat-ninja correction missing")
    need("non-authoritative" in owner["source_authority_policy"].get("filename_or_prompt_label","").lower(),"filename/prompt non-authority policy missing")
    authority=d["authority"]
    need("non-authoritative" in authority["art_policy"].get("filename_or_prompt_label","").lower(),"authority manifest filename rule missing")
    art4=d["art4"]
    ninja=[x for x in art4["assets"] if "ratman ninja" in x["filename"].lower()]
    need(len(ninja)==1,"rat-ninja art record missing or duplicated")
    need(ninja[0].get("species_binding")=="Furashin","rat-ninja art must bind to Furashin")
    need(ninja[0].get("binding_authority")=="owner_identification_OVC-026","rat-ninja binding authority missing")

    taxonomy=d["taxonomy"]
    need(taxonomy["schema_version"]=="0.2.0","taxonomy v0.2 required")
    need(len(taxonomy["identity_state_layers"])==18,"expected 18 semantic layers")
    need(len(taxonomy["compatibility_dimensions"])==5,"expected 5 compatibility dimensions")
    need("constituent_body" in taxonomy["morphology_graph_contract"]["node_kinds"],"composite morphology node missing")
    profiles=d["profiles"]
    need(profiles["profile_count"]==25 and len(profiles["profiles"])==25,"25 Species morphology profiles required")
    species={x["species"] for x in profiles["profiles"]}
    for name in ["Arborae","Mythragara","Nekron","Suula","Furashin","ManyToms","Stygian","Toba-Madra","The Free","Vespin","Moravi","Rakuuta"]:
        need(name in species,"missing special Species profile "+name)
    inherited=d["species_cases"]
    need(inherited.get("case_count")==36 and len(inherited.get("cases",[]))==36,"36 inherited Species visual cases required")

    surface=d["surface"]
    need(len(surface["inspector_sections"])==18,"Appearance Studio must define 18 Inspector sections")
    section_ids=[x["id"] for x in surface["inspector_sections"]]
    need(len(section_ids)==len(set(section_ids)),"duplicate Inspector section IDs")
    low_surface=json.dumps(surface,ensure_ascii=False).lower()
    for phrase in ["fixed 3/4 full-body master","portrait/zoom","tactical token","free rotation","screen-reader","high-zoom","filename labels on reference art do not define species"]:
        need(phrase.lower() in low_surface,"control surface missing "+phrase)
    for name in ["Arborae","Mythragara","Nekron","Suula","Furashin","ManyToms","Stygian","Toba-Madra","The Free","Vespin","Moravi","Rakuuta"]:
        need(name in surface["profile_behaviors"],"control surface missing special behavior "+name)

    contract=d["contract"]
    counts=contract["counts"]
    need(counts=={"projection_groups":20,"semantic_layers":18,"compatibility_dimensions":5,"actions":30,"reads":12,"analysis_proposals":10,"writes":8,"inherited_species_reference_cases":36},"contract counts changed unexpectedly")
    groups=contract["projection_groups"]
    actions=contract["actions"]
    need(len(groups)==20 and len(actions)==30,"projection/action count mismatch")
    expected_groups={f"P06-PG-{i:03d}" for i in range(1,21)}
    expected_actions={f"P06-ACT-{i:03d}" for i in range(1,31)}
    need({x["id"] for x in groups}==expected_groups,"projection group IDs incomplete")
    need({x["id"] for x in actions}==expected_actions,"action IDs incomplete")
    bykind={k:sum(1 for x in actions if x["kind"]==k) for k in ["read","analysis_proposal","write"]}
    need(bykind=={"read":12,"analysis_proposal":10,"write":8},"action-kind counts mismatch")
    writes=[x for x in actions if x["kind"]=="write"]
    need(all(x.get("protocol")=="P06-MUT-001" for x in writes),"all writes must use P06-MUT-001")
    mut=contract["mutation_protocols"]["P06-MUT-001"]
    need(mut["required"]==["authorization","expected_version","operation_id"],"P06-MUT-001 required fields changed")
    need(mut["version_field"]=="appearance_state_version","appearance version field mismatch")
    for key in ["source_biology_mutation","current_form_or_transition_mutation","persistent_history_mutation","equipment_mutation","renderer_coverage_mutation","ai_authoritative_mutation"]:
        need(mut[key] is False,"mutation boundary enabled: "+key)
    policy=contract["projection_policy"]
    for key in ["permission_filter_before_reference_resolution","permission_filter_before_derivatives","permission_filter_before_renderer_asset_selection","permission_filter_before_counts_diagnostics_presets_export_ai_context","semantic_nonvisual_parity_required","unknown_is_first_class","humanoid_default_forbidden"]:
        need(policy[key] is True,"projection policy disabled: "+key)
    need(policy["filename_prompt_species_inference"] is False,"filename/prompt Species inference must be false")

    preset=d["preset"]
    need(len(preset["preset_scopes"])==6,"expected six preset scopes")
    need(len(preset["import_classifications"])==9,"import classifications incomplete")
    need("seed" in preset["randomization_inputs"] and "lock_set" in preset["randomization_inputs"],"deterministic randomization inputs incomplete")
    low_preset=json.dumps(preset,ensure_ascii=False).lower()
    for phrase in ["no silent substitution","required anatomy cannot be removed","equipment ownership/equipped state cannot be randomized","renderer_filename_identity_forbidden"]:
        need(phrase in low_preset,"preset/randomization contract missing "+phrase)

    cases=d["cases"]
    need(cases["counts"]=={"new_inspector_action_reference_cases":48,"inherited_species_visual_cases":36,"effective_case_surface":84},"reference case counts mismatch")
    need(len(cases["cases"])==48,"must define exactly 48 new IAR cases")
    case_ids=[x["id"] for x in cases["cases"]]
    need(len(case_ids)==len(set(case_ids)),"duplicate IAR case IDs")
    covered_groups={g for x in cases["cases"] for g in x.get("projection_groups",[])}
    covered_actions={a for x in cases["cases"] for a in x.get("actions",[])}
    need(covered_groups==expected_groups,"reference cases do not cover every projection group")
    need(covered_actions==expected_actions,"reference cases do not cover every action")
    low_cases=json.dumps(cases,ensure_ascii=False).lower()
    for phrase in ["rat-ninja","4 arms, 2 legs","persistent adaptation","hybrid derives","stale expected_version","duplicate operation_id","hidden biological marker","keyboard-only","screen reader"]:
        need(phrase in low_cases,"reference corpus missing "+phrase)

    candidate=d["candidate"].lower()
    for phrase in ["20 projection groups","30 actions","12 permission-filtered reads","10 nonmutating analysis/proposal actions","8 narrowly scoped writes","p06-mut-001","48 deterministic inspector/action/reference cases","84 cases","rat-ninja","filename/prompt text is explicitly non-authoritative","integrated workflow/traceability"]:
        need(phrase in candidate,"candidate missing "+phrase)
    need(cp["work_item_id"]=="PPIA-06" and cp["status"] in {"started","in_progress"},"PPIA-06 checkpoint must remain active")
    need(cp["branch"]=="governance/ppia-06-character-appearance-creator","PPIA-06 governed branch mismatch")
    scope=(cp.get("active_substep","")+" "+cp.get("next_action","")).lower()
    need("inspector" in scope and "action" in scope and "reference" in scope,"checkpoint no longer covers Inspector/Action/Reference")

    prohibited=(candidate+" "+low_surface+" "+json.dumps(contract).lower())
    for phrase in ["runtime_activation=true","stage-a-a2 activation=true","appearance may grant equipment","appearance may trigger ascension","arbitrary rotation allowed"]:
        need(phrase not in prohibited,"prohibited implication: "+phrase)

    print("PPIA-06 INSPECTOR/ACTION/REFERENCE: PASS")
    print("projection_groups=20 actions=30 reads=12 analysis_proposals=10 writes=8")
    print("new_reference_cases=48 inherited_species_cases=36 effective_cases=84")
    print("species_profiles=25 inspector_sections=18 compatibility_dimensions=5")
    print("mutation_protocol=P06-MUT-001 authorization+expected_version+operation_id idempotent_recovery=true")
    print("furashin_rat_ninja_binding=owner_confirmed filename_prompt_authority=false")
    print("biology_mutation=false equipment_mutation=false hidden_leak=false runtime_activation=false")

if __name__=="__main__":
    main()
