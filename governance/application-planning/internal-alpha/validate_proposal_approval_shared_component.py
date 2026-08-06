#!/usr/bin/env python3
from __future__ import annotations
import json,re
from pathlib import Path
ROOT=Path(__file__).resolve().parent
PACKETS=ROOT/'feature-packets'
FILES={
'contract':PACKETS/'IA-D04-002_PROPOSAL_APPROVAL_SHARED_COMPONENT_CONTRACT.md',
'matrix':PACKETS/'IA-D04-002_PROPOSAL_APPROVAL_COMPONENT_MATRIX.json',
'consumers':PACKETS/'IA-D04-002_CONSUMER_MAPPING.json',
'trace':PACKETS/'IA-D04-002_IMPLEMENTATION_TRACEABILITY.json',
'receipt':PACKETS/'IA-D04-002_REVIEW_RECEIPT.md',
'readiness':PACKETS/'IA-D04-002_READINESS_RECORD.md',
'completion':PACKETS/'IA-D04-002_COMPLETION_RECORD.json'}
CONSUMERS=['live-player-action','gm-npc-enemy-action','social-play-proposal','content-submission','optional-ai-proposal','destructive-change','canonical-promotion','asset-transfer-acceptance']
STATES=['local-draft','saved-draft','validation-required','ready-to-submit','submitting','submitted','pending-review','changes-requested','decision-in-progress','approved-pending-commit','modified-approved-pending-commit','denied','committed','withdrawn','expired','superseded','conflict','recovery-required','forbidden-or-unavailable','commit-failed']
CRITERIA=[f'PAC-AC-{i:03d}' for i in range(1,21)]
SLICES=[f'PAC-S{i:02d}' for i in range(1,11)]
FIXTURES=[f'PAC-FX-{i:03d}' for i in range(1,17)]
FLAGS=['implementationAuthorized','paidServicesAuthorized','productionCredentialsAuthorized','realUserDataCollectionAuthorized','internalAlphaReleaseAuthorized','productionAuthorized','publicReleaseAuthorized']

def load(path,errors):
    if not path.is_file(): errors.append(f'missing {path.relative_to(ROOT)}'); return {}
    try: return json.loads(path.read_text(encoding='utf-8'))
    except json.JSONDecodeError as exc: errors.append(f'invalid JSON {path.name}: {exc}'); return {}

def require(text,phrases,label,errors):
    low=text.lower()
    for phrase in phrases:
        if phrase.lower() not in low: errors.append(f'{label} missing {phrase!r}')

def main():
    errors=[]
    contract=FILES['contract'].read_text(encoding='utf-8') if FILES['contract'].is_file() else ''
    receipt=FILES['receipt'].read_text(encoding='utf-8') if FILES['receipt'].is_file() else ''
    readiness=FILES['readiness'].read_text(encoding='utf-8') if FILES['readiness'].is_file() else ''
    matrix=load(FILES['matrix'],errors); consumers=load(FILES['consumers'],errors); trace=load(FILES['trace'],errors); completion=load(FILES['completion'],errors)
    if not contract.startswith('# IA-D04-002 — Proposal and Approval Shared-Component Contract'): errors.append('contract title incorrect')
    sections=[int(m.group(1)) for line in contract.splitlines() if (m:=re.match(r'^## (\d+)\. ',line))]
    if sections!=list(range(1,25)): errors.append(f'contract sections must be 1-24 exactly; got {sections}')
    require(contract,['John Brandon Turner','SS-06 — Proposal and approval framework','does not become the authority for any domain','missing, unknown, incompatible, or unavailable consumer adapter fails closed','assignment is routing metadata, not reviewer authority','approve','deny','modify-and-approve','field-addressed','owner-only','exactly one versioned domain commit adapter','partial success is prohibited','Silent last-write-wins is prohibited','status using the original operation ID before retry','Realtime messages are advisory','Offline authoritative submit, decision, approval, denial, modification, commit, owner decision, promotion, deletion, or transfer is prohibited','AI is optional and proposal-only','zero AI','IA-D04-003','Silence is not approval'], 'contract',errors)
    for cid in CRITERIA:
        if cid not in contract: errors.append(f'contract missing {cid}')
    if (matrix.get('workItemId'),matrix.get('sharedSystemId'),matrix.get('owner'),matrix.get('status'))!=('IA-D04-002','SS-06','John Brandon Turner','complete-design-contract'): errors.append('matrix identity/status incorrect')
    checks=[('consumerTypes',CONSUMERS),('stateVocabulary',STATES)]
    for key,expected in checks:
        if matrix.get(key)!=expected: errors.append(f'matrix {key} incorrect')
    counts={'requiredSharedContracts':24,'requiredPreparationContracts':28,'proposalRequiredFields':30,'decisionReceiptRequiredFields':24,'approvalPolicies':4,'validationClasses':24,'operationTypes':24,'eventTypes':24,'deniedCases':36,'deterministicFixtures':16,'implementationSlices':10,'acceptanceCriteria':20}
    for key,expected in counts.items():
        if len(matrix.get(key,[]))!=expected: errors.append(f'matrix {key} must contain {expected}')
    if [x.get('fixtureId') for x in matrix.get('deterministicFixtures',[])]!=FIXTURES: errors.append('fixture IDs/order incorrect')
    if [x.get('sliceId') for x in matrix.get('implementationSlices',[])]!=SLICES: errors.append('slice IDs/order incorrect')
    if [x.get('criterionId') for x in matrix.get('acceptanceCriteria',[])]!=CRITERIA: errors.append('acceptance IDs/order incorrect')
    if matrix.get('blockingFindings')!=[] or matrix.get('nextWorkItemId')!='IA-D04-003': errors.append('matrix findings or next item incorrect')
    if any(matrix.get('authorizations',{}).get(flag) is not False for flag in FLAGS): errors.append('matrix authorization boundary incorrect')
    mapped=consumers.get('consumers',[])
    if [x.get('consumerType') for x in mapped]!=CONSUMERS: errors.append('consumer mapping IDs/order incorrect')
    required_consumer_fields={'consumerType','domainAuthority','proposerEligibility','reviewerAuthority','evidenceProfile','modifiableFieldsPolicy','approvalPolicy','commitAdapter','domainEvents','visibilityPolicy','ownerGate','offlinePolicy','fallback','retestList'}
    for item in mapped:
        missing=required_consumer_fields-set(item)
        if missing: errors.append(f"consumer {item.get('consumerType')} missing {sorted(missing)}")
        if not item.get('domainEvents') or not item.get('retestList'): errors.append(f"consumer {item.get('consumerType')} incomplete")
    canonical=next((x for x in mapped if x.get('consumerType')=='canonical-promotion'),{})
    ai=next((x for x in mapped if x.get('consumerType')=='optional-ai-proposal'),{})
    if canonical.get('approvalPolicy')!='owner-only' or canonical.get('ownerGate') is not True: errors.append('canonical promotion owner gate incorrect')
    if 'no reviewer' not in ai.get('reviewerAuthority','').lower() and 'human' not in ai.get('reviewerAuthority','').lower(): errors.append('AI reviewer boundary incomplete')
    if consumers.get('blockingFindings')!=[]: errors.append('consumer mapping retains blocking findings')
    if len(trace.get('acceptanceTrace',[]))!=20 or len(trace.get('consumerTrace',[]))!=8 or len(trace.get('implementationSliceTrace',[]))!=10: errors.append('traceability counts incorrect')
    if trace.get('untracedAcceptanceCriteria')!=[] or trace.get('unmappedConsumers')!=[] or trace.get('blockingFindings')!=[]: errors.append('traceability gaps remain')
    metrics=completion.get('metrics',{})
    expected={'consumerTypes':8,'lifecycleStates':20,'proposalFields':30,'decisionReceiptFields':24,'approvalPolicies':4,'validationClasses':24,'operationTypes':24,'eventTypes':24,'deniedCases':36,'deterministicFixtures':16,'implementationSlices':10,'acceptanceCriteria':20,'blockingFindings':0}
    if completion.get('status')!='complete-design-contract' or completion.get('owner')!='John Brandon Turner' or completion.get('nextWorkItemId')!='IA-D04-003': errors.append('completion identity/status/next incorrect')
    for key,value in expected.items():
        if metrics.get(key)!=value: errors.append(f'completion {key} must be {value}')
    if any(completion.get('authorizations',{}).get(flag) is not False for flag in FLAGS): errors.append('completion authorization boundary incorrect')
    require(receipt,['PASS — SHARED-COMPONENT DESIGN COMPLETE','eight consumer types','zero blocking findings','IA-D04-003','Silence is not approval'],'receipt',errors)
    require(readiness,['READY FOR IMPLEMENTATION HANDOFF — DEPENDENCY GATED','sixteen deterministic fixtures','eight mapped consumers','IA-D04-003'],'readiness',errors)
    shared=(ROOT/'INTERNAL_ALPHA_SHARED_SYSTEMS.md').read_text(encoding='utf-8')
    backlog=(ROOT/'INTERNAL_ALPHA_DESIGN_BACKLOG.md').read_text(encoding='utf-8')
    readme=(ROOT/'README.md').read_text(encoding='utf-8')
    packet_index=(PACKETS/'README.md').read_text(encoding='utf-8')
    require(shared,['SS-06 — Proposal and approval framework','IA-D04-002_PROPOSAL_APPROVAL_SHARED_COMPONENT_CONTRACT.md','eight consumer types','IA-D04-003'],'shared systems',errors)
    require(backlog,['IA-D04-002 — proposal and approval shared-component contract — complete','IA-D04-003 — two-device interruption and reconnect matrix — next'],'backlog',errors)
    require(readme,['IA-D04-002 — Proposal and Approval Shared-Component Contract','IA-D04-003 — Two-Device Interruption and Reconnect Matrix'],'program README',errors)
    require(packet_index,['IA-D04-002','Proposal and Approval Shared-Component Contract','IA-D04-003'],'packet index',errors)
    f006=load(PACKETS/'MV-IA-F006_ACTION_APPROVAL_MATRIX.json',errors)
    sfi=load(PACKETS/'IA-D02-006_SHARED_FOUNDATIONS_CONTRACT_MATRIX.json',errors)
    cci=load(PACKETS/'IA-D03-005_CHARACTER_CAMPAIGN_CONTRACT_MATRIX.json',errors)
    if f006.get('featureId')!='MV-IA-F006' or len(f006.get('acceptanceCriteria',[]))!=20 or f006.get('blockingFindings')!=[]: errors.append('F006 baseline incomplete')
    if len(sfi.get('contractOwnership',[]))!=24 or sfi.get('blockingFindings')!=[]: errors.append('shared-foundation baseline incomplete')
    if len(cci.get('contractOwnership',[]))!=28 or cci.get('blockingFindings')!=[]: errors.append('preparation baseline incomplete')
    roadmap=load(ROOT.parent.parent/'ai/runtime/ROADMAP_INDEX.json',errors)
    ids=[x.get('work_item_id') for x in roadmap.get('entries',[])]
    if 'IA-D04-003' not in ids: errors.append('ROADMAP_INDEX missing IA-D04-003')
    if errors: raise SystemExit('IA-D04-002 PROPOSAL/APPROVAL SHARED COMPONENT VALIDATION: FAIL\n'+'\n'.join(f'- {x}' for x in errors))
    print('IA-D04-002 PROPOSAL/APPROVAL SHARED COMPONENT VALIDATION: PASS')
    print('Consumers: 8')
    print('Lifecycle states: 20')
    print('Proposal fields: 30')
    print('Decision fields: 24')
    print('Approval policies: 4')
    print('Validation classes: 24')
    print('Operations: 24')
    print('Events: 24')
    print('Denied cases: 36')
    print('Fixtures: 16')
    print('Slices: 10')
    print('Acceptance criteria: 20')
    print('Blocking findings: 0')
    return 0
if __name__=='__main__': raise SystemExit(main())
