#!/usr/bin/env python3
"""Dependency-free Multiversal continuity state manager."""
from __future__ import annotations
import argparse, datetime as dt, hashlib, json, re, sys
from pathlib import Path

STATUSES={"started","in_progress","validation_failed","blocked_non_owner","blocked_owner","ready_for_review","completed_verified","superseded"}
EVIDENCE={"commit","pull_request","review","ci_run","merge","artifact","checksum","file","issue_comment","owner_decision"}
PROMPT=("Continue Multiversal from the canonical repositories. Follow cybalicistjt-stack/multiversal-aioc/"
"governance/ai/MULTIVERSAL_NEW_CONVERSATION_BOOTSTRAP.md, recover the latest verified active-work checkpoint "
"and branch, and resume the exact unfinished operation; never assume started or in-progress work is complete.")
POINTER=Path("governance/ai/runtime/CURRENT_WORK_POINTER.json")
STATUS=Path("governance/ai/runtime/CURRENT_IMPLEMENTATION_STATUS.json")
INDEX=Path("governance/ai/runtime/ROADMAP_INDEX.json")
PROMPT_PATH=Path("governance/ai/MULTIVERSAL_STATIC_RESTART_PROMPT.txt")
BOOTSTRAP=Path("governance/ai/MULTIVERSAL_NEW_CONVERSATION_BOOTSTRAP.md")
FOUNDATION=Path("governance/ai/interaction-system/foundation/v0.1.0")
REFERENCE=Path("governance/ai/interaction-system/FOUNDATION_PACKAGE_REFERENCE.json")
TESTS=Path("governance/ai/interaction-system/CONTINUITY_ACCEPTANCE_TESTS.md")

class Error(RuntimeError): pass

def need(ok,msg):
    if not ok: raise Error(msg)
def now(): return dt.datetime.now(dt.timezone.utc).replace(microsecond=0).isoformat()
def read(path):
    try: return json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError as e: raise Error(f"missing required file: {path}") from e
    except json.JSONDecodeError as e: raise Error(f"invalid JSON in {path}: {e}") from e
def write(path,data):
    path.parent.mkdir(parents=True,exist_ok=True); path.write_text(json.dumps(data,indent=2,ensure_ascii=False)+"\n",encoding="utf-8")
def keys(data,required,label):
    missing=sorted(set(required)-set(data)); need(not missing,f"{label} missing keys: {', '.join(missing)}")
def digest(path): return hashlib.sha256(path.read_bytes()).hexdigest()
def cp_path(root,entry): return root/entry["checkpoint_path"]

def validate_checkpoint(cp,label):
    keys(cp,{"schema_version","revision","work_item_id","attempt_id","track","repository","branch","status","started_at","updated_at","objective","last_verified_action","active_substep","next_action","expected_remote_head","completion_gate","validation","unresolved_failures","owner_decision_required","evidence","roadmap_projection_pending"},label)
    need(cp["schema_version"]=="1.0.0",f"{label}: bad schema version")
    need(isinstance(cp["revision"],int) and cp["revision"]>=1,f"{label}: bad revision")
    need(cp["status"] in STATUSES,f"{label}: bad status")
    need(re.fullmatch(r"[^/]+/[^/]+",cp["repository"]) is not None,f"{label}: bad repository")
    for item in cp["evidence"]:
        keys(item,{"kind","value"},f"{label} evidence"); need(item["kind"] in EVIDENCE and item["value"],f"{label}: bad evidence")
    gate=cp["completion_gate"]; keys(gate,{"required_evidence_kinds","required_validation_commands","owner_approval_required"},f"{label} gate")
    if cp["status"]=="completed_verified":
        need(cp.get("completed_at"),f"{label}: completed_at required")
        need(cp.get("active_substep") is None,f"{label}: active_substep must be null")
        need(not cp["unresolved_failures"] and not cp["owner_decision_required"],f"{label}: unresolved completion state")
        work_tokens=(cp["work_item_id"],cp["attempt_id"])
        scoped_kinds={x["kind"] for x in cp["evidence"] if any(token in x["value"] for token in work_tokens)}
        missing=set(gate["required_evidence_kinds"])-scoped_kinds
        need(not missing,f"{label}: completion evidence missing {sorted(missing)}")
        validations={x["command"]:x["status"] for x in cp["validation"]}
        pending=[x for x in gate["required_validation_commands"] if validations.get(x)!="passed"]
        need(not pending,f"{label}: completion validations not passed {pending}")
        if gate["owner_approval_required"]: need("owner_decision" in scoped_kinds,f"{label}: owner approval missing")
    else:
        need(cp.get("completed_at") in (None,""),f"{label}: non-complete item has completed_at")
        need(cp.get("active_substep") not in (None,""),f"{label}: unfinished item lacks active_substep")

def validate_pointer(root):
    p=read(root/POINTER); keys(p,{"schema_version","updated_at","canonical_bootstrap","static_restart_prompt","primary_attempt_id","selection_reason","active_attempts","deferred_tracks"},"pointer")
    need(p["schema_version"]=="1.0.0","bad pointer schema")
    need(p["canonical_bootstrap"]==str(BOOTSTRAP) and p["static_restart_prompt"]==str(PROMPT_PATH),"pointer path mismatch")
    attempts=p["active_attempts"]; need(attempts,"pointer has no attempts")
    ids=[x["attempt_id"] for x in attempts]; need(len(ids)==len(set(ids)) and p["primary_attempt_id"] in ids,"pointer attempt identity conflict")
    need(sum(bool(x.get("owner_selected")) for x in attempts)<=1,"multiple owner-selected attempts")
    checkpoints={}
    for entry in attempts:
        keys(entry,{"work_item_id","attempt_id","track","priority","owner_selected","repository","branch","checkpoint_path","status","updated_at","roadmap_projection_pending"},"pointer attempt")
        cp=read(cp_path(root,entry)); validate_checkpoint(cp,f"checkpoint {entry['attempt_id']}")
        for field in ("work_item_id","attempt_id","track","repository","branch","status","updated_at","roadmap_projection_pending"):
            need(cp[field]==entry[field],f"pointer/checkpoint mismatch: {entry['attempt_id']} {field}")
        checkpoints[entry["attempt_id"]]=cp
    deferred=[(x["track"],x["next_work_item_id"]) for x in p["deferred_tracks"]]
    need(len(deferred)==len(set(deferred)),"duplicate deferred track")
    return p,checkpoints

def build_status(p,c,stamp=None):
    cp=c[p["primary_attempt_id"]]
    return {"schema_version":"1.0.0","generated_at":stamp or now(),"source_pointer":str(POINTER),"primary":{
        "work_item_id":cp["work_item_id"],"attempt_id":cp["attempt_id"],"track":cp["track"],"repository":cp["repository"],"branch":cp["branch"],"status":cp["status"],"active_substep":cp.get("active_substep"),"next_action":cp["next_action"],"latest_pushed_commit":cp.get("latest_pushed_commit"),"pull_request":cp.get("pull_request"),"owner_decision_required":cp["owner_decision_required"],"unresolved_failures":cp["unresolved_failures"],"roadmap_projection_pending":cp["roadmap_projection_pending"]},
        "active_attempt_count":sum(x["status"] not in {"completed_verified","superseded"} for x in p["active_attempts"]),"deferred_track_count":len(p["deferred_tracks"])}

def validate_foundation(root):
    base=root/FOUNDATION; manifest=read(base/"MANIFEST.json"); ref=read(root/REFERENCE)
    need(ref.get("package_id")==manifest.get("package_id"),"foundation reference mismatch")
    omitted={x["name"]:x for x in ref.get("not_published",[])}
    sums={line.split(None,1)[1]:line.split(None,1)[0] for line in (base/"SHA256SUMS.txt").read_text().splitlines() if line.strip()}
    for item in manifest["files"]:
        path=base/item["name"]
        if not path.exists():
            x=omitted.get(item["name"]); need(x and x.get("sha256")==item["sha256"] and x.get("bytes")==item["bytes"] and x.get("reason"),f"unrecorded foundation omission: {item['name']}"); continue
        need(path.stat().st_size==item["bytes"] and digest(path)==item["sha256"] and sums.get(item["name"])==item["sha256"],f"foundation integrity mismatch: {item['name']}")
    counts=manifest["conversation_counts"]; source=ref["source_counts"]
    need((source["conversations"],source["messages"],source["user_messages"],source["assistant_messages"])==(counts["total"],counts["messages"],counts["user_messages"],counts["assistant_messages"]),"foundation counts mismatch")

def validate_all(root):
    text=(root/PROMPT_PATH).read_text(encoding="utf-8"); need(text.rstrip("\n")==PROMPT and "\n" not in text.rstrip("\n"),"static prompt changed")
    need((root/BOOTSTRAP).is_file(),"bootstrap missing")
    validate_foundation(root)
    tests=(root/TESTS).read_text(encoding="utf-8")
    for test_id in [*(f"CONT-{i:03d}" for i in range(1,19)),*(f"PERF-{i:03d}" for i in range(1,5))]: need(test_id in tests,f"acceptance test missing: {test_id}")
    p,c=validate_pointer(root); idx=read(root/INDEX); ids=[x["work_item_id"] for x in idx["entries"]]
    need(len(ids)==len(set(ids)),"duplicate roadmap index item")
    required={x["work_item_id"] for x in p["active_attempts"]}|{x["next_work_item_id"] for x in p["deferred_tracks"]}
    need(required<=set(ids),f"roadmap index missing {sorted(required-set(ids))}")
    stored=read(root/STATUS); need(stored==build_status(p,c,stored.get("generated_at")),"compact status is stale")

def refresh(root):
    p,c=validate_pointer(root); write(root/STATUS,build_status(p,c))
def find(p,attempt):
    for x in p["active_attempts"]:
        if x["attempt_id"]==attempt:return x
    raise Error(f"unknown attempt_id: {attempt}")
def update(args,root):
    p=read(root/POINTER); entry=find(p,args.attempt_id); path=cp_path(root,entry); cp=read(path)
    need(cp["revision"]==args.expected_revision,f"revision conflict: expected {args.expected_revision}, current {cp['revision']}")
    for name in ("status","next_action","last_verified_action","latest_pushed_commit","pull_request","completed_at"):
        value=getattr(args,name,None)
        if value is not None: cp[name]=value
    if args.active_substep is not None: cp["active_substep"]=None if args.active_substep=="-" else args.active_substep
    if args.latest_pushed_commit is not None: cp["expected_remote_head"]=args.latest_pushed_commit
    if args.add_completed_substep: cp.setdefault("completed_substeps",[]).extend(args.add_completed_substep)
    if args.add_failure: cp["unresolved_failures"].extend(args.add_failure)
    if args.clear_failures: cp["unresolved_failures"]=[]
    for raw in args.add_evidence or []:
        kind,sep,value=raw.partition(":"); need(sep and kind in EVIDENCE and value,f"bad evidence: {raw}"); cp["evidence"].append({"kind":kind,"value":value})
    if args.validation_status:
        command,state,evidence=args.validation_status; need(state in {"not_run","passed","failed"},"bad validation state")
        record=next((x for x in cp["validation"] if x["command"]==command),None)
        if record: record.update(status=state,evidence=None if evidence=="-" else evidence)
        else: cp["validation"].append({"command":command,"status":state,"evidence":None if evidence=="-" else evidence})
    if args.roadmap_projection_pending is not None: cp["roadmap_projection_pending"]=args.roadmap_projection_pending=="true"
    cp["revision"]+=1; cp["updated_at"]=now(); validate_checkpoint(cp,f"checkpoint {cp['attempt_id']}"); write(path,cp)
    entry.update(status=cp["status"],updated_at=cp["updated_at"],roadmap_projection_pending=cp["roadmap_projection_pending"]); p["updated_at"]=cp["updated_at"]
    write(root/POINTER,p); refresh(root)
def start(args,root):
    p=read(root/POINTER); need(not any(x["attempt_id"]==args.attempt_id for x in p["active_attempts"]),f"attempt already exists: {args.attempt_id}")
    stamp=now(); rel=Path("governance/ai/work-state")/f"{args.attempt_id}.json"; need(not (root/rel).exists(),f"checkpoint exists: {rel}")
    cp={"schema_version":"1.0.0","revision":1,"work_item_id":args.work_item_id,"attempt_id":args.attempt_id,"track":args.track,"repository":args.repository,"branch":args.branch,"status":"started","started_at":stamp,"updated_at":stamp,"completed_at":None,"base_commit":args.base_commit,"latest_pushed_commit":None,"expected_remote_head":args.base_commit,"pull_request":None,"objective":args.objective,"last_verified_action":"Attempt created by continuity_state.py.","active_substep":args.active_substep,"completed_substeps":[],"next_action":args.next_action,"changed_paths":[],"completion_gate":{"required_evidence_kinds":args.required_evidence,"required_validation_commands":args.required_validation,"owner_approval_required":args.owner_approval_required},"validation":[{"command":x,"status":"not_run","evidence":None} for x in args.required_validation],"unresolved_failures":[],"owner_decision_required":False,"evidence":[],"roadmap_projection_pending":True,"notes":[]}
    validate_checkpoint(cp,args.attempt_id); write(root/rel,cp)
    p["active_attempts"].append({"work_item_id":args.work_item_id,"attempt_id":args.attempt_id,"track":args.track,"priority":args.priority,"owner_selected":args.owner_selected,"repository":args.repository,"branch":args.branch,"checkpoint_path":str(rel),"status":"started","updated_at":stamp,"roadmap_projection_pending":True})
    if args.make_primary:p["primary_attempt_id"]=args.attempt_id;p["selection_reason"]=args.selection_reason
    p["updated_at"]=stamp; write(root/POINTER,p); refresh(root)
def select(args,root):
    p=read(root/POINTER); find(p,args.attempt_id)
    for x in p["active_attempts"]:x["owner_selected"]=x["attempt_id"]==args.attempt_id and args.owner_selected
    p["primary_attempt_id"]=args.attempt_id;p["selection_reason"]=args.reason;p["updated_at"]=now();write(root/POINTER,p);refresh(root)

def cli():
    a=argparse.ArgumentParser();a.add_argument("--root",default=".");s=a.add_subparsers(dest="cmd",required=True);s.add_parser("validate");s.add_parser("refresh-status")
    u=s.add_parser("update");u.add_argument("--attempt-id",required=True);u.add_argument("--expected-revision",type=int,required=True);u.add_argument("--status",choices=sorted(STATUSES));u.add_argument("--active-substep");u.add_argument("--next-action");u.add_argument("--last-verified-action");u.add_argument("--latest-pushed-commit");u.add_argument("--pull-request",type=int);u.add_argument("--completed-at");u.add_argument("--add-completed-substep",action="append");u.add_argument("--add-failure",action="append");u.add_argument("--clear-failures",action="store_true");u.add_argument("--add-evidence",action="append");u.add_argument("--validation-status",nargs=3);u.add_argument("--roadmap-projection-pending",choices=("true","false"))
    n=s.add_parser("start")
    for x in ("work_item_id","attempt_id","track","repository","branch","objective","active_substep","next_action"):n.add_argument("--"+x.replace("_","-"),dest=x,required=True)
    n.add_argument("--base-commit");n.add_argument("--priority",type=int,default=100);n.add_argument("--required-evidence",action="append",default=[]);n.add_argument("--required-validation",action="append",default=[]);n.add_argument("--owner-approval-required",action="store_true");n.add_argument("--owner-selected",action="store_true");n.add_argument("--make-primary",action="store_true");n.add_argument("--selection-reason",default="Selected by continuity_state.py.")
    q=s.add_parser("select-primary");q.add_argument("--attempt-id",required=True);q.add_argument("--reason",required=True);q.add_argument("--owner-selected",action="store_true")
    return a.parse_args()
def main():
    args=cli();root=Path(args.root).resolve()
    try:
        if args.cmd=="validate":validate_all(root);print("Conversation continuity validation: PASS")
        elif args.cmd=="refresh-status":refresh(root);print(f"Refreshed {STATUS}")
        elif args.cmd=="update":update(args,root);print(f"Updated checkpoint {args.attempt_id}")
        elif args.cmd=="start":start(args,root);print(f"Started checkpoint {args.attempt_id}")
        else:select(args,root);print(f"Selected primary checkpoint {args.attempt_id}")
        return 0
    except (Error,OSError) as e:print(f"Conversation continuity error: {e}",file=sys.stderr);return 1
if __name__=="__main__":raise SystemExit(main())
