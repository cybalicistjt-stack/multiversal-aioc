#!/usr/bin/env python3
from __future__ import annotations
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / "governance/application-planning/parallel-preimplementation"
FILES = {
    "owner": BASE / "PPIA-06_OWNER_VISUAL_CANON_DECISIONS_v0.1.0.json",
    "authority": BASE / "PPIA-06_SPECIES_VISUAL_AUTHORITY_MANIFEST_v0.1.0.json",
    "profiles": BASE / "PPIA-06_SPECIES_MORPHOLOGY_PROFILES_v0.1.0.json",
    "taxonomy": BASE / "PPIA-06_APPEARANCE_SEMANTIC_TAXONOMY_v0.2.0.json",
    "renderer": BASE / "PPIA-06_PIXEL_ART_RENDERER_CONTRACT_v0.2.0.json",
    "surface": BASE / "PPIA-06_APPEARANCE_STUDIO_CONTROL_SURFACE_v0.1.0.json",
    "inspector": BASE / "PPIA-06_APPEARANCE_INSPECTOR_ACTION_CONTRACT_MATRIX_v0.1.0.json",
    "preset": BASE / "PPIA-06_PRESET_RANDOMIZATION_IMPORT_EXPORT_CONTRACT_v0.1.0.json",
    "iar": BASE / "PPIA-06_APPEARANCE_INSPECTOR_REFERENCE_CASES_v0.1.0.json",
    "species_cases": BASE / "PPIA-06_SPECIES_VISUAL_REFERENCE_CASES_v0.1.0.json",
    "workflows": BASE / "PPIA-06_APPEARANCE_WORKFLOW_CONTRACT_MATRIX_v0.2.0.json",
    "trace": BASE / "PPIA-06_APPEARANCE_WORKFLOW_TRACEABILITY_MATRIX_v0.1.0.json",
    "species_coverage": BASE / "PPIA-06_SPECIES_WORKFLOW_COVERAGE_MATRIX_v0.1.0.json",
    "integrated_cases": BASE / "PPIA-06_INTEGRATED_WORKFLOW_REFERENCE_CASES_v0.1.0.json",
    "index": BASE / "PPIA-06_WORKFLOW_PACKAGE_INDEX_v0.1.0.json",
}
REPORT = BASE / "PPIA-06_COMPLETION_REPORT.md"
BACKLOG = BASE / "PPIA_PROGRAM_BACKLOG.json"
CP = ROOT / "governance/ai/work-state/PPIA-06-attempt-001.json"
PTR = ROOT / "governance/ai/runtime/CURRENT_WORK_POINTER.json"
STATUS = ROOT / "governance/ai/runtime/CURRENT_IMPLEMENTATION_STATUS.json"

MILESTONES = [
    ("d788d42187c5d53d2121a1f738b9d3445d0f67d8", "66789fcb140b06c7873231e28baf1c00dec8db91"),
    ("17b333d950b8748e625f1b96cc294d1ec582bc63", "65b6a7cd9d2cbaa72cad20aab1b72781df37f145"),
    ("4c25ea2e59b0fc40639387eed6654bf74a83d64c", "f4657ba33c4c9ad48ee97354be0ad3eed55433c2"),
    ("58222dacbbf7e3ed40c5d8dad1630a01acf32876", "37b974e0395c77d546276ea5a5a20fe3859334c3"),
]
EXPECTED_SPECIES = {
    "Human","Elf","Dwarf","Goblin","Orc","Giantkin","Stygian","Sharr","Gray","The Free",
    "Ratman","Furashin","Rog","Rohai","Moravi","Vespin","Rakuuta","Traiga","Kola-Ha","Toba-Madra",
    "Arborae","Mythragara","Suula","Nekron","ManyToms"
}
EXPECTED_COUNTS = {
    "workflows":16,"mutation_workflows":14,"read_analysis_workflows":2,"species_profiles":25,
    "projection_groups":20,"actions":30,"iar_cases":48,"species_visual_cases":36,"integrated_cases":32,
    "effective_cases":116,"semantic_layers":18,"compatibility_dimensions":5,"handoffs":9
}


def fail(msg):
    raise SystemExit("PPIA-06 COMPLETION CONTRACT: FAIL — " + msg)


def req(cond, msg):
    if not cond:
        fail(msg)


def load(path):
    req(path.exists(), f"missing {path.relative_to(ROOT)}")
    return json.loads(path.read_text(encoding="utf-8"))


def main():
    docs = {k: load(v) for k, v in FILES.items()}
    backlog, cp, ptr, status = map(load, (BACKLOG, CP, PTR, STATUS))
    req(REPORT.exists(), "missing completion report")
    report = REPORT.read_text(encoding="utf-8").lower()

    owner = docs["owner"]
    req(len(owner.get("decisions", [])) == 27, "expected 27 owner visual-canon decisions")
    ovc27 = next((x for x in owner.get("decisions", []) if x.get("id") == "OVC-027"), None)
    req(ovc27 is not None and "all rat-humanoid images" in ovc27.get("decision", "").lower(), "OVC-027 missing")
    req("separate canonical ratman species" in ovc27.get("decision", "").lower(), "OVC-027 Ratman separation missing")
    req("non-authoritative" in owner.get("source_authority_policy", {}).get("filename_or_prompt_label", "").lower(), "filename/prompt authority weakened")

    authority = docs["authority"]
    inv = authority.get("inventory", {})
    req(inv.get("pdf_count") == 27 and inv.get("art_count") == 88, "Species visual source inventory changed")
    req(len(authority.get("document_sources", [])) == 27, "27 document sources required")
    req(len(authority.get("art_manifest_parts", [])) == 4, "four art manifest parts required")
    req("non-authoritative" in authority.get("art_policy", {}).get("filename_or_prompt_label", "").lower(), "art filename/prompt policy weakened")

    profiles = docs["profiles"]
    req(profiles.get("profile_count") == 25 and len(profiles.get("profiles", [])) == 25, "25 Species morphology profiles required")
    req({x.get("species") for x in profiles.get("profiles", [])} == EXPECTED_SPECIES, "Species profile set changed")

    taxonomy = docs["taxonomy"]
    req(taxonomy.get("schema_version") == "0.2.0", "taxonomy v0.2.0 required")
    req([x.get("id") for x in taxonomy.get("identity_state_layers", [])] == [f"P06-L{i:02d}" for i in range(1, 19)], "18 semantic layer IDs changed")
    req([x.get("id") for x in taxonomy.get("compatibility_dimensions", [])] == [f"P06-COMP-{i:02d}" for i in range(1, 6)], "five compatibility dimensions changed")
    req(taxonomy.get("renderer_support_states") == ["supported","partial","unsupported","unknown"], "renderer support states changed")
    graph = taxonomy.get("morphology_graph_contract", {})
    req("constituent_body" in graph.get("node_kinds", []) and "nested_appendage" in graph.get("node_kinds", []), "nonhumanoid/composite morphology nodes missing")
    state_rules = " ".join(taxonomy.get("state_rules", [])).lower()
    for phrase in ("unknown/source-unspecified", "valid character remains valid", "hidden biological facts", "presentation wardrobe", "actual equipment preview", "randomization", "color is never"):
        req(phrase in state_rules, f"taxonomy state rule missing {phrase!r}")

    renderer = docs["renderer"]
    req(renderer.get("renderer_id") == "pixel-art-v1" and renderer.get("renderer_version") == "0.2.0", "pixel-art-v1 contract changed")
    future = renderer.get("future_renderer_boundary", {})
    req(all(future.get(k) is True for k in ("future_3d_supported_by_contract","core_state_may_not_require_sprite_or_pixel_fields","renderer_metadata_separate_from_character_truth")), "future renderer boundary weakened")
    views = renderer.get("view_contract", {})
    req(views.get("master_view") == "full_body_three_quarter", "master view changed")
    req(set(views.get("switchable_during_customization", [])) == {"full_body_three_quarter","portrait_zoom","tactical_token"}, "view set changed")
    req(views.get("arbitrary_rotation") is False and views.get("pseudo_3d_rotation") is False, "2D renderer rotation boundary weakened")
    req(renderer.get("stable_asset_identity", {}).get("required") is True and renderer.get("stable_asset_identity", {}).get("filename_authoritative") is False, "stable asset identity changed")
    req(renderer.get("topology", {}).get("humanoid_default_forbidden") is True and renderer.get("topology", {}).get("unsupported_topology_does_not_invalidate_character") is True, "renderer topology boundary weakened")
    perm = renderer.get("permission_and_export", {})
    req(all(perm.get(k) is True for k in ("filter_before_asset_selection","filter_before_derivatives","filter_before_export","filter_before_ai_context")), "renderer permission filtering weakened")

    surface = docs["surface"]
    req(len(surface.get("inspector_sections", [])) == 18, "18 Appearance Studio Inspector sections required")
    req(len({x.get("id") for x in surface.get("inspector_sections", [])}) == 18, "Inspector section IDs must be unique")

    inspector = docs["inspector"]
    req(inspector.get("counts") == {"projection_groups":20,"semantic_layers":18,"compatibility_dimensions":5,"actions":30,"reads":12,"analysis_proposals":10,"writes":8,"inherited_species_reference_cases":36}, "Inspector/action counts changed")
    groups, actions = inspector.get("projection_groups", []), inspector.get("actions", [])
    req({x.get("id") for x in groups} == {f"P06-PG-{i:03d}" for i in range(1,21)}, "20 projection groups changed")
    req({x.get("id") for x in actions} == {f"P06-ACT-{i:03d}" for i in range(1,31)}, "30 governed actions changed")
    req(sum(x.get("kind") == "read" for x in actions) == 12 and sum(x.get("kind") == "analysis_proposal" for x in actions) == 10 and sum(x.get("kind") == "write" for x in actions) == 8, "12/10/8 action split changed")
    req(all(x.get("protocol") == "P06-MUT-001" for x in actions if x.get("kind") == "write"), "all writes must use P06-MUT-001")
    mut = inspector.get("mutation_protocols", {}).get("P06-MUT-001", {})
    req(mut.get("required") == ["authorization","expected_version","operation_id"], "P06-MUT-001 required fields changed")
    req(mut.get("version_field") == "appearance_state_version", "appearance version field changed")
    for key in ("source_biology_mutation","current_form_or_transition_mutation","persistent_history_mutation","equipment_mutation","renderer_coverage_mutation","ai_authoritative_mutation"):
        req(mut.get(key) is False, f"mutation boundary enabled: {key}")

    preset = docs["preset"]
    req(len(preset.get("preset_scopes", [])) == 6, "six preset scopes required")
    req(len(preset.get("import_classifications", [])) == 9, "nine import classifications required")
    req("seed" in preset.get("randomization_inputs", []) and "lock_set" in preset.get("randomization_inputs", []), "deterministic randomization inputs changed")
    low_preset = json.dumps(preset, ensure_ascii=False).lower()
    for phrase in ("no silent substitution", "required anatomy cannot be removed", "equipment ownership/equipped state cannot be randomized", "renderer_filename_identity_forbidden"):
        req(phrase in low_preset, f"preset/randomization invariant missing {phrase!r}")

    iar = docs["iar"]
    req(iar.get("counts") == {"new_inspector_action_reference_cases":48,"inherited_species_visual_cases":36,"effective_case_surface":84}, "IAR counts changed")
    req(len(iar.get("cases", [])) == 48 and {x.get("id") for x in iar.get("cases", [])} == {f"P06-IAR-{i:03d}" for i in range(1,49)}, "48 IAR cases changed")
    species_cases = docs["species_cases"]
    req(species_cases.get("case_count") == 36 and len(species_cases.get("cases", [])) == 36, "36 Species Visual cases changed")

    workflows, trace = docs["workflows"], docs["trace"]
    req(workflows.get("counts") == EXPECTED_COUNTS and trace.get("counts") == EXPECTED_COUNTS, "workflow/trace counts changed")
    req([x.get("id") for x in workflows.get("workflows", [])] == [f"P06-WF-{i:03d}" for i in range(1,17)], "16 workflow IDs changed")
    req(sum(x.get("mutation") is True for x in workflows.get("workflows", [])) == 14 and sum(x.get("mutation") is False for x in workflows.get("workflows", [])) == 2, "14/2 workflow split changed")
    policy = workflows.get("workflow_policy", {})
    for key in ("all_species_profiles_exercised","permission_filter_before_reference_resolution","permission_filter_before_derivatives","permission_filter_before_renderer_asset_selection","mutation_requires_P06_MUT_001","expected_version_required_for_write","operation_id_required_for_write","ambiguous_result_recovery_before_retry","semantic_nonvisual_parity_required"):
        req(policy.get(key) is True, f"workflow policy disabled: {key}")
    for key in ("hidden_derivative_leak","renderer_output_authoritative","view_output_authoritative","filename_prompt_species_inference","species_form_biology_mutation","equipment_state_mutation","presentation_wardrobe_grants_mechanics","silent_preset_substitution","arbitrary_rotation","pseudo_3d","runtime_activation"):
        req(policy.get(key) is False, f"workflow prohibition weakened: {key}")

    expected_iar = {f"P06-IAR-{i:03d}" for i in range(1,49)}
    expected_sv = {f"P06-SV-{i:02d}" for i in range(1,37)}
    expected_iw = {f"P06-IW-{i:03d}" for i in range(1,33)}
    rows = trace.get("rows", [])
    assigned_iar = [c for row in rows for c in row.get("iar_cases", [])]
    assigned_sv = [c for row in rows for c in row.get("species_visual_cases", [])]
    assigned_iw = [c for row in rows for c in row.get("integrated_cases", [])]
    req(len(assigned_iar) == 48 and set(assigned_iar) == expected_iar and len(set(assigned_iar)) == 48, "IAR cases not assigned exactly once")
    req(len(assigned_sv) == 36 and set(assigned_sv) == expected_sv and len(set(assigned_sv)) == 36, "Species Visual cases not assigned exactly once")
    req(len(assigned_iw) == 32 and set(assigned_iw) == expected_iw and len(set(assigned_iw)) == 32, "integrated cases not assigned exactly once")
    req(trace.get("coverage") == {"workflows":"16/16","species_profiles":"25/25","projection_groups":"20/20 derived from action groups","actions":"30/30","iar_cases":"48/48 exactly once","species_visual_cases":"36/36 exactly once","integrated_cases":"32/32 exactly once","semantic_layers":"18/18 inherited","compatibility_dimensions":"5/5 inherited","handoffs":"9/9"}, "trace coverage changed")

    species_cov = docs["species_coverage"]
    req(species_cov.get("profile_count") == 25 and len(species_cov.get("rows", [])) == 25 and species_cov.get("coverage") == "25/25", "25/25 Species workflow coverage changed")
    req({x.get("species") for x in species_cov.get("rows", [])} == EXPECTED_SPECIES, "Species workflow coverage set changed")
    special = species_cov.get("special_assertions", {})
    req("distinct canonical Species" in special.get("Ratman", "") and "OVC-027" in special.get("Furashin", ""), "Ratman/Furashin coverage separation changed")

    integrated = docs["integrated_cases"]
    req(integrated.get("case_count") == 32 and len(integrated.get("cases", [])) == 32, "32 integrated cases changed")
    req({x.get("id") for x in integrated.get("cases", [])} == expected_iw, "integrated case IDs changed")

    index = docs["index"]
    req(index.get("active_workflow_contract") == "PPIA-06_APPEARANCE_WORKFLOW_CONTRACT_MATRIX_v0.2.0.json", "active workflow contract changed")
    req(index.get("counts") == {"species":25,"workflows":16,"effective_cases":116}, "workflow package index counts changed")

    for head, merge in MILESTONES:
        req(head in report and merge in report, f"completion report missing milestone {head}/{merge}")
    for phrase in (
        "completion candidate — not complete until this exact head passes required validation and merges",
        "implementation-ready appearance-studio specification", "all 25 governed species", "18 renderer-independent semantic appearance layers",
        "5 compatibility dimensions", "20 permission-safe projection groups", "30 governed actions", "12 reads / 10 analysis-proposals / 8 writes",
        "16 integrated workflows", "9 explicit authority/domain handoffs", "116 effective deterministic cases", "ovc-027 furashin/ratman separation",
        "p06-mut-001", "pixel-art-v1", "future renderer boundary", "semantic nonvisual", "ppia-06 → ppia-13 transition"
    ):
        req(phrase in report, f"completion report missing {phrase!r}")

    tranches = {x.get("work_item_id"): x for x in backlog.get("tranches", [])}
    req("PPIA-06" in tranches and "PPIA-13" in tranches, "PPIA-06/PPIA-13 backlog entries missing")
    cp_status = cp.get("status")
    req(cp_status in {"started","completed_verified"}, f"unexpected checkpoint status {cp_status!r}")
    req(cp.get("attempt_id") == "PPIA-06-attempt-001" and cp.get("branch") == "governance/ppia-06-character-appearance-creator", "checkpoint identity changed")
    req(cp.get("unresolved_failures") == [] and cp.get("owner_decision_required") is False, "PPIA-06 unresolved state")
    history = json.dumps({"last_verified_action":cp.get("last_verified_action"),"completed_substeps":cp.get("completed_substeps",[]),"validation":cp.get("validation",[]),"evidence":cp.get("evidence",[])}, ensure_ascii=False).lower()
    for head, merge in MILESTONES:
        req(head in history and merge in history, f"checkpoint missing immutable milestone evidence {head}/{merge}")

    p06_status = tranches["PPIA-06"].get("status")
    if p06_status == "started":
        req(backlog.get("current_work_item_id") == "PPIA-06" and tranches["PPIA-13"].get("status") == "planned", "pre-transition backlog continuity changed")
        req(ptr.get("primary_attempt_id") == "PPIA-06-attempt-001" and status.get("primary", {}).get("work_item_id") == "PPIA-06", "pre-transition runtime continuity changed")
        if cp_status == "started":
            active = ((cp.get("active_substep") or "") + " " + (cp.get("next_action") or "")).lower()
            req("completion" in active and "ppia-06" in active, "started checkpoint not on PPIA-06 completion gate")
        else:
            req("validate ppia-06 completion contract" in history, "completed checkpoint missing completion validation evidence")
        continuity = "ppia06_completion_pretransition"
    else:
        req(p06_status == "completed_verified", "post-transition PPIA-06 must be completed_verified")
        req(tranches["PPIA-13"].get("status") == "started" and backlog.get("current_work_item_id") == "PPIA-13", "post-transition backlog must select PPIA-13")
        req(cp_status == "completed_verified", "post-transition PPIA-06 checkpoint must remain completed_verified")
        req(status.get("primary", {}).get("work_item_id") == "PPIA-13" and status.get("primary", {}).get("status") == "started", "post-transition compact status must select PPIA-13")
        continuity = "ppia06_historical_after_ppia13_transition"

    bounds = backlog.get("boundaries", {})
    for key in ("application_runtime_mutation_authorized","a2_activation_authorized","release_authorized","deployment_authorized","tester_access_authorized","canonical_promotion_without_source_evidence_authorized"):
        req(bounds.get(key) is False, f"program boundary changed: {key}")

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
