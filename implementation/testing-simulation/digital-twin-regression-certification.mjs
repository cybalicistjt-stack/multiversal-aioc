import crypto from 'node:crypto';

const stable = value => {
  if (Array.isArray(value)) return value.map(stable);
  if (value && typeof value === 'object') return Object.fromEntries(Object.keys(value).sort().map(k => [k, stable(value[k])]));
  return value;
};

export const fingerprint = value => crypto.createHash('sha256').update(JSON.stringify(stable(value))).digest('hex');

const finding = (severity, code, message, evidence = []) => ({ severity, code, message, evidence: [...evidence].sort() });

export function certifyDigitalTwin(input) {
  const findings = [];
  const canonical = input?.canonical ?? {};
  const twin = input?.twin ?? {};
  const regressions = Array.isArray(input?.regressions) ? input.regressions : [];
  const tests = Array.isArray(input?.tests) ? input.tests : [];

  if (input?.continuity?.result !== 'PASS') findings.push(finding('error', 'continuity.blocked', 'Continuity certification must pass.'));
  if (!['healthy', 'pass'].includes(String(input?.repositoryHealth?.status ?? '').toLowerCase())) findings.push(finding('error', 'repository.unhealthy', 'Repository health must be healthy.'));
  for (const key of ['repository', 'branch', 'milestoneId', 'workItemId']) {
    if (!canonical[key]) findings.push(finding('error', `canonical.${key}.missing`, `Canonical ${key} is required.`));
  }
  if (canonical.workItemId !== 'AIOC-I-006C') findings.push(finding('error', 'canonical.workItem.mismatch', 'Active work item must be AIOC-I-006C.'));

  if (!twin.id) findings.push(finding('error', 'twin.id.missing', 'Digital twin ID is required.'));
  if (!twin.baselineFingerprint) findings.push(finding('error', 'twin.baseline.missing', 'Evidence-backed baseline fingerprint is required.'));
  if (!twin.modelVersion) findings.push(finding('error', 'twin.version.missing', 'Digital twin model version is required.'));
  if (!Array.isArray(twin.domains) || twin.domains.length === 0) findings.push(finding('error', 'twin.domains.missing', 'At least one modeled domain is required.'));
  if (!Array.isArray(twin.evidence) || twin.evidence.length === 0) findings.push(finding('error', 'twin.evidence.missing', 'Digital twin evidence is required.'));

  const requiredDomains = ['combat', 'progression', 'economy', 'content'];
  for (const domain of requiredDomains) {
    if (!(twin.domains ?? []).includes(domain)) findings.push(finding('error', `twin.domain.${domain}.missing`, `Digital twin must cover ${domain}.`));
  }

  const regressionIds = new Set();
  for (const regression of regressions) {
    if (!regression.id) findings.push(finding('error', 'regression.id.missing', 'Regression ID is required.'));
    else if (regressionIds.has(regression.id)) findings.push(finding('error', 'regression.id.duplicate', `Duplicate regression ID: ${regression.id}.`));
    else regressionIds.add(regression.id);
    if (!regression.sourceEvidence?.length) findings.push(finding('error', 'regression.evidence.missing', `Regression ${regression.id ?? '<unknown>'} lacks source evidence.`));
    if (regression.status === 'open' && regression.severity === 'critical') findings.push(finding('error', 'regression.critical.open', `Critical regression ${regression.id} remains open.`, regression.sourceEvidence));
    else if (regression.status === 'open') findings.push(finding('warning', 'regression.open', `Regression ${regression.id} remains open.`, regression.sourceEvidence));
  }

  const testIds = new Set();
  for (const test of tests) {
    if (!test.id) findings.push(finding('error', 'test.id.missing', 'Test ID is required.'));
    else if (testIds.has(test.id)) findings.push(finding('error', 'test.id.duplicate', `Duplicate test ID: ${test.id}.`));
    else testIds.add(test.id);
    if (!test.evidence?.length) findings.push(finding('error', 'test.evidence.missing', `Test ${test.id ?? '<unknown>'} lacks durable evidence.`));
    if (test.result === 'fail') findings.push(finding(test.required === false ? 'warning' : 'error', 'test.failed', `Test ${test.id} failed.`, test.evidence));
  }

  const covered = new Set(tests.filter(t => t.result === 'pass').flatMap(t => t.domains ?? []));
  for (const domain of requiredDomains) {
    if (!covered.has(domain)) findings.push(finding('error', `test.coverage.${domain}.missing`, `Passing test coverage is required for ${domain}.`));
  }

  if (!input?.runner?.capabilities?.includes('digital-twin')) findings.push(finding('error', 'runner.capability.missing', 'Runner must provide digital-twin capability.'));
  if (!input?.runner?.capabilities?.includes('regression-mining')) findings.push(finding('error', 'runner.regressionMining.missing', 'Runner must provide regression-mining capability.'));
  if (!input?.evidenceSink?.durable) findings.push(finding('error', 'evidenceSink.notDurable', 'A durable evidence sink is required.'));

  const errors = findings.filter(f => f.severity === 'error');
  const warnings = findings.filter(f => f.severity === 'warning');
  const result = errors.length ? 'FAIL' : warnings.length ? 'PASS WITH WARNINGS' : 'PASS';
  const orderedFindings = findings.sort((a, b) => `${a.severity}:${a.code}:${a.message}`.localeCompare(`${b.severity}:${b.code}:${b.message}`));
  const certification = {
    schemaVersion: '1.0.0',
    workItemId: canonical.workItemId ?? null,
    result,
    executionAllowed: result === 'PASS',
    completionAllowed: result === 'PASS',
    findings: orderedFindings,
    regressionSummary: {
      total: regressions.length,
      open: regressions.filter(r => r.status === 'open').length,
      criticalOpen: regressions.filter(r => r.status === 'open' && r.severity === 'critical').length
    },
    testSummary: {
      total: tests.length,
      passed: tests.filter(t => t.result === 'pass').length,
      failed: tests.filter(t => t.result === 'fail').length,
      coveredDomains: [...covered].sort()
    },
    nextAction: result === 'PASS' ? 'Complete AIOC-I-006 and advance to the next canonical milestone.' : 'Freeze completion and resolve all blocking digital-twin or regression findings.'
  };
  return { ...certification, fingerprint: fingerprint(certification) };
}
