import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
contract = json.loads((ROOT / "governance/object-system/csv-intake/P0_SECONDARY_EVIDENCE_RESOLUTION_CONTRACT.json").read_text())
report_path = ROOT / contract["outputDirectory"] / "P0_SECONDARY_EVIDENCE_RESOLUTION.json"
report = json.loads(report_path.read_text())

assert report["format"] == "multiversal-p0-secondary-evidence-resolution-report"
assert report["workstream"] == contract["workstream"]
assert report["rows"] == contract["expectedRows"] == len(report["records"])
assert report["canonicalIdsAssigned"] == 0
assert report["promotionReadyRows"] == 0
assert sum(report["states"].values()) == report["rows"]

for record in report["records"]:
    assert record["canonicalId"] is None
    assert record["promotionReady"] is False
    citation = record["pageCitation"]
    if record["resolutionState"] == "resolved-unique-page":
        assert citation is not None
        assert citation["sourcePath"] == contract["sourcePath"]
        assert isinstance(citation["page"], int) and citation["page"] > 0
        assert record["resolutionBasis"] in {"unique-governed-alias", "unique-secondary-evidence-score"}
    else:
        assert record["resolutionState"] == "secondary-evidence-insufficient-quarantined"
        assert citation is None
        assert record["resolutionBasis"] is None

assert report["pageCitationsAssigned"] == report["states"].get("resolved-unique-page", 0)
print(json.dumps({"validatedRows": report["rows"], "pageCitationsAssigned": report["pageCitationsAssigned"], "states": report["states"]}, sort_keys=True))
