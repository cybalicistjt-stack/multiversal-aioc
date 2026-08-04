#!/usr/bin/env python3
import json
import sys
from pathlib import Path

base = Path('governance/object-system/csv-intake')
source = json.loads((base / 'CSV_SOURCE_REGISTRY.json').read_text())
contracts = json.loads((base / 'CSV_DOMAIN_ROUTING_CONTRACT_REGISTRY.json').read_text())
failures = []

if contracts.get('format') != 'multiversal-csv-domain-routing-contract-registry':
    failures.append('unsupported routing contract format')
if contracts.get('workstream') != '8E-009L11':
    failures.append('wrong workstream')
entries = contracts.get('contracts', [])
if len(entries) != 13:
    failures.append('expected 13 remaining dataset contracts')
if sum(e.get('rows', 0) for e in entries) != 14378:
    failures.append('remaining row total must equal 14378')
source_by_file = {e['file']: e for e in source.get('datasets', [])}
seen = set()
for entry in entries:
    dataset = entry.get('dataset')
    if dataset in seen:
        failures.append(f'duplicate contract {dataset}')
    seen.add(dataset)
    registered = source_by_file.get(dataset)
    if not registered:
        failures.append(f'unknown dataset {dataset}')
        continue
    if registered.get('rows') != entry.get('rows'):
        failures.append(f'row mismatch {dataset}')
    if registered.get('domain') != entry.get('domain'):
        failures.append(f'domain mismatch {dataset}')
    if not entry.get('queue') or not entry.get('requiredRegistries') or not entry.get('nextAction'):
        failures.append(f'incomplete routing contract {dataset}')

mapped = {
    'expanded_melee_weapons_all_genres.csv',
    'expanded_ranged_weapons_catalog.csv',
    'expanded_items_all_genres.csv',
    'expanded_eva_suits_and_modules_all_genres.csv',
    'expanded_computers_all_genres.csv',
    'expanded_living_spellbooks_and_magic_charge_holders_all_genres.csv',
    'expanded_symbiotes_and_cybernetics_all_genres.csv'
}
all_files = set(source_by_file)
if seen != all_files - mapped:
    failures.append('routing contracts do not exactly cover the 13 previously unmapped datasets')
rules = contracts.get('rules', {})
for key in ('preserveRawRows','noCrossDomainCoercion','noCanonicalIds','noSilentDefaults','exactHeaderMappingRequiredBeforeConversion','domainRegistryRequiredBeforePromotion','crossFileIdentityReconciliationRequired','pdfVerificationRequiredForAmbiguityAndMissingFields'):
    if rules.get(key) is not True:
        failures.append(f'missing safety rule {key}')
if 'do not authorize canonical conversion' not in contracts.get('promotionBoundary', ''):
    failures.append('promotion boundary missing')

if failures:
    print('\n'.join(failures), file=sys.stderr)
    raise SystemExit(1)
print('CSV domain routing contracts validated: 13 datasets, 14378 rows.')
