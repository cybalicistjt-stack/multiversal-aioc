#!/usr/bin/env python3
"""Validate PPIA-01 recommendation overlays against immutable CSV source facts."""
from __future__ import annotations

import argparse
import csv
import io
import json
import zipfile
from pathlib import Path

OVERLAY = "governance/application-planning/parallel-preimplementation/PPIA-01_CONTENT_REPAIR_OVERLAY_v0.1.0.json"
DATASET = "species_elementalist_and_innate_abilities_catalog.csv"


def clean(value):
    return (value or "").strip()


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", default=".")
    args = parser.parse_args()
    root = Path(args.root)
    overlay = json.loads((root / OVERLAY).read_text(encoding="utf-8"))
    delegation = json.loads((root / overlay["authority"]).read_text(encoding="utf-8"))
    if delegation.get("status") != "approved-and-active":
        raise SystemExit("owner recommendation delegation is not active")
    if overlay["status"] != "governed_recommendation_overlay_not_source_rewrite":
        raise SystemExit("overlay status does not preserve the source/recommendation boundary")
    if overlay["policy"].get("recommendations_are_source_facts") is not False:
        raise SystemExit("overlay incorrectly marks recommendations as source facts")
    if overlay["policy"].get("preserve_raw_source") is not True:
        raise SystemExit("overlay does not preserve raw source")
    if overlay["policy"].get("automatic_identity_merge") is not False:
        raise SystemExit("overlay enables automatic identity merge")

    with zipfile.ZipFile(root / "Csv.zip") as zf:
        members = {Path(name).name: name for name in zf.namelist() if name.lower().endswith(".csv")}
        with zf.open(members[DATASET]) as source:
            rows = list(csv.DictReader(io.StringIO(source.read().decode("utf-8-sig"))))

    validated = 0
    seen_targets = set()
    for batch in overlay["batches"]:
        if batch["dataset"] != DATASET:
            raise SystemExit(f"unsupported validation dataset in v0.1.0: {batch['dataset']}")
        if batch["branch"] != "Combat Forms" or batch["source_page"] != "16":
            raise SystemExit("v0.1.0 batch is not the governed Combat Forms page-16 repair batch")
        for repair in batch["repairs"]:
            target = repair["target"]
            source_row = target["source_row"]
            if source_row in seen_targets:
                raise SystemExit(f"duplicate overlay target source row {source_row}")
            seen_targets.add(source_row)
            if source_row < 2 or source_row > len(rows) + 1:
                raise SystemExit(f"invalid source row {source_row}")
            row = rows[source_row - 2]
            exact = {
                "record_id": clean(row.get("Record_ID")),
                "name": clean(row.get("Ability_Name")),
                "tier": clean(row.get("Tier")),
                "xp_cost": clean(row.get("Ability_XP_Cost")),
            }
            if target != {"source_row": source_row, **exact}:
                raise SystemExit(f"source-fact mismatch at row {source_row}: target={target}, source={exact}")
            if clean(row.get("Parent_Tree")) != "Shapeshifter Archetype":
                raise SystemExit(f"row {source_row} is not in the Shapeshifter Archetype")
            if clean(row.get("Branch")) != "Combat Forms":
                raise SystemExit(f"row {source_row} is not a Combat Forms row")
            if "pricing list" not in clean(row.get("Source_Section")).casefold():
                raise SystemExit(f"row {source_row} is not a pricing-list source row")
            if clean(row.get("Source_PDF")) != "Innate Trees(3).PDF" or clean(row.get("Source_Page")) != "16":
                raise SystemExit(f"row {source_row} source citation changed")
            if clean(row.get("Effect")).casefold() != "not specified in source":
                raise SystemExit(f"row {source_row} already has source-declared effect text; overlay is invalid")

            recommendation = repair["recommendation"]
            if not clean(recommendation.get("Effect")) or not clean(recommendation.get("Mechanics")):
                raise SystemExit(f"row {source_row} recommendation is incomplete")
            if not repair.get("evidence") or len(repair["evidence"]) < 2:
                raise SystemExit(f"row {source_row} lacks evidence record")
            if not clean(repair.get("rationale")):
                raise SystemExit(f"row {source_row} lacks rationale")
            if len(repair.get("alternatives_considered") or []) < 2:
                raise SystemExit(f"row {source_row} lacks alternatives")
            if repair.get("confidence") not in {"low", "medium", "high"}:
                raise SystemExit(f"row {source_row} has invalid confidence")
            if repair.get("reversible") is not True:
                raise SystemExit(f"row {source_row} is not reversible")
            validated += 1

    if validated != 20 or seen_targets != set(range(1898, 1918)):
        raise SystemExit(f"expected exact Combat Forms rows 1898-1917; validated {validated}")

    print(json.dumps({
        "overlay": OVERLAY,
        "validatedRepairs": validated,
        "sourceRows": "1898-1917",
        "sourceFactsPreserved": True,
        "recommendationsMarkedNonSource": True,
        "ownerDelegation": "approved-and-active",
        "result": "PASS"
    }, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
