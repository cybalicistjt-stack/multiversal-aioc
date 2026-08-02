#!/usr/bin/env python3
"""Apply second high-certainty survivor-review decisions.

Targets malformed headings, embedded chat residue, summary/container headings, and
compound multi-topic blocks discovered in survivor tranche 04. This stage is
non-canonical and preserves every rejection with provenance.
"""
from __future__ import annotations

import argparse
import json
import re
from collections import Counter
from pathlib import Path

CHAT_RESIDUE = re.compile(r"\b(?:you said:|chatgpt said:|assistant said:|user said:)\b", re.I)
SUMMARY_CONTAINER = re.compile(
    r"^(?:summary of|overview of|key .* rules|summary of key|quick summary|"
    r"design summary|rules summary|system summary)\b",
    re.I,
)
MALFORMED_TABLE_HEADING = re.compile(
    r"^(?:rollconsequence|rollresult|d\d+result|resultconsequence|"
    r"nameeffect|typeeffect|roll effect)$",
    re.I,
)
EXAMPLE_CONTAINER = re.compile(
    r"\b(?:examples? at each tier|example outcomes?|sample consequences?|"
    r"illustrative examples?|example progression)\b",
    re.I,
)
COMPOUND_TRANSITION = re.compile(
    r"\b(?:creating an? .* system|here'?s a framework|the following framework|"
    r"next,? we|now,? we|this section also covers)\b",
    re.I,
)


def load_jsonl(path: Path) -> list[dict]:
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]


def reason(row: dict) -> str | None:
    name = str(row.get("name") or "").strip()
    summary = str((row.get("specification") or {}).get("summary") or "").strip()
    combined = f"{name}\n{summary}"

    if CHAT_RESIDUE.search(combined):
        return "embedded-chat-transcript-residue"
    if SUMMARY_CONTAINER.search(name):
        return "summary-container-as-object"
    if MALFORMED_TABLE_HEADING.fullmatch(re.sub(r"\s+", "", name.lower())):
        return "malformed-table-heading"
    if EXAMPLE_CONTAINER.search(name):
        return "example-container-as-object"

    # Reject blocks whose title suggests one object but whose body abruptly begins
    # an unrelated framework/system, indicating merged document regions.
    if COMPOUND_TRANSITION.search(summary) and len(summary) > 350:
        return "compound-multi-topic-block"

    # Concatenated camel/title tokens without spaces often come from collapsed table
    # columns. Preserve normal PascalCase proper names by requiring mechanical terms.
    if re.fullmatch(r"[A-Za-z]{8,}", name) and re.search(
        r"(?:roll|result|consequence|cost|effect|duration|range)$", name, re.I
    ):
        return "collapsed-table-column-heading"

    return None


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--candidates", type=Path, required=True)
    ap.add_argument("--out", type=Path, required=True)
    args = ap.parse_args()

    src = args.candidates
    if src.is_dir():
        preferred = src / "survivor-filtered-candidates-v4.jsonl"
        src = preferred if preferred.exists() else src / "canonical-candidates-v4.jsonl"

    rows = load_jsonl(src)
    kept: list[dict] = []
    rejected: list[dict] = []
    counts: Counter[str] = Counter()

    for row in rows:
        why = reason(row)
        if why:
            counts[why] += 1
            rejected.append({
                "candidateId": row.get("id"),
                "objectType": row.get("objectType") or row.get("type"),
                "name": row.get("name"),
                "reason": why,
                "source": (row.get("provenance") or [{}])[0],
                "authority": "Direct-review rejection evidence only; never canonical.",
            })
        else:
            kept.append(row)

    args.out.mkdir(parents=True, exist_ok=True)
    with (args.out / "survivor-filtered-candidates-v4-2.jsonl").open("w", encoding="utf-8") as handle:
        for row in kept:
            handle.write(json.dumps(row, ensure_ascii=False) + "\n")

    (args.out / "survivor-review-rejections-v4-2.json").write_text(
        json.dumps({"records": rejected}, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    families = Counter((row.get("objectType") or row.get("type")) for row in kept)
    index = {
        "format": "multiversal-survivor-review-decisions-v4-2",
        "version": "1.0.0",
        "inputCandidateCount": len(rows),
        "survivingCandidateCount": len(kept),
        "rejectedCandidateCount": len(rejected),
        "rejectionReasons": dict(counts),
        "survivingFamilyCounts": dict(families),
        "authority": "Review evidence only; no canonical import, merge, or approval.",
    }
    (args.out / "survivor-review-decisions-v4-2-index.json").write_text(
        json.dumps(index, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    print(json.dumps(index, indent=2))


if __name__ == "__main__":
    main()
