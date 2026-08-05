#!/usr/bin/env python3
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
roles = json.loads((ROOT/'governance/ai/8D-008_EXECUTABLE_ROLE_PROMPTS.json').read_text())
routing = json.loads((ROOT/'governance/ai/8D-008_TASK_ROUTING_AND_HANDOFF_SCHEMA.json').read_text())
role_ids = {r['id'] for r in roles['roles']}
required = set(routing['handoffRequiredFields'])

stages = [
    ('route','orchestrator','implementation-agent'),
    ('implement','implementation-agent','verification-agent'),
    ('verify','verification-agent','ci-incident-agent'),
    ('ci-review','ci-incident-agent','release-handoff-agent'),
    ('release','release-handoff-agent','orchestrator'),
]
base = {
    'workItemId':'SIM-8D-008-001',
    'objective':'Add a governed deterministic validator without changing canonical mechanics.',
    'repository':'cybalicistjt-stack/multiversal-aioc',
    'baseSha':'246dcbbd0e78c8e4f7a2256d38c9f2f3cb4e8bbd',
    'branch':'governance/8d-008-executable-team-package',
    'scopePaths':['governance/ai/**','scripts/simulate-8d-008-multi-agent-workstream.py','.github/workflows/validate-8d-008-executable-team-package.yml'],
    'requirements':['role accountability','independent verification','truthful completion','SHA-anchored handoff'],
    'openRisks':[],
    'approvalGate':'none',
}
handovers=[]
for index,(stage,source,target) in enumerate(stages,1):
    assert source in role_ids and target in role_ids
    evidence=[{'kind':'executed','claim':stage,'reference':f'simulation-stage-{index}'}]
    if source=='verification-agent': evidence.append({'kind':'observed','claim':'independent review passed','reference':'simulation-independent-review'})
    item={**base,'handoffId':f'SIM-HO-{index:02d}','fromRole':source,'toRole':target,'evidence':evidence,'nextAction':stages[index][0] if index<len(stages) else 'workstream-complete'}
    assert required.issubset(item)
    handovers.append(item)

assert any(h['fromRole']=='verification-agent' for h in handovers)
assert handovers[-1]['nextAction']=='workstream-complete'
payload={
    'format':'multiversal-8d-008-multi-agent-simulation',
    'version':'0.1.0',
    'roleCount':len(role_ids),
    'handoffCount':len(handovers),
    'independentVerificationPresent':True,
    'allRequiredHandoffFieldsPresent':True,
    'unsupportedCompletionClaims':0,
    'sourceTruthChanged':False,
    'workstreamCompleted':True,
    'handoffs':handovers,
}
canonical=json.dumps(payload,sort_keys=True,separators=(',',':')).encode()
payload['artifactSha256']=hashlib.sha256(canonical).hexdigest()
out=ROOT/'out/8d-008-team-simulation'; out.mkdir(parents=True,exist_ok=True)
(out/'MULTI_AGENT_WORKSTREAM_REPORT.json').write_text(json.dumps(payload,indent=2,sort_keys=True)+'\n')
print(json.dumps({k:payload[k] for k in ['roleCount','handoffCount','workstreamCompleted','artifactSha256']}))
