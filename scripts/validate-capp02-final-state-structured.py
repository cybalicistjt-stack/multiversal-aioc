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
    if not x: raise SystemExit('CAPP-02 structured final-state FAILED: '+m)
def git(*args):
    p=subprocess.run(['git',*args],cwd=R,text=True,capture_output=True)
    req(p.returncode==0,f"git {' '.join(args)} failed")
    return p.stdout

def main():
    receipt=load(B/'CAPP-02_VERIFIED_COMPLETION_RECEIPT_v1.0.0.json')
    backlog=load(B/'CAPP_PROGRAM_BACKLOG.json')
    cp=load(R/'governance/ai/work-state/CAPP-02-attempt-001.json')
    ptr=load(R/'governance/ai/runtime/CURRENT_WORK_POINTER.json')
    status=load(R/'governance/ai/runtime/CURRENT_IMPLEMENTATION_STATUS.json')
    items={x['id']:x for x in backlog['work_items']}
    req(receipt['state']=='completed_verified','receipt state')
    req(receipt['exact_validated_head']==HEAD and receipt['applicable_pull_request_workflows']=='72/72','candidate evidence')
    req(receipt['pull_request']==301 and receipt['merge_commit']==MERGE and receipt['merge_verification']=='verified valid','merge evidence')
    req(all(v is False for v in receipt['boundaries'].values()),'receipt boundaries')
    req(items['CAPP-02']['status']=='completed_verified','backlog state')
    req(cp['status']=='completed_verified' and cp['latest_pushed_commit']==HEAD and cp['merge_commit']==MERGE and cp['pull_request']==301,'checkpoint evidence')
    req(cp['unresolved_failures']==[] and cp['owner_decision_required'] is False,'checkpoint closure')
    req(any(x.get('kind')=='merge' and MERGE in x.get('value','') for x in cp['evidence']),'scoped merge evidence')
    req(any(x.get('attempt_id')=='PPIA-16-attempt-001' and x.get('status')=='completed_verified' for x in ptr['active_attempts']),'PPIA completion anchor')
    req(any(x.get('attempt_id')=='DS-008-working-series-attempt-002' and x.get('status')=='blocked_non_owner' for x in ptr['active_attempts']),'DS-008 preserved')
    req(any(x.get('track')=='application-implementation' and x.get('next_work_item_id')=='STAGE-A-A2' for x in ptr['deferred_tracks']),'A2 preserved')
    req(status['primary']['status'] in {'completed_verified','started','in_progress'},'compact lifecycle state')
    req(all(v is False for v in backlog['boundaries'].values()),'program boundaries')
    git('merge-base','--is-ancestor',MERGE,'HEAD')
    changed=set(x for x in git('show','--pretty=','--name-only',MERGE).splitlines() if x)
    for path in ('governance/application-planning/character-appearance-production/CAPP-02_PRESET_RANDOMIZATION_LOCK_LIBRARY_v0.1.0.json','governance/application-planning/character-appearance-production/CAPP-02_COMPLETION_REPORT.md','tools/capp02_randomization_reference.py','scripts/validate-capp02-completion.py'):
        req(path in changed,'canonical merge missing '+path)
    print('CAPP-02 structured final-state validation: PASS')
    print('Completion truth comes from structured receipt/checkpoint/backlog evidence; prose wording is non-authoritative.')

if __name__=='__main__': main()
