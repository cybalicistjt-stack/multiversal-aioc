#!/usr/bin/env python3
"""Validate the PPIA-01 quantitative-gap closure against immutable Csv.zip rows."""
from __future__ import annotations

import csv
import io
import json
import re
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CLOSURE = ROOT / "governance/application-planning/parallel-preimplementation/PPIA-01_QUANTITATIVE_GAP_CLOSURE_v0.1.0.json"
ARCHIVE = ROOT / "Csv.zip"
AMOUNT_RE = re.compile(
    r"\b(?:exact\s+)?(?:hp\s+)?(?:amount|value|cost|damage|healing|range|duration|dc|capacity|speed|weight|rating)\b"
    r"[^.;|]{0,80}\bnot specified\b",
    re.I,
)
HEX64 = re.compile(r"^[0-9a-f]{64}$")
BONE_CRUSHER_QUANTITY_RE = re.compile(r"two additional(?: weapon)? damage dice", re.I)
NAME_COLUMNS = {
    "expanded_symbiotes_and_cybernetics_all_genres.csv": "Item",
    "magic_arcane_and_faction_ability_trees_catalog.csv": "Ability_Name",
    "species_elementalist_and_innate_abilities_catalog.csv": "Ability_Name",
}
EXPECTED_TARGETS = {
    ("expanded_symbiotes_and_cybernetics_all_genres.csv", 55),
    ("expanded_symbiotes_and_cybernetics_all_genres.csv", 57),
    ("magic_arcane_and_faction_ability_trees_catalog.csv", 99),
    ("species_elementalist_and_innate_abilities_catalog.csv", 33),
    ("species_elementalist_and_innate_abilities_catalog.csv", 336),
    ("species_elementalist_and_innate_abilities_catalog.csv", 534),
    ("species_elementalist_and_innate_abilities_catalog.csv", 953),
    ("species_elementalist_and_innate_abilities_catalog.csv", 958),
    ("species_elementalist_and_innate_abilities_catalog.csv", 1040),
    ("species_elementalist_and_innate_abilities_catalog.csv", 1131),
    ("species_elementalist_and_innate_abilities_catalog.csv", 1387),
    ("species_elementalist_and_innate_abilities_catalog.csv", 2183),
}


def clean(value):
    return (value or "").strip()


def row_record_id(row: dict) -> str:
    return clean(
        row.get("Record_ID")
        or row.get("Catalog_ID")
        or row.get("Item_ID")
        or row.get("Vehicle_ID")
        or row.get("Spell_ID")
    )


def target_from_row(dataset: str, source_row: int, row: dict) -> dict:
    return {
        "dataset": dataset,
        "source_row": source_row,
        "record_id": row_record_id(row),
        "name": clean(row.get(NAME_COLUMNS[dataset])),
        "source_pdf": clean(row.get("Source_PDF") or row.get("Source PDF")),
        "source_page": clean(row.get("Source_Page") or row.get("Source_Page_or_Block")),
        "source_section": clean(row.get("Source_Section") or row.get("Source_Subsection")),
    }


def has_amount_gap(row: dict) -> bool:
    return any(AMOUNT_RE.search(clean(value)) for value in row.values() if clean(value))


def main() -> int:
    closure = json.loads(CLOSURE.read_text(encoding="utf-8"))
    delegation = json.loads((ROOT / closure["authority"]).read_text(encoding="utf-8"))
    if delegation.get("status") != "approved-and-active":
        raise SystemExit("owner recommendation delegation is not active")
    if closure.get("format") != "multiversal-ppia01-quantitative-gap-closure":
        raise SystemExit("unexpected closure format")
    if closure.get("version") != "0.1.0" or closure.get("work_item") != "PPIA-01":
        raise SystemExit("closure identity mismatch")
    if closure.get("status") != "governed_overlay_not_source_rewrite":
        raise SystemExit("closure does not preserve the raw-source boundary")

    policy = closure.get("policy") or {}
    required_policy = {
        "preserve_raw_csv": True,
        "source_grounded_values_are_not_recommendations": True,
        "owner_recommendations_are_source_facts": False,
        "automatic_identity_merge": False,
        "reversible": True,
    }
    for key, expected in required_policy.items():
        if policy.get(key) is not expected:
            raise SystemExit(f"invalid policy {key}: {policy.get(key)!r}")
    if policy.get("later_balance_review") != "PPIA-11":
        raise SystemExit("quantitative recommendations are not routed to PPIA-11 balance review")

    with zipfile.ZipFile(ARCHIVE) as zf:
        members = {Path(name).name: name for name in zf.namelist() if name.lower().endswith(".csv")}
        tables: dict[str, list[dict]] = {}
        for dataset in NAME_COLUMNS:
            with zf.open(members[dataset]) as source:
                tables[dataset] = list(csv.DictReader(io.StringIO(source.read().decode("utf-8-sig"))))

    seen: set[tuple[str, int]] = set()
    source_grounded = 0
    recommended = 0
    for entry in closure.get("entries") or []:
        target = entry.get("target") or {}
        dataset = target.get("dataset")
        source_row = target.get("source_row")
        key = (dataset, source_row)
        if key in seen:
            raise SystemExit(f"duplicate closure target {key}")
        seen.add(key)
        if key not in EXPECTED_TARGETS:
            raise SystemExit(f"unexpected quantitative closure target {key}")
        if dataset not in tables or not isinstance(source_row, int):
            raise SystemExit(f"invalid quantitative target {key}")
        rows = tables[dataset]
        if source_row < 2 or source_row > len(rows) + 1:
            raise SystemExit(f"source row out of range {key}")
        row = rows[source_row - 2]
        exact_target = target_from_row(dataset, source_row, row)
        if target != exact_target:
            raise SystemExit(f"source metadata mismatch at {key}: target={target}, source={exact_target}")
        if not has_amount_gap(row):
            raise SystemExit(f"{key} is no longer an amount-not-specified source row")

        evidence = entry.get("source_evidence") or {}
        if not clean(evidence.get("project_source_member")):
            raise SystemExit(f"{key} lacks project-source provenance")
        if not HEX64.fullmatch(clean(evidence.get("sha256"))):
            raise SystemExit(f"{key} has invalid source PDF SHA-256")
        if not entry.get("source_support"):
            raise SystemExit(f"{key} lacks source-support record")
        if entry.get("confidence") not in {"low", "medium", "high"}:
            raise SystemExit(f"{key} has invalid confidence")
        if entry.get("reversible") is not True:
            raise SystemExit(f"{key} is not reversible")

        kind = entry.get("resolution_kind")
        if kind == "source_grounded_quantitative_correction":
            source_grounded += 1
            resolution = clean(entry.get("quantitative_resolution"))
            if not resolution:
                raise SystemExit(f"{key} source-grounded quantity is empty")
            full_text = clean(row.get("Full_Source_Text") or row.get("Mechanics") or row.get("Effect"))
            if target.get("name") == "Bone Crusher":
                if not BONE_CRUSHER_QUANTITY_RE.search(full_text):
                    raise SystemExit("Bone Crusher no longer contains its source-grounded dice quantity")
                if not BONE_CRUSHER_QUANTITY_RE.search(resolution):
                    raise SystemExit("Bone Crusher resolution does not preserve the source quantity")
            elif target.get("name") == "Starfire Charge":
                if "50% additional damage" not in full_text.casefold():
                    raise SystemExit("Starfire Charge no longer contains its source-grounded percentage")
                if "50% additional damage" not in resolution.casefold():
                    raise SystemExit("Starfire Charge resolution does not preserve the source percentage")
            else:
                raise SystemExit(f"unexpected source-grounded quantitative row {key}")
        elif kind == "owner_delegated_quantitative_recommendation":
            recommended += 1
            recommendation = entry.get("recommendation") or {}
            if not recommendation or not any(clean(value) for value in recommendation.values()):
                raise SystemExit(f"{key} quantitative recommendation is empty")
            if not clean(entry.get("rationale")):
                raise SystemExit(f"{key} quantitative recommendation lacks rationale")
            if len(entry.get("alternatives_considered") or []) < 2:
                raise SystemExit(f"{key} quantitative recommendation lacks alternatives")
        else:
            raise SystemExit(f"{key} has unsupported resolution kind {kind!r}")

    if seen != EXPECTED_TARGETS:
        raise SystemExit(f"quantitative target set mismatch missing={sorted(EXPECTED_TARGETS-seen)} extra={sorted(seen-EXPECTED_TARGETS)}")
    if source_grounded != 2 or recommended != 10:
        raise SystemExit(f"expected 2 source-grounded and 10 recommended quantities; got {source_grounded}/{recommended}")

    expected_summary = {
        "amount_not_specified_rows": 12,
        "source_grounded_quantitative_corrections": 2,
        "owner_delegated_quantitative_recommendations": 10,
        "raw_source_rows_modified": 0,
    }
    if closure.get("summary") != expected_summary:
        raise SystemExit(f"closure summary mismatch: {closure.get('summary')}")

    print(json.dumps({
        "closure": str(CLOSURE.relative_to(ROOT)),
        "validatedRows": len(seen),
        "sourceGroundedCorrections": source_grounded,
        "ownerDelegatedRecommendations": recommended,
        "rawSourceRowsModified": 0,
        "balanceReview": "PPIA-11",
        "ownerDelegation": "approved-and-active",
        "result": "PASS",
    }, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
