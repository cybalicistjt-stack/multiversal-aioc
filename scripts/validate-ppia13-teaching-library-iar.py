#!/usr/bin/env python3
from __future__ import annotations
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / "governance/application-planning/parallel-preimplementation"
P = lambda name: BASE / name
CHECKPOINT = ROOT / "governance/ai/work-state/PPIA-13-attempt-001.json"
POINTER = ROOT / "governance/ai/runtime/CURRENT_WORK_POINTER.json"
STATUS = ROOT / "governance/ai/runtime/CURRENT_IMPLEMENTATION_STATUS.json"
BACKLOG = BASE / "PPIA_PROGRAM_BACKLOG.json"
P13_FINAL_HEAD = "81e5c75effa1d4f8a8215493ef84b57108e20fae"
P13_FINAL_MERGE = "cbfb6b931b11326afd5b826ad2a500e9b6d2d9c9"

FILES = {
    "projection": P("PPIA-13_TEACHING_LIBRARY_PROJECTION_CONTRACT_v0.1.0.json"),
    "actions": P("PPIA-13_TEACHING_LIBRARY_ACTION_CONTRACT_MATRIX_v0.1.0.json"),
    "corpus": P("PPIA-13_TEACHING_LIBRARY_CONTENT_CORPUS_v0.1.0.json"),
    "cases": P("PPIA-13_TEACHING_LIBRARY_REFERENCE_CASES_v0.1.0.json"),
    "index": P("PPIA-13_TEACHING_LIBRARY_PACKAGE_INDEX_v0.1.0.json"),
    "candidate": P("PPIA-13_TEACHING_LIBRARY_INSPECTOR_ACTION_REFERENCE_CANDIDATE.md"),
    "foundation_taxonomy": P("PPIA-13_TEACHING_CONTENT_TAXONOMY_v0.1.0.json"),
    "foundation_authority": P("PPIA-13_AUTHORITY_AND_BOUNDARY_MATRIX_v0.1.0.json"),
    "academy": P("PPIA-13_GM_ACADEMY_CURRICULUM_AND_MULTIVERSAL_MAP_v0.1.0.json"),
    "academy_cases": P("PPIA-13_GM_ACADEMY_REFERENCE_CASES_v0.1.0.json"),
    "foundation_cases": P("PPIA-13_FOUNDATION_REFERENCE_CASES_v0.1.0.json"),
}

def fail(msg: str) -> None: raise SystemExit(f"PPIA-13 TEACHING LIBRARY IAR: FAIL — {msg}")
def require(cond: bool, msg: str) -> None:
    if not cond: fail(msg)
def load(path: Path) -> dict:
    require(path.exists(), f"missing {path.relative_to(ROOT)}")
    return json.loads(path.read_text(encoding="utf-8"))

def main() -> None:
    projection=load(FILES["projection"]); actions=load(FILES["actions"]); corpus=load(FILES["corpus"]); cases=load(FILES["cases"]); index=load(FILES["index"]); taxonomy=load(FILES["foundation_taxonomy"]); authority=load(FILES["foundation_authority"]); academy=load(FILES["academy"]); foundation_cases=load(FILES["foundation_cases"]); academy_cases=load(FILES["academy_cases"]); checkpoint=load(CHECKPOINT); pointer=load(POINTER); status=load(STATUS); backlog=load(BACKLOG); candidate=FILES["candidate"].read_text(encoding="utf-8")
    require(len(taxonomy["teaching_surfaces"])==18,"Foundation teaching surface count changed")
    require(len(taxonomy["audience_roles"])==9,"Foundation role count changed")
    require(len(taxonomy["content_types"])==12,"Foundation content-type count changed")
    require(academy["locked_counts"]["total_modules"]==53,"Academy module count changed")
    require(academy["locked_counts"]["initial_curated_source_backed_modules"]==24,"Academy curated count changed")
    require(projection["counts"]["projection_groups"]==18 and len(projection["projection_groups"])==18,"projection group count mismatch")
    pg_ids=[x["id"] for x in projection["projection_groups"]]
    require(pg_ids==[f"P13-PG-{i:03d}" for i in range(1,19)],"projection IDs must be stable/sequential")
    policy=projection["projection_policy"]
    for key in ("permission_filter_before_discovery","permission_filter_before_search_counts_ranking_autocomplete","permission_filter_before_examples_screenshots_tutorial_branches","permission_filter_before_diagnostics_exports_notifications_ai_context","unknown_and_unresolved_gap_first_class","return_context_preserved","nonvisual_semantic_parity_required"): require(policy[key] is True,f"projection policy {key} must remain true")
    for key in ("hidden_state_inference_allowed","academy_completion_capability_gate","outline_only_multiversal_topic_user_factual_lesson_allowed_without_grounding","world_creation_table_output_canonical","tutorial_campaign_canonical","generated_teaching_authoritative_game_truth"): require(policy[key] is False,f"projection policy {key} must remain false")
    require(actions["counts"]=={"projection_groups":18,"actions":30,"reads":12,"analysis_proposals":10,"writes":8},"action counts changed")
    require([x["id"] for x in actions["actions"]]==[f"P13-ACT-{i:03d}" for i in range(1,31)],"action IDs unstable")
    kinds=[x["kind"] for x in actions["actions"]]
    require(kinds.count("read")==12 and kinds.count("analysis_proposal")==10 and kinds.count("write")==8,"action kind counts mismatch")
    for action in actions["actions"]:
        require(set(action["groups"]).issubset(set(pg_ids)),f"{action['id']} references unknown projection group")
        if action["kind"]=="write": require(action.get("protocol")=="P13-MUT-001" and action["authority"]=="explicit_human_authorization",f"{action['id']} write boundary changed")
    ap=actions["action_policy"]
    for key in ("gameplay_mutation","permission_mutation","campaign_truth_mutation","character_truth_mutation","pack_lifecycle_mutation","canonical_content_promotion","tutorial_fixture_promotion","academy_completion_capability_gate","offline_authoritative_mutation","ai_irreversible_authority"): require(ap[key] is False,f"action policy may not enable {key}")
    mut=actions["mutation_protocol"]
    for reqv in ("authenticated_actor","authorization_context","expected_version","operation_id","requested_change"): require(reqv in mut["required_inputs"],f"P13-MUT-001 missing {reqv}")
    mut_text=json.dumps(mut).lower()
    for phrase in ("stale","deduplicate","status lookup","durable","offline"): require(phrase in mut_text,f"P13-MUT-001 missing {phrase!r} recovery semantics")
    require(corpus["counts"]["core_teaching_objects"]==28 and corpus["counts"]["academy_module_bindings"]==24 and corpus["counts"]["effective_teaching_entries"]==52,"teaching corpus counts changed")
    require(corpus["counts"]["multiversal_grounding_records"]==10 and len(corpus["multiversal_grounding_records"])==10,"Multiversal grounding count mismatch")
    core=corpus["core_teaching_objects"]; bindings=corpus["academy_module_bindings"]
    ids=[x["teachingContentId"] for x in core]+[x["teachingContentId"] for x in bindings]
    require(ids==[f"P13-TL-{i:03d}" for i in range(1,53)],"teaching content IDs unstable")
    required_fields=set(taxonomy["required_object_fields"])
    for obj in core:
        require(required_fields.issubset(obj),f"{obj['teachingContentId']} missing Foundation-required fields")
        require(set(obj["audienceRoles"]).issubset(set(taxonomy["audience_roles"])),f"{obj['teachingContentId']} unknown role")
        require(set(obj["surfaceIds"]).issubset({x["id"] for x in taxonomy["teaching_surfaces"]}),f"{obj['teachingContentId']} unknown surface")
        require(set(obj["triggerClassIds"]).issubset({x["id"] for x in taxonomy["trigger_classes"]}),f"{obj['teachingContentId']} unknown trigger")
        require("service-actor" not in obj["audienceRoles"] and "ai" not in obj["audienceRoles"],f"{obj['teachingContentId']} targets nonhuman role")
    covered={sid for obj in core for sid in obj["surfaceIds"]}|{sid for b in bindings for sid in b["surfaceIds"]}
    require(covered=={x["id"] for x in taxonomy["teaching_surfaces"]},"representative corpus must cover all 18 Foundation surfaces")
    require(all(b["sourceStatus"]=="developed" and b["curationStatus"]=="initial_curated" for b in bindings),"Academy bindings must remain developed/source-backed")
    for rec in corpus["multiversal_grounding_records"]:
        if rec["status"]=="grounding_pending": require(rec["userFacingFactStatus"]=="no_factual_lesson_yet",f"pending grounding topic {rec['topic']} may not render factual lesson")
    pending={x["topic"] for x in corpus["multiversal_grounding_records"] if x["status"]=="grounding_pending"}
    for topic in ("Handling Inter-Reality Travel & Causal Complexity","Mastering Faction Play in Multiversal","Advanced Multiversal Economics & Politics","Running Multiversal Warfare and Strategic Play"): require(topic in pending,f"{topic} must remain explicit gap")
    require(cases["counts"]=={"new_cases":40,"inherited_foundation_cases":30,"inherited_gm_academy_cases":20,"effective_cases":90},"IAR case counts changed")
    require(len(cases["cases"])==40 and len(foundation_cases["cases"])==30 and len(academy_cases["cases"])==20,"actual case counts changed")
    require([x["id"] for x in cases["cases"]]==[f"P13-IAR-{i:03d}" for i in range(1,41)],"IAR case IDs unstable")
    require(all(x["permissionFilterRequired"] and x["nonvisualRequired"] for x in cases["cases"]),"every IAR case must require permission filter/nonvisual parity")
    require(index["counts"]=={"projection_groups":18,"actions":30,"new_reference_cases":40,"effective_reference_cases":90,"effective_teaching_entries":52},"package index counts mismatch")
    low=candidate.lower()
    for phrase in ("52 effective semantic teaching entries","90 effective deterministic cases","ppia-13 integrated teaching workflows / traceability","no application runtime","f024","ppia-14","expected_version","operation_id","accepted durable event"): require(phrase in low,f"candidate narrative missing {phrase!r}")
    auth_text=json.dumps(authority).lower()
    for phrase in ("permission filtering occurs before help search","hidden object","offline state never implies authoritative mutation","tutorial-campaign content is synthetic/noncanonical","unresolved f024","no application runtime"): require(phrase in auth_text,f"Foundation authority invariant missing {phrase!r}")
    require(checkpoint["work_item_id"]=="PPIA-13" and checkpoint["owner_decision_required"] is False and checkpoint["unresolved_failures"]==[],"PPIA-13 checkpoint identity/unresolved state changed")
    if backlog["current_work_item_id"]=="PPIA-13":
        require(checkpoint["status"] in {"started","ready_for_review"},"current PPIA-13 must remain active")
        selected=[x for x in pointer["active_attempts"] if x.get("owner_selected")]
        require(len(selected)==1 and selected[0]["work_item_id"]=="PPIA-13" and status["primary"]["work_item_id"]=="PPIA-13","runtime continuity must select current PPIA-13")
        mode="current"
    else:
        require(checkpoint["status"]=="completed_verified" and checkpoint["active_substep"] is None,"historical PPIA-13 must be completed_verified")
        require(checkpoint["latest_pushed_commit"]==P13_FINAL_HEAD and checkpoint["merge_commit"]==P13_FINAL_MERGE and checkpoint["pull_request"]==279,"historical PPIA-13 completion evidence changed")
        mode="historical"
    all_text=(json.dumps(projection)+json.dumps(actions)+json.dumps(corpus)+json.dumps(cases)+candidate).lower()
    for prohibited in ("runtime_activation=true","a2_activation_authorized=true","release_authorized=true","deployment_authorized=true","tester_access_authorized=true","canonical_promotion_without_source_evidence_authorized=true"): require(prohibited not in all_text,f"prohibited authorization {prohibited!r}")
    print("PPIA-13 TEACHING LIBRARY IAR: PASS")
    print("surface=18 projection_groups / 30 actions / 52 effective teaching entries")
    print("actions=12 reads / 10 analysis-proposals / 8 P13-MUT-001 writes")
    print("cases=40 new + 30 Foundation + 20 GM Academy = 90 effective")
    print("continuity_mode="+mode+" runtime_activation=false")

if __name__=="__main__": main()
