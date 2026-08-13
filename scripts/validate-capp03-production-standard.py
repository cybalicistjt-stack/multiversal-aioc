#!/usr/bin/env python3
from __future__ import annotations
import json
from pathlib import Path
R=Path(__file__).resolve().parents[1]
C=R/'governance/application-planning/character-appearance-production'
P=R/'governance/application-planning/parallel-preimplementation'

def load(p): return json.loads(p.read_text(encoding='utf-8'))
def req(x,m):
    if not x: raise SystemExit('CAPP-03 validation FAILED: '+m)

std=load(C/'CAPP-03_PIXEL_ART_ASSET_PRODUCTION_STANDARD_v0.1.0.json')
top=load(C/'CAPP-03_TOPOLOGY_TEMPLATE_CONTRACT_v0.1.0.json')
schema=load(C/'CAPP-03_ASSET_METADATA_SCHEMA_v0.1.0.json')
renderer=load(P/'PPIA-06_PIXEL_ART_RENDERER_CONTRACT_v0.2.0.json')
sem=load(P/'PPIA-06_APPEARANCE_SEMANTIC_TAXONOMY_v0.2.0.json')
registry=load(C/'CAPP-01_APPEARANCE_CHOICE_REGISTRY_v0.1.0.json')
req(std['work_item_id']=='CAPP-03','work item')
req(std['renderer_id']==renderer['renderer_id']=='pixel-art-v1','renderer identity')
req(set(std['canvases'])==set(renderer['view_contract']['switchable_during_customization']),'view/canvas coverage')
req(std['bands']==renderer['semantic_render_bands'],'semantic bands drift')
req(std['anchors']['universal']==renderer['anchors']['universal'],'universal anchors drift')
req(std['support_states']==sem['renderer_support_states'],'support states drift')
req(std['palette']['zone_ids'] and std['palette']['controlled_ramps'] and std['palette']['semantic_names'] and std['palette']['noncolor_labels'],'palette contract incomplete')
req(std['boundary']=={'classification':'renderer_metadata','character_truth':False,'species_taxonomy':False,'biology':False,'equipment_ownership':False},'authority boundary')
req(registry['profile_count']==25 and len(registry['profiles'])==25,'CAPP-01 profile coverage')
required={'asset_id','asset_pack_id','asset_pack_version','renderer_id','asset_kind','semantic_band','view_ids','topology_template_ids','support_state','anchors','mask_refs','palette_zone_refs','provenance_class'}
req(required<=set(schema['required']),'asset metadata required fields')
req(schema['properties']['renderer_id']['const']=='pixel-art-v1','metadata renderer const')
req(top['special_templates']['CAPP03-TOP-MORAVI']=={'arms':2,'legs':4},'Moravi topology')
req(top['special_templates']['CAPP03-TOP-VESPIN']=={'arms':4,'legs':2},'Vespin topology')
req(top['special_templates']['CAPP03-TOP-SUULA']['nested_hands'] is True,'Suula nested hands')
req(top['special_templates']['CAPP03-TOP-MANYTOMS']['repeated_constituents'] is True,'ManyToms composite topology')
req(top['fallback']['support_state']=='unknown' and top['fallback']['synthesize_anatomy'] is False,'unknown topology fallback')
print('CAPP-03 production standard: PASS')
print('profiles=25 views=3 bands=10 special_templates=4')
