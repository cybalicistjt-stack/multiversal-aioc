#!/usr/bin/env python3
from __future__ import annotations
import json, sys
from pathlib import Path
ROOT=Path(__file__).resolve().parent
P=ROOT/'feature-packets'
FILES={
 'review':P/'IA-D05-006_NONCOMBAT_INTEGRATION_REVIEW.md',
 'matrix':P/'IA-D05-006_NONCOMBAT_INTEGRATION_MATRIX.json',
 'trace':P/'IA-D05-006_IMPLEMENTATION_TRACEABILITY.json',
 'ready':P/'IA-D05-006_READINESS_RECORD.md',
 'completion':P/'IA-D05-006_COMPLETION_RECORD.json',
 'backlog':ROOT/'INTERNAL_ALPHA_DESIGN_BACKLOG.md'
}
def load(path): return json.loads(path.read_text())
def main():
    errors=[]
    for path in FILES.values():
        if not path.is_file(): errors.append(f'missing {path}')
    if errors:
        print('\n'.join(errors)); return 1
    review=FILES['review'].read_text(); matrix=load(FILES['matrix']); trace=load(FILES['trace']); completion=load(FILES['completion']); backlog=FILES['backlog'].read_text()
    required=['objective truth','atomic outcome group','role-safe','graph geometry','P9-06-008-attempt-002','IA-D06-001']
    for phrase in required:
        if phrase.lower() not in review.lower(): errors.append(f'missing phrase {phrase}')
    checks={
      'reviewedFeatures':5,
      'domainAuthorities':5,
      'integratedJourneys':8,
      'crossDomainAdapters':11,
      'fixtures':24,
      'implementationSlices':8,
      'acceptanceCriteria':28
    }
    for key,count in checks.items():
        value=matrix.get(key,[])
        if len(value)!=count: errors.append(f'{key} count')
    ids=[x.get('fixtureId') for x in matrix.get('fixtures',[])]
    expected=[f'NCI-FX-{i:03d}' for i in range(1,25)]
    if ids!=expected: errors.append('fixture IDs')
    if matrix.get('blockingFindings')!=[] or matrix.get('nextWorkItemId')!='IA-D06-001': errors.append('matrix completion')
    if trace.get('untracedAcceptanceCriteria')!=[] or trace.get('blockingFindings')!=[]: errors.append('trace gaps')
    result=completion.get('result',{})
    if result.get('fixtures')!=24 or result.get('blockingFindings')!=0: errors.append('completion metrics')
    if completion.get('parallelWork',{}).get('modified') is not False: errors.append('parallel work modified')
    if 'IA-D05-006 — noncombat integration review — complete' not in backlog: errors.append('backlog completion')
    if 'IA-D06-001 — MV-IA-F007 Full Combat Interface — next' not in backlog: errors.append('backlog next')
    if errors:
        print('IA-D05-006 NONCOMBAT INTEGRATION VALIDATION: FAIL')
        for error in errors: print('-',error)
        return 1
    print('IA-D05-006 NONCOMBAT INTEGRATION VALIDATION: PASS')
    print('Reviewed features: 5\nFixtures: 24\nAcceptance criteria: 28\nBlocking findings: 0')
    return 0
if __name__=='__main__': sys.exit(main())
