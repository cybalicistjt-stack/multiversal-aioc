#!/usr/bin/env python3
"""Deterministic PPIA-01 audit of the governed CSV-first content registry."""
from __future__ import annotations

import argparse
import csv
import hashlib
import io
import json
import re
import zipfile
from collections import defaultdict
from pathlib import Path

NAME_COLUMNS = {
    "magic_arcane_and_faction_ability_trees_catalog.csv": "Ability_Name",
    "profession_and_crafting_ability_trees_catalog.csv": "Ability_Name",
    "prestige_environment_and_special_ability_trees_catalog.csv": "Ability_Name",
    "species_elementalist_and_innate_abilities_catalog.csv": "Ability_Name",
    "ability_trees_and_abilities_catalog.csv": "Ability_Name",
    "expanded_living_spellbooks_and_magic_charge_holders_all_genres.csv": "Item_Name",
    "completed_magic_spells_catalog.csv": "Spell_Name",
    "expanded_hazards_and_traps_all_genres.csv": "Item_Name",
    "expanded_mecha_and_components_all_genres.csv": "Item_Name",
    "expanded_spacecraft_and_components_all_genres.csv": "Item_Name",
    "expanded_land_sea_air_vehicles_all_genres.csv": "Item_Name",
    "expanded_computers_all_genres.csv": "Item_Name",
    "expanded_bases_facilities_materials_and_homesteads_all_genres.csv": "Item",
    "expanded_symbiotes_and_cybernetics_all_genres.csv": "Item",
    "expanded_eva_suits_and_modules_all_genres.csv": "Item",
    "expanded_magitech_items_all_genres.csv": "Item",
    "expanded_items_all_genres.csv": "Item",
    "expanded_melee_weapons_all_genres.csv": "Weapon",
    "expanded_ranged_weapons_catalog.csv": "Weapon",
    "weapons_and_ammo.csv": "Weapon",
}

MISSING_STATUS_PHRASES = (
    "missing source definition",
    "source omits cost and description",
    "standalone definition and xp price are missing",
    "source omits the trees and all member entries",
    "no ability-tree content available to extract",
)
NO_EFFECT_RE = re.compile(r"source provides no effect text", re.I)
AMOUNT_RE = re.compile(
    r"\b(?:exact\s+)?(?:hp\s+)?(?:amount|value|cost|damage|healing|range|duration|dc|capacity|speed|weight|rating)\b"
    r"[^.;|]{0,80}\bnot specified\b",
    re.I,
)
INFERENCE_RE = re.compile(r"\b(?:inferred|estimated|balanced estimate|balanced estimates|assumed)\b", re.I)
SOURCE_UNSPECIFIED_RE = re.compile(r"not specified in source", re.I)


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def norm(value: str | None) -> str:
    return (value or "").strip()


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", default=".")
    parser.add_argument("--archive", default="Csv.zip")
    parser.add_argument("--output")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    root = Path(args.root)
    base = root / "governance/object-system/csv-intake"
    snapshot = json.loads((base / "CSV_INTAKE_AUDIT_SNAPSHOT.json").read_text(encoding="utf-8"))
    contract = json.loads((base / "FULL_REGISTRY_RECONCILIATION_CONTRACT.json").read_text(encoding="utf-8"))
    delegation = json.loads((base / "OWNER_RECOMMENDATION_DELEGATION.json").read_text(encoding="utf-8"))

    archive = root / args.archive
    archive_bytes = archive.read_bytes()
    actual_archive_sha = sha256_bytes(archive_bytes)
    if actual_archive_sha != snapshot["archiveSha256"]:
        raise SystemExit(
            f"archive SHA mismatch: {actual_archive_sha} != {snapshot['archiveSha256']}"
        )
    if delegation.get("status") != "approved-and-active":
        raise SystemExit("owner recommendation delegation is not active")

    expected = {entry["name"]: (entry["rows"], entry["columns"]) for entry in snapshot["files"]}
    if snapshot["totals"]["csvFiles"] != contract["expectedCsvFiles"]:
        raise SystemExit("snapshot/contract dataset count mismatch")
    if snapshot["totals"]["rows"] != contract["expectedRows"]:
        raise SystemExit("snapshot/contract row count mismatch")

    datasets = []
    high_priority = []
    total_rows = 0
    total_blank_cells = 0
    total_source_unspecified_cells = 0
    total_inference_rows = 0

    with zipfile.ZipFile(io.BytesIO(archive_bytes)) as zf:
        members = {Path(name).name: name for name in zf.namelist() if name.lower().endswith(".csv")}
        if set(members) != set(expected):
            raise SystemExit(
                "dataset set mismatch "
                f"missing={sorted(set(expected) - set(members))} "
                f"extra={sorted(set(members) - set(expected))}"
            )

        for snapshot_entry in snapshot["files"]:
            dataset = snapshot_entry["name"]
            with zf.open(members[dataset]) as source:
                text = source.read().decode("utf-8-sig")
            reader = csv.DictReader(io.StringIO(text))
            rows = list(reader)
            headers = reader.fieldnames or []
            expected_rows, expected_columns = expected[dataset]
            if len(rows) != expected_rows or len(headers) != expected_columns:
                raise SystemExit(
                    f"{dataset} shape mismatch: rows={len(rows)}/{expected_rows}, "
                    f"columns={len(headers)}/{expected_columns}"
                )

            name_column = NAME_COLUMNS[dataset]
            if name_column not in headers:
                raise SystemExit(f"{dataset} is missing governed name column {name_column}")

            names: dict[str, list[int]] = defaultdict(list)
            blank_cells = 0
            source_unspecified_cells = 0
            inference_rows = 0
            amount_rows = 0
            missing_definition_rows = 0
            no_effect_rows = 0

            for source_row, row in enumerate(rows, start=2):
                values = {key: norm(value) for key, value in row.items()}
                name = values.get(name_column, "")
                names[name.casefold()].append(source_row)
                blank_cells += sum(1 for value in values.values() if not value)
                source_unspecified_cells += sum(
                    len(SOURCE_UNSPECIFIED_RE.findall(value))
                    for value in values.values()
                    if value
                )
                if any(INFERENCE_RE.search(value) for value in values.values() if value):
                    inference_rows += 1

                amount_hit = any(AMOUNT_RE.search(value) for value in values.values() if value)
                status_text = (
                    values.get("Completion_Status", "") + " " + values.get("Completion_Notes", "")
                ).casefold()
                missing_hit = any(phrase in status_text for phrase in MISSING_STATUS_PHRASES)
                no_effect_hit = bool(NO_EFFECT_RE.search(status_text))

                if amount_hit:
                    amount_rows += 1
                if missing_hit:
                    missing_definition_rows += 1
                if no_effect_hit:
                    no_effect_rows += 1

                if amount_hit or missing_hit or no_effect_hit:
                    high_priority.append(
                        {
                            "dataset": dataset,
                            "sourceRow": source_row,
                            "recordId": values.get("Record_ID")
                            or values.get("Catalog_ID")
                            or values.get("Item_ID")
                            or values.get("Vehicle_ID")
                            or values.get("Spell_ID")
                            or "",
                            "name": name,
                            "sourcePdf": values.get("Source_PDF")
                            or values.get("Source PDF")
                            or "",
                            "sourcePage": values.get("Source_Page")
                            or values.get("Source_Page_or_Block")
                            or "",
                            "sourceSection": values.get("Source_Section")
                            or values.get("Source_Subsection")
                            or "",
                            "reasons": sorted(
                                reason
                                for reason, hit in (
                                    ("amount-not-specified", amount_hit),
                                    ("missing-definition", missing_hit),
                                    ("no-effect-text", no_effect_hit),
                                )
                                if hit
                            ),
                        }
                    )

            duplicate_name_groups = sum(
                1 for name, source_rows in names.items() if name and len(source_rows) > 1
            )
            datasets.append(
                {
                    "dataset": dataset,
                    "rows": len(rows),
                    "columns": len(headers),
                    "nameColumn": name_column,
                    "blankCells": blank_cells,
                    "sourceUnspecifiedCells": source_unspecified_cells,
                    "rowsWithInferenceOrEstimate": inference_rows,
                    "rowsWithAmountNotSpecified": amount_rows,
                    "rowsWithMissingDefinitionStatus": missing_definition_rows,
                    "rowsWithNoEffectText": no_effect_rows,
                    "duplicateNameGroups": duplicate_name_groups,
                }
            )
            total_rows += len(rows)
            total_blank_cells += blank_cells
            total_source_unspecified_cells += source_unspecified_cells
            total_inference_rows += inference_rows

    high_priority.sort(key=lambda item: (item["dataset"], item["sourceRow"]))
    report = {
        "format": "multiversal-ppia01-csv-content-quality-baseline",
        "version": "0.1.0",
        "sourceAuthority": {
            "archive": "Csv.zip",
            "archiveSha256": snapshot["archiveSha256"],
            "finalRegistryWorkstream": contract["workstream"],
            "governedRows": contract["expectedRows"],
            "ownerDelegationStatus": delegation["status"],
        },
        "summary": {
            "datasets": len(datasets),
            "rows": total_rows,
            "blankCells": total_blank_cells,
            "sourceUnspecifiedCells": total_source_unspecified_cells,
            "rowsWithInferenceOrEstimate": total_inference_rows,
            "highPrioritySourceGapRows": len(high_priority),
        },
        "classification": {
            "blankCells": "Structural blanks; may be intentional and require field-context review.",
            "sourceUnspecifiedCells": "Explicit source-absence markers; informational until the field is judged required/applicable.",
            "rowsWithInferenceOrEstimate": "Rows containing governed inferred/estimated values; not automatically defects because the active owner delegation permits bounded evidence-based recommendations.",
            "highPrioritySourceGapRows": "Rows with explicit missing-definition, no-effect-text, or amount-not-specified evidence; first source-recovery queue.",
        },
        "datasets": datasets,
        "highPrioritySourceGapRows": high_priority,
    }

    if report["summary"]["datasets"] != 20 or report["summary"]["rows"] != 19199:
        raise SystemExit("PPIA-01 baseline totals do not match the governed registry")

    serialized = json.dumps(report, indent=2, sort_keys=True) + "\n"
    if args.output:
        output = Path(args.output)
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_text(serialized, encoding="utf-8")

    print(
        json.dumps(
            {
                "archiveSha256": snapshot["archiveSha256"],
                "datasets": report["summary"]["datasets"],
                "rows": report["summary"]["rows"],
                "sourceUnspecifiedCells": report["summary"]["sourceUnspecifiedCells"],
                "rowsWithInferenceOrEstimate": report["summary"]["rowsWithInferenceOrEstimate"],
                "highPrioritySourceGapRows": report["summary"]["highPrioritySourceGapRows"],
            },
            sort_keys=True,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
