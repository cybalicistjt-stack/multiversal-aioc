#!/usr/bin/env python3
import csv
import json
import re
import sys
import zipfile
from pathlib import Path

contract_path = Path('governance/object-system/csv-intake/CSV_BATCH_STAGING_CONTRACT.json')
contract = json.loads(contract_path.read_text())
out_dir = Path('artifacts/csv-staging-batch')
out_dir.mkdir(parents=True, exist_ok=True)

INFERENCE_MARKERS = ('best judgment', 'inferred', 'completed by best judgment')
summary = {'format':'multiversal-csv-batch-staging-summary','workstream':'8E-009L10','datasets':[], 'totalRows':0, 'quarantinedRows':0}

def slug(value):
    value = re.sub(r'[^a-z0-9]+', '-', value.lower()).strip('-')
    return value or 'unnamed'

with zipfile.ZipFile(contract['archive']) as archive:
    names = set(archive.namelist())
    for spec in contract['datasets']:
        filename = spec['file']
        matches = [n for n in names if n.endswith('/' + filename) or n == filename]
        if len(matches) != 1:
            raise SystemExit(f'archive member resolution failed for {filename}: {matches}')
        member = matches[0]
        output_path = out_dir / f'{Path(filename).stem}.jsonl'
        count = 0
        quarantined = 0
        with archive.open(member) as raw, output_path.open('w', encoding='utf-8') as output:
            text = (line.decode('utf-8-sig') for line in raw)
            reader = csv.DictReader(text)
            if spec['identityColumn'] not in (reader.fieldnames or []):
                raise SystemExit(f'{filename} missing identity column {spec["identityColumn"]}')
            for row_number, row in enumerate(reader, start=2):
                count += 1
                identity_value = (row.get(spec['identityColumn']) or '').strip()
                inference_text = ' '.join(str(v or '') for v in row.values()).lower()
                inference_warning = any(marker in inference_text for marker in INFERENCE_MARKERS)
                if inference_warning:
                    quarantined += 1
                record = {
                    'stagingId': f'mvstg:{slug(Path(filename).stem)}:{slug(identity_value) if identity_value else row_number}',
                    'dataset': filename,
                    'rowNumber': row_number,
                    'sourceIdentity': identity_value or None,
                    'candidateTarget': spec['target'],
                    'rawSource': row,
                    'provenance': {'archive': contract['archive'], 'dataset': filename, 'rowNumber': row_number},
                    'unresolvedManifest': ['template-routing-verification','field-level-provenance','identity-reconciliation','promotion-verification'],
                    'inferenceWarning': inference_warning,
                    'validationState': 'staged-inference-quarantine' if inference_warning else 'staged-unverified',
                    'canonicalId': None
                }
                output.write(json.dumps(record, ensure_ascii=False, sort_keys=True) + '\n')
        if count != spec['rows']:
            raise SystemExit(f'{filename} row count {count} != expected {spec["rows"]}')
        summary['datasets'].append({'file': filename, 'rows': count, 'quarantinedRows': quarantined, 'output': str(output_path)})
        summary['totalRows'] += count
        summary['quarantinedRows'] += quarantined

if summary['totalRows'] != contract['expectedTotalRows']:
    raise SystemExit(f'total rows {summary["totalRows"]} != expected {contract["expectedTotalRows"]}')
summary['canonicalIdsAssigned'] = 0
summary['promotionReadyRows'] = 0
summary['status'] = 'batch-staging-complete'
(out_dir / 'SUMMARY.json').write_text(json.dumps(summary, indent=2) + '\n', encoding='utf-8')
print(json.dumps(summary, sort_keys=True))
