#!/usr/bin/env python3
from __future__ import annotations
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / "governance/application-planning/parallel-preimplementation"
CHECKPOINT = ROOT / "governance/ai/work-state/PPIA-13-attempt-001.json"
POINTER = ROOT / "governance/ai/runtime/CURRENT_WORK_POINTER.json"
STATUS = ROOT / "governance/ai/runtime/CURRENT_IMPLEMENTATION_STATUS.json"
BACKLOG = BASE / "PPIA_PROGRAM_BACKLOG.json"

MILESTONES = [
    ("6c63e7d601e72d23d4fbede14dd529494a3672fa", "d7b2a9b5db79629fe2faf6b12d95f620a4f66d42", 51),
    ("4ccb2b0f98743e9cc98d4f0b8de2ded082110ca7", "7bab30448acd8a143069d1f5e780a75bd1130283", 52),
    ("c125fd9fae540df6d6cdcc7dca307f334da42bf2", "0d2d03abd911d7726393d46e9d4b61139d92e0cb", 53),
    ("834b2f9fccc3d23bc997df1a6a4d7ccf47fb5f61", "c83801da1592f7d837b3b25db3811538ea9ceb64", 54),
]
COUNTS = {"workflows":18,"mutation_workflows":10,"read_analysis_workflows":8,"teaching_surfaces":18,"roles":9,"projection_groups":18,"actions":30,"foundation_cases":30,"academy_cases":20,"iar_cases":40,"integrated_cases":36,"effective_cases":126,"handoffs":13}

def fail(msg):
    raise SystemExit(f"PPIA-13 COMPLETION CONTRACT: FAIL — {msg}")
def require(cond, msg):
    if not cond: fail(msg)
def load(path):
    require(path.exists(), f"missing {path.relative_to(ROOT)}")
    return json.loads(path.read_text(encoding="utf-8"))
def j(name): return load(BASE / name)

def main():
    foundation_index=j("PPIA-13_FOUNDATION_PACKAGE_INDEX_v0.1.0.json")
    taxonomy=j("PPIA-13_TEACHING_CONTENT_TAXONOMY_v0.1.0.json")
    authority=j("PPIA-13_AUTHORITY_AND_BOUNDARY_MATRIX_v0.1.0.json")
    foundation_cases=j("PPIA-13_FOUNDATION_REFERENCE_CASES_v0.1.0.json")
    academy=j("PPIA-13_GM_ACADEMY_CURRICULUM_AND_MULTIVERSAL_MAP_v0.1.0.json")
    academy_cases=j("PPIA-13_GM_ACADEMY_REFERENCE_CASES_v0.1.0.json")
    library_index=j("PPIA-13_TEACHING_LIBRARY_PACKAGE_INDEX_v0.1.0.json")
    projection=j("PPIA-13_TEACHING_LIBRARY_PROJECTION_CONTRACT_v0.1.0.json")
    actions=j("PPIA-13_TEACHING_LIBRARY_ACTION_CONTRACT_MATRIX_v0.1.0.json")
    corpus=j("PPIA-13_TEACHING_LIBRARY_CONTENT_CORPUS_v0.1.0.json")
    iar_cases=j("PPIA-13_TEACHING_LIBRARY_REFERENCE_CASES_v0.1.0.json")
    integrated_index=j("PPIA-13_INTEGRATED_TEACHING_PACKAGE_INDEX_v0.1.0.json")
    workflows=j("PPIA-13_INTEGRATED_TEACHING_WORKFLOW_CONTRACT_MATRIX_v0.1.0.json")
    trace=j("PPIA-13_INTEGRATED_TEACHING_TRACEABILITY_MATRIX_v0.1.0.json")
    integrated_cases=j("PPIA-13_INTEGRATED_TEACHING_REFERENCE_CASES_v0.1.0.json")
    acceptance=j("PPIA-13_COMPLETION_ACCEPTANCE_MATRIX_v0.1.0.json")
    scope=j("PPIA-13_COMPLETION_SCOPE_LOCK_v0.1.0.json")
    package=j("PPIA-13_COMPLETION_PACKAGE_INDEX_v0.1.0.json")
    checkpoint=load(CHECKPOINT); pointer=load(POINTER); status=load(STATUS); backlog=load(BACKLOG)
    report_path=BASE/"PPIA-13_COMPLETION_REPORT.md"; readme_path=BASE/"PPIA-13_COMPLETION_README.md"
    require(report_path.exists() and readme_path.exists(), "completion narrative/readme missing")
    report=report_path.read_text(encoding="utf-8").lower()

    verified=package.get("verified_milestones",[])
    require(len(verified)==4, "four verified milestone records required")
    for rec, expected in zip(verified, MILESTONES):
        require((rec.get("validated_head"),rec.get("merge"),rec.get("hosted_workflows"))==expected, f"milestone evidence changed for {rec.get('milestone')}")
    require(package.get("milestone")=="final_completion_gate", "completion package milestone changed")
    require(package.get("state")=="completion_candidate_only_until_exact_head_all_green_and_merge", "completion package may not self-complete")
    require(package.get("transition_after_completion")=="PPIA-13 -> PPIA-14 separate governed operation", "PPIA-14 transition must remain separate")

    require(foundation_index.get("counts")=={"evidence_classes":6,"teaching_content_types":12,"trigger_classes":12,"teaching_surfaces":18,"roles":9,"foundation_journeys":5,"reference_cases":30}, "Foundation counts changed")
    require(foundation_index.get("primary_authority")=="MV-IA-F025", "MV-IA-F025 primary authority changed")
    require("P13-GAP-001" in foundation_index.get("source_gap",""), "P13-GAP-001 must remain explicit")
    require(foundation_index.get("completion_claim") is False and foundation_index.get("runtime_activation") is False, "Foundation may not claim completion/runtime activation")
    require([x.get("id") for x in taxonomy.get("content_types",[])]==[f"P13-TC-{i:03d}" for i in range(1,13)], "12 teaching-content type IDs changed")
    require([x.get("id") for x in taxonomy.get("trigger_classes",[])]==[f"P13-TR-{i:03d}" for i in range(1,13)], "12 trigger IDs changed")
    surface_ids=[x.get("id") for x in taxonomy.get("teaching_surfaces",[])]
    require(surface_ids==[f"P13-SF-{i:03d}" for i in range(1,19)], "18 teaching surface IDs changed")
    roles=taxonomy.get("audience_roles",[])
    require(len(roles)==9 and set(taxonomy.get("primary_human_teaching_roles",[]))=={"player","game-master","content-creator"}, "role surface changed")
    require(len(foundation_cases.get("cases",[]))==30, "30 Foundation cases required")
    auth_text=json.dumps(authority,ensure_ascii=False).lower()
    for phrase in ("permission filtering occurs before help search","hidden object","offline state never implies authoritative mutation","tutorial-campaign content is synthetic/noncanonical","unresolved f024","no application runtime"):
        require(phrase in auth_text, f"Foundation authority invariant missing {phrase!r}")

    require(academy.get("locked_counts")=={"tracks":5,"total_modules":53,"developed_source_modules":35,"outline_only_multiversal_modules":18,"initial_curated_source_backed_modules":24}, "GM Academy locked counts changed")
    require(len(academy.get("tracks",[]))==5, "five GM Academy tracks required")
    delivery=academy.get("delivery_model",{})
    require("optional progressive learning track" in delivery.get("academy_track","").lower(), "Academy optionality changed")
    require("never a permission/capability gate" in delivery.get("course_progress","").lower(), "Academy gating boundary changed")
    require(academy.get("multiversal_outline_policy",{}).get("status")=="approved_outline_scaffold_not_developed_lesson_source", "Multiversal outline-only status changed")
    require(academy.get("world_creation_tables_policy",{}).get("canonical_promotion") is False, "World Creation exercises may not auto-promote")
    require(len(academy_cases.get("cases",[]))==20, "20 GM Academy cases required")

    require(library_index.get("counts")=={"projection_groups":18,"actions":30,"new_reference_cases":40,"effective_reference_cases":90,"effective_teaching_entries":52}, "Teaching Library package counts changed")
    require(projection.get("counts",{}).get("projection_groups")==18 and len(projection.get("projection_groups",[]))==18, "18 projection groups required")
    require(actions.get("counts")=={"projection_groups":18,"actions":30,"reads":12,"analysis_proposals":10,"writes":8}, "30 action split changed")
    action_rows=actions.get("actions",[])
    require([x.get("id") for x in action_rows]==[f"P13-ACT-{i:03d}" for i in range(1,31)], "30 action IDs changed")
    require(all(x.get("protocol")=="P13-MUT-001" for x in action_rows if x.get("kind")=="write"), "all teaching writes must use P13-MUT-001")
    for key in ("gameplay_mutation","permission_mutation","campaign_truth_mutation","character_truth_mutation","pack_lifecycle_mutation","canonical_content_promotion","tutorial_fixture_promotion","academy_completion_capability_gate","offline_authoritative_mutation","ai_irreversible_authority"):
        require(actions.get("action_policy",{}).get(key) is False, f"action boundary enabled: {key}")
    mut=actions.get("mutation_protocol",{})
    for item in ("authenticated_actor","authorization_context","expected_version","operation_id","requested_change"):
        require(item in mut.get("required_inputs",[]), f"P13-MUT-001 missing {item}")
    mut_text=json.dumps(mut).lower()
    for phrase in ("reject stale write","deduplicate operation_id","immutable operation receipt","status lookup","offline"):
        require(phrase in mut_text, f"P13-MUT-001 recovery missing {phrase!r}")
    require(corpus.get("counts",{}).get("core_teaching_objects")==28, "28 core teaching objects required")
    require(corpus.get("counts",{}).get("academy_module_bindings")==24, "24 Academy bindings required")
    require(corpus.get("counts",{}).get("effective_teaching_entries")==52, "52 effective teaching entries required")
    pending={x.get("topic") for x in corpus.get("multiversal_grounding_records",[]) if x.get("status")=="grounding_pending"}
    for topic in ("Handling Inter-Reality Travel & Causal Complexity","Mastering Faction Play in Multiversal","Advanced Multiversal Economics & Politics","Running Multiversal Warfare and Strategic Play"):
        require(topic in pending, f"explicit Multiversal grounding gap lost: {topic}")
    require(len(iar_cases.get("cases",[]))==40, "40 IAR cases required")

    require(integrated_index.get("counts")==COUNTS, "Integrated package counts changed")
    require(integrated_index.get("completion_claim") is False and integrated_index.get("runtime_activation") is False, "Integrated milestone may not self-complete/activate runtime")
    require(integrated_index.get("next_milestone_after_merge")=="PPIA-13 Final Completion Gate", "Integrated predecessor next milestone changed")
    require(workflows.get("counts")==COUNTS and trace.get("counts")==COUNTS, "Integrated workflow/trace counts changed")
    wf_rows=workflows.get("workflows",[])
    require([x.get("id") for x in wf_rows]==[f"P13-WF-{i:03d}" for i in range(1,19)], "18 workflow IDs changed")
    require(sum(x.get("mutation") is True for x in wf_rows)==10 and sum(x.get("mutation") is False for x in wf_rows)==8, "10/8 workflow split changed")
    policy=workflows.get("workflow_policy",{})
    for key in ("permission_filter_before_discovery_search_counts_ranking_autocomplete_examples_tutorial_diagnostics_export_ai","teaching_write_requires_P13_MUT_001","expected_version_required_for_write","operation_id_required_for_write","ambiguous_result_status_lookup_before_retry","academy_optional_non_gating","multiversal_specific_claim_requires_canonical_grounding","mobile_keyboard_touch_screen_reader_high_zoom_reduced_motion_noncolor_parity","zero_ai_parity"):
        require(policy.get(key) is True, f"workflow policy disabled: {key}")
    for key in ("hidden_derivative_leak","outline_gap_fabrication","tutorial_campaign_canonical","world_creation_output_canonical","pack_lifecycle_invention","p14_final_microcopy_claim","offline_authoritative_mutation","gameplay_mutation","permission_mutation","runtime_activation"):
        require(policy.get(key) is False, f"workflow prohibition weakened: {key}")
    require([x.get("id") for x in workflows.get("handoffs",[])]==[f"P13-HO-{i:03d}" for i in range(1,14)], "13 handoff IDs changed")
    require(trace.get("coverage")=={"workflows":"18/18","teaching_surfaces":"18/18","roles":"9/9","projection_groups":"18/18 derived from action groups","actions":"30/30","handoffs":"13/13","foundation_cases":"30/30 exactly once","academy_cases":"20/20 exactly once","iar_cases":"40/40 exactly once","integrated_cases":"36/36 exactly once","effective_cases":"126"}, "Integrated trace coverage changed")
    require(len(integrated_cases.get("cases",[]))==36, "36 integrated cases required")

    assigned_f=[c for w in wf_rows for c in w.get("foundation_case_ids",[])]
    assigned_a=[c for w in wf_rows for c in w.get("academy_case_ids",[])]
    assigned_i=[c for w in wf_rows for c in w.get("iar_case_ids",[])]
    assigned_w=[c for w in wf_rows for c in w.get("integrated_case_ids",[])]
    require(len(assigned_f)==len(set(assigned_f))==30 and set(assigned_f)=={f"PPIA13-FC-{i:03d}" for i in range(1,31)}, "Foundation cases not exactly once")
    require(len(assigned_a)==len(set(assigned_a))==20 and set(assigned_a)=={f"P13-GMA-RC-{i:03d}" for i in range(1,21)}, "Academy cases not exactly once")
    require(len(assigned_i)==len(set(assigned_i))==40 and set(assigned_i)=={f"P13-IAR-{i:03d}" for i in range(1,41)}, "IAR cases not exactly once")
    require(len(assigned_w)==len(set(assigned_w))==36 and set(assigned_w)=={f"P13-IW-{i:03d}" for i in range(1,37)}, "Integrated cases not exactly once")
    wf_surface={sid for w in wf_rows for sid in w.get("surface_ids",[])}; wf_roles={r for w in wf_rows for r in w.get("roles",[])}
    wf_actions={a for w in wf_rows for a in w.get("actions",[])}; wf_handoffs={h for w in wf_rows for h in w.get("handoffs",[])}
    action_map={x["id"]:x for x in action_rows}; wf_projection={pg for aid in wf_actions for pg in action_map[aid].get("groups",[])}
    require(wf_surface==set(surface_ids), "not all 18 teaching surfaces exercised")
    require(wf_roles==set(roles), "not all nine governed roles exercised")
    require(wf_actions=={f"P13-ACT-{i:03d}" for i in range(1,31)}, "not all 30 actions exercised")
    require(wf_handoffs=={f"P13-HO-{i:03d}" for i in range(1,14)}, "not all 13 handoffs exercised")
    require(wf_projection=={f"P13-PG-{i:03d}" for i in range(1,19)}, "not all 18 projection groups exercised")
    for w in wf_rows:
        if w.get("mutation") is True: require(w.get("protocol")=="P13-MUT-001", f"{w['id']} mutation workflow missing P13-MUT-001")

    expected_accept_counts={"acceptance_categories":18,"teaching_surfaces":18,"roles":9,"content_types":12,"trigger_classes":12,"foundation_journeys":5,"academy_tracks":5,"academy_modules":53,"curated_academy_modules":24,"effective_teaching_entries":52,"projection_groups":18,"actions":30,"workflows":18,"handoffs":13,"effective_cases":126}
    require(acceptance.get("counts")==expected_accept_counts, "completion acceptance counts changed")
    require([x.get("id") for x in acceptance.get("categories",[])]==[f"P13-CG-{i:02d}" for i in range(1,19)], "18 completion acceptance categories changed")
    require(acceptance.get("result")=="completion_candidate_only_until_exact_head_validation_and_merge", "completion acceptance may not self-complete")
    require(scope.get("scope_locked") is True and scope.get("completion_requires")=="exact_head_all_green_hosted_validation_and_merge", "completion scope lock weakened")
    for item in ("P13_GAP_001_F024_pack_gap","PPIA_14_final_microcopy_handoff","zero_ai_parity","no_runtime_activation"):
        require(item in scope.get("required_categories",[]), f"scope lock missing {item}")
    require("transition_to_PPIA_14_before_verified_completion" in scope.get("prohibited_shortcuts",[]), "premature PPIA-14 transition prohibition missing")
    for phrase in ("complete role-aware onboarding/help/teaching content library","52 effective teaching entries","18 integrated workflows","13 explicit authority","126 effective deterministic cases","p13-mut-001","p13-gap-001","f024 pack lifecycle","ppia-14 retains final","tutorial-campaign content and world creation exercises are synthetic/noncanonical","academy progress is advisory learning only","zero-ai parity","no application runtime","completion candidate","ppia-13 → ppia-14 transition"):
        require(phrase in report, f"completion report missing {phrase!r}")

    tranches={x["work_item_id"]:x for x in backlog.get("tranches",[])}
    require(backlog.get("current_work_item_id")=="PPIA-13", "backlog current work must remain PPIA-13")
    require(tranches["PPIA-13"].get("status")=="started", "PPIA-13 backlog must remain started during completion review")
    require(tranches["PPIA-14"].get("status")=="planned" and "PPIA-13" in tranches["PPIA-14"].get("dependencies",[]), "PPIA-14 must remain planned/dependent")
    require(tranches["PPIA-08"].get("status")=="completed_verified", "PPIA-08 dependency must remain complete")
    require(checkpoint.get("work_item_id")=="PPIA-13" and checkpoint.get("status") in {"started","ready_for_review"}, "PPIA-13 checkpoint must remain active")
    require(checkpoint.get("owner_decision_required") is False and checkpoint.get("unresolved_failures")==[], "completion candidate must be unblocked")
    governed_scope=json.dumps({"objective":checkpoint.get("objective"),"active_substep":checkpoint.get("active_substep"),"next_action":checkpoint.get("next_action"),"completed_substeps":checkpoint.get("completed_substeps",[]),"notes":checkpoint.get("notes",[])},ensure_ascii=False).lower()
    for phrase in ("player","gm","creator","first launch","campaign join","character creation","first action","approval","library","inspector","permission","hidden-information","offline","reconnect","packs","troubleshooting","contextual","empty state","glossary","tutorial-campaign","accessibility","mobile","nonvisual","ppia-14","gm academy","completion"):
        require(phrase in governed_scope, f"checkpoint governed scope missing {phrase!r}")
    selected=[x for x in pointer.get("active_attempts",[]) if x.get("owner_selected")]
    require(len(selected)==1 and selected[0].get("work_item_id")=="PPIA-13", "pointer must select PPIA-13")
    current=selected[0]
    for field in ("attempt_id","branch","status","updated_at","roadmap_projection_pending"):
        require(current.get(field)==checkpoint.get(field), f"pointer/checkpoint mismatch {field}")
    primary=status.get("primary",{})
    for field in ("work_item_id","attempt_id","branch","status","active_substep","next_action","latest_pushed_commit","pull_request","owner_decision_required","unresolved_failures","roadmap_projection_pending"):
        require(primary.get(field)==checkpoint.get(field), f"compact status/checkpoint mismatch {field}")
    boundaries=backlog.get("boundaries",{})
    for key in ("application_runtime_mutation_authorized","a2_activation_authorized","release_authorized","deployment_authorized","tester_access_authorized","canonical_promotion_without_source_evidence_authorized"):
        require(boundaries.get(key) is False, f"completion gate may not enable {key}")
    require(boundaries.get("requires_codex") is False, "PPIA completion may not require Codex")
    all_text=(json.dumps(acceptance)+json.dumps(scope)+json.dumps(package)+report+json.dumps(workflows)+json.dumps(actions)+governed_scope).lower()
    for prohibited in ("runtime_activation=true","a2_activation_authorized=true","release_authorized=true","deployment_authorized=true","tester_access_authorized=true","canonical_promotion_without_source_evidence_authorized=true"):
        require(prohibited not in all_text, f"prohibited authorization {prohibited!r}")

    print("PPIA-13 COMPLETION CONTRACT: PASS")
    print("surface=18 teaching surfaces / 9 roles / 12 content types / 12 triggers")
    print("library=52 effective teaching entries / 18 projection groups / 30 actions")
    print("academy=5 tracks / 53 modules / 24 curated developed-source modules / optional non-gating")
    print("workflows=18 / handoffs=13 / cases=30+20+40+36=126 exactly once")
    print("mutation=P13-MUT-001 permission_before_derivatives=true offline_authoritative_mutation=false")
    print("gaps=P13-GAP-001 preserved / Multiversal outline gaps explicit / PPIA-14 final microcopy retained")
    print("accessibility=mobile+keyboard+touch+screen-reader+high-zoom+reduced-motion+noncolor zero-ai-parity")
    print("completion_candidate=true runtime_activation=false ppia13_status=started")

if __name__ == "__main__":
    main()
