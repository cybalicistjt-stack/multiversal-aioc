export const severityRank = Object.freeze({ info: 0, warning: 1, error: 2, blocking: 3 });

const normalizeList = values => [...new Set((values ?? []).filter(Boolean).map(String))].sort();
const finding = (code, severity, message, evidence = []) => ({ code, severity, message, evidence: normalizeList(evidence) });

export function certifyChange({ plan, review = {}, validation = {}, continuity, repositoryHealth } = {}) {
  const findings = [];
  if (!plan?.id) findings.push(finding('change.plan.missing', 'blocking', 'A governed change plan is required.'));
  if (continuity?.result !== 'PASS') findings.push(finding('continuity.not-certified', 'blocking', 'Continuity certification must pass before patch certification.', continuity?.evidence));
  if (repositoryHealth?.status === 'blocked' || repositoryHealth?.status === 'unknown') findings.push(finding('repository.not-executable', 'blocking', 'Repository health does not permit execution.', repositoryHealth?.evidence));

  const expectedFiles = normalizeList(plan?.files);
  const reviewedFiles = normalizeList(review.files);
  const validatedFiles = normalizeList(validation.files);
  const missingReview = expectedFiles.filter(path => !reviewedFiles.includes(path));
  const missingValidation = expectedFiles.filter(path => !validatedFiles.includes(path));
  if (missingReview.length) findings.push(finding('review.coverage', 'blocking', `Review is missing ${missingReview.length} planned file(s).`, missingReview));
  if (missingValidation.length) findings.push(finding('validation.coverage', 'blocking', `Validation is missing ${missingValidation.length} planned file(s).`, missingValidation));

  const unresolved = (review.findings ?? []).filter(item => !['resolved', 'accepted'].includes(item.status));
  for (const item of unresolved) {
    const severity = item.severity === 'blocking' || item.severity === 'error' ? 'blocking' : 'warning';
    findings.push(finding(`review.${item.code ?? 'finding'}`, severity, item.message ?? 'Unresolved review finding.', item.evidence));
  }

  const failedChecks = (validation.checks ?? []).filter(check => check.status !== 'pass');
  for (const check of failedChecks) {
    findings.push(finding(`validation.${check.id ?? 'check'}`, check.required === false ? 'warning' : 'blocking', check.message ?? 'Validation check did not pass.', check.evidence));
  }

  if (!normalizeList(review.evidence).length) findings.push(finding('review.evidence', 'blocking', 'Review evidence is required.'));
  if (!normalizeList(validation.evidence).length) findings.push(finding('validation.evidence', 'blocking', 'Validation evidence is required.'));
  if (plan?.risk === 'high' && !normalizeList(review.approvals).length) findings.push(finding('approval.high-risk', 'blocking', 'High-risk changes require explicit approval evidence.'));

  findings.sort((a, b) => severityRank[b.severity] - severityRank[a.severity] || a.code.localeCompare(b.code));
  const blocked = findings.some(item => item.severity === 'blocking');
  const warnings = findings.some(item => item.severity === 'warning');
  return {
    schemaVersion: '1.0.0',
    changePlanId: plan?.id ?? null,
    result: blocked ? 'FAIL' : warnings ? 'PASS WITH WARNINGS' : 'PASS',
    executionAllowed: !blocked,
    files: expectedFiles,
    evidence: normalizeList([...(review.evidence ?? []), ...(validation.evidence ?? [])]),
    findings
  };
}

export function assertCertifiedChange(input) {
  const result = certifyChange(input);
  if (!result.executionAllowed) {
    const error = new Error('Change certification failed; execution is frozen.');
    error.code = 'change.certification-failed';
    error.certification = result;
    throw error;
  }
  return result;
}
