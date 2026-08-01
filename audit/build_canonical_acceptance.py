#!/usr/bin/env python3
"""Compile production staging into governed acceptance manifests and blocker plans.

Nothing generated here changes canonical content. Import manifests target the
legacy-recovery branch and remain invalid until designer and owner approvals
are recorded.
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


def staged_records(root: Path) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    for path in sorted(root.glob("production-stage-*.json")):
        rows.extend(load(path).get("records", []))
    return rows


def blocker_action(blocker: str) -> dict[str, str]:
    if blocker.startswith("missing:"):
        return {"owner": "content-architect", "action": f"Supply canonical field {blocker.split(':',1)[1]}", "gate": "schema"}
    if blocker.startswith("recovery:"):
        return {"owner": "recovery-reviewer", "action": f"Recover missing content field {blocker.split(':',1)[1]}", "gate": "recovery"}
    if blocker == "unresolved-relationships":
        return {"owner": "relationship-reviewer", "action": "Resolve every proposed relationship to a canonical ID or explicitly reject it", "gate": "relationships"}
    if blocker == "readiness-below-76":
        return {"owner": "content-architect", "action": "Complete structure until readiness reaches the staging threshold", "gate": "readiness"}
    if blocker == "missing-provenance":
        return {"owner": "source-reviewer", "action": "Attach source document and page evidence", "gate": "provenance"}
    return {"owner": "designer", "action": f"Resolve blocker: {blocker}", "gate": "other"}


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--staging", type=Path, required=True)
    parser.add_argument("--out", type=Path, required=True)
    parser.add_argument("--batch-size", type=int, default=50)
    args = parser.parse_args()
    args.out.mkdir(parents=True, exist_ok=True)

    stage_index = load(args.staging / "production-staging-index.json")
    staged = staged_records(args.staging)
    blocked = load(args.staging / "blocked-staging-receipts.json") if (args.staging / "blocked-staging-receipts.json").exists() else []

    manifests: list[dict[str, Any]] = []
    for record in staged:
        draft = record.get("canonicalDraft") or {}
        candidate_id = record.get("candidateId") or draft.get("id") or "unknown"
        manifests.append({
            "format": "multiversal-canonical-import-manifest-entry",
            "version": "1.0.0",
            "acceptanceId": stable("accept", candidate_id),
            "candidateId": candidate_id,
            "stagingId": record.get("stagingId"),
            "targetBranch": record.get("targetBranch", "legacy-recovery"),
            "targetPack": record.get("recommendedPack"),
            "objectId": draft.get("id"),
            "objectType": draft.get("objectType"),
            "name": draft.get("name"),
            "contentHash": hashlib.sha256(json.dumps(draft, sort_keys=True, ensure_ascii=False).encode("utf-8")).hexdigest(),
            "canonicalDraft": draft,
            "acceptanceGates": {
                "stagingValidated": True,
                "duplicateReviewComplete": False,
                "relationshipReviewComplete": True,
                "designerApproved": False,
                "ownerApproved": False,
                "branchImportExecuted": False,
                "postImportValidationPassed": False,
            },
            "acceptanceState": "awaiting-approval",
            "authority": "Manifest entry only. It cannot enter Main Canon without explicit owner approval and post-import validation.",
        })

    batches = []
    for index in range(0, len(manifests), args.batch_size):
        chunk = manifests[index:index + args.batch_size]
        batch_id = f"canonical-acceptance-{index // args.batch_size + 1:04d}"
        payload = {
            "format": "multiversal-canonical-acceptance-batch",
            "version": "1.0.0",
            "batchId": batch_id,
            "targetBranch": "legacy-recovery",
            "entryCount": len(chunk),
            "entries": chunk,
        }
        (args.out / f"{batch_id}.json").write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
        batches.append({"batchId": batch_id, "entryCount": len(chunk)})

    resolution_rows = []
    for receipt in blocked:
        candidate_id = receipt.get("candidateId") or "unknown"
        actions = [blocker_action(blocker) for blocker in receipt.get("blockers", [])]
        resolution_rows.append({
            "resolutionId": stable("resolve", candidate_id),
            "candidateId": candidate_id,
            "readinessScore": receipt.get("readinessScore", 0),
            "recommendedPack": receipt.get("recommendedPack"),
            "blockers": receipt.get("blockers", []),
            "warnings": receipt.get("warnings", []),
            "requiredActions": actions,
            "resolutionState": "open",
            "reviewNotes": "",
        })
    (args.out / "blocker-resolution-queue.json").write_text(json.dumps(resolution_rows, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    by_pack = Counter(entry.get("targetPack") or "unassigned" for entry in manifests)
    by_type = Counter(entry.get("objectType") or "unknown" for entry in manifests)
    blocker_counts = Counter(blocker for row in blocked for blocker in row.get("blockers", []))
    gate_counts = Counter(action["gate"] for row in resolution_rows for action in row.get("requiredActions", []))

    source_closure = []
    source_groups: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for entry in manifests:
        provenance = entry.get("canonicalDraft", {}).get("provenance") or []
        source_path = str((provenance[0] if provenance else {}).get("sourcePath") or "unassigned")
        group = "/".join([p for p in source_path.replace("\\", "/").split("/") if p][:3]) or "unassigned"
        source_groups[group].append(entry)
    for group, rows in sorted(source_groups.items()):
        source_closure.append({
            "sourceGroup": group,
            "acceptedForBranchCount": len(rows),
            "ownerApprovedCount": 0,
            "mainCanonCount": 0,
            "closureState": "open",
            "closureRequirements": [
                "all source candidates reviewed",
                "all blockers resolved or dispositioned",
                "all accepted records imported to legacy-recovery",
                "post-import validation passed",
                "owner signs source closure receipt",
            ],
        })
    (args.out / "source-closure-receipts.json").write_text(json.dumps(source_closure, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    summary = {
        "format": "multiversal-canonical-acceptance-index",
        "version": "1.0.0",
        "generatedAt": datetime.now(timezone.utc).isoformat(),
        "stagingHandoffCount": stage_index.get("handoffCount", len(staged) + len(blocked)),
        "acceptanceCandidateCount": len(manifests),
        "blockedCandidateCount": len(blocked),
        "acceptanceBatchCount": len(batches),
        "targetBranch": "legacy-recovery",
        "packCounts": dict(by_pack),
        "objectTypeCounts": dict(by_type),
        "blockerCounts": dict(blocker_counts),
        "resolutionGateCounts": dict(gate_counts),
        "sourceClosureCount": len(source_closure),
        "publishedAcceptanceSample": manifests[:150],
        "publishedResolutionSample": resolution_rows[:150],
        "approvalPolicy": {
            "designerApprovalRequired": True,
            "ownerApprovalRequired": True,
            "postImportValidationRequired": True,
            "automaticMainCanonWrites": False,
        },
        "authorityNote": "Acceptance manifests prepare controlled branch imports only; they do not approve or modify Main Canon.",
    }
    (args.out / "canonical-acceptance-index.json").write_text(json.dumps(summary, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(json.dumps({k: summary[k] for k in ("acceptanceCandidateCount", "blockedCandidateCount", "acceptanceBatchCount", "sourceClosureCount")}, indent=2))


if __name__ == "__main__":
    main()
