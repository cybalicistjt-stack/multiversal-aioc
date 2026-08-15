#!/usr/bin/env python3
from __future__ import annotations
import json, subprocess
from pathlib import Path
R=Path(__file__).resolve().parents[1]
B=R/'governance/application-planning/character-appearance-production'
HEAD='ce0d9ffd8784619b7d7ffccdc5c64a3b15dee447'
MERGE='b8c05844ca2df6218cd2c9b0f75a384f3d8eb74c'

def load(p): return json.loads(p.read_text(encoding='utf-8'))
def req(x,m):
    if not x: raise SystemExit('CAPP-01 structured final-state FAILED: '+m)
def git(*args):
    p=subprocess.run(['git',*args],cwd=R,text=True,capture_output=True)
    req(p.returncode==0,f"git {' '.join(args)} failed")
    return p.stdout

def main():
    receipt=load(B/'CAPP-01_VERIFIED_COMPLETION_RECEIPT_v1.0.0.json')
    backlog=load(B/'CAPP_PROGRAM_BACKLOG.json')
    cp=load(R/'governance/ai/work-state/CAPP-01-attempt-001.json')
    ppia=load(R/'governance/ai/work-state/PPIA-16-attempt-001.json')
    ptr=load(R/'governance/ai/runtime/CURRENT_WORK_POINTER.json')
    registry=load(B/'CAPP-01_APPEARANCE_CHOICE_REGISTRY_v0.1.0.json')
    items={x['id']:x for x in backlog['work_items']}
    req(receipt['state']=='completed_verified','receipt state')
    req(receipt['exact_validated_head']==HEAD and receipt['applicable_pull_request_workflows']=='72/72','candidate evidence')
    req(receipt['pull_request']==299 and receipt['merge_commit']==MERGE and receipt['merge_verification']=='verified valid','merge evidence')
    req(all(v is False for v in receipt['boundaries'].values()),'receipt boundaries')
    req(items['CAPP-01']['status']=='completed_verified','backlog state')
    req(cp['status']=='completed_verified' and cp['latest_pushed_commit']==HEAD and cp['merge_commit']==MERGE and cp['pull_request']==299,'checkpoint evidence')
    req(cp['unresolved_failures']==[] and cp['owner_decision_required'] is False,'checkpoint closure')
    # PPIA is a closed immutable predecessor, not a permanent live-pointer occupant.
    req(ppia['work_item_id']=='PPIA-16' and ppia['status']=='completed_verified' and ppia['completed_at'],'PPIA completion anchor')
    req(any(x.get('attempt_id')=='DS-008-working-series-attempt-002' and x.get('status')=='blocked_non_owner' for x in ptr['active_attempts']),'DS-008 preserved')
    app_tracks=[x for x in ptr['deferred_tracks'] if x.get('track')=='application-implementation']
    req(len(app_tracks)==1 and app_tracks[0].get('next_work_item_id','').startswith('STAGE-A-A'),'current Stage A routing preserved')
    req(registry['profile_count']==25 and registry['choice_surface_count']==10,'registry counts')
    ids=[]
    for profile in registry['profiles']:
        ids += [x['choice_id'] for x in profile['required_feature_contracts']]
        ids += [x['choice_id'] for x in profile['bounded_choice_contracts']]
        ids += [x['stable_id'] for x in profile['explicit_choice_contracts'].values()]
    req(len(ids)==180 and len(set(ids))==180,'stable choice ids')
    req(all(v is False for v in backlog['boundaries'].values()),'program boundaries')
    git('merge-base','--is-ancestor',MERGE,'HEAD')
    changed=set(x for x in git('show','--pretty=','--name-only',MERGE).splitlines() if x)
    for path in ('governance/application-planning/character-appearance-production/CAPP-01_APPEARANCE_CHOICE_REGISTRY_v0.1.0.json','governance/application-planning/character-appearance-production/CAPP-01_CONSTRAINT_MODEL_v0.1.0.json','governance/application-planning/character-appearance-production/CAPP-01_SOURCE_AUTHORITY_AND_PROFILE_INDEX_v0.1.0.json','scripts/validate-capp01-completion.py'):
        req(path in changed,'canonical merge missing '+path)
    print('CAPP-01 structured final-state validation: PASS')
    print('Completion truth comes from structured receipt/checkpoint/backlog evidence; prose wording is non-authoritative.')

if __name__=='__main__': main()
