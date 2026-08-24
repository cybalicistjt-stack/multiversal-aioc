from __future__ import annotations
import hashlib,json,re,tarfile
from pathlib import Path
from typing import Any
COUNTS={"acquire_retrieve":20,"protect_escort":20,"escape_evade":20,"survive_endure":20,"reach_traverse":20,"investigate_reveal":20,"negotiate_secure_agreement":20,"disrupt_sabotage":20,"control_hold":20,"race_deadline":20,"repair_restore_transform":20,"competing_multi_objective":20}

def load(root:Path,manifest:dict[str,Any])->list[dict[str,Any]]:
 d=root/"governance/application-planning/gm-construction-library"; s=manifest["storage"]; assert s["encoding"]=="tar.gz+gcl05-dictionary-columnar-v1" and s["hidden_defaults"] is False
 a=d/s["archive"]["path"]; assert a.exists(); assert hashlib.sha256(a.read_bytes()).hexdigest()==s["archive_sha256"],"GCL-05 archive digest drift"
 expected={x["path"]:x for x in s["archive"]["members"]}; out=[]
 with tarfile.open(a,"r:gz") as tf:
  actual={m.name for m in tf.getmembers() if m.isfile()}; assert actual==set(expected),f"GCL-05 archive member drift: {sorted(actual ^ set(expected))}"
  for name,meta in expected.items():
   h=tf.extractfile(name); assert h is not None; p=json.loads(h.read().decode()); assert p["work_item"]=="GCL-05" and p["encoding"]=="gcl05-dictionary-columnar-v1" and p["production_library_content"] is True
   cols,ds=p["columns"],p["dictionaries"]; assert len(cols)==len(set(cols))==len(ds); rows=[]
   for n,row in enumerate(p["records"]):
    assert len(row)==len(cols); vals=[]
    for i,idx in enumerate(row): assert isinstance(idx,int) and 0<=idx<len(ds[i]),f"GCL-05 dictionary index drift: {name} row {n}"; vals.append(ds[i][idx])
    rows.append(dict(zip(cols,vals)))
   assert len(rows)==meta["record_count"]; out.extend(rows)
 return out

def check(root:Path,base:Any)->dict[str,Any]:
 d=root/"governance/application-planning/gm-construction-library"; paths=[d/"GCL_PROGRAM_BACKLOG.json",d/"GCL-05_OBJECTIVE_LIBRARY_CONTRACT_v0.1.0.json",d/"GCL-05_OBJECTIVE_MATERIALIZATION_PROFILE_v0.1.0.json",d/"GCL-05_OBJECTIVE_LIBRARY_MANIFEST_v0.1.0.json",root/"governance/ai/work-state/GCL-05-attempt-001.json"]
 for p in paths: base.require(p)
 backlog,contract,profile,manifest,cp=[base.read_json(p) for p in paths]; assert backlog["program_id"]=="GCL" and backlog["current_item"]=="GCL-05" and backlog["current_item_status"] in {"in_progress","completed_verified"}; item=next(x for x in backlog["tranches"] if x["id"]=="GCL-05"); assert item["status"] in {"in_progress","completed_verified"}
 assert cp["work_item_id"]=="GCL-05" and cp["attempt_id"]=="GCL-05-attempt-001" and cp["status"] in {"in_progress","completed_verified"} and cp["repository"]=="cybalicistjt-stack/multiversal-aioc" and cp["nonauthorization"]
 assert contract["family_id"]=="GCL-FAM-OBJECTIVE" and set(contract["objective_families"])==set(COUNTS); slots={x["slot_id"] for x in contract["slot_vocabulary"]}; assert len(slots)==len(contract["slot_vocabulary"])
 o=contract["outcome_openness"]; profile_ok=profile["deterministic"] is True and profile["hidden_defaults"] is False and profile["target_family_id"]=="GCL-FAM-OBJECTIVE" and profile["authority_projection"]["runtime_authority"]=="none" and profile["composition_profile"]["deterministic_manual_path"] is True and profile["structure_mapping"]["difficulty_pressure_levers"]==[]; assert profile_ok
 assert manifest["record_count"]==240 and manifest["objective_family_count"]==12 and manifest["records_per_objective_family"]==20; q=manifest["quality_rules"]
 for k in ["parameterized","outcome_open","partial_success_first_class","fail_forward_first_class","non_defeat_outcomes_first_class","owning_domain_acceptance_required"]: assert q[k] is True
 for k in ["live_objective_authority","difficulty_shaping_authority","reward_or_aftermath_authority","ai_required"]: assert q[k] is False
 assert q["runtime_authority"]==q["canon_authority"]=="none"
 records=load(root,manifest); assert len(records)==240; req=set(contract["compact_record_required_fields"]); forbidden=set(o["forbidden_compact_fields"]); prefixes={x["id"]:x["prefix"] for x in manifest["objective_families"]}; seen=set(); counts={k:0 for k in COUNTS}; play=set(); scopes=set(); needs=set(); ph=re.compile(r"\{([a-z][a-z0-9_]*)\}")
 for r in records:
  rid=r.get("objective_template_id"); assert req.issubset(r) and not forbidden.intersection(r) and isinstance(rid,str) and rid not in seen; seen.add(rid); fam=r["objective_family"]; assert fam in COUNTS and rid.startswith(prefixes[fam]); counts[fam]+=1
  assert r["no_live_objective_truth"] is True and r["no_guaranteed_outcome"] is True and r["genre_affinity"]==["genre-neutral"]
  assert len(r["success_definition_prompts"])>=q["minimum_success_definition_prompts"] and len(r["partial_success_states"])>=q["minimum_partial_success_states"] and len(r["failure_or_fail_forward_states"])>=q["minimum_failure_or_fail_forward_states"] and len(r["stakes_prompts"])>=q["minimum_stakes_prompts"] and len(r["time_condition_prompts"])>=q["minimum_time_condition_prompts"] and len(r["non_defeat_outcomes"])>=q["minimum_non_defeat_outcomes"] and len(r["competing_priority_prompts"])>=q["minimum_competing_priority_prompts"]
  assert r["slot_ids"] and set(r["slot_ids"]).issubset(slots); text=" ".join([r["objective_pattern"]]+r["success_definition_prompts"]+r["partial_success_states"]+r["failure_or_fail_forward_states"]+r["stakes_prompts"]+r["time_condition_prompts"]+r["competing_priority_prompts"]); assert set(ph.findall(text)).issubset(set(r["slot_ids"])); assert r["composition_targets"]
  play.update(r["play_emphasis"]); scopes.update(r["scopes"]); needs.update(r["construction_needs"])
 assert counts==COUNTS and len(seen)==240 and set(manifest["discovery_coverage"]["play_emphasis_expected"]).issubset(play) and set(manifest["discovery_coverage"]["scopes_expected"]).issubset(scopes) and set(manifest["discovery_coverage"]["construction_needs_expected"]).issubset(needs)
 return {"gcl05_status":item["status"],"records":240,"objective_families":12,"records_per_family":[20],"unique_ids":240,"partial_success_first_class":True,"fail_forward_first_class":True,"non_defeat_outcomes_first_class":True,"deterministic_materialization":True,"hidden_defaults":False,"runtime_authority":"none","live_objective_authority":False,"difficulty_shaping_authority":False,"reward_or_aftermath_authority":False}
