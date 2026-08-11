#!/usr/bin/env python3
from __future__ import annotations

import csv
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / "governance/application-planning/parallel-preimplementation"
INVENTORY = BASE / "PPIA-03_SOURCE_AND_DESIGN_INVENTORY.md"
TAXONOMY = BASE / "PPIA-03_ITEM_EXPERIENCE_TAXONOMY_v0.1.0.json"
R1_SOURCE = BASE / "PPIA-03_R1_DEFERRED_ITEM_CANDIDATES.csv"
R1_ROUTING = BASE / "PPIA-03_R1_DEFERRED_ITEM_ROUTING_v0.1.0.json"


def fail(msg: str) -> None:
    raise SystemExit(f"PPIA-03 FOUNDATION: FAIL — {msg}")


def require(cond: bool, msg: str) -> None:
    if not cond:
        fail(msg)


def main() -> None:
    for p in (INVENTORY, TAXONOMY, R1_SOURCE, R1_ROUTING):
        require(p.exists(), f"missing {p.relative_to(ROOT)}")

    inv = INVENTORY.read_text(encoding="utf-8")
    required_inventory_phrases = [
        "13 dedicated PDFs / 218 pages",
        "nine direct Item-domain datasets totaling 5,389 governed rows",
        "Taser",
        "Seven source-unspecified energy-weapon capacity fields",
        "Energy Sniper Rifle",
        "Plasma Carbine",
        "Cryo Blaster",
        "53 Item-classified structural candidates",
        "not 53 missing Item Definitions",
        "obsolete 487-object semantic database is compatibility debt only",
        "MV-IA-F008",
        "PPIA-04",
        "PPIA-05",
        "PPIA-11",
    ]
    for phrase in required_inventory_phrases:
        require(phrase in inv, f"inventory missing required boundary phrase: {phrase!r}")

    taxonomy = json.loads(TAXONOMY.read_text(encoding="utf-8"))
    require(taxonomy.get("format") == "multiversal-ppia03-item-experience-taxonomy", "wrong taxonomy format")
    authority = taxonomy.get("authority", {})
    require(authority.get("direct_item_csv_datasets") == 9, "direct item dataset count must be 9")
    require(authority.get("direct_item_csv_rows") == 5389, "direct item row count must be 5389")
    require(authority.get("retained_item_pdfs") == 13, "retained item PDF count must be 13")
    require(authority.get("retained_item_pdf_pages") == 218, "retained item PDF page count must be 218")
    require(authority.get("obsolete_semantic_database_is_content_authority") is False, "obsolete semantic DB must not be content authority")
    require(authority.get("r1_structural_candidates_are_canonical_items") is False, "R1 structural candidates must not be canonical items")

    layers = taxonomy.get("identity_layers", [])
    layer_ids = [x.get("id") for x in layers]
    expected_layer_ids = [
        "definition",
        "definition-variant",
        "asset-instance",
        "authority-relations",
        "location-containment",
        "equipment-assignment",
        "quantity-representation",
        "runtime-state",
        "knowledge-state",
        "transaction-history",
    ]
    require(layer_ids == expected_layer_ids, "identity/state layers changed or are incomplete")

    guardrails = taxonomy.get("source_guardrails", {})
    require(guardrails.get("source_unspecified_energy_capacity", {}).get("record_count") == 7, "must preserve seven source-unspecified capacities")
    ammo = guardrails.get("ammo_reference_only_names", {})
    require(ammo.get("record_count") == 3, "must preserve three ammo-reference-only names")
    require(ammo.get("names") == ["Energy Sniper Rifle", "Plasma Carbine", "Cryo Blaster"], "ammo-reference-only names changed")
    require("auto-merge" in guardrails.get("taser", {}).get("rule", "").lower(), "Taser rule must forbid auto-merge")

    mutation = " ".join(taxonomy.get("mutation_invariants", [])).lower()
    require("equip/unequip never silently transfers ownership" in mutation, "equipment/ownership boundary missing")
    require("lineage" in mutation, "lineage preservation boundary missing")
    require("offline authoritative inventory mutation is prohibited" in mutation, "offline mutation boundary missing")

    with R1_SOURCE.open(encoding="utf-8", newline="") as f:
        source_rows = list(csv.DictReader(f))
    require(len(source_rows) == 53, f"expected 53 R1 Item-classified candidates, got {len(source_rows)}")
    source_ids = [r["structural_candidate_id"] for r in source_rows]
    require(len(source_ids) == len(set(source_ids)), "duplicate R1 candidate IDs in source reference")

    routing = json.loads(R1_ROUTING.read_text(encoding="utf-8"))
    require(routing.get("format") == "multiversal-ppia03-r1-deferred-item-routing", "wrong R1 routing format")
    require(routing.get("source_candidate_count") == 53, "R1 routing candidate count must be 53")
    expected_counts = {
        "ppia03_supporting_rule_or_catalog_heading": 23,
        "ppia03_specific_item_or_loot_candidate": 4,
        "ppia04_vehicle_system_context": 10,
        "creature_or_body_action_context": 6,
        "context_required_before_domain_assignment": 6,
        "non_item_world_or_gm_context": 4,
    }
    groups = routing.get("groups", [])
    require(len(groups) == 6, "R1 routing must contain six disposition groups")
    counts = {g.get("classification"): g.get("count") for g in groups}
    require(counts == expected_counts, "R1 routing class counts changed")
    require(all(g.get("canonical_item_definition") is False for g in groups), "no R1 group may promote candidates")
    routing_ids = [cid for g in groups for cid in g.get("candidate_ids", [])]
    require(len(routing_ids) == 53, "R1 routing must account for exactly 53 candidates")
    require(len(routing_ids) == len(set(routing_ids)), "R1 routing contains duplicate candidate IDs")
    require(set(routing_ids) == set(source_ids), "R1 routing candidate set must match the source reference exactly")
    require(sum(expected_counts.values()) == 53, "R1 routing class counts must sum to 53")

    print("PPIA-03 FOUNDATION: PASS")
    print("retained_item_pdfs=13")
    print("retained_item_pdf_pages=218")
    print("direct_item_csv_datasets=9")
    print("direct_item_csv_rows=5389")
    print("r1_candidates=53")
    print("identity_layers=10")


if __name__ == "__main__":
    main()
