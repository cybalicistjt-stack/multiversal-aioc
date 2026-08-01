#!/usr/bin/env python3
"""Build non-executing owner-review packets and final source-closure certificates."""
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

def plans(root: Path) -> list[dict[str, Any]]:
    out=[]
    for path in sorted(root.glob("branch-import-*.json")):
        out.extend(load(path).get("entries", []))
    return out

def main() -> None:
    ap=argparse.ArgumentParser(); ap.add_argument("--merge-readiness",type=Path,required=True); ap.add_argument("--out",type=Path,required=True); ap.add_argument("--batch-size",type=int,default=50)
    a=ap.parse_args(); a.out.mkdir(parents=True,exist_ok=True)
    index=load(a.merge_readiness/"merge-readiness-index.json")
    rows=plans(a.merge_readiness)
    source_receipts=load(a.merge_readiness/"source-merge-readiness.json") if (a.merge_readiness/"source-merge-readiness.json").exists() else []
    review=[]
    for row in rows:
        cid=row.get("candidateId") or "unknown"
        review.append({
            "format":"multiversal-owner-review-packet",
            "version":"1.0.0",
            "ownerReviewId":stable("owner-review",cid),
            "candidateId":cid,
            "name":row.get("name"),
            "objectType":row.get("objectType"),
            "targetPack":row.get("targetPack"),
            "sourceGroup":row.get("sourceGroup"),
            "contentHash":row.get("contentHash"),
            "canonicalDraft":row.get("canonicalDraft"),
            "decision":"pending",
            "decisionOptions":["approve-for-legacy-recovery","request-changes","reject","defer"],
            "requiredOwnerChecks":["identity is correct","source evidence is sufficient","object type is correct","duplicate risk is resolved","relationships are acceptable","pack placement is acceptable"],
            "signatures":{"designer":None,"owner":None},
            "mainCanonAuthorization":False,
            "authority":"Owner-review packet only. Approval permits branch import review, not Main Canon merge."
        })
    batches=[]
    for i in range(0,len(review),a.batch_size):
        chunk=review[i:i+a.batch_size]; bid=f"owner-review-{i//a.batch_size+1:04d}"
        (a.out/f"{bid}.json").write_text(json.dumps({"format":"multiversal-owner-review-batch","version":"1.0.0","batchId":bid,"entryCount":len(chunk),"entries":chunk},indent=2,ensure_ascii=False)+"\n",encoding="utf-8")
        batches.append({"batchId":bid,"entryCount":len(chunk)})
    decisions=[{"ownerReviewId":r["ownerReviewId"],"candidateId":r["candidateId"],"decision":"pending","notes":"","decidedAt":None,"ownerSignature":None} for r in review]
    (a.out/"merge-decision-ledger.json").write_text(json.dumps(decisions,indent=2,ensure_ascii=False)+"\n",encoding="utf-8")
    closure=[]
    by_group=defaultdict(list)
    for r in review: by_group[r.get("sourceGroup") or "unassigned"].append(r)
    for group,group_rows in sorted(by_group.items()):
        closure.append({"sourceGroup":group,"candidateCount":len(group_rows),"approvedForBranchCount":0,"validatedOnBranchCount":0,"mainCanonMergedCount":0,"closureState":"open","ownerSigned":False,"closureCertificateId":stable("source-close",group),"closureRequirements":["all candidates dispositioned","all accepted records validated on legacy-recovery","all blockers closed or explicitly waived","source coverage reviewed","owner signs closure certificate"]})
    (a.out/"final-source-closure-certificates.json").write_text(json.dumps(closure,indent=2,ensure_ascii=False)+"\n",encoding="utf-8")
    summary={"format":"multiversal-owner-review-index","version":"1.0.0","generatedAt":datetime.now(timezone.utc).isoformat(),"reviewPacketCount":len(review),"reviewBatchCount":len(batches),"sourceClosureCertificateCount":len(closure),"openBlockerCount":index.get("openBlockerCount",0),"targetBranch":index.get("targetBranch","legacy-recovery"),"objectTypeCounts":dict(Counter(r.get("objectType") or "unknown" for r in review)),"packCounts":dict(Counter(r.get("targetPack") or "unassigned" for r in review)),"publishedReviewSample":review[:150],"publishedClosureSample":closure[:150],"releaseGate":{"technicalReadinessRequired":True,"designerApprovalRequired":True,"ownerApprovalRequired":True,"branchValidationRequired":True,"sourceClosureRequired":True,"automaticMainCanonMerge":False},"authorityNote":"Owner review can authorize controlled branch work only; Main Canon merge remains a separate explicit decision."}
    (a.out/"owner-review-index.json").write_text(json.dumps(summary,indent=2,ensure_ascii=False)+"\n",encoding="utf-8")
    print(json.dumps({k:summary[k] for k in ("reviewPacketCount","reviewBatchCount","sourceClosureCertificateCount","openBlockerCount")},indent=2))

if __name__=="__main__": main()
