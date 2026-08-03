import { createHash } from 'node:crypto';

const stable = value => JSON.stringify(value, Object.keys(value ?? {}).sort());
const fingerprint = value => createHash('sha256').update(stable(value)).digest('hex');
const finding = (code, severity, message, evidence = []) => ({ code, severity, message, evidence });

export function certifyContentPack(input) {
  const findings = [];
  const canonical = input?.canonical ?? {};
  const conversion = input?.conversion ?? {};
  const pack = input?.pack ?? {};
  const available = new Set(input?.availableDependencies ?? []);
  const entities = Array.isArray(pack.entities) ? pack.entities : [];
  const dependencies = [...new Set(pack.dependencies ?? [])].sort();

  if (input?.continuityCertification?.result !== 'PASS') {
    findings.push(finding('CONTINUITY_NOT_CERTIFIED', 'blocking', 'Continuity certification must PASS.', input?.continuityCertification?.evidence));
  }
  if (!['healthy', 'degraded'].includes(input?.repositoryHealth?.status)) {
    findings.push(finding('REPOSITORY_NOT_EXECUTABLE', 'blocking', 'Repository health does not permit pack execution.', input?.repositoryHealth?.evidence));
  }
  for (const field of ['repository', 'branch', 'milestoneId', 'workItemId']) {
    if (!canonical[field] || pack[field] !== canonical[field]) {
      findings.push(finding(`CANONICAL_${field.toUpperCase()}_MISMATCH`, 'blocking', `Pack ${field} must match canonical state.`));
    }
  }
  if (!conversion.sourceFormat || !conversion.targetFormat || !conversion.converterVersion) {
    findings.push(finding('CONVERSION_CONTRACT_INCOMPLETE', 'blocking', 'Conversion requires source format, target format, and converter version.'));
  }
  if (conversion.result !== 'PASS') {
    findings.push(finding('CONVERSION_FAILED', 'blocking', 'Content conversion must PASS before assembly.', conversion.evidence));
  }
  if (!pack.id || !pack.version || pack.extension !== '.pack') {
    findings.push(finding('PACK_IDENTITY_INVALID', 'blocking', 'Pack requires id, version, and .pack extension.'));
  }
  if (!pack.manifest || !Array.isArray(pack.manifest.entities)) {
    findings.push(finding('MANIFEST_MISSING', 'blocking', 'Pack manifest with entity references is required.'));
  }

  const ids = entities.map(entity => entity?.id).filter(Boolean);
  if (ids.length !== entities.length || new Set(ids).size !== ids.length) {
    findings.push(finding('ENTITY_IDS_INVALID', 'blocking', 'Every entity must have a unique stable ID.'));
  }
  const manifestIds = new Set(pack.manifest?.entities ?? []);
  for (const id of ids) {
    if (!manifestIds.has(id)) findings.push(finding('MANIFEST_ENTITY_MISSING', 'blocking', `Manifest omits entity ${id}.`));
  }
  for (const id of manifestIds) {
    if (!ids.includes(id)) findings.push(finding('MANIFEST_ENTITY_ORPHAN', 'blocking', `Manifest references missing entity ${id}.`));
  }
  for (const dependency of dependencies) {
    if (!available.has(dependency)) findings.push(finding('DEPENDENCY_UNRESOLVED', 'blocking', `Dependency ${dependency} is unavailable.`));
  }
  if (!Array.isArray(pack.provenance) || pack.provenance.length === 0) {
    findings.push(finding('PACK_PROVENANCE_MISSING', 'blocking', 'Pack-level provenance evidence is required.'));
  }
  if (pack.installTest?.result !== 'PASS') {
    findings.push(finding('INSTALL_TEST_FAILED', 'blocking', 'Pack installation test must PASS.', pack.installTest?.evidence));
  }
  if (pack.uninstallTest?.result !== 'PASS') {
    findings.push(finding('UNINSTALL_TEST_FAILED', 'blocking', 'Pack uninstall test must PASS.', pack.uninstallTest?.evidence));
  }
  if (pack.warnings?.length) {
    for (const warning of pack.warnings) findings.push(finding('PACK_WARNING', 'warning', warning));
  }

  const blocking = findings.filter(item => item.severity === 'blocking');
  const warnings = findings.filter(item => item.severity === 'warning');
  const result = blocking.length ? 'FAIL' : warnings.length ? 'PASS WITH WARNINGS' : 'PASS';
  const assembly = {
    packId: pack.id ?? null,
    version: pack.version ?? null,
    extension: pack.extension ?? null,
    entityIds: [...ids].sort(),
    dependencies,
    manifestFingerprint: fingerprint(pack.manifest ?? {}),
    contentFingerprint: fingerprint(entities),
    stages: ['convert', 'normalize', 'assemble', 'install-test', 'uninstall-test', 'certify']
  };

  return {
    schemaVersion: '1.0.0',
    result,
    executionAllowed: result !== 'FAIL',
    completionAllowed: result !== 'FAIL',
    assembly,
    findings,
    evidence: [...new Set([...(conversion.evidence ?? []), ...(pack.provenance ?? []), ...(pack.installTest?.evidence ?? []), ...(pack.uninstallTest?.evidence ?? [])])],
    certificationFingerprint: fingerprint({ result, assembly, findings })
  };
}

export function assertContentPackCertified(certification) {
  if (!certification || certification.result === 'FAIL' || !certification.completionAllowed) {
    throw new Error('Content pack is not certified; completion is frozen.');
  }
  return certification;
}
