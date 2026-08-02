#!/usr/bin/env python3
"""Sanitize v4 relationship candidates and recalculate canonical diagnostics."""
from __future__ import annotations
import argparse, json, re
from collections import Counter
from pathlib import Path

SCALAR = re.compile(r"^(?:DC\s*\d+|[-+]?\d+(?:\.\d+)?(?:\s*(?:ft|feet|miles?|hours?|minutes?|rounds?|turns?|XP|MC))?|\d+d\d+(?:\s*[+-]\s*\d+)?)$", re.I)
BAD = re.compile(r"^(?:[a-z],?|[a-z]\d?|the|a|an|this|that|target|caster|user|creature|character|characters|players?)$", re.I)
LEXICAL = re.compile(r"^[A-Za-z][A-Za-z0-9 '&’()\-]{2,79}$")


def load(path: Path) -> list[dict]:
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]


def valid_target(value: object) -> bool:
    text = re.sub(r"\s+", " ", str(value or "")).strip(" .,:;–—-")
    if not text or SCALAR.fullmatch(text) or BAD.fullmatch(text):
        return False
    if not LEXICAL.fullmatch(text):
        return False
    words = text.split()
    if len(words) > 10 or len(text) < 3:
        return False
    return any(ch.isalpha() for ch in text)


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--canonical", type=Path, required=True)
    args = ap.parse_args()
    data_path = args.canonical / "canonical-candidates-v4.jsonl"
    index_path = args.canonical / "canonical-candidate-v4-index.json"
    rows = load(data_path)
    removed = Counter()
    resolved = unresolved = 0
    routes = Counter()
    for row in rows:
        cleaned = []
        seen = set()
        for rel in row.get("relationships") or []:
            target = rel.get("targetName")
            if not valid_target(target):
                removed["invalid-relationship-target"] += 1
                continue
            sig = (rel.get("relationshipType"), rel.get("targetId"), re.sub(r"\W+", "", str(target).lower()))
            if sig in seen:
                removed["duplicate-relationship"] += 1
                continue
            seen.add(sig)
            cleaned.append(rel)
            if rel.get("targetId"):
                resolved += 1
            else:
                unresolved += 1
        row["relationships"] = cleaned
        gates = ((row.get("validation") or {}).get("gates") or {})
        gates["relationshipsReviewed"] = unresolved == 0 if len(rows) == 1 else not any(not r.get("targetId") for r in cleaned)
        # Re-evaluate route after sanitization. Expert tier still requires strong boundaries.
        rec = row.get("recovery") or {}
        strong = (
            rec.get("identityConfidence", 0) >= 92
            and rec.get("completenessScore", 0) >= 80
            and rec.get("familyMargin", 0) >= 6
            and rec.get("boundaryEvidenceCount", 0) >= 2
            and rec.get("sectionCount", 0) >= 2
            and not any(not r.get("targetId") for r in cleaned)
        )
        row["reviewRoute"] = "expert-sample" if strong else ("human-review" if rec.get("identityConfidence", 0) >= 70 else "evidence-only")
        routes[row["reviewRoute"]] += 1
    with data_path.open("w", encoding="utf-8") as handle:
        for row in rows:
            handle.write(json.dumps(row, ensure_ascii=False) + "\n")
    index = json.loads(index_path.read_text(encoding="utf-8"))
    index.update({
        "version": "4.3.1",
        "resolvedRelationshipCount": resolved,
        "unresolvedRelationshipCount": unresolved,
        "relationshipSanitizerRemovedCounts": dict(removed),
        "expertSampleCount": routes["expert-sample"],
        "humanReviewCount": routes["human-review"],
        "evidenceOnlyCount": routes["evidence-only"],
        "publishedSample": rows[:200],
    })
    index_path.write_text(json.dumps(index, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(json.dumps({"resolved": resolved, "unresolved": unresolved, "removed": dict(removed), "routes": dict(routes)}, indent=2))


if __name__ == "__main__":
    main()
