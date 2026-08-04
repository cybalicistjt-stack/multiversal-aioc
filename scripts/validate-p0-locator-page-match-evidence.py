import json
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
contract = json.loads((ROOT / "governance/object-system/csv-intake/P0_LOCATOR_PAGE_MATCHING_CONTRACT.json").read_text())
evidence = json.loads((ROOT / contract["evidence"]).read_text())
records = evidence["records"]

assert contract["workstream"] == evidence["workstream"] == "8E-009L38"
assert len(records) == contract["expectedRows"] == 107
assert len({record["row"] for record in records}) == 107
assert evidence["sourcePath"] == "Legacy pdfs/Vehicles/Mecha 11-7-24.PDF"
assert evidence["sourceArchiveSha256"] == "60a81e247f203fa8b52eb8cd7a95d1e2039c48aacc5c29d5c7f63bef6a573183"
assert evidence["matchMethod"] == "exact-normalized-locator-phrase"

states = Counter(record["state"] for record in records)
assert states == Counter({
    "unique-page-match": 54,
    "unmatched-locator-quarantined": 39,
    "ambiguous-page-match-quarantined": 14,
})
for record in records:
    assert record["locator"]
    pages = record["pages"]
    assert all(isinstance(page, int) and 1 <= page <= contract["expectedPages"] for page in pages)
    if record["state"] == "unique-page-match":
        assert len(pages) == 1
    elif record["state"] == "ambiguous-page-match-quarantined":
        assert len(pages) > 1
    else:
        assert pages == []

assert evidence["canonicalIdsAssigned"] == 0
assert evidence["promotionReadyRows"] == 0
print(json.dumps({
    "workstream": "8E-009L38",
    "rows": len(records),
    "pages": contract["expectedPages"],
    "pageCitationsAssigned": states["unique-page-match"],
    "ambiguousRowsQuarantined": states["ambiguous-page-match-quarantined"],
    "unmatchedRowsQuarantined": states["unmatched-locator-quarantined"],
    "canonicalIdsAssigned": 0,
    "promotionReadyRows": 0,
}, sort_keys=True))
