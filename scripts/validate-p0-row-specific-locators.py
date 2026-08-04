import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
contract = json.loads((ROOT / "governance/object-system/csv-intake/P0_ROW_SPECIFIC_LOCATOR_CONTRACT.json").read_text())
out_dir = ROOT / contract["outputDirectory"]
summary = json.loads((out_dir / "SUMMARY.json").read_text())
records = [json.loads(line) for line in (out_dir / "ROW_SPECIFIC_LOCATORS.jsonl").read_text().splitlines() if line]

assert summary["workstream"] == "8E-009L37"
assert len(records) == contract["expectedRows"] == 107
assert sum(summary["states"].values()) == 107
assert all(record["rowNumber"] >= 2 for record in records)
assert all(record["sourceClaim"] == contract["sourceClaim"] for record in records)
assert all(record["sourcePath"] == contract["sourcePath"] for record in records)
assert all(record["pageCitation"] is None for record in records)
assert all(record["canonicalId"] is None and not record["promotionReady"] for record in records)
assert summary["pageCitationsAssigned"] == 0
assert summary["canonicalIdsAssigned"] == 0
assert summary["promotionReadyRows"] == 0
print(json.dumps(summary, sort_keys=True))
