import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
contract = json.loads((ROOT / 'governance/object-system/csv-intake/P0_ROW_PAGE_MATCH_BATCH_1_CONTRACT.json').read_text())
out_dir = ROOT / contract['outputDirectory']
summary = json.loads((out_dir / 'SUMMARY.json').read_text())
records = [json.loads(line) for line in (out_dir / 'ROW_PAGE_MATCH_RESULTS.jsonl').read_text().splitlines() if line.strip()]

assert contract['workstream'] == '8E-009L36'
assert len(records) == contract['expectedRows'] == 107
assert summary['rowsAttempted'] == 107
assert summary['uniquePageCitationsAssigned'] == 0
assert summary['ambiguousRowsQuarantined'] == 107
assert summary['canonicalIdsAssigned'] == 0
assert summary['promotionReadyRows'] == 0
assert all(r['documentScopeVerified'] is True for r in records)
assert all(r['pageCitation'] is None for r in records)
assert all(r['candidatePageRange'] == [1, 39] for r in records)
assert all(r['matchState'] == 'quarantined-ambiguous-no-row-specific-locator' for r in records)
assert all(r['canonicalId'] is None and r['promotionReady'] is False for r in records)
print(json.dumps(summary, sort_keys=True))
