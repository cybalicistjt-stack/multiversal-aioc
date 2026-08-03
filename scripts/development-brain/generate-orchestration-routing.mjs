import fs from 'node:fs';
import path from 'node:path';
import crypto from 'node:crypto';
import { execFileSync } from 'node:child_process';

const root = process.cwd();
const contractsPath = process.argv[2] || 'tmp/AIOC_SPECIALIST_AGENT_CONTRACTS.json';
const outputPath = process.argv[3] || 'governance/development-brain/orchestration-routing/AIOC_ORCHESTRATION_ROUTING.generated.json';
const resolvePath = value => path.isAbsolute(value) ? value : path.join(root, value);
if (!fs.existsSync(resolvePath(contractsPath))) execFileSync(process.execPath, ['scripts/development-brain/generate-specialist-agent-contracts.mjs', contractsPath], { cwd: root, stdio: 'inherit' });
const source = JSON.parse(fs.readFileSync(resolvePath(contractsPath), 'utf8'));
const hash = value => crypto.createHash('sha256').update(String(value)).digest('hex');
const coordinator = source.contracts.find(c => c.roleId === 'AGENT-ROLE-DEVELOPMENT-COORDINATOR');
if (!coordinator) throw new Error('Development Coordinator contract is required.');

const classes = [
  ['knowledge-retrieval', ['retrieval', 'inventory', 'provenance']],
  ['rules-mechanics', ['rules', 'mechanics', 'balance']],
  ['setting-lore', ['settings', 'lore', 'canon']],
  ['content-pack', ['packs', 'schemas', 'structure']],
  ['application-ux', ['application', 'ui', 'ux', 'accessibility']],
  ['verification-testing', ['validation', 'testing', 'regression', 'coverage']],
  ['governance-authority', ['governance', 'authority', 'approval', 'lifecycle']],
  ['cross-domain-coordination', ['coordination', 'routing', 'synthesis']]
];

const routes = classes.map(([taskClass, scopes]) => {
  const eligible = source.contracts.filter(c => c.roleId !== coordinator.roleId && c.domainScope.some(scope => scopes.includes(scope)));
  const exact = eligible.filter(c => scopes.some(scope => c.domainScope[0] === scope));
  const selected = (exact.length === 1 ? exact[0] : eligible.length === 1 ? eligible[0] : null);
  const status = selected ? 'routable' : eligible.length > 1 ? 'ambiguous' : 'blocked';
  const handoff = selected ? source.handoffs.find(h => h.fromRoleId === coordinator.roleId && h.toRoleId === selected.roleId) : null;
  const authorityMode = selected?.authorityMode || 'advisory';
  return {
    routeId: `ROUTE-${taskClass.toUpperCase()}`,
    taskClass,
    coordinatorRoleId: coordinator.roleId,
    eligibleRoleIds: eligible.map(c => c.roleId).sort(),
    selectedRoleId: selected?.roleId || null,
    requiredInputs: selected?.requiredInputs || [],
    permittedOutputs: selected?.permittedOutputs || [],
    handoff: {
      fromRoleId: coordinator.roleId,
      toRoleId: selected?.roleId || null,
      requiredPayload: handoff?.requiredPayload || ['task identity', 'evidence pointers', 'constraints', 'authority mode', 'expected output type'],
      authorityPreserved: true
    },
    status,
    reasons: selected ? ['Narrowest eligible specialist selected deterministically from governed scope.'] : eligible.length ? ['Multiple eligible specialists require coordinator or owner resolution.'] : ['No governed specialist capability matches this task class.'],
    evidence: [{ sourcePath: contractsPath, pointer: '/contracts', claim: 'Routing is derived only from validated specialist contracts and handoffs.' }],
    freshness: { sourceFingerprint: source.sourceFingerprint, stale: false },
    authorityMode
  };
});

const ambiguousRoutes = routes.filter(r => r.status === 'ambiguous').map(r => ({ routeId: r.routeId, eligibleRoleIds: r.eligibleRoleIds }));
const missingInputs = routes.filter(r => r.status === 'routable' && !r.requiredInputs.length).map(r => ({ routeId: r.routeId }));
const unavailableCapabilities = routes.filter(r => r.status === 'blocked').map(r => ({ routeId: r.routeId, taskClass: r.taskClass }));
const authorityMismatches = routes.filter(r => !['read-only', 'advisory', 'proposal-only'].includes(r.authorityMode)).map(r => ({ routeId: r.routeId }));
const invalidHandoffs = routes.filter(r => r.status === 'routable' && (!r.handoff.toRoleId || !r.handoff.authorityPreserved)).map(r => ({ routeId: r.routeId }));
const circularRouting = source.diagnostics?.circularHandoffs || [];

const artifact = {
  format: 'multiversal-aioc-orchestration-routing',
  version: '1.0.0',
  generatedAt: '2026-08-03T00:00:00.000Z',
  sourceFingerprint: hash(JSON.stringify(source)),
  routes,
  diagnostics: { ambiguousRoutes, missingInputs, unavailableCapabilities, authorityMismatches, invalidHandoffs, circularRouting },
  authority: { advisoryOnly: true, executionAllowed: false, canonicalMutationAllowed: false, approvalGranted: false, assignmentAllowed: false, schedulingAllowed: false }
};
fs.mkdirSync(path.dirname(resolvePath(outputPath)), { recursive: true });
fs.writeFileSync(resolvePath(outputPath), `${JSON.stringify(artifact, null, 2)}\n`);
console.log(`Generated ${routes.length} governed routes at ${outputPath}`);
