const clone = value => globalThis.structuredClone ? globalThis.structuredClone(value) : JSON.parse(JSON.stringify(value));

function assert(condition, message, code = 'continuity.invalid') {
  if (!condition) {
    const error = new Error(message);
    error.code = code;
    throw error;
  }
}

function stableStringify(value) {
  if (Array.isArray(value)) return `[${value.map(stableStringify).join(',')}]`;
  if (value && typeof value === 'object') {
    return `{${Object.keys(value).sort().map(key => `${JSON.stringify(key)}:${stableStringify(value[key])}`).join(',')}}`;
  }
  return JSON.stringify(value);
}

async function digest(value) {
  const text = typeof value === 'string' ? value : stableStringify(value);
  if (globalThis.crypto?.subtle) {
    const bytes = new TextEncoder().encode(text);
    const hash = await crypto.subtle.digest('SHA-256', bytes);
    return [...new Uint8Array(hash)].map(byte => byte.toString(16).padStart(2, '0')).join('');
  }
  let hash = 2166136261;
  for (let i = 0; i < text.length; i += 1) hash = Math.imul(hash ^ text.charCodeAt(i), 16777619);
  return `fnv1a-${(hash >>> 0).toString(16).padStart(8, '0')}`;
}

function normalizeEvidence(values = []) {
  return [...new Set(values.filter(Boolean))].sort();
}

function latestHandoff(state) {
  return [...(state.handoffs || [])]
    .filter(item => item.workItemId === state.active?.workItemId)
    .sort((a, b) => String(b.createdAt).localeCompare(String(a.createdAt)))[0] || null;
}

function collectBlockingFindings({ health, recovery }) {
  const findings = [];
  for (const repository of health?.repositories || []) {
    for (const finding of repository.findings || []) {
      if (finding.severity === 'blocking' || finding.blocking === true) findings.push(clone(finding));
    }
  }
  for (const finding of recovery?.findings || []) {
    if (finding.severity === 'blocking' || finding.blocking === true) findings.push(clone(finding));
  }
  return findings.sort((a, b) => `${a.code}:${a.repositoryId || ''}`.localeCompare(`${b.code}:${b.repositoryId || ''}`));
}

export class ContinuitySnapshotService {
  constructor({ clock = () => new Date().toISOString(), maxAgeMs = 15 * 60 * 1000 } = {}) {
    this.clock = clock;
    this.maxAgeMs = maxAgeMs;
  }

  async create({ state, health, recovery = null, capabilityEvidence = [], repositoryEvidence = [] }) {
    assert(state?.active, 'Canonical active state is required.', 'continuity.state');
    const activeWorkItem = (state.workItems || []).find(item => item.id === state.active.workItemId);
    const activeMilestone = (state.milestones || []).find(item => item.id === state.active.milestoneId);
    const activeRepository = (state.repositories || []).find(item => item.id === state.active.repositoryId);
    assert(activeWorkItem, 'Active work item is missing.', 'continuity.work-item');
    assert(activeMilestone, 'Active milestone is missing.', 'continuity.milestone');
    assert(activeRepository, 'Active repository is missing.', 'continuity.repository');

    const createdAt = this.clock();
    const blockers = collectBlockingFindings({ health, recovery });
    const handoff = latestHandoff(state);
    const evidence = normalizeEvidence([
      ...(activeWorkItem.evidence || []),
      ...(activeMilestone.evidence || []),
      ...capabilityEvidence,
      ...repositoryEvidence,
      ...(handoff?.evidence || [])
    ]);

    const payload = {
      schemaVersion: '1.0.0',
      projectId: state.project.id,
      createdAt,
      expiresAt: new Date(new Date(createdAt).getTime() + this.maxAgeMs).toISOString(),
      executionAllowed: blockers.length === 0,
      orientation: {
        repository: { id: activeRepository.id, fullName: activeRepository.fullName, branch: state.active.branch },
        milestone: { id: activeMilestone.id, title: activeMilestone.title },
        workItem: { id: activeWorkItem.id, title: activeWorkItem.title, status: activeWorkItem.status },
        nextAction: handoff?.nextAction || `Execute ${activeWorkItem.id} according to canonical state.`
      },
      health: {
        overall: health?.overall || 'unknown',
        generatedAt: health?.generatedAt || null
      },
      blockers,
      recoveryRequired: blockers.length > 0 || Boolean(recovery?.required),
      evidence
    };
    return Object.freeze({ ...payload, fingerprint: await digest(payload) });
  }

  async validate(snapshot, { now = this.clock(), expectedState = null } = {}) {
    const findings = [];
    const add = (severity, code, message) => findings.push({ severity, code, message });
    if (!snapshot || snapshot.schemaVersion !== '1.0.0') add('blocking', 'snapshot.version', 'Snapshot schema is missing or unsupported.');
    if (!snapshot?.fingerprint) add('blocking', 'snapshot.fingerprint.missing', 'Snapshot fingerprint is missing.');
    if (snapshot?.fingerprint) {
      const unsigned = clone(snapshot);
      delete unsigned.fingerprint;
      if (await digest(unsigned) !== snapshot.fingerprint) add('blocking', 'snapshot.fingerprint.invalid', 'Snapshot fingerprint does not match its contents.');
    }
    if (!snapshot?.createdAt || !snapshot?.expiresAt) add('blocking', 'snapshot.time.missing', 'Snapshot timestamps are incomplete.');
    if (snapshot?.expiresAt && new Date(now).getTime() > new Date(snapshot.expiresAt).getTime()) add('blocking', 'snapshot.stale', 'Snapshot has expired.');
    if (snapshot?.recoveryRequired || snapshot?.blockers?.length) add('blocking', 'snapshot.recovery-required', 'Snapshot contains blocking recovery findings.');
    if (expectedState) {
      if (snapshot?.orientation?.workItem?.id !== expectedState.active?.workItemId) add('blocking', 'snapshot.work-item-drift', 'Snapshot work item conflicts with canonical state.');
      if (snapshot?.orientation?.repository?.id !== expectedState.active?.repositoryId) add('blocking', 'snapshot.repository-drift', 'Snapshot repository conflicts with canonical state.');
      if (snapshot?.orientation?.repository?.branch !== expectedState.active?.branch) add('blocking', 'snapshot.branch-drift', 'Snapshot branch conflicts with canonical state.');
    }
    return { valid: findings.every(item => item.severity !== 'blocking'), findings };
  }

  async restore(snapshot, options = {}) {
    const validation = await this.validate(snapshot, options);
    if (!validation.valid) {
      return {
        status: 'recovery-required',
        executionAllowed: false,
        findings: validation.findings,
        nextAction: 'Freeze writes, reload canonical state and repository observations, then issue a fresh continuity snapshot.'
      };
    }
    return {
      status: 'ready',
      executionAllowed: true,
      orientation: clone(snapshot.orientation),
      evidence: clone(snapshot.evidence),
      fingerprint: snapshot.fingerprint
    };
  }
}

export { stableStringify, digest, collectBlockingFindings };
