#!/usr/bin/env python3
"""Operations V4 guard for agent development feedback and remote CI acceptance."""
from __future__ import annotations
import argparse, json
from pathlib import Path
from typing import Any
PREFLIGHT_REQUIRED="OPS4.PREFLIGHT_REQUIRED"; PREFLIGHT_SKIPPED="OPS4.PREFLIGHT_SKIPPED"; PREFLIGHT_UNAVAILABLE_UNPROVED="OPS4.PREFLIGHT_UNAVAILABLE_UNPROVED"; DUPLICATE_REMOTE_VALIDATION="OPS4.DUPLICATE_REMOTE_VALIDATION"; SAME_HEAD_PRODUCT_RETRY="OPS4.SAME_HEAD_PRODUCT_RETRY"; REPAIR_EVIDENCE_REQUIRED="OPS4.REPAIR_EVIDENCE_REQUIRED"; INFRA_RETRY_EVIDENCE_REQUIRED="OPS4.INFRA_RETRY_EVIDENCE_REQUIRED"; INFRA_RETRY_EXHAUSTED="OPS4.INFRA_RETRY_EXHAUSTED"; UNRESOLVED_FLAKE="OPS4.UNRESOLVED_FLAKE"; MOCK_ONLY_REAL_BOUNDARY="OPS4.MOCK_ONLY_REAL_BOUNDARY"; INVALID_REQUEST="OPS4.INVALID_REMOTE_VALIDATION_REQUEST"
_REAL_BOUNDARIES={"network","storage","process","authentication","admission","persistence","filesystem","installed_app","cross_platform"}; _PRODUCT_FAILURES={"product","configuration"}; _ACTIVE_REMOTE={"queued","in_progress"}
def _text(v:Any)->str: return v.strip() if isinstance(v,str) else ""
def validate_preflight(p:Any)->list[str]:
    if not isinstance(p,dict): return [PREFLIGHT_REQUIRED]
    s=_text(p.get("status"))
    if s=="skipped": return [PREFLIGHT_SKIPPED]
    if s=="green": return [] if _text(p.get("kind")) and _text(p.get("evidence")) else [PREFLIGHT_REQUIRED]
    if s=="unavailable": return [] if _text(p.get("reason")) and p.get("attempted_capabilities") else [PREFLIGHT_UNAVAILABLE_UNPROVED]
    return [PREFLIGHT_REQUIRED]
def validate_remote_request(r:dict[str,Any])->list[str]:
    e=validate_preflight(r.get("preflight")); h=_text(r.get("candidate_head"))
    if not h: e.append(INVALID_REQUEST); return sorted(set(e))
    p=r.get("prior_remote")
    if isinstance(p,dict):
        ph=_text(p.get("candidate_head")); st=_text(p.get("status")); co=_text(p.get("conclusion")); same=bool(ph) and ph==h
        if same and st in _ACTIVE_REMOTE: e.append(DUPLICATE_REMOTE_VALIDATION)
        if st=="completed" and co=="failure":
            f=_text(p.get("failure_class"))
            if f in _PRODUCT_FAILURES:
                if same: e.append(SAME_HEAD_PRODUCT_RETRY)
                elif not _text(r.get("repair_evidence")): e.append(REPAIR_EVIDENCE_REQUIRED)
            elif f=="infrastructure_transient" and same:
                n=p.get("same_head_infra_retry_count",0)
                if not isinstance(n,int) or n<0: e.append(INVALID_REQUEST)
                elif n>=1: e.append(INFRA_RETRY_EXHAUSTED)
                elif not _text(r.get("infra_retry_evidence")): e.append(INFRA_RETRY_EVIDENCE_REQUIRED)
            elif f=="flaky_unknown":
                if same:
                    n=p.get("same_head_flake_retry_count",0)
                    if not isinstance(n,int) or n<0: e.append(INVALID_REQUEST)
                    elif n>=1 or not _text(r.get("flake_classification_evidence")): e.append(UNRESOLVED_FLAKE)
                elif not _text(r.get("repair_evidence")): e.append(REPAIR_EVIDENCE_REQUIRED)
            elif f not in _PRODUCT_FAILURES|{"infrastructure_transient","flaky_unknown"}: e.append(INVALID_REQUEST)
    return sorted(set(e))
def validate_acceptance_evidence(*,boundary_kind:str,evidence_kinds:list[str]|tuple[str,...]|set[str])->list[str]:
    b=_text(boundary_kind); k={_text(x) for x in evidence_kinds if _text(x)}
    if b not in _REAL_BOUNDARIES: return []
    independent={"existing_regression","real_integration","deterministic_system_receipt","separate_evaluator","installed_runtime","cross_platform_gate","real_boundary_test"}
    return [] if k.intersection(independent) else [MOCK_ONLY_REAL_BOUNDARY]
def main()->int:
    p=argparse.ArgumentParser();p.add_argument("request");p.add_argument("--boundary-kind");p.add_argument("--evidence-kind",action="append",default=[]);a=p.parse_args();r=json.loads(Path(a.request).read_text(encoding="utf-8"));e=validate_remote_request(r)
    if a.boundary_kind:e.extend(validate_acceptance_evidence(boundary_kind=a.boundary_kind,evidence_kinds=a.evidence_kind))
    e=sorted(set(e));print(json.dumps({"status":"FAIL" if e else "PASS","errors":e},sort_keys=True));return 1 if e else 0
if __name__=="__main__": raise SystemExit(main())
