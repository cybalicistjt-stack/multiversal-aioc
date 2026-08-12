#!/usr/bin/env python3
from __future__ import annotations
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / "governance/application-planning/parallel-preimplementation"

def j(name):
    p = BASE / name
    if not p.exists():
        raise SystemExit(f"PPIA-06 COMPLETION CONTRACT: FAIL — missing {p.relative_to(ROOT)}")
    return json.loads(p.read_text(encoding="utf-8"))

def req(cond, msg):
    if not cond:
        raise SystemExit("PPIA-06 COMPLETION CONTRACT: FAIL — " + msg)

MILESTONES = [
    ("d788d42187c5d53d2121a1f738b9d3445d0f67d8", "66789fcb140b06c7873231e28baf1c00dec8db91"),
    ("17b333d950b8748e625f1b96cc294d1ec582bc63", "65b6a7cd9d2cbaa72cad20aab1b72781df37f145"),
    ("4c25ea2e59b0fc40639387eed6654bf74a83d64c", "f4657ba33c4c9ad48ee97354be0ad3eed55433c2"),
    ("58222dacbbf7e3ed40c5d8dad1630a01acf32876", "37b974e0395c77d546276ea5a5a20fe3859334c3"),
]
SPECIES = {"Human","Elf","Dwarf","Goblin","Orc","Giantkin","Stygian","Sharr","Gray","The Free","Ratman","Furashin","Rog","Rohai","Moravi","Vespin","Rakuuta","Traiga","Kola-Ha","Toba-Madra","Arborae","Mythragara","Suula","Nekron","ManyToms"}
COUNTS = {"workflows":16,"mutation_workflows":14,"read_analysis_workflows":2,"species_profiles":25,"projection_groups":20,"actions":30,"iar_cases":48,"species_visual_cases":36,"integrated_cases":32,"effective_cases":116,"semantic_layers":18,"compatibility_dimensions":5,"handoffs":9}

def main():
    owner = j("PPIA-06_OWNER_VISUAL_CANON_DECISIONS_v0.1.0.json")
    authority = j("PPIA-06_SPECIES_VISUAL_AUTHORITY_MANIFEST_v0.1.0.json")
    profiles = j("PPIA-06_SPECIES_MORPHOLOGY_PROFILES_v0.1.0.json")
    taxonomy = j("PPIA-06_APPEARANCE_SEMANTIC_TAXONOMY_v0.2.0.json")
    renderer = j("PPIA-06_PIXEL_ART_RENDERER_CONTRACT_v0.2.0.json")
    surface = j("PPIA-06_APPEARANCE_STUDIO_CONTROL_SURFACE_v0.1.0.json")
    inspector = j("PPIA-06_APPEARANCE_INSPECTOR_ACTION_CONTRACT_MATRIX_v0.1.0.json")
    preset = j("PPIA-06_PRESET_RANDOMIZATION_IMPORT_EXPORT_CONTRACT_v0.1.0.json")
    iar = j("PPIA-06_APPEARANCE_INSPECTOR_REFERENCE_CASES_v0.1.0.json")
    sv = j("PPIA-06_SPECIES_VISUAL_REFERENCE_CASES_v0.1.0.json")
    workflows = j("PPIA-06_APPEARANCE_WORKFLOW_CONTRACT_MATRIX_v0.2.0.json")
    trace = j("PPIA-06_APPEARANCE_WORKFLOW_TRACEABILITY_MATRIX_v0.1.0.json")
    coverage = j("PPIA-06_SPECIES_WORKFLOW_COVERAGE_MATRIX_v0.1.0.json")
    iw = j("PPIA-06_INTEGRATED_WORKFLOW_REFERENCE_CASES_v0.1.0.json")
    index = j("PPIA-06_WORKFLOW_PACKAGE_INDEX_v0.1.0.json")
    acceptance = j("PPIA-06_COMPLETION_ACCEPTANCE_MATRIX_v0.1.0.json")
    scope = j("PPIA-06_COMPLETION_SCOPE_LOCK_v0.1.0.json")
    package = j("PPIA-06_COMPLETION_PACKAGE_INDEX_v0.1.0.json")

    report_path = BASE / "PPIA-06_COMPLETION_REPORT.md"
    req(report_path.exists(), "missing completion report")
    report = report_path.read_text(encoding="utf-8").lower()

    req(len(owner.get("decisions", [])) == 27, "27 owner visual-canon decisions required")
    ovc27 = next((x for x in owner["decisions"] if x.get("id") == "OVC-027"), None)
    req(ovc27 and "all rat-humanoid images" in ovc27.get("decision", "").lower(), "OVC-027 missing")
    req("separate canonical ratman species" in ovc27.get("decision", "").lower(), "OVC-027 Ratman separation missing")
    req("non-authoritative" in owner["source_authority_policy"]["filename_or_prompt_label"].lower(), "filename/prompt authority weakened")

    inv = authority.get("inventory", {})
    req((inv.get("pdf_count"), inv.get("art_count")) == (27, 88), "27-PDF/88-art source inventory changed")
    req(len(authority.get("document_sources", [])) == 27 and len(authority.get("art_manifest_parts", [])) == 4, "source manifest structure changed")

    req(profiles.get("profile_count") == 25 and len(profiles.get("profiles", [])) == 25, "25 Species profiles required")
    req({x.get("species") for x in profiles["profiles"]} == SPECIES, "Species profile set changed")

    req([x.get("id") for x in taxonomy.get("identity_state_layers", [])] == [f"P06-L{i:02d}" for i in range(1,19)], "18 semantic layers changed")
    req([x.get("id") for x in taxonomy.get("compatibility_dimensions", [])] == [f"P06-COMP-{i:02d}" for i in range(1,6)], "five compatibility dimensions changed")
    req(taxonomy.get("renderer_support_states") == ["supported","partial","unsupported","unknown"], "renderer support states changed")
    graph = taxonomy.get("morphology_graph_contract", {})
    req("nested_appendage" in graph.get("node_kinds", []) and "constituent_body" in graph.get("node_kinds", []), "nested/composite morphology support missing")
    rules = " ".join(taxonomy.get("state_rules", [])).lower()
    for phrase in ("unknown/source-unspecified", "valid character remains valid", "hidden biological facts", "presentation wardrobe", "actual equipment preview", "randomization", "color is never"):
        req(phrase in rules, f"semantic boundary missing {phrase!r}")

    req(renderer.get("renderer_id") == "pixel-art-v1" and renderer.get("renderer_version") == "0.2.0", "renderer identity changed")
    future = renderer.get("future_renderer_boundary", {})
    req(all(future.get(k) is True for k in ("future_3d_supported_by_contract","core_state_may_not_require_sprite_or_pixel_fields","renderer_metadata_separate_from_character_truth")), "future renderer boundary weakened")
    views = renderer.get("view_contract", {})
    req(views.get("master_view") == "full_body_three_quarter", "master view changed")
    req(set(views.get("switchable_during_customization", [])) == {"full_body_three_quarter","portrait_zoom","tactical_token"}, "view support changed")
    req(views.get("arbitrary_rotation") is False and views.get("pseudo_3d_rotation") is False, "2D rotation boundary weakened")
    req(renderer.get("stable_asset_identity", {}).get("required") is True and renderer.get("stable_asset_identity", {}).get("filename_authoritative") is False, "stable asset boundary changed")
    req(renderer.get("topology", {}).get("humanoid_default_forbidden") is True and renderer.get("topology", {}).get("unsupported_topology_does_not_invalidate_character") is True, "renderer topology boundary weakened")
    req(all(renderer.get("permission_and_export", {}).get(k) is True for k in ("filter_before_asset_selection","filter_before_derivatives","filter_before_export","filter_before_ai_context")), "renderer permission filtering weakened")

    req(len(surface.get("inspector_sections", [])) == 18, "18 Appearance Studio sections required")
    req(len({x.get("id") for x in surface["inspector_sections"]}) == 18, "Appearance Studio section IDs duplicated")

    req(inspector.get("counts") == {"projection_groups":20,"semantic_layers":18,"compatibility_dimensions":5,"actions":30,"reads":12,"analysis_proposals":10,"writes":8,"inherited_species_reference_cases":36}, "Inspector/action counts changed")
    actions = inspector.get("actions", [])
    req({x.get("id") for x in inspector.get("projection_groups", [])} == {f"P06-PG-{i:03d}" for i in range(1,21)}, "20 projection groups changed")
    req({x.get("id") for x in actions} == {f"P06-ACT-{i:03d}" for i in range(1,31)}, "30 actions changed")
    req(sum(x.get("kind") == "read" for x in actions) == 12 and sum(x.get("kind") == "analysis_proposal" for x in actions) == 10 and sum(x.get("kind") == "write" for x in actions) == 8, "12/10/8 action split changed")
    req(all(x.get("protocol") == "P06-MUT-001" for x in actions if x.get("kind") == "write"), "write protocol changed")
    mut = inspector.get("mutation_protocols", {}).get("P06-MUT-001", {})
    req(mut.get("required") == ["authorization","expected_version","operation_id"] and mut.get("version_field") == "appearance_state_version", "P06-MUT-001 version/idempotency inputs changed")
    for key in ("source_biology_mutation","current_form_or_transition_mutation","persistent_history_mutation","equipment_mutation","renderer_coverage_mutation","ai_authoritative_mutation"):
        req(mut.get(key) is False, f"mutation boundary enabled: {key}")

    req(len(preset.get("preset_scopes", [])) == 6 and len(preset.get("import_classifications", [])) == 9, "preset/import classifications changed")
    req("seed" in preset.get("randomization_inputs", []) and "lock_set" in preset.get("randomization_inputs", []), "randomization determinism inputs changed")
    lowp = json.dumps(preset, ensure_ascii=False).lower()
    for phrase in ("no silent substitution","required anatomy cannot be removed","equipment ownership/equipped state cannot be randomized","renderer_filename_identity_forbidden"):
        req(phrase in lowp, f"preset/randomization boundary missing {phrase!r}")

    req(iar.get("counts") == {"new_inspector_action_reference_cases":48,"inherited_species_visual_cases":36,"effective_case_surface":84}, "IAR counts changed")
    req(len(iar.get("cases", [])) == 48 and {x.get("id") for x in iar["cases"]} == {f"P06-IAR-{i:03d}" for i in range(1,49)}, "48 IAR cases changed")
    req(sv.get("case_count") == 36 and len(sv.get("cases", [])) == 36, "36 Species Visual cases changed")

    req(workflows.get("counts") == COUNTS and trace.get("counts") == COUNTS, "workflow/trace counts changed")
    req([x.get("id") for x in workflows.get("workflows", [])] == [f"P06-WF-{i:03d}" for i in range(1,17)], "16 workflow IDs changed")
    req(sum(x.get("mutation") is True for x in workflows["workflows"]) == 14 and sum(x.get("mutation") is False for x in workflows["workflows"]) == 2, "14/2 workflow split changed")
    policy = workflows.get("workflow_policy", {})
    for key in ("all_species_profiles_exercised","permission_filter_before_reference_resolution","permission_filter_before_derivatives","permission_filter_before_renderer_asset_selection","mutation_requires_P06_MUT_001","expected_version_required_for_write","operation_id_required_for_write","ambiguous_result_recovery_before_retry","semantic_nonvisual_parity_required"):
        req(policy.get(key) is True, f"workflow policy disabled: {key}")
    for key in ("hidden_derivative_leak","renderer_output_authoritative","view_output_authoritative","filename_prompt_species_inference","species_form_biology_mutation","equipment_state_mutation","presentation_wardrobe_grants_mechanics","silent_preset_substitution","arbitrary_rotation","pseudo_3d","runtime_activation"):
        req(policy.get(key) is False, f"workflow prohibition weakened: {key}")

    rows = trace.get("rows", [])
    assigned_iar = [c for r in rows for c in r.get("iar_cases", [])]
    assigned_sv = [c for r in rows for c in r.get("species_visual_cases", [])]
    assigned_iw = [c for r in rows for c in r.get("integrated_cases", [])]
    req(len(assigned_iar) == 48 and set(assigned_iar) == {f"P06-IAR-{i:03d}" for i in range(1,49)} and len(set(assigned_iar)) == 48, "IAR trace not exactly once")
    req(len(assigned_sv) == 36 and set(assigned_sv) == {f"P06-SV-{i:02d}" for i in range(1,37)} and len(set(assigned_sv)) == 36, "Species Visual trace not exactly once")
    req(len(assigned_iw) == 32 and set(assigned_iw) == {f"P06-IW-{i:03d}" for i in range(1,33)} and len(set(assigned_iw)) == 32, "integrated trace not exactly once")
    req(trace.get("coverage") == {"workflows":"16/16","species_profiles":"25/25","projection_groups":"20/20 derived from action groups","actions":"30/30","iar_cases":"48/48 exactly once","species_visual_cases":"36/36 exactly once","integrated_cases":"32/32 exactly once","semantic_layers":"18/18 inherited","compatibility_dimensions":"5/5 inherited","handoffs":"9/9"}, "trace coverage changed")

    req(coverage.get("profile_count") == 25 and len(coverage.get("rows", [])) == 25 and coverage.get("coverage") == "25/25", "25/25 Species workflow coverage changed")
    req({x.get("species") for x in coverage["rows"]} == SPECIES, "Species workflow set changed")
    req("distinct canonical Species" in coverage.get("special_assertions", {}).get("Ratman", "") and "OVC-027" in coverage.get("special_assertions", {}).get("Furashin", ""), "Ratman/Furashin workflow separation changed")

    req(iw.get("counts", {}).get("integrated_cases") == 32 and len(iw.get("cases", [])) == 32, "32 integrated cases changed")
    req({x.get("id") for x in iw["cases"]} == {f"P06-IW-{i:03d}" for i in range(1,33)}, "integrated case IDs changed")
    req(iw.get("counts", {}).get("species_profiles_covered") == 25 and iw.get("counts", {}).get("effective_case_surface") == 116, "integrated coverage counts changed")

    req(index.get("active_workflow_contract") == "PPIA-06_APPEARANCE_WORKFLOW_CONTRACT_MATRIX_v0.2.0.json" and index.get("counts") == {"species":25,"workflows":16,"effective_cases":116}, "workflow package index changed")
    req(acceptance.get("counts") == {"acceptance_categories":16,"species":25,"semantic_layers":18,"compatibility_dimensions":5,"projection_groups":20,"actions":30,"workflows":16,"handoffs":9,"effective_cases":116}, "completion acceptance matrix counts changed")
    req([x.get("id") for x in acceptance.get("categories", [])] == [f"P06-CG-{i:02d}" for i in range(1,17)], "16 completion acceptance categories changed")
    req(acceptance.get("result") == "completion_candidate_only_until_exact_head_validation_and_merge", "completion acceptance result changed")
    req(scope.get("scope_locked") is True and scope.get("completion_requires") == "exact_head_all_green_hosted_validation_and_merge", "completion scope lock weakened")
    req(package.get("state") == "completion_candidate_only_until_exact_head_all_green_and_merge" and package.get("transition_after_completion") == "PPIA-06 -> PPIA-13 separate governed operation", "completion package transition boundary changed")

    for head, merge in MILESTONES:
        req(head in report and merge in report, f"completion report missing milestone {head}/{merge}")
    for phrase in ("completion candidate — not complete until this exact head passes required validation and merges","implementation-ready appearance-studio specification","all 25 governed species","eighteen stable semantic identity/state layers","five independent compatibility dimensions","twenty permission-safe projection groups","thirty governed actions","p06-mut-001","sixteen integrated workflows","nine explicit authority/domain handoffs","116 effective deterministic cases","ovc-027 furashin/ratman separation","pixel-art-v1","future renderer boundary","semantic nonvisual representation","ppia-06 → ppia-13 transition"):
        req(phrase in report, f"completion report missing {phrase!r}")

    backlog = j("PPIA_PROGRAM_BACKLOG.json")
    cp = json.loads((ROOT / "governance/ai/work-state/PPIA-06-attempt-001.json").read_text(encoding="utf-8"))
    ptr = json.loads((ROOT / "governance/ai/runtime/CURRENT_WORK_POINTER.json").read_text(encoding="utf-8"))
    status = json.loads((ROOT / "governance/ai/runtime/CURRENT_IMPLEMENTATION_STATUS.json").read_text(encoding="utf-8"))
    tranches = {x.get("work_item_id"): x for x in backlog.get("tranches", [])}
    req(cp.get("status") in {"started","completed_verified"} and cp.get("attempt_id") == "PPIA-06-attempt-001", "checkpoint identity/status changed")
    req(cp.get("unresolved_failures") == [] and cp.get("owner_decision_required") is False, "PPIA-06 unresolved state")
    history = json.dumps({"last_verified_action":cp.get("last_verified_action"),"completed_substeps":cp.get("completed_substeps",[]),"validation":cp.get("validation",[]),"evidence":cp.get("evidence",[])}, ensure_ascii=False).lower()
    for head, merge in MILESTONES:
        req(head in history and merge in history, f"checkpoint missing milestone evidence {head}/{merge}")

    if tranches.get("PPIA-06", {}).get("status") == "started":
        req(backlog.get("current_work_item_id") == "PPIA-06" and tranches.get("PPIA-13", {}).get("status") == "planned", "pre-transition backlog continuity changed")
        req(ptr.get("primary_attempt_id") == "PPIA-06-attempt-001" and status.get("primary", {}).get("work_item_id") == "PPIA-06", "pre-transition runtime continuity changed")
        if cp.get("status") == "started":
            active = ((cp.get("active_substep") or "") + " " + (cp.get("next_action") or "")).lower()
            req("completion" in active and "ppia-06" in active, "checkpoint not on completion gate")
        else:
            req("validate ppia-06 completion contract" in history, "completed checkpoint missing completion evidence")
        continuity = "ppia06_completion_pretransition"
    else:
        req(tranches.get("PPIA-06", {}).get("status") == "completed_verified" and tranches.get("PPIA-13", {}).get("status") == "started", "post-transition backlog state invalid")
        req(backlog.get("current_work_item_id") == "PPIA-13" and status.get("primary", {}).get("work_item_id") == "PPIA-13", "post-transition runtime must select PPIA-13")
        req(cp.get("status") == "completed_verified", "historical PPIA-06 checkpoint must remain completed_verified")
        continuity = "ppia06_historical_after_ppia13_transition"

    for key in ("application_runtime_mutation_authorized","a2_activation_authorized","release_authorized","deployment_authorized","tester_access_authorized","canonical_promotion_without_source_evidence_authorized"):
        req(backlog.get("boundaries", {}).get(key) is False, f"program boundary changed: {key}")

    print("PPIA-06 COMPLETION CONTRACT: PASS")
    print("surface=25 Species / 18 semantic layers / 5 compatibility dimensions / 20 projections")
    print("actions=30 (12 read / 10 analysis-proposal / 8 write) mutation=P06-MUT-001")
    print("workflows=16 (14 mutation / 2 read-analysis) / 9 handoffs")
    print("cases=48 IAR + 36 Species Visual + 32 integrated = 116 exactly traced")
    print("renderer=pixel-art-v1 fixed_three_quarter+portrait+token future_renderer_boundary=true")
    print("ovc027=all Arthold rat-humanoid art Furashin; Ratman separate=true")
    print(f"continuity={continuity} runtime_activation=false")

if __name__ == "__main__":
    main()
