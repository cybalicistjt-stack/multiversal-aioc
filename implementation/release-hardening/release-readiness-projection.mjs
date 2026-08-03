import crypto from 'node:crypto';

const REQUIRED_DOMAINS = ['operational-core','continuity','orchestration','developer-workbench','content-studio','testing-simulation'];
const REQUIRED_SECURITY = ['secret-scan','dependency-audit','permission-review','artifact-integrity'];

function stable(value) {
  if (Array.isArray(value)) return value.map(stable);
  if (value && typeof value === 'object') return Object.fromEntries(Object.keys(value).sort().map(k => [k, stable(value[k])]));
  return value;
}

function fingerprint(value) {
  return crypto.createHash('sha256').update(JSON.stringify(stable(value))).digest('hex');
}

function finding(severity, code, message, evidence = []) {
  return { severity, code, message, evidence: [...new Set(evidence)].sort() };
}

export function projectReleaseReadiness(input) {
  const findings = [];
  const canonical = input.canonical ?? {};
  const release = input.release ?? {};
  const certifications = input.certifications ?? [];
  const securityChecks = input.securityChecks ?? [];
  const deployment = input.deployment ?? {};
  const recovery = input.recovery ?? {};

  if (canonical.repository !== input.repository) findings.push(finding('error','canonical.repository','Repository does not match canonical state.'));
  if (canonical.branch !== input.branch) findings.push(finding('error','canonical.branch','Branch does not match canonical state.'));
  if (canonical.workItem !== 'AIOC-I-007A') findings.push(finding('error','canonical.work-item','AIOC-I-007A is not the active work item.'));
  if (input.continuityStatus !== 'PASS') findings.push(finding('error','continuity.status','Continuity certification must PASS.'));
  if (!['healthy','degraded'].includes(input.repositoryHealth)) findings.push(finding('error','repository.health','Repository health blocks release readiness.'));

  for (const domain of REQUIRED_DOMAINS) {
    const cert = certifications.find(c => c.domain === domain);
    if (!cert || cert.status !== 'PASS' || !(cert.evidence?.length)) findings.push(finding('error',`certification.${domain}`,`Missing clean PASS certification for ${domain}.`, cert?.evidence));
  }

  for (const check of REQUIRED_SECURITY) {
    const result = securityChecks.find(c => c.id === check);
    if (!result || result.status !== 'PASS' || !(result.evidence?.length)) findings.push(finding('error',`security.${check}`,`Security check ${check} must PASS with evidence.`, result?.evidence));
  }

  if (!release.id) findings.push(finding('error','release.id','Release ID is required.'));
  if (!release.version) findings.push(finding('error','release.version','Release version is required.'));
  if (!(release.artifacts?.length)) findings.push(finding('error','release.artifacts','At least one release artifact is required.'));
  for (const artifact of release.artifacts ?? []) {
    if (!artifact.path || !artifact.sha256) findings.push(finding('error','release.artifact-integrity','Every artifact requires path and SHA-256.'));
  }

  for (const stage of ['preflight','deploy','verify']) {
    if (deployment[stage]?.status !== 'PASS' || !(deployment[stage]?.evidence?.length)) findings.push(finding('error',`deployment.${stage}`,`${stage} stage must PASS with evidence.`, deployment[stage]?.evidence));
  }

  if (recovery.rollback?.status !== 'PASS' || !(recovery.rollback?.evidence?.length)) findings.push(finding('error','recovery.rollback','Rollback must PASS with evidence.', recovery.rollback?.evidence));
  if (recovery.restore?.status !== 'PASS' || !(recovery.restore?.evidence?.length)) findings.push(finding('error','recovery.restore','Restore must PASS with evidence.', recovery.restore?.evidence));
  if (release.channel === 'stable' && !(release.approvals ?? []).some(a => a.role === 'owner' && a.status === 'approved' && a.evidence?.length)) findings.push(finding('error','approval.owner','Stable release requires evidence-backed owner approval.'));

  const errors = findings.filter(f => f.severity === 'error');
  const warnings = findings.filter(f => f.severity === 'warning');
  const status = errors.length ? 'FAIL' : warnings.length ? 'PASS WITH WARNINGS' : 'PASS';
  const executionFrozen = status !== 'PASS';
  const plan = executionFrozen ? [] : [
    'Lock certified source commit and artifact checksums',
    'Deploy through governed preflight and release stages',
    'Verify runtime health and canonical continuity',
    'Archive release, security, deployment, and recovery evidence',
    'Authorize milestone completion only after clean certification'
  ];

  const projection = { schemaVersion:'1.0.0', workItem:'AIOC-I-007A', status, executionFrozen, findings: findings.sort((a,b)=>a.code.localeCompare(b.code)), plan, release:{ id:release.id ?? null, version:release.version ?? null, channel:release.channel ?? null } };
  return { ...projection, fingerprint: fingerprint(projection) };
}
