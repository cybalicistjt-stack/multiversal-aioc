#!/usr/bin/env python3
from __future__ import annotations
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
BASE=ROOT/'governance/application-planning/parallel-preimplementation'
IA=ROOT/'governance/application-planning/internal-alpha/feature-packets'
MAN=BASE/'PPIA-10_SOURCE_MANIFEST_v0.1.0.json'
INV=BASE/'PPIA-10_SOURCE_AND_DESIGN_INVENTORY.md'
TAX=BASE/'PPIA-10_RELATIONSHIP_SOCIAL_FACTION_TAXONOMY_v0.1.0.json'
AUTH=BASE/'PPIA-10_AUTHORITY_AND_BOUNDARY_MATRIX_v0.1.0.json'
CAND=BASE/'PPIA-10_FOUNDATION_CANDIDATE.md'
F009=IA/'MV-IA-F009_RELATIONSHIP_TRACKER_MATRIX.json'
F009SRC=IA/'MV-IA-F009_SOURCE_COVERAGE_AND_PROVENANCE.json'
F010=IA/'MV-IA-F010_SOCIAL_INTERACTION_MATRIX.json'
F010SRC=IA/'MV-IA-F010_SOURCE_COVERAGE_AND_PROVENANCE.json'
F016=IA/'MV-IA-F016_FACTION_REPUTATION_MATRIX.json'
F016SRC=IA/'MV-IA-F016_SOURCE_COVERAGE_AND_PROVENANCE.json'
CP=ROOT/'governance/ai/work-state/PPIA-10-attempt-001.json'
PTR=ROOT/'governance/ai/runtime/CURRENT_WORK_POINTER.json'
STATUS=ROOT/'governance/ai/runtime/CURRENT_IMPLEMENTATION_STATUS.json'
PACKAGE_SHA='c5732c5b4c3cdf5eca1d19eef7354289d1f92a87397b56aa7623b3f0a24177ec'

def fail(m): raise SystemExit('PPIA-10 FOUNDATION: FAIL — '+m)
def req(c,m):
    if not c: fail(m)
def load(p):
    req(p.exists(),f'missing {p.relative_to(ROOT)}')
    return json.loads(p.read_text(encoding='utf-8'))

def main():
    for p in (MAN,INV,TAX,AUTH,CAND,F009,F009SRC,F010,F010SRC,F016,F016SRC,CP,PTR,STATUS): req(p.exists(),f'missing {p.relative_to(ROOT)}')
    man,tax,auth=load(MAN),load(TAX),load(AUTH)
    f9,f9s,f10,f10s,f16,f16s=load(F009),load(F009SRC),load(F010),load(F010SRC),load(F016),load(F016SRC)
    cp,ptr,status=load(CP),load(PTR),load(STATUS)
    inv=INV.read_text(encoding='utf-8'); cand=CAND.read_text(encoding='utf-8')

    req(man.get('format')=='multiversal-ppia10-source-manifest' and man.get('version')=='0.1.0' and man.get('work_item_id')=='PPIA-10','manifest identity/version')
    req(man['retained_package']['sha256']==PACKAGE_SHA,'retained package SHA changed')
    pdfs=man['direct_pdf_sources']; req(len(pdfs)==5 and man['direct_pdf_totals']=={'files':5,'pages':44},'direct PDF boundary must remain 5 files / 44 pages')
    req(all(x.get('visual_review_complete') is True for x in pdfs),'all direct PDFs must remain visually reviewed')
    expected_pdf={'6a2798d6deeb5004aae1858e99cad781419f9240525725da5559ccbbd81291a7':4,'ae8e95152eb23fa81eef5c080da3642bfeab5e05139637caddf15ec61f3c9953':18,'135b21712d5ecd65ab0b55d1ede5daa22ba7638eee6889af51e2367960a43c6d':10,'dd44d18997d38520030d3ef6162008fa8a1646cb6949fec6c6e883f1c5b4b1b8':10,'d075de181f78096ba29d512055181d5c1c1dcc1db03744b156108625c46c4cde':2}
    req({x['sha256']:x['pages'] for x in pdfs}==expected_pdf,'direct PDF hash/page evidence changed')
    req(man['direct_structured_totals']=={'files':2,'rows':1374,'structural_relevant_rows':94},'structured totals changed')
    structured={Path(x['path']).name:x for x in man['direct_structured_sources']}
    req(structured['Abilities_Core.csv']['rows']==1256 and structured['Abilities_Core.csv']['structural_relevant_rows']==82,'Abilities_Core social boundary changed')
    req(structured['Abilities_Core.csv']['structural_relevant_breakdown']=={'Social Play Ability Tree':61,'Politician Tree':21},'Abilities_Core explicit social breakdown changed')
    req(structured['Magic_Faction_Abilities.csv']['rows']==118 and structured['Magic_Faction_Abilities.csv']['structural_relevant_rows']==12,'Magic faction boundary changed')
    req(len(man['source_backed_findings'])==18 and len(man['explicit_source_gaps'])==12,'source finding/gap counts changed')
    req(all(v is False for v in man['non_assumptions'].values()),'non-assumptions must remain false')

    req(f9['featureId']=='MV-IA-F009' and len(f9['relationshipDimensions'])==14 and len(f9['revealLayers'])==7 and len(f9['fixtures'])==24,'F009 contract drift')
    req(f9['scaleProfileKinds']==['numeric','ordered-enum','band-only','validated-custom-scalar'],'F009 scale profiles changed')
    req(f9s['sources'][2]['rows']==154 and f9s['sources'][2]['sourceExplicitRelationshipFacts']==4,'F009 relationship provenance changed')
    req('universal relationship scale' in f9s['unsupportedClaimsProhibited'],'F009 universal-scale prohibition missing')

    req(f10['featureId']=='MV-IA-F010' and len(f10['interactionModes'])==3 and len(f10['actionCategories'])==14,'F010 interaction/category contract drift')
    req(f10['sourceActionForms']==49 and len(f10['alphaActions'])==7 and len(f10['resolutionMethods'])==6 and len(f10['degreeOutcomes'])==7,'F010 action/resolution counts changed')
    req(len(f10['outcomeEventDraftTypes'])==29 and len(f10['fixtures'])==24,'F010 outcome/fixture counts changed')
    req(f10s['sources'][3]['rows']==209 and f10s['sources'][3]['unmatchedLocalWrapper']==196 and f10s['sources'][3]['ambiguousExactName']==3,'F010 mechanic provenance changed')
    req('universal social DC table' in f10s['unsupportedClaimsProhibited'] and 'persuasion mind control' in f10s['unsupportedClaimsProhibited'],'F010 source guardrails missing')

    req(f16['featureId']=='MV-IA-F016' and len(f16['contractFamilies'])==16 and len(f16['visibilityLayers'])==9 and len(f16['fixtures'])==24,'F016 contract/fixture drift')
    req(len(f16['membershipStatuses'])==9 and len(f16['ownedCommands'])==14 and len(f16['ownedEvents'])==14,'F016 membership/event counts changed')
    req(f16['sourceProgressionBoundary']['canonicalRecords']==956 and f16['sourceProgressionBoundary']['automaticAuthorityGrants']==0,'F016 progression boundary changed')
    req(f16s['sources'][2]['rows']==153 and f16s['sources'][2]['stableFactionReferences']==0,'F016 faction-register provenance changed')
    req(len(f16s['convertedOrganizations'])==7 and f16s['progressionCorpus']['canonicalRecords']==956,'F016 converted-organization/progression evidence changed')

    req(tax.get('format')=='multiversal-ppia10-relationship-social-faction-taxonomy' and tax.get('version')=='0.1.0','taxonomy identity/version')
    layers=tax['identity_state_layers']; req(len(layers)==18 and [x['id'] for x in layers]==[f'P10-L{i:02d}' for i in range(1,19)],'taxonomy must retain 18 continuous layers')
    req(len(tax['presentation_profiles'])==14 and len(set(tax['presentation_profiles']))==14,'taxonomy must retain 14 unique presentation profiles')
    req(tax['relationship_dimension_registry']==f9['relationshipDimensions'],'taxonomy must preserve F009 relationship dimensions exactly')
    req(tax['relationship_reveal_layers']==f9['revealLayers'],'taxonomy must preserve F009 reveal layers exactly')
    req(tax['social_action_categories']==f10['actionCategories'],'taxonomy must preserve F010 action categories exactly')
    req(tax['faction_contract_families']==f16['contractFamilies'],'taxonomy must preserve F016 contract families exactly')
    req(len(tax['core_separation_invariants'])==16,'expected sixteen core separation invariants')
    req(all(v is False for v in tax['foundation_non_assumptions'].values()),'taxonomy non-assumptions changed')

    req(auth.get('format')=='multiversal-ppia10-authority-boundary-matrix' and auth.get('version')=='0.1.0','authority identity/version')
    req(len(auth['authority_levels'])==4,'expected four authority levels')
    handoffs=auth['domain_handoffs']; req(len(handoffs)==15 and [x['id'] for x in handoffs]==[f'P10-HO-{i:03d}' for i in range(1,16)],'expected 15 continuous handoffs')
    guard=' '.join(auth['blocking_guardrails']).lower()
    for phrase in ('directional','no universal','membership','rank','objective truth','mind control','filtered before graph topology','atomic event group','information path','expected_version','operation_id','semantic nonvisual','ai','no application runtime'):
        req(phrase in guard,f'authority guardrail missing {phrase!r}')
    req(len(auth['proposal_stage_design_domains'])==6 and len(auth['forbidden_ownership_transfers'])==8,'authority design/boundary counts changed')

    low=(inv+'\n'+cand).lower()
    for phrase in ('5 direct pdfs / 44','1,374 rows','94 structurally explicit','82 social & influence','12 faction-related','18 semantic layers','14 presentation profiles','15 domain handoffs','eleven','near-duplicate','persuasion is not mind control','semantic nonvisual','not ppia-10 complete','no application runtime'):
        req(phrase in low,f'candidate/inventory missing {phrase!r}')

    req(cp.get('work_item_id')=='PPIA-10' and cp.get('attempt_id')=='PPIA-10-attempt-001','PPIA-10 checkpoint identity mismatch')
    req(cp.get('branch')=='governance/ppia-10-relationship-social-faction','PPIA-10 branch mismatch')
    req(cp.get('status') in {'started','completed_verified'},'unexpected PPIA-10 status')
    req(cp.get('owner_decision_required') is False and cp.get('unresolved_failures')==[],'PPIA-10 unresolved state')
    if cp.get('status')=='started':
        req(ptr.get('primary_attempt_id')=='PPIA-10-attempt-001','pointer must select PPIA-10 while active')
        req(status.get('primary',{}).get('work_item_id')=='PPIA-10' and status.get('primary',{}).get('status')=='started','compact status must select started PPIA-10')
        active=((cp.get('active_substep') or '')+' '+(cp.get('next_action') or '')).lower()
        history=json.dumps({'completed_substeps':cp.get('completed_substeps',[]),'last_verified_action':cp.get('last_verified_action','')}).lower()
        req(('foundation' in active) or ('ppia-10 foundation' in history and 'merge' in history),'checkpoint must retain active or historical foundation evidence')

    print('PPIA-10 FOUNDATION: PASS')
    print('direct_pdfs=5 direct_pdf_pages=44 direct_structured_files=2 direct_structured_rows=1374 structurally_relevant_rows=94')
    print('f009_relationship_dimensions=14 f009_reveal_layers=7 f010_action_categories=14 f010_outcome_event_drafts=29')
    print('f016_contract_families=16 f016_visibility_layers=9 f016_progression_records=956')
    print('semantic_layers=18 presentation_profiles=14 domain_handoffs=15 source_gaps=12')
    print('universal_relationship_scale=false universal_standing_scale=false universal_influence_scale=false universal_social_dc=false')
    print('runtime_activation=false')
if __name__=='__main__': main()
