#!/usr/bin/env python3
"""Build governed promotion batches from refined forensic findings.

This tool never edits canonical content. It converts reviewable findings into
portable candidate envelopes with provenance, confidence, validation notes, and
explicit approval gates. Complete queues remain workflow artifacts; bounded
batch indexes may be published to the static AIOC.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

QUEUE_NAMES = ("likely-new", "likely-existing", "possibly-existing", "ambiguous")
TYPE_MAP = {
    "ability": "ability", "creature": "creature", "npc": "npc",
    "item": "item", "vehicle": "vehicle", "species": "species",
    "world": "world", "environment": "environment", "adventure": "adventure",
    "faction": "faction", "rule": "rule", "economy": "rule",
}


def read_json(path: Path, default: Any = None) -> Any:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception:
        return default


def slug(value: str) -> str:
    text = re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")
    return text[:64] or "untitled"


def stable_id(*parts: str) -> str:
    return hashlib.sha256("\n".join(parts).encode("utf-8", "ignore")).hexdigest()[:16]


def dominant_family(row: dict[str, Any]) -> str:
    scores = row.get("family_scores") or row.get("familyScores") or {}
    if isinstance(scores, dict) and scores:
        return max(scores, key=lambda key: scores.get(key, 0))
    families = row.get("families") or []
    return families[0] if families else "rule"


def source_receipt(row: dict[str, Any]) -> dict[str, Any]:
    return {
        "sourcePath": row.get("source_path") or row.get("sourcePath") or "",
        "documentId": row.get("document_id") or row.get("documentId") or "",
        "locator": row.get("locator") or "",
        "page": row.get("page"),
        "findingId": row.get("finding_id") or row.get("findingId") or "",
        "textHash": hashlib.sha256(str(row.get("text") or "").encode("utf-8", "ignore")).hexdigest(),
    }


def candidate_from(row: dict[str, Any], queue: str) -> dict[str, Any]:
    title = str(row.get("normalized_title") or row.get("title_candidate") or row.get("title") or "Untitled finding").strip()
    family = dominant_family(row)
    finding_id = str(row.get("finding_id") or row.get("findingId") or stable_id(title, str(row.get("locator"))))
    object_type = TYPE_MAP.get(family, "rule")
    candidate_id = f"audit-{object_type}-{slug(title)}-{finding_id[:8]}"
    confidence = float(row.get("confidence") or row.get("signal_strength") or row.get("signalStrength") or 0)
    suggested = row.get("canonical_candidates") or row.get("canonicalCandidates") or []
    return {
        "format": "multiversal-canonical-candidate",
        "version": "1.0.0",
        "candidateId": candidate_id,
        "queue": queue,
        "proposedObjectType": object_type,
        "proposedName": title,
        "proposedStableId": "",
        "confidence": confidence,
        "source": source_receipt(row),
        "suggestedCanonicalMatches": suggested[:10] if isinstance(suggested, list) else [],
        "evidenceText": str(row.get("text") or "")[:12000],
        "mechanicSignals": row.get("mechanic_signals") or row.get("mechanicSignals") or [],
        "familyScores": row.get("family_scores") or row.get("familyScores") or {},
        "review": {
            "state": "unreviewed",
            "decision": "",
            "reviewer": "",
            "reviewedAt": "",
            "notes": "",
        },
        "promotionGates": {
            "identityConfirmed": False,
            "objectTypeConfirmed": False,
            "sourceVerified": False,
            "duplicateResolved": False,
            "schemaPrepared": False,
            "ownerApproved": False,
        },
        "authorityNote": "Candidate evidence only. This record cannot enter canon until every promotion gate is explicitly satisfied.",
    }


def load_queue(root: Path, name: str) -> list[dict[str, Any]]:
    candidates = [
        root / f"{name}.json",
        root / f"{name}-queue.json",
        root / "refined-queues" / f"{name}.json",
    ]
    for path in candidates:
        payload = read_json(path)
        if isinstance(payload, list):
            return payload
        if isinstance(payload, dict):
            for key in ("findings", "items", "records", "queue"):
                if isinstance(payload.get(key), list):
                    return payload[key]
    return []


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--source", type=Path, default=Path("audit-output"))
    parser.add_argument("--out", type=Path, default=Path("audit-output/promotion"))
    parser.add_argument("--batch-size", type=int, default=100)
    parser.add_argument("--publish-limit", type=int, default=500)
    args = parser.parse_args()
    args.out.mkdir(parents=True, exist_ok=True)

    all_candidates: list[dict[str, Any]] = []
    queue_counts: Counter[str] = Counter()
    type_counts: Counter[str] = Counter()
    batches: list[dict[str, Any]] = []

    for queue_name in QUEUE_NAMES:
        rows = load_queue(args.source, queue_name)
        queue_candidates = [candidate_from(row, queue_name) for row in rows]
        queue_counts[queue_name] = len(queue_candidates)
        all_candidates.extend(queue_candidates)
        type_counts.update(item["proposedObjectType"] for item in queue_candidates)
        for offset in range(0, len(queue_candidates), max(1, args.batch_size)):
            batch_items = queue_candidates[offset:offset + args.batch_size]
            batch_id = f"{queue_name}-{offset // args.batch_size + 1:04d}"
            batch = {
                "format": "multiversal-forensic-promotion-batch",
                "version": "1.0.0",
                "batchId": batch_id,
                "queue": queue_name,
                "createdAt": datetime.now(timezone.utc).isoformat(),
                "candidateCount": len(batch_items),
                "candidates": batch_items,
                "batchDecision": "unreviewed",
                "authorityNote": "Batch decisions do not modify canon. Approved candidates must be imported through the Production Database review workflow.",
            }
            (args.out / f"{batch_id}.json").write_text(json.dumps(batch, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
            batches.append({k: batch[k] for k in ("batchId", "queue", "createdAt", "candidateCount", "batchDecision")})

    index = {
        "format": "multiversal-forensic-promotion-index",
        "version": "1.0.0",
        "generatedAt": datetime.now(timezone.utc).isoformat(),
        "candidateCount": len(all_candidates),
        "queueCounts": dict(queue_counts),
        "objectTypeCounts": dict(type_counts),
        "batchSize": args.batch_size,
        "batchCount": len(batches),
        "batches": batches,
        "publishedCandidateSample": all_candidates[: max(0, args.publish_limit)],
        "promotionPolicy": {
            "automaticCanonicalWrites": False,
            "requiredGates": ["identityConfirmed", "objectTypeConfirmed", "sourceVerified", "duplicateResolved", "schemaPrepared", "ownerApproved"],
        },
    }
    (args.out / "promotion-index.json").write_text(json.dumps(index, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(json.dumps({k: index[k] for k in ("candidateCount", "queueCounts", "objectTypeCounts", "batchCount")}, indent=2))


if __name__ == "__main__":
    main()
