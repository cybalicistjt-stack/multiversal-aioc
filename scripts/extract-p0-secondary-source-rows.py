import csv
import json
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
contract = json.loads((ROOT / "governance/object-system/csv-intake/P0_SECONDARY_EVIDENCE_RESOLUTION_CONTRACT.json").read_text())
queue = json.loads((ROOT / contract["inputQueue"]).read_text())
wanted = {record["row"] for record in queue["records"]}
rows = []
with zipfile.ZipFile(ROOT / "Csv.zip") as archive:
    member = next((name for name in archive.namelist() if Path(name).name == contract["dataset"]), None)
    if not member:
        raise SystemExit("target dataset missing from Csv.zip")
    with archive.open(member) as raw:
        reader = csv.DictReader(line.decode("utf-8-sig") for line in raw)
        for row_number, row in enumerate(reader, start=2):
            if row_number in wanted:
                rows.append({"row": row_number, "fields": row})
if len(rows) != contract["expectedRows"]:
    raise SystemExit(f"row count {len(rows)} != {contract['expectedRows']}")
out = ROOT / contract["outputDirectory"]
out.mkdir(parents=True, exist_ok=True)
(out / "P0_SECONDARY_SOURCE_ROWS.json").write_text(json.dumps({"format":"multiversal-p0-secondary-source-rows","rows":len(rows),"records":rows}, indent=2, sort_keys=True) + "\n")
print(json.dumps({"rows": len(rows)}, sort_keys=True))
