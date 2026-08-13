#!/usr/bin/env python3
from __future__ import annotations
import json
from pathlib import Path
from collections import Counter

ROOT=Path(__file__).resolve().parents[1]
BASE=ROOT/"governance/application-planning/parallel-preimplementation"
FILES={
 "foundation_cases":BASE/"PPIA-15_FOUNDATION_REFERENCE_CASES_v0.1.0.json",
 "foundation_gaps":BASE/"PPIA-15_COVERAGE_GAP_MATRIX_v0.1.0.json",
 "foundation_oracle":BASE/"PPIA-15_ORACLE_AND_FIXTURE_RULES_v0.1.0.json",
 "scenarios":BASE/"PPIA-15_EXPANDED_REGRESSION_SCENARIO_LIBRARY_v0.1.0.json",
 "projections":BASE/"PPIA-15_INSPECTOR_PROJECTION_CONTRACTS_v0.1.0.json",
 "actions":BASE/"PPIA-15_ACTION_AND_REFERENCE_CONTRACTS_v0.1.0.json",
 "cases":BASE/"PPIA-15_IAR_REFERENCE_CASES_v0.1.0.json",
 "trace":BASE/"PPIA-15_IAR_TRACEABILITY_MATRIX_v0.1.0.json",
 "package":BASE/"PPIA-15_IAR_PACKAGE_INDEX_v0.1.0.json"}
README=BASE/"PPIA-15_EXPANDED_REGRESSION_IAR_README.md"
BACKLOG=BASE/"PPIA_PROGRAM_BACKLOG.json"
CHECKPOINT=ROOT/"governance/ai/work-state/PPIA-15-attempt-001.json"
POINTER=ROOT/"governance/ai/runtime/CURRENT_WORK_POINTER.json"
STATUS=ROOT/"governance/ai/runtime/CURRENT_IMPLEMENTATION_STATUS.json"
WORKFLOW=ROOT/".github/workflows/validate-ppia-15-expanded-regression-iar.yml"

def fail(m):
 text="PPIA-15 EXPANDED REGRESSION IAR: FAIL — "+m
 print("::error title=PPIA-15 Expanded Regression IAR Validator::"+text.replace("\n","%0A").replace("\r","%0D"))
 raise SystemExit(text)
def req(c,m):
 if not c: fail(m)
def load(p):
 req(p.exists(),f"missing {p.relative_to(ROOT)}")
 return json.loads(p.read_text(encoding="utf-8"))

def main():
 d={k:load(v) for k,v in FILES.items()}
 backlog,checkpoint,pointer,status=map(load,(BACKLOG,CHECKPOINT,POINTER,STATUS))
 for p in (README,WORKFLOW): req(p.exists(),f"missing {p.relative_to(ROOT)}")
 for k in ("scenarios","projections","actions","cases","trace","package"):
  req(d[k].get("work_item_id")=="PPIA-15",f"{k} work item changed")
  req(d[k].get("artifact_version")=="0.1.0",f"{k} artifact version changed")

 fc=d["foundation_cases"]
 req(fc.get("case_count")==32 and len(fc.get("cases",[]))==32,"Foundation 32-case baseline changed")
 req([x.get("id") for x in fc.get("cases",[])]==[f"PPIA15-FC-{i:03d}" for i in range(1,33)],"Foundation case IDs changed")
 gap=d["foundation_gaps"]; rows=gap.get("rows",[])
 req([x.get("awkward_id") for x in rows]==[f"P15-AWK-{i:03d}" for i in range(1,19)],"Foundation awkward rows changed")
 req(Counter(x.get("status") for x in rows)==Counter({"gap_direct":7,"partial_awkward_variant":10,"baseline_covered_no_clone":1}),"Foundation 7/10/1 gap split changed")
 gm=next(x for x in rows if x.get("awkward_id")=="P15-AWK-004")
 req(gm.get("status")=="baseline_covered_no_clone" and "do not clone" in gm.get("foundation_disposition","").lower(),"Foundation GM no-clone baseline changed")
 ot=json.dumps(d["foundation_oracle"],ensure_ascii=False).lower()
 for phrase in ("status-unknown is not failure","offline/local state is not authoritative mutation","silent last-write-wins is forbidden","no balanced/fair/safe/winnable/optimal/guaranteed oracle"): req(phrase in ot,f"Foundation oracle invariant missing {phrase!r}")

 sc=d["scenarios"]; sr=sc.get("scenario_contracts",[])
 req(sc.get("scenario_count")==24 and len(sr)==24,"24 stable scenario contracts changed")
 req([x.get("id") for x in sr]==[f"P15-SCN-{i:03d}" for i in range(1,25)],"scenario IDs changed")
 allowed={f"P15-AWK-{i:03d}" for i in range(1,19)}; covered=set()
 for x in sr:
  awk=set(x.get("awkward_family_ids",[])); req(awk and awk<=allowed,f"invalid awkward binding in {x.get('id')}"); covered|=awk
  for f in ("nearest_inherited_anchors","foundation_case_ids","material_differential","governing_domains","actor_role","context","channel","device_profile","interaction_mode","accessibility_modes","connection_state","fixture_id","operation","expected_authoritative_outcome","projection_group_id","action_ids","expected_recovery_or_conflict","provenance","forbidden_outcomes"): req(x.get(f),f"{x.get('id')} missing {f}")
 req(covered==allowed,"scenario library does not cover all 18 awkward families")
 guard=sc.get("protected_nonclone_baseline",{}); rule=guard.get("rule","").lower()
 req(guard.get("awkward_family_id")=="P15-AWK-004" and "remains inherited coverage" in rule and "p15-scn-005" in rule and "stale-version" in rule,"GM modification protected no-clone guard missing")
 req(sum(1 for x in sr if x.get("awkward_family_ids")==["P15-AWK-004"])==0,"ordinary GM modification was cloned as a standalone scenario")
 sg=sc.get("source_gap_guard",{})
 req(sg.get("foundation_case_id")=="PPIA15-FC-032" and sg.get("provenance")=="P15-PV-004" and "F024" in sg.get("source_gap",""),"F024 source-gap guard changed")
 req(all(v is False for v in sc.get("nonactivation",{}).values()),"scenario nonactivation boundary changed")

 pg=d["projections"]; pgr=pg.get("projection_groups",[])
 req(pg.get("projection_group_count")==12 and len(pgr)==12,"12 Inspector projection groups changed")
 req([x.get("id") for x in pgr]==[f"P15-PG-{i:03d}" for i in range(1,13)],"projection IDs changed")
 pids={x.get("id") for x in pgr}; req(all(x.get("semantic_nonvisual_parity") is True for x in pgr),"nonvisual projection parity changed")
 pgt=json.dumps(pg,ensure_ascii=False).lower()
 for phrase in ("hidden and missing remain externally equivalent","case-local scale fixture sizes","never create mutation"): req(phrase in pgt,f"Inspector rule missing {phrase!r}")

 ac=d["actions"]; ar=ac.get("actions",[])
 req(ac.get("action_count")==20 and len(ar)==20,"20 action/reference contracts changed")
 req([x.get("id") for x in ar]==[f"P15-ACT-{i:03d}" for i in range(1,21)],"action IDs changed")
 aids={x.get("id") for x in ar}; req(all(x.get("ppia15_mutates_authoritative_state") is False for x in ar),"PPIA-15 action gained mutation authority")
 act=json.dumps(ac,ensure_ascii=False).lower()
 for phrase in ("not new application commands or mutation authority","status-unknown never becomes permission to retry blindly","f024 as unsupported"): req(phrase in act,f"action rule missing {phrase!r}")
 for x in sr:
  req(x.get("projection_group_id") in pids,f"{x.get('id')} references unknown projection")
  req(set(x.get("action_ids",[]))<=aids,f"{x.get('id')} references unknown action")

 tr=d["trace"]; fr=tr.get("family_rows",[])
 req([x.get("awkward_id") for x in fr]==[f"P15-AWK-{i:03d}" for i in range(1,19)],"trace family IDs changed")
 sids={x.get("id") for x in sr}
 for x in fr:
  req(x.get("scenario_ids") and set(x.get("scenario_ids"))<=sids,f"trace {x.get('awkward_id')} missing scenario")
  req(x.get("projection_groups") and set(x.get("projection_groups"))<=pids,f"trace {x.get('awkward_id')} missing projection")
  req(x.get("actions") and set(x.get("actions"))<=aids,f"trace {x.get('awkward_id')} missing action")
 tsum=tr.get("coverage_summary",{})
 req((tsum.get("required_awkward_families"),tsum.get("stable_scenario_contracts"),tsum.get("projection_groups"),tsum.get("action_contracts"),tsum.get("ordinary_gm_modification_clone_count"))==(18,24,12,20,0),"trace locked counts changed")
 sgr=tr.get("source_gap_row",{}); req(sgr.get("gap_id")=="P15-GAP-001" and sgr.get("foundation_case_id")=="PPIA15-FC-032" and sgr.get("closure")=="open-not-invented","trace F024 gap changed")

 ca=d["cases"]; cr=ca.get("cases",[])
 req(ca.get("case_count")==40 and ca.get("effective_case_count_with_foundation")==72 and len(cr)==40,"40 IAR / 72 effective accounting changed")
 req([x.get("id") for x in cr]==[f"P15-IAR-{i:03d}" for i in range(1,41)],"IAR IDs changed")
 for x in cr:
  req(x.get("scenario_id") in sids,f"{x.get('id')} references unknown scenario")
  req(x.get("projection_group_id") in pids,f"{x.get('id')} references unknown projection")
  req(x.get("action_ids") and set(x.get("action_ids"))<=aids,f"{x.get('id')} references unknown action")
  for f in ("variant","authoritative_class","projection_class","recovery_class","forbidden"): req(x.get(f),f"{x.get('id')} missing {f}")
 f024=cr[-1]; req(f024.get("id")=="P15-IAR-040" and f024.get("provenance")=="P15-PV-004" and "F024" in f024.get("source_gap","") and f024.get("authoritative_class")=="indeterminate-blocked-source-gap","IAR F024 case changed")
 gr=ca.get("global_requirements",{})
 for k in ("permission_filter_before_derivatives","hidden_missing_equivalence_when_existence_protected","status_unknown_not_failure","accepted_event_distinct_from_projection","offline_local_not_authoritative","semantic_nonvisual_parity","synthetic_noncanonical"): req(gr.get(k) is True,f"IAR safety requirement changed: {k}")
 for k in ("runtime_activation","tester_access","release","deployment","canonical_promotion"): req(gr.get(k) is False,f"IAR activation changed: {k}")

 pk=d["package"]
 req([x.get("id") for x in pk.get("package_artifacts",[])]==[f"P15-IAR-PKG-{i:03d}" for i in range(1,9)],"package IDs changed")
 lc=pk.get("locked_counts",{}); req((lc.get("foundation_cases"),lc.get("stable_scenario_contracts"),lc.get("required_awkward_families"),lc.get("projection_groups"),lc.get("action_contracts"),lc.get("new_iar_cases"),lc.get("effective_cases"),lc.get("ordinary_gm_modification_clones"),lc.get("open_f024_source_gaps"))==(32,24,18,12,20,40,72,0,1),"package counts changed")
 imm=pk.get("immutable_foundation_evidence",{}); req((imm.get("exact_validated_head"),imm.get("hosted_workflows"),imm.get("dedicated_run"),imm.get("pull_request"),imm.get("merge"),imm.get("merge_signature"))==("d876093989e656d3cf8366c19755295ef0f785e8","62/62","31652241636",286,"a1f6b7380a07e65469ba8072e8aa4135d7b1e42f","verified valid"),"immutable Foundation evidence changed")
 acc=pk.get("acceptance",{})
 for k in ("all_18_awkward_families_traced","ordinary_gm_modification_not_cloned","every_scenario_has_material_differential","every_scenario_has_foundation_or_inherited_anchor","every_scenario_binds_projection_and_action_contracts","source_gap_f024_remains_open","synthetic_noncanonical_only","foundation_only_not_ppia15_completion"): req(acc.get(k) is True,f"acceptance changed: {k}")
 for k in ("application_runtime_activation","stage_a_a2_activation","tester_access_activation","release_activation","deployment_activation","paid_service_activation","production_credentials_activation","canonical_promotion"): req(acc.get(k) is False,f"activation changed: {k}")
 req(pk.get("next_milestone")=="PPIA-15 Integrated Expanded Regression Workflows / Traceability","next milestone changed")

 rt=README.read_text(encoding="utf-8").lower()
 for phrase in ("24 stable expanded regression scenario contracts","12 inspector projection groups","20 action/reference contracts","40 new synthetic noncanonical iar cases","72 effective ppia-15 cases","ordinary gm modification remains a protected inherited baseline","p15-gap-001","not ppia-15 completion","integrated expanded regression workflows / traceability"): req(phrase in rt,f"README missing {phrase!r}")

 tranches={x.get("work_item_id"):x for x in backlog.get("tranches",[])}
 for dep in ("PPIA-09","PPIA-10","PPIA-11","PPIA-14"): req(tranches.get(dep,{}).get("status")=="completed_verified",f"{dep} dependency changed")
 current=backlog.get("current_work_item_id")
 req(checkpoint.get("attempt_id")=="PPIA-15-attempt-001" and checkpoint.get("branch")=="governance/ppia-15-internal-alpha-test-content-expansion","checkpoint identity changed")
 req(checkpoint.get("unresolved_failures")==[] and checkpoint.get("owner_decision_required") is False,"PPIA-15 unresolved state")
 if current=="PPIA-15":
  req(tranches.get("PPIA-15",{}).get("status") in {"started","ready_for_review"},"PPIA-15 backlog state changed")
  req(checkpoint.get("status") in {"started","ready_for_review"} and checkpoint.get("completed_at") is None,"active PPIA-15 state changed")
  sub=checkpoint.get("active_substep") or ""
  if "Expanded Regression Scenario Library" in sub:
   mode="active_iar"
  else:
   req(any(s in sub for s in ("Integrated Expanded Regression Workflows","Completion Contract / Evidence Closure")),"PPIA-15 successor milestone is not recognized")
   evidence=json.dumps(checkpoint,ensure_ascii=False)
   for token in ("94029c704fa097f99440a58a64c4293d52b4ad36","31653764114","#287","740683e33ff6e3a0b1a8672c06fbbf9d87fa3bf5"):
    req(token in evidence,f"successor mode missing immutable IAR evidence {token}")
   mode="successor_after_verified_iar"
  req(pointer.get("primary_attempt_id")=="PPIA-15-attempt-001","pointer does not select PPIA-15")
  req(status.get("primary",{}).get("work_item_id")=="PPIA-15" and status.get("primary",{}).get("status") in {"started","ready_for_review"},"compact status does not select PPIA-15")
 else:
  order=backlog.get("execution_order",[])
  req(current in order and order.index(current)>order.index("PPIA-15"),"historical IAR validation only allowed after PPIA-15")
  req(tranches.get("PPIA-15",{}).get("status")=="completed_verified","historical PPIA-15 backlog must be completed_verified")
  req(checkpoint.get("status")=="completed_verified" and checkpoint.get("completed_at"),"historical checkpoint must be completed_verified")
  mode="historical_after_ppia15"
 bounds=backlog.get("boundaries",{})
 for k in ("application_runtime_mutation_authorized","a2_activation_authorized","release_authorized","deployment_authorized","tester_access_authorized","canonical_promotion_without_source_evidence_authorized"): req(bounds.get(k) is False,f"program boundary changed: {k}")
 print("PPIA-15 EXPANDED REGRESSION IAR: PASS")
 print("scenarios=24 awkward_families=18 projections=12 actions=20 new_iar_cases=40 effective_cases=72")
 print("gm_baseline_clones=0 f024_gap=open-not-invented synthetic_noncanonical=true")
 print(f"milestone_mode={mode} runtime_activation=false a2_activation=false tester_access=false release=false deployment=false")
if __name__=="__main__": main()
