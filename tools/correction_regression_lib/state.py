from __future__ import annotations
import copy
from pathlib import Path
from .common import *

def validate_correction(item,patterns,controls):
    required={"correction_id","fingerprint","captured_at","source_ref","correction_summary","failure_summary","severity","pattern_ids","control_ids","authority","immediate_correction","privacy","candidate_id","status"}
    require(set(item)==required,"correction fields mismatch")
    require(CORRECTION_ID_RE.fullmatch(item["correction_id"]) is not None,"invalid correction ID")
    require(HEX64_RE.fullmatch(item["fingerprint"]) is not None,"invalid correction fingerprint")
    require(SOURCE_REF_RE.fullmatch(item["source_ref"]) is not None,"invalid correction source_ref")
    compact(item["correction_summary"],"correction summary",400); compact(item["failure_summary"],"failure summary",400)
    require(item["severity"] in {"P0","P1","P2","P3"},"invalid correction severity")
    require(item["status"] in {"proposed","approved","rejected","promoted"},"invalid correction status")
    require(CANDIDATE_ID_RE.fullmatch(item["candidate_id"]) is not None,"invalid candidate link")
    require(set(item["pattern_ids"])<=patterns,"correction references unknown pattern")
    require(set(item["control_ids"])<=controls,"correction references unknown control")
    require(item["authority"]["actor_id"]==OWNER_ID,"correction owner mismatch")
    require(item["privacy"]["raw_transcript_included"] is False and item["privacy"]["minimized"] is True,"correction privacy failed")

def validate_candidate(item,correction,cases):
    required={"candidate_id","correction_id","fingerprint","created_at","status","source_patterns","proposed_case","review","promotion"}
    require(set(item)==required,"candidate fields mismatch")
    require(CANDIDATE_ID_RE.fullmatch(item["candidate_id"]) is not None,"invalid candidate ID")
    require(item["correction_id"]==correction["correction_id"],"candidate/correction link mismatch")
    require(item["fingerprint"]==correction["fingerprint"],"candidate fingerprint mismatch")
    require(item["source_patterns"]==correction["pattern_ids"],"candidate pattern mismatch")
    require(item["status"]==correction["status"],"candidate/correction status mismatch")
    validate_case(item["proposed_case"],"candidate.proposed_case")
    review=item["review"]; promotion=item["promotion"]
    require(set(review)=={"decision","decided_at","reviewer","evidence"},"review fields mismatch")
    require(set(promotion)=={"case_id","promoted_at","evidence"},"promotion fields mismatch")
    if item["status"]=="proposed":
        require(review=={"decision":"pending","decided_at":None,"reviewer":None,"evidence":[]},"proposed candidate has review state")
        require(promotion=={"case_id":None,"promoted_at":None,"evidence":[]},"proposed candidate has promotion state")
    elif item["status"] in {"approved","rejected"}:
        require(review["decision"]==item["status"] and review["reviewer"]==OWNER_ID,"review decision or authority mismatch")
        require(review["decided_at"] and review["evidence"],"review evidence missing")
        require(promotion=={"case_id":None,"promoted_at":None,"evidence":[]},"unpromoted candidate has promotion data")
    else:
        require(review["decision"]=="approved" and review["reviewer"]==OWNER_ID and review["evidence"],"promoted candidate lacks approval")
        case_id=promotion["case_id"]; require(CASE_ID_RE.fullmatch(case_id or "") is not None,"invalid promoted case ID")
        require(promotion["promoted_at"] and promotion["evidence"],"promotion evidence missing")
        require(case_id in cases,"promoted case missing")
        expected={"case_id":case_id,"name":item["proposed_case"]["name"],"source_patterns":item["source_patterns"]}
        for key in ("setup","owner_input","expected_actions","prohibited_actions","pass_condition"): expected[key]=item["proposed_case"][key]
        require(cases[case_id]==expected,"promoted case differs from candidate")

def validate_repository(root:Path):
    patterns,controls=catalogs(root)
    ledger=load_json(root/LEDGER); examples=load_json(root/EXAMPLES)
    base=load_json(root/EVALUATIONS); promoted=load_json(root/PROMOTED_EVALUATIONS)
    extension=load_json(root/CONTROL_EXTENSION); mappings=load_json(root/EVAL_CONTROL_EXTENSION); gaps=load_json(root/GAPS)
    require(ledger.get("schema_version")=="1.0.0" and ledger.get("work_item_id")=="MV-CONT-004","ledger identity mismatch")
    corrections=ledger.get("corrections"); candidates=ledger.get("candidates")
    require(isinstance(corrections,list) and isinstance(candidates,list),"ledger arrays missing")
    ext_controls=extension.get("control_catalog",{}); require(CONTROL_ID in ext_controls,"correction control missing")
    control=ext_controls[CONTROL_ID]; require(control.get("status")=="implemented_in_mv_cont_004","correction control status mismatch")
    artifacts={str(LEDGER),str(INTAKE_SCHEMA),str(CANDIDATE_SCHEMA),str(README),str(PROMOTION_POLICY),str(PROMOTED_EVALUATIONS),str(CONTROL_EXTENSION),str(EVAL_CONTROL_EXTENSION),"tools/correction_regression.py","tools/correction_regression_lib/__init__.py","tools/correction_regression_lib/common.py","tools/correction_regression_lib/state.py",".github/workflows/validate-correction-regression.yml"}
    require(artifacts<=set(control.get("artifacts",[])),"correction control artifacts incomplete")
    controls|=set(ext_controls)
    closure=next((x for x in extension.get("gap_closures",[]) if x.get("gap_id")==GAP_ID),None)
    require(closure and closure.get("status")=="closed" and closure.get("control_id")==CONTROL_ID,"gap closure missing")
    historical=next((x for x in gaps.get("gaps",[]) if x.get("gap_id")==GAP_ID),None)
    require(historical and historical.get("implemented_control_id") is None,"historical gap snapshot changed")
    coverage=next((x for x in extension.get("pattern_coverage",[]) if x.get("pattern_id")==OWNER_PATTERN),None)
    require(coverage and coverage.get("prior_coverage_status")=="partial" and coverage.get("coverage_status")=="enforced","coverage extension invalid")
    require(CONTROL_ID in coverage.get("added_control_ids",[]),"coverage control missing")
    require(promoted.get("schema_version")=="1.0.0" and promoted.get("work_item_id")=="MV-CONT-004","promoted corpus identity mismatch")
    all_cases=base.get("cases",[])+promoted.get("cases",[]); case_ids=[x["case_id"] for x in all_cases]
    require(len(case_ids)==len(set(case_ids)),"duplicate case ID across corpora"); case_map={x["case_id"]:x for x in all_cases}
    mapping_items=mappings.get("cases",[]); mapped=[x.get("case_id") for x in mapping_items]
    require(len(mapped)==len(set(mapped)),"duplicate extension mapping")
    owner_map=next((x for x in mapping_items if x.get("case_id")==OWNER_CASE),None)
    require(owner_map and CONTROL_ID in owner_map.get("control_ids",[]),"owner case mapping missing")
    for item in mapping_items:
        require(item.get("case_id") in case_map,"mapping references unknown case")
        require(CONTROL_ID in item.get("control_ids",[]),"mapping lacks correction control")
    ids=[x.get("correction_id") for x in corrections]; candidate_ids=[x.get("candidate_id") for x in candidates]; fps=[x.get("fingerprint") for x in corrections]
    require(len(ids)==len(set(ids)),"duplicate correction ID"); require(len(candidate_ids)==len(set(candidate_ids)),"duplicate candidate ID"); require(len(fps)==len(set(fps)),"duplicate fingerprint")
    require(len(corrections)==len(candidates),"every correction needs one candidate")
    by_candidate={x["candidate_id"]:x for x in candidates}
    for correction in corrections:
        validate_correction(correction,patterns,controls); require(correction["candidate_id"] in by_candidate,"candidate missing")
        validate_candidate(by_candidate[correction["candidate_id"]],correction,case_map)
    promoted_from_candidates={x["promotion"]["case_id"] for x in candidates if x.get("status")=="promoted"}
    promoted_ids={x["case_id"] for x in promoted.get("cases",[])}
    require(promoted_from_candidates==promoted_ids,"promoted candidate/corpus mismatch")
    for item in examples.get("intakes",[]): validate_intake(item,patterns,controls)
    require(examples.get("intakes"),"correction examples empty")
    for rel in (INTAKE_SCHEMA,CANDIDATE_SCHEMA,README,PROMOTION_POLICY,PROMOTED_EVALUATIONS,CONTROL_EXTENSION,EVAL_CONTROL_EXTENSION):
        require((root/rel).is_file(),f"required artifact missing: {rel}")

def capture(root:Path,input_path:Path):
    patterns,controls=catalogs(root); intake=load_json(input_path); validate_intake(intake,patterns,controls)
    ledger_path=root/LEDGER; ledger=load_json(ledger_path); fp=fingerprint(intake)
    existing=next((x for x in ledger["corrections"] if x["fingerprint"]==fp),None)
    if existing: return existing["correction_id"],existing["candidate_id"],False
    correction_id=stable_id("MV-CORR",fp); candidate_id=stable_id("MV-REG","candidate:"+fp)
    correction={"correction_id":correction_id,"fingerprint":fp,"captured_at":intake["captured_at"],"source_ref":intake["source_ref"],"correction_summary":intake["correction_summary"],"failure_summary":intake["failure_summary"],"severity":intake["severity"],"pattern_ids":intake["pattern_ids"],"control_ids":intake["control_ids"],"authority":intake["authority"],"immediate_correction":intake["immediate_correction"],"privacy":intake["privacy"],"candidate_id":candidate_id,"status":"proposed"}
    candidate={"candidate_id":candidate_id,"correction_id":correction_id,"fingerprint":fp,"created_at":intake["captured_at"],"status":"proposed","source_patterns":intake["pattern_ids"],"proposed_case":intake["proposed_case"],"review":{"decision":"pending","decided_at":None,"reviewer":None,"evidence":[]},"promotion":{"case_id":None,"promoted_at":None,"evidence":[]}}
    ledger["corrections"].append(correction); ledger["candidates"].append(candidate); ledger["updated_at"]=now()
    atomic_write(ledger_path,ledger); validate_repository(root)
    return correction_id,candidate_id,True

def review(root:Path,candidate_id,decision,reviewer,evidence,decided_at=None):
    require(decision in {"approved","rejected"},"invalid review decision"); require(reviewer==OWNER_ID,"only the owner may review")
    require(evidence,"review evidence required"); ledger_path=root/LEDGER; ledger=load_json(ledger_path)
    candidate=next((x for x in ledger["candidates"] if x["candidate_id"]==candidate_id),None)
    require(candidate is not None,"unknown candidate"); require(candidate["status"]=="proposed","only proposed candidates may be reviewed")
    correction=next(x for x in ledger["corrections"] if x["correction_id"]==candidate["correction_id"]); stamp=decided_at or now()
    candidate["status"]=decision; candidate["review"]={"decision":decision,"decided_at":stamp,"reviewer":reviewer,"evidence":evidence}; correction["status"]=decision; ledger["updated_at"]=stamp
    atomic_write(ledger_path,ledger); validate_repository(root)

def promote(root:Path,candidate_id,case_id,evidence,promoted_at=None):
    require(CASE_ID_RE.fullmatch(case_id) is not None,"invalid target case ID"); require(evidence,"promotion evidence required")
    ledger_path=root/LEDGER; promoted_path=root/PROMOTED_EVALUATIONS; mapping_path=root/EVAL_CONTROL_EXTENSION
    ledger=load_json(ledger_path); base=load_json(root/EVALUATIONS); promoted=load_json(promoted_path); mappings=load_json(mapping_path)
    candidate=next((x for x in ledger["candidates"] if x["candidate_id"]==candidate_id),None)
    require(candidate is not None,"unknown candidate"); require(candidate["status"]=="approved","candidate must be owner-approved")
    require(candidate["review"]["reviewer"]==OWNER_ID and candidate["review"]["evidence"],"owner approval missing")
    require(case_id not in {x["case_id"] for x in base["cases"]+promoted["cases"]},"evaluation case already exists")
    correction=next(x for x in ledger["corrections"] if x["correction_id"]==candidate["correction_id"]); stamp=promoted_at or now()
    case={"case_id":case_id,"name":candidate["proposed_case"]["name"],"source_patterns":candidate["source_patterns"]}
    for key in ("setup","owner_input","expected_actions","prohibited_actions","pass_condition"): case[key]=copy.deepcopy(candidate["proposed_case"][key])
    promoted["cases"].append(case); promoted["updated_at"]=stamp
    mappings["cases"].append({"case_id":case_id,"control_ids":sorted(set(correction["control_ids"]+[CONTROL_ID]))}); mappings["updated_at"]=stamp
    candidate["status"]="promoted"; candidate["promotion"]={"case_id":case_id,"promoted_at":stamp,"evidence":evidence}; correction["status"]="promoted"; ledger["updated_at"]=stamp
    old=[ledger_path.read_bytes(),promoted_path.read_bytes(),mapping_path.read_bytes()]
    try:
        atomic_write(promoted_path,promoted); atomic_write(mapping_path,mappings); atomic_write(ledger_path,ledger); validate_repository(root)
    except Exception:
        ledger_path.write_bytes(old[0]); promoted_path.write_bytes(old[1]); mapping_path.write_bytes(old[2]); raise
