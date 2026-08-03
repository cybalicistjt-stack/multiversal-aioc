const blocking = (code, message, evidence = []) => ({ code, severity: 'blocking', message, evidence });
const warning = (code, message, evidence = []) => ({ code, severity: 'warning', message, evidence });

export function certifyWorkbenchExecution(input) {
  const findings = [];
  const {
    continuityCertification,
    changeCertification,
    execution,
    canonical,
    handoff,
    requiredEvidence = []
  } = input ?? {};

  if (!continuityCertification || continuityCertification.result === 'FAIL') {
    findings.push(blocking('CONTINUITY_NOT_CERTIFIED', 'Continuity certification must permit execution.'));
  }
  if (!changeCertification || changeCertification.result === 'FAIL') {
    findings.push(blocking('CHANGE_NOT_CERTIFIED', 'The change must pass change certification before execution.'));
  }
  if (!execution) {
    findings.push(blocking('EXECUTION_MISSING', 'Execution result is required.'));
  } else {
    if (execution.repositoryId !== canonical?.repositoryId) findings.push(blocking('REPOSITORY_DRIFT', 'Execution repository does not match canonical state.'));
    if (execution.branch !== canonical?.branch) findings.push(blocking('BRANCH_DRIFT', 'Execution branch does not match canonical state.'));
    if (execution.workItemId !== canonical?.workItemId) findings.push(blocking('WORK_ITEM_DRIFT', 'Execution work item does not match canonical state.'));
    if (!execution.commitSha) findings.push(blocking('COMMIT_EVIDENCE_MISSING', 'Execution must identify the resulting commit.'));
    if (!Array.isArray(execution.changedFiles) || execution.changedFiles.length === 0) findings.push(blocking('CHANGED_FILES_MISSING', 'Execution must identify changed files.'));
    if (!Array.isArray(execution.validationEvidence) || execution.validationEvidence.length === 0) findings.push(blocking('VALIDATION_EVIDENCE_MISSING', 'Execution must include validation evidence.'));
    if (execution.status === 'failed' && !execution.failureEvidence?.length) findings.push(blocking('FAILURE_EVIDENCE_MISSING', 'Failed execution requires failure evidence.'));
    if (execution.status === 'partial') findings.push(warning('PARTIAL_EXECUTION', 'Execution is partial and must not be marked complete.'));
  }

  for (const evidence of requiredEvidence) {
    const available = new Set([...(execution?.validationEvidence ?? []), ...(execution?.evidence ?? [])]);
    if (!available.has(evidence)) findings.push(blocking('REQUIRED_EVIDENCE_MISSING', `Required evidence is missing: ${evidence}`));
  }

  if (!handoff) {
    findings.push(blocking('HANDOFF_MISSING', 'A governed handoff is required.'));
  } else {
    if (handoff.repositoryId !== canonical?.repositoryId) findings.push(blocking('HANDOFF_REPOSITORY_DRIFT', 'Handoff repository does not match canonical state.'));
    if (handoff.branch !== canonical?.branch) findings.push(blocking('HANDOFF_BRANCH_DRIFT', 'Handoff branch does not match canonical state.'));
    if (handoff.completedWorkItemId !== canonical?.workItemId) findings.push(blocking('HANDOFF_WORK_ITEM_DRIFT', 'Handoff completion does not match the active work item.'));
    if (!handoff.nextAction) findings.push(blocking('NEXT_ACTION_MISSING', 'Handoff must identify the next executable action.'));
    if (!Array.isArray(handoff.evidence) || handoff.evidence.length === 0) findings.push(blocking('HANDOFF_EVIDENCE_MISSING', 'Handoff must include evidence.'));
  }

  const blockingFindings = findings.filter(f => f.severity === 'blocking');
  const result = blockingFindings.length ? 'FAIL' : findings.length ? 'PASS WITH WARNINGS' : 'PASS';
  return {
    result,
    executionAllowed: result !== 'FAIL',
    completionAllowed: result === 'PASS' && execution?.status === 'success',
    findings,
    evidence: [...new Set([...(execution?.evidence ?? []), ...(execution?.validationEvidence ?? []), ...(handoff?.evidence ?? [])])]
  };
}

export function assertWorkbenchExecutionCertified(certification) {
  if (!certification || certification.result === 'FAIL') {
    const error = new Error('Developer Workbench execution certification failed; completion is frozen.');
    error.code = 'WORKBENCH_EXECUTION_CERTIFICATION_FAILED';
    throw error;
  }
  return certification;
}
