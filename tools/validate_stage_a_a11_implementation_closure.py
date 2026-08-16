#!/usr/bin/env python3
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
def load(path): return json.loads((ROOT/path).read_text(encoding='utf-8'))
def need(ok,msg):
    if not ok: raise SystemExit(f'A11 implementation closure FAIL: {msg}')
r=load('governance/application-planning/stage-a-a11/implementation-closure/STAGE_A_A11_IMPLEMENTATION_COMPLETION_RECEIPT.json')
w=load('governance/ai/work-state/STAGE-A-A11-implementation-attempt-001.json')
p=load('governance/ai/runtime/CURRENT_WORK_POINTER.json')
s=load('governance/ai/runtime/CURRENT_IMPLEMENTATION_STATUS.json')
i=load('governance/ai/runtime/ROADMAP_INDEX_STAGE_A_A11_SUPPLEMENT.json')['entries'][0]
need(r['status']=='completed_verified','receipt state')
need(r['application_pull_request']==149,'app PR')
need(r['application_merge_commit']=='bf54f36737fe02041f02ab44a69f45c3b0b294ac','app merge SHA')
need(r['application_merge_signature_verified'] is True,'verified merge signature')
need(r['construction']['all_slices_before_checks'] is True,'construction-before-checks')
need((r['construction']['slice_count'],r['construction']['source_fixture_count'],r['construction']['blocking_source_acceptance_key_count'],r['construction']['planned_provider_neutral_contract_count'])==(24,72,76,26),'24/72/76/26 accounting')
need(r['construction']['unpublished_acceptance_text_invented'] is False,'criterion prose integrity')
need(r['exact_head_validation']['conclusion']=='success' and r['exact_head_validation']['all_companions_passed'] is True,'exact-head validation')
b=r['headed_browser_evidence']
need(b['product_sha']==r['application_merge_commit'],'browser exact product SHA')
need(b['run_id']==31934719569 and b['job_id']==95134737004 and b['conclusion']=='success','browser run')
need(b['headed_chromium'] is True and b['exact_product_sha_proved_before_and_after'] is True,'real browser exact-SHA proof')
need(b['artifact_id']==9260312052 and b['artifact_digest']=='sha256:bc0d683f51e3d809b6353eff8dc23e4a992ef1c51e5ef95568af616edcee9dd7','browser artifact')
need(all(v is False for v in r['restrictions'].values()),'restricted authorities remain false')
need(w['status']=='completed_verified' and w['application_merge_commit']==r['application_merge_commit'],'work-state projection')
need(p['primary_attempt_id']==w['attempt_id'] and p['active_attempts'][0]['status']=='completed_verified','pointer projection')
need(p['deferred_tracks'][0]['next_work_item_id']=='STAGE-A-A12' and p['deferred_tracks'][0]['state']=='requires_current_repository_revalidation','A12 revalidation next')
need(s['primary']['attempt_id']==w['attempt_id'] and s['primary']['status']=='completed_verified','status projection')
need(i['implementation_state']=='completed_verified' and i['headed_browser_evidence_run']==31934719569,'roadmap supplement projection')
print('STAGE-A-A11 implementation closure: PASS')
