import { createHash } from 'node:crypto';

const REQUIRED_BINDINGS = ['repository','branch','milestoneId','workItemId'];
const REQUIRED_SCENARIO_FIELDS = ['id','title','kind','expectedOutcome'];

function stable(value) {
  if (Array.isArray(value)) return value.map(stable);
  if (value && typeof value === 'object') {
    return Object.fromEntries(Object.keys(value).sort().map((key) => [key, stable(value[key])]));
  }
  return value;
}

export function fingerprint(value) {
  return createHash('sha256').update(JSON.stringify(stable(value))).digest('hex');
}

export function normalizeScenario(raw = {}) {
  return {
    id: String(raw.id ?? '').trim(),
    title: String(raw.title ?? '').trim(),
    kind: String(raw.kind ?? '').trim().toLowerCase(),
    expectedOutcome: String(raw.expectedOutcome ?? '').trim(),
    dependencies: [...new Set((raw.dependencies ?? []).map(String))].sort(),
    fixtures: [...new Set((raw.fixtures ?? []).map(String))].sort(),
    tags: [...new Set((raw.tags ?? []).map(String))].sort(),
    risk: String(raw.risk ?? 'normal').toLowerCase(),
  };
}

export function projectTestHarness(input = {}) {
  const findings = [];
  const canonical = input.canonical ?? {};
  const request = input.request ?? {};
  const continuity = input.continuity ?? {};
  const repositoryHealth = input.repositoryHealth ?? {};

  if (continuity.certified !== true) findings.push({code:'CONTINUITY_NOT_CERTIFIED', severity:'blocking'});
  if (repositoryHealth.status === 'blocked' || repositoryHealth.status === 'unknown') {
    findings.push({code:'REPOSITORY_HEALTH_BLOCKING', severity:'blocking'});
  }

  for (const field of REQUIRED_BINDINGS) {
    if (!request[field] || request[field] !== canonical[field]) {
      findings.push({code:`CANONICAL_${field.toUpperCase()}_MISMATCH`, severity:'blocking'});
    }
  }

  const scenarios = (request.scenarios ?? []).map(normalizeScenario);
  if (!scenarios.length) findings.push({code:'NO_SCENARIOS', severity:'blocking'});

  const seen = new Set();
  for (const scenario of scenarios) {
    for (const field of REQUIRED_SCENARIO_FIELDS) {
      if (!scenario[field]) findings.push({code:`SCENARIO_${field.toUpperCase()}_MISSING`, severity:'blocking', scenarioId:scenario.id || null});
    }
    if (seen.has(scenario.id)) findings.push({code:'DUPLICATE_SCENARIO_ID', severity:'blocking', scenarioId:scenario.id});
    seen.add(scenario.id);
    if (scenario.risk === 'high' && !(request.approvals ?? []).some((a) => a.scope === scenario.id && a.approved === true && a.evidence)) {
      findings.push({code:'HIGH_RISK_SCENARIO_APPROVAL_MISSING', severity:'blocking', scenarioId:scenario.id});
    }
    for (const dependency of scenario.dependencies) {
      if (!(request.availableDependencies ?? []).includes(dependency)) {
        findings.push({code:'SCENARIO_DEPENDENCY_MISSING', severity:'blocking', scenarioId:scenario.id, dependency});
      }
    }
  }

  const requiredKinds = new Set(request.requiredKinds ?? []);
  const actualKinds = new Set(scenarios.map((s) => s.kind));
  for (const kind of requiredKinds) {
    if (!actualKinds.has(kind)) findings.push({code:'REQUIRED_SCENARIO_KIND_MISSING', severity:'blocking', kind});
  }

  if (!(request.evidenceSinks ?? []).length) findings.push({code:'EVIDENCE_SINK_MISSING', severity:'blocking'});
  if (!(request.runnerCapabilities ?? []).includes('execute-tests')) findings.push({code:'RUNNER_CAPABILITY_MISSING', severity:'blocking'});

  const blocking = findings.filter((f) => f.severity === 'blocking');
  const warnings = findings.filter((f) => f.severity === 'warning');
  const status = blocking.length ? 'FAIL' : warnings.length ? 'PASS WITH WARNINGS' : 'PASS';
  const plan = blocking.length ? [] : scenarios.map((scenario, index) => ({
    sequence:index + 1,
    scenarioId:scenario.id,
    action:'execute-scenario',
    expectedOutcome:scenario.expectedOutcome,
    evidenceRequired:true,
  }));

  const projection = {
    schemaVersion:'1.0.0',
    status,
    executionAllowed:blocking.length === 0,
    canonicalBindings:{
      repository:request.repository,
      branch:request.branch,
      milestoneId:request.milestoneId,
      workItemId:request.workItemId,
    },
    scenarioCount:scenarios.length,
    scenarios,
    plan,
    findings,
    requiredEvidence:[...new Set(['runner-log','scenario-result','assertion-summary',...(request.evidenceSinks ?? [])])].sort(),
  };
  return {...projection, fingerprint:fingerprint(projection)};
}

export function assertExecutableProjection(projection) {
  if (!projection?.executionAllowed || projection.status === 'FAIL') {
    throw new Error('Test harness execution is frozen by governed findings.');
  }
  return projection;
}
