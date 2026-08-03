import assert from 'node:assert/strict';
import { analyzeSimulationBalance } from './simulation-balance-impact-analysis.mjs';

const base = () => ({
  continuity: { certification: 'PASS', evidence: ['continuity://pass'] },
  repository: { fullName: 'cybalicistjt-stack/multiversal-aioc', branch: 'governance/session-bootstrap-v1', health: 'healthy', evidence: ['repo://healthy'] },
  canonical: { repository: 'cybalicistjt-stack/multiversal-aioc', branch: 'governance/session-bootstrap-v1', workItemId: 'AIOC-I-006B' },
  baselines: [{ id: 'base-1', version: '1.0.0', metrics: { damage: 10 }, evidence: ['baseline://1'] }],
  simulations: [
    { id: 'sim-combat', kind: 'combat', baselineId: 'base-1', iterations: 1000, metrics: ['damage'], runnerCapabilities: ['deterministic-seed'], evidenceSink: { durable: true }, changeIds: ['chg-1'] },
    { id: 'sim-progression', kind: 'progression', baselineId: 'base-1', iterations: 1000, metrics: ['xp'], runnerCapabilities: ['deterministic-seed'], evidenceSink: { durable: true }, changeIds: [] },
    { id: 'sim-economy', kind: 'economy', baselineId: 'base-1', iterations: 1000, metrics: ['cost'], runnerCapabilities: ['deterministic-seed'], evidenceSink: { durable: true }, changeIds: [] },
    { id: 'sim-content', kind: 'content-impact', baselineId: 'base-1', iterations: 1000, metrics: ['coverage'], runnerCapabilities: ['deterministic-seed'], evidenceSink: { durable: true }, changeIds: ['chg-1'] },
  ],
  changes: [{ id: 'chg-1', scope: ['combat', 'content'], expectedEffects: ['damage adjustment'], risk: 'low' }],
  results: [
    { simulationId: 'sim-combat', evidence: ['result://combat'], metrics: [{ id: 'damage', delta: 0.05, threshold: 0.1 }] },
    { simulationId: 'sim-progression', evidence: ['result://progression'], metrics: [] },
    { simulationId: 'sim-economy', evidence: ['result://economy'], metrics: [] },
    { simulationId: 'sim-content', evidence: ['result://content'], metrics: [] },
  ],
});

const tests = [];
const test = (name, fn) => tests.push([name, fn]);

test('valid simulation matrix passes', () => assert.equal(analyzeSimulationBalance(base()).status, 'PASS'));
test('continuity failure blocks execution', () => { const x = base(); x.continuity.certification = 'FAIL'; assert.equal(analyzeSimulationBalance(x).executionFrozen, true); });
test('repository mismatch fails', () => { const x = base(); x.repository.fullName = 'wrong/repo'; assert.equal(analyzeSimulationBalance(x).status, 'FAIL'); });
test('branch mismatch fails', () => { const x = base(); x.repository.branch = 'main'; assert.equal(analyzeSimulationBalance(x).status, 'FAIL'); });
test('wrong active work item fails', () => { const x = base(); x.canonical.workItemId = 'AIOC-I-006A'; assert.equal(analyzeSimulationBalance(x).status, 'FAIL'); });
test('duplicate baseline fails', () => { const x = base(); x.baselines.push({ ...x.baselines[0] }); assert.equal(analyzeSimulationBalance(x).status, 'FAIL'); });
test('missing baseline evidence fails', () => { const x = base(); x.baselines[0].evidence = []; assert.equal(analyzeSimulationBalance(x).status, 'FAIL'); });
test('duplicate simulation id fails', () => { const x = base(); x.simulations.push({ ...x.simulations[0] }); assert.equal(analyzeSimulationBalance(x).status, 'FAIL'); });
test('missing required kind fails', () => { const x = base(); x.simulations = x.simulations.filter(s => s.kind !== 'economy'); assert.equal(analyzeSimulationBalance(x).status, 'FAIL'); });
test('missing referenced baseline fails', () => { const x = base(); x.simulations[0].baselineId = 'missing'; assert.equal(analyzeSimulationBalance(x).status, 'FAIL'); });
test('low sample produces warning', () => { const x = base(); x.simulations[0].iterations = 20; assert.equal(analyzeSimulationBalance(x).status, 'PASS WITH WARNINGS'); });
test('non deterministic runner fails', () => { const x = base(); x.simulations[0].runnerCapabilities = []; assert.equal(analyzeSimulationBalance(x).status, 'FAIL'); });
test('non durable sink fails', () => { const x = base(); x.simulations[0].evidenceSink.durable = false; assert.equal(analyzeSimulationBalance(x).status, 'FAIL'); });
test('high risk change requires approval', () => { const x = base(); x.changes[0].risk = 'high'; assert.equal(analyzeSimulationBalance(x).status, 'FAIL'); });
test('high risk change with evidence passes', () => { const x = base(); x.changes[0].risk = 'high'; x.changes[0].approval = { actor: 'owner', evidence: ['approval://1'] }; assert.equal(analyzeSimulationBalance(x).status, 'PASS'); });
test('blocking metric threshold fails', () => { const x = base(); x.results[0].metrics[0].delta = 0.2; assert.equal(analyzeSimulationBalance(x).status, 'FAIL'); });
test('nonblocking metric threshold warns', () => { const x = base(); x.results[0].metrics[0] = { id: 'damage', delta: 0.2, threshold: 0.1, blocking: false }; assert.equal(analyzeSimulationBalance(x).status, 'PASS WITH WARNINGS'); });
test('result evidence is required', () => { const x = base(); x.results[0].evidence = []; assert.equal(analyzeSimulationBalance(x).status, 'FAIL'); });
test('impact matrix maps changes deterministically', () => { const r = analyzeSimulationBalance(base()); assert.deepEqual(r.impactMatrix[0].simulationIds, ['sim-combat', 'sim-content']); });
test('fingerprint is deterministic', () => { const a = analyzeSimulationBalance(base()); const b = analyzeSimulationBalance(base()); assert.equal(a.fingerprint, b.fingerprint); });

let passed = 0;
for (const [name, fn] of tests) {
  try { fn(); passed += 1; console.log(`PASS ${name}`); }
  catch (error) { console.error(`FAIL ${name}`); console.error(error); }
}
console.log(`RESULT ${passed}/${tests.length} passed`);
if (passed !== tests.length) process.exit(1);
