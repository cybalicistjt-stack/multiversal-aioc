#!/usr/bin/env python3
from __future__ import annotations
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
BASE=ROOT/"governance/application-planning/parallel-preimplementation"
BAL=ROOT/"governance/balance"
MANIFEST=BASE/"PPIA-11_SOURCE_MANIFEST_v0.1.0.json"
TAXONOMY=BASE/"PPIA-11_ENCOUNTER_BALANCE_TAXONOMY_v0.1.0.json"
AUTHORITY=BASE/"PPIA-11_AUTHORITY_AND_BOUNDARY_MATRIX_v0.1.0.json"
INVENTORY=BASE/"PPIA-11_SOURCE_AND_DESIGN_INVENTORY.md"
CANDIDATE=BASE/"PPIA-11_FOUNDATION_CANDIDATE.md"
CP=ROOT/"governance/ai/work-state/PPIA-11-attempt-001.json"
POINTER=ROOT/"governance/ai/runtime/CURRENT_WORK_POINTER.json"
STATUS=ROOT/"governance/ai/runtime/CURRENT_IMPLEMENTATION_STATUS.json"
BACKLOG=BASE/"PPIA_PROGRAM_BACKLOG.json"

def load(p:Path): return json.loads(p.read_text(encoding="utf-8"))
def req(x,msg):
    if not x: raise AssertionError(msg)

def main():
    required=[MANIFEST,TAXONOMY,AUTHORITY,INVENTORY,CANDIDATE,CP,POINTER,STATUS,BACKLOG,
      BAL/"8D-007_GOLDEN_CORPUS_CONTRACT.json",BAL/"8D-007_GOLDEN_CORPUS_MANIFEST.json",BAL/"8D-007_RUNTIME_SCENARIO_REGISTRY.json",
      BAL/"8D-007_BALANCE_OBSERVATION_SCHEMA.json",BAL/"8D-007_PEER_GROUP_TARGET_BAND_CONTRACT.json",BAL/"8D-007_COMPLETION_GOVERNANCE.json"]
    for p in required: req(p.exists(),f"missing {p.relative_to(ROOT)}")
    m,t,a,cp,pointer,status,backlog=map(load,(MANIFEST,TAXONOMY,AUTHORITY,CP,POINTER,STATUS,BACKLOG))
    corpus=load(BAL/"8D-007_GOLDEN_CORPUS_CONTRACT.json")
    fixtures=load(BAL/"8D-007_GOLDEN_CORPUS_MANIFEST.json")
    scenarios=load(BAL/"8D-007_RUNTIME_SCENARIO_REGISTRY.json")
    peer=load(BAL/"8D-007_PEER_GROUP_TARGET_BAND_CONTRACT.json")
    completion=load(BAL/"8D-007_COMPLETION_GOVERNANCE.json")
    inv=INVENTORY.read_text(encoding="utf-8").lower(); cand=CANDIDATE.read_text(encoding="utf-8").lower()

    req(m["work_item"]==t["work_item"]==a["work_item"]=="PPIA-11","package identity")
    req([x["id"] for x in m["evidence_classes"]]==["source_truth","inherited_contract","observed_benchmark","authored_methodology","unresolved_gap"],"five evidence classes")
    anchor=m["governed_balance_anchor"]
    req(anchor["coverage_domains"]==18 and anchor["golden_fixtures"]==36 and anchor["deterministic_scenarios"]==24 and anchor["scenario_executions"]==72,"anchor counts")
    req(anchor["non_destructive_recommendations"]==36 and anchor["mutation_sensitivity_cases"]==7,"anchor recommendation/sensitivity counts")
    req(anchor["source_truth_changed"] is False and anchor["installation_residue"]==0 and anchor["blocking_observations"]==0,"anchor integrity")
    req(len(m["inherited_contracts"])==6 and {x["work_item"] for x in m["inherited_contracts"]}=={"PPIA-02","PPIA-03","PPIA-04","PPIA-05","PPIA-07","PPIA-08"},"inherited contract set")
    for x in m["inherited_contracts"]: req((ROOT/x["path"]).exists(),f"missing inherited {x['work_item']}")
    non=" ".join(m["explicit_non_assumptions"]).lower()
    for phrase in ("no universal challenge-rating","within-domain","not source truth","action economy","not numerically interchangeable","map pixels","sci/csl","automatically","does not activate"):
        req(phrase in non,f"non-assumption missing {phrase}")

    req(corpus["documentId"]=="MV-8D-007-CONTRACT-001" and corpus["sourceCorpus"]["datasets"]==20 and corpus["sourceCorpus"]["promotedRecords"]==19199,"8D corpus contract")
    req(len(corpus["coverageMatrix"])==18 and fixtures["fixtureCount"]==len(fixtures["fixtures"])==36,"8D domain/fixture counts")
    req(len(scenarios["scenarios"])==24 and len({x["id"] for x in scenarios["scenarios"]})==24,"8D scenarios")
    crit=completion["completionCriteria"]
    req(crit["scenarioExecutions"]==72 and crit["nonDestructiveRecommendationsRecorded"]==36 and crit["mutationSensitivityCases"]==7,"8D completion counts")
    req(crit["sourceTruthChanged"] is False and completion["governance"]["canonicalSourceMechanicsImmutable"] is True,"8D source truth")
    req(completion["governance"]["automaticBalanceRewriteProhibited"] is True and completion["governance"]["recommendationsRemainSeparate"] is True,"8D recommendation boundary")
    areas=set(anchor["observation_areas"])
    req(areas=={"output","cost","resource_efficiency","survivability","action_economy","range","duration","reliability","compatibility","complexity"},"observation areas")
    req("within-domain" in json.dumps(peer).lower(),"peer comparison scope")

    factors=t["factor_families"]
    req(len(factors)==20 and [x["id"] for x in factors]==[f"P11-F-{i:03d}" for i in range(1,21)],"twenty factor families")
    req([x["id"] for x in t["uncertainty_bands"]]==["low","moderate","high","indeterminate"],"uncertainty bands")
    taxonomy=json.dumps(t,ensure_ascii=False).lower()
    for phrase in ("action_economy","resource_pressure","environment_terrain","boss_elite_solo","waves_reinforcements","retreat_disengagement","mixed_composition_scale","benchmark_fixture_scenario","uncertainty_band_calibration"):
        req(phrase in taxonomy,f"taxonomy missing {phrase}")
    req(len(a["domain_handoffs"])==10 and [x["id"] for x in a["domain_handoffs"]]==[f"P11-HO-{i:03d}" for i in range(1,11)],"ten handoffs")
    auth=json.dumps(a,ensure_ascii=False).lower()
    for phrase in ("no universal cr","within-domain","automatic balance rewrite","permission filtering","mixed-scale","no guaranteed-balance","ai may summarize"):
        req(phrase in auth,f"authority invariant missing {phrase}")

    for phrase in ("five evidence classes","20 independently inspectable","no universal cr","within-domain","sci measures structural/cognitive complexity, not power","map pixels","indeterminate","no guaranteed-balance"):
        req(phrase in inv+" "+cand,f"narrative missing {phrase}")

    req(cp["work_item_id"]=="PPIA-11" and cp["attempt_id"]=="PPIA-11-attempt-001" and cp["status"] in {"started","in_progress","ready_for_review","completed_verified"},"PPIA-11 checkpoint")
    req(cp["branch"]=="governance/ppia-11-encounter-balance-laboratory" and cp["owner_decision_required"] is False and cp["unresolved_failures"]==[],"PPIA-11 checkpoint boundary")
    if cp["status"] == "completed_verified":
        req(pointer["primary_attempt_id"] != "PPIA-11-attempt-001","historical pointer must advance beyond PPIA-11")
        req(status["primary"]["work_item_id"] != "PPIA-11","historical status projection must advance beyond PPIA-11")
        history=json.dumps({"last_verified_action":cp.get("last_verified_action"),"completed_substeps":cp.get("completed_substeps",[]),"validation":cp.get("validation",[]),"evidence":cp.get("evidence",[])},ensure_ascii=False).lower()
        req("bcd9464ebbf4be7ce15d1764d74890ef12e831fc" in history,"historical foundation merge evidence missing")
        continuity_mode="historical_after_ppia11"
    else:
        req(pointer["primary_attempt_id"]=="PPIA-11-attempt-001","pointer")
        req(status["primary"]["work_item_id"]=="PPIA-11","status projection")
        continuity_mode="active_ppia11"
    boundaries=backlog["boundaries"]
    for key in ("application_runtime_mutation_authorized","a2_activation_authorized","release_authorized","deployment_authorized","tester_access_authorized","canonical_promotion_without_source_evidence_authorized"):
        req(boundaries[key] is False,f"forbidden boundary enabled: {key}")

    print("PPIA-11 FOUNDATION: PASS")
    print("evidence_classes=5 factors=20 uncertainty_bands=4 handoffs=10")
    print("8D007=18 domains / 36 fixtures / 24 scenarios / 72 executions")
    print("source_truth_immutable=true automatic_balance_rewrite=false universal_scalar=false guaranteed_balance=false")
    print(f"continuity_mode={continuity_mode}")
    return 0
if __name__=="__main__": raise SystemExit(main())
