#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / "governance/application-planning/parallel-preimplementation"
TAX = BASE / "PPIA-12_WORLD_SETTING_TAXONOMY_v0.1.0.json"
MATRIX = BASE / "PPIA-12_WORLD_SETTING_INSPECTOR_PROJECTION_MATRIX_v0.1.0.json"
CASES = BASE / "PPIA-12_REFERENCE_CASES_v0.1.0.json"
INVENTORY = BASE / "PPIA-12_SOURCE_AND_DESIGN_INVENTORY.md"
ROUTING = BASE / "PPIA-12_SETTING_EXTENSION_ROUTING_v0.1.0.json"


def fail(message: str) -> None:
    raise SystemExit(f"PPIA-12 INSPECTOR/REFERENCE: FAIL — {message}")


def require(condition: bool, message: str) -> None:
    if not condition:
        fail(message)


def load(path: Path):
    require(path.exists(), f"missing {path.relative_to(ROOT)}")
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> None:
    tax = load(TAX)
    matrix = load(MATRIX)
    cases = load(CASES)
    routing = load(ROUTING)
    inventory = INVENTORY.read_text(encoding="utf-8")

    layers = [x["id"] for x in tax["identity_state_layers"]]
    groups = matrix["field_groups"]
    actions = matrix["action_contracts"]
    refs = cases["cases"]

    require(len(layers) == 14, "taxonomy must preserve 14 layers")
    require(len(groups) == 14, "Inspector matrix must have 14 projection groups")
    require(len(actions) == 16, "Inspector matrix must have 16 governed action contracts")
    require(len(refs) == 20, "reference set must contain 20 cases")

    group_layers = [g["layers"][0] for g in groups]
    require(group_layers == layers, "projection groups must align one-to-one and in order with taxonomy layers")
    require(len({g["id"] for g in groups}) == 14, "projection group IDs must be unique")
    require(len({a["id"] for a in actions}) == 16, "action IDs must be unique")
    require(len({c["case_id"] for c in refs}) == 20, "reference-case IDs must be unique")
    require([c["case_id"] for c in refs] == [f"PPIA12-RC-{i:03d}" for i in range(1, 21)], "reference-case IDs must be contiguous PPIA12-RC-001..020")

    required_actions = {
        "inspect_compare", "author_setting_definition", "author_hierarchy_relation", "attach_environment_profile",
        "author_infrastructure_landmark", "author_faction_governance", "author_culture_society_economy",
        "author_history_timeline", "scope_content_extension", "scope_local_rule_extension",
        "author_route_connectivity", "campaign_scene_handoff", "reveal_hide_setting_fact",
        "generate_authoring_proposal", "source_conflict_resolution_candidate", "history_export_recovery"
    }
    require({a["id"] for a in actions} == required_actions, "governed action contract set mismatch")

    kinds = {k: sum(1 for c in refs if c["kind"] == k) for k in ("contract_grounded", "synthetic_qa", "guardrail")}
    require(kinds == {"contract_grounded": 13, "synthetic_qa": 4, "guardrail": 3}, f"reference-kind counts mismatch: {kinds}")
    require(all(c.get("acceptance") for c in refs), "every reference case needs acceptance criteria")

    policy = cases["policy"]
    for key in (
        "setting_local_means_universal", "cooccurrence_creates_hierarchy", "environment_template_instantiates_setting",
        "authoring_proposal_is_canonical", "unknown_uses_default", "conflict_is_silently_reconciled",
        "campaign_state_mutates_definition", "hidden_facts_are_counted_before_filtering", "synthetic_qa_records_are_canonical"
    ):
        require(policy[key] is False, f"guardrail policy must be false: {key}")

    summary = tax["source_summary"]
    require(summary["primary_setting_cosmology_location_pdfs"] == 22 and summary["primary_pages"] == 693, "primary source count/pages changed")
    require(summary["environment_template_pdfs"] == 8 and summary["environment_template_pages"] == 238, "environment source count/pages changed")
    require(summary["authoring_guidance_pdfs"] == 2 and summary["authoring_guidance_pages"] == 30, "authoring source count/pages changed")
    require(summary["total_pdfs"] == 32 and summary["total_pages"] == 961, "total source count/pages changed")
    require(summary["dedicated_world_setting_csv_catalog_present"] is False, "dedicated World/Setting CSV catalog must remain absent")

    for value in (
        "Havalaea.PDF", "Vertigon.PDF", "Black Vegas.PDF", "The Antiquaria.PDF", "The Rakuuta Road.PDF",
        "Musical Reality Gameplay.PDF", "New Branches Info.PDF", "Stratebrait.PDF", "Worldbuilding.PDF",
        "World Creation tables.PDF", "32 retained PDFs / 961 pages"
    ):
        require(value in inventory, f"source inventory missing anchor {value!r}")

    principles = " ".join(matrix["principles"]).lower()
    for fragment in (
        "authorize", "campaign/scene", "typed hierarchy", "co-occurrence", "environment templates",
        "world-local", "proposals", "unknown", "conflicted", "nonvisual"
    ):
        require(fragment in principles, f"Inspector principles missing {fragment!r}")

    routing_text = json.dumps(routing).lower()
    for fragment in ("ppia-08", "ppia-02", "ppia-03", "ppia-04", "ppia-05", "ppia-11"):
        require(fragment in routing_text, f"setting-extension routing lost {fragment}")

    case_text = json.dumps(cases)
    for value in (
        "Havalaea → Vertigon", "spaceborne city-station", "semi-transdimensional generation-ship",
        "pathways connecting realities", "certain musical realities", "branch-specific gameplay mechanics",
        "older/current/new material", "operation ID/status before retry", "map geometry"
    ):
        require(value in case_text, f"reference cases missing governed anchor {value!r}")

    role_text = json.dumps(matrix["role_projection"]).lower()
    require("hidden" in role_text and "canonical" in role_text and "campaign" in role_text, "role projection missing privacy/authority boundaries")
    access = matrix["responsive_accessibility"]
    for key in ("keyboard", "screen_reader", "high_zoom_reflow", "reduced_motion", "nonvisual_navigation"):
        require(key in access and access[key], f"accessibility profile missing {key}")

    mutation_actions = [a for a in actions if a["mutates"]]
    require(len(mutation_actions) == 12, f"expected 12 mutating action contracts, got {len(mutation_actions)}")
    mut_text = json.dumps(mutation_actions).lower()
    require("expected version" in mut_text and "idempotency" in mut_text, "mutation contracts must preserve version/idempotency controls")

    print("PPIA-12 INSPECTOR/REFERENCE: PASS")
    print("projection_groups=14")
    print("action_contracts=16")
    print("mutating_action_contracts=12")
    print("reference_cases=20")
    print("contract_grounded=13")
    print("synthetic_qa=4")
    print("guardrail=3")
    print("source_pdfs=32")
    print("source_pages=961")


if __name__ == "__main__":
    main()
