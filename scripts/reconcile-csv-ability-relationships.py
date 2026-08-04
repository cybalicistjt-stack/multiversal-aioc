import csv
import json
import zipfile
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
contract = json.loads((ROOT / 'governance/object-system/csv-intake/CSV_ABILITY_RELATIONSHIP_RECONCILIATION_CONTRACT.json').read_text())
out_dir = ROOT / contract['outputDirectory']
out_dir.mkdir(parents=True, exist_ok=True)
archive = ROOT / 'Csv.zip'

rows = []
with zipfile.ZipFile(archive) as zf:
    members = {Path(n).name: n for n in zf.namelist() if not n.endswith('/')}
    for filename in contract['datasets']:
        member = members.get(filename)
        if not member:
            raise SystemExit(f'missing {filename}')
        with zf.open(member) as raw:
            reader = csv.DictReader(line.decode('utf-8-sig') for line in raw)
            fields = reader.fieldnames or []
            required = {'Record_ID', 'Record_Type', 'Tree_ID'}
            missing = sorted(required - set(fields))
            if missing:
                raise SystemExit(f'{filename} missing required columns {missing}')
            parent_columns = [c for c in fields if c.lower() in {'parent_id', 'parent_record_id', 'prerequisite_id', 'prerequisite_record_id'}]
            for row_number, row in enumerate(reader, start=2):
                rows.append({'dataset': filename, 'rowNumber': row_number, 'row': row, 'parentColumns': parent_columns})

if len(rows) != contract['expectedRows']:
    raise SystemExit(f'row count {len(rows)} != {contract["expectedRows"]}')

def clean(value):
    return (value or '').strip()

def is_tree(row):
    return 'tree' in clean(row.get('Record_Type')).lower()

tree_index = defaultdict(list)
record_index = defaultdict(list)
for entry in rows:
    row = entry['row']
    rid = clean(row.get('Record_ID'))
    if rid:
        record_index[rid].append(entry)
    if is_tree(row):
        for key in {rid, clean(row.get('Tree_ID'))} - {''}:
            tree_index[key].append(entry)

summary = {
    'format': 'multiversal-csv-ability-relationship-reconciliation-report',
    'workstream': contract['workstream'],
    'rows': len(rows),
    'treeRecords': sum(1 for e in rows if is_tree(e['row'])),
    'abilityRecords': sum(1 for e in rows if not is_tree(e['row'])),
    'treeLinks': {'resolved': 0, 'missing': 0, 'ambiguous': 0, 'notApplicable': 0},
    'parentLinks': {'resolved': 0, 'missing': 0, 'ambiguous': 0, 'notProvided': 0},
    'canonicalIdsAssigned': 0,
    'promotionReadyRows': 0
}
queue_path = out_dir / 'UNRESOLVED_RELATIONSHIPS.jsonl'
resolved_path = out_dir / 'RESOLVED_RELATIONSHIPS.jsonl'
with queue_path.open('w', encoding='utf-8') as unresolved, resolved_path.open('w', encoding='utf-8') as resolved:
    for entry in rows:
        row = entry['row']
        rid = clean(row.get('Record_ID'))
        tree_id = clean(row.get('Tree_ID'))
        tree_state = 'not-applicable' if is_tree(row) and not tree_id else None
        tree_targets = tree_index.get(tree_id, []) if tree_id else []
        if tree_state is None:
            if not tree_id:
                tree_state = 'missing'
            elif len(tree_targets) == 1:
                tree_state = 'resolved'
            elif len(tree_targets) > 1:
                tree_state = 'ambiguous'
            else:
                tree_state = 'missing'
        summary['treeLinks'][tree_state.replace('-', '').replace('notapplicable', 'notApplicable') if tree_state == 'not-applicable' else tree_state] += 1

        parent_values = []
        for col in entry['parentColumns']:
            value = clean(row.get(col))
            if value:
                parent_values.append({'column': col, 'value': value})
        parent_results = []
        for parent in parent_values:
            matches = record_index.get(parent['value'], [])
            state = 'resolved' if len(matches) == 1 else ('ambiguous' if len(matches) > 1 else 'missing')
            summary['parentLinks'][state] += 1
            parent_results.append({**parent, 'state': state, 'matches': [{'dataset': m['dataset'], 'rowNumber': m['rowNumber'], 'recordId': clean(m['row'].get('Record_ID'))} for m in matches]})
        if not parent_values:
            summary['parentLinks']['notProvided'] += 1

        result = {
            'dataset': entry['dataset'],
            'rowNumber': entry['rowNumber'],
            'recordId': rid or None,
            'recordType': clean(row.get('Record_Type')) or None,
            'treeIdSource': tree_id or None,
            'treeResolution': {
                'state': tree_state,
                'matches': [{'dataset': m['dataset'], 'rowNumber': m['rowNumber'], 'recordId': clean(m['row'].get('Record_ID')), 'treeId': clean(m['row'].get('Tree_ID'))} for m in tree_targets]
            },
            'parentResolutions': parent_results,
            'canonicalId': None,
            'promotionReady': False
        }
        has_unresolved = tree_state in {'missing', 'ambiguous'} or any(p['state'] != 'resolved' for p in parent_results)
        (unresolved if has_unresolved else resolved).write(json.dumps(result, ensure_ascii=False, sort_keys=True) + '\n')

(out_dir / 'SUMMARY.json').write_text(json.dumps(summary, indent=2, sort_keys=True) + '\n')
print(json.dumps(summary, sort_keys=True))
