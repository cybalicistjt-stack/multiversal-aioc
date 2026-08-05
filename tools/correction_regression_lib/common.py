from __future__ import annotations
import datetime as dt
import hashlib
import json
import os
import re
import tempfile
from pathlib import Path

CORRECTION_ID_RE=re.compile(r"^MV-CORR-[0-9A-F]{12}$")
CANDIDATE_ID_RE=re.compile(r"^MV-REG-[0-9A-F]{12}$")
CASE_ID_RE=re.compile(r"^MV-EVAL-[0-9]{3}$")
PATTERN_ID_RE=re.compile(r"^MV-(FRIC|SUCC)-[A-Z]+-[0-9]{3}$")
CONTROL_ID_RE=re.compile(r"^C-[A-Z0-9-]+$")
HEX64_RE=re.compile(r"^[0-9a-f]{64}$")
SOURCE_REF_RE=re.compile(r"^opaque:[A-Za-z0-9._:-]{8,160}$")

BASE=Path("governance/ai/interaction-system")
LEDGER=BASE/"corrections/CORRECTION_REGRESSION_LEDGER.json"
EXAMPLES=BASE/"corrections/CORRECTION_INTAKE.examples.json"
INTAKE_SCHEMA=BASE/"corrections/CORRECTION_INTAKE.schema.json"
CANDIDATE_SCHEMA=BASE/"corrections/REGRESSION_CANDIDATE.schema.json"
README=BASE/"corrections/README.md"
PROMOTION_POLICY=BASE/"corrections/PROMOTION_POLICY.md"
EVALUATIONS=BASE/"evaluation/EVALUATION_CASES.json"
PROMOTED_EVALUATIONS=BASE/"evaluation/PROMOTED_EVALUATION_CASES.json"
FRICTION=BASE/"analysis/FAILURE_FRICTION_TAXONOMY.json"
SUCCESS=BASE/"analysis/SUCCESS_PATTERN_CATALOG.json"
MATRIX=BASE/"enforcement/CONTROL_COVERAGE_MATRIX.json"
GAPS=BASE/"enforcement/CONTROL_GAP_REGISTER.json"
CONTROL_EXTENSION=BASE/"corrections/CONTROL_COVERAGE_EXTENSION.json"
EVAL_CONTROL_EXTENSION=BASE/"corrections/EVALUATION_CONTROL_EXTENSION.json"

FORBIDDEN_KEYS={"raw_message","raw_text","raw_transcript","transcript","quote","conversation_title","attachment_content","message_text","full_message"}
OWNER_ID="john-brandon-turner"
CONTROL_ID="C-CORRECTION-REGRESSION-INTAKE"
GAP_ID="MV-GAP-008"
OWNER_PATTERN="MV-SUCC-OWNER-001"
OWNER_CASE="MV-EVAL-015"

class CorrectionError(RuntimeError): pass

def require(condition:bool,message:str)->None:
    if not condition: raise CorrectionError(message)

def now()->str:
    return dt.datetime.now(dt.timezone.utc).replace(microsecond=0).isoformat()

def load_json(path:Path):
    try: return json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError as exc: raise CorrectionError(f"missing file: {path}") from exc
    except json.JSONDecodeError as exc: raise CorrectionError(f"invalid JSON in {path}: {exc}") from exc

def canonical(value)->bytes:
    return json.dumps(value,ensure_ascii=False,sort_keys=True,separators=(",",":")).encode()

def fingerprint(intake:dict)->str:
    durable={"source_ref":intake["source_ref"],"correction_summary":intake["correction_summary"],"failure_summary":intake["failure_summary"],"severity":intake["severity"],"recurrence_material":intake["recurrence_material"],"pattern_ids":sorted(intake["pattern_ids"]),"control_ids":sorted(intake["control_ids"]),"proposed_case":intake["proposed_case"]}
    return hashlib.sha256(canonical(durable)).hexdigest()

def stable_id(prefix:str,seed:str)->str:
    return f"{prefix}-{hashlib.sha256(seed.encode()).hexdigest()[:12].upper()}"

def atomic_write(path:Path,data)->None:
    path.parent.mkdir(parents=True,exist_ok=True)
    payload=json.dumps(data,indent=2,ensure_ascii=False)+"\n"
    fd,temp=tempfile.mkstemp(prefix=f".{path.name}.",suffix=".tmp",dir=path.parent)
    try:
        with os.fdopen(fd,"w",encoding="utf-8",newline="\n") as handle:
            handle.write(payload); handle.flush(); os.fsync(handle.fileno())
        os.replace(temp,path)
    finally:
        if os.path.exists(temp): os.unlink(temp)

def no_raw_fields(value,location="root")->None:
    if isinstance(value,dict):
        for key,child in value.items():
            require(key not in FORBIDDEN_KEYS,f"forbidden raw-content field at {location}.{key}")
            no_raw_fields(child,f"{location}.{key}")
    elif isinstance(value,list):
        for index,child in enumerate(value): no_raw_fields(child,f"{location}[{index}]")

def compact(value,label,maximum)->None:
    require(isinstance(value,str) and value.strip(),f"{label} must be non-empty text")
    require(len(value)<=maximum,f"{label} exceeds {maximum} characters")
    require("\n" not in value and "\r" not in value,f"{label} must be a minimized single-line paraphrase")

def validate_case(case:dict,label:str)->None:
    required={"name","setup","owner_input","expected_actions","prohibited_actions","pass_condition"}
    require(set(case)==required,f"{label} fields mismatch")
    compact(case["name"],f"{label}.name",160); compact(case["setup"],f"{label}.setup",600)
    compact(case["owner_input"],f"{label}.owner_input",300); compact(case["pass_condition"],f"{label}.pass_condition",600)
    for field in ("expected_actions","prohibited_actions"):
        values=case[field]; require(isinstance(values,list) and values,f"{label}.{field} must be a non-empty array")
        require(len(values)==len(set(values)),f"{label}.{field} contains duplicates")
        for index,item in enumerate(values): compact(item,f"{label}.{field}[{index}]",300)

def catalogs(root:Path):
    friction=load_json(root/FRICTION); success=load_json(root/SUCCESS); matrix=load_json(root/MATRIX)
    patterns={item["pattern_id"] for item in friction["patterns"]+success["patterns"]}
    controls=set(matrix["control_catalog"])
    if (root/CONTROL_EXTENSION).is_file(): controls|=set(load_json(root/CONTROL_EXTENSION).get("control_catalog",{}))
    return patterns,controls

def validate_intake(intake:dict,patterns:set[str],controls:set[str])->None:
    required={"schema_version","source_ref","captured_at","correction_summary","failure_summary","severity","recurrence_material","pattern_ids","control_ids","authority","immediate_correction","proposed_case","privacy"}
    require(set(intake)==required,f"intake fields mismatch: {sorted(set(intake)^required)}"); no_raw_fields(intake)
    require(intake["schema_version"]=="1.0.0","intake schema version mismatch")
    require(SOURCE_REF_RE.fullmatch(intake["source_ref"]) is not None,"source_ref must be opaque")
    compact(intake["captured_at"],"captured_at",40); compact(intake["correction_summary"],"correction_summary",400); compact(intake["failure_summary"],"failure_summary",400)
    require(intake["severity"] in {"P0","P1","P2","P3"},"invalid severity")
    require(intake["recurrence_material"] is True,"only material recurrence corrections enter regression intake")
    require(isinstance(intake["pattern_ids"],list) and intake["pattern_ids"],"pattern_ids must be non-empty")
    require(isinstance(intake["control_ids"],list) and intake["control_ids"],"control_ids must be non-empty")
    require(len(intake["pattern_ids"])==len(set(intake["pattern_ids"])),"duplicate pattern IDs")
    require(len(intake["control_ids"])==len(set(intake["control_ids"])),"duplicate control IDs")
    for item in intake["pattern_ids"]:
        require(PATTERN_ID_RE.fullmatch(item) is not None,f"invalid pattern ID: {item}"); require(item in patterns,f"unknown pattern ID: {item}")
    for item in intake["control_ids"]:
        require(CONTROL_ID_RE.fullmatch(item) is not None,f"invalid control ID: {item}"); require(item in controls,f"unknown control ID: {item}")
    authority=intake["authority"]; require(set(authority)=={"actor_id","explicit_correction","evidence"},"authority fields mismatch")
    require(authority["actor_id"]==OWNER_ID and authority["explicit_correction"] is True,"correction lacks explicit owner authority")
    require(isinstance(authority["evidence"],list) and authority["evidence"],"owner correction evidence missing")
    immediate=intake["immediate_correction"]; require(set(immediate)=={"status","evidence"},"immediate_correction fields mismatch")
    require(immediate["status"] in {"applied","blocked"},"immediate correction must be applied or blocked")
    require(isinstance(immediate["evidence"],list) and immediate["evidence"],"immediate correction evidence missing")
    privacy=intake["privacy"]; require(set(privacy)=={"raw_transcript_included","minimized","sensitive_attachment_included"},"privacy fields mismatch")
    require(privacy=={"raw_transcript_included":False,"minimized":True,"sensitive_attachment_included":False},"privacy boundary failed")
    validate_case(intake["proposed_case"],"proposed_case")
