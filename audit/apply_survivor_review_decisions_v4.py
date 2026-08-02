#!/usr/bin/env python3
"""Apply high-certainty direct-review decisions to Semantic Recovery v4 candidates.

This stage is deliberately separate from broad boundary filtering. It records
human-semantic decisions from survivor review, preserves rejected records in an
audit file, and never writes canonical content.
"""
from __future__ import annotations

import argparse
import json
import re
from collections import Counter
from pathlib import Path

MECHANIC_FRAGMENT = re.compile(
    r"^(?:\d+\s*)?uses?\s*/\s*day\b|^(?:can|may|must|requires?)\s+|"
    r"^[^A-Za-z]{0,3}(?:range|duration|cost|weight|battery|activation)\s*[:=]",
    re.I,
)
CHILD_SECTION = re.compile(
    r"^(?:mechanics of|function in play|duration and limitations|casting limitations|"
    r"activation and power source|activation & power source|death and severance|"
    r"thematic examples? of|examples? of|optional racial traits|terrain types|"
    r"using .* in your campaign|.* setting in your campaign)$",
    re.I,
)
GUIDANCE_OR_EXAMPLES = re.compile(
    r"\b(?:thematic examples?|example consequences?|function in play|"
    r"in your campaign|gm guidance|design guidance|usage guidance)\b",
    re.I,
)


def load_jsonl(path: Path) -> list[dict]:
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]


def review_reason(row: dict) -> str | None:
    name = str(row.get("name") or "").strip()
    family = str(row.get("objectType") or row.get("type") or "")
    summary = str((row.get("specification") or {}).get("summary") or "").strip()

    if MECHANIC_FRAGMENT.search(name):
        return "survivor-mechanic-fragment"
    if CHILD_SECTION.fullmatch(name):
        return "survivor-child-or-guidance-section"
    if GUIDANCE_OR_EXAMPLES.search(name):
        return "survivor-guidance-or-example-container"
    if family == "ability" and re.match(r"^mechanics of\s+", name, re.I):
        return "ability-mechanics-child-section"
    if family == "species" and re.match(r"^optional\s+(?:racial|species)\s+traits$", name, re.I):
        return "species-optional-trait-container"
    if family in {"world", "environment", "adventure"} and re.search(r"\bin your campaign$", name, re.I):
        return "setting-campaign-guidance"
    # Reject obvious sentence-like fragments while preserving named mechanics.
    words = name.split()
    if len(words) >= 4 and name[:1].islower() and not re.search(r"[:()\-]", name):
        return "survivor-sentence-fragment"
    # A short semicolon-delimited mechanic value is not an identity.
    if ";" in name and len(words) <= 8 and re.search(r"\b(?:can|uses?|range|rotate|duration)\b", name, re.I):
        return "survivor-inline-mechanic-fragment"
    return None


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--candidates", type=Path, required=True)
    ap.add_argument("--out", type=Path, required=True)
    args = ap.parse_args()

    src = args.candidates
    if src.is_dir():
        src = src / "canonical-candidates-v4.jsonl"
    rows = load_jsonl(src)
    kept: list[dict] = []
    rejected: list[dict] = []
    reasons: Counter[str] = Counter()

    for row in rows:
        reason = review_reason(row)
        if reason:
            reasons[reason] += 1
            rejected.append({
                "candidateId": row.get("id"),
                "objectType": row.get("objectType") or row.get("type"),
                "name": row.get("name"),
                "reason": reason,
                "source": (row.get("provenance") or [{}])[0],
                "authority": "Direct-review rejection evidence only; never canonical.",
            })
        else:
            kept.append(row)

    args.out.mkdir(parents=True, exist_ok=True)
    with (args.out / "survivor-filtered-candidates-v4.jsonl").open("w", encoding="utf-8") as handle:
        for row in kept:
            handle.write(json.dumps(row, ensure_ascii=False) + "\n")
    (args.out / "survivor-review-rejections-v4.json").write_text(
        json.dumps({"records": rejected}, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    family_counts = Counter((row.get("objectType") or row.get("type")) for row in kept)
    index = {
        "format": "multiversal-survivor-review-decisions-v4",
        "version": "1.0.0",
        "inputCandidateCount": len(rows),
        "survivingCandidateCount": len(kept),
        "rejectedCandidateCount": len(rejected),
        "rejectionReasons": dict(reasons),
        "survivingFamilyCounts": dict(family_counts),
        "authority": "Review evidence only; no canonical import, merge, or approval.",
    }
    (args.out / "survivor-review-decisions-v4-index.json").write_text(
        json.dumps(index, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    print(json.dumps(index, indent=2))


if __name__ == "__main__":
    main()
