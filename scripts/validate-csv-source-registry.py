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

coverage_entries = coverage.get('currentTemplateCoverage', [])
coverage_ids = {item.get('templateId') for item in coverage_entries}
legacy_required = {
    'item.weapon.melee','item.weapon.firearm','item.protection.armor','item.protection.eva-suit',
    'item.storage.typed-container','item.consumable.effect-delivery','item.device.computer',
    'item.magic.implement','item.living.sentient-companion','item.living.symbiote',
    'item.material.crafting-resource'
}
extension_required = {
    'item.weapon.ranged','item.weapon.energy','item.ammunition','item.implant',
    'item.modification.module','item.tool','item.device.general','item.trap','item.software'
}
for template_id in sorted(legacy_required | extension_required):
    if template_id not in coverage_ids:
        failures.append(f'missing coverage entry {template_id}')
resolved = set(coverage.get('resolvedTemplateGaps', []))
if resolved != extension_required:
    failures.append('resolved template gap set mismatch')
if coverage.get('status') != 'template-gaps-defined':
    failures.append('coverage matrix status not advanced')

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
print(f"CSV source registry validated: {len(files)} datasets, {len(coverage_entries)} covered templates, {len(mappings['contracts'])} mapping contracts.")
