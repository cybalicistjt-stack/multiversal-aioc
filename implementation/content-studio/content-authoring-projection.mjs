import crypto from 'node:crypto';

const REQUIRED_PROVENANCE_FIELDS = ['sourceId', 'sourceType', 'sourceVersion'];
const BLOCKING_SEVERITIES = new Set(['error', 'critical']);

function stable(value) {
  if (Array.isArray(value)) return value.map(stable);
  if (value && typeof value === 'object') {
    return Object.fromEntries(Object.keys(value).sort().map((key) => [key, stable(value[key])]));
  }
  return value;
}

function fingerprint(value) {
  return crypto.createHash('sha256').update(JSON.stringify(stable(value))).digest('hex');
}

function normalizeStrings(values = []) {
  return [...new Set(values.filter((value) => typeof value === 'string' && value.trim()).map((value) => value.trim()))].sort();
}

function normalizeEntity(entity = {}) {
  return {
    id: String(entity.id ?? '').trim(),
    type: String(entity.type ?? '').trim(),
    name: String(entity.name ?? '').trim(),
    schemaVersion: String(entity.schemaVersion ?? '').trim(),
    payload: stable(entity.payload ?? {}),
    tags: normalizeStrings(entity.tags),
    dependencies: normalizeStrings(entity.dependencies),
    provenance: stable(entity.provenance ?? {}),
  };
}

function finding(code, severity, message, evidence = []) {
  return { code, severity, message, evidence: normalizeStrings(evidence) };
}

export function projectContentDraft(input = {}) {
  const entity = normalizeEntity(input.entity);
  const findings = [];
  const canonical = input.canonical ?? {};
  const validation = input.validation ?? {};
  const repositoryHealth = input.repositoryHealth ?? {};
  const continuity = input.continuity ?? {};

  if (!entity.id) findings.push(finding('CONTENT_ID_MISSING', 'error', 'Content entity requires a stable identifier.'));
  if (!entity.type) findings.push(finding('CONTENT_TYPE_MISSING', 'error', 'Content entity requires a governed type.'));
  if (!entity.name) findings.push(finding('CONTENT_NAME_MISSING', 'error', 'Content entity requires a display name.'));
  if (!entity.schemaVersion) findings.push(finding('SCHEMA_VERSION_MISSING', 'error', 'Content entity requires a schema version.'));

  if (continuity.result !== 'PASS') {
    findings.push(finding('CONTINUITY_NOT_CERTIFIED', 'critical', 'Content authoring is blocked until continuity certification passes.', continuity.evidence));
  }
  if (repositoryHealth.status === 'blocked' || repositoryHealth.status === 'unknown') {
    findings.push(finding('REPOSITORY_HEALTH_BLOCKING', 'critical', `Repository health is ${repositoryHealth.status ?? 'unknown'}.`, repositoryHealth.evidence));
  }
  if (canonical.repositoryId && input.repositoryId !== canonical.repositoryId) {
    findings.push(finding('REPOSITORY_BINDING_DRIFT', 'critical', 'Content draft targets a non-canonical repository.'));
  }
  if (canonical.branch && input.branch !== canonical.branch) {
    findings.push(finding('BRANCH_BINDING_DRIFT', 'error', 'Content draft targets a non-canonical branch.'));
  }
  if (canonical.workItemId && input.workItemId !== canonical.workItemId) {
    findings.push(finding('WORK_ITEM_BINDING_DRIFT', 'error', 'Content draft is not bound to the active work item.'));
  }

  for (const field of REQUIRED_PROVENANCE_FIELDS) {
    if (!entity.provenance[field]) {
      findings.push(finding('PROVENANCE_FIELD_MISSING', 'error', `Provenance field ${field} is required.`));
    }
  }

  const knownDependencies = new Set(normalizeStrings(input.knownEntityIds));
  for (const dependency of entity.dependencies) {
    if (!knownDependencies.has(dependency)) {
      findings.push(finding('DEPENDENCY_UNRESOLVED', 'error', `Dependency ${dependency} is unresolved.`));
    }
  }

  for (const issue of validation.issues ?? []) {
    const severity = String(issue.severity ?? 'warning').toLowerCase();
    findings.push(finding(issue.code ?? 'VALIDATION_ISSUE', severity, issue.message ?? 'Validation issue.', issue.evidence));
  }

  if (validation.schemaValid === false) {
    findings.push(finding('SCHEMA_VALIDATION_FAILED', 'critical', 'Entity payload failed schema validation.', validation.evidence));
  }
  if (validation.duplicateId === true) {
    findings.push(finding('DUPLICATE_STABLE_ID', 'critical', `Stable identifier ${entity.id} already exists.`, validation.evidence));
  }

  const blockers = findings.filter((item) => BLOCKING_SEVERITIES.has(item.severity));
  const warnings = findings.filter((item) => item.severity === 'warning');
  const mode = blockers.length ? 'recovery' : 'authoring';
  const result = blockers.length ? 'FAIL' : warnings.length ? 'PASS WITH WARNINGS' : 'PASS';

  const provenanceRecord = {
    entityId: entity.id,
    sourceId: entity.provenance.sourceId ?? null,
    sourceType: entity.provenance.sourceType ?? null,
    sourceVersion: entity.provenance.sourceVersion ?? null,
    locator: entity.provenance.locator ?? null,
    transformation: entity.provenance.transformation ?? 'direct-authoring',
    evidence: normalizeStrings(entity.provenance.evidence),
  };

  const projection = {
    schemaVersion: '1.0.0',
    result,
    mode,
    executionAllowed: blockers.length === 0,
    binding: {
      repositoryId: input.repositoryId ?? null,
      branch: input.branch ?? null,
      milestoneId: input.milestoneId ?? null,
      workItemId: input.workItemId ?? null,
    },
    entity,
    provenanceRecord,
    findings: findings.sort((a, b) => `${a.severity}:${a.code}`.localeCompare(`${b.severity}:${b.code}`)),
    authoringPlan: blockers.length ? [] : [
      { sequence: 10, operation: 'validate-schema', entityId: entity.id },
      { sequence: 20, operation: 'resolve-dependencies', entityId: entity.id },
      { sequence: 30, operation: 'record-provenance', entityId: entity.id },
      { sequence: 40, operation: 'stage-content', entityId: entity.id },
      { sequence: 50, operation: 'request-certification', entityId: entity.id },
    ],
  };

  return { ...projection, fingerprint: fingerprint(projection) };
}

export function assertAuthoringAllowed(projection) {
  if (!projection?.executionAllowed) {
    const error = new Error('Content authoring is frozen by blocking governance findings.');
    error.code = 'CONTENT_AUTHORING_FROZEN';
    error.findings = projection?.findings ?? [];
    throw error;
  }
  return true;
}
