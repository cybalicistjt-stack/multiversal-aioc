#!/usr/bin/env python3
import json
from pathlib import Path
R=Path(__file__).resolve().parents[1]
B=R/'governance/application-planning/character-appearance-production'
def j(n): return json.loads((B/n).read_text(encoding='utf-8'))
def need(c,m):
 if not c: raise SystemExit('CAPP-04 VALIDATION: FAIL — '+m)
reg=j('CAPP-01_APPEARANCE_CHOICE_REGISTRY_v0.1.0.json')
std=j('CAPP-03_PIXEL_ART_ASSET_PRODUCTION_STANDARD_v0.1.0.json')
top=j('CAPP-03_TOPOLOGY_TEMPLATE_CONTRACT_v0.1.0.json')
man=j('CAPP-04_ASSET_MANIFEST_CONTRACT_v0.1.0.json')
cov=j('CAPP-04_COVERAGE_MODEL_v0.1.0.json')
ana=j('CAPP-04_REFERENCE_ANALYZER_CONTRACT_v0.1.0.json')
empty=j('CAPP-04_REFERENCE_EMPTY_MANIFEST_v0.1.0.json')
acc=j('CAPP-04_ACCEPTANCE_MATRIX_v0.1.0.json')
ext=j('CAPP-04_CONTEXTUAL_COVERAGE_EXTENSION_v0.1.0.json')
back=j('CAPP_PROGRAM_BACKLOG.json')
need(reg.get('profile_count')==25 and len(reg.get('profiles',[]))==25,'profile coverage')
need(std.get('renderer_id')=='pixel-art-v1' and len(std.get('canvases',{}))==3 and len(std.get('bands',[]))==10,'CAPP-03 renderer axes')
need(top.get('profile_coverage_required')==25,'topology profile coverage')
need({'CAPP03-TOP-MORAVI','CAPP03-TOP-VESPIN','CAPP03-TOP-SUULA','CAPP03-TOP-MANYTOMS'}<=set(top.get('special_templates',{})),'special topology templates')
need(man.get('renderer_id')=='pixel-art-v1' and 'profile_ids' in man.get('asset_required',[]),'manifest profile linkage')
need(set(cov.get('states',[]))=={'supported','partial','unsupported','unknown'},'coverage states')
need(cov.get('privacy',{}).get('hidden_asset_counts_reported') is False and cov.get('character_effect',{}).get('changes_character_truth') is False,'privacy/truth boundary')
e=ana.get('expected_catalog',{})
need(e.get('profile_count')==25 and e.get('view_count')==3 and e.get('semantic_band_count')==10 and e.get('expected_cell_count')==750,'deterministic base grid')
need(empty.get('authorized_projection') is True and empty.get('assets')==[] and empty.get('provenance',{}).get('canonical_asset_inventory') is False,'empty reference manifest')
need(len(acc.get('cases',[]))==18 and len(ext.get('acceptance_cases',[]))==4,'22-case acceptance coverage')
need(set(ext.get('contextual_dimensions',[]))=={'semantic_choice_id','pose_id','fit_class','asset_pack_id','asset_pack_version'},'context dimensions')
items={x['id']:x for x in back.get('work_items',[])}
need(items.get('CAPP-04',{}).get('status')=='in_progress' and items.get('CAPP-05',{}).get('status')=='planned','lifecycle boundary')
need(not any(back.get('boundaries',{}).values()),'non-activation boundary')
print('CAPP-04 VALIDATION: PASS — profiles=25 views=3 bands=10 base_cells=750 cases=22')
