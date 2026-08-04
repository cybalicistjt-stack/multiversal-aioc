import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
contract = json.loads((ROOT / "governance/object-system/csv-intake/P0_SECONDARY_EVIDENCE_RESOLUTION_CONTRACT.json").read_text())
report = json.loads((ROOT / "governance/object-system/csv-intake/P0_SECONDARY_EVIDENCE_RESOLUTION.json").read_text())

assert report["format"] == "multiversal-p0-secondary-evidence-resolution-report"
assert report["workstream"] == contract["workstream"]
assert report["sourcePath"] == contract["sourcePath"]
assert report["rows"] == contract["expectedRows"]
assert report["canonicalIdsAssigned"] == 0
assert report["promotionReadyRows"] == 0
assert len(report["resolved"]) == report["states"]["resolved-unique-page"]
assert len(report["quarantined"]) == report["states"]["secondary-evidence-insufficient-quarantined"]
assert len(report["resolved"]) + len(report["quarantined"]) == report["rows"]
assert report["pageCitationsAssigned"] == len(report["resolved"])

seen = set()
for record in report["resolved"]:
    assert record["row"] not in seen
    seen.add(record["row"])
    assert isinstance(record["page"], int) and record["page"] > 0
    assert record["basis"] in {"unique-secondary-field-context", "unique-candidate-within-explicit-source-range"}
    numbers = [int(value) for value in re.findall(r"\d+", record["sourcePageOrBlock"])]
    assert numbers
    if record["sourcePageOrBlock"].lower().startswith("pages") and len(numbers) >= 2:
        assert numbers[0] <= record["page"] <= numbers[1]
    else:
        assert record["page"] == numbers[0]

for record in report["quarantined"]:
    assert record["row"] not in seen
    seen.add(record["row"])
    assert record["sourcePageOrBlock"]
    assert isinstance(record["priorCandidatePages"], list)

artifact = report["sourceRowsArtifact"]
assert artifact["artifactId"] == 8913055532
assert artifact["name"] == "csv-p0-secondary-source-rows-53"
assert len(artifact["sha256"]) == 64
print(json.dumps({"validatedRows": report["rows"], "pageCitationsAssigned": report["pageCitationsAssigned"], "quarantinedRows": len(report["quarantined"])}, sort_keys=True))
