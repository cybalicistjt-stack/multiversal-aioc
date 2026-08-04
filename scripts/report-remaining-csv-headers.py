#!/usr/bin/env python3
import csv
import json
import zipfile
from pathlib import Path

source_registry = json.loads(Path('governance/object-system/csv-intake/CSV_SOURCE_REGISTRY.json').read_text())
mapping_registry = json.loads(Path('governance/object-system/csv-intake/CSV_MAPPING_CONTRACT_REGISTRY.json').read_text())
mapped = {item['dataset'] for item in mapping_registry.get('contracts', [])}
remaining = [item for item in source_registry['datasets'] if item['file'] not in mapped]
result = {'format':'multiversal-remaining-csv-header-report','datasetCount':len(remaining),'totalRows':sum(item['rows'] for item in remaining),'datasets':[]}
with zipfile.ZipFile('Csv.zip') as archive:
    names = set(archive.namelist())
    for item in remaining:
        filename = item['file']
        matches = [name for name in names if name == filename or name.endswith('/' + filename)]
        if len(matches) != 1:
            raise SystemExit(f'archive member resolution failed for {filename}: {matches}')
        with archive.open(matches[0]) as raw:
            reader = csv.reader(line.decode('utf-8-sig') for line in raw)
            headers = next(reader)
        result['datasets'].append({'file':filename,'rows':item['rows'],'domain':item['domain'],'headers':headers,'primaryTargets':item['primaryTargets'],'readiness':item['readiness']})
print('CSV_REMAINING_HEADERS=' + json.dumps(result, ensure_ascii=False, sort_keys=True))
