#!/usr/bin/env python3
from __future__ import annotations
import json, subprocess
from pathlib import Path
R=Path(__file__).resolve().parents[1]
B=R/'governance/application-planning/character-appearance-production'
HEAD='c1dd19cc7793fe3605f601280c4a2b82268b4a0a'
MERGE='7fbe37fd5914bdc60f125064a11c15f6cee9d8bb'

def load(p): return json.loads(p.read_text(encoding='utf-8'))
def req(x,m):
    if not x: raise SystemExit('CAPP-02 final-state FAILED: '+m)
def git(*args):
    p=subprocess.run(['git',*args],cwd=R,text=True,capture_output=True)
    req(p.returncode==0,f"git {' '.join(args)}: {p.stdout}{p.stderr}")
    return p.stdout

def main():
    receipt=load(B/'CAPP-02_VERIFIED_COMPLETION_RECEIPT_v1.0.0.json')
    lib=load(B/'CAPP-02_PRESET_RANDOMIZATION_LOCK_LIBRARY_v0.1.0.json')
    backlog=load(B/'CAPP_PROGRAM_BACKLOG.json')
    cp=load(R/'governance/ai/work-state/CAPP-02-attempt-001.json')
    ptr=load(R/'governance/ai/runtime/CURRENT_WORK_POINTER.json')
    status=load(R/'governance/ai/runtime/CURRENT_IMPLEMENTATION_STATUS.json')
    report=(B/'CAPP-02_COMPLETION_REPORT.md').read_text(encoding='utf-8')

    req(receipt['state']=='completed_verified','receipt state')
    req(receipt['exact_validated_head']==HEAD and receipt['applicable_pull_request_workflows']=='72/72','exact candidate evidence')
    req(receipt['pull_request']==301 and receipt['merge_commit']==MERGE and receipt['merge_verification']=='verified valid','PR/merge evidence')
    req(receipt['delivered']=={'governed_profiles':25,'recipes':3,'profile_specific_policies':19,'concrete_source_backed_pools':5,'special_reference_cases':20,'fixed_deterministic_vectors':3,'effective_synthetic_presets':25},'delivered counts')
    req(receipt['next_work_item']=={'id':'CAPP-03','state':'planned_not_activated'},'next item boundary')
    req(all(v is False for v in receipt['boundaries'].values()),'receipt boundaries')

    items={x['id']:x for x in backlog['work_items']}
    req(items['CAPP-01']['status']=='completed_verified' and items['CAPP-02']['status']=='completed_verified' and items['CAPP-03']['status']=='planned','backlog lifecycle')
    req(backlog['completed_work_items']>=2 and backlog['active_work_item_id'] is None and backlog['next_planned_work_item_id']=='CAPP-03','program projection')
    req(backlog['last_completed']['work_item_id']=='CAPP-02' and backlog['last_completed']['exact_validated_head']==HEAD and backlog['last_completed']['pull_request']==301 and backlog['last_completed']['merge_commit']==MERGE,'backlog completion evidence')
    req(all(v is False for v in backlog['boundaries'].values()),'program boundaries')

    req(cp['status']=='completed_verified' and cp['completed_at'],'checkpoint final state')
    req(cp['latest_pushed_commit']==HEAD and cp['expected_remote_head']==MERGE and cp['pull_request']==301 and cp['merge_commit']==MERGE,'checkpoint exact evidence')
    req(cp['active_substep'] is None and cp['unresolved_failures']==[] and cp['owner_decision_required'] is False and cp['roadmap_projection_pending'] is False,'checkpoint closure')
    req(any(x.get('status')=='passed' and '72/72' in x.get('evidence','') for x in cp['validation']),'hosted validation evidence')
    req(any(x.get('kind')=='merge' and MERGE in x.get('value','') for x in cp['evidence']),'merge evidence kind')

    selected=[x for x in ptr['active_attempts'] if x.get('owner_selected')]
    req(len(selected)==1 and selected[0]['attempt_id']=='CAPP-02-attempt-001' and selected[0]['status']=='completed_verified','selected completion anchor')
    req(ptr['primary_attempt_id']=='CAPP-02-attempt-001','pointer primary')
    req(status['primary']['work_item_id']=='CAPP-02' and status['primary']['status']=='completed_verified','compact primary')
    req(status['active_attempt_count']==1,'only DS-008 remains unfinished active attempt')
    req(any(x.get('attempt_id')=='CAPP-01-attempt-001' and x.get('status')=='completed_verified' for x in ptr['active_attempts']),'CAPP-01 anchor')
    req(any(x.get('attempt_id')=='PPIA-16-attempt-001' and x.get('status')=='completed_verified' for x in ptr['active_attempts']),'PPIA-16 anchor')
    req(any(x.get('attempt_id')=='DS-008-working-series-attempt-002' and x.get('status')=='blocked_non_owner' for x in ptr['active_attempts']),'DS-008 preserved')
    req(any(x.get('track')=='application-implementation' and x.get('next_work_item_id')=='STAGE-A-A2' for x in ptr['deferred_tracks']),'A2 preserved')
    req('historically batched/pending and is now complete' in ptr['selection_reason'],'PPIA provenance retained')

    req(lib['status']=='completion_candidate','candidate library remains historical package state')
    req(lib['seed']['algorithm']=='sha256-counter-v1' and lib['eligible_set']['no_fabricated_values'] is True,'determinism/no invention')
    req(len(lib['profiles'])==19 and len(lib['synthetic']['special_cases'])==20 and len(lib['synthetic']['vectors'])==3,'library counts')
    req('NOT COMPLETED_VERIFIED' in report,'candidate report historical boundary retained')

    git('merge-base','--is-ancestor',MERGE,'HEAD')
    message=git('show','-s','--format=%B',MERGE)
    req(HEAD in message and ('72/72' in message or 'all 72 applicable' in message) and 'CAPP-02' in message,'canonical merge message evidence')
    changed=set(x for x in git('show','--pretty=','--name-only',MERGE).splitlines() if x)
    for path in ('governance/application-planning/character-appearance-production/CAPP-02_PRESET_RANDOMIZATION_LOCK_LIBRARY_v0.1.0.json','governance/application-planning/character-appearance-production/CAPP-02_COMPLETION_REPORT.md','tools/capp02_randomization_reference.py','scripts/validate-capp02-completion.py'):
        req(path in changed,'canonical merge missing '+path)

    print('CAPP-02 final-state validation: PASS')
    print('state=completed_verified profiles=25 recipes=3 policies=19 pools=5 special_cases=20 vectors=3 effective_presets=25')
    print('evidence=head '+HEAD+' workflows=72/72 PR=301 merge='+MERGE+' signature=verified_valid')
    print('next=CAPP-03 planned_not_activated runtime_activation=false')

if __name__=='__main__': main()
