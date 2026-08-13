#!/usr/bin/env python3
from __future__ import annotations
import importlib.util,json,subprocess
from pathlib import Path
R=Path(__file__).resolve().parents[1]; B=R/'governance/application-planning/character-appearance-production'
BASE='eac1baf9951bb80dd925d4eeba92395b8b49dceb'
def load(p):return json.loads(p.read_text(encoding='utf-8'))
def req(x,m):
    if not x:raise SystemExit('CAPP-02 completion FAILED: '+m)
def git(*a):
    p=subprocess.run(['git',*a],cwd=R,text=True,capture_output=True); req(p.returncode==0,'git '+' '.join(a)+': '+p.stdout+p.stderr); return p.stdout
spec=importlib.util.spec_from_file_location('ref',R/'tools/capp02_randomization_reference.py'); ref=importlib.util.module_from_spec(spec); spec.loader.exec_module(ref)
reg=load(B/'CAPP-01_APPEARANCE_CHOICE_REGISTRY_v0.1.0.json'); con=load(B/'CAPP-01_CONSTRAINT_MODEL_v0.1.0.json'); lib=load(B/'CAPP-02_PRESET_RANDOMIZATION_LOCK_LIBRARY_v0.1.0.json')
back=load(B/'CAPP_PROGRAM_BACKLOG.json'); cp=load(R/'governance/ai/work-state/CAPP-02-attempt-001.json'); ptr=load(R/'governance/ai/runtime/CURRENT_WORK_POINTER.json'); st=load(R/'governance/ai/runtime/CURRENT_IMPLEMENTATION_STATUS.json'); report=(B/'CAPP-02_COMPLETION_REPORT.md').read_text()
req(reg['profile_count']==25 and len(reg['profiles'])==25,'25 CAPP-01 profiles')
req(lib['status']=='completion_candidate' and lib['eligible_set']['version']=='capp02-eligible-set-v1','library state/version')
req(lib['eligible_set']['no_fabricated_values'] is True and lib['eligible_set']['empty_pool']=='no_concrete_source_values','no invention')
req(lib['seed']['algorithm']=='sha256-counter-v1' and lib['seed']['python_random'] is False and lib['seed']['clock_entropy'] is False,'deterministic seed')
req(lib['weights']['default']=='uniform_source_neutral' and lib['weights']['nonuniform_requires_authority'] is True,'weight authority')
req({x['op'] for x in lib['recipes']}=={'randomize_all','randomize_unlocked','randomize_category'},'three recipes')
req(set(lib['preset']['forbidden'])=={'current_form','persistent_biology','active_biology','actual_equipment','renderer_asset_ids','live_pose','hidden_state'},'portable preset exclusions')
profiles={p['species']:p for p in reg['profiles']}; req(len(lib['profiles'])==19 and len({x['id'] for x in lib['profiles']})==19,'19 profile policies'); req({x['species'] for x in lib['profiles']}<=set(profiles),'policy species')
exp={'Arborae','Mythragara','Nekron','Suula','Furashin','ManyToms','Kola-Ha','Stygian','Vespin','Moravi','Rakuuta','Toba-Madra','Gray','The Free'}; req(exp<={x['species'] for x in lib['profiles']},'special policies')
explicit={}
for s,p in profiles.items():
    for _,c in p['explicit_choice_contracts'].items():explicit[c['stable_id']]=(s,c)
seen=set(); pools=0
for ov in lib['profiles']:
    for key in ('pools','conditional_pools'):
        for q in ov.get(key,[]):
            pools+=1; cid=q['choice_id']; req(cid not in seen,'duplicate pool '+cid); seen.add(cid); req(cid in explicit,'unknown pool '+cid); s,c=explicit[cid]; req(s==ov['species'],'pool/profile mismatch '+cid); req(len(q['values'])==len(q['weights']) and all(isinstance(w,int) and w>0 for w in q['weights']),'weights '+cid)
            if 'values' in c:req(q['values']==c['values'],'enumeration mismatch '+cid)
            else:req(c.get('eligibility')=='optional' and q['values']==['absent','present'],'optional-presence only '+cid)
req(pools==5,'five source-backed pools')
req(lib['synthetic']['coverage']['selector']=='all CAPP-01 profiles' and lib['synthetic']['coverage']['expected']==25,'synthetic all-profile coverage')
req(len(lib['synthetic']['special_cases'])==20 and len({x[0] for x in lib['synthetic']['special_cases']})==20,'20 special cases')
req(len(lib['synthetic']['vectors'])==3,'three fixed vectors')
cat=ref.materialize_catalog(); req(cat['profile_count']==25 and len(cat['presets'])==25,'25 effective presets'); req({x['profile_id'] for x in cat['presets']}=={x['profile_id'] for x in reg['profiles']},'effective profile coverage'); req(json.dumps(cat,sort_keys=True)==json.dumps(ref.materialize_catalog(),sort_keys=True),'deterministic catalog')
for v in lib['synthetic']['vectors']:
    got=ref.materialize(v['profile_id'],v['seed'],v['recipe']); req(got['root_digest']==v['root'],'vector root '+v['id']); req(got['authored_choices'].get(v['choice_id'])==v['value'],'vector value '+v['id'])
for p in cat['presets']:
    for cid,val in p['authored_choices'].items():
        req(cid in explicit,'materialized unknown id'); c=explicit[cid][1]; req((val in c['values']) if 'values' in c else (c.get('eligibility')=='optional' and val in {'absent','present'}),'materialized source bound')
        locked=ref.materialize(p['profile_id'],p['seed'],p['recipe_id'],{cid}); req(cid not in locked['authored_choices'] and any(d['code']=='choice_locked' and d['choice_id']==cid for d in locked['diagnostics']),'lock '+cid)
req({'unknown','unavailable','read_only'}<=set(con['outcomes']),'CAPP-01 exclusion states')
items={x['id']:x for x in back['work_items']}; req(items['CAPP-01']['status']=='completed_verified' and items['CAPP-02']['status'] in {'in_progress','ready_for_review'} and items['CAPP-03']['status']=='planned','CAPP lifecycle')
req(cp['status'] in {'started','ready_for_review'} and cp['active_substep'],'checkpoint candidate'); req(ptr['primary_attempt_id']=='CAPP-02-attempt-001' and sum(bool(x.get('owner_selected')) for x in ptr['active_attempts'])==1,'pointer primary'); req(st['primary']['attempt_id']=='CAPP-02-attempt-001' and st['primary']['status']==cp['status'] and st['active_attempt_count']==2,'compact status')
req(any(x['attempt_id']=='CAPP-01-attempt-001' and x['status']=='completed_verified' for x in ptr['active_attempts']),'CAPP-01 anchor'); req(any(x['attempt_id']=='PPIA-16-attempt-001' and x['status']=='completed_verified' for x in ptr['active_attempts']),'PPIA anchor'); req(any(x['attempt_id']=='DS-008-working-series-attempt-002' and x['status']=='blocked_non_owner' for x in ptr['active_attempts']),'DS-008'); req(any(x['track']=='application-implementation' and x['next_work_item_id']=='STAGE-A-A2' for x in ptr['deferred_tracks']),'A2')
req(all(v is False for v in back['boundaries'].values()) and all(v is False for v in lib['boundaries'].values()),'boundaries')
req('NOT COMPLETED_VERIFIED' in report and 'no_concrete_source_values' in report,'candidate report boundary')
git('merge-base','--is-ancestor',BASE,'HEAD'); changed=set(git('diff','--name-only',BASE,'HEAD').split())
need={'governance/application-planning/character-appearance-production/CAPP-02_PRESET_RANDOMIZATION_LOCK_LIBRARY_v0.1.0.json','governance/application-planning/character-appearance-production/CAPP-02_COMPLETION_REPORT.md','governance/application-planning/character-appearance-production/CAPP_PROGRAM_BACKLOG.json','governance/ai/work-state/CAPP-02-attempt-001.json','governance/ai/runtime/CURRENT_WORK_POINTER.json','governance/ai/runtime/CURRENT_IMPLEMENTATION_STATUS.json','tools/capp02_randomization_reference.py','scripts/validate-capp02-completion.py','.github/workflows/validate-capp-02-completion.yml'}
req(need<=changed,'changed-path coverage '+str(sorted(need-changed))); req(not any(x.startswith('src/') or x.startswith('app/') for x in changed),'no runtime paths')
print('CAPP-02 completion candidate validation: PASS')
print('profiles=25 recipes=3 policies=19 pools=5 special_cases=20 vectors=3 effective_presets=25')
print('deterministic=true no_fabricated_values=true runtime_activation=false')
