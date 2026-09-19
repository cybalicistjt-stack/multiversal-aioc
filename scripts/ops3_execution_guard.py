#!/usr/bin/env python3
"""Operations V3 execution response, progress and conformance guard."""
from __future__ import annotations
import argparse, json
from copy import deepcopy
from pathlib import Path
from typing import Any
NONTERMINAL="OPS3.NONTERMINAL_RESPONSE"; MULTI_CONTINUE="OPS3.MULTI_CONTINUE_UNRECORDED"; STALL_NUDGE="OPS3.STALL_NUDGE_UNRECORDED"; INVALID_BLOCKER="OPS3.INVALID_BLOCKER"; NO_MATERIAL_PROGRESS="OPS3.NO_MATERIAL_PROGRESS"; INVALID_PROGRESS_RECEIPT="OPS3.INVALID_PROGRESS_RECEIPT"
_ALLOWED_BLOCKERS={"owner_only","external_blocker"}; _ALLOWED_TERMINAL_REASONS={"completed",*_ALLOWED_BLOCKERS}
def _guard(c): return c.get("execution_guard",{}) if isinstance(c.get("execution_guard",{}),dict) else {}
def _conformance(c): return c.get("execution_conformance",{}) if isinstance(c.get("execution_conformance",{}),dict) else {}
def _violations(c):
    raw=_conformance(c).get("policy_violations",[]); return {str(v) for v in raw} if isinstance(raw,list) else set()
def _valid_stop_reason(v):
    return isinstance(v,dict) and v.get("kind") in _ALLOWED_TERMINAL_REASONS and isinstance(v.get("evidence"),str) and bool(v["evidence"].strip())
def observe_owner_execution_command(checkpoint: dict[str,Any])->dict[str,Any]:
    r=deepcopy(checkpoint); g=r.setdefault("execution_guard",{}); c=r.setdefault("execution_conformance",{"status":"in_progress","policy_violations":[]}); violations=c.setdefault("policy_violations",[])
    seq=g.get("material_progress_seq",0); turns=g.get("continue_turns",0); prior=g.get("progress_at_last_owner_command")
    if not isinstance(seq,int) or seq<0 or not isinstance(turns,int) or turns<0: raise ValueError(INVALID_PROGRESS_RECEIPT)
    if turns>0 and prior==seq:
        g["no_progress_cycles"]=int(g.get("no_progress_cycles",0))+1; g["active_stall"]=True
        if NO_MATERIAL_PROGRESS not in violations: violations.append(NO_MATERIAL_PROGRESS)
        c["status"]="stalled_recovery_required"
    g["continue_turns"]=turns+1; g["progress_at_last_owner_command"]=seq; g["terminal_response_allowed"]=False; g["stop_reason"]=None
    return r
def record_material_progress(checkpoint: dict[str,Any],*,kind:str,evidence:str)->dict[str,Any]:
    r=deepcopy(checkpoint); g=r.setdefault("execution_guard",{}); kind,evidence=kind.strip(),evidence.strip()
    if not kind or not evidence: raise ValueError(INVALID_PROGRESS_RECEIPT)
    seq=g.get("material_progress_seq",0)
    if not isinstance(seq,int) or seq<0: raise ValueError(INVALID_PROGRESS_RECEIPT)
    seq+=1; g["material_progress_seq"]=seq; g["last_material_progress"]={"seq":seq,"kind":kind,"evidence":evidence}; g["active_stall"]=False; return r
def validate_progress_receipt(checkpoint):
    g=_guard(checkpoint); keys={"material_progress_seq","progress_at_last_owner_command","no_progress_cycles","last_material_progress","active_stall"}
    if not keys.intersection(g): return []
    errors=[]; seq=g.get("material_progress_seq"); observed=g.get("progress_at_last_owner_command"); cycles=g.get("no_progress_cycles",0); last=g.get("last_material_progress")
    if not isinstance(seq,int) or seq<0 or not isinstance(observed,int) or observed<0 or observed>seq: errors.append(INVALID_PROGRESS_RECEIPT)
    if not isinstance(cycles,int) or cycles<0: errors.append(INVALID_PROGRESS_RECEIPT)
    if seq and (not isinstance(last,dict) or last.get("seq")!=seq or not str(last.get("evidence","")).strip()): errors.append(INVALID_PROGRESS_RECEIPT)
    if cycles>0 and NO_MATERIAL_PROGRESS not in _violations(checkpoint): errors.append(NO_MATERIAL_PROGRESS)
    return sorted(set(errors))
def validate_terminal_response(checkpoint):
    errors=[]; status=checkpoint.get("status"); g=_guard(checkpoint); allowed=g.get("terminal_response_allowed") is True; reason=g.get("stop_reason")
    if status=="in_progress":
        if not allowed: errors.append(NONTERMINAL)
        elif not _valid_stop_reason(reason) or reason.get("kind") not in _ALLOWED_BLOCKERS: errors.append(INVALID_BLOCKER)
    elif status=="completed_verified":
        if not allowed or not _valid_stop_reason(reason) or reason.get("kind")!="completed": errors.append(NONTERMINAL)
    elif status=="selected_not_started":
        if g.get("continue_turns",0): errors.append(NONTERMINAL)
    else: errors.append(NONTERMINAL)
    return errors
def validate_execution_conformance(checkpoint):
    errors=[]; g=_guard(checkpoint); violations=_violations(checkpoint); cs=_conformance(checkpoint).get("status"); ct=g.get("continue_turns",0); sn=g.get("stall_nudges",0)
    if not isinstance(ct,int) or ct<0: errors.append(MULTI_CONTINUE)
    elif ct>1 and MULTI_CONTINUE not in violations and cs in {"completed_verified","conforming"}: errors.append(MULTI_CONTINUE)
    if not isinstance(sn,int) or sn<0: errors.append(STALL_NUDGE)
    elif sn>0 and STALL_NUDGE not in violations and cs in {"completed_verified","conforming"}: errors.append(STALL_NUDGE)
    errors.extend(validate_progress_receipt(checkpoint)); return sorted(set(errors))
def validate_checkpoint(checkpoint,*,terminal_response=False):
    errors=validate_execution_conformance(checkpoint)
    if terminal_response: errors.extend(validate_terminal_response(checkpoint))
    return sorted(set(errors))
def main():
    p=argparse.ArgumentParser(); p.add_argument("checkpoint"); p.add_argument("--terminal-response",action="store_true"); a=p.parse_args()
    c=json.loads(Path(a.checkpoint).read_text(encoding="utf-8")); errors=validate_checkpoint(c,terminal_response=a.terminal_response); print(json.dumps({"status":"FAIL" if errors else "PASS","errors":errors},sort_keys=True)); return 1 if errors else 0
if __name__=="__main__": raise SystemExit(main())
