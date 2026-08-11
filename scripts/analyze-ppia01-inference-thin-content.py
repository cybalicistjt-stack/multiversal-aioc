#!/usr/bin/env python3
"""Prioritize inference-bearing and structurally thin CSV rows for PPIA-01 review."""
from __future__ import annotations

import argparse
import csv
import io
import json
import re
import zipfile
from collections import Counter
from pathlib import Path

INFERENCE_RE = re.compile(r"\b(inferred|estimated|balanced estimate(?:s)?|assumed)\b", re.I)
SOURCE_RISK_RE = re.compile(
    r"\b(unclear|ambiguous|unknown|conflict(?:ing)?|contradict(?:s|ory|ion)?|"
    r"not specified|not stated|not provided|not found|missing|omitted|unavailable)\b",
    re.I,
)
BALANCE_RE = re.compile(r"\b(balanc(?:e|ed|ing)|estimate(?:d|s)?|assum(?:e|ed|ption))\b", re.I)
DIRECT_INFERENCE_RE = re.compile(r"\b(inferred|inference)\b", re.I)

GENERIC_MISSING_COMPLETION_MARKERS = (
    "estimated to fill missing source field",
    "estimated to fill missing field",
    "missing weight/cost inferred",
    "unspecified fields are balanced estimates",
)

METADATA_INFERENCE_FIELDS = {
    "Weight",
    "Origin",
    "Price_Basis",
    "Currency",
    "Attunement or Bonding",
    "Source Notes",
    "GM_Notes",
}

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

AFFECTED_TRANCHES = {
    "magic_arcane_and_faction_ability_trees_catalog.csv": ["PPIA-11"],
    "profession_and_crafting_ability_trees_catalog.csv": ["PPIA-11"],
    "prestige_environment_and_special_ability_trees_catalog.csv": ["PPIA-05", "PPIA-11"],
    "species_elementalist_and_innate_abilities_catalog.csv": ["PPIA-05", "PPIA-11"],
    "ability_trees_and_abilities_catalog.csv": ["PPIA-11"],
    "expanded_living_spellbooks_and_magic_charge_holders_all_genres.csv": ["PPIA-03", "PPIA-11"],
    "completed_magic_spells_catalog.csv": ["PPIA-11"],
    "expanded_hazards_and_traps_all_genres.csv": ["PPIA-08", "PPIA-11"],
    "expanded_mecha_and_components_all_genres.csv": ["PPIA-04", "PPIA-11"],
    "expanded_spacecraft_and_components_all_genres.csv": ["PPIA-04", "PPIA-11"],
    "expanded_land_sea_air_vehicles_all_genres.csv": ["PPIA-04", "PPIA-11"],
    "expanded_computers_all_genres.csv": ["PPIA-03", "PPIA-11"],
    "expanded_bases_facilities_materials_and_homesteads_all_genres.csv": ["PPIA-12", "PPIA-08", "PPIA-11"],
    "expanded_symbiotes_and_cybernetics_all_genres.csv": ["PPIA-03", "PPIA-05", "PPIA-11"],
    "expanded_eva_suits_and_modules_all_genres.csv": ["PPIA-03", "PPIA-04", "PPIA-11"],
    "expanded_magitech_items_all_genres.csv": ["PPIA-03", "PPIA-11"],
    "expanded_items_all_genres.csv": ["PPIA-03", "PPIA-11"],
    "expanded_melee_weapons_all_genres.csv": ["PPIA-03", "PPIA-11"],
    "expanded_ranged_weapons_catalog.csv": ["PPIA-03", "PPIA-11"],
    "weapons_and_ammo.csv": ["PPIA-03", "PPIA-11"],
}

COMMON_AFFECTED_SURFACES = ["STAGE-A-A2", "SD-1007", "SD-1107"]


def clean(value: str | None) -> str:
    return (value or "").strip()


def record_id(row: dict[str, str]) -> str:
    for key in ("Record_ID", "Catalog_ID", "Item_ID", "Vehicle_ID", "Spell_ID", "ID"):
        if clean(row.get(key)):
            return clean(row.get(key))
    return ""


def risk_matches(matches: list[dict[str, str]]) -> list[dict[str, str]]:
    return [item for item in matches if SOURCE_RISK_RE.search(item["value"])]


def is_generic_missing_completion(matches: list[dict[str, str]]) -> bool:
    risky = risk_matches(matches)
    if not risky:
        return False
    for item in risky:
        value = item["value"].casefold()
        if not any(marker in value for marker in GENERIC_MISSING_COMPLETION_MARKERS):
            return False
    return True


def classify_inference(dataset: str, matches: list[dict[str, str]]) -> str:
    joined = " | ".join(item["value"] for item in matches)
    fields = {item["field"] for item in matches}

    if SOURCE_RISK_RE.search(joined):
        if is_generic_missing_completion(matches):
            return "delegated_missing_field_completion"
        return "source_recovery_review"

    if DIRECT_INFERENCE_RE.search(joined):
        if dataset == "completed_magic_spells_catalog.csv":
            return "systematic_magic_completion"
        if dataset == "expanded_bases_facilities_materials_and_homesteads_all_genres.csv" and not fields.issubset(METADATA_INFERENCE_FIELDS):
            return "systematic_base_engineering_completion"
        if fields.issubset(METADATA_INFERENCE_FIELDS):
            return "delegated_metadata_inference"
        return "mechanical_interpretation_review"

    if BALANCE_RE.search(joined):
        return "delegated_balance_estimate"
    return "delegated_inference_other"


def mechanical_priority(category: str, matches: list[dict[str, str]]) -> str:
    if category == "source_recovery_review":
        return "P0-owner-eye-useful"
    if category == "mechanical_interpretation_review":
        return "P1-high" if len(matches) >= 3 else "P2-normal"
    if category in {"systematic_magic_completion", "systematic_base_engineering_completion"}:
        return "P3-systematic"
    if category in {"delegated_balance_estimate", "delegated_missing_field_completion", "delegated_metadata_inference"}:
        return "P4-deferred-or-PPIA-11"
    return "P4-other"


def classify_structural_blank(row: dict[str, str], blank_fields: list[str]) -> str:
    blank_set = set(blank_fields)
    core_stats = {"Damage", "Range", "Weight", "Cost"}
    capacity = {"Standard Capacity", "Extended Clip", "High-Capacity Mag"}
    notes = clean(row.get("Source Notes")).casefold()
    if blank_set & core_stats:
        if "ammo-only" in notes:
            return "ammo_reference_only"
        return "core_stat_gap_review"
    if blank_set & capacity:
        return "capacity_unspecified_review"
    return "optional_annotation_blank"


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
    if delegation.get("scope", {}).get("ownerReviewNotRequired") is not True:
        raise SystemExit("standing owner delegation no longer permits bounded autonomous recommendation")

    expected = {entry["name"]: entry for entry in snapshot["files"]}
    rows_out: list[dict[str, object]] = []
    structural_blanks: list[dict[str, object]] = []
    category_counts: Counter[str] = Counter()
    dataset_counts: Counter[str] = Counter()
    field_counts: Counter[str] = Counter()
    priority_counts: Counter[str] = Counter()
    tranche_counts: Counter[str] = Counter()
    structural_counts: Counter[str] = Counter()

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
                    category = classify_inference(dataset, matches)
                    priority = mechanical_priority(category, matches)
                    category_counts[category] += 1
                    dataset_counts[dataset] += 1
                    priority_counts[priority] += 1
                    for tranche in AFFECTED_TRANCHES[dataset]:
                        tranche_counts[tranche] += 1
                    rows_out.append({
                        "dataset": dataset,
                        "sourceRow": source_row,
                        "recordId": record_id(values),
                        "name": values.get(name_col, ""),
                        "sourcePdf": values.get("Source_PDF", values.get("Source PDF", "")),
                        "sourcePage": values.get("Source_Page", values.get("Source_Page_or_Block", "")),
                        "category": category,
                        "priority": priority,
                        "matchingFields": [item["field"] for item in matches],
                        "matchingText": [item["value"] for item in matches],
                        "affectedTranches": AFFECTED_TRANCHES[dataset],
                        "affectedSurfaces": COMMON_AFFECTED_SURFACES,
                    })

                blank_fields = [field for field, value in values.items() if not value]
                if blank_fields:
                    if dataset != "weapons_and_ammo.csv":
                        raise SystemExit(f"unexpected structural blanks outside weapons_and_ammo.csv at {dataset}:{source_row}")
                    blank_class = classify_structural_blank(values, blank_fields)
                    structural_counts[blank_class] += 1
                    structural_blanks.append({
                        "dataset": dataset,
                        "sourceRow": source_row,
                        "recordId": record_id(values),
                        "name": values.get(name_col, ""),
                        "blankFields": blank_fields,
                        "classification": blank_class,
                        "sourceNotes": values.get("Source Notes", ""),
                        "affectedTranches": AFFECTED_TRANCHES[dataset],
                    })

    blank_cells = sum(len(row["blankFields"]) for row in structural_blanks)
    source_recovery = [row for row in rows_out if row["category"] == "source_recovery_review"]
    mechanical = [row for row in rows_out if row["category"] == "mechanical_interpretation_review"]
    high_mechanical = [row for row in mechanical if row["priority"] == "P1-high"]
    normal_mechanical = [row for row in mechanical if row["priority"] == "P2-normal"]

    expected_categories = {
        "delegated_balance_estimate": 8554,
        "delegated_missing_field_completion": 370,
        "delegated_metadata_inference": 403,
        "systematic_magic_completion": 385,
        "systematic_base_engineering_completion": 350,
        "mechanical_interpretation_review": 531,
        "source_recovery_review": 1,
    }
    if dict(category_counts) != expected_categories:
        raise SystemExit(f"unexpected inference category counts: {dict(category_counts)}")
    if len(rows_out) != 10594:
        raise SystemExit(f"expected 10,594 inference/estimate rows; found {len(rows_out)}")
    if len(high_mechanical) != 111 or len(normal_mechanical) != 420:
        raise SystemExit(f"mechanical-priority split changed: high={len(high_mechanical)} normal={len(normal_mechanical)}")
    if len(source_recovery) != 1 or source_recovery[0]["name"] != "Quantum Weaver":
        raise SystemExit(f"source-recovery queue is no longer the single Quantum Weaver record: {source_recovery}")
    if len(structural_blanks) != 33 or blank_cells != 76:
        raise SystemExit(f"unexpected structural blank totals rows={len(structural_blanks)} cells={blank_cells}")
    expected_structural = {
        "optional_annotation_blank": 23,
        "capacity_unspecified_review": 7,
        "ammo_reference_only": 3,
    }
    if dict(structural_counts) != expected_structural:
        raise SystemExit(f"unexpected structural blank classification: {dict(structural_counts)}")

    report = {
        "format": "multiversal-ppia01-inference-thin-content-triage",
        "version": "0.2.0",
        "source": {
            "archive": "Csv.zip",
            "archiveSha256": snapshot["archiveSha256"],
            "rows": snapshot["totals"]["rows"],
            "datasets": snapshot["totals"]["csvFiles"],
        },
        "delegation": {
            "status": delegation["status"],
            "ownerReviewNotRequired": delegation["scope"]["ownerReviewNotRequired"],
            "escalationBoundary": "Escalate only for scope/owner-decision/legal-safety conflict or when unsupported facts would have to be invented.",
        },
        "summary": {
            "inferenceEstimateRows": len(rows_out),
            "delegatedBalanceEstimateRows": category_counts["delegated_balance_estimate"],
            "delegatedMissingFieldCompletionRows": category_counts["delegated_missing_field_completion"],
            "delegatedMetadataInferenceRows": category_counts["delegated_metadata_inference"],
            "systematicMagicCompletionRows": category_counts["systematic_magic_completion"],
            "systematicBaseEngineeringCompletionRows": category_counts["systematic_base_engineering_completion"],
            "mechanicalInterpretationReviewRows": len(mechanical),
            "highPriorityMechanicalReviewRows": len(high_mechanical),
            "normalPriorityMechanicalReviewRows": len(normal_mechanical),
            "sourceRecoveryReviewRows": len(source_recovery),
            "structuralBlankRows": len(structural_blanks),
            "structuralBlankCells": blank_cells,
        },
        "categoryCounts": dict(sorted(category_counts.items())),
        "priorityCounts": dict(sorted(priority_counts.items())),
        "datasetCounts": dict(sorted(dataset_counts.items())),
        "matchingFieldCounts": dict(field_counts.most_common()),
        "affectedTrancheCounts": dict(sorted(tranche_counts.items())),
        "ownerAttentionCandidates": source_recovery,
        "highPriorityMechanicalReview": high_mechanical,
        "normalPriorityMechanicalReview": normal_mechanical,
        "structuralBlankRows": structural_blanks,
        "policy": {
            "delegated_balance_estimate": "Already within standing owner delegation; retain and route numerical balance review to PPIA-11 unless another defect signal exists.",
            "delegated_missing_field_completion": "Explicit missing-field completion already labeled as inferred/estimated; not source recovery by itself.",
            "delegated_metadata_inference": "Low-impact metadata/attunement/weight inference; retain unless downstream implementation exposes a contradiction.",
            "systematic_magic_completion": "Bulk spell normalization based on source effect scale plus governed Magic rules; review as a system, not 385 isolated source failures.",
            "systematic_base_engineering_completion": "Bulk construction/hardness/crafting completion; route balance values to PPIA-11 and authoring semantics to PPIA-12/PPIA-08.",
            "mechanical_interpretation_review": "Material gameplay behavior was inferred; prioritize rows with three or more inferred fields before normal two-or-fewer-field rows.",
            "source_recovery_review": "Exact source is too thin to support the inferred mechanics; keep recommendations explicitly non-source and surface for owner eye when useful.",
            "structural_blanks": "Blank applicability is classified before repair. Ammo-only reference rows remain intentionally thin and are not promoted into invented full weapon records.",
        },
    }

    output = Path(args.output)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    csv_output = Path(args.csv_output)
    csv_output.parent.mkdir(parents=True, exist_ok=True)
    with csv_output.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.writer(handle)
        writer.writerow([
            "priority", "category", "dataset", "source_row", "record_id", "name", "source_pdf", "source_page",
            "matching_fields", "matching_text", "affected_tranches", "affected_surfaces",
        ])
        for row in rows_out:
            writer.writerow([
                row["priority"], row["category"], row["dataset"], row["sourceRow"], row["recordId"], row["name"],
                row["sourcePdf"], row["sourcePage"], " | ".join(row["matchingFields"]), " | ".join(row["matchingText"]),
                " | ".join(row["affectedTranches"]), " | ".join(row["affectedSurfaces"]),
            ])

    print(json.dumps(report["summary"], sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
