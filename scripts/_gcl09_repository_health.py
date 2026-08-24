from __future__ import annotations
import hashlib
from pathlib import Path
from typing import Any
FAMILIES={"hidden_identity","missing_person","hidden_location","missing_object","concealed_motive","secret_method","timeline_reconstruction","sabotage_tampering","infiltration_imposture","conspiracy_network","corruption_abuse","betrayal_double_dealing","hidden_history","false_appearance","anomalous_event","pattern_series","contested_account","causal_chain","locked_access","layered_mystery"}
PATTERNS={"redundancy_web","orthogonal_sources","alternate_route","prerequisite_gate","misleading_but_fair","partial_signal","failure_resilient","hypothesis_discriminator"}
SOURCE_TYPES={"direct_observation","testimony_claim","record_artifact","environmental_trace","relational_signal","action_consequence","external_reference","absence_or_inconsistency"}
EPISTEMIC={"objective_truth","observation","claim","evidence_reference","hypothesis","conclusion","player_knowledge","planned_revelation"}
def _records(lib):
 out=[]; s=lib["shared_record_fields"]
 assert lib["encoding"]=="gcl09-parametric-mystery-matrix-v1" and lib["hidden_defaults"] is False
 assert len(lib["mystery_families"])==20 and len(lib["construction_patterns"])==8
 for fi,fam in enumerate(lib["mystery_families"],1):
  for pi,pat in enumerate(lib["construction_patterns"],1):
   out.append({
    "mystery_kit_id":f"GCL09-{fi:02d}-{pi:02d}",
    "mystery_family":fam["mystery_family"],"construction_pattern":pat["pattern_id"],
    "title":f"{fam['mystery_family'].replace('_',' ').title()} — {pat['pattern_id'].replace('_',' ').title()}",
    "construction_goal":fam["construction_goal"],"question_shape":fam["question_shape"],
    "design_focus":pat["design_focus"],"candidate_move":pat["candidate_move"],"pattern_rule":pat["pattern_rule"],
    "planned_revelation_role":"pre-authoritative design target only; never runtime discovery or objective-truth assertion",
    "source_type_vocabulary":s["source_type_vocabulary"],"epistemic_roles":s["epistemic_roles"],
    "source_selection_prompts":s["source_selection_prompts"],"redundancy_prompts":s["redundancy_prompts"],
    "information_gate_rule":s["information_gate_rule"],"misleading_evidence_rule":s["misleading_evidence_rule"],
    "failure_recovery_modes":s["failure_recovery_modes"],"hypothesis_discrimination_prompts":s["hypothesis_discrimination_prompts"],
    "verification_questions":s["verification_questions"],"fairness_checks":s["fairness_checks"],
    "scopes":s["scopes"],"genre_affinity":s["genre_affinity"],"composition_targets":s["composition_targets"],
    "authorization_filtered":s["authorization_filtered"],"no_runtime_discovery":s["no_runtime_discovery"],
    "no_objective_truth_assertion":s["no_objective_truth_assertion"],"no_hypothesis_resolution":s["no_hypothesis_resolution"],
    "no_universal_clue_count":s["no_universal_clue_count"],"no_forced_solution":s["no_forced_solution"],
    "proposal_only":s["proposal_only"],"no_live_state_mutation":s["no_live_state_mutation"],
    "hidden_existence_safe":s["hidden_existence_safe"],"ai_required":s["ai_required"]})
 return out
def check(root:Path,base:Any)->dict[str,Any]:
 d=root/"governance/application-planning/gm-construction-library"; paths=[d/"GCL_PROGRAM_BACKLOG.json",d/"GCL-09_MYSTERY_INVESTIGATION_LIBRARY_CONTRACT_v0.1.0.json",d/"GCL-09_MYSTERY_INVESTIGATION_MATERIALIZATION_PROFILE_v0.1.0.json",d/"GCL-09_MYSTERY_INVESTIGATION_LIBRARY_MANIFEST_v0.1.0.json",d/"GCL-09_MYSTERY_INVESTIGATION_LIBRARY_v0.1.0.json",root/"governance/ai/work-state/GCL-09-attempt-001.json"]
 for p in paths: base.require(p)
 backlog,contract,profile,manifest,lib,cp=[base.read_json(p) for p in paths]
 assert backlog["program_id"]=="GCL" and backlog["current_item"]=="GCL-09" and backlog["current_item_status"] in {"in_progress","completed_verified"}
 item=next(x for x in backlog["tranches"] if x["id"]=="GCL-09"); assert item["status"] in {"in_progress","completed_verified"}
 assert cp["work_item_id"]=="GCL-09" and cp["status"] in {"in_progress","completed_verified"} and cp["repository"]=="cybalicistjt-stack/multiversal-aioc"
 assert contract["family_id"]=="GCL-FAM-MYSTERY-INVESTIGATION" and set(contract["mystery_families"])==FAMILIES and set(contract["construction_patterns"])==PATTERNS and set(contract["source_type_vocabulary"])==SOURCE_TYPES and set(contract["epistemic_roles"])==EPISTEMIC
 assert profile["deterministic"] is True and profile["hidden_defaults"] is False and profile["record_count"]==160 and profile["mystery_family_count"]==20 and profile["construction_pattern_count"]==8 and profile["records_per_mystery_family"]==8 and profile["records_per_construction_pattern"]==20
 assert manifest["record_count"]==160 and manifest["mystery_family_count"]==20 and manifest["construction_pattern_count"]==8 and manifest["records_per_mystery_family"]==8 and manifest["records_per_construction_pattern"]==20 and manifest["hidden_defaults"] is False
 raw=(d/"GCL-09_MYSTERY_INVESTIGATION_LIBRARY_v0.1.0.json").read_bytes(); assert hashlib.sha256(raw).hexdigest()==manifest["library_sha256"],"GCL-09 library digest drift"
 recs=_records(lib); assert len(recs)==160; req=set(contract["required_record_fields"]); ids=set(); fc={x:0 for x in FAMILIES}; pc={x:0 for x in PATTERNS}
 for r in recs:
  assert req.issubset(r); rid=r["mystery_kit_id"]; assert rid.startswith("GCL09-") and rid not in ids; ids.add(rid)
  fam=r["mystery_family"]; pat=r["construction_pattern"]; assert fam in FAMILIES and pat in PATTERNS; fc[fam]+=1; pc[pat]+=1
  assert set(r["source_type_vocabulary"])==SOURCE_TYPES and set(r["epistemic_roles"])==EPISTEMIC
  assert len(r["source_selection_prompts"])>=4 and len(r["redundancy_prompts"])>=3 and len(r["hypothesis_discrimination_prompts"])>=4 and len(r["verification_questions"])>=5 and len(r["fairness_checks"])>=4 and len(r["failure_recovery_modes"])>=6
  assert r["scopes"]==["mystery","investigation","pre-authoritative-construction"] and r["genre_affinity"]==["genre-neutral"]
  for target in ["CSW-05","A9","GCL-02","GCL-03","GCL-05","GCL-06"]: assert target in r["composition_targets"]
  for k in ["authorization_filtered","no_runtime_discovery","no_objective_truth_assertion","no_hypothesis_resolution","no_universal_clue_count","no_forced_solution","proposal_only","no_live_state_mutation","hidden_existence_safe"]: assert r[k] is True
  assert r["ai_required"] is False
 assert set(fc.values())=={8} and set(pc.values())=={20} and len(ids)==160
 c=manifest["coverage"]
 for k in ["revelation_clue_redundancy","misleading_but_fair","clue_source_alternatives","information_gates","failure_resistant_investigation","hypothesis_discrimination","epistemic_separation","authorization_filtered","no_universal_clue_count","no_runtime_discovery","no_objective_truth_assertion","no_hypothesis_resolution","hidden_existence_safe"]: assert c[k] is True
 a=contract["authority_contract"]; assert a["no_universal_clue_count"] is True and a["no_runtime_mutation"] is True and "runtime clue/discovery" in a["a9"] and "pre-authoritative" in a["csw05"]
 return {"gcl09_status":item["status"],"records":160,"mystery_families":20,"construction_patterns":8,"records_per_family":8,"records_per_pattern":20,"authorization_filtered":True,"universal_clue_count":False,"runtime_discovery_authority":"none","objective_truth_authority":"none","hypothesis_resolution_authority":"none","hidden_existence_leak":False}
