#!/usr/bin/env python3
from __future__ import annotations
import json, re
from pathlib import Path

ROOT = Path(__file__).resolve().parent
PACKETS = ROOT / "feature-packets"
REVIEW = PACKETS / "IA-D03-005_CHARACTER_CAMPAIGN_INTEGRATION_REVIEW.md"
MATRIX = PACKETS / "IA-D03-005_CHARACTER_CAMPAIGN_CONTRACT_MATRIX.json"
FINDINGS = PACKETS / "IA-D03-005_INTEGRATION_FINDINGS_REGISTER.json"
TRACE = PACKETS / "IA-D03-005_IMPLEMENTATION_TRACEABILITY.json"
RECEIPT = PACKETS / "IA-D03-005_REVIEW_RECEIPT.md"
READINESS = PACKETS / "IA-D03-005_READINESS_RECORD.md"
COMPLETION = PACKETS / "IA-D03-005_COMPLETION_RECORD.json"

EXPECTED_FEATURES = ["MV-IA-F004","MV-IA-F005","MV-IA-F012","IA-D03-004"]
EXPECTED_CONTRACTS = [f"CCI-C{i:03d}" for i in range(1,29)]
EXPECTED_JOURNEYS = [f"CCI-J{i:03d}" for i in range(1,9)]
EXPECTED_FINDINGS = [f"CCI-F{i:03d}" for i in range(1,13)]
EXPECTED_SLICES = [f"CCI-S{i:02d}" for i in range(1,11)]
EXPECTED_CRITERIA = [f"CCI-AC-{i:03d}" for i in range(1,25)]

def load(path, errors):
    if not path.is_file():
        errors.append(f"missing {path.relative_to(ROOT)}")
        return {}
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        errors.append(f"invalid JSON {path.relative_to(ROOT)}: {exc}")
        return {}

def require(text, phrases, label, errors):
    lower = text.lower()
    for phrase in phrases:
        if phrase.lower() not in lower:
            errors.append(f"{label} missing {phrase!r}")

def main():
    errors=[]
    review = REVIEW.read_text(encoding="utf-8") if REVIEW.is_file() else ""
    receipt = RECEIPT.read_text(encoding="utf-8") if RECEIPT.is_file() else ""
    readiness = READINESS.read_text(encoding="utf-8") if READINESS.is_file() else ""
    matrix=load(MATRIX,errors); findings=load(FINDINGS,errors); trace=load(TRACE,errors); completion=load(COMPLETION,errors)

    if not review.startswith("# IA-D03-005 — Character/Campaign Integration Review"):
        errors.append("review title incorrect")
    sections=[int(m.group(1)) for line in review.splitlines() if (m:=re.match(r"^## (\d+)\. ",line))]
    if sections != list(range(1,21)):
        errors.append(f"review sections must be 1-20 exactly; got {sections}")
    require(review,[
        "Owner and final authority: John Brandon Turner",
        "No blocking integration finding remains open",
        "Campaign-scoped grant",
        "immutable launch snapshot",
        "Silent last-write-wins is prohibited",
        "status lookup using the original operation or command ID",
        "36 source-backed governed selectors",
        "119 explicitly synthetic noncanonical fixtures",
        "does not cover the complete game",
        "zero AI",
        "IA-D04-001",
        "Silence is not approval"
    ],"review",errors)
    for cid in EXPECTED_CRITERIA:
        if cid not in review: errors.append(f"review missing {cid}")

    if matrix.get("workItemId")!="IA-D03-005" or matrix.get("owner")!="John Brandon Turner":
        errors.append("matrix identity incorrect")
    if matrix.get("status")!="complete-design-integration-review":
        errors.append("matrix status incorrect")
    if matrix.get("reviewedFeatures")!=EXPECTED_FEATURES:
        errors.append("reviewed features incorrect")
    contracts=matrix.get("contractOwnership",[])
    if [x.get("contractId") for x in contracts] != EXPECTED_CONTRACTS:
        errors.append("contract IDs/count incorrect")
    if any(not x.get("controller") or not x.get("rule") for x in contracts):
        errors.append("contract ownership incomplete")
    journeys=matrix.get("integratedJourneys",[])
    if [x.get("journeyId") for x in journeys] != EXPECTED_JOURNEYS:
        errors.append("journey IDs/count incorrect")
    known=set(EXPECTED_CONTRACTS)
    for j in journeys:
        unknown=set(j.get("requiredContracts",[]))-known
        if unknown: errors.append(f"{j.get('journeyId')} unknown contracts {sorted(unknown)}")
    if [x.get("findingId") for x in matrix.get("resolvedFindings",[])] != EXPECTED_FINDINGS:
        errors.append("matrix findings incorrect")
    if matrix.get("blockingFindings") != []:
        errors.append("matrix retains blocking findings")
    if [x.get("sliceId") for x in matrix.get("implementationSlices",[])] != EXPECTED_SLICES:
        errors.append("implementation slice IDs/count incorrect")
    if [x.get("criterionId") for x in matrix.get("acceptanceCriteria",[])] != EXPECTED_CRITERIA:
        errors.append("matrix acceptance criteria incorrect")
    fixtures=matrix.get("fixtureCoverage",{})
    if (fixtures.get("sourceBackedFixtures"),fixtures.get("syntheticFixtures"),fixtures.get("totalFixtureIdentities")) != (36,119,155):
        errors.append("fixture counts incorrect")
    if len(fixtures.get("requiredFamilies",[])) != 15:
        errors.append("fixture family coverage incomplete")
    for flag in ["implementationAuthorized","paidServicesAuthorized","productionCredentialsAuthorized","realUserDataCollectionAuthorized","internalAlphaReleaseAuthorized","productionAuthorized","publicReleaseAuthorized"]:
        if matrix.get("authorizations",{}).get(flag) is not False:
            errors.append(f"matrix {flag} must be false")
    if matrix.get("nextWorkItemId")!="IA-D04-001":
        errors.append("matrix next work item incorrect")

    if findings.get("status")!="resolved-no-blocking-findings":
        errors.append("findings register status incorrect")
    if [x.get("findingId") for x in findings.get("findings",[])] != EXPECTED_FINDINGS:
        errors.append("findings register IDs incorrect")
    if findings.get("blockingFindings") != []:
        errors.append("findings register retains blocking findings")

    if len(trace.get("acceptanceTrace",[])) != 24 or trace.get("untracedAcceptanceCriteria") != []:
        errors.append("traceability acceptance coverage incomplete")
    if len(trace.get("journeyTrace",[])) != 8 or len(trace.get("implementationSliceTrace",[])) != 10:
        errors.append("traceability journey or slice coverage incomplete")
    if trace.get("blockingFindings") != []:
        errors.append("traceability retains blocking findings")

    metrics=completion.get("metrics",{})
    expected={"reviewedSources":4,"integrationContracts":28,"integratedJourneys":8,"resolvedFindings":12,"blockingFindings":0,"implementationSlices":10,"acceptanceCriteria":24,"sourceBackedFixtures":36,"syntheticFixtures":119,"totalFixtureIdentities":155}
    if completion.get("status")!="complete-design-integration-review" or completion.get("owner")!="John Brandon Turner":
        errors.append("completion identity/status incorrect")
    for key,value in expected.items():
        if metrics.get(key)!=value: errors.append(f"completion {key} must be {value}")
    if completion.get("nextWorkItemId")!="IA-D04-001":
        errors.append("completion next item incorrect")
    for flag in ["implementationAuthorized","paidServicesAuthorized","productionCredentialsAuthorized","realUserDataCollectionAuthorized","internalAlphaReleaseAuthorized","productionAuthorized","publicReleaseAuthorized"]:
        if completion.get("authorizations",{}).get(flag) is not False:
            errors.append(f"completion {flag} must be false")

    require(receipt,["PASS — DESIGN INTEGRATION COMPLETE","twenty-eight normalized integration contracts","zero blocking findings","IA-D04-001","Silence is not approval"],"receipt",errors)
    require(readiness,["READY FOR IMPLEMENTATION HANDOFF — DEPENDENCY GATED","155 provenance-labeled deterministic fixture identities","IA-D04-001"],"readiness",errors)

    f004=load(PACKETS/"MV-IA-F004_CHARACTER_CREATION_MATRIX.json",errors)
    f005=load(PACKETS/"MV-IA-F005_CAMPAIGN_SCENE_SESSION_MATRIX.json",errors)
    f012=load(PACKETS/"MV-IA-F012_ENCOUNTER_BALANCE_MATRIX.json",errors)
    fixtures_source=load(ROOT/"INTERNAL_ALPHA_FIXTURE_COVERAGE_MATRIX.json",errors)
    if f004.get("featureId")!="MV-IA-F004" or len(f004.get("acceptanceCriteria",[]))!=20:
        errors.append("F004 baseline incomplete")
    if f005.get("featureId")!="MV-IA-F005" or len(f005.get("acceptanceCriteria",[]))!=20 or f005.get("blockingFindings")!=[]:
        errors.append("F005 baseline incomplete")
    if f012.get("featureId")!="MV-IA-F012" or len(f012.get("acceptanceCriteria",[]))!=20 or f012.get("blockingFindings")!=[]:
        errors.append("F012 baseline incomplete")
    if (fixtures_source.get("sourceFixtureCount"),fixtures_source.get("syntheticFixtureCount")) != (36,119):
        errors.append("IA-D03-004 fixture baseline incomplete")
    if len(fixtures_source.get("coverageRows",[])) != 15 or fixtures_source.get("blockingFindings")!=[]:
        errors.append("IA-D03-004 coverage baseline incomplete")

    backlog=(ROOT/"INTERNAL_ALPHA_DESIGN_BACKLOG.md").read_text(encoding="utf-8")
    readme=(ROOT/"README.md").read_text(encoding="utf-8")
    packet_index=(PACKETS/"README.md").read_text(encoding="utf-8")
    require(backlog,["IA-D03 — Character and Campaign preparation — COMPLETE","IA-D03-005 — Character/Campaign integration review — complete","IA-D04-001 — MV-IA-F006 First Playable Action and GM Approval Loop — next"],"backlog",errors)
    require(readme,["IA-D03-005 — Character/Campaign Integration Review","IA-D04-001 — MV-IA-F006 First Playable Action and GM Approval Loop"],"program README",errors)
    require(packet_index,["IA-D03-005","Character/Campaign preparation","IA-D04-001"],"packet index",errors)

    if errors:
        raise SystemExit("IA-D03-005 CHARACTER/CAMPAIGN INTEGRATION VALIDATION: FAIL\n" + "\n".join(f"- {e}" for e in errors))
    print("IA-D03-005 CHARACTER/CAMPAIGN INTEGRATION VALIDATION: PASS")
    print("Reviewed sources: 4")
    print("Integration contracts: 28")
    print("Integrated journeys: 8")
    print("Resolved findings: 12")
    print("Blocking findings: 0")
    print("Implementation slices: 10")
    print("Acceptance criteria: 24")
    print("Fixture identities: 155")
    return 0
if __name__=="__main__":
    raise SystemExit(main())
