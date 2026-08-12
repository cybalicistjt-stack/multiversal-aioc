#!/usr/bin/env python3
from __future__ import annotations
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
BASE=ROOT/"governance/application-planning/parallel-preimplementation"
MATRIX=BASE/"PPIA-11_ENCOUNTER_LAB_INSPECTOR_ACTION_CONTRACT_MATRIX_v0.1.0.json"
CASES=BASE/"PPIA-11_ENCOUNTER_LAB_REFERENCE_CASES_v0.1.0.json"
CANDIDATE=BASE/"PPIA-11_ENCOUNTER_LAB_INSPECTOR_ACTION_REFERENCE_CANDIDATE.md"
TAXONOMY=BASE/"PPIA-11_ENCOUNTER_BALANCE_TAXONOMY_v0.1.0.json"
AUTHORITY=BASE/"PPIA-11_AUTHORITY_AND_BOUNDARY_MATRIX_v0.1.0.json"
METHOD=BASE/"PPIA-11_ENCOUNTER_METHODOLOGY_CONTRACT_v0.1.0.json"
BENCH=BASE/"PPIA-11_BENCHMARK_REFERENCE_CASES_v0.1.0.json"
CHECKPOINT=ROOT/"governance/ai/work-state/PPIA-11-attempt-001.json"
POINTER=ROOT/"governance/ai/runtime/CURRENT_WORK_POINTER.json"
STATUS=ROOT/"governance/ai/runtime/CURRENT_IMPLEMENTATION_STATUS.json"
BACKLOG=BASE/"PPIA_PROGRAM_BACKLOG.json"
METHODOLOGY_MERGE="a5556fb3253baae0f302d9ea9b4b5f582fa9e05e"
PRESSURE=["durability-recovery","sustained-output","burst-spike","action-economy","control-denial","mobility-position","environment-hazard","objective-time","information-surprise","attrition-resource","reinforcement-escalation","failure-path"]


def load(p:Path): return json.loads(p.read_text(encoding="utf-8"))
def req(v,msg):
    if not v: raise AssertionError(msg)


def main():
    for p in (MATRIX,CASES,CANDIDATE,TAXONOMY,AUTHORITY,METHOD,BENCH,CHECKPOINT,POINTER,STATUS,BACKLOG):
        req(p.exists(),f"missing {p.relative_to(ROOT)}")
    m,c,t,a,method,bench,cp,pointer,status,backlog=map(load,(MATRIX,CASES,TAXONOMY,AUTHORITY,METHOD,BENCH,CHECKPOINT,POINTER,STATUS,BACKLOG))
    narrative=CANDIDATE.read_text(encoding="utf-8").lower()

    req(m["work_item"]==c["work_item"]==t["work_item"]==a["work_item"]==method["work_item"]==bench["work_item"]=="PPIA-11","package identity")
    req(m["version"]==c["version"]=="0.1.0","package version")
    req(m["methodology_merge"]==c["methodology_merge"]==METHODOLOGY_MERGE,"methodology merge drift")

    factor_ids=[x["id"] for x in t["factor_families"]]
    req(factor_ids==[f"P11-F-{i:03d}" for i in range(1,21)],"twenty factor ids")
    req([x["id"] for x in t["uncertainty_bands"]]==["low","moderate","high","indeterminate"],"four uncertainty bands")
    req(len(method["assessment_steps"])==13,"thirteen assessment steps")
    req(set(method["pressure_dimension_support"])==set(PRESSURE),"twelve inherited pressure dimensions")
    req(len(a["domain_handoffs"])==10,"ten domain handoffs")

    counts=m["counts"]
    req(counts=={"projection_groups":16,"factor_families":20,"pressure_dimensions":12,"uncertainty_bands":4,"actions":24,"reads":12,"analysis_proposals":8,"writes":4,"inherited_benchmark_cases":18},"matrix counts")
    groups=m["projection_groups"]
    req(len(groups)==16 and [x["id"] for x in groups]==[f"P11-PG-{i:03d}" for i in range(1,17)],"sixteen projection groups")
    req(all(x["fields"] for x in groups),"projection group fields")
    req({fid for g in groups for fid in g["factor_ids"]}==set(factor_ids),"all factors projected")
    req({dim for g in groups for dim in g["pressure_dimensions"]}==set(PRESSURE),"all pressure dimensions projected")
    factor_group=next(x for x in groups if x["id"]=="P11-PG-009")
    pressure_group=next(x for x in groups if x["id"]=="P11-PG-010")
    req(set(factor_group["factor_ids"])==set(factor_ids),"complete factor ledger")
    req(set(pressure_group["pressure_dimensions"])==set(PRESSURE),"complete pressure ledger")
    pol=m["projection_policy"]
    for key in ("filter_before_reference_resolution","filter_before_derivatives","filter_before_counts_aggregates_benchmark_selection_charts_deltas_ai_export","semantic_nonvisual_parity_required","indeterminate_is_first_class"):
        req(pol[key] is True,f"projection policy {key}")
    for key in ("hidden_derivative_leak","chart_graph_authoritative","universal_scalar","weighted_pressure_collapse","source_defaulting"):
        req(pol[key] is False,f"projection prohibition {key}")
    req(pol["mixed_scale_without_interaction_rule"]=="indeterminate_blocked","mixed-scale block")

    actions=m["actions"]
    req(len(actions)==24 and [x["id"] for x in actions]==[f"P11-ACT-{i:03d}" for i in range(1,25)],"twenty-four actions")
    req(len({x["name"] for x in actions})==24,"unique action names")
    reads=[x for x in actions if x["kind"]=="read"]
    analysis=[x for x in actions if x["kind"]=="analysis_proposal"]
    writes=[x for x in actions if x["kind"]=="write"]
    req((len(reads),len(analysis),len(writes))==(12,8,4),"12/8/4 action split")
    required_names={"read_encounter_snapshot","read_factor_ledger","read_pressure_ledger","read_uncertainty_ledger","read_benchmark_candidates","read_benchmark_comparison","read_sensitivity_delta","read_evidence_provenance","read_recommendations","read_calibration_history","read_replay_diagnostics","read_hidden_structure_authorized_projection","assess_encounter_deterministic","compare_benchmark","run_scenario_delta","replay_assessment","propose_encounter_adjustment","propose_benchmark_annotation","propose_calibration_update","preview_authorized_disclosure","accept_advisory_adjustment_into_encounter_draft","record_playtest_observation","record_calibration_outcome","curate_noncanonical_qa_benchmark"}
    req({x["name"] for x in actions}==required_names,"action surface")
    req(all(x["authority"] in {"analysis_only","proposal_only"} for x in analysis),"analysis/proposal authority")
    req(all(x.get("protocol")=="P11-MUT-001" for x in writes),"write protocol binding")
    proto=m["mutation_protocols"]["P11-MUT-001"]
    req(proto["required"]==["authorization","expected_version","operation_id"],"mutation required inputs")
    req(proto["ambiguous_result"]==["query_operation_status","query_current_version","retry_only_if_safe"],"ambiguous recovery")
    for key in ("offline_authoritative_mutation","source_truth_mutation","owning_domain_mechanics_mutation","automatic_balance_rewrite","automatic_canonical_promotion","ai_authoritative_mutation"):
        req(proto[key] is False,f"mutation prohibition {key}")
    req("encounter draft" in proto["draft_acceptance_rule"].lower() and "source facts" in proto["draft_acceptance_rule"].lower(),"draft-only acceptance")
    req("historical evidence" in proto["calibration_rule"].lower() and "immutable" in proto["calibration_rule"].lower(),"historical calibration integrity")
    action_policy=m["action_policy"]
    for key in ("reads_are_permission_filtered","analysis_is_nonmutating","proposal_actions_are_nonauthoritative","writes_are_limited_to_encounter_draft_observation_calibration_or_noncanonical_qa_scope"):
        req(action_policy[key] is True,f"action policy {key}")
    for key in ("owning_domain_source_mutation","automatic_balance_rewrite","automatic_benchmark_canonical_promotion","ai_irreversible_authority","guaranteed_balance_certification"):
        req(action_policy[key] is False,f"action prohibition {key}")

    req(bench["case_count"]==len(bench["cases"])==18,"eighteen inherited benchmarks")
    req([x["id"] for x in bench["cases"]]==[f"PPIA11-BM-{i:03d}" for i in range(1,19)],"benchmark ids")
    imports=c["fixture_imports"]
    req(len(imports)==1 and imports[0]["count"]==18 and imports[0]["resolved_id_range"]=="PPIA11-IR-001..018","benchmark import declaration")
    req(imports[0]["preserve"]==["id","classification","noncanonical","encounter_forms","factor_ids","pressure_dimensions","expected_uncertainty","expected_disposition"],"benchmark preservation fields")
    req(c["imported_case_count"]==18 and c["local_case_count"]==24 and c["resolved_case_count"]==42,"42 resolved cases")
    local=c["local_cases"]
    req([x["id"] for x in local]==[f"PPIA11-IR-{i:03d}" for i in range(19,43)],"local reference ids")
    action_ids={x["id"] for x in actions}; group_ids={x["id"] for x in groups}
    used_actions={v for x in local for v in x["actions"]}; used_groups={v for x in local for v in x["groups"]}
    req(used_actions==action_ids,f"local action coverage gap {sorted(action_ids-used_actions)}")
    req(used_groups==group_ids,f"local projection coverage gap {sorted(group_ids-used_groups)}")
    req(set(c["coverage_requirements"]["actions"])==action_ids and set(c["coverage_requirements"]["projection_groups"])==group_ids,"declared coverage")
    req(all(x["title"] and x["basis"] and x["expected"] for x in local),"local case completeness")
    titles={x["title"] for x in local}
    required_titles={"Unauthorized hidden reinforcement is excluded before derivatives","Unknown source value increases uncertainty without default","Mixed scale without an interaction rule blocks assessment","Incompatible benchmark versions are rejected","Benchmark comparison never normalizes to a universal scalar","Chart and nonvisual projections preserve semantic parity","Deterministic replay reproduces the same assessment","Version change invalidates stale replay","Accepted adjustment changes encounter draft only","AI proposal cannot auto-apply","Compatible duplicate operation id converges","Conflicting operation id reuse fails safely","Ambiguous mutation result recovers before retry","Calibration changes future advisory interpretation only","Permission revocation purges protected cached derivatives","Export and AI context filter hidden state before derivatives","Playtest observation is evidence not source truth","Curated QA benchmark remains noncanonical","Scenario delta changes only named variables","Benchmark annotation proposal cannot canonically promote","Recommendation remains evidence and provenance backed","Factors and pressure dimensions remain independently inspectable"}
    req(required_titles<=titles,f"required cases missing {sorted(required_titles-titles)}")
    req(all(v is False for v in c["policy"].values()),"reference policy")

    authority=" ".join(a["blocking_invariants"]).lower()
    for phrase in ("no universal cr","permission filtering occurs before","unknown/source-unspecified","mixed-scale analysis requires explicit interaction rules","ai may summarize","no guaranteed-balance"):
        req(phrase in authority,f"authority invariant {phrase}")
    method_text=json.dumps(method,ensure_ascii=False).lower()
    for phrase in ("no weighted sum","indeterminate","fabricated precision","simulation and benchmark output is evidence","approval and scene attachment"):
        req(phrase in method_text,f"methodology invariant {phrase}")

    for phrase in ("16 projection groups","24 actions","12 permission-filtered reads","8 nonmutating analysis/proposal","4 narrowly scoped authoritative writes","42 deterministic cases","expected_version","operation_id","permission filtering","semantic list/table/linear","indeterminate_blocked","no universal cr","ai"):
        req(phrase in narrative,f"candidate narrative missing {phrase}")

    req(cp["work_item_id"]=="PPIA-11" and cp["attempt_id"]=="PPIA-11-attempt-001" and cp["branch"]=="governance/ppia-11-encounter-balance-laboratory","checkpoint identity")
    req(cp["status"] in {"started","completed_verified"} and cp.get("owner_decision_required") is False and cp.get("unresolved_failures")==[],"checkpoint state")
    if cp["status"]=="started":
        milestone=((cp.get("active_substep") or "")+" "+(cp.get("next_action") or "")).lower()
        if "inspector" in milestone and "reference" in milestone:
            mode="active_inspector_candidate"
        else:
            history=json.dumps({"last_verified_action":cp.get("last_verified_action"),"completed_substeps":cp.get("completed_substeps",[]),"evidence":cp.get("evidence",[])},ensure_ascii=False).lower()
            req("inspector" in history and "16 projection groups" in history and "24" in history and "42" in history,"historical inspector evidence")
            mode="historical_after_inspector"
        req(pointer["primary_attempt_id"]=="PPIA-11-attempt-001","pointer selection")
        selected=[x for x in pointer["active_attempts"] if x.get("owner_selected")]
        req(len(selected)==1 and selected[0]["attempt_id"]=="PPIA-11-attempt-001","selected PPIA-11 attempt")
        primary=status["primary"]
        for field in ("work_item_id","attempt_id","branch","status","active_substep","next_action","latest_pushed_commit","pull_request","owner_decision_required","unresolved_failures","roadmap_projection_pending"):
            req(primary[field]==cp[field],f"compact status/checkpoint mismatch {field}")
    else:
        mode="historical_after_ppia11"

    boundaries=backlog["boundaries"]
    for key in ("application_runtime_mutation_authorized","a2_activation_authorized","release_authorized","deployment_authorized","tester_access_authorized","canonical_promotion_without_source_evidence_authorized"):
        req(boundaries[key] is False,f"forbidden boundary enabled {key}")

    print("PPIA-11 INSPECTOR / ACTION / REFERENCE: PASS")
    print("projection_groups=16 factors=20 pressure_dimensions=12 uncertainty_bands=4")
    print("actions=24 reads=12 analysis_proposals=8 writes=4")
    print("reference_cases=42 inherited_benchmarks=18 local_cases=24")
    print(f"continuity_mode={mode}")
    print("universal_scalar=false source_rewrite=false hidden_derivative_leak=false guaranteed_balance=false runtime_activation=false")
    return 0

if __name__=="__main__": raise SystemExit(main())
