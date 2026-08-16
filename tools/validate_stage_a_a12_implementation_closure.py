#!/usr/bin/env python3
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
CP=ROOT/'governance/ai/work-state/STAGE-A-A12-implementation-attempt-001.json'
RECEIPT=ROOT/'governance/application-planning/stage-a-a12/implementation-closure/STAGE_A_A12_IMPLEMENTATION_COMPLETION_RECEIPT.json'
POINTER=ROOT/'governance/ai/runtime/CURRENT_WORK_POINTER.json'

read=lambda p: json.loads(p.read_text(encoding='utf-8'))

def main():
    cp=read(CP); r=read(RECEIPT); p=read(POINTER)
    assert cp['status']=='completed_verified'
    assert cp['attempt_id']=='STAGE-A-A12-implementation-attempt-001'
    assert cp['latest_pushed_commit']=='47a060c70f23bf5b60226f1aaa433bf301fa24db'
    assert all(x['status']=='passed' for x in cp['validation'])
    assert not cp['unresolved_failures'] and cp['owner_decision_required'] is False
    assert r['state']=='completed_verified' and r['candidate_state']=='candidate-validated'
    assert r['release_approved'] is False and r['owner_decisions_resolved'] is False
    assert r['validated_evidence_head']=='56b127f1fc01eebe5c73ba0472a5b6496fe92b5e'
    assert r['final_validation']['run_id']==31938591853 and r['artifact']['id']==9261392785
    assert r['application_merge_commit']=='4a488f366058c4b63af9f897744388cc77688763'
    assert r['application_closure_merge']=='47a060c70f23bf5b60226f1aaa433bf301fa24db'
    assert p['primary_attempt_id']=='STAGE-A-A12-implementation-attempt-001'
    assert not any(x.get('state')=='authorized_not_activated' and x.get('next_work_item_id')=='STAGE-A-A12' for x in p['deferred_tracks'])
    print('STAGE-A-A12 IMPLEMENTATION CLOSURE: PASS')
    print('candidate=candidate-validated release_approved=false owner_decisions=unresolved')
    return 0

if __name__=='__main__': raise SystemExit(main())
