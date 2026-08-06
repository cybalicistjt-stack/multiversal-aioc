#!/usr/bin/env python3
from __future__ import annotations
import json,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parent; P=ROOT/'feature-packets'
F={'design':P/'MV-IA-F008_INVENTORY_OWNERSHIP_AND_SHARED_ASSETS.md','matrix':P/'MV-IA-F008_ASSET_INTEGRITY_MATRIX.json','trace':P/'MV-IA-F008_IMPLEMENTATION_TRACEABILITY.json','ready':P/'MV-IA-F008_READINESS_RECORD.md','completion':P/'MV-IA-F008_COMPLETION_RECORD.json','backlog':ROOT/'INTERNAL_ALPHA_DESIGN_BACKLOG.md'}
def main():
 e=[]
 for p in F.values():
  if not p.is_file(): e.append(f'missing {p}')
 if e: print('\n'.join(e)); return 1
 d=F['design'].read_text(); m=json.loads(F['matrix'].read_text()); t=json.loads(F['trace'].read_text()); c=json.loads(F['completion'].read_text()); b=F['backlog'].read_text()
 for phrase in ['ownership, custody, control','acyclic authoritative graph','status lookup','P9-06-008-attempt-002','IA-D06-003']:
  if phrase.lower() not in d.lower(): e.append(f'missing phrase {phrase}')
 for k,n in {'assetStates':12,'authorityDimensions':8,'locationTypes':10,'mutationTypes':19,'fixtures':24,'implementationSlices':8,'acceptanceCriteria':28}.items():
  if len(m.get(k,[]))!=n: e.append(f'{k} count')
 if [x.get('fixtureId') for x in m.get('fixtures',[])] != [f'AST-FX-{i:03d}' for i in range(1,25)]: e.append('fixture IDs')
 if m.get('blockingFindings')!=[] or m.get('nextWorkItemId')!='IA-D06-003': e.append('matrix completion')
 if t.get('untracedAcceptanceCriteria')!=[] or t.get('blockingFindings')!=[]: e.append('trace gaps')
 if c.get('result',{}).get('fixtures')!=24 or c.get('parallelWork',{}).get('modified') is not False: e.append('completion record')
 if 'IA-D06-002 — MV-IA-F008 Inventory, Ownership, and Shared Assets — complete' not in b: e.append('backlog completion')
 if 'IA-D06-003 — bounded MV-IA-F013 Maps, Zones, and Tactical Positioning — next' not in b: e.append('backlog next')
 if e:
  print('IA-D06-002 INVENTORY/ASSET VALIDATION: FAIL'); [print('-',x) for x in e]; return 1
 print('IA-D06-002 INVENTORY/ASSET VALIDATION: PASS\nFixtures: 24\nAcceptance criteria: 28\nBlocking findings: 0'); return 0
if __name__=='__main__': sys.exit(main())
