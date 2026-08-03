const STATUS_TRANSITIONS = Object.freeze({
  planned: new Set(['ready', 'cancelled']),
  ready: new Set(['active', 'blocked', 'cancelled']),
  active: new Set(['blocked', 'review', 'complete', 'cancelled']),
  blocked: new Set(['ready', 'active', 'cancelled']),
  review: new Set(['active', 'complete', 'blocked']),
  complete: new Set(),
  cancelled: new Set()
});

const clone = value => globalThis.structuredClone ? globalThis.structuredClone(value) : JSON.parse(JSON.stringify(value));
const now = () => new Date().toISOString();

function assert(condition, message, code = 'state.invalid') {
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

async function sha256(value) {
  const text = typeof value === 'string' ? value : stableStringify(value);
  if (globalThis.crypto?.subtle) {
    const digest = await crypto.subtle.digest('SHA-256', new TextEncoder().encode(text));
    return [...new Uint8Array(digest)].map(byte => byte.toString(16).padStart(2, '0')).join('');
  }
  let hash = 2166136261;
  for (let index = 0; index < text.length; index += 1) hash = Math.imul(hash ^ text.charCodeAt(index), 16777619);
  return `fnv1a-${(hash >>> 0).toString(16).padStart(8, '0')}`;
}

function uniqueIds(items, label, issues) {
  const ids = new Set();
  for (const item of items) {
    if (!item?.id) issues.push({ severity: 'error', code: `${label}.id`, message: `${label} entry is missing id.` });
    else if (ids.has(item.id)) issues.push({ severity: 'error', code: `${label}.duplicate`, message: `Duplicate ${label} id: ${item.id}.` });
    else ids.add(item.id);
  }
  return ids;
}

function nextExecutableFrom(state, excludedIds = new Set()) {
  const complete = new Set(state.workItems.filter(item => item.status === 'complete').map(item => item.id));
  return [...state.workItems]
    .filter(item => !excludedIds.has(item.id))
    .filter(item => ['planned', 'ready'].includes(item.status))
    .filter(item => (item.dependsOn || []).every(id => complete.has(id)))
    .sort((left, right) => left.sequence - right.sequence || left.id.localeCompare(right.id))[0] || null;
}

export function validateProjectState(state) {
  const issues = [];
  const push = (code, message) => issues.push({ severity: 'error', code, message });
  if (!state || typeof state !== 'object') return [{ severity: 'error', code: 'state.type', message: 'State must be an object.' }];
  if (state.schemaVersion !== '1.0.0') push('state.version', 'schemaVersion must be 1.0.0.');
  if (state.project?.id !== 'multiversal') push('project.id', 'Project id must be multiversal.');

  const repositories = Array.isArray(state.repositories) ? state.repositories : [];
  const milestones = Array.isArray(state.milestones) ? state.milestones : [];
  const workItems = Array.isArray(state.workItems) ? state.workItems : [];
  const decisions = Array.isArray(state.decisions) ? state.decisions : [];
  const handoffs = Array.isArray(state.handoffs) ? state.handoffs : [];
  const ledger = Array.isArray(state.ledger) ? state.ledger : [];
  const repositoryIds = uniqueIds(repositories, 'repository', issues);
  const milestoneIds = uniqueIds(milestones, 'milestone', issues);
  const workItemIds = uniqueIds(workItems, 'workItem', issues);
  uniqueIds(decisions, 'decision', issues);
  uniqueIds(handoffs, 'handoff', issues);
  uniqueIds(ledger, 'ledger', issues);

  for (const item of workItems) {
    if (!milestoneIds.has(item.milestoneId)) push('workItem.milestone', `${item.id} references missing milestone ${item.milestoneId}.`);
    for (const dependency of item.dependsOn || []) if (!workItemIds.has(dependency)) push('workItem.dependency', `${item.id} references missing dependency ${dependency}.`);
    if (item.status === 'complete' && !(item.evidence || []).length) push('workItem.evidence', `${item.id} is complete without evidence.`);
  }

  const active = state.active || {};
  if (!repositoryIds.has(active.repositoryId)) push('active.repository', 'Active repository does not exist.');
  if (!milestoneIds.has(active.milestoneId)) push('active.milestone', 'Active milestone does not exist.');
  if (!workItemIds.has(active.workItemId)) push('active.workItem', 'Active work item does not exist.');
  const activeItems = workItems.filter(item => item.status === 'active');
  if (activeItems.length !== 1) push('active.count', `Exactly one active work item is required; found ${activeItems.length}.`);
  if (activeItems[0] && activeItems[0].id !== active.workItemId) push('active.pointer', 'Active work item pointer does not match the active record.');

  for (const milestone of milestones) {
    const children = workItems.filter(item => item.milestoneId === milestone.id);
    if (milestone.status === 'complete' && children.some(item => !['complete', 'cancelled'].includes(item.status))) {
      push('milestone.incomplete-child', `${milestone.id} is complete while child work remains.`);
    }
  }
  return issues;
}

function validationError(state) {
  const errors = validateProjectState(state).filter(issue => issue.severity === 'error');
  if (!errors.length) return null;
  const error = new Error(errors.map(issue => `${issue.code}: ${issue.message}`).join('\n'));
  error.code = 'state.validation';
  error.issues = errors;
  return error;
}

export class ProjectStateEngine {
  constructor({ initialState, actor = 'system', persist = null } = {}) {
    assert(initialState, 'initialState is required', 'state.required');
    this.state = clone(initialState);
    this.actor = actor;
    this.persist = persist;
    this.listeners = new Set();
    const error = validationError(this.state);
    if (error) throw error;
  }

  snapshot() { return clone(this.state); }
  subscribe(listener) { this.listeners.add(listener); return () => this.listeners.delete(listener); }
  emit(event) { for (const listener of this.listeners) listener(clone(event)); }
  getWorkItem(id) { return this.state.workItems.find(item => item.id === id) || null; }
  getMilestone(id) { return this.state.milestones.find(item => item.id === id) || null; }
  getNextExecutableWorkItem() { return nextExecutableFrom(this.state); }

  async transaction({ operation, entityType, entityId, reason, evidence = [], apply }) {
    assert(typeof apply === 'function', 'Transaction apply function is required.', 'transaction.apply');
    const before = this.snapshot();
    const draft = clone(before);
    const result = await apply(draft);
    draft.project.updatedAt = now();

    const error = validationError(draft);
    if (error) throw error;

    const beforeHash = await sha256(before);
    const afterHash = await sha256(draft);
    draft.ledger.push({
      id: `ledger-${Date.now()}-${draft.ledger.length + 1}`,
      at: draft.project.updatedAt,
      actor: this.actor,
      operation,
      entityType,
      entityId,
      beforeHash,
      afterHash,
      reason,
      evidence: [...evidence]
    });

    const ledgerError = validationError(draft);
    if (ledgerError) throw ledgerError;
    if (this.persist) await this.persist(clone(draft));

    this.state = draft;
    const event = { operation, entityType, entityId, at: draft.project.updatedAt, result: clone(result) };
    this.emit(event);
    return clone(result);
  }

  async completeAndAdvance(id, { reason, evidence = [] } = {}) {
    assert(evidence.length > 0, 'Completion requires evidence.', 'workItem.completion-evidence');
    return this.transaction({
      operation: 'complete-and-advance', entityType: 'workItem', entityId: id, reason, evidence,
      apply: draft => {
        const target = draft.workItems.find(item => item.id === id);
        assert(target, `Unknown work item ${id}`, 'workItem.missing');
        assert(['active', 'review'].includes(target.status), `Cannot complete work item from ${target.status}.`, 'workItem.transition');
        target.status = 'complete';
        target.blocker = null;
        target.evidence = [...new Set([...(target.evidence || []), ...evidence])];

        const next = nextExecutableFrom(draft, new Set([id]));
        assert(next, 'No dependency-ready successor exists. Add the next governed work item before completing this one.', 'workItem.no-successor');
        for (const item of draft.workItems) if (item.id !== next.id && item.status === 'active') item.status = 'review';
        next.status = 'active';
        next.blocker = null;
        draft.active.workItemId = next.id;
        draft.active.milestoneId = next.milestoneId;
        return { completed: clone(target), activated: clone(next) };
      }
    });
  }

  async transitionWorkItem(id, nextStatus, { reason, evidence = [], blocker = null } = {}) {
    if (nextStatus === 'complete') return this.completeAndAdvance(id, { reason, evidence });
    const current = this.getWorkItem(id);
    assert(current, `Unknown work item ${id}`, 'workItem.missing');
    assert(STATUS_TRANSITIONS[current.status]?.has(nextStatus), `Invalid transition ${current.status} -> ${nextStatus}`, 'workItem.transition');
    return this.transaction({
      operation: 'transition', entityType: 'workItem', entityId: id, reason, evidence,
      apply: draft => {
        const target = draft.workItems.find(item => item.id === id);
        if (nextStatus === 'active') {
          const unmet = (target.dependsOn || []).filter(dep => draft.workItems.find(item => item.id === dep)?.status !== 'complete');
          assert(!unmet.length, `Unmet dependencies: ${unmet.join(', ')}`, 'workItem.dependencies');
          for (const other of draft.workItems) if (other.id !== id && other.status === 'active') other.status = 'review';
          draft.active.workItemId = id;
          draft.active.milestoneId = target.milestoneId;
        }
        target.status = nextStatus;
        target.blocker = nextStatus === 'blocked' ? blocker || 'Unspecified blocker' : null;
        if (evidence.length) target.evidence = [...new Set([...(target.evidence || []), ...evidence])];
        return clone(target);
      }
    });
  }

  async recordDecision(decision, { reason = 'Record project decision', evidence = [] } = {}) {
    assert(decision?.id && decision?.title, 'Decision id and title are required.', 'decision.required');
    assert(!this.state.decisions.some(item => item.id === decision.id), `Decision ${decision.id} already exists.`, 'decision.duplicate');
    return this.transaction({
      operation: 'create', entityType: 'decision', entityId: decision.id, reason, evidence,
      apply: draft => {
        const record = { status: 'open', createdAt: now(), rationale: '', evidence: [], ...clone(decision) };
        draft.decisions.push(record);
        return record;
      }
    });
  }

  async createHandoff({ id, workItemId, summary, nextAction, evidence = [] }) {
    assert(id && workItemId && summary && nextAction, 'Handoff fields are required.', 'handoff.required');
    assert(this.getWorkItem(workItemId), `Unknown handoff work item ${workItemId}`, 'handoff.workItem');
    return this.transaction({
      operation: 'create', entityType: 'handoff', entityId: id, reason: 'Create session handoff', evidence,
      apply: draft => {
        const handoff = { id, createdAt: now(), workItemId, summary, nextAction, evidence: [...evidence] };
        draft.handoffs.push(handoff);
        return handoff;
      }
    });
  }

  async reconcile(candidate, { reason = 'Reconcile canonical project state', evidence = [] } = {}) {
    const candidateError = validationError(candidate);
    if (candidateError) {
      candidateError.code = 'reconcile.invalid';
      throw candidateError;
    }
    return this.transaction({
      operation: 'reconcile', entityType: 'state', entityId: 'canonical', reason, evidence,
      apply: draft => {
        const preservedLedger = draft.ledger;
        Object.keys(draft).forEach(key => delete draft[key]);
        Object.assign(draft, clone(candidate));
        draft.ledger = [...preservedLedger, ...(candidate.ledger || [])];
        return { active: clone(draft.active), workItems: draft.workItems.length };
      }
    });
  }
}

export { stableStringify, sha256, STATUS_TRANSITIONS, nextExecutableFrom };
