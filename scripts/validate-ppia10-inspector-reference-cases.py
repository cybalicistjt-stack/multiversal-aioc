#!/usr/bin/env python3
from __future__ import annotations
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
BASE=ROOT/"governance/application-planning/parallel-preimplementation"
MATRIX=BASE/"PPIA-10_INSPECTOR_ACTION_CONTRACT_MATRIX_v0.1.0.json"
CASES=BASE/"PPIA-10_REFERENCE_CASES_v0.1.0.json"
CANDIDATE=BASE/"PPIA-10_INSPECTOR_ACTION_REFERENCE_CANDIDATE.md"
TAXONOMY=BASE/"PPIA-10_RELATIONSHIP_SOCIAL_FACTION_TAXONOMY_v0.1.0.json"
AUTHORITY=BASE/"PPIA-10_AUTHORITY_AND_BOUNDARY_MATRIX_v0.1.0.json"
SOURCE=BASE/"PPIA-10_SOURCE_MANIFEST_v0.1.0.json"
IA=ROOT/"governance/application-planning/internal-alpha/feature-packets"
F009=IA/"MV-IA-F009_RELATIONSHIP_TRACKER_MATRIX.json"
F010=IA/"MV-IA-F010_SOCIAL_INTERACTION_MATRIX.json"
F016=IA/"MV-IA-F016_FACTION_REPUTATION_MATRIX.json"
F016_PROV=IA/"MV-IA-F016_SOURCE_COVERAGE_AND_PROVENANCE.json"
CHECKPOINT=ROOT/"governance/ai/work-state/PPIA-10-attempt-001.json"
POINTER=ROOT/"governance/ai/runtime/CURRENT_WORK_POINTER.json"
STATUS=ROOT/"governance/ai/runtime/CURRENT_IMPLEMENTATION_STATUS.json"
FOUNDATION_MERGE="0c0b8ce17cd80e47b7b12285a2bd8278e58a732e"

def load(p:Path): return json.loads(p.read_text(encoding="utf-8"))
def req(x,msg):
    if not x: raise AssertionError(msg)

def main():
    for p in (MATRIX,CASES,CANDIDATE,TAXONOMY,AUTHORITY,SOURCE,F009,F010,F016,F016_PROV,CHECKPOINT,POINTER,STATUS):
        req(p.exists(),f"missing {p.relative_to(ROOT)}")
    m,c,t,a,s,f9,f10,f16,f16p,cp,pointer,status=map(load,(MATRIX,CASES,TAXONOMY,AUTHORITY,SOURCE,F009,F010,F016,F016_PROV,CHECKPOINT,POINTER,STATUS))
    narrative=CANDIDATE.read_text(encoding="utf-8").lower()

    req(m["work_item"]=="PPIA-10" and m["version"]=="0.1.0","matrix identity/version")
    req(c["work_item"]=="PPIA-10" and c["version"]=="0.1.0","corpus identity/version")
    req(m["foundation_merge"]==c["foundation_merge"]==FOUNDATION_MERGE,"foundation merge drift")

    layers=[x["id"] for x in t["identity_state_layers"]]
    groups=m["projection_groups"]
    req(len(layers)==len(groups)==m["counts"]["layers"]==18,"eighteen-layer contract required")
    req([g["id"] for g in groups]==[f"P10-PG-{i:03d}" for i in range(1,19)],"projection IDs")
    req([g["layer"] for g in groups]==layers,"one-to-one layer mapping")
    expected_profiles=set(t["presentation_profiles"])
    used_profiles={p for g in groups for p in g["profiles"]}
    req(len(expected_profiles)==m["counts"]["profiles"]==14 and used_profiles==expected_profiles,"fourteen profile coverage")
    req(all(g["fields"] and g["profiles"] for g in groups),"empty projection group")
    req(m["projection_policy"]["filter_before_reference_resolution"] is True,"filter before reference resolution")
    req(m["projection_policy"]["filter_before_derivatives"] is True,"filter before derivatives")
    req(m["projection_policy"]["hidden_derivative_leak"] is False,"hidden derivative leak forbidden")
    req(m["projection_policy"]["graph_authoritative"] is False,"graph cannot be authoritative")

    actions=m["actions"]
    req(len(actions)==m["counts"]["actions"]==34,"thirty-four actions required")
    req([x["id"] for x in actions]==[f"P10-ACT-{i:03d}" for i in range(1,35)],"action IDs")
    req(len({x["name"] for x in actions})==34,"unique action names")
    reads=[x for x in actions if x["kind"]=="read"]; writes=[x for x in actions if x["kind"]=="write"]
    req(len(reads)==m["counts"]["reads"]==10 and len(writes)==m["counts"]["writes"]==24,"read/write counts")
    proto=m["mutation_protocols"]["P10-MUT-001"]
    req(proto["required"]==["authorization","expected_version","operation_id"],"mandatory mutation inputs")
    req(proto["ambiguous_result"]==["query_operation_status","query_current_version","retry_only_if_safe"],"ambiguous-result recovery")
    req("one accepted Event group or none" in proto["cross_domain_rule"],"atomic cross-domain rule")
    req(proto["offline_authoritative_mutation"] is False,"offline authoritative mutation forbidden")
    req(all(x.get("protocol")=="P10-MUT-001" for x in writes),"every write must bind P10-MUT-001")
    required_names={"create_relationship_edge","change_relationship_dimension","create_or_update_bond_obligation",
      "propose_social_action","review_social_action","resolve_social_action_atomic","bind_social_status_scope",
      "change_membership_status","define_or_assign_rank_office","change_faction_standing","change_faction_influence",
      "change_faction_relationship_edge","record_secret_claim_rumor_knowledge","commit_role_projection_reveal",
      "compensate_reversible_consequence","accept_generated_social_faction_proposal","request_projection_revocation_purge"}
    req(required_names<={x["name"] for x in actions},"required action surface")

    req(f9["featureId"]=="MV-IA-F009" and len(f9["relationshipDimensions"])==14 and len(f9["revealLayers"])==7 and len(f9["fixtures"])==24,"F009 regression")
    req(f10["featureId"]=="MV-IA-F010" and len(f10["interactionModes"])==3 and len(f10["actionCategories"])==14 and len(f10["outcomeEventDraftTypes"])==29 and len(f10["fixtures"])==24,"F010 regression")
    req(f16["featureId"]=="MV-IA-F016" and len(f16["contractFamilies"])==16 and len(f16["visibilityLayers"])==9 and len(f16["fixtures"])==24,"F016 regression")
    orgs=["Warden Faction","McBride Agency","Blackburn & Briar","Katica Graduate","Karma Ceutrica","Sacred Order","WarDogs"]
    req([x["name"] for x in f16p["convertedOrganizations"]]==orgs,"converted organization provenance")

    req(s["direct_pdf_totals"]=={"files":5,"pages":44},"5-PDF/44-page boundary")
    st=s["direct_structured_totals"]; req(st["files"]==2 and st["rows"]==1374 and st["structural_relevant_rows"]==94,"structured source boundary")
    source_text=json.dumps(s,ensure_ascii=False).lower()
    for phrase in ("kindred","blood","rivalry","romantic","mentor","near-duplicate","universal social difficulty/dc table","eleven named organization/faction/government headings","20 artisan/craftsman/performer"):
        req(phrase in source_text,f"source invariant missing {phrase}")
    req(len(a["domain_handoffs"])==15,"fifteen handoffs")
    auth=json.dumps(a,ensure_ascii=False).lower()
    for phrase in ("relationships are directional","persuasion is not mind control","plausible information path","expected_version and operation_id","semantic nonvisual","ai may validate, summarize or propose only"):
        req(phrase in auth,f"authority invariant missing {phrase}")

    imports=c["fixture_imports"]
    req(len(imports)==3 and c["imported_case_count"]==72 and c["local_case_count"]==18 and c["resolved_case_count"]==90,"corpus counts")
    imported_sources=[f9,f10,f16]
    expected_prefixes=["REL-FX-","SOC-FX-","FRO-FX-"]
    expected_ranges=["PPIA10-RC-001..024","PPIA10-RC-025..048","PPIA10-RC-049..072"]
    for imp,src,prefix,rng in zip(imports,imported_sources,expected_prefixes,expected_ranges):
        fixtures=src[imp["fixture_field"]]
        req(imp["count"]==len(fixtures)==24 and imp["id_prefix"]==prefix and imp["resolved_id_range"]==rng,"import declaration drift")
        req(imp["preserve"]==["fixtureId","scenario","expected"],"imports must preserve fixture triple")
        req([x["fixtureId"] for x in fixtures]==[f"{prefix}{i:03d}" for i in range(1,25)],f"{prefix} fixture IDs")
        req(all(x["scenario"] and x["expected"] for x in fixtures),"inherited fixture content missing")

    local=c["local_cases"]
    req([x["id"] for x in local]==[f"PPIA10-RC-{i:03d}" for i in range(73,91)],"local case IDs")
    action_ids={x["id"] for x in actions}; group_ids={x["id"] for x in groups}
    used_actions={x for case in local for x in case["actions"]}; used_groups={x for case in local for x in case["groups"]}
    req(used_actions==action_ids,f"local action coverage gap {sorted(action_ids-used_actions)}")
    req(used_groups==group_ids,f"local projection coverage gap {sorted(group_ids-used_groups)}")
    req(all(case["title"] and case["basis"] and case["expected"] for case in local),"local case completeness")
    titles={x["title"] for x in local}
    for title in ("Directional relationship source boundary","Five Bond examples remain profile examples",
      "Area/community and interpersonal status stay scoped","Seven converted organizations retain provenance boundaries",
      "Standing requires attributable information path","Influence remains separate from standing",
      "Membership rank office service and permission stay separate","Atomic Social Mode consequences and compensation",
      "Revocation purges two-device protected projections","Semantic nonvisual parity preserves actions" if False else "Lost response recovers before retry with semantic nonvisual parity",
      "AI proposal remains nonauthoritative until acceptance"):
        req(title in titles,f"required case missing {title}")
    req(all(v is False for v in c["policy"].values()),"corpus policy drift")

    for phrase in ("18 projection groups","34 actions","90 deterministic cases","warden faction","mcbride agency","blackburn & briar",
                   "katica graduate","karma ceutrica","sacred order","wardogs","expected_version","operation_id",
                   "permission filtering","atomic event group","semantic nonvisual","ai"):
        req(phrase in narrative,f"candidate narrative missing {phrase}")

    req(cp["work_item_id"]=="PPIA-10" and cp["branch"]=="governance/ppia-10-relationship-social-faction" and cp["status"]=="started","checkpoint identity/status")
    req(cp.get("owner_decision_required") is False and cp.get("unresolved_failures")==[],"checkpoint unresolved state")
    milestone=((cp.get("active_substep") or "")+" "+(cp.get("next_action") or "")).lower()
    req("inspector" in milestone and "reference" in milestone,"checkpoint milestone continuity")
    req(pointer["primary_attempt_id"]=="PPIA-10-attempt-001","pointer selection")
    req(status["primary"]["work_item_id"]=="PPIA-10" and status["primary"]["status"]=="started","compact status selection")

    print("PPIA-10 inspector/action/reference validation passed: 18 layers, 14 profiles, 34 actions, 90 resolved cases.")
    return 0
if __name__=="__main__": raise SystemExit(main())
