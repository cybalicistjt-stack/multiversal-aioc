import csv
import json
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / "governance/object-system/csv-intake"
contract = json.loads((BASE / "P0_MECHA_CONCRETE_RECORD_CONTRACT.json").read_text())
registry = json.loads((ROOT / contract["templateRegistry"]).read_text())
delegation = json.loads((ROOT / contract["ownerDelegation"]).read_text())
assert delegation["status"] == "approved-and-active"
templates = {t["templateId"]: t for t in registry["templates"]}

wanted = set(contract["sourceRows"])
rows = {}
with zipfile.ZipFile(ROOT / "Csv.zip") as archive:
    member = next(name for name in archive.namelist() if Path(name).name == contract["dataset"])
    with archive.open(member) as raw:
        reader = csv.DictReader(line.decode("utf-8-sig") for line in raw)
        for row_number, row in enumerate(reader, start=2):
            if row_number in wanted:
                rows[row_number] = {k: (v if v is not None else "") for k, v in row.items()}
assert set(rows) == wanted

records = []
for row_number in contract["sourceRows"]:
    raw = rows[row_number]
    template_id = contract["templates"][str(row_number)]
    template = templates[template_id]
    name = raw.get("Item_Name") or raw.get("Name") or f"source-row-{row_number}"
    nonblank = {k: v for k, v in raw.items() if v.strip()}
    is_frame = template_id == "vehicle.mecha.frame"
    compatibility = "not-applicable-shared-rules" if is_frame else "unresolved-without-explicit-host-evidence"
    power_fields = {k: v for k, v in nonblank.items() if any(token in k.lower() for token in ("power", "energy", "capacitor", "draw", "capacity"))}
    mechanical_fields = {k: v for k, v in nonblank.items() if any(token in k.lower() for token in ("damage", "range", "speed", "armor", "cost", "output", "bonus", "penalty", "require"))}
    required_assessment = {field: "represented-by-governed-envelope" for field in template["requiredFields"]}
    required_assessment["identity"] = "staging-identity-present"
    required_assessment["provenance"] = "source-row-and-governed-pdf-locator-present"
    record = {
        "recordId": f"staging:mecha:row-{row_number}",
        "sourceRow": row_number,
        "templateId": template_id,
        "identity": {"name": name, "state": "staging-only", "canonicalId": None},
        "classification": {"template": template_id, "recommendationBasis": contract["ownerDelegation"]},
        "provisionalValues": nonblank,
        "rawCsv": raw,
        "validation": {
            "templateCompleteness": required_assessment,
            "compatibility": compatibility,
            "powerBudget": "provisional-fields-retained-no-unsupported-arithmetic" if power_fields else "not-computable-from-present-source-fields",
            "relationship": compatibility,
            "runtimeBehaviors": {behavior: "supported-by-template-requires-runtime-fixture" for behavior in template["runtimeBehaviors"]},
            "mechanicalFieldCount": len(mechanical_fields),
            "powerFieldCount": len(power_fields)
        },
        "ownerDelegatedRecommendation": "retain source claim as reversible provisional working value until field-specific verification contradicts it",
        "promotionReady": False
    }
    records.append(record)

report = {
    "format": "multiversal-p0-mecha-concrete-record-report",
    "version": "0.1.0",
    "workstream": contract["workstream"],
    "recordsGenerated": len(records),
    "sourceRows": contract["sourceRows"],
    "templatesExercised": sorted({r["templateId"] for r in records}),
    "allRawFieldsPreserved": all(len(r["rawCsv"]) > 0 for r in records),
    "compatibilityResolvedWithoutEvidence": 0,
    "powerBudgetsFabricated": 0,
    "canonicalIdsAssigned": 0,
    "promotionReadyRows": 0,
    "records": records
}
out = ROOT / contract["outputDirectory"]
out.mkdir(parents=True, exist_ok=True)
(out / "P0_MECHA_CONCRETE_RECORDS.json").write_text(json.dumps(report, indent=2, sort_keys=True) + "\n")
assert report["recordsGenerated"] == 3
assert report["canonicalIdsAssigned"] == report["promotionReadyRows"] == 0
for record in records:
    assert record["identity"]["canonicalId"] is None
    assert record["promotionReady"] is False
    assert record["rawCsv"]
    assert record["validation"]["runtimeBehaviors"]
print(json.dumps({"records": 3, "templates": report["templatesExercised"], "canonicalIdsAssigned": 0, "promotionReadyRows": 0}, sort_keys=True))
