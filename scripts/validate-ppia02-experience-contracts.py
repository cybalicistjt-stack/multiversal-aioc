#!/usr/bin/env python3
"""Validate PPIA-02 Inspector/projection contracts and reference cases."""
from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PROGRAM = ROOT / "governance/application-planning/parallel-preimplementation"
MATRIX = PROGRAM / "PPIA-02_INSPECTOR_PROJECTION_MATRIX_v0.1.0.json"
CASES = PROGRAM / "PPIA-02_REFERENCE_CASES_v0.1.0.json"
HEX64 = re.compile(r"^[0-9a-f]{64}$")


def main() -> int:
    matrix = json.loads(MATRIX.read_text(encoding="utf-8"))
    cases = json.loads(CASES.read_text(encoding="utf-8"))

    if matrix.get("format") != "multiversal-ppia02-creature-npc-inspector-projection-matrix":
        raise SystemExit("unexpected Inspector/projection matrix format")
    if matrix.get("version") != "0.1.0" or matrix.get("work_item") != "PPIA-02":
        raise SystemExit("Inspector/projection matrix identity mismatch")

    groups = matrix.get("field_groups") or []
    expected_groups = {
        "identity", "encounter_core", "attributes_skills", "traits_actions", "defenses_conditions",
        "ecology_behavior", "persona_social", "assets_loot", "variants_forms", "summon_control",
        "placement", "runtime", "source_provenance",
    }
    if {group.get("id") for group in groups} != expected_groups:
        raise SystemExit("Inspector field-group set changed")

    profile_order = matrix.get("profile_section_order") or {}
    expected_profiles = {
        "creature_standard", "npc_persona", "sentient_hybrid", "swarm_group",
        "summon_minion_spawn", "stage_variant", "type_modifier", "playable_conversion",
    }
    if set(profile_order) != expected_profiles:
        raise SystemExit("Inspector profile-order set changed")

    overlays = matrix.get("context_overlays") or {}
    expected_contexts = {
        "library_reference", "gm_authoring", "scene_placement", "encounter_preparation", "live_runtime",
        "investigation_social", "exploration_bestiary", "comparison_variant", "summon_minion_spawn", "playable_conversion",
    }
    if set(overlays) != expected_contexts:
        raise SystemExit("Inspector context-overlay set changed")

    visibility = {item.get("id") for item in matrix.get("visibility_classes") or []}
    required_visibility = {
        "source_public", "campaign_revealed", "campaign_gm_private", "runtime_shared",
        "runtime_gm_private", "source_diagnostic", "user_private",
    }
    if visibility != required_visibility:
        raise SystemExit("visibility-class set changed")

    role_projection = matrix.get("role_projection") or {}
    if set(role_projection) != {"player", "gm", "assistant_gm", "creator_owner_admin", "service_ai"}:
        raise SystemExit("role-projection set changed")
    player_never = set(role_projection["player"].get("never_receive_without_explicit_separate_authority") or [])
    if not {"campaign_gm_private", "runtime_gm_private", "user_private"}.issubset(player_never):
        raise SystemExit("Player projection can receive private data by default")
    if "user_private" not in set(role_projection["gm"].get("never_implicit") or []):
        raise SystemExit("GM projection incorrectly implies user-private access")

    acceptance = matrix.get("acceptance_invariants") or []
    required_acceptance_terms = [
        "Hidden creature/NPC existence",
        "Source Definition identity, placement identity, and live instance identity",
        "source-backed variant chain",
        "without fabricating replacement content",
    ]
    for term in required_acceptance_terms:
        if not any(term in item for item in acceptance):
            raise SystemExit(f"Inspector acceptance lost invariant: {term}")

    if cases.get("format") != "multiversal-ppia02-creature-npc-reference-cases":
        raise SystemExit("unexpected PPIA-02 reference-case format")
    if cases.get("version") != "0.1.0" or cases.get("work_item") != "PPIA-02":
        raise SystemExit("reference-case identity mismatch")
    policy = cases.get("policy") or {}
    if policy.get("source_grounded_cases_preserve_source_facts") is not True:
        raise SystemExit("reference-case source facts are not preserved")
    if policy.get("synthetic_cases_are_canonical_content") is not False:
        raise SystemExit("synthetic QA cases were promoted into canonical content")
    if policy.get("legacy_semantic_database_required") is not False:
        raise SystemExit("reference cases require obsolete semantic database")
    if policy.get("automatic_identity_merge") is not False:
        raise SystemExit("reference cases allow automatic identity merge")

    sources = cases.get("source_evidence") or []
    if len(sources) != 4 or len({item.get("id") for item in sources}) != 4:
        raise SystemExit("reference-case source evidence set changed")
    if any(not HEX64.fullmatch(item.get("sha256") or "") for item in sources):
        raise SystemExit("reference-case source evidence has invalid SHA-256")

    rows = cases.get("cases") or []
    if len(rows) != 12 or len({row.get("case_id") for row in rows}) != 12:
        raise SystemExit("reference-case set must contain 12 unique cases")
    source_grounded = [row for row in rows if row.get("kind") == "source_grounded"]
    synthetic = [row for row in rows if row.get("kind") == "synthetic_qa"]
    if len(source_grounded) != 7 or len(synthetic) != 5:
        raise SystemExit("reference-case source/synthetic split changed")
    if any(row.get("canonical_content") is not False for row in synthetic):
        raise SystemExit("a synthetic reference case is not explicitly noncanonical")

    first = next(row for row in rows if row["case_id"] == "PPIA02-RC-001")
    if first.get("subject") != "Sapcrawl Varnet":
        raise SystemExit(f"Havalaea source subject mismatch: {first.get('subject')!r}")
    if not any("Behavior" in fact for fact in first.get("source_facts") or []):
        raise SystemExit("ordinary creature reference lost source-backed Behavior")

    type_case = next(row for row in rows if row["case_id"] == "PPIA02-RC-003")
    if type_case.get("profile") != "type_modifier":
        raise SystemExit("Creature Types case no longer tests modifier-layer presentation")
    if not any("word 'may' remains conditional" in item for item in type_case.get("acceptance") or []):
        raise SystemExit("Creature Types case no longer protects conditional source language")

    conversion = next(row for row in rows if row["case_id"] == "PPIA02-RC-006")
    if conversion.get("profile") != "playable_conversion":
        raise SystemExit("playable conversion case lost conversion profile")
    if not any("without identity equivalence" in item for item in conversion.get("acceptance") or []):
        raise SystemExit("playable conversion case lost identity boundary")

    hidden = next(row for row in rows if row["case_id"] == "PPIA02-RC-009")
    hidden_acceptance = " ".join(hidden.get("acceptance") or [])
    for term in ("no existence", "count", "wave", "search suggestion", "facet contribution", "compare target"):
        if term not in hidden_acceptance:
            raise SystemExit(f"hidden placement case lost leak-protection term: {term}")

    summary = cases.get("summary") or {}
    expected_summary = {
        "cases": 12,
        "source_grounded_cases": 7,
        "synthetic_qa_cases": 5,
        "canonical_synthetic_records": 0,
        "source_pdfs_used": 4,
    }
    if summary != expected_summary:
        raise SystemExit(f"reference-case summary changed: {summary}")

    print(json.dumps({
        "fieldGroups": len(groups),
        "presentationProfiles": len(profile_order),
        "contextOverlays": len(overlays),
        "referenceCases": len(rows),
        "sourceGroundedCases": len(source_grounded),
        "syntheticQaCases": len(synthetic),
        "canonicalSyntheticRecords": 0,
        "result": "PASS",
    }, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
