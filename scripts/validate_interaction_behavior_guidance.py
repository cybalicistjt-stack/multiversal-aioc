#!/usr/bin/env python3
"""Validate Multiversal interaction behavior-guidance hardening."""
from __future__ import annotations
import argparse,json,sys
from pathlib import Path
from typing import Any

ARCHIVE_SHA="f0f2ae22cfc434c93c209a6c366fc436b0930c44456635e2aef118682d54dea7"
SUPP_ID="MV-CONT-SUPP-2026-08-27-001"
BASE=Path("governance/ai/interaction-system")
SUPP=BASE/"analysis/INTERACTION_ARCHIVE_SUPPLEMENT_2026-08-27.json"
SOURCE=BASE/"analysis/SOURCE_CORPUS_REFERENCE.json"
REPORT=BASE/"analysis/BEHAVIOR_GUIDANCE_REFRESH_2026-08-27.md"
BOOT=Path("governance/ai/MULTIVERSAL_NEW_CONVERSATION_BOOTSTRAP.md")
CONTRACT=BASE/"OWNER_AI_INTERACTION_CONTRACT.md"
TESTS=BASE/"CONTINUITY_ACCEPTANCE_TESTS.md"
PROMOTED=BASE/"evaluation/PROMOTED_EVALUATION_CASES.json"
LEDGER=BASE/"corrections/CORRECTION_REGRESSION_LEDGER.json"
CONTROLS=BASE/"corrections/CONTROL_COVERAGE_EXTENSION.json"
MAP=BASE/"corrections/EVALUATION_CONTROL_EXTENSION.json"

SOURCES={
"supp-001":("a684ed5661905760f0d6ce9b4a501d7975cd284070de73642c403dc47710848a",6,3,3),
"supp-002":("f8f136aa5e97093c34df1e1f50bd508e6847607e4cdf1546bbbda66199324dda",4,2,2),
"supp-003":("6e93404f99b2a99b9c1d885abaedaf800886dd903b53ad8ccc348c4151095c2d",4,2,2),
"supp-004":("a2a113ff4fc4bb75086379555e48a465d55a34fea76a19b63a044db9c01ac7c4",1,1,0),
"supp-005":("2888406865d070ced0b66036accd1fea39697fac8cffefd95c757ba67b8499de",0,0,0),
"supp-006":("2a35ed9e536d722d5e0bb0e346728c1a8de3e259188c7fa963d07d62c5e95ea4",5,2,3),
"supp-007":("7782442f0ad8d72b9c7e3a2890fcc872634e2f49e43617e3da92d063a0b090c0",6,3,3),
"supp-008":("e3b78632594795dee5cbd2d7a3ad6529e259896ce7962530acb101e131630b03",28,14,14),
"supp-009":("3e52ac721c6ddb4577a0c2becc5bfeb5f5931acbcdde81e905d144179e141741",4,2,2),
}
CASES={
"MV-EVAL-016":("MV-CORR-70B803CEF75E","MV-REG-4B7BB4030D4B","bd963a46ede7be0a6429461a485640fdc6a3b8e74c60f9ab47de68ee31d88622","C-EXECUTION-TERMINATION-GATE"),
"MV-EVAL-017":("MV-CORR-31564EEDA09A","MV-REG-EF0FE64CC2A8","ec7a70b299f3585f0fe37ff683f625f440a445180f6b70ae001ffb570b401559","C-COMMAND-MODE-FIDELITY"),
"MV-EVAL-018":("MV-CORR-AB8AF39A7E0E","MV-REG-A4FD1C7999B2","094ee3a0e82b191988478852ef9b667789b2bd442c8936f0f6c6e937d0b03771","C-EXECUTION-TERMINATION-GATE"),
}
FORBIDDEN={"text","raw_text","raw_message","raw_transcript","transcript","quote","message_text","full_message","source_filename","conversation_title","attachment_content","credential","token","url"}

class Error(RuntimeError):pass
def req(ok:bool,msg:str):
 if not ok:raise Error(msg)
def load(root:Path,p:Path):
 try:return json.loads((root/p).read_text(encoding="utf-8"))
 except FileNotFoundError as e:raise Error(f"missing file: {p}") from e
 except json.JSONDecodeError as e:raise Error(f"invalid JSON: {p}: {e}") from e
def text(root:Path,p:Path):
 try:return (root/p).read_text(encoding="utf-8")
 except FileNotFoundError as e:raise Error(f"missing file: {p}") from e
def walk(v:Any):
 if isinstance(v,dict):
  for k,c in v.items():yield k;yield from walk(c)
 elif isinstance(v,list):
  for c in v:yield from walk(c)
def has_terms(label:str,value:str,groups:list[tuple[str,...]]):
 low=value.lower()
 for group in groups:req(any(term.lower() in low for term in group),f"{label} missing semantic marker group {group}")
def candidate_case(case_id:str,c:dict)->dict:
 p=c["proposed_case"];out={"case_id":case_id,"name":p["name"],"source_patterns":c["source_patterns"]}
 for k in ("setup","owner_input","expected_actions","prohibited_actions","pass_condition"):out[k]=p[k]
 return out

def check(root:Path)->dict[str,Any]:
 root=root.resolve();s=load(root,SUPP)
 req(s.get("schema_version")=="1.0.0" and s.get("supplement_id")==SUPP_ID,"supplement identity mismatch")
 req(s.get("archive_sha256")==ARCHIVE_SHA,"supplement archive hash mismatch")
 req((s.get("source_count"),s.get("visible_message_count"),s.get("visible_user_message_count"),s.get("visible_assistant_message_count"))==(9,58,29,29),"supplement counts mismatch")
 rows={x.get("source_id"):x for x in s.get("sources",[])};req(set(rows)==set(SOURCES),"supplement source set mismatch")
 for sid,(sha,n,u,a) in SOURCES.items():
  r=rows[sid];req((r.get("sha256"),r.get("visible_message_count"),r.get("visible_user_message_count"),r.get("visible_assistant_message_count"))==(sha,n,u,a),f"{sid}: evidence mismatch")
 req(s.get("privacy")=={"raw_bytes_published":False,"source_filenames_published":False,"conversation_titles_published":False,"verbatim_messages_published":False},"supplement privacy mismatch")
 req(not(FORBIDDEN&set(walk(s))),"supplement contains prohibited raw-content field")
 req(".mht" not in json.dumps(s).lower(),"supplement exposes private archive filename/extension")

 src=load(root,SOURCE);req(src.get("source_package_sha256")=="eba9af96055c7a2d7f1bda3823440bc2a7c623ea34a77a6bc5b536d7e3d996a6","foundation source hash changed")
 req(src.get("private_corpus_sha256")=="c5a26a20cfe09bce23cd3359b32831e4446db1e57ab2eed111428268c3e2e4c8" and src.get("conversation_count")==9 and src.get("message_count")==114,"foundation corpus identity changed")
 ref=next((x for x in src.get("supplements",[]) if x.get("supplement_id")==SUPP_ID),None);req(ref is not None,"supplement source reference missing")
 req(ref.get("reference_path")==str(SUPP) and ref.get("archive_sha256")==ARCHIVE_SHA and ref.get("source_count")==9 and ref.get("visible_message_count")==58,"supplement source reference mismatch")

 b=text(root,BOOT);c=text(root,CONTRACT);t=text(root,TESTS);r=text(root,REPORT)
 req("**Version:** 6.2.0" in b,"bootstrap version mismatch");req("**Version:** 1.2.0" in c,"contract version mismatch")
 semantics=[("get ready",),("status report and continue",),("continue until you need me","keep going"),("termination preflight",),("queued or running","queued/running"),("completed_verified",),("reversible ambiguity",)]
 has_terms("bootstrap",b,semantics);has_terms("contract",c,semantics)
 for n in range(19,27):req(f"CONT-{n:03d}" in t,f"CONT-{n:03d} missing")
 has_terms("behavior refresh report",r,[("what consistently works",),("repeated failure modes",),("why the prior prose controls were insufficient",),("c-execution-termination-gate",),("c-command-mode-fidelity",),("mv-eval-016",),("mv-eval-017",),("mv-eval-018",)])
 req(".mht" not in r.lower(),"behavior report exposes private archive filename/extension")

 promoted=load(root,PROMOTED);pm={x.get("case_id"):x for x in promoted.get("cases",[])};req(set(CASES)<=set(pm),"behavior evaluation cases missing")
 ledger=load(root,LEDGER);req(ledger.get("schema_version")=="1.0.0","correction ledger schema changed")
 corrections={x.get("correction_id"):x for x in ledger.get("corrections",[])};candidates={x.get("candidate_id"):x for x in ledger.get("candidates",[])}
 control_doc=load(root,CONTROLS);catalog=control_doc.get("control_catalog",{})
 for cid in ("C-EXECUTION-TERMINATION-GATE","C-COMMAND-MODE-FIDELITY"):
  req(cid in catalog and catalog[cid].get("status")=="implemented_2026_08_27_behavior_refresh",f"control missing/inactive: {cid}")
  req("scripts/validate_interaction_behavior_guidance.py" in catalog[cid].get("artifacts",[]),f"validator not bound to {cid}")
 mappings={x.get("case_id"):set(x.get("control_ids",[])) for x in load(root,MAP).get("cases",[])}
 for case_id,(corr_id,cand_id,fp,primary) in CASES.items():
  corr=corrections.get(corr_id);cand=candidates.get(cand_id);req(corr is not None and cand is not None,f"{case_id}: correction/candidate missing")
  req(corr.get("fingerprint")==fp and cand.get("fingerprint")==fp,f"{case_id}: fingerprint mismatch")
  req(corr.get("status")=="promoted" and cand.get("status")=="promoted",f"{case_id}: not promoted")
  req(cand.get("correction_id")==corr_id and corr.get("candidate_id")==cand_id,f"{case_id}: link mismatch")
  review=cand.get("review",{});promotion=cand.get("promotion",{})
  req(review.get("decision")=="approved" and review.get("reviewer")=="john-brandon-turner" and review.get("evidence"),f"{case_id}: owner approval missing")
  req(promotion.get("case_id")==case_id and promotion.get("evidence"),f"{case_id}: promotion evidence missing")
  req(pm[case_id]==candidate_case(case_id,cand),f"{case_id}: promoted case differs from reviewed candidate")
  req(case_id in mappings and primary in mappings[case_id] and "C-CORRECTION-REGRESSION-INTAKE" in mappings[case_id],f"{case_id}: control mapping incomplete")

 return {"status":"PASS","validator":"scripts/validate_interaction_behavior_guidance.py","archive_sha256":ARCHIVE_SHA,"supplement_id":SUPP_ID,"promoted_cases":sorted(CASES),"controls":["C-EXECUTION-TERMINATION-GATE","C-COMMAND-MODE-FIDELITY"]}

def main()->int:
 p=argparse.ArgumentParser();p.add_argument("--root",default=".");p.add_argument("--output");a=p.parse_args()
 try:result=check(Path(a.root))
 except (Error,OSError) as e:print(f"Interaction behavior guidance validation error: {e}",file=sys.stderr);return 1
 payload=json.dumps(result,indent=2,sort_keys=True)+"\n"
 if a.output:Path(a.output).write_text(payload,encoding="utf-8")
 print(payload,end="");return 0
if __name__=="__main__":raise SystemExit(main())
