import csv
import json
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / "governance/object-system/csv-intake"
contract = json.loads((BASE / "P0_MECHA_PROMOTION_READINESS_CONTRACT.json").read_text())
delegation = json.loads((ROOT / contract["ownerDelegation"]).read_text())
registry = json.loads((ROOT / contract["templateRegistry"]).read_text())
assert delegation["status"] == "approved-and-active"
assert {t["templateId"] for t in registry["templates"]} == {"vehicle.mecha.frame", "vehicle.mecha.component"}

wanted = set(range(2, 22)) | set(range(52, 139))
rows = {}
with zipfile.ZipFile(ROOT / "Csv.zip") as archive:
    member = next(n for n in archive.namelist() if Path(n).name == contract["dataset"])
    with archive.open(member) as raw:
        reader = csv.DictReader(line.decode("utf-8-sig") for line in raw)
        for row_number, row in enumerate(reader, start=2):
            if row_number in wanted:
                rows[row_number] = {k: (v or "") for k, v in row.items()}
assert set(rows) == wanted

records = []
for row_number in sorted(rows):
    raw = rows[row_number]
    is_frame = row_number <= 21
    blockers = [
        "field-specific-source-verification-complete",
        "mechanical-values-verified",
        "runtime-validation-complete",
        "canonical-id-approved"
    ]
    if not is_frame:
        blockers += ["required-relationships-resolved-or-not-applicable", "compatibility-verified-or-not-applicable"]
    name = raw.get("Item_Name") or raw.get("Name") or f"source-row-{row_number}"
    records.append({
        "sourceRow": row_number,
        "name": name,
        "templateId": "vehicle.mecha.frame" if is_frame else "vehicle.mecha.component",
        "passedGates": [
            "governed-template-assigned",
            "page-or-page-range-provenance-resolved",
            "subtype-routing-resolved",
            "identity-conflict-reviewed",
            "install-uninstall-validation-complete"
        ],
        "blockingGates": blockers,
        "recommendation": "retain as validated staging record and continue automatic evidence-backed resolution; do not promote or assign canonical identity yet",
        "recommendationApprovalBasis": contract["ownerDelegation"],
        "canonicalId": None,
        "promotionReady": False
    })

report = {
    "format": "multiversal-p0-mecha-promotion-readiness-report",
    "version": "0.1.0",
    "workstream": contract["workstream"],
    "recordsEvaluated": len(records),
    "promotionReadyRows": sum(r["promotionReady"] for r in records),
    "blockedRows": sum(not r["promotionReady"] for r in records),
    "canonicalIdsAssigned": 0,
    "blockerCounts": {gate: sum(gate in r["blockingGates"] for r in records) for gate in contract["promotionGates"]},
    "records": records
}
out = ROOT / contract["outputDirectory"]
out.mkdir(parents=True, exist_ok=True)
(out / "P0_MECHA_PROMOTION_READINESS.json").write_text(json.dumps(report, indent=2, sort_keys=True) + "\n")
assert report["recordsEvaluated"] == report["blockedRows"] == 107
assert report["promotionReadyRows"] == report["canonicalIdsAssigned"] == 0
assert all(r["blockingGates"] and r["canonicalId"] is None and not r["promotionReady"] for r in records)
print(json.dumps({"evaluated": 107, "blocked": 107, "promotionReady": 0, "canonicalIds": 0}, sort_keys=True))
