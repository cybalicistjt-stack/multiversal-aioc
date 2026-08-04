#!/usr/bin/env python3
import json, sys
from pathlib import Path
p=Path('governance/object-system/item-examples/CSV_REPRESENTATIVE_OBJECT_SELECTIONS.json')
r=json.loads(p.read_text(encoding='utf-8'))
f=[]
if r.get('format')!='multiversal-csv-representative-object-selections': f.append('format')
if r.get('workstream')!='8E-009L7': f.append('workstream')
s=r.get('selections',[])
if len(s)!=7: f.append('expected seven selections')
keys=set()
for x in s:
  for k in ['dataset','rowNumber','sourceObjectName','candidateTemplate','stagingKey','sourceSignals','verificationNeeded','selectionStatus']:
    if k not in x: f.append(f"{x.get('sourceObjectName','unknown')} missing {k}")
  if x.get('stagingKey') in keys: f.append('duplicate staging key')
  keys.add(x.get('stagingKey'))
  if not str(x.get('stagingKey','')).startswith('mvstg:'): f.append('bad staging key')
  if not x.get('verificationNeeded'): f.append('verification list required')
if 'not complete representative objects' not in r.get('promotionBoundary',''): f.append('promotion boundary')
if f:
 print('\n'.join(f),file=sys.stderr); raise SystemExit(1)
print(f'CSV representative selections validated: {len(s)} staging candidates.')
