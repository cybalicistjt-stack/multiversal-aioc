from __future__ import annotations
import hashlib
from pathlib import Path
from typing import Any
FAMILIES={"heist","rescue","expedition","siege","mystery_case","faction_sandbox","survival_journey","hunt","political_crisis","point_crawl","branching_dilemma","defense_holdout","infiltration_exfiltration","escort_convoy","exploration_discovery","race_deadline","rebellion_resistance","disaster_response","negotiation_summit","artifact_recovery"}
PATTERNS={"linear_with_offramps","hub_and_spoke","branch_and_reconverge","open_route_network","escalating_clock","layered_objectives","faction_reactive","threshold_loop"}
PHASES={"engagement","orientation","preparation","approach","pressure","reversal","resolution","aftermath"}
SLOTS={"hook_or_premise","situation_or_scene","encounter_archetype","objective_or_stakes","complication_or_escalation","branch_or_route","optional_content","endpoint_or_aftermath"}
TARGETS={"GCL-02","GCL-03","GCL-04","GCL-05","GCL-06","CSW-05","D28","MV-IA-F005","MV-IA-F012","APM-04"}
def _records(lib):
 out=[]; s=lib["shared_record_fields"]
 assert lib["encoding"]=="gcl10-parametric-adventure-matrix-v1" and lib["hidden_defaults"] is False
 assert len(lib["adventure_families"])==20 and len(lib["architecture_patterns"])==8
 for fi,fam in enumerate(lib["adventure_families"],1):
  for pi,pat in enumerate(lib["architecture_patterns"],1):
   out.append({
    "adventure_structure_id":f"GCL10-{fi:02d}-{pi:02d}","adventure_family":fam["adventure_family"],"architecture_pattern":pat["pattern_id"],
    "title":f"{fam['adventure_family'].replace('_',' ').title()} — {pat['pattern_id'].replace('_',' ').title()}",
    "construction_goal":fam["construction_goal"],"question_shape":fam["question_shape"],"design_focus":pat["design_focus"],
    "candidate_move":pat["candidate_move"],"pattern_rule":pat["pattern_rule"],"phase_role_vocabulary":s["phase_role_vocabulary"],
    "component_slots":s["component_slots"],"composition_prompts":s["composition_prompts"],"branch_modes":s["branch_modes"],
    "failure_recovery_modes":s["failure_recovery_modes"],"endpoint_modes":s["endpoint_modes"],"optional_content_modes":s["optional_content_modes"],
    "projection_rules":s["projection_rules"],"provenance_rules":s["provenance_rules"],"scopes":s["scopes"],"genre_affinity":s["genre_affinity"],
    "composition_targets":s["composition_targets"],"authorization_filtered":s["authorization_filtered"],"no_live_adventure_state":s["no_live_adventure_state"],
    "no_d28_identity_creation":s["no_d28_identity_creation"],"no_campaign_scene_session_mutation":s["no_campaign_scene_session_mutation"],
    "no_live_encounter_mutation":s["no_live_encounter_mutation"],"no_forced_route":s["no_forced_route"],"no_required_golden_path":s["no_required_golden_path"],
    "no_runtime_outcome_assertion":s["no_runtime_outcome_assertion"],"no_auto_incorporation":s["no_auto_incorporation"],
    "no_completeness_guarantee":s["no_completeness_guarantee"],"proposal_only":s["proposal_only"],"ai_required":s["ai_required"]})
 return out
def check(root:Path,base:Any)->dict[str,Any]:
 d=root/"governance/application-planning/gm-construction-library"
 paths=[d/"GCL_PROGRAM_BACKLOG.json",d/"GCL-10_ADVENTURE_STRUCTURE_LIBRARY_CONTRACT_v0.1.0.json",d/"GCL-10_ADVENTURE_STRUCTURE_MATERIALIZATION_PROFILE_v0.1.0.json",d/"GCL-10_ADVENTURE_STRUCTURE_LIBRARY_MANIFEST_v0.1.0.json",d/"GCL-10_ADVENTURE_STRUCTURE_LIBRARY_v0.1.0.json",root/"governance/ai/work-state/GCL-10-attempt-001.json"]
 for p in paths:base.require(p)
 backlog,contract,profile,manifest,lib,cp=[base.read_json(p) for p in paths]
 assert backlog["program_id"]=="GCL" and backlog["current_item"]=="GCL-10" and backlog["current_item_status"] in {"in_progress","completed_verified"}
 item=next(x for x in backlog["tranches"] if x["id"]=="GCL-10"); assert item["status"] in {"in_progress","completed_verified"}
 assert cp["work_item_id"]=="GCL-10" and cp["status"] in {"in_progress","completed_verified"} and cp["repository"]=="cybalicistjt-stack/multiversal-aioc"
 assert contract["family_id"]=="GCL-FAM-ADVENTURE-STRUCTURE" and set(contract["adventure_families"])==FAMILIES and set(contract["architecture_patterns"])==PATTERNS
 assert set(contract["phase_role_vocabulary"])==PHASES and set(contract["component_slots"])==SLOTS
 assert profile["deterministic"] is True and profile["hidden_defaults"] is False and profile["record_count"]==160 and profile["adventure_family_count"]==20 and profile["architecture_pattern_count"]==8 and profile["records_per_adventure_family"]==8 and profile["records_per_architecture_pattern"]==20
 assert manifest["record_count"]==160 and manifest["adventure_family_count"]==20 and manifest["architecture_pattern_count"]==8 and manifest["records_per_adventure_family"]==8 and manifest["records_per_architecture_pattern"]==20 and manifest["hidden_defaults"] is False
 raw=(d/"GCL-10_ADVENTURE_STRUCTURE_LIBRARY_v0.1.0.json").read_bytes(); assert hashlib.sha256(raw).hexdigest()==manifest["library_sha256"],"GCL-10 library digest drift"
 recs=_records(lib); assert len(recs)==160; req=set(contract["required_record_fields"]); ids=set(); fc={x:0 for x in FAMILIES}; pc={x:0 for x in PATTERNS}
 for r in recs:
  assert req.issubset(r); rid=r["adventure_structure_id"]; assert rid.startswith("GCL10-") and rid not in ids; ids.add(rid)
  fam=r["adventure_family"]; pat=r["architecture_pattern"]; assert fam in FAMILIES and pat in PATTERNS; fc[fam]+=1; pc[pat]+=1
  assert set(r["phase_role_vocabulary"])==PHASES and set(r["component_slots"])==SLOTS and set(r["composition_targets"])==TARGETS
  assert len(r["composition_prompts"])>=6 and len(r["branch_modes"])>=8 and len(r["failure_recovery_modes"])>=8 and len(r["endpoint_modes"])>=8 and len(r["optional_content_modes"])>=8 and len(r["provenance_rules"])>=3
  assert set(r["projection_rules"])=={"ready_to_use","construction_material"}; assert r["scopes"]==["adventure","quest","mission","pre-authoritative-construction"] and r["genre_affinity"]==["genre-neutral"]
  for k in ["authorization_filtered","no_live_adventure_state","no_d28_identity_creation","no_campaign_scene_session_mutation","no_live_encounter_mutation","no_forced_route","no_required_golden_path","no_runtime_outcome_assertion","no_auto_incorporation","no_completeness_guarantee","proposal_only"]:assert r[k] is True
  assert r["ai_required"] is False
 assert set(fc.values())=={8} and set(pc.values())=={20} and len(ids)==160
 c=manifest["coverage"]; assert c["gcl18_adventure_proof_target_met"] is True and manifest["record_count"]>=50
 for k in ["ready_to_use_projection","construction_material_projection","failure_resistant_routes","optional_content","multiple_endpoint_modes","no_required_golden_path","no_live_adventure_state","no_auto_incorporation"]:assert c[k] is True
 a=contract["authority_contract"]; assert a["no_runtime_mutation"] is True and a["no_completeness_guarantee"] is True and "D28" in a["d28"] and "MV-IA-F005" in a["f005"] and "MV-IA-F012" in a["f012"] and "pre-authoritative" in a["csw05"]
 return {"gcl10_status":item["status"],"records":160,"adventure_families":20,"architecture_patterns":8,"records_per_family":8,"records_per_pattern":20,"gcl18_adventure_proof_target_met":True,"ready_to_use_projection":True,"construction_material_projection":True,"required_golden_path":False,"live_adventure_authority":"none","d28_identity_authority":"none","runtime_outcome_authority":"none","auto_incorporation":False}
