#!/usr/bin/env python3
"""Build schema-oriented canonical-object factory outputs from forensic promotion batches.

This stage does not write to canonical content. It reshapes evidence candidates,
rejects weak names, consolidates repeated evidence, recommends packs, and emits
review tiers with explicit gates.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

GENERIC = {
    "introduction", "overview", "description", "rules", "rule", "abilities",
    "items", "creatures", "vehicles", "world", "worlds", "notes", "example",
    "examples", "chapter", "section", "contents", "table", "appendix",
}
TYPE_TO_PACK = {
    "ability": "core-abilities.pack",
    "rule": "core-rules.pack",
    "item": "core-items.pack",
    "creature": "core-creatures.pack",
    "npc": "core-npcs.pack",
    "vehicle": "core-vehicles.pack",
    "species": "core-species.pack",
    "world": "legacy-worlds.pack",
    "environment": "core-environments.pack",
    "adventure": "legacy-adventures.pack",
    "faction": "legacy-factions.pack",
}
REQUIRED_COMMON = ("id", "objectType", "name", "status", "provenance", "spec")


def norm(value: str) -> str:
    value = re.sub(r"[^a-z0-9]+", " ", (value or "").lower()).strip()
    return re.sub(r"\s+", " ", value)


def slug(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", norm(value)).strip("-")[:72] or "untitled"


def load(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def clean_source(path: str) -> str:
    marker = "/audit-work/corpus/"
    if marker in path:
        return path.split(marker, 1)[1]
    return path.replace("\\", "/")


def good_name(name: str) -> tuple[bool, list[str]]:
    reasons: list[str] = []
    n = norm(name)
    words = n.split()
    if not n or n in GENERIC:
        reasons.append("generic-or-empty")
    if len(words) > 16:
        reasons.append("too-long")
    if len(n) < 3:
        reasons.append("too-short")
    if re.search(r"\b(page|chapter|section)\s*\d+\b", n):
        reasons.append("document-navigation")
    if sum(ch.isdigit() for ch in name) > max(3, len(name) // 3):
        reasons.append("numeric-heavy")
    return not reasons, reasons


def load_batches(root: Path) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    for path in sorted(root.glob("*.json")):
        if path.name == "promotion-index.json":
            continue
        payload = load(path)
        candidates = payload.get("candidates", payload if isinstance(payload, list) else [])
        for c in candidates:
            c = dict(c)
            c["_batch"] = path.stem
            rows.append(c)
    return rows


def evidence_key(c: dict[str, Any]) -> str:
    return "|".join([
        str(c.get("proposedObjectType") or c.get("objectType") or "unknown"),
        norm(str(c.get("proposedName") or c.get("name") or "")),
    ])


def make_object(group: list[dict[str, Any]]) -> dict[str, Any]:
    first = group[0]
    object_type = str(first.get("proposedObjectType") or first.get("objectType") or "rule")
    name = str(first.get("proposedName") or first.get("name") or "Untitled candidate").strip()
    source_rows = []
    signals: list[str] = []
    possible_matches: list[Any] = []
    for row in group:
        prov = row.get("provenance") or {}
        source_rows.append({
            "sourcePath": clean_source(str(prov.get("sourcePath") or row.get("sourcePath") or "")),
            "locator": prov.get("locator") or row.get("locator"),
            "findingId": prov.get("findingId") or row.get("findingId"),
            "evidenceHash": prov.get("evidenceHash") or row.get("evidenceHash"),
        })
        signals.extend(row.get("mechanicSignals") or [])
        possible_matches.extend(row.get("possibleCanonicalMatches") or [])
    unique_sources = []
    seen = set()
    for src in source_rows:
        key = json.dumps(src, sort_keys=True)
        if key not in seen:
            seen.add(key); unique_sources.append(src)
    raw_id = f"legacy.{object_type}.{slug(name)}"
    suffix = hashlib.sha256(evidence_key(first).encode()).hexdigest()[:8]
    stable_id = f"{raw_id}.{suffix}"
    name_ok, name_issues = good_name(name)
    schema_issues = [] if object_type in TYPE_TO_PACK else ["unmapped-object-type"]
    confidence = max(float(r.get("confidence") or r.get("signalStrength") or 0) for r in group)
    gates = {
        "identityConfirmed": False,
        "objectTypeConfirmed": object_type in TYPE_TO_PACK,
        "sourceVerified": bool(unique_sources),
        "duplicateResolved": len(group) == 1,
        "schemaPrepared": name_ok and not schema_issues,
        "ownerApproved": False,
    }
    if not name_ok:
        tier = "needs-retitling"
    elif confidence >= 7 and object_type in TYPE_TO_PACK and unique_sources:
        tier = "designer-review"
    elif confidence >= 4:
        tier = "needs-structure"
    else:
        tier = "low-confidence"
    return {
        "format": "multiversal-object-factory-candidate",
        "version": "1.0.0",
        "candidateId": stable_id,
        "candidateTier": tier,
        "sourceQueue": first.get("queue"),
        "sourceBatches": sorted({r.get("_batch") for r in group}),
        "evidenceCount": len(unique_sources),
        "canonicalEnvelope": {
            "id": stable_id,
            "objectType": object_type,
            "name": name,
            "status": "candidate",
            "provenance": unique_sources,
            "spec": {
                "legacyText": first.get("evidenceText") or first.get("text") or "",
                "mechanicSignals": sorted(set(signals))[:80],
            },
        },
        "recommendedPack": TYPE_TO_PACK.get(object_type),
        "possibleCanonicalMatches": possible_matches[:10],
        "quality": {
            "confidence": confidence,
            "nameIssues": name_issues,
            "schemaIssues": schema_issues,
            "duplicateEvidenceCount": max(0, len(group) - 1),
        },
        "gates": gates,
        "authority": "Candidate only; requires designer review and owner approval before canonical promotion.",
    }


def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument("--promotion", type=Path, required=True)
    p.add_argument("--out", type=Path, required=True)
    p.add_argument("--batch-size", type=int, default=50)
    args = p.parse_args()
    args.out.mkdir(parents=True, exist_ok=True)

    rows = load_batches(args.promotion)
    groups: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for row in rows:
        groups[evidence_key(row)].append(row)
    objects = [make_object(group) for _, group in sorted(groups.items())]
    objects.sort(key=lambda x: (x["candidateTier"], x["canonicalEnvelope"]["objectType"], x["canonicalEnvelope"]["name"].lower()))

    tiers = Counter(o["candidateTier"] for o in objects)
    types = Counter(o["canonicalEnvelope"]["objectType"] for o in objects)
    packs = Counter(o["recommendedPack"] or "unassigned" for o in objects)
    batches = []
    for i in range(0, len(objects), args.batch_size):
        chunk = objects[i:i + args.batch_size]
        batch_id = f"factory-{i // args.batch_size + 1:04d}"
        payload = {
            "format": "multiversal-object-factory-batch",
            "version": "1.0.0",
            "batchId": batch_id,
            "candidateCount": len(chunk),
            "candidates": chunk,
        }
        (args.out / f"{batch_id}.json").write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
        batches.append({"batchId": batch_id, "candidateCount": len(chunk), "tiers": dict(Counter(x["candidateTier"] for x in chunk))})

    summary = {
        "format": "multiversal-object-factory-index",
        "version": "1.0.0",
        "generatedAt": datetime.now(timezone.utc).isoformat(),
        "sourcePromotionCandidateCount": len(rows),
        "consolidatedCandidateCount": len(objects),
        "duplicateEvidenceCollapsed": len(rows) - len(objects),
        "tierCounts": dict(tiers),
        "objectTypeCounts": dict(types),
        "packCounts": dict(packs),
        "batchSize": args.batch_size,
        "batchCount": len(batches),
        "batches": batches,
        "publishedSample": objects[:200],
        "requiredCommonFields": list(REQUIRED_COMMON),
        "authorityNote": "Factory outputs are schema-oriented candidates, not canonical objects.",
    }
    (args.out / "object-factory-index.json").write_text(json.dumps(summary, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(json.dumps({k: summary[k] for k in ("sourcePromotionCandidateCount", "consolidatedCandidateCount", "duplicateEvidenceCollapsed", "tierCounts", "batchCount")}, indent=2))


if __name__ == "__main__":
    main()
