#!/usr/bin/env python3
from __future__ import annotations
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
BASE=ROOT/"governance/application-planning/parallel-preimplementation"
CHECKPOINT=ROOT/"governance/ai/work-state/PPIA-13-attempt-001.json"; POINTER=ROOT/"governance/ai/runtime/CURRENT_WORK_POINTER.json"; STATUS=ROOT/"governance/ai/runtime/CURRENT_IMPLEMENTATION_STATUS.json"; BACKLOG=BASE/"PPIA_PROGRAM_BACKLOG.json"
P13_FINAL_HEAD="81e5c75effa1d4f8a8215493ef84b57108e20fae"; P13_FINAL_MERGE="cbfb6b931b11326afd5b826ad2a500e9b6d2d9c9"; P13_FINAL_RUN="31638609641"
MILESTONES=[("6c63e7d601e72d23d4fbede14dd529494a3672fa","d7b2a9b5db79629fe2faf6b12d95f620a4f66d42",51),("4ccb2b0f98743e9cc98d4f0b8de2ded082110ca7","7bab30448acd8a143069d1f5e780a75bd1130283",52),("c125fd9fae540df6d6cdcc7dca307f334da42bf2","0d2d03abd911d7726393d46e9d4b61139d92e0cb",53),("834b2f9fccc3d23bc997df1a6a4d7ccf47fb5f61","c83801da1592f7d837b3b25db3811538ea9ceb64",54)]
COUNTS={"workflows":18,"mutation_workflows":10,"read_analysis_workflows":8,"teaching_surfaces":18,"roles":9,"projection_groups":18,"actions":30,"foundation_cases":30,"academy_cases":20,"iar_cases":40,"integrated_cases":36,"effective_cases":126,"handoffs":13}
ACCEPT_COUNTS={"acceptance_categories":18,"teaching_surfaces":18,"roles":9,"content_types":12,"trigger_classes":12,"foundation_journeys":5,"academy_tracks":5,"academy_modules":53,"curated_academy_modules":24,"effective_teaching_entries":52,"projection_groups":18,"actions":30,"workflows":18,"handoffs":13,"effective_cases":126}
def load(p): return json.loads(p.read_text(encoding="utf-8"))
def j(n): return load(BASE/n)
def req(c,m):
    if not c: raise SystemExit("PPIA-13 COMPLETION CONTRACT: FAIL — "+m)
def main():
    foundation=j("PPIA-13_FOUNDATION_PACKAGE_INDEX_v0.1.0.json"); taxonomy=j("PPIA-13_TEACHING_CONTENT_TAXONOMY_v0.1.0.json"); authority=j("PPIA-13_AUTHORITY_AND_BOUNDARY_MATRIX_v0.1.0.json"); academy=j("PPIA-13_GM_ACADEMY_CURRICULUM_AND_MULTIVERSAL_MAP_v0.1.0.json"); library=j("PPIA-13_TEACHING_LIBRARY_PACKAGE_INDEX_v0.1.0.json"); projection=j("PPIA-13_TEACHING_LIBRARY_PROJECTION_CONTRACT_v0.1.0.json"); actions=j("PPIA-13_TEACHING_LIBRARY_ACTION_CONTRACT_MATRIX_v0.1.0.json"); corpus=j("PPIA-13_TEACHING_LIBRARY_CONTENT_CORPUS_v0.1.0.json"); integrated=j("PPIA-13_INTEGRATED_TEACHING_PACKAGE_INDEX_v0.1.0.json"); workflows=j("PPIA-13_INTEGRATED_TEACHING_WORKFLOW_CONTRACT_MATRIX_v0.1.0.json"); trace=j("PPIA-13_INTEGRATED_TEACHING_TRACEABILITY_MATRIX_v0.1.0.json"); acceptance=j("PPIA-13_COMPLETION_ACCEPTANCE_MATRIX_v0.1.0.json"); scope=j("PPIA-13_COMPLETION_SCOPE_LOCK_v0.1.0.json"); package=j("PPIA-13_COMPLETION_PACKAGE_INDEX_v0.1.0.json"); checkpoint=load(CHECKPOINT); pointer=load(POINTER); status=load(STATUS); backlog=load(BACKLOG); report=(BASE/"PPIA-13_COMPLETION_REPORT.md").read_text(encoding="utf-8").lower()
    verified=package.get("verified_milestones",[]); req(len(verified)==4,"four verified milestone records required")
    for rec,exp in zip(verified,MILESTONES): req((rec.get("validated_head"),rec.get("merge"),rec.get("hosted_workflows"))==exp,f"milestone evidence changed {rec.get('milestone')}")
    req(package.get("milestone")=="final_completion_gate" and package.get("state")=="completion_candidate_only_until_exact_head_all_green_and_merge","completion package state changed")
    req(package.get("transition_after_completion")=="PPIA-13 -> PPIA-14 separate governed operation","successor transition boundary changed")
    req(foundation.get("counts")=={"evidence_classes":6,"teaching_content_types":12,"trigger_classes":12,"teaching_surfaces":18,"roles":9,"foundation_journeys":5,"reference_cases":30},"Foundation counts changed")
    req("P13-GAP-001" in foundation.get("source_gap",""),"P13-GAP-001 lost")
    req(len(taxonomy.get("teaching_surfaces",[]))==18 and len(taxonomy.get("audience_roles",[]))==9 and len(taxonomy.get("content_types",[]))==12 and len(taxonomy.get("trigger_classes",[]))==12,"Foundation taxonomy counts changed")
    auth=json.dumps(authority).lower()
    for p in ("permission filtering occurs before help search","hidden object","offline state never implies authoritative mutation","tutorial-campaign content is synthetic/noncanonical","unresolved f024","no application runtime"): req(p in auth,f"authority invariant missing {p!r}")
    req(academy.get("locked_counts")=={"tracks":5,"total_modules":53,"developed_source_modules":35,"outline_only_multiversal_modules":18,"initial_curated_source_backed_modules":24},"Academy counts changed")
    req("never a permission/capability gate" in academy["delivery_model"]["course_progress"],"Academy gating changed"); req(academy["world_creation_tables_policy"]["canonical_promotion"] is False,"World Creation promotion changed")
    req(library.get("counts")=={"projection_groups":18,"actions":30,"new_reference_cases":40,"effective_reference_cases":90,"effective_teaching_entries":52},"Teaching Library counts changed")
    req(projection["counts"]["projection_groups"]==18 and actions["counts"]=={"projection_groups":18,"actions":30,"reads":12,"analysis_proposals":10,"writes":8},"projection/action counts changed")
    req([x["id"] for x in actions["actions"]]==[f"P13-ACT-{i:03d}" for i in range(1,31)],"action IDs changed")
    req(all(x.get("protocol")=="P13-MUT-001" for x in actions["actions"] if x.get("kind")=="write"),"write protocol changed")
    for k in ("gameplay_mutation","permission_mutation","campaign_truth_mutation","character_truth_mutation","pack_lifecycle_mutation","canonical_content_promotion","tutorial_fixture_promotion","academy_completion_capability_gate","offline_authoritative_mutation","ai_irreversible_authority"): req(actions["action_policy"][k] is False,f"action boundary enabled {k}")
    for v in ("authenticated_actor","authorization_context","expected_version","operation_id","requested_change"): req(v in actions["mutation_protocol"]["required_inputs"],f"P13-MUT-001 missing {v}")
    req(corpus["counts"]["core_teaching_objects"]==28 and corpus["counts"]["academy_module_bindings"]==24 and corpus["counts"]["effective_teaching_entries"]==52,"corpus counts changed")
    req(integrated["counts"]==COUNTS and workflows["counts"]==COUNTS and trace["counts"]==COUNTS,"integrated counts changed")
    req([x["id"] for x in workflows["workflows"]]==[f"P13-WF-{i:03d}" for i in range(1,19)],"workflow IDs changed")
    pol=workflows["workflow_policy"]
    for k in ("permission_filter_before_discovery_search_counts_ranking_autocomplete_examples_tutorial_diagnostics_export_ai","teaching_write_requires_P13_MUT_001","expected_version_required_for_write","operation_id_required_for_write","ambiguous_result_status_lookup_before_retry","academy_optional_non_gating","multiversal_specific_claim_requires_canonical_grounding","mobile_keyboard_touch_screen_reader_high_zoom_reduced_motion_noncolor_parity","zero_ai_parity"): req(pol[k] is True,f"workflow policy disabled {k}")
    for k in ("hidden_derivative_leak","outline_gap_fabrication","tutorial_campaign_canonical","world_creation_output_canonical","pack_lifecycle_invention","p14_final_microcopy_claim","offline_authoritative_mutation","gameplay_mutation","permission_mutation","runtime_activation"): req(pol[k] is False,f"workflow prohibition weakened {k}")
    req(acceptance["counts"]==ACCEPT_COUNTS,"acceptance counts changed")
    req([x["id"] for x in acceptance["categories"]]==[f"P13-CG-{i:02d}" for i in range(1,19)],"acceptance category IDs changed")
    req(scope.get("scope_locked") is True and "transition_to_PPIA_14_before_verified_completion" in scope.get("prohibited_shortcuts",[]),"scope lock changed")
    for p in ("complete role-aware onboarding/help/teaching content library","52 effective teaching entries","18 integrated workflows","13 explicit authority","126 effective deterministic cases","p13-mut-001","p13-gap-001","f024 pack lifecycle","ppia-14 retains final","tutorial-campaign content and world creation exercises are synthetic/noncanonical","academy progress is advisory learning only","zero-ai parity","no application runtime","ppia-13 → ppia-14 transition"): req(p in report,f"completion report missing {p!r}")
    t={x["work_item_id"]:x for x in backlog["tranches"]}; req(t["PPIA-08"]["status"]=="completed_verified","PPIA-08 dependency changed")
    current=backlog["current_work_item_id"]
    if current=="PPIA-13":
        req(t["PPIA-13"]["status"]=="started" and t["PPIA-14"]["status"]=="planned","completion review state invalid")
        req(checkpoint["status"] in {"started","ready_for_review"},"PPIA-13 checkpoint must be active during completion review")
        selected=[x for x in pointer["active_attempts"] if x.get("owner_selected")]; req(len(selected)==1 and selected[0]["work_item_id"]=="PPIA-13" and status["primary"]["work_item_id"]=="PPIA-13","runtime continuity must select current PPIA-13")
        mode="current"
    else:
        req(t["PPIA-13"]["status"]=="completed_verified" and checkpoint["status"]=="completed_verified" and checkpoint["active_substep"] is None,"historical PPIA-13 must be completed_verified")
        req(checkpoint["latest_pushed_commit"]==P13_FINAL_HEAD and checkpoint["merge_commit"]==P13_FINAL_MERGE and checkpoint["pull_request"]==279,"historical PPIA-13 completion evidence changed")
        req(any(P13_FINAL_RUN in x.get("command","") and x.get("status")=="passed" for x in checkpoint.get("validation",[])),"historical completion run missing")
        mode="historical"
    req(checkpoint["owner_decision_required"] is False and checkpoint["unresolved_failures"]==[],"PPIA-13 unresolved state")
    for k in ("application_runtime_mutation_authorized","a2_activation_authorized","release_authorized","deployment_authorized","tester_access_authorized","canonical_promotion_without_source_evidence_authorized"): req(backlog["boundaries"][k] is False,f"completion gate may not enable {k}")
    print("PPIA-13 COMPLETION CONTRACT: PASS"); print("surface=18 / roles=9 / library=52 / actions=30 / workflows=18 / handoffs=13 / cases=126"); print("continuity_mode="+mode+" runtime_activation=false")
if __name__=="__main__": main()
