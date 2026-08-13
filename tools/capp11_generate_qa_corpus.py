#!/usr/bin/env python3
"""Generate the CAPP-11 deterministic synthetic/noncanonical QA corpus."""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any

SCHEMA_VERSION = "0.1.0"
VIEWS = ["full_body_three_quarter", "portrait_zoom", "tactical_token"]
SUPPORT = ["supported", "partial", "unsupported", "unknown"]
INTERACTIONS = ["desktop", "tablet", "mobile", "keyboard", "screen_reader", "high_zoom", "reduced_motion"]
MIGRATIONS = ["renamed_option", "removed_option", "asset_pack_upgrade", "missing_asset_pack", "renderer_capability_change", "old_preset", "permission_projection_change"]
FIT_STATES = ["supported", "partial", "unsupported", "unknown"]
RANDOMIZATION = ["all_eligible", "unlocked_only", "category_only", "locked_incompatible_review"]


def canonical(value: Any) -> bytes:
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode("utf-8")


def case_id(payload: dict[str, Any]) -> str:
    return "CAPP11-QA-" + hashlib.sha256(canonical(payload)).hexdigest()[:16].upper()


def make_case(profile: dict[str, Any], category: str, dimensions: dict[str, Any], expected: list[str]) -> dict[str, Any]:
    core = {
        "profile_id": profile["profile_id"],
        "category": category,
        "dimensions": dimensions,
        "expected": expected,
    }
    return {
        "case_id": case_id(core),
        "provenance_class": "synthetic_noncanonical",
        **core,
    }


def generate(profile_index: dict[str, Any]) -> dict[str, Any]:
    profiles = profile_index.get("profiles", [])
    if len(profiles) != 25:
        raise ValueError(f"expected 25 profiles, found {len(profiles)}")
    cases: list[dict[str, Any]] = []

    for p in profiles:
        pid = p["profile_id"]
        topology = p.get("baseline_topology", "unknown")
        special = p.get("special_customizer_behavior", [])
        profile_behavior = p.get("studio_profile_behavior")
        appearance_model = p.get("appearance_state_model")

        for view in VIEWS:
            for support in SUPPORT:
                expected = ["character_state_remains_valid", "no_hidden_information_leak", "no_anatomy_fabrication"]
                if support != "supported":
                    expected.append("explicit_renderer_diagnostic")
                if support in {"unsupported", "unknown"}:
                    expected.append("no_silent_asset_substitution")
                cases.append(make_case(p, "renderer_coverage", {"view": view, "support_state": support, "topology": topology}, expected))

        for fit in FIT_STATES:
            expected = ["inventory_ownership_unchanged", "equipment_mechanics_unchanged", "topology_preserved"]
            if fit != "supported":
                expected.append("explicit_fit_diagnostic")
            if fit in {"unsupported", "unknown"}:
                expected.append("no_silent_warp")
            cases.append(make_case(p, "equipment_fit", {"fit_state": fit, "topology": topology}, expected))

        for interaction in INTERACTIONS:
            expected = ["same_semantic_choices_available", "commit_requires_explicit_authorization", "preview_is_not_character_truth"]
            if interaction == "keyboard":
                expected += ["all_actions_keyboard_reachable", "focus_preserved_after_preview"]
            if interaction == "screen_reader":
                expected += ["structured_nonvisual_summary", "deterministic_change_announcements"]
            if interaction == "high_zoom":
                expected += ["mandatory_controls_not_clipped", "preview_yields_before_control_loss"]
            if interaction == "reduced_motion":
                expected += ["no_state_requires_animation"]
            cases.append(make_case(p, "interaction_accessibility", {"mode": interaction}, expected))

        for event in MIGRATIONS:
            expected = ["deterministic_migration_receipt", "no_character_truth_write", "no_silent_substitution"]
            if event in {"removed_option", "missing_asset_pack", "old_preset"}:
                expected.append("review_or_explicit_missing_state_when_unresolved")
            if event == "permission_projection_change":
                expected += ["permission_sensitive_derivatives_invalidated", "hidden_state_not_exported"]
            cases.append(make_case(p, "migration", {"event": event}, expected))

        for recipe in RANDOMIZATION:
            expected = ["source_owned_biology_unchanged", "equipment_ownership_unchanged", "deterministic_seed_behavior"]
            if recipe == "unlocked_only":
                expected.append("locked_choices_preserved")
            if recipe == "locked_incompatible_review":
                expected += ["locked_value_preserved_for_review", "no_silent_replacement"]
            cases.append(make_case(p, "randomization", {"recipe": recipe}, expected))

        cases.append(make_case(
            p,
            "profile_transition",
            {"appearance_state_model": appearance_model, "has_special_profile_behavior": profile_behavior is not None},
            ["upstream_form_or_biology_authority_preserved", "appearance_cannot_trigger_mechanical_transition", "renderer_gap_does_not_invalidate_profile"],
        ))

        cases.append(make_case(
            p,
            "permission_projection",
            {"projection": "public_only"},
            ["hidden_semantic_fields_removed_before_render", "hidden_assets_removed_before_selection", "accessible_summary_filtered", "export_filtered"],
        ))

        if special or profile_behavior:
            cases.append(make_case(
                p,
                "special_profile_rules",
                {"special_customizer_behavior": special, "studio_profile_behavior": profile_behavior},
                ["special_rules_preserved", "no_generic_humanoid_override", "no_mechanics_granted_by_appearance"],
            ))

    cases.sort(key=lambda c: c["case_id"])
    categories: dict[str, int] = {}
    for c in cases:
        categories[c["category"]] = categories.get(c["category"], 0) + 1

    output = {
        "schema_version": SCHEMA_VERSION,
        "work_item_id": "CAPP-11",
        "provenance_class": "synthetic_noncanonical",
        "profile_count": len(profiles),
        "case_count": len(cases),
        "category_counts": dict(sorted(categories.items())),
        "generation_dimensions": {
            "views": VIEWS,
            "renderer_support_states": SUPPORT,
            "interaction_modes": INTERACTIONS,
            "migration_events": MIGRATIONS,
            "fit_states": FIT_STATES,
            "randomization_recipes": RANDOMIZATION,
        },
        "cases": cases,
        "corpus_sha256": hashlib.sha256(canonical(cases)).hexdigest(),
    }
    return output


def self_test() -> None:
    profiles = [{"profile_id": f"species.synthetic_{i}", "baseline_topology": "unknown", "appearance_state_model": "single_profile", "special_customizer_behavior": [], "studio_profile_behavior": None} for i in range(25)]
    index = {"profiles": profiles}
    one = generate(index)
    two = generate(index)
    assert one == two
    assert one["profile_count"] == 25
    assert one["case_count"] >= 800
    assert len({c["case_id"] for c in one["cases"]}) == one["case_count"]
    assert all(c["provenance_class"] == "synthetic_noncanonical" for c in one["cases"])


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--profile-index", type=Path)
    parser.add_argument("--output", type=Path)
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args()
    if args.self_test:
        self_test()
        print("CAPP-11 self-test: PASS")
        return 0
    if not args.profile_index:
        parser.error("--profile-index is required unless --self-test is used")
    profile_index = json.loads(args.profile_index.read_text(encoding="utf-8"))
    result = generate(profile_index)
    text = json.dumps(result, ensure_ascii=False, sort_keys=True, indent=2) + "\n"
    if args.output:
        args.output.write_text(text, encoding="utf-8")
    else:
        print(text, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
