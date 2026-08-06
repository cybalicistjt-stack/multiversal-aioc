#!/usr/bin/env python3
from __future__ import annotations
import json,re,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parent
P=ROOT/'feature-packets'
PACKET=P/'MV-IA-F006_FIRST_PLAYABLE_ACTION_AND_GM_APPROVAL_LOOP.md'
MATRIX=P/'MV-IA-F006_ACTION_APPROVAL_MATRIX.json'
TRACE=P/'MV-IA-F006_IMPLEMENTATION_TRACEABILITY.json'
REVIEW=P/'MV-IA-F006_REVIEW_RECEIPT.md'
READINESS=P/'MV-IA-F006_READINESS_RECORD.md'
COMPLETION=P/'MV-IA-F006_COMPLETION_RECORD.json'
REGISTRY=ROOT/'INTERNAL_ALPHA_FEATURE_REGISTRY.json'
BACKLOG=ROOT/'INTERNAL_ALPHA_DESIGN_BACKLOG.md'
PROGRAM=ROOT/'README.md'
PACKET_INDEX=P/'README.md'
ROADMAP=ROOT.parents[2]/'governance/ai/runtime/ROADMAP_INDEX.json'
EXPECTED_SHARED=[f'SFI-C{i:03d}' for i in range(1,25)]
EXPECTED_PREP=[f'CCI-C{i:03d}' for i in range(1,29)]
EXPECTED_CRITERIA=[f'FPA-AC-{i:03d}' for i in range(1,21)]
EXPECTED_FIXTURES=[f'F006-FX-{i:03d}' for i in range(1,15)]
EXPECTED_SLICES=[f'F006-S{i:02d}' for i in range(1,11)]

def load(path,errors):
    try:return json.loads(path.read_text(encoding='utf-8'))
    except Exception as exc:errors.append(f'cannot parse {path}: {exc}');return {}
def need(ok,msg,errors):
    if not ok:errors.append(msg)
def require_phrases(text,phrases,label,errors):
    low=text.lower()
    for phrase in phrases:
        need(phrase.lower() in low,f'{label} missing required phrase {phrase!r}',errors)

def main():
    errors=[]
    for path in [PACKET,MATRIX,TRACE,REVIEW,READINESS,COMPLETION,REGISTRY,BACKLOG,PROGRAM,PACKET_INDEX,ROADMAP]:
        need(path.is_file(),f'missing required file {path}',errors)
    if errors: raise SystemExit('\n'.join(errors))
    packet=PACKET.read_text(encoding='utf-8'); review=REVIEW.read_text(encoding='utf-8'); readiness=READINESS.read_text(encoding='utf-8')
    backlog=BACKLOG.read_text(encoding='utf-8'); program=PROGRAM.read_text(encoding='utf-8'); index=PACKET_INDEX.read_text(encoding='utf-8')
    matrix=load(MATRIX,errors); trace=load(TRACE,errors); completion=load(COMPLETION,errors); registry=load(REGISTRY,errors); roadmap=load(ROADMAP,errors)
    need(packet.startswith('# MV-IA-F006 — First Playable Action and GM Approval Loop'),'packet title mismatch',errors)
    need('**Design status:** implementation-ready' in packet,'packet not implementation-ready',errors)
    sections=[int(m.group(1)) for line in packet.splitlines() if (m:=re.match(r'^## (\d+)\. ',line))]
    need(sections==list(range(1,25)),f'packet sections must be 1-24 exactly; got {sections}',errors)
    require_phrases(packet,[
      'IA-D02-006','IA-D03-005','MV-IA-F003','MV-IA-F004','MV-IA-F005','MV-IA-F020','MV-IA-F021',
      'approve, deny, or modify-and-approve','GM-controlled NPC and enemy Actions','ActionResultCommitted',
      'Action history and My Proposals remain secondary','status lookup','silent last-write-wins is prohibited',
      'offline authoritative','realtime messages are advisory','zero AI','IA-D04-002','Silence is not approval'
    ],'packet',errors)
    for cid in EXPECTED_CRITERIA:need(cid in packet,f'packet missing {cid}',errors)
    need((matrix.get('programId'),matrix.get('workItemId'),matrix.get('featureId'),matrix.get('owner'),matrix.get('status'))==('MV-IA-001','IA-D04-001','MV-IA-F006','John Brandon Turner','implementation-ready-design'),'matrix identity/status mismatch',errors)
    need(matrix.get('requiredSharedContracts')==EXPECTED_SHARED,'shared contract coverage mismatch',errors)
    need(matrix.get('requiredPreparationContracts')==EXPECTED_PREP,'preparation contract coverage mismatch',errors)
    expected_counts={'stateVocabulary':18,'proposalRequiredFields':28,'decisionReceiptRequiredFields':20,'validationClasses':28,'operationTypes':28,'eventTypes':28,'deniedCases':40,'deterministicFixtures':14,'implementationSlices':10,'acceptanceCriteria':20}
    for key,count in expected_counts.items():need(len(matrix.get(key,[]))==count,f'matrix {key} must contain {count}',errors)
    need([x.get('fixtureId') for x in matrix.get('deterministicFixtures',[])]==EXPECTED_FIXTURES,'fixture IDs mismatch',errors)
    need([x.get('sliceId') for x in matrix.get('implementationSlices',[])]==EXPECTED_SLICES,'slice IDs mismatch',errors)
    need([x.get('criterionId') for x in matrix.get('acceptanceCriteria',[])]==EXPECTED_CRITERIA,'acceptance IDs mismatch',errors)
    need(all(x.get('blocking') is True for x in matrix.get('acceptanceCriteria',[])),'all acceptance criteria must be blocking',errors)
    need(matrix.get('decisionTypes')==['approve','deny','modify-and-approve'],'decision types mismatch',errors)
    need(matrix.get('blockingFindings')==[],'matrix retains blocking findings',errors)
    need(matrix.get('nextWorkItemId')=='IA-D04-002','matrix next work item mismatch',errors)
    for flag in ['implementationAuthorized','paidServicesAuthorized','productionCredentialsAuthorized','realUserDataCollectionAuthorized','internalAlphaReleaseAuthorized','productionAuthorized','publicReleaseAuthorized']:
        need(matrix.get('authorizations',{}).get(flag) is False,f'matrix {flag} must be false',errors)
    need((trace.get('workItemId'),trace.get('featureId'),trace.get('owner'),trace.get('status'))==('IA-D04-001','MV-IA-F006','John Brandon Turner','complete'),'traceability identity mismatch',errors)
    need([x.get('criterionId') for x in trace.get('acceptanceTraceability',[])]==EXPECTED_CRITERIA,'traceability criteria mismatch',errors)
    need([x.get('fixtureId') for x in trace.get('fixtureTraceability',[])]==EXPECTED_FIXTURES,'traceability fixtures mismatch',errors)
    need([x.get('sliceId') for x in trace.get('implementationSlices',[])]==EXPECTED_SLICES,'traceability slices mismatch',errors)
    need(trace.get('untracedAcceptanceCriteria')==[] and trace.get('blockingFindings')==[],'traceability gap or blocking finding',errors)
    metrics=completion.get('metrics',{})
    need((completion.get('workItemId'),completion.get('featureId'),completion.get('status'),completion.get('owner'))==('IA-D04-001','MV-IA-F006','complete-design-implementation-ready','John Brandon Turner'),'completion identity/status mismatch',errors)
    for key,value in {'packetSections':24,'acceptanceCriteria':20,'requiredSharedContracts':24,'requiredPreparationContracts':28,'stateVocabulary':18,'proposalRequiredFields':28,'decisionReceiptFields':20,'validationClasses':28,'operationTypes':28,'eventTypes':28,'deniedCases':40,'fixtures':14,'implementationSlices':10,'blockingFindings':0}.items():
        need(metrics.get(key)==value,f'completion {key} must be {value}',errors)
    need(completion.get('nextDesignAction',{}).get('workItemId')=='IA-D04-002','completion next action mismatch',errors)
    require_phrases(review,['PASS — IMPLEMENTATION-READY DESIGN','twenty-four shared-foundation contracts','forty denied cases','fourteen deterministic fixtures','GM-controlled NPC and enemy Actions','IA-D04-002','Silence is not approval'],'review receipt',errors)
    require_phrases(readiness,['READY FOR IMPLEMENTATION HANDOFF — DEPENDENCY GATED','approve, deny, and field-addressed modify-and-approve','fourteen deterministic fixtures','zero-service and zero-AI','IA-D04-002'],'readiness',errors)
    features={x.get('featureId'):x for x in registry.get('features',[])}; f006=features.get('MV-IA-F006',{})
    need(f006.get('designStatus')=='implementation-ready','registry does not mark F006 implementation-ready',errors)
    need(f006.get('packetPath')=='feature-packets/MV-IA-F006_FIRST_PLAYABLE_ACTION_AND_GM_APPROVAL_LOOP.md','registry packet path mismatch',errors)
    companions=set(f006.get('companionFiles',[]))
    need('feature-packets/MV-IA-F006_ACTION_APPROVAL_MATRIX.json' in companions and 'feature-packets/MV-IA-F006_IMPLEMENTATION_TRACEABILITY.json' in companions,'registry companions incomplete',errors)
    require_phrases(backlog,['IA-D04-001 — MV-IA-F006 First Playable Action and GM Approval Loop — complete','IA-D04-002 — proposal and approval shared-component contract — next'],'backlog',errors)
    require_phrases(program,['IA-D04-001 — First Playable Action and GM Approval Loop','IA-D04-002 — Proposal and Approval Shared-Component Contract'],'program README',errors)
    require_phrases(index,['| MV-IA-F006 | First Playable Action and GM Approval Loop |','`MV-IA-F006_ACTION_APPROVAL_MATRIX.json`','IA-D04-002'],'packet index',errors)
    ids={x.get('work_item_id') for x in roadmap.get('entries',[])}
    need({'IA-D04-001','IA-D04-002'}<=ids,'roadmap index missing IA-D04-001 or IA-D04-002',errors)
    if errors:
        print('MV-IA-F006 FIRST PLAYABLE ACTION/GM APPROVAL DESIGN VALIDATION: FAIL')
        for error in errors:print(f'- {error}')
        return 1
    print('MV-IA-F006 FIRST PLAYABLE ACTION/GM APPROVAL DESIGN VALIDATION: PASS')
    print('Packet sections: 24\nAcceptance criteria: 20\nShared contracts: 24\nPreparation contracts: 28\nProposal states: 18\nProposal fields: 28\nDecision receipt fields: 20\nValidation classes: 28\nOperation types: 28\nEvent types: 28\nDenied cases: 40\nFixtures: 14\nImplementation slices: 10\nBlocking findings: 0')
    return 0
if __name__=='__main__':sys.exit(main())
