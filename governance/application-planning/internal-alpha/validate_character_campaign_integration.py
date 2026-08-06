#!/usr/bin/env python3
from __future__ import annotations
import json,re
from pathlib import Path
R=Path(__file__).resolve().parent; P=R/"feature-packets"
paths={
"review":P/"IA-D03-005_CHARACTER_CAMPAIGN_INTEGRATION_REVIEW.md",
"matrix":P/"IA-D03-005_CHARACTER_CAMPAIGN_CONTRACT_MATRIX.json",
"findings":P/"IA-D03-005_INTEGRATION_FINDINGS_REGISTER.json",
"trace":P/"IA-D03-005_IMPLEMENTATION_TRACEABILITY.json",
"receipt":P/"IA-D03-005_REVIEW_RECEIPT.md",
"readiness":P/"IA-D03-005_READINESS_RECORD.md",
"completion":P/"IA-D03-005_COMPLETION_RECORD.json"}
C=[f"CCI-C{i:03d}" for i in range(1,29)]; J=[f"CCI-J{i:03d}" for i in range(1,9)]
F=[f"CCI-F{i:03d}" for i in range(1,13)]; S=[f"CCI-S{i:02d}" for i in range(1,11)]
A=[f"CCI-AC-{i:03d}" for i in range(1,25)]
def load(path,e):
    try:return json.loads(path.read_text())
    except Exception as x:e.append(f"{path.name}: {x}");return {}
def phrases(text,items,label,e):
    low=text.lower()
    for x in items:
        if x.lower() not in low:e.append(f"{label} missing {x!r}")
def main():
    e=[]; review=paths["review"].read_text() if paths["review"].is_file() else ""
    receipt=paths["receipt"].read_text() if paths["receipt"].is_file() else ""
    ready=paths["readiness"].read_text() if paths["readiness"].is_file() else ""
    m=load(paths["matrix"],e); f=load(paths["findings"],e); t=load(paths["trace"],e); c=load(paths["completion"],e)
    if not review.startswith("# IA-D03-005 — Character/Campaign Integration Review"):e.append("review title")
    nums=[int(x.group(1)) for line in review.splitlines() if (x:=re.match(r"^## (\d+)\. ",line))]
    if nums!=list(range(1,21)):e.append(f"review sections {nums}")
    phrases(review,["John Brandon Turner","No blocking integration finding remains open","Campaign-scoped grant","immutable launch snapshot","Silent last-write-wins is prohibited","status lookup using the original operation or command ID","36 source-backed governed selectors","119 explicitly synthetic noncanonical fixtures","does not cover the complete game","zero AI","IA-D04-001","Silence is not approval"],"review",e)
    for x in A:
        if x not in review:e.append(f"review missing {x}")
    if (m.get("workItemId"),m.get("owner"),m.get("status"),m.get("reviewedFeatures"))!=("IA-D03-005","John Brandon Turner","complete-design-integration-review",["MV-IA-F004","MV-IA-F005","MV-IA-F012","IA-D03-004"]):e.append("matrix identity")
    if [x.get("contractId") for x in m.get("contractOwnership",[])]!=C:e.append("contracts")
    if any(not x.get("controller") or not x.get("rule") for x in m.get("contractOwnership",[])):e.append("contract ownership")
    if [x.get("journeyId") for x in m.get("integratedJourneys",[])]!=J:e.append("journeys")
    for x in m.get("integratedJourneys",[]):
        if set(x.get("requiredContracts",[]))-set(C):e.append(f"{x.get('journeyId')} unknown contract")
    if [x.get("findingId") for x in m.get("resolvedFindings",[])]!=F or m.get("blockingFindings")!=[]:e.append("matrix findings")
    if [x.get("sliceId") for x in m.get("implementationSlices",[])]!=S:e.append("slices")
    if [x.get("criterionId") for x in m.get("acceptanceCriteria",[])]!=A:e.append("criteria")
    fc=m.get("fixtureCoverage",{})
    if (fc.get("sourceBackedFixtures"),fc.get("syntheticFixtures"),fc.get("totalFixtureIdentities"),len(fc.get("requiredFamilies",[])))!=(36,119,155,15):e.append("fixture coverage")
    if m.get("nextWorkItemId")!="IA-D04-001":e.append("matrix next")
    flags=["implementationAuthorized","paidServicesAuthorized","productionCredentialsAuthorized","realUserDataCollectionAuthorized","internalAlphaReleaseAuthorized","productionAuthorized","publicReleaseAuthorized"]
    if any(m.get("authorizations",{}).get(x) is not False for x in flags):e.append("matrix authorization")
    if f.get("status")!="resolved-no-blocking-findings" or [x.get("findingId") for x in f.get("findings",[])]!=F or f.get("blockingFindings")!=[]:e.append("findings register")
    if len(t.get("acceptanceTrace",[]))!=24 or len(t.get("journeyTrace",[]))!=8 or len(t.get("implementationSliceTrace",[]))!=10 or t.get("untracedAcceptanceCriteria")!=[] or t.get("blockingFindings")!=[]:e.append("traceability")
    exp={"reviewedSources":4,"integrationContracts":28,"integratedJourneys":8,"resolvedFindings":12,"blockingFindings":0,"implementationSlices":10,"acceptanceCriteria":24,"sourceBackedFixtures":36,"syntheticFixtures":119,"totalFixtureIdentities":155}
    if c.get("status")!="complete-design-integration-review" or c.get("owner")!="John Brandon Turner" or c.get("nextWorkItemId")!="IA-D04-001" or any(c.get("metrics",{}).get(k)!=v for k,v in exp.items()) or any(c.get("authorizations",{}).get(x) is not False for x in flags):e.append("completion")
    phrases(receipt,["PASS — DESIGN INTEGRATION COMPLETE","twenty-eight normalized integration contracts","zero blocking findings","IA-D04-001","Silence is not approval"],"receipt",e)
    phrases(ready,["READY FOR IMPLEMENTATION HANDOFF — DEPENDENCY GATED","155 provenance-labeled deterministic fixture identities","IA-D04-001"],"readiness",e)
    src=[load(P/"MV-IA-F004_CHARACTER_CREATION_MATRIX.json",e),load(P/"MV-IA-F005_CAMPAIGN_SCENE_SESSION_MATRIX.json",e),load(P/"MV-IA-F012_ENCOUNTER_BALANCE_MATRIX.json",e),load(R/"INTERNAL_ALPHA_FIXTURE_COVERAGE_MATRIX.json",e)]
    if src[0].get("featureId")!="MV-IA-F004" or len(src[0].get("acceptanceCriteria",[]))!=20:e.append("F004")
    if src[1].get("featureId")!="MV-IA-F005" or len(src[1].get("acceptanceCriteria",[]))!=20 or src[1].get("blockingFindings")!=[]:e.append("F005")
    if src[2].get("featureId")!="MV-IA-F012" or len(src[2].get("acceptanceCriteria",[]))!=20 or src[2].get("blockingFindings")!=[]:e.append("F012")
    if (src[3].get("sourceFixtureCount"),src[3].get("syntheticFixtureCount"),len(src[3].get("coverageRows",[])),src[3].get("blockingFindings"))!=(36,119,15,[]):e.append("IA-D03-004")
    phrases((R/"INTERNAL_ALPHA_DESIGN_BACKLOG.md").read_text(),["IA-D03 — Character and Campaign preparation — COMPLETE","IA-D03-005 — Character/Campaign integration review — complete","IA-D04-001 — MV-IA-F006 First Playable Action and GM Approval Loop — next"],"backlog",e)
    phrases((R/"README.md").read_text(),["IA-D03-005 — Character/Campaign Integration Review","IA-D04-001 — MV-IA-F006 First Playable Action and GM Approval Loop"],"README",e)
    phrases((P/"README.md").read_text(),["IA-D03-005","Character/Campaign preparation","IA-D04-001"],"packet index",e)
    if e:raise SystemExit("IA-D03-005 CHARACTER/CAMPAIGN INTEGRATION VALIDATION: FAIL\n"+"\n".join(f"- {x}" for x in e))
    print("IA-D03-005 CHARACTER/CAMPAIGN INTEGRATION VALIDATION: PASS")
    print("Reviewed sources: 4\nIntegration contracts: 28\nIntegrated journeys: 8\nResolved findings: 12\nBlocking findings: 0\nImplementation slices: 10\nAcceptance criteria: 24\nFixture identities: 155")
    return 0
if __name__=="__main__":raise SystemExit(main())
