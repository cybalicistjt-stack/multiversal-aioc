#!/usr/bin/env python3
"""Prioritize inference-bearing and structurally thin CSV rows for PPIA-01 review."""
from __future__ import annotations

import argparse
import csv
import io
import json
import re
import zipfile
from collections import Counter, defaultdict
from pathlib import Path

INFERENCE_RE = re.compile(r"\b(inferred|estimated|balanced estimate(?:s)?|assumed)\b", re.I)
SOURCE_RISK_RE = re.compile(
    r"\b(unclear|ambiguous|unknown|conflict(?:ing)?|contradict(?:s|ory|ion)?|"
    r"not specified|not stated|not provided|not found|missing|omitted|unavailable)\b",
    re.I,
)
BALANCE_RE = re.compile(r"\b(balanc(?:e|ed|ing)|estimate(?:d|s)?|assum(?:e|ed|ption))\b", re.I)
DIRECT_INFERENCE_RE = re.compile(r"\b(inferred|inference)\b", re.I)

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


def clean(value: str | None) -> str:
    return (value or "").strip()


def record_id(row: dict[str, str]) -> str:
    for key in ("Record_ID", "Catalog_ID", "Item_ID", "Vehicle_ID", "Spell_ID", "ID"):
        if clean(row.get(key)):
            return clean(row.get(key))
    return ""


def classify_inference(matches: list[dict[str, str]]) -> str:
    joined = " | ".join(item["value"] for item in matches)
    if SOURCE_RISK_RE.search(joined):
        return "source_recovery_review"
    if DIRECT_INFERENCE_RE.search(joined):
        return "source_interpretation_review"
    if BALANCE_RE.search(joined):
        return "delegated_balance_estimate"
    return "delegated_inference_other"


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", default=".")
    parser.add_argument("--archive", default="Csv.zip")
    parser.add_argument("--output", required=True)
    parser.add_argument("--csv-output", required=True)
    args = parser.parse_args()

    root = Path(args.root)
    archive = root / args.archive
    snapshot = json.loads((root / "governance/object-system/csv-intake/CSV_INTAKE_AUDIT_SNAPSHOT.json").read_text(encoding="utf-8"))
    delegation = json.loads((root / "governance/object-system/csv-intake/OWNER_RECOMMENDATION_DELEGATION.json").read_text(encoding="utf-8"))
    if delegation.get("status") != "approved-and-active":
        raise SystemExit("owner recommendation delegation is not active")

    expected = {entry["name"]: entry for entry in snapshot["files"]}
    rows_out: list[dict[str, object]] = []
    blank_rows: list[dict[str, object]] = []
    category_counts: Counter[str] = Counter()
    dataset_counts: Counter[str] = Counter()
    field_counts: Counter[str] = Counter()

    with zipfile.ZipFile(archive) as zf:
        members = {Path(name).name: name for name in zf.namelist() if name.lower().endswith(".csv")}
        if set(members) != set(expected):
            raise SystemExit("Csv.zip member set does not match governed snapshot")
        for dataset in expected:
            with zf.open(members[dataset]) as source:
                reader = csv.DictReader(io.StringIO(source.read().decode("utf-8-sig")))
                rows = list(reader)
                headers = reader.fieldnames or []
            if len(rows) != expected[dataset]["rows"] or len(headers) != expected[dataset]["columns"]:
                raise SystemExit(f"shape mismatch for {dataset}")
            name_col = NAME_COLUMNS[dataset]
            for source_row, row in enumerate(rows, start=2):
                values = {key: clean(value) for key, value in row.items()}
                matches: list[dict[str, str]] = []
                for field, value in values.items():
                    if value and INFERENCE_RE.search(value):
                        matches.append({"field": field, "value": value})
                        field_counts[field] += 1
                if matches:
                    category = classify_inference(matches)
                    category_counts[category] += 1
                    dataset_counts[dataset] += 1
                    rows_out.append({
                        "dataset": dataset,
                        "sourceRow": source_row,
                        "recordId": record_id(values),
                        "name": values.get(name_col, ""),
                        "sourcePdf": values.get("Source_PDF", values.get("Source PDF", "")),
                        "sourcePage": values.get("Source_Page", values.get("Source_Page_or_Block", "")),
                        "category": category,
                        "matchingFields": [item["field"] for item in matches],
                        "matchingText": [item["value"] for item in matches],
                    })
                blanks = [field for field, value in values.items() if not value]
                if blanks:
                    blank_rows.append({
                        "dataset": dataset,
                        "sourceRow": source_row,
                        "recordId": record_id(values),
                        "name": values.get(name_col, ""),
                        "blankFields": blanks,
                    })

    # Baseline guarantees only the weapons/ammo file has true structural blanks.
    structural_blanks = [row for row in blank_rows if row["dataset"] == "weapons_and_ammo.csv"]
    unexpected_blank_rows = [row for row in blank_rows if row["dataset"] != "weapons_and_ammo.csv"]
    if unexpected_blank_rows:
        raise SystemExit(f"unexpected structural blank rows outside weapons_and_ammo.csv: {len(unexpected_blank_rows)}")
    blank_cells = sum(len(row["blankFields"]) for row in structural_blanks)

    # Owner attention is intentionally narrow: only source-risk rows are candidates for source lookup.
    owner_attention = [row for row in rows_out if row["category"] == "source_recovery_review"]
    source_interpretation = [row for row in rows_out if row["category"] == "source_interpretation_review"]
    balance = [row for row in rows_out if row["category"] == "delegated_balance_estimate"]

    report = {
        "format": "multiversal-ppia01-inference-thin-content-triage",
        "version": "0.1.0",
        "source": {"archive": "Csv.zip", "archiveSha256": snapshot["archiveSha256"], "rows": snapshot["totals"]["rows"]},
        "delegation": {"status": delegation["status"], "ownerReviewNotRequired": delegation["scope"]["ownerReviewNotRequired"]},
        "summary": {
            "inferenceEstimateRows": len(rows_out),
            "delegatedBalanceEstimateRows": len(balance),
            "sourceInterpretationReviewRows": len(source_interpretation),
            "sourceRecoveryReviewRows": len(owner_attention),
            "structuralBlankRows": len(structural_blanks),
            "structuralBlankCells": blank_cells,
        },
        "categoryCounts": dict(sorted(category_counts.items())),
        "datasetCounts": dict(sorted(dataset_counts.items())),
        "matchingFieldCounts": dict(field_counts.most_common()),
        "ownerAttentionCandidates": owner_attention,
        "sourceInterpretationReview": source_interpretation,
        "structuralBlankRows": structural_blanks,
        "policy": {
            "delegated_balance_estimate": "Already within standing owner delegation; review later in PPIA-11 unless another defect signal exists.",
            "source_interpretation_review": "Inference without an explicit missing/conflict marker; prioritize only when downstream feature impact is high.",
            "source_recovery_review": "Inference coexists with explicit source uncertainty/absence language; best candidate for exact-source or owner lookup.",
            "structural_blanks": "Judge applicability before repair; blank weapon-only fields on ammunition/support rows may be valid.",
        },
    }
    if len(rows_out) != 10594:
        raise SystemExit(f"expected 10,594 inference/estimate rows; found {len(rows_out)}")
    if blank_cells != 76:
        raise SystemExit(f"expected 76 structural blank cells; found {blank_cells}")

    output = Path(args.output)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    csv_output = Path(args.csv_output)
    csv_output.parent.mkdir(parents=True, exist_ok=True)
    with csv_output.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.writer(handle)
        writer.writerow(["category", "dataset", "source_row", "record_id", "name", "source_pdf", "source_page", "matching_fields", "matching_text"])
        for row in rows_out:
            writer.writerow([
                row["category"], row["dataset"], row["sourceRow"], row["recordId"], row["name"], row["sourcePdf"], row["sourcePage"],
                " | ".join(row["matchingFields"]), " | ".join(row["matchingText"]),
            ])

    print(json.dumps(report["summary"], sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
