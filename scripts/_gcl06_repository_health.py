from __future__ import annotations
import hashlib,json,re,tarfile
from pathlib import Path
from typing import Any

COUNTS={"color_signal":20,"nuisance_inconvenience":20,"resource_complication":20,"time_complication":20,"access_route_shift":20,"environmental_change":20,"opposition_change":20,"third_party_arrival":20,"information_reveal":20,"assumption_reversal":20,"relationship_shift":20,"authority_intervention":20,"objective_reframe":20,"advantage_reversal":20,"consequence_echo":20,"cascading_crisis":20,"derailment_recovery":20}
SEVERITY={"color","inconvenience","pressure","setback","crisis"}
FORMS={"complication","escalation","reversal","twist","recovery"}
PRESSURE={"durability-recovery","sustained-output","burst-spike","action-economy","control-denial","mobility-position","environment-hazard","objective-time","information-surprise","attrition-resource","reinforcement-escalation","failure-path"}

def load(root:Path,manifest:dict[str,Any])->list[dict[str,Any]]:
 d=root/"governance/application-planning/gm-construction-library"; s=manifest["storage"]; assert s["encoding"]=="tar.gz+gcl06-dictionary-columnar-v1" and s["hidden_defaults"] is False
 a=d/s["archive"]["path"]; assert a.exists(); assert hashlib.sha256(a.read_bytes()).hexdigest()==s["archive_sha256"],"GCL-06 archive digest drift"
 expected={x["path"]:x for x in s["archive"]["members"]}; out=[]
 with tarfile.open(a,"r:gz") as tf:
  actual={m.name for m in tf.getmembers() if m.isfile()}; assert actual==set(expected),f"GCL-06 archive member drift: {sorted(actual ^ set(expected))}"
  for name,meta in expected.items():
   h=tf.extractfile(name); assert h is not None; p=json.loads(h.read().decode()); assert p["work_item"]=="GCL-06" and p["encoding"]=="gcl06-dictionary-columnar-v1" and p["production_library_content"] is True
   cols,ds=p["columns"],p["dictionaries"]; assert len(cols)==len(set(cols))==len(ds); rows=[]
   for n,row in enumerate(p["records"]):
    assert len(row)==len(cols); vals=[]
    for i,idx in enumerate(row): assert isinstance(idx,int) and 0<=idx<len(ds[i]),f"GCL-06 dictionary index drift: {name} row {n}"; vals.append(ds[i][idx])
    rows.append(dict(zip(cols,vals)))
   assert len(rows)==meta["record_count"]; out.extend(rows)
 return out

def check(root:Path,base:Any)->dict[str,Any]:
 d=root/"governance/application-planning/gm-construction-library"; paths=[d/"GCL_PROGRAM_BACKLOG.json",d/"GCL-06_COMPLICATION_LIBRARY_CONTRACT_v0.1.0.json",d/"GCL-06_COMPLICATION_MATERIALIZATION_PROFILE_v0.1.0.json",d/"GCL-06_COMPLICATION_LIBRARY_MANIFEST_v0.1.0.json",root/"governance/ai/work-state/GCL-06-attempt-001.json"]
 for p in paths: base.require(p)
 backlog,contract,profile,manifest,cp=[base.read_json(p) for p in paths]; assert backlog["program_id"]=="GCL" and backlog["current_item"]=="GCL-06" and backlog["current_item_status"] in {"in_progress","completed_verified"}; item=next(x for x in backlog["tranches"] if x["id"]=="GCL-06"); assert item["status"] in {"in_progress","completed_verified"}
 assert cp["work_item_id"]=="GCL-06" and cp["attempt_id"]=="GCL-06-attempt-001" and cp["status"] in {"in_progress","completed_verified"} and cp["repository"]=="cybalicistjt-stack/multiversal-aioc" and cp["nonauthorization"]
 assert contract["family_id"]=="GCL-FAM-COMPLICATION" and set(contract["complication_families"])==set(COUNTS) and set(contract["severity_bands"])==SEVERITY and set(contract["complication_forms"])==FORMS and set(contract["pressure_dimension_vocabulary"])==PRESSURE
 slots={x["slot_id"] for x in contract["slot_vocabulary"]}; assert len(slots)==len(contract["slot_vocabulary"])
 o=contract["outcome_openness"]; assert profile["deterministic"] is True and profile["hidden_defaults"] is False and profile["target_family_id"]=="GCL-FAM-COMPLICATION" and profile["authority_projection"]["runtime_authority"]=="none" and profile["composition_profile"]["deterministic_manual_path"] is True and profile["structure_mapping"]["difficulty_pressure_levers"]==[]
 assert manifest["record_count"]==340 and manifest["complication_family_count"]==17 and manifest["records_per_complication_family"]==20 and set(manifest["severity_bands"])==SEVERITY and set(manifest["complication_forms"])==FORMS
 q=manifest["quality_rules"]
 for k in ["parameterized","multiple_responses","multiple_continuations","derailment_recovery_first_class","opportunity_bearing","preserve_player_agency","no_forced_outcome","no_mandatory_choice","no_live_state_mutation","no_guaranteed_consequence","owning_domain_acceptance_required"]: assert q[k] is True
 for k in ["difficulty_shaping_authority","reward_or_aftermath_authority","ai_required"]: assert q[k] is False
 assert q["runtime_authority"]==q["canon_authority"]=="none"
 records=load(root,manifest); assert len(records)==340; req=set(contract["compact_record_required_fields"]); forbidden=set(o["forbidden_compact_fields"]); prefixes={x["id"]:x["prefix"] for x in manifest["complication_families"]}; seen=set(); counts={k:0 for k in COUNTS}; sever=set(); forms=set(); play=set(); scopes=set(); needs=set(); pressure=set(); ph=re.compile(r"\{([a-z][a-z0-9_]*)\}")
 for r in records:
  rid=r.get("complication_template_id"); assert req.issubset(r) and not forbidden.intersection(r) and isinstance(rid,str) and rid not in seen; seen.add(rid); fam=r["complication_family"]; assert fam in COUNTS and rid.startswith(prefixes[fam]); counts[fam]+=1
  assert r["no_forced_outcome"] is True and r["no_mandatory_choice"] is True and r["no_live_state_mutation"] is True and r["no_guaranteed_consequence"] is True and r["genre_affinity"]==["genre-neutral"]
  assert r["severity_band"] in SEVERITY and r["complication_form"] in FORMS; sever.add(r["severity_band"]); forms.add(r["complication_form"])
  assert len(r["trigger_prompts"])>=q["minimum_trigger_prompts"] and len(r["escalation_vectors"])>=q["minimum_escalation_vectors"] and len(r["reversal_prompts"])>=q["minimum_reversal_prompts"] and len(r["response_openings"])>=q["minimum_response_openings"] and len(r["continuation_vectors"])>=q["minimum_continuation_vectors"] and len(r["derailment_recovery_prompts"])>=q["minimum_derailment_recovery_prompts"] and len(r["opportunity_openings"])>=q["minimum_opportunity_openings"]
  assert r["slot_ids"] and set(r["slot_ids"]).issubset(slots); text=" ".join([r["complication_pattern"]]+r["trigger_prompts"]+r["escalation_vectors"]+r["reversal_prompts"]+r["response_openings"]+r["continuation_vectors"]+r["derailment_recovery_prompts"]+r["opportunity_openings"]); assert set(ph.findall(text)).issubset(set(r["slot_ids"]))
  ps=set(r["pressure_dimensions"]); assert ps.issubset(PRESSURE); pressure.update(ps); assert r["composition_targets"]; play.update(r["play_emphasis"]); scopes.update(r["scopes"]); needs.update(r["construction_needs"])
 assert counts==COUNTS and len(seen)==340 and sever==SEVERITY and forms==FORMS and counts["derailment_recovery"]==20
 proof=manifest["proof_target_coverage"]["complications_escalations"]; assert proof["minimum"]>=100 and proof["actual"]==340 and proof["met"] is True
 assert set(manifest["discovery_coverage"]["play_emphasis_expected"]).issubset(play) and set(manifest["discovery_coverage"]["scopes_expected"]).issubset(scopes) and set(manifest["discovery_coverage"]["construction_needs_expected"]).issubset(needs) and set(manifest["discovery_coverage"]["severity_bands_expected"])==SEVERITY
 return {"gcl06_status":item["status"],"records":340,"complication_families":17,"records_per_family":[20],"unique_ids":340,"severity_bands":sorted(sever),"complication_forms":sorted(forms),"proof_target_met":True,"derailment_recovery_records":20,"deterministic_materialization":True,"hidden_defaults":False,"runtime_authority":"none","forced_outcome":False,"mandatory_choice":False,"live_state_authority":False,"difficulty_shaping_authority":False,"reward_or_aftermath_authority":False}
