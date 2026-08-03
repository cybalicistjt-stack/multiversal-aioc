import fs from 'node:fs';
import path from 'node:path';
import crypto from 'node:crypto';

const root = process.cwd();
const outputPath = process.argv[2] || 'governance/development-brain/specialist-agents/AIOC_SPECIALIST_AGENT_CONTRACTS.generated.json';
const resolvePath = value => path.isAbsolute(value) ? value : path.join(root, value);
const hash = value => crypto.createHash('sha256').update(String(value)).digest('hex');

const sharedProhibitions = [
  'Do not mutate canonical content.',
  'Do not grant approval, promotion, certification, assignment, or scheduling authority.',
  'Do not conceal uncertainty, conflicting evidence, stale inputs, or unresolved questions.',
  'Do not exceed the authority carried by the source artifact or handoff.'
];
const sharedEvidence = [
  'Cite stable source paths or artifact identities for every material claim.',
  'Preserve provenance, confidence, freshness, derivation method, and authority.',
  'Distinguish source facts from derived findings, recommendations, and unresolved questions.'
];
const sharedHandoff = [
  'Include originating role, target role, task classification, evidence pointers, constraints, unresolved questions, and authority mode.',
  'Use stable subject and recommendation identities where available.',
  'Preserve blockers and approval requirements without reinterpretation.'
];

const definitions = [
  {
    role: 'knowledge-librarian', name: 'Knowledge Librarian', scope: ['inventory', 'provenance', 'retrieval', 'knowledge-quality'],
    responsibilities: ['Assemble source-backed context.', 'Detect stale, duplicate, unsupported, or missing knowledge.', 'Maintain retrieval and provenance discipline.'],
    inputs: ['Unified Object Inventory', 'Semantic Retrieval', 'Project Memory'], outputs: ['context-package', 'knowledge-gap-report', 'provenance-review'], authority: 'read-only',
    escalations: ['Missing or contradictory provenance.', 'Stale context package.', 'Unsupported semantic assertion.']
  },
  {
    role: 'rules-mechanics-architect', name: 'Rules and Mechanics Architect', scope: ['rules', 'mechanics', 'resources', 'progression', 'balance'],
    responsibilities: ['Analyze cross-domain mechanical consistency.', 'Trace rule dependencies and impact paths.', 'Prepare bounded mechanics proposals.'],
    inputs: ['Dependency Graph', 'Causal Impact', 'Design Intent', 'Constraint Rationale'], outputs: ['mechanics-analysis', 'rule-conflict-report', 'proposal-draft'], authority: 'proposal-only',
    escalations: ['Owner intent conflict.', 'Unresolved causal hypothesis.', 'Cross-domain rule contradiction.']
  },
  {
    role: 'setting-lore-architect', name: 'Setting and Lore Architect', scope: ['settings', 'lore', 'canon', 'continuity', 'world-packs'],
    responsibilities: ['Review setting continuity and pack relationships.', 'Identify unsupported canon claims.', 'Prepare source-bounded lore proposals.'],
    inputs: ['Semantic Ontology', 'Design Intent', 'Decision History', 'Semantic Retrieval'], outputs: ['continuity-review', 'canon-gap-report', 'lore-proposal'], authority: 'proposal-only',
    escalations: ['Conflicting owner-approved canon.', 'Missing source material.', 'Cross-setting continuity conflict.']
  },
  {
    role: 'content-pack-architect', name: 'Content and Pack Architect', scope: ['packs', 'schemas', 'objects', 'structure', 'compatibility'],
    responsibilities: ['Classify object and pack structure.', 'Review stable IDs and containment.', 'Prepare bounded pack and schema proposals.'],
    inputs: ['Unified Object Inventory', 'Structure Intelligence', 'Dependency Graph', 'Completion Readiness'], outputs: ['structure-review', 'pack-plan', 'schema-proposal'], authority: 'proposal-only',
    escalations: ['Ambiguous object identity.', 'Conflicting structure decisions.', 'Breaking dependency or uninstall risk.']
  },
  {
    role: 'application-ux-architect', name: 'Application and UX Architect', scope: ['application', 'ui', 'ux', 'accessibility', 'interaction'],
    responsibilities: ['Translate governed requirements into interface proposals.', 'Review workflow clarity and accessibility.', 'Preserve gameplay and governance intent in UI decisions.'],
    inputs: ['Design Intent', 'Decision History', 'Semantic Retrieval', 'Recommendation Planner'], outputs: ['ux-review', 'interface-specification', 'implementation-proposal'], authority: 'proposal-only',
    escalations: ['UI request conflicts with governance.', 'Missing user-flow evidence.', 'Accessibility or authority risk.']
  },
  {
    role: 'verification-testing-agent', name: 'Verification and Testing Agent', scope: ['validation', 'testing', 'regression', 'coverage', 'quality'],
    responsibilities: ['Validate artifacts and proposals against explicit contracts.', 'Identify regressions and missing coverage.', 'Produce auditable verification records.'],
    inputs: ['Verification Governance', 'Completion Readiness', 'Recommendation Planner', 'repository checks'], outputs: ['verification-record', 'regression-risk-report', 'coverage-gap-report'], authority: 'advisory',
    escalations: ['Failed required validation.', 'Insufficient evidence.', 'Authority or lifecycle incompatibility.']
  },
  {
    role: 'governance-provenance-agent', name: 'Governance and Provenance Agent', scope: ['governance', 'authority', 'approval', 'provenance', 'lifecycle'],
    responsibilities: ['Review authority and lifecycle compatibility.', 'Preserve owner decisions and evidence chains.', 'Block unauthorized execution or mutation.'],
    inputs: ['Project Memory', 'Decision History', 'Constraint Rationale', 'Verification Governance'], outputs: ['governance-review', 'authority-decision-support', 'escalation-record'], authority: 'advisory',
    escalations: ['Owner decision required.', 'Authority conflict.', 'Attempted canonical mutation without approval.']
  },
  {
    role: 'development-coordinator', name: 'Development Coordinator', scope: ['coordination', 'prioritization', 'routing', 'handoff', 'synthesis'],
    responsibilities: ['Route work to the narrowest supported specialist.', 'Assemble bounded task context.', 'Coordinate recommendations without executing them.'],
    inputs: ['Priority and Impact', 'Recommendation Planner', 'Verification Governance', 'Specialist Agent Contracts'], outputs: ['routing-proposal', 'task-context-package', 'coordination-summary'], authority: 'proposal-only',
    escalations: ['No supported specialist.', 'Multiple equal-authority specialists disagree.', 'Owner approval or cross-domain synthesis required.']
  }
];

const contracts = definitions.map(item => ({
  contractId: `AGENT-CONTRACT-${item.role.toUpperCase()}`,
  roleId: `AGENT-ROLE-${item.role.toUpperCase()}`,
  name: item.name,
  domainScope: item.scope,
  responsibilities: item.responsibilities,
  requiredInputs: item.inputs,
  permittedOutputs: item.outputs,
  evidenceRequirements: sharedEvidence,
  escalationTriggers: item.escalations,
  handoffRequirements: sharedHandoff,
  prohibitedActions: sharedProhibitions,
  authorityMode: item.authority
}));

const coordinator = 'AGENT-ROLE-DEVELOPMENT-COORDINATOR';
const handoffs = contracts.filter(c => c.roleId !== coordinator).flatMap(c => [
  { handoffId: `AGENT-HANDOFF-COORDINATOR-TO-${c.roleId.slice(11)}`, fromRoleId: coordinator, toRoleId: c.roleId, trigger: 'Task domain matches specialist scope and required inputs are available.', requiredPayload: ['task identity', 'evidence pointers', 'constraints', 'authority mode', 'expected output type'], authorityPreserved: true },
  { handoffId: `AGENT-HANDOFF-${c.roleId.slice(11)}-TO-COORDINATOR`, fromRoleId: c.roleId, toRoleId: coordinator, trigger: 'Specialist completes analysis or requires escalation.', requiredPayload: ['findings', 'evidence', 'confidence', 'unresolved questions', 'escalation status'], authorityPreserved: true }
]);

const scopeOwners = new Map();
const roleOverlaps = [];
for (const contract of contracts) for (const scope of contract.domainScope) {
  const owners = scopeOwners.get(scope) || [];
  owners.push(contract.roleId);
  scopeOwners.set(scope, owners);
}
for (const [scope, owners] of scopeOwners) if (owners.length > 1 && !['provenance', 'governance'].includes(scope)) roleOverlaps.push({ scope, roleIds: owners, resolution: 'Coordinator must route by required output and narrowest responsibility.' });

const requiredCapabilities = ['retrieval', 'rules', 'settings', 'packs', 'ui', 'testing', 'governance', 'coordination'];
const covered = new Set(contracts.flatMap(c => c.domainScope));
const missingCapabilities = requiredCapabilities.filter(capability => !covered.has(capability)).map(capability => ({ capability, severity: 'blocking' }));
const authorityConflicts = contracts.filter(c => !['read-only', 'advisory', 'proposal-only'].includes(c.authorityMode)).map(c => ({ roleId: c.roleId }));

const artifact = {
  format: 'multiversal-aioc-specialist-agent-contracts',
  version: '1.0.0',
  generatedAt: '2026-08-03T00:00:00.000Z',
  sourceFingerprint: hash(JSON.stringify(definitions)),
  contracts,
  handoffs,
  diagnostics: { roleOverlaps, missingCapabilities, circularHandoffs: [], unsupportedSpecializations: [], authorityConflicts },
  authority: { advisoryOnly: true, canonicalMutationAllowed: false, approvalGranted: false, certificationAllowed: false }
};

fs.mkdirSync(path.dirname(resolvePath(outputPath)), { recursive: true });
fs.writeFileSync(resolvePath(outputPath), `${JSON.stringify(artifact, null, 2)}\n`);
console.log(`Generated ${contracts.length} specialist contracts and ${handoffs.length} governed handoffs at ${outputPath}`);
