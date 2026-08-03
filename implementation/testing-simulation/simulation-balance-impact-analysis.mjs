import crypto from 'node:crypto';

const stable = value => {
  if (Array.isArray(value)) return value.map(stable);
  if (value && typeof value === 'object') {
    return Object.fromEntries(Object.keys(value).sort().map(key => [key, stable(value[key])]));
  }
  return value;
};

const fingerprint = value => crypto.createHash('sha256').update(JSON.stringify(stable(value))).digest('hex');
const finding = (severity, code, message, evidence = []) => ({ severity, code, message, evidence: [...evidence].sort() });

export function analyzeSimulationBalance(input) {
  const findings = [];
  const continuity = input?.continuity ?? {};
  const repository = input?.repository ?? {};
  const canonical = input?.canonical ?? {};
  const simulations = [...(input?.simulations ?? [])];
  const baselines = [...(input?.baselines ?? [])];
  const changes = [...(input?.changes ?? [])];

  if (continuity.certification !== 'PASS') findings.push(finding('error', 'continuity.blocked', 'Continuity certification must PASS.', continuity.evidence));
  if (!['healthy', 'degraded'].includes(repository.health)) findings.push(finding('error', 'repository.blocked', 'Repository health must be healthy or degraded.', repository.evidence));
  if (repository.fullName !== canonical.repository) findings.push(finding('error', 'canonical.repository', 'Repository does not match canonical state.'));
  if (repository.branch !== canonical.branch) findings.push(finding('error', 'canonical.branch', 'Branch does not match canonical state.'));
  if (canonical.workItemId !== 'AIOC-I-006B') findings.push(finding('error', 'canonical.work-item', 'AIOC-I-006B must be the active work item.'));

  const baselineIds = new Set();
  for (const baseline of baselines) {
    if (!baseline.id || !baseline.version || !baseline.metrics || !Object.keys(baseline.metrics).length) {
      findings.push(finding('error', 'baseline.invalid', 'Every baseline requires id, version, and metrics.'));
      continue;
    }
    if (baselineIds.has(baseline.id)) findings.push(finding('error', 'baseline.duplicate', `Duplicate baseline ${baseline.id}.`));
    baselineIds.add(baseline.id);
    if (!(baseline.evidence?.length > 0)) findings.push(finding('error', 'baseline.evidence', `Baseline ${baseline.id} requires evidence.`));
  }

  const simulationIds = new Set();
  const requiredKinds = new Set(['combat', 'progression', 'economy', 'content-impact']);
  for (const simulation of simulations) {
    if (!simulation.id || !simulation.kind || !simulation.baselineId || !simulation.iterations || !simulation.metrics?.length) {
      findings.push(finding('error', 'simulation.invalid', 'Every simulation requires id, kind, baselineId, iterations, and metrics.'));
      continue;
    }
    if (simulationIds.has(simulation.id)) findings.push(finding('error', 'simulation.duplicate', `Duplicate simulation ${simulation.id}.`));
    simulationIds.add(simulation.id);
    requiredKinds.delete(simulation.kind);
    if (!baselineIds.has(simulation.baselineId)) findings.push(finding('error', 'simulation.baseline-missing', `Simulation ${simulation.id} references missing baseline ${simulation.baselineId}.`));
    if (simulation.iterations < 100) findings.push(finding('warning', 'simulation.low-sample', `Simulation ${simulation.id} uses fewer than 100 iterations.`));
    if (!(simulation.runnerCapabilities ?? []).includes('deterministic-seed')) findings.push(finding('error', 'simulation.non-deterministic', `Simulation ${simulation.id} lacks deterministic-seed capability.`));
    if (!(simulation.evidenceSink?.durable)) findings.push(finding('error', 'simulation.evidence-sink', `Simulation ${simulation.id} requires a durable evidence sink.`));
  }
  for (const kind of [...requiredKinds].sort()) findings.push(finding('error', 'coverage.missing-kind', `Missing required simulation kind: ${kind}.`));

  const changeIds = new Set();
  for (const change of changes) {
    if (!change.id || !change.scope?.length || !change.expectedEffects?.length) {
      findings.push(finding('error', 'change.invalid', 'Every proposed change requires id, scope, and expectedEffects.'));
      continue;
    }
    if (changeIds.has(change.id)) findings.push(finding('error', 'change.duplicate', `Duplicate change ${change.id}.`));
    changeIds.add(change.id);
    if (change.risk === 'high' && !(change.approval?.actor && change.approval?.evidence?.length)) {
      findings.push(finding('error', 'change.high-risk-approval', `High-risk change ${change.id} requires approval evidence.`));
    }
  }

  for (const result of input?.results ?? []) {
    if (!simulationIds.has(result.simulationId)) findings.push(finding('error', 'result.unknown-simulation', `Result references unknown simulation ${result.simulationId}.`));
    if (!(result.evidence?.length > 0)) findings.push(finding('error', 'result.evidence', `Result for ${result.simulationId} requires evidence.`));
    for (const metric of result.metrics ?? []) {
      if (typeof metric.delta !== 'number' || typeof metric.threshold !== 'number') findings.push(finding('error', 'metric.invalid', `Metric ${metric.id ?? 'unknown'} requires numeric delta and threshold.`));
      else if (Math.abs(metric.delta) > metric.threshold) findings.push(finding(metric.blocking === false ? 'warning' : 'error', 'metric.threshold-exceeded', `Metric ${metric.id} exceeded its governed threshold.`));
    }
  }

  const errors = findings.filter(item => item.severity === 'error');
  const warnings = findings.filter(item => item.severity === 'warning');
  const status = errors.length ? 'FAIL' : warnings.length ? 'PASS WITH WARNINGS' : 'PASS';
  const orderedSimulations = simulations
    .map(item => ({ ...item, fingerprint: fingerprint(item) }))
    .sort((a, b) => a.kind.localeCompare(b.kind) || a.id.localeCompare(b.id));

  const impactMatrix = changes.map(change => ({
    changeId: change.id,
    scope: [...(change.scope ?? [])].sort(),
    simulationIds: orderedSimulations.filter(sim => (sim.changeIds ?? []).includes(change.id)).map(sim => sim.id),
    expectedEffects: [...(change.expectedEffects ?? [])].sort(),
  })).sort((a, b) => a.changeId.localeCompare(b.changeId));

  return {
    schemaVersion: '1.0.0',
    workItemId: 'AIOC-I-006B',
    status,
    executionFrozen: status === 'FAIL',
    findings: findings.sort((a, b) => a.code.localeCompare(b.code) || a.message.localeCompare(b.message)),
    plan: status === 'FAIL' ? [] : [
      'lock-baselines-and-seeds',
      'execute-simulation-matrix',
      'compare-governed-metrics',
      'project-cross-domain-change-impact',
      'publish-balance-and-impact-evidence',
    ],
    simulations: orderedSimulations,
    impactMatrix,
    summary: {
      baselineCount: baselines.length,
      simulationCount: simulations.length,
      changeCount: changes.length,
      errorCount: errors.length,
      warningCount: warnings.length,
    },
    fingerprint: fingerprint({ canonical, repository, simulations: orderedSimulations, baselines, changes, findings }),
  };
}

export { fingerprint };
