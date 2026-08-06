#!/usr/bin/env python3
from __future__ import annotations
import json, sys
from pathlib import Path
R=Path(__file__).resolve().parent
files=[R/'IA-D06-006_COMBAT_AND_ASSETS_INTEGRATION_REVIEW.md',R/'IA-D06-006_INTEGRATION_MATRIX.json',R/'IA-D06-006_IMPLEMENTATION_TRACEABILITY.json',R/'IA-D06-006_REVIEW_RECEIPT.md',R/'IA-D06-006_READINESS_RECORD.md',R/'IA-D06-006_COMPLETION_RECORD.json',R/'INTERNAL_ALPHA_DESIGN_BACKLOG.md']
def main():
 e=[]
 for p in files:
  if not p.exists(): e.append(f'missing {p.name}')
 if e: print('\n'.join(e)); return 1
 spec=files[0].read_text(); matrix=json.loads(files[1].read_text()); trace=json.loads(files[2].read_text()); comp=json.loads(files[5].read_text()); backlog=files[6].read_text()
 checks=[(spec.startswith('# IA-D06-006 — Combat and Assets Integration Review'),'title'),('P9-06-008-attempt-002' in spec,'parallel work'),('IA-D07-001' in spec,'next in spec'),(len(matrix.get('integratedJourneys',[]))==8,'journeys'),(len(matrix.get('domainAdapters',[]))==11,'adapters'),(len(matrix.get('fixtures',[]))==24,'fixtures'),(len(matrix.get('implementationSlices',[]))==8,'slices'),(len(matrix.get('acceptanceCriteria',[]))==28,'criteria'),(matrix.get('blockingFindings')==[],'blockers'),(trace.get('blockingFindings')==0,'trace blockers'),(comp.get('phaseStatus')=='IA-D06-complete','phase complete'),('**Version:** 0.25.0' in backlog,'backlog version'),('IA-D06-006 — combat and Assets integration review — complete' in backlog,'backlog complete'),('**IA-D07-001 — MV-IA-F015 World and Setting Management — next.**' in backlog,'backlog next')]
 for ok,msg in checks:
  if not ok:e.append(msg)
 if e:
  print('IA-D06-006 COMBAT/ASSETS INTEGRATION VALIDATION: FAIL'); [print('- '+x) for x in e]; return 1
 print('IA-D06-006 COMBAT/ASSETS INTEGRATION VALIDATION: PASS'); print('Journeys: 8\nAdapters: 11\nFixtures: 24\nSlices: 8\nCriteria: 28\nBlocking findings: 0'); return 0
if __name__=='__main__': sys.exit(main())
