#!/usr/bin/env python3
"""Find exact-name candidates for PPIA-01 explicit gaps without treating names as identity."""
from __future__ import annotations

import argparse
import csv
import io
import json
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

DETAIL_FIELDS = (
    "Effect",
    "Mechanics",
    "Description",
    "Full_Source_Text",
    "Notes",
    "Special_Rules",
    "Completion_Notes",
)


def clean(value: str | None) -> str:
    return (value or "").strip()


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", default=".")
    parser.add_argument("--archive", default="Csv.zip")
    parser.add_argument("--baseline", required=True)
    parser.add_argument("--output")
    return parser.parse_args()


def context(dataset: str, source_row: int, row: dict[str, str]) -> dict:
    detail = {
        field: clean(row.get(field))
        for field in DETAIL_FIELDS
        if clean(row.get(field))
        and clean(row.get(field)).casefold() not in {"not specified in source", "n/a", "none"}
    }
    return {
        "dataset": dataset,
        "sourceRow": source_row,
        "recordId": clean(row.get("Record_ID"))
        or clean(row.get("Catalog_ID"))
        or clean(row.get("Item_ID"))
        or clean(row.get("Vehicle_ID"))
        or clean(row.get("Spell_ID")),
        "name": clean(row.get(NAME_COLUMNS[dataset])),
        "recordType": clean(row.get("Record_Type")),
        "tree": clean(row.get("Ability_Tree")),
        "parentTree": clean(row.get("Parent_Tree")),
        "branch": clean(row.get("Branch")),
        "tier": clean(row.get("Tier")),
        "sourcePdf": clean(row.get("Source_PDF")) or clean(row.get("Source PDF")),
        "sourcePage": clean(row.get("Source_Page")) or clean(row.get("Source_Page_or_Block")),
        "sourceSection": clean(row.get("Source_Section")) or clean(row.get("Source_Subsection")),
        "detailFields": detail,
    }


def main() -> int:
    args = parse_args()
    root = Path(args.root)
    baseline = json.loads(Path(args.baseline).read_text(encoding="utf-8"))
    gaps = baseline["highPrioritySourceGapRows"]
    if len(gaps) != 84:
        raise SystemExit(f"expected 84 high-priority gaps, found {len(gaps)}")

    rows_by_dataset: dict[str, list[dict[str, str]]] = {}
    with zipfile.ZipFile(root / args.archive) as zf:
        members = {Path(name).name: name for name in zf.namelist() if name.lower().endswith(".csv")}
        if set(members) != set(NAME_COLUMNS):
            raise SystemExit("Csv.zip dataset set does not match the governed name-column registry")
        for dataset in NAME_COLUMNS:
            with zf.open(members[dataset]) as source:
                reader = csv.DictReader(io.StringIO(source.read().decode("utf-8-sig")))
                rows_by_dataset[dataset] = list(reader)

    by_name: dict[str, list[tuple[str, int, dict[str, str]]]] = defaultdict(list)
    for dataset, rows in rows_by_dataset.items():
        name_column = NAME_COLUMNS[dataset]
        for source_row, row in enumerate(rows, start=2):
            name = clean(row.get(name_column))
            if name:
                by_name[name.casefold()].append((dataset, source_row, row))

    matrix = []
    gap_rows_with_candidates = 0
    total_candidate_occurrences = 0
    automatic_resolutions = 0

    for gap in gaps:
        candidates = []
        for dataset, source_row, row in by_name.get(gap["name"].casefold(), []):
            if dataset == gap["dataset"] and source_row == gap["sourceRow"]:
                continue
            item = context(dataset, source_row, row)
            same_dataset = dataset == gap["dataset"]
            same_pdf = bool(gap.get("sourcePdf")) and item["sourcePdf"] == gap.get("sourcePdf")
            item["relationshipToGap"] = (
                "same-dataset-same-pdf-different-context"
                if same_dataset and same_pdf
                else "same-dataset-different-source-context"
                if same_dataset
                else "cross-dataset-name-collision"
            )
            item["candidateAuthority"] = "review-only-name-match-not-identity"
            candidates.append(item)
        candidates.sort(key=lambda item: (item["dataset"], item["sourceRow"]))
        if candidates:
            gap_rows_with_candidates += 1
            total_candidate_occurrences += len(candidates)
        matrix.append(
            {
                "gap": gap,
                "exactNameCandidates": candidates,
                "automaticResolutionAuthorized": False,
                "disposition": "candidate-context-review" if candidates else "no-exact-name-candidate",
            }
        )

    report = {
        "format": "multiversal-ppia01-gap-name-candidate-analysis",
        "version": "0.1.0",
        "summary": {
            "gapRows": len(gaps),
            "gapRowsWithExactNameCandidates": gap_rows_with_candidates,
            "gapRowsWithoutExactNameCandidates": len(gaps) - gap_rows_with_candidates,
            "exactNameCandidateOccurrences": total_candidate_occurrences,
            "automaticResolutions": automatic_resolutions,
        },
        "policy": (
            "Exact name equality is a discovery signal, not canonical identity. Cross-tree, cross-branch, "
            "cross-dataset, or different-source-context matches cannot fill a gap without stronger source evidence."
        ),
        "matrix": matrix,
    }

    serialized = json.dumps(report, indent=2, sort_keys=True) + "\n"
    if args.output:
        out = Path(args.output)
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(serialized, encoding="utf-8")
    print(json.dumps(report["summary"], sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
