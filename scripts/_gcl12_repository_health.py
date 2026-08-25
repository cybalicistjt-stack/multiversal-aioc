from __future__ import annotations
import hashlib
from pathlib import Path
from typing import Any

FAMILIES={"episodic","serial","sandbox","faction","villain","exploration","mystery","political","military","survival","settlement","mercantile","academy","resistance","dynasty","generational","time_travel","multiversal","cozy","rotating_cast","asynchronous","anthology"}
PATTERNS={"modular_arcs","escalating_serial","hub_and_spoke","open_thread_network","fronts_and_clocks","seasons_and_milestones","legacy_turnover","rotating_focus"}
PHASES={"campaign_premise","establish_anchor","develop_threads","pressure_and_change","pivot_or_reframe","convergence_or_split","transition_or_renewal","legacy_or_endpoint"}
SLOTS={"campaign_premise","anchor_setting_or_frame","recurring_cast_factions","adventure_pipeline","session_rhythm","progression_or_evolution","continuity_legacy","endpoint_or_renewal"}
TARGETS={"GCL-10","GCL-11","MV-IA-F005","CSW-05","D28","APM-04","world/reality-authorities"}

def _records(lib):
 out=[]; s=lib["shared_record_fields"]
 assert lib["encoding"]=="gcl12-parametric-campaign-architecture-matrix-v1" and lib["hidden_defaults"] is False
 assert len(lib["campaign_families"])==22 and len(lib["architecture_patterns"])==8
 for fi,fam in enumerate(lib["campaign_families"],1):
  for pi,pat in enumerate(lib["architecture_patterns"],1):
   out.append({
    "campaign_architecture_id":f"GCL12-{fi:02d}-{pi:02d}",
    "campaign_family":fam["campaign_family"],"architecture_pattern":pat["pattern_id"],
    "title":f"{fam['campaign_family'].replace('_',' ').title()} — {pat['pattern_id'].replace('_',' ').title()}",
    "construction_goal":fam["construction_goal"],"question_shape":fam["question_shape"],
    "design_focus":pat["design_focus"],"pattern_rule":pat["pattern_rule"],
    "phase_roles":s["phase_roles"],"component_slots":s["component_slots"],
    "cadence_modes":s["cadence_modes"],"continuity_modes":s["continuity_modes"],
    "recovery_modes":s["recovery_modes"],"endpoint_modes":s["endpoint_modes"],
    "projection_rules":s["projection_rules"],"provenance_rules":s["provenance_rules"],
    "scopes":s["scopes"],"genre_affinity":s["genre_affinity"],"composition_targets":s["composition_targets"],
    "authorization_filtered":s["authorization_filtered"],"no_live_campaign_state":s["no_live_campaign_state"],
    "no_scene_or_session_mutation":s["no_scene_or_session_mutation"],
    "no_membership_or_control_mutation":s["no_membership_or_control_mutation"],
    "no_adventure_identity_creation":s["no_adventure_identity_creation"],
    "no_world_or_reality_truth_creation":s["no_world_or_reality_truth_creation"],
    "no_runtime_clock_creation":s["no_runtime_clock_creation"],"no_hidden_info_leak":s["no_hidden_info_leak"],
    "no_time_causality_rule_invention":s["no_time_causality_rule_invention"],
    "no_auto_launch_or_direct":s["no_auto_launch_or_direct"],
    "no_completeness_guarantee":s["no_completeness_guarantee"],"proposal_only":s["proposal_only"],"ai_required":s["ai_required"]})
 return out

def check(root:Path,base:Any)->dict[str,Any]:
 d=root/"governance/application-planning/gm-construction-library"
 paths=[d/"GCL_PROGRAM_BACKLOG.json",d/"GCL-12_CAMPAIGN_ARCHITECTURE_LIBRARY_CONTRACT_v0.1.0.json",d/"GCL-12_CAMPAIGN_ARCHITECTURE_MATERIALIZATION_PROFILE_v0.1.0.json",d/"GCL-12_CAMPAIGN_ARCHITECTURE_LIBRARY_MANIFEST_v0.1.0.json",d/"GCL-12_CAMPAIGN_ARCHITECTURE_LIBRARY_v0.1.0.json",root/"governance/ai/work-state/GCL-12-attempt-001.json"]
 for p in paths:base.require(p)
 backlog,contract,profile,manifest,lib,cp=[base.read_json(p) for p in paths]
 assert backlog["program_id"]=="GCL" and backlog["current_item"] in {"GCL-11","GCL-12"}
 item=next(x for x in backlog["tranches"] if x["id"]=="GCL-12"); assert item["status"] in {"ready_to_start","in_progress","completed_verified"}
 assert cp["work_item_id"]=="GCL-12" and cp["status"] in {"in_progress","completed_verified"} and cp["repository"]=="cybalicistjt-stack/multiversal-aioc"
 assert contract["family_id"]=="GCL-FAM-CAMPAIGN-ARCHITECTURE" and set(contract["campaign_families"])==FAMILIES and set(contract["architecture_patterns"])==PATTERNS
 assert set(contract["phase_role_vocabulary"])==PHASES and set(contract["component_slots"])==SLOTS
 assert profile["deterministic"] is True and profile["hidden_defaults"] is False and profile["record_count"]==176 and profile["campaign_family_count"]==22 and profile["architecture_pattern_count"]==8 and profile["records_per_campaign_family"]==8 and profile["records_per_architecture_pattern"]==22
 assert manifest["record_count"]==176 and manifest["campaign_family_count"]==22 and manifest["architecture_pattern_count"]==8 and manifest["records_per_campaign_family"]==8 and manifest["records_per_architecture_pattern"]==22 and manifest["hidden_defaults"] is False
 raw=(d/"GCL-12_CAMPAIGN_ARCHITECTURE_LIBRARY_v0.1.0.json").read_bytes()
 assert hashlib.sha256(raw).hexdigest()==manifest["library_sha256"],"GCL-12 library digest drift"
 recs=_records(lib); assert len(recs)==176
 req=set(contract["required_record_fields"]); ids=set(); fc={x:0 for x in FAMILIES}; pc={x:0 for x in PATTERNS}
 for r in recs:
  assert req.issubset(r); rid=r["campaign_architecture_id"]; assert rid.startswith("GCL12-") and rid not in ids; ids.add(rid)
  fam=r["campaign_family"]; pat=r["architecture_pattern"]; assert fam in FAMILIES and pat in PATTERNS; fc[fam]+=1; pc[pat]+=1
  assert set(r["phase_roles"])==PHASES and set(r["component_slots"])==SLOTS and set(r["composition_targets"])==TARGETS
  assert len(r["cadence_modes"])>=8 and len(r["continuity_modes"])>=8 and len(r["recovery_modes"])>=8 and len(r["endpoint_modes"])>=8 and len(r["provenance_rules"])>=3
  assert set(r["projection_rules"])=={"ready_to_use","construction_material"}
  assert r["scopes"]==["campaign","campaign-preparation","pre-authoritative-construction"] and r["genre_affinity"]==["genre-neutral"]
  for k in ["authorization_filtered","no_live_campaign_state","no_scene_or_session_mutation","no_membership_or_control_mutation","no_adventure_identity_creation","no_world_or_reality_truth_creation","no_runtime_clock_creation","no_hidden_info_leak","no_time_causality_rule_invention","no_auto_launch_or_direct","no_completeness_guarantee","proposal_only"]:assert r[k] is True
  assert r["ai_required"] is False
 assert set(fc.values())=={8} and set(pc.values())=={22} and len(ids)==176
 c=manifest["coverage"]
 for fam in FAMILIES: assert c[fam] is True
 for k in ["all_roadmap_named_campaign_patterns","ready_to_use_projection","construction_material_projection","hiatus_and_turnover_recovery","legacy_and_endpoint_modes","no_live_campaign_state","no_world_or_reality_truth_creation","no_time_causality_rule_invention","no_auto_launch_or_direct"]:assert c[k] is True
 a=contract["authority_contract"]
 assert a["no_runtime_mutation"] is True and a["no_completeness_guarantee"] is True
 assert "MV-IA-F005" in a["f005"] and "D28" in a["d28"] and "pre-authoritative" in a["csw05"]
 assert "cannot invent causality" in a["time_travel"] and "cannot create Reality/World/Branch identities" in a["multiversal"]
 return {"gcl12_status":item["status"],"records":176,"campaign_families":22,"architecture_patterns":8,"records_per_family":8,"records_per_pattern":22,"all_roadmap_named_campaign_patterns":True,"ready_to_use_projection":True,"construction_material_projection":True,"live_campaign_authority":"none","world_reality_truth_authority":"none","temporal_causality_authority":"none","auto_directing":False}
