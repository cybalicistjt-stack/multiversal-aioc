#!/usr/bin/env python3
"""Validate PPIA-01 recommendation overlays against immutable CSV source facts."""
from __future__ import annotations

import argparse
import csv
import io
import json
import zipfile
from pathlib import Path

DATASET = "species_elementalist_and_innate_abilities_catalog.csv"
OVERLAY_SPECS = [
    {
        "path": "governance/application-planning/parallel-preimplementation/PPIA-01_CONTENT_REPAIR_OVERLAY_v0.1.0.json",
        "version": "0.1.0",
        "branch": "Combat Forms",
        "page": "16",
        "rows": set(range(1898, 1918)),
        "expected": 20,
    },
    {
        "path": "governance/application-planning/parallel-preimplementation/PPIA-01_CONTENT_REPAIR_OVERLAY_v0.2.0.json",
        "version": "0.2.0",
        "branch": "Environmental Adaptations",
        "page": "19",
        "rows": set(range(1939, 1958)),
        "expected": 19,
    },
    {
        "path": "governance/application-planning/parallel-preimplementation/PPIA-01_CONTENT_REPAIR_OVERLAY_v0.3.0.json",
        "version": "0.3.0",
        "branch": "Utility Transformations",
        "page": "22",
        "rows": set(range(1979, 1997)),
        "expected": 18,
    },
]


def clean(value):
    return (value or "").strip()


def validate_overlay(root: Path, spec: dict, rows: list[dict]) -> dict:
    overlay_path = root / spec["path"]
    overlay = json.loads(overlay_path.read_text(encoding="utf-8"))
    delegation = json.loads((root / overlay["authority"]).read_text(encoding="utf-8"))

    if delegation.get("status") != "approved-and-active":
        raise SystemExit(f"{spec['path']}: owner recommendation delegation is not active")
    if overlay.get("format") != "multiversal-ppia01-content-repair-overlay":
        raise SystemExit(f"{spec['path']}: unexpected overlay format")
    if overlay.get("version") != spec["version"]:
        raise SystemExit(f"{spec['path']}: version mismatch")
    if overlay.get("work_item") != "PPIA-01":
        raise SystemExit(f"{spec['path']}: wrong work item")
    if overlay.get("status") != "governed_recommendation_overlay_not_source_rewrite":
        raise SystemExit(f"{spec['path']}: overlay status does not preserve source/recommendation boundary")

    policy = overlay.get("policy") or {}
    if policy.get("recommendations_are_source_facts") is not False:
        raise SystemExit(f"{spec['path']}: recommendations incorrectly marked as source facts")
    if policy.get("preserve_raw_source") is not True:
        raise SystemExit(f"{spec['path']}: raw source is not preserved")
    if policy.get("automatic_identity_merge") is not False:
        raise SystemExit(f"{spec['path']}: automatic identity merge is enabled")
    if policy.get("reversible") is not True:
        raise SystemExit(f"{spec['path']}: overlay is not reversible")

    batches = overlay.get("batches") or []
    if len(batches) != 1:
        raise SystemExit(f"{spec['path']}: expected exactly one governed batch")
    batch = batches[0]
    if batch.get("dataset") != DATASET:
        raise SystemExit(f"{spec['path']}: wrong dataset")
    if batch.get("source_pdf") != "Innate Trees(3).PDF":
        raise SystemExit(f"{spec['path']}: wrong source PDF")
    if batch.get("branch") != spec["branch"] or batch.get("source_page") != spec["page"]:
        raise SystemExit(f"{spec['path']}: branch/page mismatch")

    validated = 0
    seen_targets: set[int] = set()
    for repair in batch.get("repairs") or []:
        target = repair["target"]
        source_row = target["source_row"]
        if source_row in seen_targets:
            raise SystemExit(f"{spec['path']}: duplicate target source row {source_row}")
        seen_targets.add(source_row)
        if source_row < 2 or source_row > len(rows) + 1:
            raise SystemExit(f"{spec['path']}: invalid source row {source_row}")

        row = rows[source_row - 2]
        exact = {
            "record_id": clean(row.get("Record_ID")),
            "name": clean(row.get("Ability_Name")),
            "tier": clean(row.get("Tier")),
            "xp_cost": clean(row.get("Ability_XP_Cost")),
        }
        if target != {"source_row": source_row, **exact}:
            raise SystemExit(
                f"{spec['path']}: source-fact mismatch at row {source_row}: "
                f"target={target}, source={exact}"
            )
        if clean(row.get("Parent_Tree")) != "Shapeshifter Archetype":
            raise SystemExit(f"{spec['path']}: row {source_row} is not Shapeshifter")
        if clean(row.get("Branch")) != spec["branch"]:
            raise SystemExit(f"{spec['path']}: row {source_row} branch changed")
        if "pricing list" not in clean(row.get("Source_Section")).casefold():
            raise SystemExit(f"{spec['path']}: row {source_row} is not a pricing-list row")
        if clean(row.get("Source_PDF")) != "Innate Trees(3).PDF":
            raise SystemExit(f"{spec['path']}: row {source_row} source PDF changed")
        if clean(row.get("Source_Page")) != spec["page"]:
            raise SystemExit(f"{spec['path']}: row {source_row} source page changed")
        if clean(row.get("Effect")).casefold() != "not specified in source":
            raise SystemExit(f"{spec['path']}: row {source_row} already has source effect text")

        recommendation = repair.get("recommendation") or {}
        if not clean(recommendation.get("Effect")) or not clean(recommendation.get("Mechanics")):
            raise SystemExit(f"{spec['path']}: row {source_row} recommendation is incomplete")
        if not repair.get("evidence") or len(repair["evidence"]) < 2:
            raise SystemExit(f"{spec['path']}: row {source_row} lacks evidence")
        if not clean(repair.get("rationale")):
            raise SystemExit(f"{spec['path']}: row {source_row} lacks rationale")
        if len(repair.get("alternatives_considered") or []) < 2:
            raise SystemExit(f"{spec['path']}: row {source_row} lacks alternatives")
        if repair.get("confidence") not in {"low", "medium", "high"}:
            raise SystemExit(f"{spec['path']}: row {source_row} has invalid confidence")
        if repair.get("reversible") is not True:
            raise SystemExit(f"{spec['path']}: row {source_row} is not reversible")
        validated += 1

    if validated != spec["expected"] or seen_targets != spec["rows"]:
        raise SystemExit(
            f"{spec['path']}: expected {spec['expected']} exact rows "
            f"{min(spec['rows'])}-{max(spec['rows'])}; validated {validated}"
        )
    return {
        "overlay": spec["path"],
        "branch": spec["branch"],
        "validatedRepairs": validated,
        "sourceRows": f"{min(spec['rows'])}-{max(spec['rows'])}",
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", default=".")
    args = parser.parse_args()
    root = Path(args.root)

    with zipfile.ZipFile(root / "Csv.zip") as zf:
        members = {Path(name).name: name for name in zf.namelist() if name.lower().endswith(".csv")}
        with zf.open(members[DATASET]) as source:
            rows = list(csv.DictReader(io.StringIO(source.read().decode("utf-8-sig"))))

    results = [validate_overlay(root, spec, rows) for spec in OVERLAY_SPECS]
    total = sum(item["validatedRepairs"] for item in results)
    all_rows = set().union(*(spec["rows"] for spec in OVERLAY_SPECS))
    if total != 57 or len(all_rows) != 57:
        raise SystemExit(f"expected 57 distinct governed repairs; validated {total}")

    print(json.dumps({
        "overlays": results,
        "validatedRepairs": total,
        "sourceFactsPreserved": True,
        "recommendationsMarkedNonSource": True,
        "automaticIdentityMerges": 0,
        "ownerDelegation": "approved-and-active",
        "result": "PASS",
    }, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
