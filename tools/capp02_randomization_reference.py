#!/usr/bin/env python3
from __future__ import annotations
import argparse, hashlib, json, re, unicodedata
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
B=ROOT/'governance/application-planning/character-appearance-production'
REG=B/'CAPP-01_APPEARANCE_CHOICE_REGISTRY_v0.1.0.json'
LIB=B/'CAPP-02_PRESET_RANDOMIZATION_LOCK_LIBRARY_v0.1.0.json'
def load(p): return json.loads(p.read_text(encoding='utf-8'))
def slug(s): return re.sub(r'[^a-z0-9]+','-',s.lower()).strip('-')
def root_digest(pid,state,version,recipe,seed):
    vals=[unicodedata.normalize('NFC',x) for x in (pid,state,version,recipe,seed)]
    text=json.dumps(vals,separators=(',',':'),ensure_ascii=False)
    return hashlib.sha256(text.encode()).hexdigest()
def pick(root,cid,values,weights):
    raw=(root+'|'+cid+'|0').encode()
    n=int.from_bytes(hashlib.sha256(raw).digest(),'big'); r=n%sum(weights); c=0
    for v,w in zip(values,weights):
        c+=w
        if r<c:return v
    raise AssertionError('selection')
def materialize(pid,seed,recipe='CAPP02-RCP-RANDOMIZE-ALL',locks=None,conditions=None,include=None):
    reg,lib=load(REG),load(LIB); locks=set(locks or ()); conditions=conditions or {}
    p=next((x for x in reg['profiles'] if x['profile_id']==pid),None)
    if not p: raise KeyError(pid)
    if recipe not in {x['id'] for x in lib['recipes']}: raise KeyError(recipe)
    ver=lib['eligible_set']['version']; root=root_digest(pid,p['appearance_state_model'],ver,recipe,seed)
    ov=next((x for x in lib['profiles'] if x['species']==p['species']),{})
    selected={}; diag=[]
    pools=[(x,False) for x in ov.get('pools',[])]+[(x,True) for x in ov.get('conditional_pools',[])]
    for pool,conditional in sorted(pools,key=lambda x:x[0]['choice_id']):
        cid=pool['choice_id']
        if include is not None and cid not in include: continue
        if cid in locks: diag.append({'choice_id':cid,'code':'choice_locked'}); continue
        if conditional and conditions.get(cid) is not True:
            diag.append({'choice_id':cid,'code':'choice_condition_unresolved'}); continue
        selected[cid]=pick(root,cid,pool['values'],pool['weights'])
    if not selected and not diag: diag.append({'choice_id':None,'code':'no_concrete_source_values'})
    return {'preset_id':f"CAPP02-REF-{slug(p['species']).upper()}-001",'schema_id':lib['preset']['schema'],'profile_id':pid,'appearance_state_model':p['appearance_state_model'],'eligible_choice_set_version':ver,'authored_choices':selected,'locks':sorted(locks),'recipe_id':recipe,'seed':seed,'provenance':'synthetic_noncanonical_reference','root_digest':root,'diagnostics':diag}
def materialize_catalog():
    reg,lib=load(REG),load(LIB); c=lib['synthetic']['coverage']; out=[]
    for p in reg['profiles']:
        out.append(materialize(p['profile_id'],c['seed_template'].format(profile_id=p['profile_id']),c['recipe']))
    return {'schema_version':'0.1.0','work_item_id':'CAPP-02','profile_count':len(out),'provenance':'synthetic_noncanonical_reference','presets':out,'special_cases':lib['synthetic']['special_cases']}
def cli():
    a=argparse.ArgumentParser(); a.add_argument('--profile-id'); a.add_argument('--seed'); a.add_argument('--recipe-id',default='CAPP02-RCP-RANDOMIZE-ALL'); a.add_argument('--lock',action='append',default=[]); a.add_argument('--condition-true',action='append',default=[]); a.add_argument('--include-choice-id',action='append'); a.add_argument('--emit-catalog',action='store_true'); x=a.parse_args()
    if x.emit_catalog:o=materialize_catalog()
    else:
        if not x.profile_id or x.seed is None:a.error('--profile-id and --seed required')
        o=materialize(x.profile_id,x.seed,x.recipe_id,set(x.lock),{v:True for v in x.condition_true},None if x.include_choice_id is None else set(x.include_choice_id))
    print(json.dumps(o,indent=2,sort_keys=True,ensure_ascii=False))
if __name__=='__main__':cli()
