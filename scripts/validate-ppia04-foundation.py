#!/usr/bin/env python3
from __future__ import annotations

import csv
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / "governance/application-planning/parallel-preimplementation"
INVENTORY = BASE / "PPIA-04_SOURCE_AND_DESIGN_INVENTORY.md"
TAXONOMY = BASE / "PPIA-04_VEHICLE_EXPERIENCE_TAXONOMY_v0.1.0.json"
R1 = BASE / "PPIA-04_R1_DEFERRED_VEHICLE_SYSTEM_CANDIDATES.csv"


def fail(message: str) -> None:
    raise SystemExit(f"PPIA-04 FOUNDATION: FAIL — {message}")


def require(condition: bool, message: str) -> None:
    if not condition:
        fail(message)


def main() -> None:
    for path in (INVENTORY, TAXONOMY, R1):
        require(path.exists(), f"missing {path.relative_to(ROOT)}")

    inventory = INVENTORY.read_text(encoding="utf-8")
    required_inventory = [
        "24 PDFs / 608 pages",
        "5,628 rows",
        "Vehicles — 1,200 rows",
        "Mecha — 2,117 rows",
        "Spacecraft — 2,311 rows",
        "953 `Vehicle`",
        "1,080 `Original Mecha Component`",
        "960 `Original Spacecraft`",
        "10 recovered R1 structural candidates",
        "name similarity cannot create a parent link",
        "MV-IA-F014",
        "MV-IA-F013",
        "PPIA-03",
        "PPIA-05",
        "PPIA-11",
        "PPIA-12",
    ]
    for phrase in required_inventory:
        require(phrase in inventory, f"inventory missing {phrase!r}")

    pdf_rows = [line for line in inventory.splitlines() if line.startswith("| `") and ".PDF` |" in line]
    require(len(pdf_rows) == 24, f"expected 24 PDF inventory rows, got {len(pdf_rows)}")

    taxonomy = json.loads(TAXONOMY.read_text(encoding="utf-8"))
    require(taxonomy.get("format") == "multiversal-ppia04-vehicle-mecha-starship-experience-taxonomy", "wrong taxonomy format")
    authority = taxonomy.get("authority", {})
    require(authority.get("vehicle_csv_datasets") == 3, "vehicle CSV dataset count must be 3")
    require(authority.get("vehicle_csv_rows") == 5628, "vehicle CSV row count must be 5628")
    require(authority.get("retained_direct_pdfs") == 24, "retained direct PDF count must be 24")
    require(authority.get("retained_direct_pdf_pages") == 608, "retained direct PDF page count must be 608")
    require(authority.get("recovered_r1_vehicle_system_candidates") == 10, "R1 vehicle/system candidate count must be 10")
    require(authority.get("obsolete_semantic_database_is_content_authority") is False, "obsolete semantic DB cannot be PPIA-04 content authority")
    require(authority.get("r1_structural_candidates_are_canonical_vehicle_or_system_definitions") is False, "R1 headings cannot be canonical definitions")

    layers = taxonomy.get("identity_state_layers", [])
    expected_layers = [
        "vehicle-definition",
        "definition-configuration-variant",
        "component-system-definition",
        "owned-vehicle-asset-instance",
        "installed-configuration-state",
        "scene-deployment-placement",
        "live-operational-state",
        "authority-relations",
        "crew-passenger-station-state",
        "cargo-containment-carried-craft",
        "damage-condition-failure",
        "resources-power-fuel-heat",
        "movement-position-environment",
        "provenance-history-recovery",
    ]
    require([layer.get("id") for layer in layers] == expected_layers, "14-layer identity/state taxonomy changed")

    require(len(taxonomy.get("station_types", [])) == 12, "expected 12 station types")
    deferred = set(taxonomy.get("explicitly_deferred_capabilities", []))
    for value in ("continuous Newtonian flight", "full orbital mechanics", "carrier fleet command", "programmable vehicle AI"):
        require(value in deferred, f"deferred capability missing: {value}")

    guards = " ".join(taxonomy.get("source_guardrails", [])).lower()
    require("name similarity is insufficient" in guards, "component parent identity guard missing")
    require("r1" in guards and "cannot create definitions" in guards, "R1 no-promotion guard missing")
    mutations = " ".join(taxonomy.get("mutation_invariants", [])).lower()
    require("station assignment never transfers ownership" in mutations, "station/ownership boundary missing")
    require("offline authoritative vehicle mutation is prohibited" in mutations, "offline mutation boundary missing")

    with R1.open(encoding="utf-8", newline="") as handle:
        rows = list(csv.DictReader(handle))
    require(len(rows) == 10, f"expected 10 R1 rows, got {len(rows)}")
    ids = [row["structural_candidate_id"] for row in rows]
    require(len(ids) == len(set(ids)), "duplicate R1 candidate ID")
    require(all(row["ppia04_disposition"].endswith("requires_source_review") for row in rows), "every R1 candidate must remain source-review-only")

    routes = taxonomy.get("cross_domain_routes", {})
    require(routes.get("personal_items_cargo_lots_generic_asset_lineage") == "PPIA-03", "PPIA-03 handoff missing")
    require(routes.get("species_forms_host_biology") == "PPIA-05", "PPIA-05 handoff missing")
    require(routes.get("encounter_and_balance_calibration") == "PPIA-11", "PPIA-11 handoff missing")
    require(routes.get("world_specific_vehicle_extensions") == "PPIA-12", "PPIA-12 handoff missing")

    print("PPIA-04 FOUNDATION: PASS")
    print("retained_pdfs=24")
    print("retained_pdf_pages=608")
    print("vehicle_csv_datasets=3")
    print("vehicle_csv_rows=5628")
    print("r1_vehicle_system_candidates=10")
    print("identity_state_layers=14")
    print("station_types=12")


if __name__ == "__main__":
    main()
