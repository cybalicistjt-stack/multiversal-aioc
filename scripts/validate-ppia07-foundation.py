#!/usr/bin/env python3
from __future__ import annotations
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
BASE=ROOT/'governance/application-planning/parallel-preimplementation'
INV=BASE/'PPIA-07_SOURCE_AND_DESIGN_INVENTORY.md'
SRC=BASE/'PPIA-07_SOURCE_MANIFEST_v0.1.0.json'
TAX=BASE/'PPIA-07_RUNE_COMPOSITION_TAXONOMY_v0.1.0.json'
AUTH=BASE/'PPIA-07_AUTHORITY_AND_BOUNDARY_MATRIX_v0.1.0.json'
CAND=BASE/'PPIA-07_FOUNDATION_CANDIDATE.md'
CP=ROOT/'governance/ai/work-state/PPIA-07-attempt-001.json'
PTR=ROOT/'governance/ai/runtime/CURRENT_WORK_POINTER.json'
STATUS=ROOT/'governance/ai/runtime/CURRENT_IMPLEMENTATION_STATUS.json'
TRANSITION='a7803f8438a837b741f78c875d7ec2e915d37a19'

def req(c,m):
    if not c: raise SystemExit('PPIA-07 FOUNDATION: FAIL — '+m)
def load(p): req(p.exists(),f'missing {p.relative_to(ROOT)}'); return json.loads(p.read_text(encoding='utf-8'))

def main():
    inv=INV.read_text(encoding='utf-8'); src=load(SRC); tax=load(TAX); auth=load(AUTH); cand=CAND.read_text(encoding='utf-8'); cp=load(CP); ptr=load(PTR); status=load(STATUS)
    s=src['pdf_summary']; req(s=={'direct_composition_enchanting_pdfs':3,'direct_pages':77,'core_magic_context_pdfs':4,'core_context_pages':66,'risk_object_context_pdfs':2,'risk_object_context_pages':27,'total_pdfs':9,'total_pages':170,'dedicated_rune_pdf_present':False},'PDF source summary mismatch')
    cs=src['csv_summary']; exp={'csvs':4,'rows_total':2225,'profession_crafting_rows':221,'profession_rows_explicitly_about_runes':3,'magic_faction_rows':118,'scripts_macros_source_rows':16,'magic_spell_rows':385,'magic_spell_rows_explicitly_about_runes':0,'living_spellbook_rows':1501,'living_spellbooks_catalog_is_context_not_grammar_authority':True}; req(cs==exp,'CSV source summary mismatch')
    req(src['source_container']['sha256']=='c5732c5b4c3cdf5eca1d19eef7354289d1f92a87397b56aa7623b3f0a24177ec','source container hash changed')
    req(src['visual_review']['rendered_pages']==170,'visual review must account for all 170 PDF pages')
    names={x['file'] for x in src['pdfs']}; req({'Scripts and Macros.PDF','Crafting, repair, enchanting v2.PDF','Magic charge holders.PDF','Magic rules.PDF','Mana.PDF','Magic Schools and Spells.PDF','Abilities- Magic & Arcane Specializations.PDF','Chaos Magic.PDF','Living Spellbooks.PDF'}==names,'PDF set mismatch')
    findings=' '.join(src['explicit_source_findings']).lower()
    for x in ['script','sigilcrafting','symbols','glyphs','logic structures','macro','resonance','enchanter binds runes','rune carving basics','perfect rune placement','do not publish a canonical basic-rune vocabulary']:
        req(x in findings,f'missing source finding {x!r}')
    layers=tax['identity_state_layers']; req(len(layers)==15,'expected 15 identity/state layers'); ids=[x['id'] for x in layers]; req(len(ids)==len(set(ids)),'duplicate taxonomy layer')
    for x in ['rune-atom-definition','connection-topology','shaping-and-geometry-modifier','trigger-condition-and-timing','sequence-branch-and-composition','resource-cost-capacity-and-budget','stability-resonance-risk-and-failure','counterplay-resistance-and-disruption','progression-knowledge-and-unlock','crafting-inscription-container-and-item-link','visibility-permission-and-accessibility','provenance-conflict-version-and-recovery']:
        req(x in ids,f'missing layer {x}')
    req(len(tax['presentation_profiles'])==12,'expected 12 presentation profiles')
    intent=tax['owner_design_intent']; req(all(intent[k] is True for k in ['basic_reusable_runes','connection_types','shaping','reuse_small_vocabulary_many_ways','fun_and_not_too_hard']),'owner design intent incomplete')
    na=tax['foundation_non_assumptions']; req(all(v is False for v in na.values()),'foundation must not project unapproved grammar/equivalences')
    levels={x['id'] for x in auth['authority_levels']}; req(levels=={'source_explicit','governed_owner_intent','derived_taxonomy','future_proposal'},'authority levels mismatch')
    route=json.dumps(auth,ensure_ascii=False).lower()
    for x in ['ppia-03','ppia-08','ppia-11','ppia-12','mv-ia-f020','mv-ia-f021','mv-ia-f002','screen design v08 crafting','expected-version','idempotent','nonvisual']:
        req(x in route,f'authority routing missing {x!r}')
    for value in ['9 PDFs / 170 pages','3 explicit rune records','16 records sourced from Scripts and Macros','basic reusable runes','connection types','shaping','fun and not too hard','do **not** publish','V08_Crafting.md','SD-707']:
        req(value in inv,f'inventory missing {value!r}')
    for value in ['FOUNDATION CANDIDATE — NOT PPIA-07 COMPLETE',TRANSITION,'15 Rune Construction identity/state layers','PPIA-07 itself remains `started`']:
        req(value in cand,f'candidate missing {value!r}')
    req(cp['work_item_id']=='PPIA-07' and cp['attempt_id']=='PPIA-07-attempt-001','checkpoint identity mismatch'); req(cp['status'] in {'started','in_progress'},'PPIA-07 must remain active'); req(cp['base_commit']==TRANSITION,'checkpoint base must be canonical transition merge'); req(cp['owner_decision_required'] is False and not cp['unresolved_failures'],'checkpoint unresolved state')
    selected=[x for x in ptr['active_attempts'] if x.get('owner_selected')]; req(len(selected)==1 and selected[0]['work_item_id']=='PPIA-07','pointer must select PPIA-07'); req(ptr['primary_attempt_id']=='PPIA-07-attempt-001','primary attempt mismatch')
    primary=status['primary']; req(primary['work_item_id']=='PPIA-07' and primary['attempt_id']==cp['attempt_id'],'compact status identity mismatch'); req(primary['status']==cp['status'],'compact status/checkpoint mismatch')
    print('PPIA-07 FOUNDATION: PASS'); print('pdfs=9 pages=170'); print('direct_pdfs=3 pages=77'); print('context_pdfs=6 pages=93'); print('csvs=4 rows=2225'); print('explicit_rune_records=3'); print('scripts_macros_records=16'); print('identity_state_layers=15'); print('presentation_profiles=12'); print('deterministic_grammar_defined=false'); print('runtime_activation=false')
if __name__=='__main__': main()
