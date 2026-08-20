#!/usr/bin/env python3
"""Deterministically materialize the ICF-03 mundane crop/staple library.

The compact source is canonical for ICF-03 authoring. This materializer emits
full ICF-02 definition-shaped records and four reviewable packs. It deliberately
owns no live Asset state, current market price/scarcity, magical effects, creature
biology, or world-specific production yields.
"""
from __future__ import annotations

import argparse
import json
import re
from collections import Counter
from pathlib import Path
from typing import Any

HERE = Path(__file__).resolve().parent
SOURCE = HERE / "ICF-03_LIBRARY_SOURCE.json"
AUTHORING_REF = "governance:ICF-03-governed-first-party-crop-library@1.0.0"
ID_RE = re.compile(r"^ingredient:[a-z0-9]+(?:-[a-z0-9]+)*$")
TAG_RE = re.compile(r"^[a-z0-9][a-z0-9:._/-]*$")

PACKS = {
    "ICF-03_CROP_LIBRARY_A_GRAINS_AND_LEGUMES.json": ["grain", "pseudograin", "legume"],
    "ICF-03_CROP_LIBRARY_B_VEGETABLES_AND_ROOTS.json": ["leafy", "allium_brassica", "fruiting_vegetable", "root_tuber"],
    "ICF-03_CROP_LIBRARY_C_FRUITS.json": ["temperate_fruit", "citrus", "tropical_fruit"],
    "ICF-03_CROP_LIBRARY_D_NUTS_SEEDS_INDUSTRIAL.json": ["nut_seed", "industrial_staple"],
}


def load_source() -> dict[str, Any]:
    return json.loads(SOURCE.read_text(encoding="utf-8"))


def display_name(slug: str, source: dict[str, Any]) -> str:
    override = source.get("displayNameOverrides", {}).get(slug)
    if override:
        return override
    return " ".join(token.capitalize() for token in slug.split("-"))


def edibility(slug: str, source: dict[str, Any]) -> str:
    overrides = source["edibilityOverrides"]
    if slug in overrides["inedible"]:
        return "inedible"
    if slug in overrides["conditional"]:
        return "conditional"
    return "known-edible"


def tags_for(slug: str, category: str, source: dict[str, Any]) -> list[str]:
    tags = ["icf-03", "mundane", "crop", f"crop-class:{category.replace('_', '-')}"]
    tags.extend(source["categoryDefaults"][category]["useTags"])
    if slug in source["useOverlays"]["oil"]:
        tags.append("use:oil")
    if slug in source["useOverlays"]["sugar"]:
        tags.append("use:sugar")
    if slug in source.get("sourceBacked", {}):
        tags.append("source-backed")
    return sorted(set(tags))


def base_record(slug: str, category: str, source: dict[str, Any]) -> dict[str, Any]:
    cfg = source["categoryDefaults"][category]
    record: dict[str, Any] = {
        "schemaVersion": "1.0.0",
        "stableId": f"ingredient:{slug}",
        "definitionVersion": "1.0.0",
        "recordKind": "primary-ingredient",
        "displayName": display_name(slug, source),
        "aliases": [],
        "lifecycle": {"status": "active"},
        "authorship": {
            "class": "governed-first-party",
            "authoringRecordRefs": [AUTHORING_REF],
        },
        "provenance": {
            "provenanceId": f"prov:icf03:{slug}",
            "sourceAssertions": [],
        },
        "taxonomy": {
            "ingredientClasses": ["class:plant"],
            "natureClasses": ["nature:mundane", "nature:botanical"],
            "originContextClasses": ["origin:unknown"],
            "rarity": {
                "defaultBand": "common",
                "reconciliation": {
                    "status": "first-party-authored",
                    "sourceAssertionRefs": [],
                    "authorityRef": AUTHORING_REF,
                    "rationale": "Generic mundane-baseline scarcity only; settings/scopes may override and MIB-13 owns market scarcity.",
                },
                "scopedOverrides": [],
            },
            "availability": {
                "baseline": cfg["availability"],
                "acquisitionModes": ["acquisition:cultivated"],
                "scopeAssertions": [],
            },
        },
        "units": {
            "primaryUnit": {"unitId": "unit:kilogram", "dimension": "mass"},
            "allowedUnits": ["unit:kilogram", "unit:gram"],
            "exactConversions": [
                {
                    "conversionId": f"conversion:{slug}:kilogram-to-gram",
                    "fromUnitId": "unit:kilogram",
                    "toUnitId": "unit:gram",
                    "numerator": 1000,
                    "denominator": 1,
                    "ruleKind": "global-exact",
                    "sourceAssertionRefs": [],
                }
            ],
            "sourceUnitAssertions": [],
        },
        "profiles": {
            "physical": {
                "forms": [cfg["physicalForm"]],
                "perishability": cfg["perishability"],
                "storageRequirementRefs": ["storage:mundane-dry-or-cool-as-appropriate"],
            },
            "ecology": {"renewability": "renewable", "sourceAssertionRefs": []},
            "agriculture": {
                "cultivationEligible": True,
                "husbandryEligible": False,
                "foragingEligible": False,
                "facilityTagRefs": ["facility-tag:crop-field"],
                "sourceAssertionRefs": [],
            },
            "economic": {
                "currentPriceAuthority": "MIB-13",
                "marketScarcityAuthority": "MIB-13",
                "tradeClassRefs": ["trade-class:agricultural-commodity"],
                "sourceValueAssertions": [],
            },
            "culinary": {
                "edibility": edibility(slug, source),
                "flavorPropertyRefs": cfg["flavorRefs"],
                "sourceAssertionRefs": [],
            },
        },
        "qualityConditionModel": {
            "liveStateAuthority": "D17 Asset Instance",
            "qualityRuleRefs": [],
            "conditionRuleRefs": [],
            "definitionMaySetCurrentInstanceState": False,
        },
        "substitutions": [],
        "coverage": {"status": "complete", "gaps": []},
        "tags": tags_for(slug, category, source),
    }
    return record


def apply_source_backing(record: dict[str, Any], source: dict[str, Any]) -> None:
    slug = record["stableId"].split(":", 1)[1]
    backing = source.get("sourceBacked", {}).get(slug)
    if not backing:
        return
    source_id = backing["sourceId"]
    assertions = []
    for assertion in backing["sourceAssertions"]:
        item = dict(assertion)
        item["sourceId"] = source_id
        assertions.append(item)
    record["authorship"] = {
        "class": backing["authorshipClass"],
        "authoringRecordRefs": [f"source:{source_id}", AUTHORING_REF],
    }
    record["provenance"] = {
        "provenanceId": f"prov:icf03:{slug}",
        "sourceAssertions": assertions,
    }
    record["units"]["sourceUnitAssertions"] = ["assertion:wheat-agriculture-unit"]
    record["profiles"]["agriculture"]["sourceAssertionRefs"] = ["assertion:wheat-agriculture-rules"]
    record["profiles"]["economic"]["sourceValueAssertions"] = [backing["sourceValue"]]
    record["coverage"] = {"status": "partial", "gaps": [backing["coverageGap"]]}


def materialize(source: dict[str, Any]) -> list[dict[str, Any]]:
    records: list[dict[str, Any]] = []
    for category, slugs in source["categories"].items():
        for slug in slugs:
            record = base_record(slug, category, source)
            apply_source_backing(record, source)
            records.append(record)
    return records


def validate(records: list[dict[str, Any]], source: dict[str, Any]) -> dict[str, Any]:
    errors: list[str] = []
    ids = [r["stableId"] for r in records]
    if len(records) != 176:
        errors.append(f"expected 176 records, found {len(records)}")
    if len(ids) != len(set(ids)):
        errors.append("stable IDs are not unique")
    for record in records:
        sid = record["stableId"]
        if not ID_RE.fullmatch(sid):
            errors.append(f"invalid stable ID: {sid}")
        if record["recordKind"] != "primary-ingredient":
            errors.append(f"non-primary record in ICF-03: {sid}")
        if "lineage" in record:
            errors.append(f"primary ingredient has lineage: {sid}")
        if record["qualityConditionModel"]["liveStateAuthority"] != "D17 Asset Instance":
            errors.append(f"wrong live-state authority: {sid}")
        if record["qualityConditionModel"]["definitionMaySetCurrentInstanceState"] is not False:
            errors.append(f"definition can set live state: {sid}")
        econ = record["profiles"]["economic"]
        if econ["currentPriceAuthority"] != "MIB-13" or econ["marketScarcityAuthority"] != "MIB-13":
            errors.append(f"wrong economy authority: {sid}")
        if "magicalCulinary" in record["profiles"] or "creatureSource" in record["profiles"] or "alchemical" in record["profiles"]:
            errors.append(f"out-of-tranche profile claim: {sid}")
        if not record["profiles"]["agriculture"]["cultivationEligible"]:
            errors.append(f"crop not cultivation eligible: {sid}")
        for tag in record["tags"]:
            if not TAG_RE.fullmatch(tag):
                errors.append(f"invalid tag {tag} on {sid}")
        forbidden = {"currentPrice", "marketPrice", "owner", "quantity", "currentQuality", "currentCondition"}
        if forbidden.intersection(record):
            errors.append(f"live/economy field leaked into definition: {sid}")

    wheat = next((r for r in records if r["stableId"] == "ingredient:wheat"), None)
    if not wheat:
        errors.append("source-backed Wheat record missing")
    else:
        if wheat["authorship"]["class"] != "hybrid":
            errors.append("Wheat must be hybrid-authored")
        if len(wheat["provenance"]["sourceAssertions"]) != 5:
            errors.append("Wheat must preserve five Agriculture assertions")
        values = wheat["profiles"]["economic"]["sourceValueAssertions"]
        if len(values) != 1 or values[0]["currencyTerm"] != "CR":
            errors.append("Wheat legacy CR value assertion missing")
        if wheat["coverage"]["status"] != "partial":
            errors.append("Wheat source-unit conversion gap must remain explicit")

    authorship = Counter(r["authorship"]["class"] for r in records)
    if authorship != Counter({"governed-first-party": 175, "hybrid": 1}):
        errors.append(f"unexpected authorship counts: {dict(authorship)}")

    return {
        "status": "FAIL" if errors else "PASS",
        "recordCount": len(records),
        "authorshipCounts": dict(authorship),
        "errors": errors,
    }


def pack_records(records: list[dict[str, Any]], source: dict[str, Any]) -> dict[str, dict[str, Any]]:
    category_for = {}
    for category, slugs in source["categories"].items():
        for slug in slugs:
            category_for[f"ingredient:{slug}"] = category
    result: dict[str, dict[str, Any]] = {}
    for filename, categories in PACKS.items():
        selected = [r for r in records if category_for[r["stableId"]] in categories]
        result[filename] = {
            "schemaVersion": "1.0.0",
            "workItem": "ICF-03",
            "packId": filename[:-5].lower().replace("_", "-"),
            "definitionSchema": "ICF-02_CANONICAL_INGREDIENT_SCHEMA.json",
            "authorshipRecord": AUTHORING_REF,
            "recordCount": len(selected),
            "categories": categories,
            "records": selected,
        }
    return result


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output-dir", help="Write the four expanded pack JSON files here.")
    parser.add_argument("--validate-only", action="store_true")
    args = parser.parse_args()

    source = load_source()
    records = materialize(source)
    result = validate(records, source)
    print(json.dumps(result, indent=2, sort_keys=True))
    if result["status"] != "PASS":
        return 1

    if args.output_dir and not args.validate_only:
        out = Path(args.output_dir)
        out.mkdir(parents=True, exist_ok=True)
        for filename, payload in pack_records(records, source).items():
            (out / filename).write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
