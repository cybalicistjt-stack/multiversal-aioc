import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / "governance/object-system/csv-intake"
contract = json.loads((BASE / "P0_MECHA_RECOMMENDATION_ADOPTION_CONTRACT.json").read_text())
delegation = json.loads((ROOT / contract["ownerDelegation"]).read_text())
report_path = ROOT / contract["outputDirectory"] / "P0_MECHA_RECOMMENDATION_ADOPTION.json"
report = json.loads(report_path.read_text())

assert delegation["status"] == "approved-and-active"
assert report["format"] == "multiversal-p0-mecha-recommendation-adoption-report"
assert report["workstream"] == contract["workstream"]
assert report["rows"] == contract["expectedRows"] == 107
assert report["semanticClaimsReviewed"] == contract["expectedSemanticClaims"] == 6435
assert report["recommendationsGenerated"] == 6435
assert report["recommendationsAdopted"] == 6435
assert report["remainingWithoutRecommendation"] == 0
assert report["fieldSpecificSourceTextVerificationStillRequired"] == 6435
assert report["canonicalIdsAssigned"] == 0
assert report["promotionReadyRows"] == 0
assert len(report["records"]) == 107
for record in report["records"]:
    assert record["canonicalId"] is None
    assert record["promotionReady"] is False
    for claim in record["claims"]:
        assert claim["rawValue"] == claim["adoptedValue"]
        assert claim["adoptionState"] == "owner-delegated-provisional-adoption"
        assert claim["recommendation"]
        assert claim["rationale"]
        assert claim["alternativesConsidered"]
        assert claim["confidence"] in {"low", "medium", "high"}
        assert claim["reversibility"]
        assert claim["ownerApprovalBasis"] == contract["ownerDelegation"]
        assert claim["fieldSpecificSourceTextVerified"] is False
print(json.dumps({"validatedRows": report["rows"], "adoptedRecommendations": report["recommendationsAdopted"], "remainingWithoutRecommendation": 0}, sort_keys=True))
