import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
contract = json.loads((ROOT / "governance/object-system/csv-intake/P0_LOCATOR_DISAMBIGUATION_CONTRACT.json").read_text())
evidence = json.loads((ROOT / contract["outputEvidence"]).read_text())

assert evidence["workstream"] == contract["workstream"]
assert evidence["rows"] == contract["expectedRows"] == len(evidence["records"])
assert evidence["states"]["ambiguous-page-match-quarantined"] == contract["expectedAmbiguousRows"]
assert evidence["states"]["unmatched-locator-quarantined"] == contract["expectedUnmatchedRows"]
assert evidence["pageCitationsAssigned"] == 0
assert evidence["canonicalIdsAssigned"] == 0
assert evidence["promotionReadyRows"] == 0

for record in evidence["records"]:
    assert record["pageCitation"] is None
    assert record["canonicalId"] is None
    assert record["promotionReady"] is False
    assert record["requiredEvidence"]

print(json.dumps({"rows": evidence["rows"], "states": evidence["states"], "status": "valid"}, sort_keys=True))
