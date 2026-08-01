#!/usr/bin/env python3
"""Build governed canonical handoffs from recovery outputs.

This stage prepares reviewable handoff bundles, relationship-resolution queues,
and source-area completion receipts. It never writes canonical content.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


def load(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def stable(prefix: str, value: str) -> str:
    return f"{prefix}-{hashlib.sha256(value.encode('utf-8')).hexdigest()[:16]}"


def source_group(candidate: dict[str, Any]) -> str:
    sources = candidate.get("provenance") or candidate.get("canonicalEnvelope", {}).get("provenance") or []
    if not sources:
        return "unassigned"
    path = str(sources[0].get("sourcePath") or "unassigned").replace("\\", "/")
    parts = [p for p in path.split("/") if p]
    return "/".join(parts[:3]) if len(parts) >= 3 else path


def iter_candidates(root: Path) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    for path in sorted(root.glob("*.json")):
        if path.name.endswith("index.json"):
            continue
        payload = load(path)
        candidates = payload.get("candidates", payload if isinstance(payload, list) else [])
        for row in candidates:
            rows.append(dict(row))
    return rows


def relationship_rows(candidate: dict[str, Any]) -> list[dict[str, Any]]:
    cid = candidate.get("candidateId") or candidate.get("canonicalEnvelope", {}).get("id")
    name = candidate.get("name") or candidate.get("canonicalEnvelope", {}).get("name")
    rows = []
    rels = candidate.get("relationships") or candidate.get("proposedRelationships") or []
    for rel in rels:
        target = rel.get("target") or rel.get("targetName") or rel.get("value")
        kind = rel.get("type") or rel.get("relationshipType") or "references"
        if not target:
            continue
        rows.append({
            "relationshipId": stable("rel", f"{cid}|{kind}|{target}"),
            "sourceCandidateId": cid,
            "sourceName": name,
            "relationshipType": kind,
            "targetText": target,
            "targetCanonicalId": None,
            "resolutionState": "unresolved",
            "confidence": rel.get("confidence", 0),
            "provenance": candidate.get("provenance") or candidate.get("canonicalEnvelope", {}).get("provenance") or [],
        })
    return rows


def handoff(candidate: dict[str, Any]) -> dict[str, Any]:
    envelope = candidate.get("canonicalEnvelope") or {}
    cid = candidate.get("candidateId") or envelope.get("id")
    readiness = candidate.get("readinessScore") or candidate.get("readiness", {}).get("score") or 0
    missing = candidate.get("missingFields") or candidate.get("readiness", {}).get("missingFields") or []
    gates = {
        "identityConfirmed": False,
        "sourceVerified": bool(candidate.get("provenance") or envelope.get("provenance")),
        "relationshipsResolved": not bool(candidate.get("relationships") or candidate.get("proposedRelationships")),
        "schemaValidated": False,
        "duplicateResolved": False,
        "designerApproved": False,
        "ownerApproved": False,
    }
    return {
        "format": "multiversal-recovery-handoff",
        "version": "1.0.0",
        "handoffId": stable("handoff", str(cid)),
        "candidateId": cid,
        "sourceGroup": source_group(candidate),
        "readinessScore": readiness,
        "missingFields": missing,
        "recommendedPack": candidate.get("recommendedPack"),
        "canonicalDraft": envelope,
        "recoveredSpec": candidate.get("recoveredSpec") or candidate.get("specializedSpec") or {},
        "relationships": candidate.get("relationships") or candidate.get("proposedRelationships") or [],
        "gates": gates,
        "handoffState": "awaiting-review",
        "authority": "Prepared handoff only. Production Database import requires explicit review and approval.",
    }


def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument("--recovery", type=Path, required=True)
    p.add_argument("--out", type=Path, required=True)
    p.add_argument("--batch-size", type=int, default=50)
    args = p.parse_args()
    args.out.mkdir(parents=True, exist_ok=True)

    candidates = iter_candidates(args.recovery)
    handoffs = [handoff(c) for c in candidates]
    handoffs.sort(key=lambda x: (-float(x.get("readinessScore") or 0), x.get("sourceGroup", ""), x.get("candidateId", "")))
    relationships = [r for c in candidates for r in relationship_rows(c)]

    batches = []
    for i in range(0, len(handoffs), args.batch_size):
        chunk = handoffs[i:i + args.batch_size]
        bid = f"recovery-handoff-{i // args.batch_size + 1:04d}"
        payload = {"format": "multiversal-recovery-handoff-batch", "version": "1.0.0", "batchId": bid, "candidateCount": len(chunk), "handoffs": chunk}
        (args.out / f"{bid}.json").write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
        batches.append({"batchId": bid, "candidateCount": len(chunk)})

    by_source: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for h in handoffs:
        by_source[h["sourceGroup"]].append(h)
    receipts = []
    for group, rows in sorted(by_source.items()):
        ready = sum(1 for r in rows if float(r.get("readinessScore") or 0) >= 76)
        receipts.append({
            "sourceGroup": group,
            "candidateCount": len(rows),
            "readyForReview": ready,
            "completionPercent": round((ready / len(rows) * 100), 2) if rows else 0,
            "relationshipCount": sum(len(r.get("relationships") or []) for r in rows),
            "canonicalizedCount": 0,
            "reviewComplete": False,
        })

    (args.out / "relationship-resolution-queue.json").write_text(json.dumps(relationships, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    (args.out / "source-completion-receipts.json").write_text(json.dumps(receipts, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    summary = {
        "format": "multiversal-recovery-handoff-index",
        "version": "1.0.0",
        "generatedAt": datetime.now(timezone.utc).isoformat(),
        "candidateCount": len(handoffs),
        "readyForReviewCount": sum(1 for h in handoffs if float(h.get("readinessScore") or 0) >= 76),
        "relationshipCount": len(relationships),
        "unresolvedRelationshipCount": len(relationships),
        "sourceGroupCount": len(receipts),
        "batchCount": len(batches),
        "batchSize": args.batch_size,
        "batches": batches,
        "readinessBands": dict(Counter(
            "ready" if float(h.get("readinessScore") or 0) >= 76 else
            "developing" if float(h.get("readinessScore") or 0) >= 50 else "early"
            for h in handoffs
        )),
        "publishedSample": handoffs[:200],
        "authorityNote": "No handoff is canonical until all review gates are satisfied.",
    }
    (args.out / "recovery-handoff-index.json").write_text(json.dumps(summary, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()
