#!/usr/bin/env python3
import json
from pathlib import Path

root = Path(__file__).resolve().parents[1]
report = json.loads((root / 'governance/object-system/csv-intake/CSV_FULL_DOMAIN_PILOT_VALIDATION_REPORT.json').read_text())
old = json.loads((root / 'governance/object-system/item-examples/CSV_PILOT_CONVERSION_OBJECTS.json').read_text())
new = json.loads((root / 'governance/object-system/csv-intake/CSV_FULL_DOMAIN_PILOT_OBJECTS.json').read_text())
objects = old['objects'] + new['objects']
assert report['scope'] == {'datasets': 20, 'pilotObjects': 20, 'archiveRowsRepresented': 19199}
assert len(objects) == 20
assert len({o['stagingId'] for o in objects}) == 20
assert len({o['provenance']['dataset'] for o in objects}) == 20
assert all(o['identity'].get('canonicalId') is None for o in objects)
assert all(o.get('unresolvedFields') for o in objects)
assert all(o.get('templateId') or o.get('templateRouting') for o in objects)
assert all(o.get('provenance', {}).get('dataset') and o['provenance'].get('rowNumber') for o in objects)
assert report['summary']['canonicalIdsAssigned'] == 0
assert report['summary']['promotionReady'] == 0
assert report['batchReadiness']['fullArchiveStagingConversionAuthorized'] is True
assert report['batchReadiness']['canonicalPromotionAuthorized'] is False
assert sum(v['datasets'] for v in report['domainCoverage'].values()) == 20
print('CSV_FULL_DOMAIN_PILOT_VALIDATION=PASS datasets=20 objects=20 canonicalIds=0 promotionReady=0')
