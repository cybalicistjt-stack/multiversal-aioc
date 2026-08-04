import csv
import json
import re
import zipfile
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CONTRACT_PATH = ROOT / "governance/object-system/csv-intake/P0_SECONDARY_EVIDENCE_RESOLUTION_CONTRACT.json"
contract = json.loads(CONTRACT_PATH.read_text())
queue = json.loads((ROOT / contract["inputQueue"]).read_text())
page_index = json.loads((ROOT / contract["pageTextIndex"]).read_text())
out_dir = ROOT / contract["outputDirectory"]
out_dir.mkdir(parents=True, exist_ok=True)


def norm(value):
    return re.sub(r"[^a-z0-9]+", " ", (value or "").lower()).strip()


def eligible_secondary_values(row, locator):
    excluded_fragments = {
        "source", "pdf", "document", "file", "name", "title", "id", "record type",
        "canonical", "promotion", "row", "index"
    }
    locator_norm = norm(locator)
    seen = set()
    values = []
    for column, raw in row.items():
        value = (raw or "").strip()
        column_norm = norm(column)
        value_norm = norm(value)
        if not value_norm or value_norm == locator_norm or len(value_norm) < 4:
            continue
        if any(fragment in column_norm for fragment in excluded_fragments):
            continue
        if value_norm in {"yes", "no", "true", "false", "none", "n a", "unknown"}:
            continue
        if value_norm not in seen:
            seen.add(value_norm)
            values.append({"column": column, "value": value, "normalized": value_norm})
    return values


pages = {entry["page"]: norm(entry.get("text")) for entry in page_index["pages"]}
rows_by_number = {}
with zipfile.ZipFile(ROOT / "Csv.zip") as archive:
    member = next((name for name in archive.namelist() if Path(name).name == contract["dataset"]), None)
    if not member:
        raise SystemExit("target dataset missing from Csv.zip")
    with archive.open(member) as raw:
        reader = csv.DictReader(line.decode("utf-8-sig") for line in raw)
        for row_number, row in enumerate(reader, start=2):
            rows_by_number[row_number] = row

results = []
states = Counter()
for queued in queue["records"]:
    row_number = queued["row"]
    row = rows_by_number.get(row_number)
    if row is None:
        raise SystemExit(f"source row {row_number} missing")
    locator = queued["locator"]
    locator_norm = norm(locator)
    secondary = eligible_secondary_values(row, locator)
    candidate_pages = list(queued.get("candidatePages") or pages.keys())
    evidence_by_page = {}

    alias = None
    if locator_norm.startswith("rules framework "):
        alias = locator_norm.removeprefix("rules framework ").strip()

    for page in candidate_pages:
        text = pages[page]
        supports = []
        if alias and alias in text:
            supports.append({"type": "governed-rules-framework-suffix", "value": alias})
        for item in secondary:
            if item["normalized"] in text:
                supports.append({"type": "secondary-csv-field", "column": item["column"], "value": item["value"]})
        if supports:
            evidence_by_page[page] = supports

    ranked = sorted(evidence_by_page.items(), key=lambda item: (-len(item[1]), item[0]))
    resolved_page = None
    resolution_basis = None
    if ranked:
        best_page, best_supports = ranked[0]
        runner_up = len(ranked[1][1]) if len(ranked) > 1 else 0
        independent_supports = len(best_supports)
        alias_only_unique = alias and independent_supports == 1 and runner_up == 0
        strong_unique = independent_supports >= contract["rules"]["minimumIndependentExactSupports"] and independent_supports > runner_up
        if alias_only_unique or strong_unique:
            resolved_page = best_page
            resolution_basis = "unique-governed-alias" if alias_only_unique else "unique-secondary-evidence-score"

    if resolved_page is not None:
        state = "resolved-unique-page"
        page_citation = {"sourcePath": contract["sourcePath"], "page": resolved_page}
    else:
        state = "secondary-evidence-insufficient-quarantined"
        page_citation = None
    states[state] += 1
    results.append({
        "row": row_number,
        "locator": locator,
        "priorState": queued["currentState"],
        "priorCandidatePages": queued.get("candidatePages", []),
        "secondaryEvidence": secondary,
        "pageEvidence": {str(page): supports for page, supports in sorted(evidence_by_page.items())},
        "resolutionState": state,
        "resolutionBasis": resolution_basis,
        "pageCitation": page_citation,
        "canonicalId": None,
        "promotionReady": False
    })

if len(results) != contract["expectedRows"]:
    raise SystemExit(f"row count {len(results)} != {contract['expectedRows']}")

report = {
    "format": "multiversal-p0-secondary-evidence-resolution-report",
    "version": "0.1.0",
    "workstream": contract["workstream"],
    "sourcePath": contract["sourcePath"],
    "rows": len(results),
    "states": dict(states),
    "pageCitationsAssigned": states.get("resolved-unique-page", 0),
    "canonicalIdsAssigned": 0,
    "promotionReadyRows": 0,
    "records": results
}
output = out_dir / "P0_SECONDARY_EVIDENCE_RESOLUTION.json"
output.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n")
print(json.dumps({k: report[k] for k in ("rows", "states", "pageCitationsAssigned", "canonicalIdsAssigned", "promotionReadyRows")}, sort_keys=True))
