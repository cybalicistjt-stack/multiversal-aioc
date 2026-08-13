#!/usr/bin/env python3
from __future__ import annotations
import json, subprocess
from pathlib import Path

R=Path(__file__).resolve().parents[1]
B=R/'governance/application-planning/character-appearance-production'
MERGE='b8c05844ca2df6218cd2c9b0f75a384f3d8eb74c'
HEAD='ce0d9ffd8784619b7d7ffccdc5c64a3b15dee447'

def load(p): return json.loads(p.read_text(encoding='utf-8'))
def req(x,m):
    if not x: raise SystemExit('CAPP-01 final-state FAILED: '+m)
def git(*args):
    p=subprocess.run(['git',*args],cwd=R,text=True,capture_output=True)
    req(p.returncode==0,f"git {' '.join(args)}: {p.stdout}{p.stderr}")
    return p.stdout

def main():
    receipt=load(B/'CAPP-01_VERIFIED_COMPLETION_RECEIPT_v1.0.0.json')
    backlog=load(B/'CAPP_PROGRAM_BACKLOG.json')
    cp=load(R/'governance/ai/work-state/CAPP-01-attempt-001.json')
    ptr=load(R/'governance/ai/runtime/CURRENT_WORK_POINTER.json')
    status=load(R/'governance/ai/runtime/CURRENT_IMPLEMENTATION_STATUS.json')
    registry=load(B/'CAPP-01_APPEARANCE_CHOICE_REGISTRY_v0.1.0.json')
    pkg=load(B/'CAPP-01_COMPLETION_PACKAGE_INDEX_v0.1.0.json')
    report=(B/'CAPP-01_COMPLETION_REPORT.md').read_text(encoding='utf-8')

    req(receipt['state']=='completed_verified','receipt state')
    req(receipt['exact_validated_head']==HEAD and receipt['applicable_pull_request_workflows']=='72/72','exact candidate evidence')
    req(receipt['pull_request']==299 and receipt['merge_commit']==MERGE and receipt['merge_verification']=='verified valid','PR/merge evidence')
    req(receipt['delivered']=={'profiles':25,'appearance_choice_surfaces':10,'stable_source_derived_choice_ids':180,'capp_roadmap_index_entries':12},'delivered receipt counts')
    req(receipt['next_work_item']=={'id':'CAPP-02','state':'planned_not_activated'},'next-item receipt boundary')
    req(all(v is False for v in receipt['boundaries'].values()),'receipt boundaries')

    items={x['id']:x for x in backlog['work_items']}
    req(items['CAPP-01']['status']=='completed_verified','backlog CAPP-01 final state')
    req(backlog['status']=='owner_approved_active_parallel_work','CAPP program remains active')
    req(backlog.get('completed_work_items',0)>=1,'completed work count')
    req(all(v is False for v in backlog['boundaries'].values()),'program boundaries')
    if items['CAPP-02']['status']=='planned':
        req(backlog.get('next_planned_work_item_id')=='CAPP-02','CAPP-02 is next planned item')

    req(cp['status']=='completed_verified' and cp['completed_at'],'checkpoint final state')
    req(cp['latest_pushed_commit']==HEAD and cp['pull_request']==299 and cp['merge_commit']==MERGE and cp['expected_remote_head']==MERGE,'checkpoint completion evidence')
    req(cp['active_substep'] is None and cp['unresolved_failures']==[] and cp['owner_decision_required'] is False,'checkpoint closure')
    req(cp['roadmap_projection_pending'] is False,'checkpoint projection complete')
    req(any(x.get('status')=='passed' and '72/72' in x.get('evidence','') for x in cp['validation']),'checkpoint hosted validation evidence')

    selected=[x for x in ptr['active_attempts'] if x.get('owner_selected')]
    req(len(selected)==1,'exactly one selected attempt')
    if selected[0]['attempt_id']=='CAPP-01-attempt-001':
        req(selected[0]['status']=='completed_verified' and selected[0]['roadmap_projection_pending'] is False,'selected CAPP-01 completion projection')
        req(status['primary']['work_item_id']=='CAPP-01' and status['primary']['status']=='completed_verified','compact CAPP-01 completion projection')
        for k in ('active_substep','next_action','latest_pushed_commit','pull_request','owner_decision_required','unresolved_failures','roadmap_projection_pending'):
            req(status['primary'][k]==cp[k],f'compact/checkpoint mismatch {k}')
    req('historically batched/pending and is now complete' in ptr['selection_reason'],'historical PPIA projection provenance')
    req(any(x.get('attempt_id')=='PPIA-16-attempt-001' and x.get('status')=='completed_verified' for x in ptr['active_attempts']),'PPIA-16 evidence anchor preserved')
    req(any(x.get('attempt_id')=='DS-008-working-series-attempt-002' and x.get('status')=='blocked_non_owner' for x in ptr['active_attempts']),'DS-008 preserved')
    req(any(x.get('track')=='application-implementation' and x.get('next_work_item_id')=='STAGE-A-A2' for x in ptr['deferred_tracks']),'A2 preserved')

    req(registry['profile_count']==25 and registry['choice_surface_count']==10,'registry counts')
    ids=[]
    for p in registry['profiles']:
        ids += [x['choice_id'] for x in p['required_feature_contracts']]
        ids += [x['choice_id'] for x in p['bounded_choice_contracts']]
        ids += [x['stable_id'] for x in p['explicit_choice_contracts'].values()]
    req(len(ids)==180 and len(set(ids))==180,'180 unique stable choice IDs')
    req(pkg['completion_claim'] is False,'pre-merge candidate package remains historical non-complete evidence')
    req('NOT COMPLETED_VERIFIED' in report,'candidate report historical boundary preserved')

    git('merge-base','--is-ancestor',MERGE,'HEAD')
    message=git('show','-s','--format=%B',MERGE)
    workflow_evidence=('72/72' in message or 'all 72 applicable' in message)
    req(HEAD in message and workflow_evidence and 'CAPP-01' in message,'canonical merge message evidence')
    changed=set(x for x in git('show','--pretty=','--name-only',MERGE).splitlines() if x)
    for path in ('governance/application-planning/character-appearance-production/CAPP-01_APPEARANCE_CHOICE_REGISTRY_v0.1.0.json','governance/application-planning/character-appearance-production/CAPP-01_CONSTRAINT_MODEL_v0.1.0.json','governance/application-planning/character-appearance-production/CAPP-01_SOURCE_AUTHORITY_AND_PROFILE_INDEX_v0.1.0.json','scripts/validate-capp01-completion.py'):
        req(path in changed,'canonical merge missing '+path)

    print('CAPP-01 final-state validation: PASS')
    print('state=completed_verified profiles=25 choice_surfaces=10 stable_choice_ids=180')
    print('evidence=head '+HEAD+' workflows=72/72 PR=299 merge='+MERGE+' signature=verified_valid')
    print('next=CAPP-02 planned_not_activated runtime_activation=false')

if __name__=='__main__': main()
