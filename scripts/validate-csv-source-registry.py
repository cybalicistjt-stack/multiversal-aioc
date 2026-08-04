#!/usr/bin/env python3
import json
import sys
from pathlib import Path

base = Path('governance/object-system/csv-intake')
registry = json.loads((base / 'CSV_SOURCE_REGISTRY.json').read_text())
coverage = json.loads((base / 'CSV_TEMPLATE_COVERAGE_MATRIX.json').read_text())
mappings = json.loads((base / 'CSV_MAPPING_CONTRACT_REGISTRY.json').read_text())
failures = []

if registry.get('datasetCount') != 20 or len(registry.get('datasets', [])) != 20:
    failures.append('source registry must contain 20 datasets')
if sum(item.get('rows', 0) for item in registry['datasets']) != 19199:
    failures.append('source registry row total mismatch')
files = [item['file'] for item in registry['datasets']]
if len(files) != len(set(files)):
    failures.append('duplicate dataset routing entry')
if not registry.get('routingRules', {}).get('structuredRowsAreNotCanonical'):
    failures.append('canonical-boundary rule missing')
if len(coverage.get('currentTemplateCoverage', [])) != 11:
    failures.append('coverage matrix must cover all 11 current templates')
if len(coverage.get('requiredTemplateGaps', [])) < 9:
    failures.append('known template gaps missing')
for contract in mappings.get('contracts', []):
    if contract.get('dataset') not in files:
        failures.append(f"mapping references unknown dataset {contract.get('dataset')}")
    if not contract.get('identityColumn') or not contract.get('mappings'):
        failures.append(f"incomplete mapping contract {contract.get('dataset')}")
    for mapping in contract.get('mappings', []):
        if mapping.get('evidence') not in {'direct','deterministic-normalization','inferred-classification'}:
            failures.append(f"unsupported evidence type in {contract.get('dataset')}")
if not mappings.get('rules', {}).get('noSilentDefaults'):
    failures.append('no-silent-defaults rule missing')

if failures:
    print('\n'.join(failures), file=sys.stderr)
    raise SystemExit(1)
print(f"CSV source registry validated: {len(files)} datasets, {len(mappings['contracts'])} initial mapping contracts.")
