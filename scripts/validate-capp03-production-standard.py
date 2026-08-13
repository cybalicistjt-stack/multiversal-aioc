#!/usr/bin/env python3
import json
from pathlib import Path
R=Path(__file__).resolve().parents[1]
C=R/'governance/application-planning/character-appearance-production'
P=R/'governance/application-planning/parallel-preimplementation'
def j(p): return json.loads(p.read_text())
def q(x,m):
    if not x: raise SystemExit('CAPP-03 validation FAILED: '+m)
s=j(C/'CAPP-03_PIXEL_ART_ASSET_PRODUCTION_STANDARD_v0.1.0.json')
t=j(C/'CAPP-03_TOPOLOGY_TEMPLATE_CONTRACT_v0.1.0.json')
m=j(C/'CAPP-03_ASSET_METADATA_SCHEMA_v0.1.0.json')
r=j(P/'PPIA-06_PIXEL_ART_RENDERER_CONTRACT_v0.2.0.json')
a=j(P/'PPIA-06_APPEARANCE_SEMANTIC_TAXONOMY_v0.2.0.json')
g=j(C/'CAPP-01_APPEARANCE_CHOICE_REGISTRY_v0.1.0.json')
q(s['renderer_id']==r['renderer_id']=='pixel-art-v1','renderer')
q(set(s['canvases'])==set(r['view_contract']['switchable_during_customization']),'views')
q(s['bands']==r['semantic_render_bands'],'bands')
q(s['anchors']['universal']==r['anchors']['universal'],'anchors')
q(s['support_states']==a['renderer_support_states'],'support states')
q(s['boundary']['character_truth'] is False and s['boundary']['species_taxonomy'] is False,'authority boundary')
q(g['profile_count']==25 and len(g['profiles'])==25 and t['profile_coverage_required']==25,'profile coverage')
q(t['special_templates']['CAPP03-TOP-MORAVI']=={'arms':2,'legs':4},'Moravi')
q(t['special_templates']['CAPP03-TOP-VESPIN']=={'arms':4,'legs':2},'Vespin')
q(t['special_templates']['CAPP03-TOP-SUULA']['nested_hands'] is True,'Suula')
q(t['special_templates']['CAPP03-TOP-MANYTOMS']['repeated_constituents'] is True,'ManyToms')
q(t['fallback']['synthesize_anatomy'] is False,'fallback')
need={'asset_id','asset_pack_id','asset_pack_version','renderer_id','asset_kind','semantic_band','view_ids','topology_template_ids','support_state','anchors','mask_refs','palette_zone_refs','provenance_class'}
q(need<=set(m['required']),'metadata schema')
print('CAPP-03 production standard: PASS profiles=25 views=3 bands=10')
