import csv
import json
import zipfile
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / "governance/object-system/csv-intake"
contract = json.loads((BASE / "P0_MECHA_FIELD_VALIDATION_CONTRACT.json").read_text())
coverage = json.loads((ROOT / contract["inputCoverage"]).read_text())

assert coverage["rows"] == contract["expectedRows"]
assert coverage["fieldLevelValidationEligibleRows"] == contract["expectedRows"]
assert coverage["readiness"]["pageOrRangeCoverageComplete"] is True

wanted = set()
for start, end in contract["rowRanges"]:
    wanted.update(range(start, end + 1))
assert len(wanted) == contract["expectedRows"]

records = []
with zipfile.ZipFile(ROOT / "Csv.zip") as archive:
    member = next((name for name in archive.namelist() if Path(name).name == contract["dataset"]), None)
    if member is None:
        raise SystemExit("target dataset missing from Csv.zip")
    with archive.open(member) as raw:
        reader = csv.DictReader(line.decode("utf-8-sig") for line in raw)
        for row_number, row in enumerate(reader, start=2):
            if row_number not in wanted:
                continue
            field_states = {}
            for field, value in row.items():
                value = value if value is not None else ""
                if field in contract["directEvidenceFields"]:
                    state = "direct-provenance-claim-present" if value.strip() else "missing-direct-provenance-claim"
                elif value.strip() in contract["structuralDefaultValues"]:
                    state = "structural-default-not-source-verified"
                else:
                    state = "semantic-claim-quarantined-pending-field-text-verification"
                field_states[field] = state
            direct_missing = [f for f in contract["directEvidenceFields"] if not (row.get(f) or "").strip()]
            records.append({
                "row": row_number,
                "catalogId": row.get("Catalog_ID"),
                "locator": row.get("Item_Name"),
                "sourcePdf": row.get("Source_PDF"),
                "sourcePageOrBlock": row.get("Source_Page_or_Block"),
                "directEvidenceComplete": not direct_missing,
                "missingDirectEvidenceFields": direct_missing,
                "fieldStates": field_states,
                "canonicalId": None,
                "promotionReady": False
            })

if len(records) != contract["expectedRows"]:
    raise SystemExit(f"row count {len(records)} != {contract['expectedRows']}")

counts = Counter(state for record in records for state in record["fieldStates"].values())
rows_complete = sum(1 for record in records if record["directEvidenceComplete"])
report = {
    "format": "multiversal-p0-mecha-field-validation-report",
    "version": "0.1.0",
    "workstream": contract["workstream"],
    "dataset": contract["dataset"],
    "sourcePath": contract["sourcePath"],
    "rows": len(records),
    "rowsWithCompleteDirectEvidence": rows_complete,
    "rowsMissingDirectEvidence": len(records) - rows_complete,
    "fieldStateCounts": dict(sorted(counts.items())),
    "fieldLevelOutcome": {
        "directProvenanceClaimsValidated": rows_complete == len(records),
        "semanticClaimsRequireFieldSpecificTextVerification": counts["semantic-claim-quarantined-pending-field-text-verification"] > 0,
        "identityPromotionMayBegin": False
    },
    "canonicalIdsAssigned": 0,
    "promotionReadyRows": 0,
    "records": records
}
out = ROOT / contract["outputDirectory"]
out.mkdir(parents=True, exist_ok=True)
(out / "P0_MECHA_FIELD_VALIDATION.json").write_text(json.dumps(report, indent=2, sort_keys=True) + "\n")
print(json.dumps({
    "rows": report["rows"],
    "rowsWithCompleteDirectEvidence": report["rowsWithCompleteDirectEvidence"],
    "rowsMissingDirectEvidence": report["rowsMissingDirectEvidence"],
    "fieldStateCounts": report["fieldStateCounts"]
}, sort_keys=True))
