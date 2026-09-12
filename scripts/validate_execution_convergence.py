#!/usr/bin/env python3
"""Validate Multiversal execution-convergence and bounded-CI controls."""
from __future__ import annotations
import argparse,json
from pathlib import Path
from typing import Any
POLICY_PATH="governance/ai/MULTIVERSAL_EXECUTION_CONVERGENCE_POLICY.md"
PROFILE_PATH="governance/ai/runtime/EXECUTION_PROFILE.json"
TAXONOMY_PATH="governance/ai/interaction-system/analysis/EXECUTION_CONVERGENCE_FAILURE_TAXONOMY.json"
SCORECARD_PATH="governance/ai/interaction-system/live/EXECUTION_CONVERGENCE_SCORECARD.json"
REMEDIATION_CHECKPOINT="governance/ai/work-state/MV-CONT-006-attempt-001.json"
LEGACY_WORKFLOW=".github/workflows/self-hosted-windows-runner-smoke.yml"
CURRENT_SELECTOR=".github/workflows/validate-current-family.yml"
SHARED_CORE=".github/workflows/_validation-core-profile.yml"
FAILURE_CLASSES={"feature_implementation","validation_contract","validation_infrastructure","runner_environment","repository_state","owner_only"};BLOCKED_STATES={"blocked_control_plane","blocked_environment","blocked_owner"}
class ConvergenceError(RuntimeError):pass
def require(c,m):
 if not c:raise ConvergenceError(m)
def load_json(root,rel):
 p=root/rel;require(p.is_file(),f"missing required file: {rel}")
 try:v=json.loads(p.read_text(encoding="utf-8"))
 except (OSError,json.JSONDecodeError) as e:raise ConvergenceError(f"invalid JSON {rel}: {e}") from e
 require(isinstance(v,dict),f"expected object JSON: {rel}");return v
def current_service_objective():
 profile=load_json(Path(__file__).resolve().parents[1],PROFILE_PATH);service=profile.get("service_objective");require(isinstance(service,dict),"execution profile service_objective missing");return service
def validate_convergence_control(control,*,status,context,service_objective=None,require_current_service_objective=True):
 if service_objective is None:service_objective=current_service_objective()
 required={"owner_continue_count","execution_cycles","repair_cycles","no_progress_cycles","diagnostic_mode","last_failure_signature","last_failure_class","diagnostic_hypotheses","retry_basis","service_objective"};require(required<=set(control),f"{context}: convergence_control missing {sorted(required-set(control))}")
 for k in ("owner_continue_count","execution_cycles","repair_cycles","no_progress_cycles"):require(isinstance(control[k],int) and control[k]>=0,f"{context}: {k} must be a non-negative integer")
 require(isinstance(control["diagnostic_mode"],bool),f"{context}: diagnostic_mode must be boolean");require(isinstance(control["diagnostic_hypotheses"],list),f"{context}: diagnostic_hypotheses must be an array")
 failure_class=control["last_failure_class"];require(failure_class is None or failure_class in FAILURE_CLASSES,f"{context}: invalid last_failure_class {failure_class!r}");objective=control["service_objective"];require(isinstance(objective,dict),f"{context}: service_objective must be an object")
 if require_current_service_objective:require(objective==service_objective,f"{context}: service objective drift from {PROFILE_PATH}")
 else:
  for k in ("unrelated_historical_validation_jobs_target","reruns_without_changed_evidence_target","post_merge_stale_pointer_target"):require(objective.get(k)==service_objective.get(k),f"{context}: legacy remediation objective drift for {k}")
 if control["repair_cycles"]>=2:require(control["diagnostic_mode"] is True,f"{context}: second repair requires diagnostic_mode");require(bool(control["last_failure_signature"]),f"{context}: diagnostic repair requires last_failure_signature");require(failure_class in FAILURE_CLASSES,f"{context}: diagnostic repair requires classified failure");require(bool(control["diagnostic_hypotheses"]),f"{context}: diagnostic repair requires hypotheses")
 retry=control["retry_basis"]
 if retry is not None:require(isinstance(retry,dict),f"{context}: retry_basis must be null or object");changed=retry.get("changed_since_previous");require(isinstance(changed,list) and any(str(x).strip() for x in changed),f"{context}: retry requires changed_since_previous evidence")
 if control["no_progress_cycles"]>=2:require(status in BLOCKED_STATES or control["diagnostic_mode"] is True,f"{context}: two no-progress cycles require blocked or diagnostic state")
def check(root:Path):
 root=root.resolve();require((root/POLICY_PATH).is_file(),f"missing convergence policy: {POLICY_PATH}");profile=load_json(root,PROFILE_PATH);service=profile.get("service_objective");require(isinstance(service,dict),"execution profile service_objective missing")
 taxonomy=load_json(root,TAXONOMY_PATH);scorecard=load_json(root,SCORECARD_PATH);remediation=load_json(root,REMEDIATION_CHECKPOINT);pointer=load_json(root,"governance/ai/runtime/CURRENT_WORK_POINTER.json");authority=load_json(root,"governance/ai/runtime/ACTIVE_AUTHORITY_REGISTRY.json");workflow_registry=load_json(root,"governance/repository-health/WORKFLOW_LIFECYCLE_REGISTRY.json")
 require(taxonomy.get("work_item_id")=="MV-CONT-006","convergence taxonomy work item mismatch");required_ids={"MV-CONV-RETRY-001","MV-CONV-DIAG-001","MV-CONV-CI-001","MV-CONV-STATE-001","MV-CONV-INTERRUPT-001","MV-CONV-NOPROGRESS-001"};require({x.get("id") for x in taxonomy.get("failure_classes",[])}==required_ids,"convergence failure taxonomy coverage drift")
 targets=scorecard.get("targets",{});operating=scorecard.get("operating_requirement",{});require(operating.get("ordinary_tranche_single_continue_completion_percent")==service.get("ordinary_tranche_single_continue_target_percent"),"live scorecard single-continue requirement drift");require(operating.get("max_execution_cycles_without_genuine_blocker")==service.get("max_execution_cycles_without_genuine_blocker"),"live scorecard execution-cycle requirement drift");require(operating.get("two_continue_measurement_role")=="diagnostic_only","live scorecard must keep two-continue measurement diagnostic-only");require(targets.get("unrelated_historical_validation_jobs")==service.get("unrelated_historical_validation_jobs_target"),"live scorecard unrelated-validation target drift");require(targets.get("reruns_without_changed_evidence")==service.get("reruns_without_changed_evidence_target"),"live scorecard retry target drift");require(targets.get("post_merge_stale_pointer_incidents")==service.get("post_merge_stale_pointer_target"),"live scorecard stale-pointer target drift")
 privacy=scorecard.get("privacy",{});require(privacy.get("aggregation_only") is True,"live scorecard must remain aggregate-only");require(privacy.get("raw_private_transcript_text_published") is False,"raw private transcript publication forbidden");require(remediation.get("work_item_id")=="MV-CONT-006","remediation checkpoint work item mismatch");validate_convergence_control(remediation.get("convergence_control",{}),status=str(remediation.get("status")),context="MV-CONT-006",service_objective=service,require_current_service_objective=False)
 active=pointer.get("active_attempt",{});rel=active.get("checkpoint_path")
 if rel:
  cp=load_json(root,rel);require(cp.get("attempt_id")==active.get("attempt_id"),"current pointer/checkpoint attempt mismatch");require(cp.get("status")==active.get("status"),"current pointer/checkpoint status mismatch")
  if active.get("implementation_authority") is True:validate_convergence_control(cp.get("convergence_control",{}),status=str(cp.get("status")),context=str(active.get("attempt_id")),service_objective=service)
 maintenance=pointer.get("exclusive_control_plane_maintenance")
 if isinstance(maintenance,dict):
  cp=load_json(root,str(maintenance.get("checkpoint_path")));validate_convergence_control(cp.get("convergence_control",{}),status=str(cp.get("status")),context=str(cp.get("attempt_id")),service_objective=service)
 current=authority.get("current",[]);pol=[x for x in current if x.get("path")==POLICY_PATH];require(len(pol)==1 and pol[0].get("lifecycle")=="CURRENT","convergence policy must be registered CURRENT")
 app=workflow_registry.get("repositories",{}).get("cybalicistjt-stack/Multiversal-app",{});live=app.get("live_workflows",[]);paths={x.get("path") for x in live};require(LEGACY_WORKFLOW not in paths,"legacy all-profile workflow remains registered live");require(paths=={SHARED_CORE,CURRENT_SELECTOR},f"application workflow registry drift: {sorted(paths)}")
 selector=next(x for x in live if x.get("path")==CURRENT_SELECTOR);require(selector.get("lifecycle")=="CURRENT","bounded current-tranche selector must be CURRENT");require(selector.get("validation_scope")=="single_governed_profile","bounded selector validation_scope mismatch");require(selector.get("automatic_repository_event_trigger") is True,"bounded selector must validate matching PR changes");observed=scorecard.get("remediation_evidence",{}).get("application_main_after_merge");require(app.get("current_main")==observed,"workflow registry current_main must equal observed post-cleanup application main")
 return {"schema_version":"2.0.0","validator":"scripts/validate_execution_convergence.py","status":"PASS","execution_profile":PROFILE_PATH,"current_attempt":active.get("attempt_id"),"current_attempt_status":active.get("status"),"registered_application_workflows":sorted(paths),"legacy_fanout_registered":False,"single_continue_target_percent":service.get("ordinary_tranche_single_continue_target_percent"),"max_execution_cycles_without_genuine_blocker":service.get("max_execution_cycles_without_genuine_blocker"),"two_continue_measurement_role":"diagnostic_only","live_same_cycle_baseline_percent":scorecard.get("baseline",{}).get("same_cycle_completion_percent")}
def main():
 p=argparse.ArgumentParser();p.add_argument("--root",default=".");p.add_argument("--output");a=p.parse_args()
 try:r=check(Path(a.root))
 except (ConvergenceError,OSError) as e:r={"schema_version":"2.0.0","validator":"scripts/validate_execution_convergence.py","status":"FAIL","error":str(e)}
 payload=json.dumps(r,indent=2,sort_keys=True)+"\n"
 if a.output:Path(a.output).write_text(payload,encoding="utf-8")
 print(payload,end="");return 0 if r["status"]=="PASS" else 1
if __name__=="__main__":raise SystemExit(main())
