from __future__ import annotations
import hashlib
from pathlib import Path
from typing import Any
ROLES={"frontliner","defender","skirmisher","artillery","controller","support","ambusher","pursuer","harrier","sniper","disruptor","reinforcer","leader","bodyguard","objective_guardian","hazard_operator","scout","infiltrator","solo_anchor","partner_pair"}
INTENTS={"emphasize_existing_strength","expose_counterplay","shift_positioning","shift_timing_cadence","redistribute_composition","soften_failure_exit"}
PRESSURE={"durability-recovery","sustained-output","burst-spike","action-economy","control-denial","mobility-position","environment-hazard","objective-time","information-surprise","attrition-resource","reinforcement-escalation","failure-path"}
def _records(lib):
 out=[]; shared=lib["shared_record_fields"]
 assert lib["encoding"]=="gcl08-parametric-role-matrix-v1" and lib["hidden_defaults"] is False
 assert len(lib["roles"])==20 and len(lib["intents"])==6
 for ri,role in enumerate(lib["roles"],1):
  for ii,(intent,prompt) in enumerate(lib["intents"],1):
   out.append({"role_kit_id":f"GCL08-{ri:02d}-{ii:02d}","role_family":role["role_family"],"transformation_intent":intent,"title":f"{role['role_family'].replace('_',' ').title()} — {intent.replace('_',' ').title()}","role_goal":role["role_goal"],"source_capability_requirements":role["source_capability_requirements"],"transformation_pattern":prompt.format(role_goal=role["role_goal"]),"allowed_adjustment_surfaces":shared["allowed_adjustment_surfaces"],"pressure_dimensions":role["pressure_dimensions"],"verification_questions":shared["verification_questions"],"counterplay_prompts":shared["counterplay_prompts"],"not_applicable_rule":shared["not_applicable_rule"],"provenance_rule":shared["provenance_rule"],"scopes":shared["scopes"],"genre_affinity":shared["genre_affinity"],"composition_targets":shared["composition_targets"],"source_mechanics_unchanged":shared["source_mechanics_unchanged"],"no_invented_mechanics":shared["no_invented_mechanics"],"no_stat_fabrication":shared["no_stat_fabrication"],"source_authorized_numeric_adjustment_only":shared["source_authorized_numeric_adjustment_only"],"proposal_only":shared["proposal_only"],"no_live_state_mutation":shared["no_live_state_mutation"],"no_balance_guarantee":shared["no_balance_guarantee"],"ai_required":shared["ai_required"]})
 return out
def check(root:Path,base:Any)->dict[str,Any]:
 d=root/"governance/application-planning/gm-construction-library"; paths=[d/"GCL_PROGRAM_BACKLOG.json",d/"GCL-08_ADVERSARY_ROLE_LIBRARY_CONTRACT_v0.1.0.json",d/"GCL-08_ADVERSARY_ROLE_MATERIALIZATION_PROFILE_v0.1.0.json",d/"GCL-08_ADVERSARY_ROLE_LIBRARY_MANIFEST_v0.1.0.json",d/"GCL-08_ADVERSARY_ROLE_LIBRARY_v0.1.0.json",root/"governance/ai/work-state/GCL-08-attempt-001.json"]
 for p in paths: base.require(p)
 backlog,contract,profile,manifest,lib,cp=[base.read_json(p) for p in paths]
 assert backlog["program_id"]=="GCL" and backlog["current_item"]=="GCL-08" and backlog["current_item_status"] in {"in_progress","completed_verified"}; item=next(x for x in backlog["tranches"] if x["id"]=="GCL-08"); assert item["status"] in {"in_progress","completed_verified"}
 assert cp["work_item_id"]=="GCL-08" and cp["status"] in {"in_progress","completed_verified"} and cp["repository"]=="cybalicistjt-stack/multiversal-aioc"
 assert contract["family_id"]=="GCL-FAM-ADVERSARY-ROLE" and set(contract["role_families"])==ROLES and set(contract["transformation_intents"])==INTENTS and set(contract["pressure_dimension_vocabulary"])==PRESSURE
 assert profile["deterministic"] is True and profile["hidden_defaults"] is False and profile["record_count"]==120 and profile["role_family_count"]==20 and profile["records_per_role_family"]==6 and profile["transformation_intent_count"]==6
 assert manifest["record_count"]==120 and manifest["role_family_count"]==20 and manifest["records_per_role_family"]==6 and manifest["records_per_intent"]==20 and manifest["hidden_defaults"] is False
 raw=(d/"GCL-08_ADVERSARY_ROLE_LIBRARY_v0.1.0.json").read_bytes(); assert hashlib.sha256(raw).hexdigest()==manifest["library_sha256"],"GCL-08 library digest drift"
 recs=_records(lib); assert len(recs)==120; req=set(contract["required_record_fields"]); ids=set(); counts={x:0 for x in ROLES}; intents={x:0 for x in INTENTS}; represented=set()
 for r in recs:
  assert req.issubset(r); rid=r["role_kit_id"]; assert rid.startswith("GCL08-") and rid not in ids; ids.add(rid)
  role=r["role_family"]; intent=r["transformation_intent"]; assert role in ROLES and intent in INTENTS; counts[role]+=1; intents[intent]+=1
  assert r["source_capability_requirements"] and len(r["verification_questions"])>=4 and len(r["counterplay_prompts"])>=2 and r["not_applicable_rule"].startswith("If the source lacks")
  ps=set(r["pressure_dimensions"]); assert ps and ps.issubset(PRESSURE); represented.update(ps)
  assert r["scopes"]==["encounter","adversary-role"] and r["genre_affinity"]==["genre-neutral"] and "GCL-07" in r["composition_targets"] and "MV-IA-F012" in r["composition_targets"]
  for k in ["source_mechanics_unchanged","no_invented_mechanics","no_stat_fabrication","source_authorized_numeric_adjustment_only","proposal_only","no_live_state_mutation","no_balance_guarantee"]: assert r[k] is True
  assert r["ai_required"] is False
 assert set(counts.values())=={6} and set(intents.values())=={20} and len(ids)==120 and len(represented)>=10
 c=manifest["coverage"]; assert c["gcl18_adversary_minimum"]>=50 and c["actual"]==120 and c["met"] is True and c["source_capability_gate"] is True and c["not_applicable_first_class"] is True and c["no_invented_mechanics"] is True and c["no_stat_fabrication"] is True and c["no_balance_guarantee"] is True
 return {"gcl08_status":item["status"],"records":120,"role_families":20,"records_per_role":6,"records_per_intent":20,"gcl18_adversary_proof_target_met":True,"source_capability_gate":True,"not_applicable_first_class":True,"invented_mechanics":False,"stat_fabrication":False,"balance_guarantee":False,"runtime_authority":"none"}
