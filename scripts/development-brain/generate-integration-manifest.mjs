import fs from 'node:fs';
import path from 'node:path';

const root = process.cwd();
const outputPath = process.argv[2] || 'governance/development-brain/integration/AIOC_INTEGRATION_MANIFEST.generated.json';
const resolvePath = value => path.isAbsolute(value) ? value : path.join(root, value);

const artifacts = [
  ['project-memory', 'governance/development-brain/project-memory'],
  ['unified-inventory', 'tmp/AIOC_UNIFIED_INVENTORY.json'],
  ['dependency-graph', 'tmp/AIOC_DEPENDENCY_GRAPH.json'],
  ['structure-intelligence', 'tmp/AIOC_STRUCTURE_INTELLIGENCE.json'],
  ['completion-readiness', 'tmp/AIOC_COMPLETION_READINESS.json'],
  ['priority-impact', 'tmp/AIOC_PRIORITY_IMPACT.json'],
  ['recommendation-planner', 'tmp/AIOC_RECOMMENDATION_PLANNER.json'],
  ['verification-governance', 'tmp/AIOC_VERIFICATION_GOVERNANCE.json']
].map(([artifactId, sourcePath]) => ({
  artifactId,
  sourcePath,
  authority: 'derived-advisory',
  freshnessToken: `git-ref:${process.env.GITHUB_SHA || 'working-tree'}`,
  provenanceRequired: true
}));

const sharedAuthority = {
  reads: 'Allowed for validated Development Brain artifacts and canonical governance records.',
  writes: 'Proposal-only; direct canonical mutation is prohibited.',
  approval: 'Owner or governance approval remains external and explicit.'
};
const staleDetection = {
  method: 'Compare artifact freshnessToken and source commit/ref before use.',
  staleBehavior: 'Reject executable interpretation and require regeneration.'
};
const audit = {
  requiredFields: ['surfaceId', 'requestId', 'artifactId', 'sourceRef', 'operation', 'timestamp', 'outcome'],
  retention: 'Repository or service audit log according to deployment policy.'
};

const surfaces = [
  {
    surfaceId: 'SURFACE-BROWSER', kind: 'browser', mode: 'read-only',
    endpoint: '/operational/development-brain/',
    capabilities: ['browse-artifacts', 'filter-findings', 'inspect-evidence', 'display-stale-warning'],
    authority: sharedAuthority, staleDetection, audit, advisory: true
  },
  {
    surfaceId: 'SURFACE-MCP', kind: 'mcp', mode: 'proposal-only',
    endpoint: '/mcp',
    capabilities: ['list-development-brain-artifacts', 'get-development-brain-record', 'search-development-brain', 'create-governed-proposal'],
    authority: sharedAuthority, staleDetection, audit, advisory: true
  },
  {
    surfaceId: 'SURFACE-REST', kind: 'rest', mode: 'proposal-only',
    endpoint: '/api/development-brain/v1',
    capabilities: ['GET /manifest', 'GET /artifacts', 'GET /artifacts/:id', 'POST /proposals'],
    authority: sharedAuthority, staleDetection, audit, advisory: true
  },
  {
    surfaceId: 'SURFACE-CODEX', kind: 'codex', mode: 'proposal-only',
    endpoint: 'bridge/skills/multiversal-aioc/SKILL.md',
    capabilities: ['read-governed-context', 'select-verified-task', 'prepare-bounded-change', 'run-validation', 'submit-reviewable-proposal'],
    authority: sharedAuthority, staleDetection, audit, advisory: true
  }
];

const result = {
  format: 'multiversal-aioc-development-brain-integration',
  version: '1.0.0',
  generatedAt: new Date().toISOString(),
  policy: {
    readWriteBoundary: 'Validated artifacts may be read; all writes are governed proposals.',
    canonicalMutationRule: 'No integration surface may directly mutate, promote, or certify canonical content.',
    approvalRule: 'No integration surface may infer or grant owner or governance approval.',
    staleRule: 'Stale or source-mismatched artifacts cannot support executable eligibility.',
    auditRule: 'Every integration request must preserve source reference, operation, and outcome.'
  },
  artifacts,
  surfaces,
  summary: {
    artifactCount: artifacts.length,
    surfaceCount: surfaces.length,
    readOnlySurfaces: surfaces.filter(item => item.mode === 'read-only').length,
    proposalOnlySurfaces: surfaces.filter(item => item.mode === 'proposal-only').length
  }
};

fs.mkdirSync(path.dirname(resolvePath(outputPath)), { recursive: true });
fs.writeFileSync(resolvePath(outputPath), `${JSON.stringify(result, null, 2)}\n`);
console.log(`Generated Step 9 integration manifest at ${outputPath}.`);
