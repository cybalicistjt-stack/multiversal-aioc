import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / "governance/object-system/csv-intake"
contract = json.loads((BASE / "P0_MECHA_FIELD_VALIDATION_CONTRACT.json").read_text())
report = json.loads((ROOT / contract["outputDirectory"] / "P0_MECHA_FIELD_VALIDATION.json").read_text())

assert report["format"] == "multiversal-p0-mecha-field-validation-report"
assert report["workstream"] == contract["workstream"]
assert report["rows"] == contract["expectedRows"] == len(report["records"])
assert report["rowsWithCompleteDirectEvidence"] + report["rowsMissingDirectEvidence"] == report["rows"]
assert report["canonicalIdsAssigned"] == 0
assert report["promotionReadyRows"] == 0
assert report["fieldLevelOutcome"]["identityPromotionMayBegin"] is False
assert report["fieldLevelOutcome"]["semanticClaimsRequireFieldSpecificTextVerification"] is True
for record in report["records"]:
    assert record["canonicalId"] is None
    assert record["promotionReady"] is False
    assert set(contract["directEvidenceFields"]).issubset(record["fieldStates"])
    if record["directEvidenceComplete"]:
        assert record["missingDirectEvidenceFields"] == []
print(json.dumps({
    "validatedRows": report["rows"],
    "rowsWithCompleteDirectEvidence": report["rowsWithCompleteDirectEvidence"],
    "rowsMissingDirectEvidence": report["rowsMissingDirectEvidence"],
    "fieldStateCounts": report["fieldStateCounts"]
}, sort_keys=True))
