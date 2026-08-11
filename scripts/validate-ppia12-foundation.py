#!/usr/bin/env python3
from __future__ import annotations
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
BASE=ROOT/'governance/application-planning/parallel-preimplementation'
INV=BASE/'PPIA-12_SOURCE_AND_DESIGN_INVENTORY.md'
TAX=BASE/'PPIA-12_WORLD_SETTING_TAXONOMY_v0.1.0.json'
ROUTE=BASE/'PPIA-12_SETTING_EXTENSION_ROUTING_v0.1.0.json'
CAND=BASE/'PPIA-12_FOUNDATION_CANDIDATE.md'
CP=ROOT/'governance/ai/work-state/PPIA-12-attempt-001.json'
PTR=ROOT/'governance/ai/runtime/CURRENT_WORK_POINTER.json'
STATUS=ROOT/'governance/ai/runtime/CURRENT_IMPLEMENTATION_STATUS.json'
TRANSITION='17dc6be36960b65bbcef5c4382b67de75c05218c'
FINAL_HEAD='ae3d538e85e09e52681df5a05bd8ee343aa5e908'
FINAL_MERGE='0ed9f9a0c53b2a132d8f38c0d3cae22cc7ae14a0'

def req(c,m):
    if not c: raise SystemExit('PPIA-12 FOUNDATION: FAIL — '+m)
def load(p): req(p.exists(),f'missing {p.relative_to(ROOT)}'); return json.loads(p.read_text(encoding='utf-8'))

def main():
    inv=INV.read_text(encoding='utf-8'); tax=load(TAX); route=load(ROUTE); cand=CAND.read_text(encoding='utf-8'); cp=load(CP); ptr=load(PTR); status=load(STATUS)
    for value in ['22 primary setting/cosmology/location sources / 693 pages','8 reusable environment-template sources / 238 pages','2 supporting worldbuilding-authoring sources / 30 pages','32 retained PDFs / 961 pages total','No dedicated World/Setting CSV catalog']:
        req(value in inv, f'inventory missing {value!r}')
    for name in ['Havalaea.PDF','Vertigon.PDF','Black Vegas.PDF','The Antiquaria.PDF','The Rakuuta Road.PDF','The layers of the multiverse.PDF','New Branches Info.PDF','Musical Reality Gameplay.PDF','Stratebrait.PDF','Worldbuilding.PDF','World Creation tables.PDF']:
        req(name in inv, f'inventory missing source {name}')
    ss=tax['source_summary']; req(ss=={'primary_setting_cosmology_location_pdfs':22,'primary_pages':693,'environment_template_pdfs':8,'environment_template_pages':238,'authoring_guidance_pdfs':2,'authoring_guidance_pages':30,'total_pdfs':32,'total_pages':961,'dedicated_world_setting_csv_catalog_present':False},'source summary mismatch')
    layers=tax['identity_state_layers']; req(len(layers)==14,'expected 14 identity/state layers'); ids=[x['id'] for x in layers]; req(len(ids)==len(set(ids)),'duplicate layer id')
    for x in ['world-setting-definition','cosmology-branch-reality-placement','region-location-site-hierarchy','environment-biome-hazard-profile','faction-institution-governance','culture-society-economy','history-era-event-timeline','world-local-content-extension','world-local-rule-mechanic-extension','campaign-instantiation-current-setting-state','knowledge-visibility-secret-state','provenance-conflict-recovery']:
        req(x in ids,f'missing layer {x}')
    req(len(tax['presentation_profiles'])==12,'expected 12 presentation profiles')
    req(len(route['source_classes'])==3,'expected three source classes'); req(len(route['ownership_routes'])>=10,'insufficient ownership routes')
    insufficient=set(route['relation_evidence_rules']['not_sufficient']); req({'same file','same name','name similarity','AI inference','random table result'}.issubset(insufficient),'relation inference guardrails incomplete')
    req(route['setting_local_mechanics']['default_scope'].startswith('source setting'),'local mechanic scope missing')
    req(route['authoring_policy']['random_tables']=='proposal_only' and route['authoring_policy']['ai_assistance']=='proposal_only','authoring proposal boundary missing')
    for value in ['foundation candidate only','exact PR head','17dc6be36960b65bbcef5c4382b67de75c05218c']:
        req(value in cand,f'candidate missing {value!r}')
    req(cp['work_item_id']=='PPIA-12' and cp['attempt_id']=='PPIA-12-attempt-001','checkpoint identity mismatch')
    req(cp['base_commit']==TRANSITION,'checkpoint base must be transition merge')
    req(cp['owner_decision_required'] is False and not cp['unresolved_failures'],'checkpoint unresolved state')
    if cp['status'] in {'started','in_progress'}:
        selected=[x for x in ptr['active_attempts'] if x.get('owner_selected')]
        req(len(selected)==1 and selected[0]['work_item_id']=='PPIA-12','active PPIA-12 pointer must select PPIA-12')
        req(ptr['primary_attempt_id']=='PPIA-12-attempt-001','active PPIA-12 primary attempt mismatch')
        primary=status['primary']; req(primary['work_item_id']=='PPIA-12' and primary['attempt_id']==cp['attempt_id'],'active compact status identity mismatch'); req(primary['status']==cp['status'],'active compact status/checkpoint mismatch')
        req('world' in ptr['selection_reason'].lower() and 'roadmap' in ptr['selection_reason'].lower() and 'pending' in ptr['selection_reason'].lower(),'active selection reason must preserve world transition and batched roadmap state')
    else:
        req(cp['status']=='completed_verified','PPIA-12 must be active or completed_verified')
        req(cp.get('active_substep') is None,'completed PPIA-12 active_substep must be null')
        req(cp.get('latest_pushed_commit')==FINAL_HEAD and cp.get('pull_request')==239 and cp.get('merge_commit')==FINAL_MERGE,'completed PPIA-12 final evidence mismatch')
        req(any('31536379370' in x.get('command','') and x.get('status')=='passed' for x in cp.get('validation',[])),'completed PPIA-12 completion gate evidence missing')
    print('PPIA-12 FOUNDATION: PASS'); print('primary_sources=22 pages=693'); print('environment_templates=8 pages=238'); print('authoring_guidance=2 pages=30'); print('total_pdfs=32 pages=961'); print('identity_state_layers=14'); print('presentation_profiles=12'); print(f'checkpoint_state={cp["status"]}'); print('runtime_activation=false')
if __name__=='__main__': main()
