#!/usr/bin/env python3
from __future__ import annotations
import json, subprocess, sys
from pathlib import Path
R=Path(__file__).resolve().parents[1]
B=R/'governance/application-planning/character-appearance-production'
P=R/'governance/application-planning/parallel-preimplementation'
def load(p): return json.loads(p.read_text(encoding='utf-8'))
def req(x,m):
 if not x: raise SystemExit('CAPP-01 foundation FAILED: '+m)
check=subprocess.run([sys.executable,str(R/'scripts/generate-capp01-registry.py'),'--check'],cwd=R,text=True,capture_output=True)
req(check.returncode==0,'generated artifacts are stale: '+check.stdout+check.stderr)
m=load(P/'PPIA-06_SPECIES_MORPHOLOGY_PROFILES_v0.1.0.json'); st=load(P/'PPIA-06_APPEARANCE_STUDIO_CONTROL_SURFACE_v0.1.0.json')
s=load(B/'CAPP-01_SOURCE_AUTHORITY_AND_PROFILE_INDEX_v0.1.0.json'); r=load(B/'CAPP-01_APPEARANCE_CHOICE_REGISTRY_v0.1.0.json'); c=load(B/'CAPP-01_CONSTRAINT_MODEL_v0.1.0.json')
back=load(B/'CAPP_PROGRAM_BACKLOG.json'); cp=load(R/'governance/ai/work-state/CAPP-01-attempt-001.json'); ptr=load(R/'governance/ai/runtime/CURRENT_WORK_POINTER.json'); compact=load(R/'governance/ai/runtime/CURRENT_IMPLEMENTATION_STATUS.json')
expected=[p['species'] for p in m['profiles']]
req(m['profile_count']==25 and len(expected)==25,'upstream canonical profile count')
req(s['profile_count']==25 and [p['species'] for p in s['profiles']]==expected,'source index must mirror canonical PPIA-06 profile order')
for src,out in zip(m['profiles'],s['profiles']):
 for key in ('written_source','baseline_topology','visual_summary','required_features','bounded_variation','appearance_state_model','special_customizer_behavior','unresolved_visual_conflicts'):
  req(out[key]==src[key],out['species']+' source mirror mismatch: '+key)
 req(out['owner_canon_ids']==src['owner_canon'],out['species']+' owner-canon IDs mismatch')
req(r['profile_count']==25 and [p['species'] for p in r['profiles']]==expected,'registry profile coverage/order')
expected_surfaces=['P06-UI-002','P06-UI-003','P06-UI-004','P06-UI-005','P06-UI-006','P06-UI-007','P06-UI-008','P06-UI-009','P06-UI-010','P06-UI-011']
req([x['surface_id'] for x in r['choice_surfaces']]==expected_surfaces,'choice surfaces must be canonical PPIA-06 Studio surfaces')
ui={x['id']:x for x in st['inspector_sections']}
for x in r['choice_surfaces']:
 req(x['semantic_layer_refs']==ui[x['surface_id']]['layers'],x['surface_id']+' semantic-layer mismatch')
 req(x['mode']==ui[x['surface_id']]['mode'],x['surface_id']+' mode mismatch')
ids=[]
by_m={p['species']:p for p in m['profiles']}
for p in r['profiles']:
 src=by_m[p['species']]
 req([x['value'] for x in p['required_feature_contracts']]==src['required_features'],p['species']+' required-feature contracts')
 req([x['statement'] for x in p['bounded_choice_contracts']]==src['bounded_variation'],p['species']+' bounded-choice contracts')
 ids += [x['choice_id'] for x in p['required_feature_contracts']] + [x['choice_id'] for x in p['bounded_choice_contracts']]
 for v in p['explicit_choice_contracts'].values(): ids.append(v['stable_id'])
 req(len(p['surface_eligibility'])==10,p['species']+' surface eligibility coverage')
 req(p['renderer_requirement']['unsupported_does_not_invalidate_identity'] is True,p['species']+' renderer independence')
req(len(ids)==len(set(ids)),'choice IDs must be unique')
rb={p['species']:p for p in r['profiles']}
req(rb['Giantkin']['explicit_choice_contracts']['lineage']['values']==['Grendelkin','Surtrborn','Daityr'],'Giantkin canonical lineages')
req(rb['Vespin']['explicit_choice_contracts']['topology']['arms']==4,'Vespin four-arm owner canon')
req(rb['Moravi']['explicit_choice_contracts']['topology']['legs']==4,'Moravi four-leg topology')
req(rb['Arborae']['explicit_choice_contracts']['season_profiles']['values']==['spring','summer','autumn','winter'],'Arborae season profiles')
req(rb['Nekron']['explicit_choice_contracts']['ascension']['transition_count_max']==1,'Nekron one-time transition')
req(rb['ManyToms']['explicit_choice_contracts']['constituent_identity']['design_once_replicate'] is True,'ManyToms composite identity')
req([p['species'] for p in c['profile_contracts']]==expected,'constraint profile coverage/order')
req(c['outcomes']==['eligible','read_only','unavailable','unknown','invalid_requires_review'],'constraint outcomes')
req(c['renderer_support_states']==['supported','partial','unsupported','unknown'],'renderer support states')
req(c['morphology_graph_contract']['rules'][0]=='No implicit humanoid limb count.','morphology graph no-humanoid-default rule')
item=next(x for x in back['work_items'] if x['id']=='CAPP-01')
req(back['status']=='owner_approved_active_parallel_work','CAPP program active state')
req(item['status'] in {'in_progress','completed_verified'},'CAPP backlog lifecycle state')
req(cp['status'] in {'started','completed_verified'},'CAPP-01 checkpoint lifecycle state')
req(ptr['primary_attempt_id']=='CAPP-01-attempt-001','CAPP-01 conversational primary')
req(compact['primary']['attempt_id']=='CAPP-01-attempt-001','CAPP-01 compact status')
req(compact['primary']['status']==cp['status'],'CAPP-01 compact/checkpoint lifecycle mismatch')
if cp['status']=='completed_verified':
 req(item['status']=='completed_verified','completed checkpoint requires completed backlog state')
 req(cp['active_substep'] is None and cp['roadmap_projection_pending'] is False,'completed checkpoint closure state')
 req(next(x for x in back['work_items'] if x['id']=='CAPP-02')['status']=='planned','CAPP-02 must remain planned after CAPP-01 completion')
else:
 req(item['status']=='in_progress' and cp['status']=='started','CAPP-01 active foundation state')
req(any(a['attempt_id']=='DS-008-working-series-attempt-002' and a['status']=='blocked_non_owner' for a in ptr['active_attempts']),'DS-008 boundary preserved')
req(any(t['track']=='application-implementation' and t['next_work_item_id']=='STAGE-A-A2' for t in ptr['deferred_tracks']),'A2 boundary preserved')
for k,v in back['boundaries'].items(): req(v is False,'unauthorized CAPP boundary: '+k)
print('CAPP-01 foundation validation: PASS')
print('canonical_profiles=25 choice_surfaces=10 stable_choice_ids='+str(len(ids)))
