#!/usr/bin/env python3
from __future__ import annotations
import argparse,json,re
from collections import Counter
from pathlib import Path
R=Path(__file__).resolve().parents[1]
C=R/'governance/application-planning/character-appearance-production'
STATES=('supported','partial','unsupported','unknown')
RANK={'supported':3,'partial':2,'unsupported':1,'unknown':0}

def load(p): return json.loads(Path(p).read_text(encoding='utf-8'))
def tid(x): return 'CAPP03-TOP-'+re.sub(r'[^A-Z0-9]+','-',x.upper()).strip('-')
def fail(m): raise ValueError(m)
def validate_manifest(m,contract,standard):
    missing=set(contract['manifest_required'])-set(m)
    if missing: fail('manifest missing '+','.join(sorted(missing)))
    if m['renderer_id']!='pixel-art-v1' or m['authorized_projection'] is not True: fail('renderer/authorization')
    seen=set()
    for a in m['assets']:
        miss=set(contract['asset_required'])-set(a)
        if miss: fail('asset fields '+','.join(sorted(miss)))
        key=(a['asset_id'],a['asset_version'])
        if key in seen: fail('duplicate asset version')
        seen.add(key)
        if a['artifact_state'] not in contract['artifact_states'] or a['support_state'] not in STATES: fail('asset state')
        if a['semantic_band'] not in standard['bands']: fail('semantic band')
        if not set(a['view_ids'])<=set(standard['canvases']): fail('view')
        if a['artifact_state']=='available':
            if not a.get('content_path') or not re.fullmatch(r'[0-9a-f]{64}',a.get('content_sha256','')): fail('available content evidence')
        if a['artifact_state']=='metadata_only' and a['support_state']=='supported': fail('metadata-only cannot support')
    return True

def resolve(states):
    return max(states,key=lambda x:RANK[x]) if states else 'unknown'
def aggregate(states):
    s=set(states)
    if s=={'supported'}: return 'supported'
    if s=={'unsupported'}: return 'unsupported'
    if s=={'unknown'} or not s: return 'unknown'
    return 'partial'
def analyze(m,registry,standard,contract):
    validate_manifest(m,contract,standard)
    cells={}
    for a in m['assets']:
        if a['artifact_state']!='available': continue
        for v in sorted(set(a['view_ids'])):
            for t in sorted(set(a['topology_template_ids'])):
                k=(v,a['semantic_band'],t)
                cells.setdefault(k,[]).append(a['support_state'])
    profiles=[]
    total=Counter()
    for p in sorted(registry['profiles'],key=lambda x:x['profile_id']):
        t=tid(p['topology_profile'])
        states=[]
        for v in standard['canvases']:
            for b in standard['bands']:
                state=resolve(cells.get((v,b,t),[]))
                states.append(state); total[state]+=1
        profiles.append({'profile_id':p['profile_id'],'topology_template_id':t,'coverage_state':aggregate(states),'cell_counts':dict(Counter(states))})
    return {'schema_version':'0.1.0','work_item_id':'CAPP-04','renderer_id':'pixel-art-v1','authorized_projection':True,'profile_count':len(profiles),'cell_count':sum(total.values()),'coverage_state':aggregate(list(total.elements())),'cell_counts':dict(total),'profiles':profiles,'hidden_asset_counts_reported':False,'character_state_validity_affected':False}
def self_test():
    contract=load(C/'CAPP-04_ASSET_MANIFEST_CONTRACT_v0.1.0.json'); standard=load(C/'CAPP-03_PIXEL_ART_ASSET_PRODUCTION_STANDARD_v0.1.0.json'); reg=load(C/'CAPP-01_APPEARANCE_CHOICE_REGISTRY_v0.1.0.json')
    m={'manifest_id':'CAPP04-MANIFEST-TEST','manifest_version':'0.1.0','asset_pack_id':'test','asset_pack_version':'0.1.0','renderer_id':'pixel-art-v1','authorized_projection':True,'assets':[]}
    out=analyze(m,reg,standard,contract)
    assert out['profile_count']==25 and out['cell_count']==750 and out['coverage_state']=='unknown' and out['cell_counts']=={'unknown':750}
    print('CAPP-04 coverage self-test: PASS profiles=25 cells=750 empty_state=unknown')
def main():
    ap=argparse.ArgumentParser(); ap.add_argument('manifest',nargs='?'); ap.add_argument('--self-test',action='store_true'); args=ap.parse_args()
    if args.self_test or not args.manifest: return self_test()
    out=analyze(load(args.manifest),load(C/'CAPP-01_APPEARANCE_CHOICE_REGISTRY_v0.1.0.json'),load(C/'CAPP-03_PIXEL_ART_ASSET_PRODUCTION_STANDARD_v0.1.0.json'),load(C/'CAPP-04_ASSET_MANIFEST_CONTRACT_v0.1.0.json'))
    print(json.dumps(out,indent=2,sort_keys=True))
if __name__=='__main__': main()
