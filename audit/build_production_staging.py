#!/usr/bin/env python3
"""Compile recovery handoffs into non-canonical production staging packets."""
from __future__ import annotations
import argparse, hashlib, json
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path

REQUIRED=("id","objectType","name","status","provenance","spec")

def load(p): return json.loads(p.read_text(encoding="utf-8"))
def sid(v): return hashlib.sha256(v.encode()).hexdigest()[:16]

def rows(root):
 out=[]
 for p in sorted(root.glob("recovery-handoff-*.json")):
  out.extend(load(p).get("handoffs",[]))
 return out

def validate(h):
 d=h.get("canonicalDraft") or {}; blockers=[]; warnings=[]
 for k in REQUIRED:
  if d.get(k) in (None,"",[],{}): blockers.append(f"missing:{k}")
 if h.get("missingFields"): blockers.extend(f"recovery:{x}" for x in h["missingFields"])
 if h.get("relationships"): blockers.append("unresolved-relationships")
 if float(h.get("readinessScore") or 0)<76: blockers.append("readiness-below-76")
 if not h.get("recommendedPack"): warnings.append("pack-unassigned")
 if not (d.get("provenance") or []): blockers.append("missing-provenance")
 return sorted(set(blockers)),sorted(set(warnings))

def main():
 ap=argparse.ArgumentParser(); ap.add_argument("--handoffs",type=Path,required=True); ap.add_argument("--out",type=Path,required=True); ap.add_argument("--batch-size",type=int,default=50); a=ap.parse_args(); a.out.mkdir(parents=True,exist_ok=True)
 staged=[]; blocked=[]
 for h in rows(a.handoffs):
  b,w=validate(h); cid=h.get("candidateId") or "unknown"
  receipt={"receiptId":"stage-"+sid(cid),"candidateId":cid,"readinessScore":h.get("readinessScore",0),"recommendedPack":h.get("recommendedPack"),"blockers":b,"warnings":w,"gates":{"structuralValidation":not b,"relationshipResolution":"unresolved-relationships" not in b,"designerApproval":False,"ownerApproval":False},"authority":"Staging only; never canonical without explicit owner approval."}
  if b: blocked.append(receipt)
  else:
   staged.append({"format":"multiversal-production-staging-record","version":"1.0.0","stagingId":"staging-"+sid(cid),"candidateId":cid,"targetBranch":"legacy-recovery","recommendedPack":h.get("recommendedPack"),"canonicalDraft":h.get("canonicalDraft"),"recoveredSpec":h.get("recoveredSpec",{}),"receipt":receipt})
 batches=[]
 for i in range(0,len(staged),a.batch_size):
  chunk=staged[i:i+a.batch_size]; bid=f"production-stage-{i//a.batch_size+1:04d}"; (a.out/f"{bid}.json").write_text(json.dumps({"format":"multiversal-production-staging-batch","version":"1.0.0","batchId":bid,"recordCount":len(chunk),"records":chunk},indent=2,ensure_ascii=False)+"\n"); batches.append({"batchId":bid,"recordCount":len(chunk)})
 (a.out/"blocked-staging-receipts.json").write_text(json.dumps(blocked,indent=2,ensure_ascii=False)+"\n")
 summary={"format":"multiversal-production-staging-index","version":"1.0.0","generatedAt":datetime.now(timezone.utc).isoformat(),"handoffCount":len(staged)+len(blocked),"stagedCount":len(staged),"blockedCount":len(blocked),"blockerCounts":dict(Counter(x for r in blocked for x in r["blockers"])),"batchCount":len(batches),"batches":batches,"publishedSample":staged[:150],"blockedSample":blocked[:150],"targetBranch":"legacy-recovery","automaticCanonicalWrites":False,"authorityNote":"Production staging is non-canonical and requires designer plus owner approval."}
 (a.out/"production-staging-index.json").write_text(json.dumps(summary,indent=2,ensure_ascii=False)+"\n"); print(json.dumps({k:summary[k] for k in ("handoffCount","stagedCount","blockedCount","batchCount")},indent=2))
if __name__=="__main__": main()
