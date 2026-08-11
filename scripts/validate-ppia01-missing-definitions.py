#!/usr/bin/env python3
"""Validate the PPIA-01 missing-definition closure against the governed CSV source."""
from __future__ import annotations

import csv
import io
import json
import re
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CLOSURE = ROOT / "governance/application-planning/parallel-preimplementation/PPIA-01_MISSING_DEFINITION_CLOSURE_v0.1.0.json"
ARCHIVE = ROOT / "Csv.zip"
MISSING_STATUS_PHRASES = (
    "missing source definition",
    "source omits cost and description",
    "standalone definition and xp price are missing",
    "source omits the trees and all member entries",
    "no ability-tree content available to extract",
)
NAME_COLUMNS = {
    "magic_arcane_and_faction_ability_trees_catalog.csv": "Ability_Name",
    "prestige_environment_and_special_ability_trees_catalog.csv": "Ability_Name",
    "profession_and_crafting_ability_trees_catalog.csv": "Ability_Name",
}
HEX64 = re.compile(r"^[0-9a-f]{64}$")


def clean(value):
    return (value or "").strip()


def row_record_id(row: dict) -> str:
    return clean(row.get("Record_ID") or row.get("Catalog_ID") or row.get("Item_ID"))


def main() -> int:
    closure = json.loads(CLOSURE.read_text(encoding="utf-8"))
    delegation = json.loads((ROOT / closure["authority"]).read_text(encoding="utf-8"))

    if delegation.get("status") != "approved-and-active":
        raise SystemExit("owner recommendation delegation is not active")
    if closure.get("format") != "multiversal-ppia01-missing-definition-closure":
        raise SystemExit("unexpected closure format")
    if closure.get("version") != "0.1.0" or closure.get("work_item") != "PPIA-01":
        raise SystemExit("closure identity mismatch")
    if closure.get("status") != "governed_overlay_not_source_rewrite":
        raise SystemExit("closure does not preserve source/recommendation boundary")

    policy = closure.get("policy") or {}
    required_policy = {
        "preserve_raw_csv": True,
        "source_grounded_definitions_are_paraphrases_not_quotes": True,
        "owner_recommendations_are_source_facts": False,
        "automatic_identity_merge": False,
        "reversible": True,
    }
    for key, expected in required_policy.items():
        if policy.get(key) is not expected:
            raise SystemExit(f"invalid policy {key}: {policy.get(key)!r}")

    with zipfile.ZipFile(ARCHIVE) as zf:
        members = {Path(name).name: name for name in zf.namelist() if name.lower().endswith(".csv")}
        tables = {}
        for dataset in NAME_COLUMNS:
            with zf.open(members[dataset]) as source:
                tables[dataset] = list(csv.DictReader(io.StringIO(source.read().decode("utf-8-sig"))))

    seen = set()
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
        if dataset not in tables:
            raise SystemExit(f"unsupported closure dataset {dataset}")
        rows = tables[dataset]
        if not isinstance(source_row, int) or source_row < 2 or source_row > len(rows) + 1:
            raise SystemExit(f"invalid source row {key}")
        row = rows[source_row - 2]

        expected = {
            "dataset": dataset,
            "source_row": source_row,
            "record_id": row_record_id(row),
            "name": clean(row.get(NAME_COLUMNS[dataset])),
            "source_pdf": clean(row.get("Source_PDF") or row.get("Source PDF")),
            "source_page": clean(row.get("Source_Page") or row.get("Source_Page_or_Block")),
            "source_section": clean(row.get("Source_Section") or row.get("Source_Subsection")),
        }
        if target != expected:
            raise SystemExit(f"source metadata mismatch at {key}: target={target}, source={expected}")

        status_text = (
            clean(row.get("Completion_Status")) + " " + clean(row.get("Completion_Notes"))
        ).casefold()
        if not any(phrase in status_text for phrase in MISSING_STATUS_PHRASES):
            raise SystemExit(f"{key} is no longer a governed missing-definition row")

        evidence = entry.get("source_evidence") or {}
        if not clean(evidence.get("project_source_member")):
            raise SystemExit(f"{key} lacks project-source member provenance")
        if not HEX64.fullmatch(clean(evidence.get("sha256"))):
            raise SystemExit(f"{key} has invalid source PDF SHA-256")

        kind = entry.get("resolution_kind")
        if kind == "source_grounded_definition":
            source_grounded += 1
            if not clean(entry.get("definition")):
                raise SystemExit(f"{key} source-grounded definition is empty")
            if not entry.get("source_support"):
                raise SystemExit(f"{key} source-grounded definition lacks support")
            if entry.get("confidence") not in {"medium", "high"} or entry.get("reversible") is not True:
                raise SystemExit(f"{key} source-grounded metadata invalid")
        elif kind == "owner_delegated_recommendation":
            recommended += 1
            recommendation = entry.get("recommendation") or {}
            if not clean(recommendation.get("Definition")):
                raise SystemExit(f"{key} recommendation is empty")
            if not entry.get("source_support"):
                raise SystemExit(f"{key} recommendation lacks source support")
            if not clean(entry.get("rationale")):
                raise SystemExit(f"{key} recommendation lacks rationale")
            if len(entry.get("alternatives_considered") or []) < 2:
                raise SystemExit(f"{key} recommendation lacks alternatives")
            if entry.get("confidence") not in {"low", "medium", "high"}:
                raise SystemExit(f"{key} recommendation has invalid confidence")
            if entry.get("reversible") is not True:
                raise SystemExit(f"{key} recommendation is not reversible")
        else:
            raise SystemExit(f"{key} has unsupported resolution kind {kind!r}")

    summary = closure.get("summary") or {}
    if len(seen) != 15:
        raise SystemExit(f"expected 15 missing-definition rows; got {len(seen)}")
    if source_grounded != 12 or recommended != 3:
        raise SystemExit(
            f"expected 12 source-grounded and 3 recommended definitions; "
            f"got {source_grounded}/{recommended}"
        )
    if summary != {
        "missing_definition_rows": 15,
        "source_grounded_definitions": 12,
        "owner_delegated_recommendations": 3,
        "raw_source_rows_modified": 0,
    }:
        raise SystemExit(f"closure summary mismatch: {summary}")

    print(json.dumps({
        "closure": str(CLOSURE.relative_to(ROOT)),
        "validatedRows": len(seen),
        "sourceGroundedDefinitions": source_grounded,
        "ownerDelegatedRecommendations": recommended,
        "rawSourceRowsModified": 0,
        "ownerDelegation": "approved-and-active",
        "result": "PASS",
    }, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
