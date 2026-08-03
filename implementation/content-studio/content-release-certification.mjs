import crypto from 'node:crypto';

const stable = value => JSON.stringify(value, Object.keys(value ?? {}).sort());
const fingerprint = value => crypto.createHash('sha256').update(stable(value)).digest('hex');

function finding(code, severity, message, evidence = []) {
  return { code, severity, message, evidence: [...new Set(evidence)].sort() };
}

export function certifyContentRelease(input) {
  const findings = [];
  const canonical = input?.canonical ?? {};
  const release = input?.release ?? {};
  const pack = input?.pack ?? {};
  const installation = input?.installation ?? {};
  const rollback = input?.rollback ?? {};

  if (input?.continuity?.status !== 'PASS') findings.push(finding('CONTINUITY_NOT_CERTIFIED', 'blocking', 'Continuity certification must pass.', input?.continuity?.evidence));
  if (!['healthy', 'degraded'].includes(input?.repositoryHealth?.status)) findings.push(finding('REPOSITORY_HEALTH_BLOCKING', 'blocking', 'Repository health does not permit release.', input?.repositoryHealth?.evidence));
  if (release.repository !== canonical.repository) findings.push(finding('REPOSITORY_DRIFT', 'blocking', 'Release repository differs from canonical repository.'));
  if (release.branch !== canonical.branch) findings.push(finding('BRANCH_DRIFT', 'blocking', 'Release branch differs from canonical branch.'));
  if (release.workItemId !== canonical.workItemId) findings.push(finding('WORK_ITEM_DRIFT', 'blocking', 'Release is not bound to the active work item.'));

  if (input?.packCertification?.status !== 'PASS') findings.push(finding('PACK_NOT_CERTIFIED', 'blocking', 'Pack certification must pass before release.', input?.packCertification?.evidence));
  if (!pack.id || !pack.version || !pack.filename?.endsWith('.pack')) findings.push(finding('INVALID_PACK_IDENTITY', 'blocking', 'Pack id, semantic version, and .pack filename are required.'));
  if (!release.releaseId || !release.channel || !release.createdAt) findings.push(finding('RELEASE_METADATA_MISSING', 'blocking', 'Release id, channel, and creation timestamp are required.'));
  if (!Array.isArray(release.artifacts) || release.artifacts.length === 0) findings.push(finding('RELEASE_ARTIFACTS_MISSING', 'blocking', 'At least one release artifact is required.'));
  if (!release.checksum || release.checksum.length < 32) findings.push(finding('CHECKSUM_MISSING', 'blocking', 'A release checksum is required.'));
  if (!Array.isArray(release.provenance) || release.provenance.length === 0) findings.push(finding('RELEASE_PROVENANCE_MISSING', 'blocking', 'Release provenance evidence is required.'));

  const requiredInstallStages = ['preflight', 'install', 'activate', 'verify'];
  for (const stage of requiredInstallStages) {
    const result = installation?.stages?.[stage];
    if (result?.status !== 'PASS' || !result?.evidence?.length) findings.push(finding(`INSTALL_${stage.toUpperCase()}_FAILED`, 'blocking', `Installation stage ${stage} must pass with evidence.`, result?.evidence));
  }

  if (installation.cleanEnvironment !== true) findings.push(finding('CLEAN_INSTALL_NOT_PROVEN', 'blocking', 'A clean-environment installation must be proven.'));
  if (installation.upgradeTest?.status !== 'PASS') findings.push(finding('UPGRADE_PATH_NOT_CERTIFIED', 'blocking', 'Upgrade-path installation must pass.', installation.upgradeTest?.evidence));
  if (installation.dependencyResolution?.status !== 'PASS') findings.push(finding('DEPENDENCY_INSTALL_FAILED', 'blocking', 'Runtime dependency resolution must pass.', installation.dependencyResolution?.evidence));

  if (rollback.uninstall?.status !== 'PASS') findings.push(finding('UNINSTALL_NOT_CERTIFIED', 'blocking', 'Uninstallation must pass.', rollback.uninstall?.evidence));
  if (rollback.restore?.status !== 'PASS') findings.push(finding('RESTORE_NOT_CERTIFIED', 'blocking', 'Rollback restoration must pass.', rollback.restore?.evidence));
  if (rollback.dataIntegrity?.status !== 'PASS') findings.push(finding('ROLLBACK_DATA_INTEGRITY_FAILED', 'blocking', 'Rollback data integrity must pass.', rollback.dataIntegrity?.evidence));

  const approvals = release.approvals ?? [];
  if (!approvals.some(a => a.role === 'owner' && a.status === 'approved' && a.evidence?.length)) findings.push(finding('OWNER_APPROVAL_MISSING', 'blocking', 'Owner approval with evidence is required.'));
  if (release.channel === 'stable' && !approvals.some(a => a.role === 'release' && a.status === 'approved' && a.evidence?.length)) findings.push(finding('STABLE_RELEASE_APPROVAL_MISSING', 'blocking', 'Stable releases require release approval.'));

  for (const warning of release.warnings ?? []) findings.push(finding(warning.code ?? 'RELEASE_WARNING', 'warning', warning.message ?? 'Release warning.', warning.evidence));

  const blocking = findings.filter(x => x.severity === 'blocking');
  const warnings = findings.filter(x => x.severity === 'warning');
  const status = blocking.length ? 'FAIL' : warnings.length ? 'PASS WITH WARNINGS' : 'PASS';
  const result = {
    schemaVersion: '1.0.0',
    certificationId: `content-release:${release.releaseId ?? 'unknown'}`,
    status,
    executionAllowed: status !== 'FAIL',
    completionAllowed: status === 'PASS',
    release: {
      id: release.releaseId ?? null,
      channel: release.channel ?? null,
      packId: pack.id ?? null,
      version: pack.version ?? null,
      filename: pack.filename ?? null,
      checksum: release.checksum ?? null
    },
    installation: {
      cleanEnvironment: installation.cleanEnvironment === true,
      stages: requiredInstallStages.map(stage => ({ stage, status: installation?.stages?.[stage]?.status ?? 'MISSING' })),
      upgrade: installation.upgradeTest?.status ?? 'MISSING',
      dependencies: installation.dependencyResolution?.status ?? 'MISSING'
    },
    rollback: {
      uninstall: rollback.uninstall?.status ?? 'MISSING',
      restore: rollback.restore?.status ?? 'MISSING',
      dataIntegrity: rollback.dataIntegrity?.status ?? 'MISSING'
    },
    findings: findings.sort((a, b) => a.code.localeCompare(b.code)),
    evidence: [...new Set([
      ...(input?.continuity?.evidence ?? []),
      ...(input?.repositoryHealth?.evidence ?? []),
      ...(input?.packCertification?.evidence ?? []),
      ...(release.provenance ?? []),
      ...approvals.flatMap(a => a.evidence ?? [])
    ])].sort()
  };
  result.fingerprint = fingerprint(result);
  return result;
}

export function assertContentReleaseCertified(result) {
  if (result?.status !== 'PASS' || result?.completionAllowed !== true) {
    throw new Error('Content release certification failed; release completion is frozen.');
  }
  return true;
}
