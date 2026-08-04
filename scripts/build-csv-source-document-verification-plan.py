import csv
import json
import zipfile
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
contract = json.loads((ROOT / 'governance/object-system/csv-intake/CSV_SOURCE_DOCUMENT_VERIFICATION_PLAN_CONTRACT.json').read_text())
registry = json.loads((ROOT / contract['sourceRegistry']).read_text())
out_dir = ROOT / contract['outputDirectory']
out_dir.mkdir(parents=True, exist_ok=True)
archive = ROOT / 'Csv.zip'

datasets = []
for group in registry['identityGroups']:
    for filename in group['datasets']:
        datasets.append((filename, group['groupId']))
if len(datasets) != contract['expectedDatasets']:
    raise SystemExit(f'dataset count {len(datasets)} != {contract["expectedDatasets"]}')

source_columns = {'source_pdf', 'source pdf', 'source_document', 'source document', 'source', 'source_file', 'source file'}
relationship_groups = {'vehicles-mecha-spacecraft-components', 'abilities'}
routing_groups = {'bases-facilities-materials', 'hazards-traps'}
summary = {
    'format': 'multiversal-csv-source-document-verification-plan',
    'workstream': contract['workstream'],
    'datasets': [],
    'totalRows': 0,
    'priorityRows': Counter(),
    'canonicalIdsAssigned': 0,
    'promotionReadyRows': 0
}
queue_path = out_dir / 'VERIFICATION_QUEUE.jsonl'
with zipfile.ZipFile(archive) as zf, queue_path.open('w', encoding='utf-8') as queue:
    members = {Path(n).name: n for n in zf.namelist() if not n.endswith('/')}
    for filename, group_id in datasets:
        member = members.get(filename)
        if not member:
            raise SystemExit(f'missing {filename}')
        counts = Counter()
        source_claims = Counter()
        with zf.open(member) as raw:
            reader = csv.DictReader(line.decode('utf-8-sig') for line in raw)
            fields = reader.fieldnames or []
            source_fields = [f for f in fields if f.strip().lower() in source_columns]
            for row_number, row in enumerate(reader, start=2):
                summary['totalRows'] += 1
                claims = sorted({(row.get(f) or '').strip() for f in source_fields if (row.get(f) or '').strip()})
                for claim in claims:
                    source_claims[claim] += 1
                if group_id in relationship_groups:
                    priority = 'P0-relationship-or-routing-blocker'
                    reason = 'relationship-reconciliation-requires-source-verification'
                elif group_id in routing_groups:
                    priority = 'P0-relationship-or-routing-blocker'
                    reason = 'domain-routing-requires-source-verification'
                elif not claims:
                    priority = 'P1-identity-conflict-or-missing-source'
                    reason = 'missing-source-document-claim'
                else:
                    priority = 'P2-field-provenance-and-domain-validation'
                    reason = 'field-provenance-and-domain-validation'
                counts[priority] += 1
                summary['priorityRows'][priority] += 1
                queue.write(json.dumps({
                    'dataset': filename,
                    'rowNumber': row_number,
                    'identityGroup': group_id,
                    'priority': priority,
                    'reason': reason,
                    'sourceDocumentClaims': claims,
                    'sourceVerificationState': 'unverified',
                    'canonicalId': None,
                    'promotionReady': False
                }, ensure_ascii=False, sort_keys=True) + '\n')
        summary['datasets'].append({
            'file': filename,
            'identityGroup': group_id,
            'rows': sum(counts.values()),
            'priorityRows': dict(counts),
            'sourceDocumentColumns': source_fields,
            'distinctSourceClaims': len(source_claims),
            'topSourceClaims': source_claims.most_common(10)
        })

summary['priorityRows'] = dict(summary['priorityRows'])
if summary['totalRows'] != contract['expectedRows']:
    raise SystemExit(f'row count {summary["totalRows"]} != {contract["expectedRows"]}')
summary['executionBatches'] = [
    {'order': 1, 'priority': 'P0-relationship-or-routing-blocker', 'scope': 'vehicles, abilities, mixed routing, hazards'},
    {'order': 2, 'priority': 'P1-identity-conflict-or-missing-source', 'scope': 'rows without source-document claims and identity review clusters'},
    {'order': 3, 'priority': 'P2-field-provenance-and-domain-validation', 'scope': 'remaining source-backed rows'},
    {'order': 4, 'priority': 'P3-nonblocking-fidelity-review', 'scope': 'post-validation fidelity and image review'}
]
(out_dir / 'SUMMARY.json').write_text(json.dumps(summary, indent=2, sort_keys=True) + '\n')
print(json.dumps(summary, sort_keys=True))
