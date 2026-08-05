import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / "governance/object-system/csv-intake"
contract = json.loads((BASE / "P0_MECHA_VERIFICATION_CONSOLIDATION_CONTRACT.json").read_text())
report = json.loads((ROOT / contract["output"]).read_text())
page_match = json.loads((BASE / "P0_LOCATOR_PAGE_MATCH_EVIDENCE.json").read_text())
secondary = json.loads((BASE / "P0_SECONDARY_EVIDENCE_RESOLUTION.json").read_text())
visual = json.loads((BASE / "P0_VISUAL_PAGE_VERIFICATION.json").read_text())

assert report["format"] == "multiversal-p0-mecha-verification-consolidation-report"
assert report["workstream"] == contract["workstream"]
assert report["rows"] == contract["expectedRows"] == 107
assert report["singlePageCitations"] == contract["expectedSinglePageCitations"] == 105
assert report["multiPageRanges"] == contract["expectedMultiPageRanges"] == 2
assert report["states"]["single-page-source-locator"] == 105
assert report["states"]["governed-multi-page-source-range"] == 2
assert report["fieldLevelValidationEligibleRows"] == 107
assert report["canonicalIdsAssigned"] == 0
assert report["promotionReadyRows"] == 0
assert page_match["pageCitationsAssigned"] == 54
assert secondary["pageCitationsAssigned"] == 20
assert visual["pageCitationsAssigned"] == 31
assert 54 + 20 + 31 == report["singlePageCitations"]
assert len(report["compositeRanges"]) == 2
assert {entry["row"] for entry in report["compositeRanges"]} == {7, 11}
for entry in report["compositeRanges"]:
    source_range = entry["sourceRange"]
    assert source_range["startPage"] > 0
    assert source_range["endPage"] >= source_range["startPage"]
    assert entry["fieldLevelValidationEligible"] is True
    assert entry["canonicalId"] is None
    assert entry["promotionReady"] is False
assert report["readiness"]["pageOrRangeCoverageComplete"] is True
assert report["readiness"]["fieldLevelValidationMayBegin"] is True
assert report["readiness"]["identityPromotionMayBegin"] is False

out = ROOT / "build/csv-p0-mecha-verification-consolidation-l42"
out.mkdir(parents=True, exist_ok=True)
(out / "P0_MECHA_VERIFICATION_CONSOLIDATION.json").write_text(json.dumps(report, indent=2) + "\n")
print(json.dumps({
    "validatedRows": report["rows"],
    "singlePageCitations": report["singlePageCitations"],
    "multiPageRanges": report["multiPageRanges"],
    "fieldLevelValidationEligibleRows": report["fieldLevelValidationEligibleRows"]
}, sort_keys=True))
