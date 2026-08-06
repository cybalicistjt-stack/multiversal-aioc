#!/usr/bin/env python3
from __future__ import annotations
import json,re,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parent; P=ROOT/'feature-packets'
F={'contract':P/'IA-D04-004_AUTHORITATIVE_RESULT_AND_HISTORY_PRESENTATION.md','matrix':P/'IA-D04-004_AUTHORITATIVE_RESULT_HISTORY_MATRIX.json','trace':P/'IA-D04-004_IMPLEMENTATION_TRACEABILITY.json','review':P/'IA-D04-004_REVIEW_RECEIPT.md','ready':P/'IA-D04-004_READINESS_RECORD.md','completion':P/'IA-D04-004_COMPLETION_RECORD.json','backlog':ROOT/'INTERNAL_ALPHA_DESIGN_BACKLOG.md','program':ROOT/'README.md','index':P/'README.md','roadmap':ROOT.parents[2]/'governance/ai/runtime/ROADMAP_INDEX.json'}
def need(x,m,e):
    if not x:e.append(m)
def load(p,e):
    try:return json.loads(p.read_text())
    except Exception as x:e.append(f'cannot parse {p}: {x}');return {}
def main():
    e=[]
    for p in F.values():need(p.is_file(),f'missing {p}',e)
    if e:print('\n'.join(e));return 1
    c=F['contract'].read_text();m=load(F['matrix'],e);t=load(F['trace'],e);co=load(F['completion'],e)
    secs=[int(x.group(1)) for line in c.splitlines() if (x:=re.match(r'^## (\d+)\. ',line))]
    need(secs==list(range(1,25)),f'sections mismatch {secs}',e)
    for p in ['Only accepted durable decisions','role-safe','original values','final values','ordered Event','IA-D04-005']:need(p.lower() in c.lower(),f'missing phrase {p}',e)
    for k,n in {'presentationSurfaces':8,'resultStates':18,'historyEntryRequiredFields':28,'validationClasses':24,'deniedCases':24,'fixtures':20,'implementationSlices':8,'acceptanceCriteria':20}.items():need(len(m.get(k,[]))==n,f'{k} count',e)
    need([x.get('fixtureId') for x in m.get('fixtures',[])]==[f'ARH-FX-{i:03d}' for i in range(1,21)],'fixture IDs',e)
    need([x.get('criterionId') for x in m.get('acceptanceCriteria',[])]==[f'ARH-AC-{i:03d}' for i in range(1,21)],'criteria IDs',e)
    need(m.get('blockingFindings')==[] and m.get('nextWorkItemId')=='IA-D04-005','matrix completion',e)
    need(t.get('untracedAcceptanceCriteria')==[] and t.get('blockingFindings')==[],'trace gaps',e)
    need(co.get('metrics',{}).get('fixtures')==20 and co.get('metrics',{}).get('blockingFindings')==0,'completion metrics',e)
    b=F['backlog'].read_text();pr=F['program'].read_text();idx=F['index'].read_text()
    need('IA-D04-004 — authoritative result and history presentation — complete' in b,'backlog result',e)
    need('IA-D04-005 — first-playable-loop implementation handoff — next' in b,'backlog next',e)
    need('IA-D04-004 — Authoritative Result and History Presentation' in pr,'program result',e)
    need('IA-D04-005 — First-Playable-Loop Implementation Handoff' in pr,'program next',e)
    need('IA-D04-004' in idx,'index result',e)
    ids={x.get('work_item_id') for x in load(F['roadmap'],e).get('entries',[])}
    need({'IA-D04-004','IA-D04-005'}<=ids,'roadmap handoff',e)
    if e:
        print('IA-D04-004 AUTHORITATIVE RESULT/HISTORY VALIDATION: FAIL')
        for x in e:print('-',x)
        return 1
    print('IA-D04-004 AUTHORITATIVE RESULT/HISTORY VALIDATION: PASS')
    print('Sections: 24\nFixtures: 20\nAcceptance criteria: 20\nBlocking findings: 0')
    return 0
if __name__=='__main__':sys.exit(main())
