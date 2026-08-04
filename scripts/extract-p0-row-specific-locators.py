import csv
import json
import re
import zipfile
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CONTRACT = ROOT / "governance/object-system/csv-intake/P0_ROW_SPECIFIC_LOCATOR_CONTRACT.json"
contract = json.loads(CONTRACT.read_text())
out_dir = ROOT / contract["outputDirectory"]
out_dir.mkdir(parents=True, exist_ok=True)


def norm(value):
    return re.sub(r"[^a-z0-9]+", " ", (value or "").lower()).strip()


def select_locator(row):
    preferred = [
        "name", "title", "object name", "object_name", "component name",
        "component_name", "mecha name", "mecha_name", "designation", "model"
    ]
    by_norm = {norm(key): key for key in row}
    for preferred_key in preferred:
        actual = by_norm.get(norm(preferred_key))
        value = (row.get(actual) or "").strip() if actual else ""
        if value:
            return actual, value
    for key, value in row.items():
        if "name" in norm(key) and (value or "").strip():
            return key, value.strip()
    return None, None

source_keys = {"source pdf", "source document", "source", "source file"}
records = []
states = Counter()
with zipfile.ZipFile(ROOT / "Csv.zip") as archive:
    member = next((name for name in archive.namelist() if Path(name).name == contract["dataset"]), None)
    if not member:
        raise SystemExit("target dataset missing from Csv.zip")
    with archive.open(member) as raw:
        reader = csv.DictReader(line.decode("utf-8-sig") for line in raw)
        fields = reader.fieldnames or []
        source_columns = [field for field in fields if norm(field) in source_keys]
        for row_number, row in enumerate(reader, start=2):
            claims = {(row.get(field) or "").strip() for field in source_columns if (row.get(field) or "").strip()}
            if contract["sourceClaim"] not in claims:
                continue
            locator_column, locator = select_locator(row)
            state = "locator-extracted" if locator else "blank-locator-quarantined"
            states[state] += 1
            records.append({
                "dataset": contract["dataset"],
                "rowNumber": row_number,
                "sourceClaim": contract["sourceClaim"],
                "sourcePath": contract["sourcePath"],
                "locatorColumn": locator_column,
                "locator": locator,
                "locatorState": state,
                "pageCitation": None,
                "canonicalId": None,
                "promotionReady": False
            })

if len(records) != contract["expectedRows"]:
    raise SystemExit(f"row count {len(records)} != {contract['expectedRows']}")

with (out_dir / "ROW_SPECIFIC_LOCATORS.jsonl").open("w", encoding="utf-8") as handle:
    for record in records:
        handle.write(json.dumps(record, ensure_ascii=False, sort_keys=True) + "\n")

summary = {
    "format": "multiversal-p0-row-specific-locator-report",
    "workstream": contract["workstream"],
    "rows": len(records),
    "states": dict(states),
    "pageCitationsAssigned": 0,
    "canonicalIdsAssigned": 0,
    "promotionReadyRows": 0
}
(out_dir / "SUMMARY.json").write_text(json.dumps(summary, indent=2, sort_keys=True) + "\n")
print(json.dumps(summary, sort_keys=True))
