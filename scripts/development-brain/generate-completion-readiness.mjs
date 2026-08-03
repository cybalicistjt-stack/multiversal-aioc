import fs from 'node:fs';
import path from 'node:path';
import { execFileSync } from 'node:child_process';

const root = process.cwd();
const resolvePath = value => path.isAbsolute(value) ? value : path.join(root, value);
const inventoryPath = process.argv[2] || 'tmp/AIOC_UNIFIED_INVENTORY.json';
const graphPath = process.argv[3] || 'tmp/AIOC_DEPENDENCY_GRAPH.json';
const structurePath = process.argv[4] || 'tmp/AIOC_STRUCTURE_INTELLIGENCE.json';
const outputPath = process.argv[5] || 'governance/development-brain/completion-readiness/AIOC_COMPLETION_READINESS.generated.json';

function ensure(file, command, args) {
  if (!fs.existsSync(resolvePath(file))) execFileSync(process.execPath, [command, ...args], { cwd: root, stdio: 'inherit' });
}
ensure(inventoryPath, 'scripts/development-brain/generate-unified-inventory.mjs', [inventoryPath]);
ensure(graphPath, 'scripts/development-brain/generate-dependency-graph.mjs', [inventoryPath, graphPath]);
ensure(structurePath, 'scripts/development-brain/generate-structure-intelligence.mjs', [inventoryPath, graphPath, structurePath]);

const inventory = JSON.parse(fs.readFileSync(resolvePath(inventoryPath), 'utf8'));
const graph = JSON.parse(fs.readFileSync(resolvePath(graphPath), 'utf8'));
const structure = JSON.parse(fs.readFileSync(resolvePath(structurePath), 'utf8'));
const edgesBySource = new Map();
for (const edge of graph.edges || []) {
  if (!edgesBySource.has(edge.source)) edgesBySource.set(edge.source, []);
  edgesBySource.get(edge.source).push(edge);
}
const structuralFindings = new Map();
for (const key of ['unresolvedClassifications', 'structuralGaps', 'orphans', 'conflicts']) {
  for (const finding of structure[key] || []) {
    const stableId = finding.stableId || finding.objectStableId || finding.subjectStableId;
    if (!stableId) continue;
    if (!structuralFindings.has(stableId)) structuralFindings.set(stableId, []);
    structuralFindings.get(stableId).push({ key, finding });
  }
}
const clamp = value => Math.max(0, Math.min(100, Math.round(value)));
const hasText = value => typeof value === 'string' && value.trim().length > 0;

const objects = (inventory.objects || []).map(object => {
  const nodeId = `NODE-${object.stableId}`;
  const outgoing = edgesBySource.get(nodeId) || [];
  const requires = outgoing.filter(edge => edge.relationship === 'requires');
  const blocking = outgoing.filter(edge => edge.relationship === 'blocks');
  const findings = structuralFindings.get(object.stableId) || [];
  const refs = object.references || {};
  const evidenceCount = ['balanceEvidence', 'testingEvidence', 'reviewItems', 'memoryIds'].reduce((sum, key) => sum + (Array.isArray(refs[key]) ? refs[key].length : 0), 0);
  const identity = clamp([object.stableId, object.inventoryId, object.name, object.objectType].filter(hasText).length * 25);
  const content = clamp((hasText(object.name) ? 25 : 0) + (hasText(object.objectType) && object.objectType !== 'Unknown' ? 25 : 0) + (object.provenance ? 25 : 0) + (object.sourceRecord ? 25 : 0));
  const evidence = clamp(Math.min(100, evidenceCount * 25));
  const structureScore = clamp(100 - findings.length * 25);
  const dependencyScore = clamp(100 - requires.filter(edge => !graph.nodes?.some(node => node.nodeId === edge.target)).length * 50 - blocking.length * 25);
  const governance = object.authorityLayer === 'canonical' ? 100 : ['review', 'game-ready', 'canonical'].includes(object.lifecycle) ? 90 : ['validation', 'development'].includes(object.lifecycle) ? 70 : 45;
  const scores = { identity, content, evidence, structure: structureScore, dependencies: dependencyScore, governance };
  const score = clamp(identity * 0.15 + content * 0.2 + evidence * 0.15 + structureScore * 0.2 + dependencyScore * 0.15 + governance * 0.15);
  const blockers = [];
  if (identity < 100) blockers.push({ code: 'IDENTITY_INCOMPLETE', severity: 'critical', message: 'Stable identity or classification fields are incomplete.', source: inventory.sources?.canonicalContent?.path || 'unified inventory' });
  if (findings.length) blockers.push({ code: 'STRUCTURE_UNRESOLVED', severity: findings.some(item => item.key === 'conflicts') ? 'critical' : 'major', message: `${findings.length} unresolved structural finding(s).`, source: 'structure intelligence' });
  if (blocking.length) blockers.push({ code: 'DECLARED_BLOCKER', severity: 'critical', message: `${blocking.length} declared blocking relationship(s).`, source: 'dependency graph' });
  if (requires.some(edge => !graph.nodes?.some(node => node.nodeId === edge.target))) blockers.push({ code: 'DEPENDENCY_MISSING', severity: 'critical', message: 'At least one required dependency is unresolved.', source: 'dependency graph' });
  if (object.authorityLayer === 'working' && !['review', 'game-ready', 'canonical'].includes(object.lifecycle)) blockers.push({ code: 'GOVERNANCE_STAGE', severity: 'major', message: `Working object lifecycle is ${object.lifecycle}.`, source: 'unified inventory' });
  if (evidenceCount === 0) blockers.push({ code: 'EVIDENCE_ABSENT', severity: 'major', message: 'No balance, testing, review, or memory evidence is linked.', source: 'unified inventory' });
  const critical = blockers.some(blocker => blocker.severity === 'critical');
  const promotionReady = object.authorityLayer === 'working' && !critical && score >= 85 && ['review', 'game-ready'].includes(object.lifecycle);
  const status = critical ? 'blocked' : score >= 90 ? 'ready' : score >= 75 ? 'review-ready' : 'incomplete';
  const reasons = [
    `Overall readiness score is ${score}.`,
    `${evidenceCount} linked evidence record(s) were found.`,
    `${findings.length} structural finding(s) and ${requires.length} required dependency relationship(s) were evaluated.`,
    promotionReady ? 'The object satisfies the derived promotion-readiness rule; owner approval is still required.' : 'The object does not satisfy the derived promotion-readiness rule.'
  ];
  return {
    readinessId: `READY-${object.stableId}`,
    stableId: object.stableId,
    inventoryId: object.inventoryId,
    name: object.name,
    objectType: object.objectType,
    authorityLayer: object.authorityLayer,
    lifecycle: object.lifecycle,
    scores,
    score,
    status,
    promotionReady,
    blockers,
    reasons,
    evidence: [
      { sourcePath: inventory.sources?.canonicalContent?.path || 'content-db/index.json', pointer: `/objects/${object.stableId}`, claim: 'Identity, lifecycle, provenance, and linked evidence basis.' },
      { sourcePath: 'dependency graph', pointer: nodeId, claim: 'Required and blocking dependency basis.' },
      { sourcePath: 'structure intelligence', pointer: object.stableId, claim: 'Structural finding basis.' }
    ]
  };
}).sort((a, b) => a.stableId.localeCompare(b.stableId));

const count = status => objects.filter(object => object.status === status).length;
const averageScore = objects.length ? Math.round((objects.reduce((sum, object) => sum + object.score, 0) / objects.length) * 100) / 100 : 0;
const result = {
  format: 'multiversal-aioc-completion-readiness',
  version: '1.0.0',
  generatedAt: new Date().toISOString(),
  sources: { inventory: inventoryPath, dependencyGraph: graphPath, structureIntelligence: structurePath },
  policy: {
    scoreRange: '0-100',
    promotionRule: 'Working object, no critical blockers, score >= 85, lifecycle review or game-ready; owner approval remains mandatory.',
    authorityRule: 'Derived readiness never edits source content, promotes an object, or overrides owner authority.'
  },
  summary: { totalObjects: objects.length, ready: count('ready'), reviewReady: count('review-ready'), blocked: count('blocked'), incomplete: count('incomplete'), averageScore },
  objects
};
fs.mkdirSync(path.dirname(resolvePath(outputPath)), { recursive: true });
fs.writeFileSync(resolvePath(outputPath), `${JSON.stringify(result, null, 2)}\n`);
console.log(`Generated readiness assessments for ${objects.length} objects at ${outputPath}.`);
