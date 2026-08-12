#!/usr/bin/env python3
from __future__ import annotations
import json,re
from collections import Counter
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
BASE=ROOT/'governance/application-planning/parallel-preimplementation'
IDX=BASE/'PPIA-10_WORKFLOW_AUTHORING_CONTRACT_MATRIX_v0.1.0.json'
TRACE=BASE/'PPIA-10_WORKFLOW_TRACEABILITY_MATRIX_v0.1.0.json'
NOTE=BASE/'PPIA-10_WORKFLOW_AUTHORING_CANDIDATE.md'
TAX=BASE/'PPIA-10_RELATIONSHIP_SOCIAL_FACTION_TAXONOMY_v0.1.0.json'
AUTH=BASE/'PPIA-10_AUTHORITY_AND_BOUNDARY_MATRIX_v0.1.0.json'
INS=BASE/'PPIA-10_INSPECTOR_ACTION_CONTRACT_MATRIX_v0.1.0.json'
CASES=BASE/'PPIA-10_REFERENCE_CASES_v0.1.0.json'
CP=ROOT/'governance/ai/work-state/PPIA-10-attempt-001.json'
PTR=ROOT/'governance/ai/runtime/CURRENT_WORK_POINTER.json'
STATUS=ROOT/'governance/ai/runtime/CURRENT_IMPLEMENTATION_STATUS.json'
INSPECTOR_MERGE='6985dd1e1f6d2e2b696f409cc74ae9e0ad18d728'
WORKFLOW_HEAD='7e23b04fa920b706278ae0467b022713cc6a9334'
WORKFLOW_PR=260
WORKFLOW_MERGE='36da845855a01da8003b699f8a68478427424d42'
def load(p): return json.loads(p.read_text(encoding='utf-8'))
def req(x,m):
    if not x: raise AssertionError(m)
def expand(r):
    a,b=r.split('..'); m1=re.fullmatch(r'PPIA10-RC-(\d{3})',a); m2=re.fullmatch(r'PPIA10-RC-(\d{3})',b); req(m1 and m2,'bad case range')
    return [f'PPIA10-RC-{n:03d}' for n in range(int(m1.group(1)),int(m2.group(1))+1)]
def main():
    for p in (IDX,TRACE,NOTE,TAX,AUTH,INS,CASES,CP,PTR,STATUS): req(p.exists(),f'missing {p.relative_to(ROOT)}')
    idx,tr,tx,au,ins,cases,cp,ptr,status=map(load,(IDX,TRACE,TAX,AUTH,INS,CASES,CP,PTR,STATUS)); note=NOTE.read_text(encoding='utf-8').lower()
    req(idx['format']=='multiversal-ppia10-workflow-authoring-contract-matrix' and idx['version']=='0.1.0' and idx['work_item']=='PPIA-10','index identity')
    req(idx['inherits']==[TAX.name,AUTH.name,INS.name,CASES.name],'inheritance drift')
    shards=[BASE/x for x in idx['shards']]; req(len(shards)==3 and all(p.exists() for p in shards),'three workflow shards required')
    workflows=[]
    for label,p in zip('ABC',shards):
        d=load(p); req(d['format']=='multiversal-ppia10-workflow-authoring-shard' and d['shard']==label,'shard identity'); workflows+=d['workflows']
    ids=[f'P10-WF-{n:03d}' for n in range(1,19)]; req([w['id'] for w in workflows]==ids==idx['workflow_ids'],'18 continuous workflows')
    for w in workflows:
        for k in ('name','personas','entry','steps','outputs','pg','profiles','actions','case_range','handoffs','owner','guards'): req(w.get(k),f"{w['id']} missing {k}")
        req(isinstance(w.get('mutation'),bool),f"{w['id']} mutation flag")
    pgs=[x['id'] for x in ins['projection_groups']]; acts=[x['id'] for x in ins['actions']]; profiles=tx['presentation_profiles']; hos=[x['id'] for x in au['domain_handoffs']]
    req(pgs==[f'P10-PG-{n:03d}' for n in range(1,19)],'projection drift'); req(acts==[f'P10-ACT-{n:03d}' for n in range(1,35)],'action drift'); req(len(profiles)==14,'profile count'); req(hos==[f'P10-HO-{n:03d}' for n in range(1,16)],'handoff drift')
    req(cases['resolved_case_count']==90 and cases['imported_case_count']==72 and cases['local_case_count']==18,'case counts')
    writes={x['id'] for x in ins['actions'] if x['kind']=='write'}; reads={x['id'] for x in ins['actions'] if x['kind']=='read'}; req((len(writes),len(reads))==(24,10),'24/10 action split')
    proto=ins['mutation_protocols']['P10-MUT-001']; req(proto['required']==['authorization','expected_version','operation_id'],'mutation requirements'); req(proto['ambiguous_result']==['query_operation_status','query_current_version','retry_only_if_safe'],'retry recovery')
    mut=[w for w in workflows if w['mutation']]; ro=[w for w in workflows if not w['mutation']]; req((len(mut),len(ro))==(15,3),'15 mutation / 3 read-only workflows')
    for w in mut:req(any(a in writes for a in w['actions']),f"{w['id']} no write")
    for w in ro:req(all(a in reads for a in w['actions']),f"{w['id']} read-only invokes write")
    routed_pgs={z for w in workflows for z in w['pg']}; routed_profiles={z for w in workflows for z in w['profiles']}; routed_actions={z for w in workflows for z in w['actions']}; routed_hos={z for w in workflows for z in w['handoffs']}; routed_cases=[z for w in workflows for z in expand(w['case_range'])]
    req(routed_pgs==set(pgs),'all 18 projections'); req(routed_profiles==set(profiles),'all 14 profiles'); req(routed_actions==set(acts),'all 34 actions'); req(routed_hos==set(hos),'all 15 handoffs'); req(routed_cases==[f'PPIA10-RC-{n:03d}' for n in range(1,91)] and all(v==1 for v in Counter(routed_cases).values()),'all 90 cases exactly once')
    pol=idx['policy']; req(pol['workflow_count']==18 and pol['authoritative_mutation_workflow_count']==15 and pol['read_only_workflow_count']==3,'policy counts')
    for k in ('all_18_projection_groups_required','all_14_presentation_profiles_required','all_34_actions_required','all_90_reference_cases_required','all_15_domain_handoffs_required','permission_filter_before_aggregation','expected_version_operation_id_for_authoritative_mutations','directional_relationships_required','atomic_cross_domain_event_group_required','standing_information_path_required','semantic_nonvisual_parity_required'): req(pol.get(k) is True,f'policy lost {k}')
    for k in ('automatic_reciprocity_allowed','universal_relationship_standing_influence_or_social_dc_scale','state_type_collapsing_allowed','rank_office_implies_permission','hidden_content_in_unauthorized_derivatives','partial_cross_domain_commit_allowed','external_reference_transfers_ownership','graph_layout_authoritative','ai_proposal_authoritative_without_acceptance','runtime_activation'): req(pol.get(k) is False,f'policy boundary {k}')
    req(tr['format']=='multiversal-ppia10-workflow-traceability-matrix' and tr['counts']=={'workflows':18,'mutation':15,'read_only':3},'trace identity/counts'); req([r['id'] for r in tr['rows']]==ids,'trace rows'); req(tr['coverage']=={'pg':'18/18','profiles':'14/14','actions':'34/34','cases':'90/90 exactly once','handoffs':'15/15'},'trace coverage'); req(len(tr['assertions'])==14,'trace assertions')
    for row,w in zip(tr['rows'],workflows):
        for k1,k2 in (('pg','pg'),('profiles','profiles'),('actions','actions'),('case_range','case_range'),('handoffs','handoffs'),('mutation','mutation')): req(row[k1]==w[k2],f"trace mismatch {w['id']} {k1}")
    req(ins['projection_policy']['filter_before_derivatives'] is True and ins['projection_policy']['hidden_derivative_leak'] is False and ins['projection_policy']['graph_authoritative'] is False,'projection policy regression')
    full=(json.dumps(idx,ensure_ascii=False)+'\n'+''.join(json.dumps(load(p),ensure_ascii=False) for p in shards)+'\n'+json.dumps(tr,ensure_ascii=False)+'\n'+note).lower()
    for phrase in ('18 end-to-end relationship/social/faction workflows','15 workflows perform authoritative mutation','3 are read-only','34 governed actions','24 authoritative mutations','90 deterministic reference cases','72 inherited','five bond','seven converted organizations','directional','plausible information path','influence is not standing','atomic event group or none','permission filtering','expected_version','operation_id','status/current-version','semantic nonvisual','proposal-only','not ppia-10 complete','no application runtime','stage-a-a2'): req(phrase in full,f'missing boundary {phrase}')
    req(cp['work_item_id']=='PPIA-10' and cp['branch']=='governance/ppia-10-relationship-social-faction' and cp['status'] in {'started','completed_verified'},'checkpoint identity/status'); req(cp.get('owner_decision_required') is False and cp.get('unresolved_failures')==[],'checkpoint unresolved')
    history=json.dumps({'last_verified_action':cp.get('last_verified_action'),'completed_substeps':cp.get('completed_substeps',[]),'validation':cp.get('validation',[]),'evidence':cp.get('evidence',[])},ensure_ascii=False).lower(); req(INSPECTOR_MERGE in history,'inspector merge evidence missing')
    active=((cp.get('active_substep') or '')+' '+(cp.get('next_action') or '')).lower()
    workflow_historical=all(v in history for v in (WORKFLOW_HEAD.lower(),f'pr #{WORKFLOW_PR}',WORKFLOW_MERGE.lower()))
    if cp['status']=='started' and not workflow_historical:
        req('workflow' in active and 'relationship/social/faction' in active,'checkpoint workflow continuity')
    else:
        req(workflow_historical,'historical workflow head/PR/merge evidence missing')
    if cp['status']=='started':
        req(ptr['primary_attempt_id']=='PPIA-10-attempt-001' and status['primary']['work_item_id']=='PPIA-10' and status['primary']['status']=='started','pointer/status continuity')
    print('PPIA-10 WORKFLOW CONTRACTS: PASS')
    print('workflows=18 mutation=15 read_only=3 projections=18 profiles=14 actions=34 cases=90 handoffs=15')
if __name__=='__main__': main()
