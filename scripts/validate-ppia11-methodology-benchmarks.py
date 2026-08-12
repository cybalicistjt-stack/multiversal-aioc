#!/usr/bin/env python3
from __future__ import annotations
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
BASE=ROOT/"governance/application-planning/parallel-preimplementation"
IA=ROOT/"governance/application-planning/internal-alpha/feature-packets"

METHOD=BASE/"PPIA-11_ENCOUNTER_METHODOLOGY_CONTRACT_v0.1.0.json"
SCHEMA=BASE/"PPIA-11_BENCHMARK_ENCOUNTER_SCHEMA_v0.1.0.json"
CASES=BASE/"PPIA-11_BENCHMARK_REFERENCE_CASES_v0.1.0.json"
CANDIDATE=BASE/"PPIA-11_METHODOLOGY_AND_BENCHMARK_CANDIDATE.md"
FOUNDATION=BASE/"PPIA-11_ENCOUNTER_BALANCE_TAXONOMY_v0.1.0.json"
AUTHORITY=BASE/"PPIA-11_AUTHORITY_AND_BOUNDARY_MATRIX_v0.1.0.json"
F012=IA/"MV-IA-F012_ENCOUNTER_BALANCE_MATRIX.json"
CP=ROOT/"governance/ai/work-state/PPIA-11-attempt-001.json"
POINTER=ROOT/"governance/ai/runtime/CURRENT_WORK_POINTER.json"
STATUS=ROOT/"governance/ai/runtime/CURRENT_IMPLEMENTATION_STATUS.json"
BACKLOG=BASE/"PPIA_PROGRAM_BACKLOG.json"

def load(p:Path): return json.loads(p.read_text(encoding="utf-8"))
def req(x,msg):
    if not x: raise AssertionError(msg)

def main():
    for p in (METHOD,SCHEMA,CASES,CANDIDATE,FOUNDATION,AUTHORITY,F012,CP,POINTER,STATUS,BACKLOG):
        req(p.exists(),f"missing {p.relative_to(ROOT)}")
    m,s,c,t,a,f012,cp,pointer,status,backlog=map(load,(METHOD,SCHEMA,CASES,FOUNDATION,AUTHORITY,F012,CP,POINTER,STATUS,BACKLOG))
    narrative=CANDIDATE.read_text(encoding="utf-8").lower()

    req(m["work_item"]==s["work_item"]==c["work_item"]==t["work_item"]==a["work_item"]=="PPIA-11","package identity")
    factor_ids=[x["id"] for x in t["factor_families"]]
    req(factor_ids==[f"P11-F-{i:03d}" for i in range(1,21)],"foundation factor ids")
    pressure=f012["pressureDimensions"]
    expected_pressure=["durability-recovery","sustained-output","burst-spike","action-economy","control-denial","mobility-position","environment-hazard","objective-time","information-surprise","attrition-resource","reinforcement-escalation","failure-path"]
    req(pressure==expected_pressure,"F012 twelve pressure dimensions")
    req(f012["simulationModes"]==["deterministic-script","bounded-seeded-sampling","sensitivity-sweep","regression-replay"],"F012 simulation modes")
    req(len(f012["acceptanceCriteria"])==20 and len(f012["deniedCases"])==48 and len(f012["fixtures"])==10,"F012 acceptance/deny/fixture corpus")

    steps=m["assessment_steps"]
    req(len(steps)==13 and [x["id"] for x in steps]==[f"P11-M-{i:03d}" for i in range(1,14)],"thirteen methodology steps")
    step_factors={fid for x in steps for fid in x["factor_ids"]}
    req(step_factors==set(factor_ids),"methodology covers all twenty factors")
    req(set(m["pressure_dimension_support"])==set(pressure),"methodology covers all twelve pressure dimensions")
    for dim,ids in m["pressure_dimension_support"].items():
        req(ids and set(ids)<=set(factor_ids),f"invalid factor support for {dim}")
    req(len(m["recommendation_types"])==9 and all(x["authority"]!="automatic_mutation" for x in m["recommendation_types"]),"nine advisory recommendation classes")
    req("indeterminate" in m["uncertainty_rule"].lower() and "fabricated precision" in m["uncertainty_rule"].lower(),"indeterminate uncertainty rule")
    blocking=" ".join(m["blocking_invariants"]).lower()
    for phrase in ("no universal cr","no weighted sum","unknown/source-unspecified","mixed-scale","simulation and benchmark output is evidence","ai may explain or propose","no application runtime"):
        req(phrase in blocking,f"methodology invariant missing {phrase}")
    req("approval and scene attachment" in blocking,"approval/attachment boundary")

    required=set(s["required_fields"])
    required_expected={"benchmark_id","version","name","benchmark_class","purpose","rules_profile_ref","schema_ref","pack_lock_ref","context_snapshot","encounter_forms","sides","objective","environment_and_hazards","waves_and_reinforcements","retreat_and_failure_paths","evidence_ledger","factor_review","pressure_dimension_review","comparison_scope","deterministic_protocol","uncertainty","expected_findings","prohibited_claims","calibration_hooks","provenance"}
    req(required==required_expected,"benchmark required fields")
    req(set(s["benchmark_classes"])=={"source_grounded_bounded","synthetic_qa","regression_replay","sensitivity_case","post_playtest_calibration"},"benchmark classes")
    proto=" ".join(s["deterministic_protocol_rules"]).lower()
    for phrase in ("same analysis result","records the seed","changes only named variables","nonmutating","ambiguous service result"):
        req(phrase in proto,f"deterministic protocol missing {phrase}")
    prov=" ".join(s["provenance_rules"]).lower()
    for phrase in ("synthetic qa fixtures are labeled noncanonical","within-domain","authored encounter recommendations","unresolved gaps"):
        req(phrase in prov,f"benchmark provenance missing {phrase}")
    privacy=" ".join(s["privacy_rules"]).lower()
    req("permission filtering occurs before" in privacy and "cannot reveal hidden participants" in privacy,"benchmark privacy boundary")
    req(set(s["prohibited_claims"])=={"balanced","fair","safe","winnable","optimal","guaranteed","universal difficulty","actual player prediction"},"prohibited claims")

    cases=c["cases"]
    req(c["case_count"]==len(cases)==18,"eighteen benchmark cases")
    req([x["id"] for x in cases]==[f"PPIA11-BM-{i:03d}" for i in range(1,19)],"contiguous benchmark ids")
    req(all(x["classification"]=="synthetic_qa_methodology_fixture" and x["noncanonical"] is True for x in cases),"all cases explicitly noncanonical synthetic QA")
    form_union={v for x in cases for v in x["encounter_forms"]}
    dim_union={v for x in cases for v in x["pressure_dimensions"]}
    factor_union={v for x in cases for v in x["factor_ids"]}
    uncertainty_union={x["expected_uncertainty"] for x in cases}
    req(form_union==set(t["encounter_forms"])==set(c["coverage_requirements"]["encounter_forms"]),"all encounter forms covered")
    req(dim_union==set(pressure)==set(c["coverage_requirements"]["pressure_dimensions"]),"all pressure dimensions covered")
    req(factor_union==set(factor_ids)==set(c["coverage_requirements"]["factor_ids"]),"all factor ids covered")
    req(uncertainty_union=={"low","moderate","high","indeterminate"},"all uncertainty bands covered")
    req(set(c["coverage_requirements"]["required_structures"])<=form_union,"required encounter structures covered")
    req(all(set(x["prohibited_claims"])=={"balanced","fair","safe","winnable","optimal","guaranteed"} for x in cases),"case claim prohibitions")

    boss=next(x for x in cases if x["id"]=="PPIA11-BM-003")
    req(boss["structure"]["boss_rules_invented"] is False and any("never invent boss-only" in y for y in boss["expected_findings"]),"boss non-invention")
    mixed_block=next(x for x in cases if x["id"]=="PPIA11-BM-014")
    req(mixed_block["expected_uncertainty"]=="indeterminate" and mixed_block["expected_disposition"]=="indeterminate_blocked" and mixed_block["structure"]["interaction_rule_present"] is False,"mixed-scale indeterminate case")
    replay=next(x for x in cases if x["id"]=="PPIA11-BM-016")
    req(replay["structure"]["simulation_mode"]=="regression-replay" and replay["structure"]["same_inputs_same_versions"] is True,"deterministic replay case")
    hidden=next(x for x in cases if x["id"]=="PPIA11-BM-017")
    req(hidden["expected_disposition"]=="projection_safety_only" and "does not reveal existence/count/timing" in hidden["structure"]["player_projection"],"hidden wave safety")
    calibration=next(x for x in cases if x["id"]=="PPIA11-BM-018")
    req(calibration["expected_disposition"]=="calibration_update" and calibration["structure"]["source_truth_changed"] is False,"calibration source preservation")

    req([x["id"] for x in t["uncertainty_bands"]]==["low","moderate","high","indeterminate"],"foundation uncertainty bands")
    authority=" ".join(a["blocking_invariants"]).lower()
    for phrase in ("no universal cr","within-domain target bands","automatic balance rewrite is prohibited","mixed-scale analysis requires explicit interaction rules","no guaranteed-balance claim"):
        req(phrase in authority,f"authority boundary missing {phrase}")

    for phrase in ("thirteen-step","twelve f012 pressure dimensions","eighteen contiguous","indeterminate/blocked","boss-only","waves and reinforcements","retreat","calibration never silently edits","no weighted sum"):
        req(phrase in narrative,f"candidate narrative missing {phrase}")

    req(cp["work_item_id"]=="PPIA-11" and cp["attempt_id"]=="PPIA-11-attempt-001" and cp["status"] in {"started","in_progress","ready_for_review"},"checkpoint")
    req(cp["branch"]=="governance/ppia-11-encounter-balance-laboratory" and cp["owner_decision_required"] is False and cp["unresolved_failures"]==[],"checkpoint boundary")
    req(pointer["primary_attempt_id"]=="PPIA-11-attempt-001","pointer")
    req(status["primary"]["work_item_id"]=="PPIA-11","status")
    boundaries=backlog["boundaries"]
    for key in ("application_runtime_mutation_authorized","a2_activation_authorized","release_authorized","deployment_authorized","tester_access_authorized","canonical_promotion_without_source_evidence_authorized"):
        req(boundaries[key] is False,f"forbidden boundary enabled: {key}")

    print("PPIA-11 METHODOLOGY & BENCHMARK CONTRACT: PASS")
    print("methodology_steps=13 factors=20 pressure_dimensions=12 recommendation_types=9")
    print("benchmark_cases=18 encounter_forms=%d uncertainty_bands=4" % len(t["encounter_forms"]))
    print("universal_scalar=false guaranteed_balance=false source_rewrite=false runtime_activation=false")
    return 0

if __name__=="__main__":
    raise SystemExit(main())
