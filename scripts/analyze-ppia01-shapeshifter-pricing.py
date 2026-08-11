#!/usr/bin/env python3
"""Analyze the 57 Shapeshifter pricing-only source rows without auto-merging them."""
from __future__ import annotations

import argparse
import csv
import difflib
import io
import json
import zipfile
from collections import defaultdict
from pathlib import Path

DATASET = "species_elementalist_and_innate_abilities_catalog.csv"
PARENT = "Shapeshifter Archetype"
BRANCH_EXPECTATIONS = {
    "Combat Forms": {"detailed": 20, "pricing": 20},
    "Environmental Adaptations": {"detailed": 20, "pricing": 19},
    "Utility Transformations": {"detailed": 20, "pricing": 18},
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", default=".")
    parser.add_argument("--archive", default="Csv.zip")
    parser.add_argument("--output")
    parser.add_argument("--csv-output")
    return parser.parse_args()


def clean(value: str | None) -> str:
    return (value or "").strip()


def compact(row: dict[str, str], source_row: int) -> dict:
    return {
        "sourceRow": source_row,
        "recordId": clean(row.get("Record_ID")),
        "name": clean(row.get("Ability_Name")),
        "tier": clean(row.get("Tier")),
        "xpCost": clean(row.get("Ability_XP_Cost")),
        "effect": clean(row.get("Effect")),
        "mechanics": clean(row.get("Mechanics")),
        "sourcePage": clean(row.get("Source_Page")),
        "sourceSection": clean(row.get("Source_Section")),
        "branch": clean(row.get("Branch")),
    }


def main() -> int:
    args = parse_args()
    root = Path(args.root)
    archive = root / args.archive
    snapshot = json.loads(
        (root / "governance/object-system/csv-intake/CSV_INTAKE_AUDIT_SNAPSHOT.json").read_text(encoding="utf-8")
    )
    expected_entry = next(entry for entry in snapshot["files"] if entry["name"] == DATASET)

    with zipfile.ZipFile(archive) as zf:
        members = {Path(name).name: name for name in zf.namelist()}
        with zf.open(members[DATASET]) as source:
            text = source.read().decode("utf-8-sig")
    reader = csv.DictReader(io.StringIO(text))
    rows = list(reader)
    if len(rows) != expected_entry["rows"]:
        raise SystemExit(f"unexpected {DATASET} row count: {len(rows)}")

    all_named: dict[str, list[tuple[int, dict[str, str]]]] = defaultdict(list)
    for source_row, row in enumerate(rows, start=2):
        name = clean(row.get("Ability_Name"))
        if name:
            all_named[name.casefold()].append((source_row, row))

    branch_summary = {}
    matrix = []
    total_detailed = 0
    total_pricing = 0
    exact_same_branch = 0
    exact_cross_branch = 0

    for branch, expected in BRANCH_EXPECTATIONS.items():
        detailed: list[tuple[int, dict[str, str]]] = []
        pricing: list[tuple[int, dict[str, str]]] = []
        for source_row, row in enumerate(rows, start=2):
            if clean(row.get("Parent_Tree")) != PARENT or clean(row.get("Branch")) != branch:
                continue
            section = clean(row.get("Source_Section"))
            record_type = clean(row.get("Record_Type"))
            if "pricing list" in section.casefold():
                pricing.append((source_row, row))
            elif record_type == "Ability":
                detailed.append((source_row, row))

        if len(detailed) != expected["detailed"] or len(pricing) != expected["pricing"]:
            raise SystemExit(
                f"{branch}: expected detailed/pricing {expected}, got "
                f"{len(detailed)}/{len(pricing)}"
            )
        total_detailed += len(detailed)
        total_pricing += len(pricing)

        detailed_by_tier: dict[str, list[tuple[int, dict[str, str]]]] = defaultdict(list)
        for source_row, row in detailed:
            detailed_by_tier[clean(row.get("Tier"))].append((source_row, row))

        tier_counts = {
            tier: {
                "detailed": len(detailed_by_tier.get(tier, [])),
                "pricing": sum(1 for _, row in pricing if clean(row.get("Tier")) == tier),
            }
            for tier in sorted({clean(row.get("Tier")) for _, row in detailed + pricing})
        }
        branch_summary[branch] = {
            "detailedAbilityRows": len(detailed),
            "pricingOnlyRows": len(pricing),
            "tierCounts": tier_counts,
        }

        for source_row, price_row in pricing:
            price_name = clean(price_row.get("Ability_Name"))
            tier = clean(price_row.get("Tier"))
            same_tier = detailed_by_tier.get(tier, [])
            exact_branch = [
                compact(candidate, candidate_row)
                for candidate_row, candidate in detailed
                if clean(candidate.get("Ability_Name")).casefold() == price_name.casefold()
            ]
            global_exact = [
                compact(candidate, candidate_row)
                for candidate_row, candidate in all_named.get(price_name.casefold(), [])
                if candidate_row != source_row
                and "pricing list" not in clean(candidate.get("Source_Section")).casefold()
            ]
            cross_branch = [candidate for candidate in global_exact if candidate["branch"] != branch]
            if exact_branch:
                exact_same_branch += 1
                disposition = "exact-name-same-branch-candidate"
            elif cross_branch:
                exact_cross_branch += 1
                disposition = "cross-branch-exact-name-review"
            else:
                disposition = "ambiguous-same-tier-candidate-set"

            tier_candidates = []
            for candidate_row, candidate in same_tier:
                candidate_name = clean(candidate.get("Ability_Name"))
                tier_candidates.append(
                    {
                        **compact(candidate, candidate_row),
                        "nameSimilarity": round(
                            difflib.SequenceMatcher(None, price_name.casefold(), candidate_name.casefold()).ratio(),
                            4,
                        ),
                        "candidateAuthority": "review-hint-only",
                    }
                )
            tier_candidates.sort(key=lambda item: (-item["nameSimilarity"], item["sourceRow"]))

            matrix.append(
                {
                    "pricing": compact(price_row, source_row),
                    "disposition": disposition,
                    "exactNameSameBranchCandidates": exact_branch,
                    "exactNameCrossBranchCandidates": cross_branch,
                    "sameBranchSameTierCandidates": tier_candidates,
                    "automaticMergeAuthorized": False,
                    "reviewRule": (
                        "Name similarity and tier are review hints only. A merge/pairing requires exact source evidence "
                        "or an explicitly recorded owner-delegated recommendation with rationale, alternatives, confidence, and reversibility."
                    ),
                }
            )

    if total_detailed != 60 or total_pricing != 57:
        raise SystemExit(f"unexpected Shapeshifter totals {total_detailed}/{total_pricing}")

    report = {
        "format": "multiversal-ppia01-shapeshifter-pricing-reconciliation",
        "version": "0.1.0",
        "dataset": DATASET,
        "parentTree": PARENT,
        "sourcePdf": "Innate Trees(3).PDF",
        "summary": {
            "detailedAbilityRows": total_detailed,
            "pricingOnlyRows": total_pricing,
            "exactNameSameBranchCandidates": exact_same_branch,
            "exactNameCrossBranchCandidates": exact_cross_branch,
            "pricingRowsWithoutExactNameCandidate": total_pricing - exact_same_branch - exact_cross_branch,
            "automaticMerges": 0,
        },
        "branches": branch_summary,
        "matrix": sorted(matrix, key=lambda item: item["pricing"]["sourceRow"]),
    }

    serialized = json.dumps(report, indent=2, sort_keys=True) + "\n"
    if args.output:
        out = Path(args.output)
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(serialized, encoding="utf-8")

    if args.csv_output:
        out = Path(args.csv_output)
        out.parent.mkdir(parents=True, exist_ok=True)
        with out.open("w", newline="", encoding="utf-8") as handle:
            writer = csv.writer(handle)
            writer.writerow(
                [
                    "pricing_source_row",
                    "pricing_record_id",
                    "branch",
                    "tier",
                    "pricing_name",
                    "xp_cost",
                    "disposition",
                    "exact_cross_branch_candidates",
                    "same_tier_candidate_names",
                ]
            )
            for item in report["matrix"]:
                pricing = item["pricing"]
                writer.writerow(
                    [
                        pricing["sourceRow"],
                        pricing["recordId"],
                        pricing["branch"],
                        pricing["tier"],
                        pricing["name"],
                        pricing["xpCost"],
                        item["disposition"],
                        " | ".join(
                            f"{candidate['recordId']}:{candidate['name']}:{candidate['branch']}"
                            for candidate in item["exactNameCrossBranchCandidates"]
                        ),
                        " | ".join(candidate["name"] for candidate in item["sameBranchSameTierCandidates"]),
                    ]
                )

    print(json.dumps(report["summary"], sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
