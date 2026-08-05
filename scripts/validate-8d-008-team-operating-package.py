#!/usr/bin/env python3
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
contract_path = ROOT / 'governance/ai-team/8D-008_AI_DEVELOPMENT_TEAM_OPERATING_CONTRACT.json'
playbook_path = ROOT / 'governance/ai-team/8D-008_EXECUTION_AND_HANDOFF_PLAYBOOK.md'
contract = json.loads(contract_path.read_text())
playbook = playbook_path.read_text()

assert contract['documentId'] == 'MV-8D-008-TEAM-OPERATING-CONTRACT-001'
assert contract['owner'] == 'John Brandon Turner'
assert contract['authorityModel']['repository'] == 'canonical source of truth'
assert contract['governance']['truthfulCompletionClaimsRequired'] is True
assert contract['governance']['fabricatedExecutionProhibited'] is True
assert contract['governance']['independentVerificationRequiredForMerge'] is True
assert contract['governance']['continuousExecutionDefault'] is True

roles = {role['roleId'] for role in contract['teamRoles']}
required_roles = {
    'orchestrator', 'repository-architect', 'implementation-agent',
    'verification-agent', 'domain-agent', 'release-agent'
}
assert roles == required_roles

lifecycle = contract['workLifecycle']
for required in ['bootstrap', 'independent-verification', 'inspect-ci', 'repair-failures', 'merge', 'continue-next-item']:
    assert required in lifecycle

for phrase in [
    'The repository is canonical.',
    'Agents execute rather than narrate.',
    'claimed commit must exist',
    'claimed pull request must exist',
    'claimed CI result must be fetched',
    'accidental writes to `main`'
]:
    assert phrase in playbook, phrase

report = {
    'format': 'multiversal-8d-008-team-operating-package-validation',
    'version': '0.1.0',
    'roleCount': len(roles),
    'lifecycleStageCount': len(lifecycle),
    'mandatoryOwnerGateCount': len(contract['authorityModel']['mandatoryOwnerGates']),
    'requiredEvidenceSections': sorted(contract['requiredEvidence'].keys()),
    'truthfulnessGuardsPresent': True,
    'independentVerificationRequired': True,
    'continuousExecutionDefault': True,
    'valid': True
}
out = ROOT / 'out/8d-008-team-operating-package'
out.mkdir(parents=True, exist_ok=True)
(out / 'validation-report.json').write_text(json.dumps(report, indent=2, sort_keys=True) + '\n')
print(json.dumps(report, sort_keys=True))
