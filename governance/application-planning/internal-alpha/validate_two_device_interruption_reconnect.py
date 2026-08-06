#!/usr/bin/env python3
from __future__ import annotations
import json,re,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parent
P=ROOT/'feature-packets'
FILES={
'contract':P/'IA-D04-003_TWO_DEVICE_INTERRUPTION_AND_RECONNECT_MATRIX.md',
'matrix':P/'IA-D04-003_TWO_DEVICE_RECONNECT_MATRIX.json',
'trace':P/'IA-D04-003_IMPLEMENTATION_TRACEABILITY.json',
'review':P/'IA-D04-003_REVIEW_RECEIPT.md',
'readiness':P/'IA-D04-003_READINESS_RECORD.md',
'completion':P/'IA-D04-003_COMPLETION_RECORD.json',
'backlog':ROOT/'INTERNAL_ALPHA_DESIGN_BACKLOG.md',
'program':ROOT/'README.md',
'index':P/'README.md',
'roadmap':ROOT.parents[2]/'governance/ai/runtime/ROADMAP_INDEX.json'
}
def need(ok,msg,errors):
    if not ok: errors.append(msg)
def load(p,errors):
    try:return json.loads(p.read_text())
    except Exception as e: errors.append(f'cannot parse {p}: {e}');return {}
def main():
    e=[]
    for p in FILES.values(): need(p.is_file(),f'missing {p}',e)
    if e: print('\n'.join(e)); return 1
    c=FILES['contract'].read_text(); m=load(FILES['matrix'],e); t=load(FILES['trace'],e); co=load(FILES['completion'],e)
    sections=[int(x.group(1)) for line in c.splitlines() if (x:=re.match(r'^## (\d+)\. ',line))]
    need(sections==list(range(1,25)),f'sections mismatch {sections}',e)
    for phrase in ['silent last-write-wins is prohibited','status lookup','review claims are advisory','ordered durable Events','role-safe projections','IA-D04-004']:
        need(phrase.lower() in c.lower(),f'contract missing {phrase}',e)
    expected={'deviceRoles':6,'interruptionBoundaries':15,'stateVocabulary':20,'stateVectorFields':20,'recoveryActions':12,'deniedCases':24,'scenarios':24,'implementationSlices':8,'acceptanceCriteria':20}
    for k,n in expected.items(): need(len(m.get(k,[]))==n,f'{k} must contain {n}',e)
    need([x.get('fixtureId') for x in m.get('scenarios',[])]==[f'TDR-FX-{i:03d}' for i in range(1,25)],'fixture IDs mismatch',e)
    need([x.get('criterionId') for x in m.get('acceptanceCriteria',[])]==[f'TDR-AC-{i:03d}' for i in range(1,21)],'criteria mismatch',e)
    need(m.get('blockingFindings')==[],'blocking findings remain',e)
    need(m.get('nextWorkItemId')=='IA-D04-004','next item mismatch',e)
    need(t.get('untracedAcceptanceCriteria')==[] and t.get('blockingFindings')==[],'traceability gaps',e)
    metrics=co.get('metrics',{})
    for k,n in {'contractSections':24,'fixtures':24,'acceptanceCriteria':20,'blockingFindings':0}.items(): need(metrics.get(k)==n,f'completion {k} mismatch',e)
    texts={k:FILES[k].read_text() for k in ['backlog','program','index']}
    need('IA-D04-003 — two-device interruption and reconnect matrix — complete' in texts['backlog'],'backlog completion missing',e)
    need('IA-D04-004 — authoritative result and history presentation — next' in texts['backlog'],'backlog next missing',e)
    need('IA-D04-003 — Two-Device Interruption and Reconnect Matrix' in texts['program'],'program result missing',e)
    need('IA-D04-004 — Authoritative Result and History Presentation' in texts['program'],'program next missing',e)
    need('IA-D04-003' in texts['index'],'packet index missing IA-D04-003',e)
    roadmap=load(FILES['roadmap'],e); ids={x.get('work_item_id') for x in roadmap.get('entries',[])}
    need({'IA-D04-003','IA-D04-004'}<=ids,'roadmap missing IA-D04-003 or IA-D04-004',e)
    if e:
        print('IA-D04-003 TWO-DEVICE RECONNECT VALIDATION: FAIL')
        for x in e: print('-',x)
        return 1
    print('IA-D04-003 TWO-DEVICE RECONNECT VALIDATION: PASS')
    print('Sections: 24\nFixtures: 24\nAcceptance criteria: 20\nBlocking findings: 0')
    return 0
if __name__=='__main__':sys.exit(main())
