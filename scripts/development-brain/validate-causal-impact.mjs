import fs from 'node:fs';
import path from 'node:path';

const file = process.argv[2] || 'governance/development-brain/causal-impact/AIOC_CAUSAL_IMPACT.generated.json';
const resolved = path.isAbsolute(file) ? file : path.join(process.cwd(), file);
const data = JSON.parse(fs.readFileSync(resolved, 'utf8'));
const issues = [];
if (data.format !== 'multiversal-aioc-causal-impact') issues.push('Invalid format.');
if (data.version !== '1.0.0') issues.push('Unsupported version.');
if (!Array.isArray(data.impactPaths)) issues.push('impactPaths must be an array.');
if (!Array.isArray(data.unresolvedHypotheses)) issues.push('unresolvedHypotheses must be an array.');
const ids = new Set();
for (const [index, item] of (data.impactPaths || []).entries()) {
  const label = `impactPaths[${index}]`;
  if (!item.impactPathId || ids.has(item.impactPathId)) issues.push(`${label}: missing or duplicate impactPathId.`);
  ids.add(item.impactPathId);
  if (!['direct-causal-evidence', 'dependency-impact', 'structural-impact'].includes(item.classification)) issues.push(`${label}: invalid classification.`);
  if (!Array.isArray(item.relationshipChain) || item.relationshipChain.length !== item.hopCount || item.hopCount < 1 || item.hopCount > 4) issues.push(`${label}: invalid bounded relationship chain.`);
  if (!['explicit', 'high', 'medium', 'low'].includes(item.confidence)) issues.push(`${label}: invalid confidence.`);
  if (!['direct-semantic-assertion', 'bounded-graph-propagation'].includes(item.derivationMethod)) issues.push(`${label}: invalid derivation method.`);
  if (item.classification === 'direct-causal-evidence' && (item.relationshipChain.length !== 1 || item.relationshipChain[0] !== 'affects')) issues.push(`${label}: direct causal evidence requires one explicit affects assertion.`);
  if (item.derivationMethod === 'direct-semantic-assertion' && item.hopCount !== 1) issues.push(`${label}: direct derivation must be one hop.`);
  if (item.derivationMethod === 'bounded-graph-propagation' && item.hopCount < 2) issues.push(`${label}: propagated derivation must be multi-hop.`);
  if (!item.blastRadius || !['low', 'medium', 'high', 'critical'].includes(item.blastRadius.rating)) issues.push(`${label}: blast radius is required.`);
  if (!Array.isArray(item.evidence) || item.evidence.length < 1) issues.push(`${label}: evidence is required.`);
  if (item.advisory !== true) issues.push(`${label}: advisory safeguard is required.`);
}
const counts = {
  totalImpactPaths: data.impactPaths?.length || 0,
  directCausalEvidence: (data.impactPaths || []).filter(item => item.classification === 'direct-causal-evidence').length,
  dependencyImpact: (data.impactPaths || []).filter(item => item.classification === 'dependency-impact').length,
  structuralImpact: (data.impactPaths || []).filter(item => item.classification === 'structural-impact').length,
  unresolvedHypotheses: data.unresolvedHypotheses?.length || 0
};
for (const [key, value] of Object.entries(counts)) if (data.summary?.[key] !== value) issues.push(`Summary mismatch for ${key}.`);
for (const item of data.unresolvedHypotheses || []) {
  if (item.status !== 'unresolved' || item.advisory !== true) issues.push(`${item.hypothesisId || 'hypothesis'}: unresolved advisory status required.`);
}
if (!String(data.policy?.causationRule || '').includes('never treated as proof of causation')) issues.push('Causation safeguard is missing.');
if (issues.length) {
  console.error(issues.join('\n'));
  process.exit(1);
}
console.log(`Validated ${data.impactPaths.length} causal and impact paths.`);
