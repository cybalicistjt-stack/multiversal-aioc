from __future__ import annotations
import hashlib
from pathlib import Path
from typing import Any
FAMILIES={"opening_kickoff","middle_momentum","finale_resolution","one_shot","short_session","convention_slot","hiatus_return","absent_player","extra_player","split_party","downtime_heavy","investigation_heavy","social_heavy","exploration_heavy","combat_heavy","travel_heavy","recovery_breathing_room","mixed_mode"}
PATTERNS={"cold_open_arc","three_phase","four_phase","modular_blocks","countdown_window","rotating_spotlight","parallel_threads","recap_to_cliffhanger"}
SEGMENTS={"recap_context","entry","establish","develop","pivot","pressure","resolution_window","handoff_closure"}
SLOTS={"recap_or_context","opening_move","primary_activity","secondary_activity","spotlight_rotation","pressure_or_clock","recovery_or_breathing_room","closure_or_handoff"}
TARGETS={"GCL-03","GCL-04","GCL-05","GCL-06","GCL-09","GCL-10","MV-IA-F005","MV-IA-F012","CSW-05","APM-04"}
def _records(lib):
 out=[]; s=lib["shared_record_fields"]
 assert lib["encoding"]=="gcl11-parametric-session-kit-matrix-v1" and lib["hidden_defaults"] is False
 assert len(lib["session_families"])==18 and len(lib["construction_patterns"])==8
 for fi,fam in enumerate(lib["session_families"],1):
  for pi,pat in enumerate(lib["construction_patterns"],1):
   out.append({
    "session_kit_id":f"GCL11-{fi:02d}-{pi:02d}","session_family":fam["session_family"],"construction_pattern":pat["pattern_id"],
    "title":f"{fam['session_family'].replace('_',' ').title()} — {pat['pattern_id'].replace('_',' ').title()}",
    "construction_goal":fam["construction_goal"],"question_shape":fam["question_shape"],"pacing_focus":pat["pacing_focus"],"pattern_rule":pat["pattern_rule"],
    "segment_roles":s["segment_roles"],"component_slots":s["component_slots"],"timing_modes":s["timing_modes"],"attendance_adaptations":s["attendance_adaptations"],
    "spotlight_rules":s["spotlight_rules"],"recovery_modes":s["recovery_modes"],"closure_modes":s["closure_modes"],"projection_rules":s["projection_rules"],
    "provenance_rules":s["provenance_rules"],"scopes":s["scopes"],"genre_affinity":s["genre_affinity"],"composition_targets":s["composition_targets"],
    "authorization_filtered":s["authorization_filtered"],"no_live_session_state":s["no_live_session_state"],"no_launch_snapshot_creation":s["no_launch_snapshot_creation"],
    "no_membership_or_control_mutation":s["no_membership_or_control_mutation"],"no_scene_mutation":s["no_scene_mutation"],"no_event_append":s["no_event_append"],
    "no_hidden_info_leak":s["no_hidden_info_leak"],"no_runtime_outcome_assertion":s["no_runtime_outcome_assertion"],"no_auto_launch":s["no_auto_launch"],
    "no_completeness_guarantee":s["no_completeness_guarantee"],"proposal_only":s["proposal_only"],"ai_required":s["ai_required"]})
 return out
def check(root:Path,base:Any)->dict[str,Any]:
 d=root/"governance/application-planning/gm-construction-library"
 paths=[d/"GCL_PROGRAM_BACKLOG.json",d/"GCL-11_SESSION_CONSTRUCTION_LIBRARY_CONTRACT_v0.1.0.json",d/"GCL-11_SESSION_CONSTRUCTION_MATERIALIZATION_PROFILE_v0.1.0.json",d/"GCL-11_SESSION_CONSTRUCTION_LIBRARY_MANIFEST_v0.1.0.json",d/"GCL-11_SESSION_CONSTRUCTION_LIBRARY_v0.1.0.json",root/"governance/ai/work-state/GCL-11-attempt-001.json"]
 for p in paths:base.require(p)
 backlog,contract,profile,manifest,lib,cp=[base.read_json(p) for p in paths]
 assert backlog["program_id"]=="GCL" and backlog["current_item"]=="GCL-11" and backlog["current_item_status"] in {"in_progress","completed_verified"}
 item=next(x for x in backlog["tranches"] if x["id"]=="GCL-11"); assert item["status"] in {"in_progress","completed_verified"}
 assert cp["work_item_id"]=="GCL-11" and cp["status"] in {"in_progress","completed_verified"} and cp["repository"]=="cybalicistjt-stack/multiversal-aioc"
 assert contract["family_id"]=="GCL-FAM-SESSION-CONSTRUCTION" and set(contract["session_families"])==FAMILIES and set(contract["construction_patterns"])==PATTERNS
 assert set(contract["segment_role_vocabulary"])==SEGMENTS and set(contract["component_slots"])==SLOTS
 assert profile["deterministic"] is True and profile["hidden_defaults"] is False and profile["record_count"]==144 and profile["session_family_count"]==18 and profile["construction_pattern_count"]==8 and profile["records_per_session_family"]==8 and profile["records_per_construction_pattern"]==18
 assert manifest["record_count"]==144 and manifest["session_family_count"]==18 and manifest["construction_pattern_count"]==8 and manifest["records_per_session_family"]==8 and manifest["records_per_construction_pattern"]==18 and manifest["hidden_defaults"] is False
 raw=(d/"GCL-11_SESSION_CONSTRUCTION_LIBRARY_v0.1.0.json").read_bytes(); assert hashlib.sha256(raw).hexdigest()==manifest["library_sha256"],"GCL-11 library digest drift"
 recs=_records(lib); assert len(recs)==144; req=set(contract["required_record_fields"]); ids=set(); fc={x:0 for x in FAMILIES}; pc={x:0 for x in PATTERNS}
 for r in recs:
  assert req.issubset(r); rid=r["session_kit_id"]; assert rid.startswith("GCL11-") and rid not in ids; ids.add(rid)
  fam=r["session_family"]; pat=r["construction_pattern"]; assert fam in FAMILIES and pat in PATTERNS; fc[fam]+=1; pc[pat]+=1
  assert set(r["segment_roles"])==SEGMENTS and set(r["component_slots"])==SLOTS and set(r["composition_targets"])==TARGETS
  assert len(r["timing_modes"])>=6 and len(r["attendance_adaptations"])>=8 and len(r["spotlight_rules"])>=4 and len(r["recovery_modes"])>=8 and len(r["closure_modes"])>=8 and len(r["provenance_rules"])>=3
  assert set(r["projection_rules"])=={"ready_to_use","construction_material"}; assert r["scopes"]==["session","session-preparation","pre-authoritative-construction"] and r["genre_affinity"]==["genre-neutral"]
  for k in ["authorization_filtered","no_live_session_state","no_launch_snapshot_creation","no_membership_or_control_mutation","no_scene_mutation","no_event_append","no_hidden_info_leak","no_runtime_outcome_assertion","no_auto_launch","no_completeness_guarantee","proposal_only"]:assert r[k] is True
  assert r["ai_required"] is False
 assert set(fc.values())=={8} and set(pc.values())=={18} and len(ids)==144
 c=manifest["coverage"]
 for k in ["roadmap_named_session_cases_covered","openings_middles_finales","one_shot","short_session","convention_play","hiatus_recovery","attendance_adaptation","split_party","downtime_heavy","play_mode_emphasis_variants","ready_to_use_projection","construction_material_projection","failure_resistant_handoffs","no_live_session_state","no_launch_snapshot_creation","no_membership_or_control_mutation","no_hidden_info_leak","no_auto_launch"]:assert c[k] is True
 a=contract["authority_contract"]; assert a["no_runtime_mutation"] is True and a["no_completeness_guarantee"] is True and "MV-IA-F005" in a["f005"] and "MV-IA-F012" in a["f012"] and "pre-authoritative" in a["csw05"] and "A9" in a["a9"]
 return {"gcl11_status":item["status"],"records":144,"session_families":18,"construction_patterns":8,"records_per_family":8,"records_per_pattern":18,"roadmap_named_session_cases_covered":True,"ready_to_use_projection":True,"construction_material_projection":True,"live_session_authority":"none","launch_authority":"none","membership_or_control_authority":"none","hidden_information_authority":"none","auto_launch":False}
