#!/usr/bin/env python3
from __future__ import annotations
import json, subprocess, sys
from pathlib import Path
R=Path(__file__).resolve().parents[1]
B=R/'governance/application-planning/character-appearance-production'
def load(p): return json.loads(p.read_text(encoding='utf-8'))
def req(x,m):
 if not x: raise SystemExit('CAPP-01 completion FAILED: '+m)
def run(path,*args):
 p=subprocess.run([sys.executable,str(R/path),*args],cwd=R,text=True,capture_output=True)
 req(p.returncode==0,f"{path} {' '.join(args)}: {p.stdout}{p.stderr}")
 return p.stdout.strip()
run('scripts/generate-capp01-registry.py','--check')
foundation=run('scripts/validate-capp01-foundation.py')
run('scripts/sync-capp-roadmap-index.py','--check')
m=load(B/'CAPP-01_COMPLETION_ACCEPTANCE_MATRIX_v0.1.0.json')
pkg=load(B/'CAPP-01_COMPLETION_PACKAGE_INDEX_v0.1.0.json')
registry=load(B/'CAPP-01_APPEARANCE_CHOICE_REGISTRY_v0.1.0.json')
constraints=load(B/'CAPP-01_CONSTRAINT_MODEL_v0.1.0.json')
index=load(R/'governance/ai/runtime/ROADMAP_INDEX.json')
backlog=load(B/'CAPP_PROGRAM_BACKLOG.json')
ptr=load(R/'governance/ai/runtime/CURRENT_WORK_POINTER.json')
cp=load(R/'governance/ai/work-state/CAPP-01-attempt-001.json')
report=(B/'CAPP-01_COMPLETION_REPORT.md').read_text(encoding='utf-8')
correction=(B/'CAPP-01_CANONICAL_SOURCE_CORRECTION.md').read_text(encoding='utf-8')
req(m['candidate_summary']=={'checks':20,'pass_candidate':20,'failed':0,'completion_claim':False},'acceptance summary')
checks=m['acceptance_checks']; req(len(checks)==20 and len({x['id'] for x in checks})==20,'20 unique acceptance checks')
req(all(x['status']=='pass_candidate' for x in checks),'all acceptance checks candidate-pass')
req(pkg['completion_claim'] is False and len(pkg['completion_evidence_pending'])==6,'package must remain non-complete before merge')
req(registry['profile_count']==25 and registry['choice_surface_count']==10,'registry cardinalities')
ids=[]
for p in registry['profiles']:
 ids += [x['choice_id'] for x in p['required_feature_contracts']]
 ids += [x['choice_id'] for x in p['bounded_choice_contracts']]
 ids += [x['stable_id'] for x in p['explicit_choice_contracts'].values()]
req(len(ids)==180 and len(ids)==len(set(ids)),'exact 180 unique current stable choice IDs')
req(constraints['morphology_graph_contract']['rules'][0]=='No implicit humanoid limb count.','no implicit humanoid topology')
req('unknown' in constraints['outcomes'] and 'invalid_requires_review' in constraints['outcomes'],'explicit failure states')
req(constraints['renderer_support_states']==['supported','partial','unsupported','unknown'],'renderer state contract')
req(len([x for x in index['entries'] if x['work_item_id'].startswith('CAPP-')])==12,'exact 12 CAPP roadmap-index entries')
req([x['work_item_id'] for x in index['entries'] if x['work_item_id'].startswith('CAPP-')]==[f'CAPP-{i:02d}' for i in range(1,13)],'CAPP roadmap-index order')
req(backlog['status']=='owner_approved_active_parallel_work','CAPP program active')
req(next(x for x in backlog['work_items'] if x['id']=='CAPP-01')['status'] in {'in_progress','ready_for_review'},'CAPP-01 review-state compatible')
req(ptr['primary_attempt_id']=='CAPP-01-attempt-001','CAPP-01 primary during review')
req(cp['status'] in {'started','ready_for_review'},'checkpoint review-state compatible')
req(any(a['attempt_id']=='DS-008-working-series-attempt-002' and a['status']=='blocked_non_owner' for a in ptr['active_attempts']),'DS-008 preserved')
req(any(t['track']=='application-implementation' and t['next_work_item_id']=='STAGE-A-A2' for t in ptr['deferred_tracks']),'A2 preserved')
for k,v in backlog['boundaries'].items(): req(v is False,'unauthorized boundary '+k)
req('31702343075' in report and '31703091730' in report and '31703316324' in report,'source-correction evidence in report')
req('legacy profile reconstruction' in correction and '31702343075' in correction,'source correction record')
req('NOT COMPLETED_VERIFIED' in report,'pre-merge completion boundary missing')
trigger=B/'CAPP-01_VALIDATION_TRIGGER.txt'
req(not trigger.exists(),'temporary validation trigger must be removed before completion gate')
print('CAPP-01 completion candidate validation: PASS')
print('checks=20 profiles=25 choice_surfaces=10 stable_choice_ids=180 roadmap_entries=12')
print(foundation.splitlines()[-1] if foundation else '')
