from __future__ import annotations
import hashlib
from pathlib import Path
from typing import Any
DIMS={"durability-recovery","sustained-output","burst-spike","action-economy","control-denial","mobility-position","environment-hazard","objective-time","information-surprise","attrition-resource","reinforcement-escalation","failure-path"}
INTENTS={"ease_pressure","increase_pressure","make_failure_tolerant","reshape_pressure"}
RECS={"composition_delta","timing_wave_delta","environment_hazard_delta","objective_failure_path_delta","resource_constraint_delta","information_visibility_delta"}
NEED={"ease_pressure":"make_easier","increase_pressure":"make_harder","make_failure_tolerant":"recover_from_failure","reshape_pressure":"alternative_shape"}
def _records(lib):
 out=[]; shared=lib["shared_record_fields"]
 assert lib["encoding"]=="gcl07-parametric-matrix-v1" and lib["hidden_defaults"] is False
 assert [x["pressure_dimension"] for x in lib["dimensions"]] and len(lib["dimensions"])==12 and lib["intents"]==["ease_pressure","increase_pressure","make_failure_tolerant","reshape_pressure"]
 for di,d in enumerate(lib["dimensions"],1):
  for ii,intent in enumerate(lib["intents"],1):
   pats=lib["patterns"][intent]; assert len(pats)==3
   for pi,(pid,prompt) in enumerate(pats,1):
    out.append({"pressure_template_id":f"GCL07-{di:02d}-{ii:02d}-{pi:02d}","pressure_dimension":d["pressure_dimension"],"transformation_intent":intent,"pattern_id":pid,"title":f"{intent.replace('_',' ').title()} — {d['pressure_dimension'].replace('-',' ').title()} — {pid.replace('_',' ').title()}","advisory_pattern":prompt.format(pressure_focus=d["pressure_focus"]),"recommendation_type":d["recommendation_type"],"governed_sources":d["governed_sources"],"preconditions":shared["preconditions"],"proposed_deltas":[f"change only a governed source that materially affects {d['pressure_dimension']}","preserve explicit before/after delta visibility","prefer the smallest interpretable change that tests the GM stated intent"],"verification_questions":shared["verification_questions"],"tradeoff_prompts":shared["tradeoff_prompts"],"uncertainty_rule":shared["uncertainty_rule"],"scopes":shared["scopes"],"play_emphasis":[d["pressure_dimension"]],"construction_needs":[NEED[intent]],"genre_affinity":shared["genre_affinity"],"composition_targets":shared["composition_targets"],"no_universal_score":shared["no_universal_score"],"no_balance_guarantee":shared["no_balance_guarantee"],"proposal_only":shared["proposal_only"],"no_live_state_mutation":shared["no_live_state_mutation"],"source_truth_unchanged":shared["source_truth_unchanged"],"ai_required":shared["ai_required"]})
 return out
def check(root:Path,base:Any)->dict[str,Any]:
 d=root/"governance/application-planning/gm-construction-library"; paths=[d/"GCL_PROGRAM_BACKLOG.json",d/"GCL-07_PRESSURE_DIFFICULTY_LIBRARY_CONTRACT_v0.1.0.json",d/"GCL-07_PRESSURE_DIFFICULTY_MATERIALIZATION_PROFILE_v0.1.0.json",d/"GCL-07_PRESSURE_DIFFICULTY_LIBRARY_MANIFEST_v0.1.0.json",d/"GCL-07_PRESSURE_DIFFICULTY_LIBRARY_v0.1.0.json",root/"governance/ai/work-state/GCL-07-attempt-001.json"]
 for p in paths:base.require(p)
 backlog,contract,profile,manifest,lib,cp=[base.read_json(p) for p in paths]
 assert backlog["program_id"]=="GCL" and backlog["current_item"]=="GCL-07" and backlog["current_item_status"] in {"in_progress","completed_verified"}; item=next(x for x in backlog["tranches"] if x["id"]=="GCL-07"); assert item["status"] in {"in_progress","completed_verified"}
 assert cp["work_item_id"]=="GCL-07" and cp["status"] in {"in_progress","completed_verified"} and cp["repository"]=="cybalicistjt-stack/multiversal-aioc"
 assert contract["family_id"]=="GCL-FAM-PRESSURE" and set(contract["pressure_dimensions"])==DIMS and set(contract["transformation_intents"])==INTENTS and set(contract["recommendation_types"])==RECS and set(contract["uncertainty_bands"])=={"low","moderate","high","indeterminate"}
 assert profile["deterministic"] is True and profile["hidden_defaults"] is False and profile["record_count"]==144 and profile["records_per_pressure_dimension"]==12; assert manifest["record_count"]==144 and manifest["pressure_dimension_count"]==12 and manifest["records_per_pressure_dimension"]==12 and manifest["records_per_intent"]==36 and manifest["hidden_defaults"] is False
 raw=(d/"GCL-07_PRESSURE_DIFFICULTY_LIBRARY_v0.1.0.json").read_bytes(); assert hashlib.sha256(raw).hexdigest()==manifest["library_sha256"],"GCL-07 library digest drift"
 recs=_records(lib); assert len(recs)==144; required=set(contract["required_record_fields"]); ids=set(); counts={x:0 for x in DIMS}; intents={x:0 for x in INTENTS}
 for r in recs:
  assert required.issubset(r); rid=r["pressure_template_id"]; assert rid.startswith("GCL07-") and rid not in ids; ids.add(rid); dim=r["pressure_dimension"]; intent=r["transformation_intent"]; assert dim in DIMS and intent in INTENTS; counts[dim]+=1; intents[intent]+=1; assert r["recommendation_type"] in RECS and len(r["proposed_deltas"])>=3 and len(r["verification_questions"])>=3 and len(r["tradeoff_prompts"])>=2; assert r["uncertainty_rule"]=="low/moderate/high/indeterminate only; never fabricate precision" and r["scopes"]==["encounter"] and r["genre_affinity"]==["genre-neutral"] and "PPIA-11" in r["composition_targets"] and "MV-IA-F012" in r["composition_targets"] and r["no_universal_score"] is True and r["no_balance_guarantee"] is True and r["proposal_only"] is True and r["no_live_state_mutation"] is True and r["source_truth_unchanged"] is True and r["ai_required"] is False
 assert set(counts.values())=={12} and set(intents.values())=={36} and len(ids)==144; c=manifest["coverage"]; assert c["all_ppia11_pressure_dimensions"] is True and c["easier_patterns_per_dimension"]==3 and c["harder_patterns_per_dimension"]==3 and c["failure_tolerant_patterns_per_dimension"]==3 and c["alternative_shape_patterns_per_dimension"]==3 and c["no_universal_score"] is True and c["no_balance_guarantee"] is True
 return {"gcl07_status":item["status"],"records":144,"pressure_dimensions":12,"records_per_dimension":12,"records_per_intent":36,"deterministic":True,"hidden_defaults":False,"universal_score":False,"balance_guarantee":False,"runtime_authority":"none","f012_authority_preserved":True}
