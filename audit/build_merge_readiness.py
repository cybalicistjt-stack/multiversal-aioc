#!/usr/bin/env python3
"""Compile acceptance manifests into branch-import plans and merge-readiness receipts.

Outputs are planning artifacts only. They never execute imports or modify Main Canon.
"""
from __future__ import annotations
import argparse, hashlib, json
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


def load(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def stable(prefix: str, value: str) -> str:
    return f"{prefix}-{hashlib.sha256(value.encode('utf-8')).hexdigest()[:16]}"


def entries(root: Path) -> list[dict[str, Any]]:
    out=[]
    for path in sorted(root.glob("canonical-acceptance-*.json")):
        out.extend(load(path).get("entries", []))
    return out


def source_group(entry: dict[str, Any]) -> str:
    provenance=(entry.get("canonicalDraft") or {}).get("provenance") or []
    path=str((provenance[0] if provenance else {}).get("sourcePath") or "unassigned").replace("\\","/")
    parts=[p for p in path.split("/") if p]
    return "/".join(parts[:3]) or "unassigned"


def main() -> None:
    ap=argparse.ArgumentParser()
    ap.add_argument("--acceptance",type=Path,required=True)
    ap.add_argument("--out",type=Path,required=True)
    ap.add_argument("--batch-size",type=int,default=50)
    a=ap.parse_args(); a.out.mkdir(parents=True,exist_ok=True)

    accepted=entries(a.acceptance)
    blockers=load(a.acceptance/"blocker-resolution-queue.json") if (a.acceptance/"blocker-resolution-queue.json").exists() else []
    plans=[]
    for e in accepted:
        cid=e.get("candidateId") or "unknown"
        draft=e.get("canonicalDraft") or {}
        plans.append({
            "format":"multiversal-branch-import-plan-entry",
            "version":"1.0.0",
            "importPlanId":stable("import",cid),
            "acceptanceId":e.get("acceptanceId"),
            "candidateId":cid,
            "targetBranch":e.get("targetBranch","legacy-recovery"),
            "targetPack":e.get("targetPack"),
            "objectId":e.get("objectId"),
            "objectType":e.get("objectType"),
            "name":e.get("name"),
            "contentHash":e.get("contentHash"),
            "sourceGroup":source_group(e),
            "canonicalDraft":draft,
            "importGates":{
                "designerApproved":False,
                "ownerApproved":False,
                "branchCreated":False,
                "preImportHashVerified":False,
                "importExecuted":False,
                "schemaValidationPassed":False,
                "referenceValidationPassed":False,
                "packValidationPassed":False,
                "rollbackSnapshotCreated":False,
            },
            "rollbackPlan":{
                "strategy":"remove imported object version and restore pre-import branch snapshot",
                "requiredSnapshot":True,
                "rollbackTested":False,
            },
            "mergeState":"awaiting-approval",
            "authority":"Plan only; no repository or canonical write is authorized.",
        })

    batches=[]
    for i in range(0,len(plans),a.batch_size):
        chunk=plans[i:i+a.batch_size]; bid=f"branch-import-{i//a.batch_size+1:04d}"
        payload={"format":"multiversal-branch-import-plan-batch","version":"1.0.0","batchId":bid,"targetBranch":"legacy-recovery","entryCount":len(chunk),"entries":chunk}
        (a.out/f"{bid}.json").write_text(json.dumps(payload,indent=2,ensure_ascii=False)+"\n",encoding="utf-8")
        batches.append({"batchId":bid,"entryCount":len(chunk)})

    by_source=defaultdict(list)
    for p in plans: by_source[p["sourceGroup"]].append(p)
    readiness=[]
    for group,rows in sorted(by_source.items()):
        readiness.append({
            "sourceGroup":group,
            "plannedImportCount":len(rows),
            "approvedCount":0,
            "importedCount":0,
            "validatedCount":0,
            "mainCanonReadyCount":0,
            "mergeReadinessPercent":0,
            "mergeGateState":"blocked",
            "requiredChecks":["designer approval","owner approval","branch import","schema validation","reference validation","pack validation","rollback snapshot","post-import smoke tests"],
        })
    (a.out/"source-merge-readiness.json").write_text(json.dumps(readiness,indent=2,ensure_ascii=False)+"\n",encoding="utf-8")

    acceptance_receipts=[]
    for p in plans:
        acceptance_receipts.append({
            "receiptId":stable("receipt",p["candidateId"]),
            "candidateId":p["candidateId"],
            "contentHash":p["contentHash"],
            "targetBranch":p["targetBranch"],
            "preImportState":"not-imported",
            "postImportState":"pending",
            "validationState":"pending",
            "mainCanonEligibility":False,
            "signedByDesigner":False,
            "signedByOwner":False,
        })
    (a.out/"post-import-validation-receipts.json").write_text(json.dumps(acceptance_receipts,indent=2,ensure_ascii=False)+"\n",encoding="utf-8")

    summary={
        "format":"multiversal-main-canon-merge-readiness-index",
        "version":"1.0.0",
        "generatedAt":datetime.now(timezone.utc).isoformat(),
        "acceptanceEntryCount":len(plans),
        "openBlockerCount":len(blockers),
        "importBatchCount":len(batches),
        "sourceGroupCount":len(readiness),
        "targetBranch":"legacy-recovery",
        "packCounts":dict(Counter(p.get("targetPack") or "unassigned" for p in plans)),
        "objectTypeCounts":dict(Counter(p.get("objectType") or "unknown" for p in plans)),
        "publishedPlanSample":plans[:150],
        "publishedReadinessSample":readiness[:150],
        "mergePolicy":{
            "automaticBranchImports":False,
            "automaticMainCanonMerges":False,
            "designerApprovalRequired":True,
            "ownerApprovalRequired":True,
            "postImportValidationRequired":True,
            "rollbackSnapshotRequired":True,
        },
        "authorityNote":"Merge-readiness outputs are non-executing plans and receipts only.",
    }
    (a.out/"merge-readiness-index.json").write_text(json.dumps(summary,indent=2,ensure_ascii=False)+"\n",encoding="utf-8")
    print(json.dumps({k:summary[k] for k in ("acceptanceEntryCount","openBlockerCount","importBatchCount","sourceGroupCount")},indent=2))

if __name__=="__main__": main()
