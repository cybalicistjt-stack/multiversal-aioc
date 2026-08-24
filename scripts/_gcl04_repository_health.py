from __future__ import annotations
import json, re, tarfile, hashlib
from pathlib import Path
from typing import Any

PRESSURE={"durability-recovery","sustained-output","burst-spike","action-economy","control-denial","mobility-position","environment-hazard","objective-time","information-surprise","attrition-resource","reinforcement-escalation","failure-path"}
COUNTS={"combat":50,"social":50,"investigation":50,"exploration":25,"travel":25,"stealth":15,"chase":15,"survival":15,"hazard":15,"puzzle_problem":25,"political":25,"hybrid":25,"boss_solo":25}

def load(root:Path, manifest:dict[str,Any])->list[dict[str,Any]]:
    d=root/"governance/application-planning/gm-construction-library"; s=manifest["storage"]
    assert s["encoding"]=="tar.gz+gcl04-dictionary-columnar-v1" and s["hidden_defaults"] is False
    assert s["explicit_inherited_record_fields"]=={"genre_affinity":["genre-neutral"]}
    archive=d/s["archive"]["path"]; assert archive.exists(),f"required path missing: {archive}"
    assert hashlib.sha256(archive.read_bytes()).hexdigest()==s["archive_sha256"],"GCL-04 archive digest drift"
    out=[]; expected={x["path"]:x for x in s["archive"]["members"]}
    with tarfile.open(archive,"r:gz") as tf:
        actual={m.name for m in tf.getmembers() if m.isfile()}; assert actual==set(expected),f"GCL-04 archive member drift: {sorted(actual ^ set(expected))}"
        for name,meta in expected.items():
            h=tf.extractfile(name); assert h is not None
            pack=json.loads(h.read().decode("utf-8")); assert pack["work_item"]=="GCL-04" and pack["encoding"]=="gcl04-dictionary-columnar-v1" and pack["production_library_content"] is True
            cols,dicts=pack["columns"],pack["dictionaries"]; assert len(cols)==len(set(cols))==len(dicts)
            rows=[]
            for n,row in enumerate(pack["records"]):
                assert len(row)==len(cols); vals=[]
                for i,idx in enumerate(row):
                    assert isinstance(idx,int) and 0<=idx<len(dicts[i]),f"GCL-04 dictionary index drift: {name} row {n}"
                    vals.append(dicts[i][idx])
                rows.append(dict(zip(cols,vals)))
            assert len(rows)==meta["record_count"]; out.extend(rows)
    return out

def check(root:Path, base:Any)->dict[str,Any]:
    d=root/"governance/application-planning/gm-construction-library"
    paths=[d/"GCL_PROGRAM_BACKLOG.json",d/"GCL-04_ENCOUNTER_LIBRARY_CONTRACT_v0.1.0.json",d/"GCL-04_ENCOUNTER_MATERIALIZATION_PROFILE_v0.1.0.json",d/"GCL-04_ENCOUNTER_LIBRARY_MANIFEST_v0.1.0.json",root/"governance/ai/work-state/GCL-04-attempt-001.json"]
    for p in paths: base.require(p)
    backlog,contract,profile,manifest,cp=[base.read_json(p) for p in paths]
    assert backlog["program_id"]=="GCL" and backlog["current_item"]=="GCL-04" and backlog["current_item_status"] in {"in_progress","completed_verified"}
    item=next(x for x in backlog["tranches"] if x["id"]=="GCL-04"); assert item["status"] in {"in_progress","completed_verified"}
    assert cp["work_item_id"]=="GCL-04" and cp["attempt_id"]=="GCL-04-attempt-001" and cp["status"] in {"in_progress","completed_verified"} and cp["repository"]=="cybalicistjt-stack/multiversal-aioc" and cp["nonauthorization"]
    assert contract["family_id"]=="GCL-FAM-ENCOUNTER" and set(contract["encounter_families"])==set(COUNTS)
    slots={x["slot_id"] for x in contract["slot_vocabulary"]}; assert len(slots)==len(contract["slot_vocabulary"])
    assert set(contract["pressure_dimension_vocabulary"])==PRESSURE
    db=contract["difficulty_boundary"]; assert db["gcl07_owns_difficulty_shaping"] is True and db["difficulty_pressure_levers_owned_here"] is False and db["universal_scalar_allowed"] is False and db["guaranteed_balance_allowed"] is False
    bb=contract["boss_solo_boundary"]; assert bb["structural_patterns_allowed"] is True and bb["adversary_transformation_owned_here"] is False and bb["source_mechanics_invention_allowed"] is False
    assert profile["deterministic"] is True and profile["hidden_defaults"] is False and profile["target_family_id"]=="GCL-FAM-ENCOUNTER"
    assert profile["authority_projection"]["runtime_authority"]=="none" and profile["authority_projection"]["requires_owning_domain_acceptance"] is True
    assert profile["composition_profile"]["deterministic_manual_path"] is True and profile["composition_profile"]["result_authority"]=="proposal_requires_owning_domain_acceptance"
    assert profile["structure_mapping"]["difficulty_pressure_levers"]==[]
    fb=profile["forbidden_materialization_behavior"]; assert any("universal Challenge Rating" in x for x in fb) and any("boss/solo mechanics" in x for x in fb)
    assert manifest["record_count"]==360 and manifest["encounter_family_count"]==13 and set(manifest["pressure_dimension_vocabulary"])==PRESSURE and manifest["storage"]["encoding"]=="tar.gz+gcl04-dictionary-columnar-v1"
    assert {x["id"] for x in manifest["encounter_families"]}==set(COUNTS)
    q=manifest["quality_rules"]
    for k in ["parameterized","multiple_approaches","no_balance_claim","no_resolved_outcome","owning_domain_acceptance_required"]: assert q[k] is True
    for k in ["campaign_local_encounter_authority","difficulty_shaping_authority","adversary_transformation_authority","ai_required"]: assert q[k] is False
    assert q["runtime_authority"]==q["canon_authority"]=="none"
    records=load(root,manifest); assert len(records)==360
    req=set(contract["compact_record_required_fields"]); forbidden=set(contract["solution_openness"]["forbidden_compact_fields"]); prefix={x["id"]:x["prefix"] for x in manifest["encounter_families"]}
    seen=set(); counts={k:0 for k in COUNTS}; play=set(); needs=set(); pressure=set(); ph=re.compile(r"\{([a-z][a-z0-9_]*)\}")
    for r in records:
        rid=r.get("encounter_template_id"); assert req.issubset(r) and not forbidden.intersection(r) and isinstance(rid,str) and rid.startswith("gcl:encounter.") and rid not in seen; seen.add(rid)
        fam=r["encounter_family"]; assert fam in COUNTS and rid.startswith(prefix[fam]); counts[fam]+=1
        assert r["no_balance_claim"] is True and r["no_resolved_outcome"] is True and r["genre_affinity"]==["genre-neutral"] and r["scopes"]==["encounter"]
        assert len(r["objective_prompts"])>=q["minimum_objective_prompts_per_record"] and len(r["pressure_dimensions"])>=q["minimum_pressure_dimensions_per_record"] and len(r["escalation_prompts"])>=q["minimum_escalation_prompts_per_record"] and len(r["exit_vectors"])>=q["minimum_exit_vectors_per_record"] and len(r["alternative_approaches"])>=q["minimum_alternative_approaches_per_record"]
        assert r["slot_ids"] and set(r["slot_ids"]).issubset(slots); found=set(ph.findall(r["structure_pattern"]+" "+r["setup_pattern"])); assert found.issubset(set(r["slot_ids"]))
        ps=set(r["pressure_dimensions"]); assert ps.issubset(PRESSURE) and r["composition_targets"]; pressure.update(ps); play.update(r["play_emphasis"]); needs.update(r["construction_needs"])
    assert counts==COUNTS and pressure==PRESSURE
    proof=manifest["proof_target_coverage"]; assert counts["combat"]>=proof["combat"]["minimum"] and counts["social"]>=proof["social"]["minimum"] and counts["investigation"]>=proof["investigation"]["minimum"] and counts["exploration"]+counts["travel"]>=proof["exploration_travel"]["minimum"] and counts["chase"]+counts["stealth"]>=proof["chase_stealth"]["minimum"] and counts["hazard"]+counts["survival"]>=proof["hazard_survival"]["minimum"] and counts["puzzle_problem"]>=proof["puzzle_problem"]["minimum"] and counts["boss_solo"]>=proof["boss_solo"]["minimum"]
    assert set(manifest["discovery_coverage"]["play_emphasis_expected"]).issubset(play) and set(manifest["discovery_coverage"]["construction_needs_expected"]).issubset(needs)
    return {"gcl04_status":item["status"],"records":360,"encounter_families":13,"family_counts":counts,"unique_ids":360,"proof_targets_met":True,"deterministic_materialization":True,"hidden_defaults":False,"runtime_authority":"none","universal_balance_claim":False,"difficulty_shaping_authority":False,"adversary_transformation_authority":False,"pressure_dimensions_covered":12}
