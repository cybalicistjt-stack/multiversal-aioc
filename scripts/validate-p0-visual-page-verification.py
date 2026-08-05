import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
contract = json.loads((ROOT / "governance/object-system/csv-intake/P0_VISUAL_PAGE_VERIFICATION_CONTRACT.json").read_text())
report = json.loads((ROOT / contract["outputReport"]).read_text())

assert report["format"] == "multiversal-p0-visual-page-verification-report"
assert report["workstream"] == contract["workstream"]
assert report["rows"] == contract["expectedRows"] == len(report["records"])
assert report["states"]["resolved-visual-page"] == contract["expectedResolvedRows"]
assert report["states"]["visual-evidence-insufficient-quarantined"] == contract["expectedQuarantinedRows"]
assert report["pageCitationsAssigned"] == contract["expectedResolvedRows"]
assert report["canonicalIdsAssigned"] == 0
assert report["promotionReadyRows"] == 0
assert len({record["row"] for record in report["records"]}) == report["rows"]

for record in report["records"]:
    assert record["canonicalId"] is None
    assert record["promotionReady"] is False
    if record["resolutionState"] == "resolved-visual-page":
        citation = record["pageCitation"]
        assert citation["sourcePath"] == contract["sourcePath"]
        assert 1 <= citation["page"] <= 39
        assert record["resolutionBasis"] == "rendered-page-heading-or-entry"
    else:
        assert record["resolutionState"] == "visual-evidence-insufficient-quarantined"
        assert record["pageCitation"] is None
        assert record["resolutionBasis"] is None

print(json.dumps({"validatedRows": report["rows"], "pageCitationsAssigned": report["pageCitationsAssigned"], "states": report["states"]}, sort_keys=True))
