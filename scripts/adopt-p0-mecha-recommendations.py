import csv
import json
import zipfile
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / "governance/object-system/csv-intake"
contract = json.loads((BASE / "P0_MECHA_RECOMMENDATION_ADOPTION_CONTRACT.json").read_text())
delegation = json.loads((ROOT / contract["ownerDelegation"]).read_text())
coverage = json.loads((ROOT / contract["inputCoverage"]).read_text())
assert delegation["status"] == "approved-and-active"
assert delegation["scope"]["ownerReviewNotRequired"] is True
assert coverage["rows"] == contract["expectedRows"]

wanted = set()
for start, end in contract["rowRanges"]:
    wanted.update(range(start, end + 1))

RULES = {
    "description": ("adopt-provisional-description", "Preserve the CSV wording as the reversible working description.", "medium"),
    "output": ("adopt-provisional-output", "Use the stated output provisionally while retaining source and balance gates.", "medium"),
    "compat": ("adopt-provisional-compatibility", "Treat listed compatibility as a constraint rather than universal compatibility.", "medium"),
    "cost": ("adopt-provisional-cost", "Use the supplied cost as an authored provisional value.", "low"),
    "require": ("adopt-provisional-requirement", "Treat the stated requirement as mandatory unless later evidence marks it optional.", "medium"),
    "damage": ("adopt-provisional-mechanical-value", "Preserve the authored mechanical value without normalization.", "low"),
    "range": ("adopt-provisional-mechanical-value", "Preserve the authored mechanical value without normalization.", "low"),
    "speed": ("adopt-provisional-mechanical-value", "Preserve the authored mechanical value without normalization.", "low"),
    "armor": ("adopt-provisional-mechanical-value", "Preserve the authored mechanical value without normalization.", "low"),
    "health": ("adopt-provisional-mechanical-value", "Preserve the authored mechanical value without normalization.", "low"),
    "power": ("adopt-provisional-resource-value", "Preserve the stated resource value pending system balance validation.", "low"),
    "energy": ("adopt-provisional-resource-value", "Preserve the stated resource value pending system balance validation.", "low")
}

def choose(field):
    lowered = field.lower()
    for token, result in RULES.items():
        if token in lowered:
            return result
    return ("adopt-provisional-authored-claim", "Preserve the nonblank CSV claim as the working authored value.", "low")

records = []
claim_count = 0
counts = Counter()
with zipfile.ZipFile(ROOT / "Csv.zip") as archive:
    member = next((n for n in archive.namelist() if Path(n).name == contract["dataset"]), None)
    if member is None:
        raise SystemExit("target dataset missing from Csv.zip")
    with archive.open(member) as raw:
        reader = csv.DictReader(line.decode("utf-8-sig") for line in raw)
        for row_number, row in enumerate(reader, start=2):
            if row_number not in wanted:
                continue
            adopted = []
            for field, source_value in row.items():
                value = source_value or ""
                if field in contract["directEvidenceFields"] or value.strip() in contract["structuralDefaultValues"]:
                    continue
                recommendation, rationale, confidence = choose(field)
                adopted.append({
                    "field": field,
                    "rawValue": value,
                    "recommendation": recommendation,
                    "adoptedValue": value,
                    "adoptionState": "owner-delegated-provisional-adoption",
                    "rationale": rationale,
                    "alternativesConsidered": ["retain quarantine", "replace with normalized value", "discard claim"],
                    "confidence": confidence,
                    "reversibility": "fully reversible; raw value and decision retained",
                    "ownerApprovalBasis": contract["ownerDelegation"],
                    "fieldSpecificSourceTextVerified": False
                })
                claim_count += 1
                counts[recommendation] += 1
            records.append({"row": row_number, "catalogId": row.get("Catalog_ID"), "locator": row.get("Item_Name"), "adoptedSemanticClaims": len(adopted), "claims": adopted, "canonicalId": None, "promotionReady": False})

assert len(records) == contract["expectedRows"]
assert claim_count == contract["expectedSemanticClaims"], (claim_count, contract["expectedSemanticClaims"])
report = {
    "format": "multiversal-p0-mecha-recommendation-adoption-report",
    "version": "0.1.0",
    "workstream": contract["workstream"],
    "dataset": contract["dataset"],
    "rows": len(records),
    "semanticClaimsReviewed": claim_count,
    "recommendationsGenerated": claim_count,
    "recommendationsAdopted": claim_count,
    "remainingWithoutRecommendation": 0,
    "recommendationCounts": dict(sorted(counts.items())),
    "adoptionState": "owner-delegated-provisional-working-values",
    "fieldSpecificSourceTextVerificationStillRequired": claim_count,
    "canonicalIdsAssigned": 0,
    "promotionReadyRows": 0,
    "records": records
}
out = ROOT / contract["outputDirectory"]
out.mkdir(parents=True, exist_ok=True)
(out / "P0_MECHA_RECOMMENDATION_ADOPTION.json").write_text(json.dumps(report, indent=2, sort_keys=True) + "\n")
print(json.dumps({k: report[k] for k in ["rows", "semanticClaimsReviewed", "recommendationsGenerated", "recommendationsAdopted", "remainingWithoutRecommendation"]}, sort_keys=True))
