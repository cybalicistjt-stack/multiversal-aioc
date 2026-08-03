const STATUS_TRANSITIONS = Object.freeze({
  planned: new Set(['ready', 'cancelled']),
  ready: new Set(['active', 'blocked', 'cancelled']),
  active: new Set(['blocked', 'review', 'complete', 'cancelled']),
  blocked: new Set(['ready', 'active', 'cancelled']),
  review: new Set(['active', 'complete', 'blocked']),
  complete: new Set([]),
  cancelled: new Set([])
});

const clone = value => globalThis.structuredClone ? globalThis.structuredClone(value) : JSON.parse(JSON.stringify(value));
const now = () => new Date().toISOString();

async function sha256(value) {
  const text = typeof value === 'string' ? value : stableStringify(value);
  if (globalThis.crypto?.subtle) {
    const bytes = new TextEncoder().encode(text);
    const digest = await crypto.subtle.digest('SHA-256', bytes);
    return [...new Uint8Array(digest)].map(b => b.toString(16).padStart(2, '0')).join('');
  }
  let hash = 2166136261;
  for (let i = 0; i < text.length; i += 1) hash = Math.imul(hash ^ text.charCodeAt(i), 16777619);
  return `fnv1a-${(hash >>> 0).toString(16).padStart(8, '0')}`;
}

function stableStringify(value) {
  if (Array.isArray(value)) return `[${value.map(stableStringify).join(',')}]`;
  if (value && typeof value === 'object') {
    return `{${Object.keys(value).sort().map(key => `${JSON.stringify(key)}:${stableStringify(value[key])}`).join(',')}}`;
  }
  return JSON.stringify(value);
}

function assert(condition, message, code = 'state.invalid') {
  if (!condition) {
    const error = new Error(message);
    error.code = code;
    throw error;
  }
}

function uniqueById(items, label) {
  const ids = new Set();
  for (const item of items) {
    assert(item?.id, `${label} entry is missing id`, `${label}.id`);
    assert(!ids.has(item.id), `Duplicate ${label} id: ${item.id}`, `${label}.duplicate`);
    ids.add(item.id);
  }
  return ids;
}

function nextExecutableFrom(state) {
  const complete = new Set(state.workItems.filter(item => item.status === 'complete').map(item => item.id));
  return [...state.workItems]
    .filter(item => ['planned', 'ready'].includes(item.status))
    .filter(item => (item.dependsOn || []).every(id => complete.has(id)))
    .sort((a, b) => a.sequence - b.sequence)[0] || null;
}

export function validateProjectState(state) {
  const issues = [];
  const push = (severity, code, message) => issues.push({ severity, code, message });
  if (!state || typeof state !== 'object') return [{ severity: 'error', code: 'state.type', message: 'State must be an object.' }];
  if (state.schemaVersion !== '1.0.0') push('error', 'state.version', 'schemaVersion must be 1.0.0.');
  if (state.project?.id !== 'multiversal') push('error', 'project.id', 'Project id must be multiversal.');

  const repositories = Array.isArray(state.repositories) ? state.repositories : [];
  const milestones = Array.isArray(state.milestones) ? state.milestones : [];
  const workItems = Array.isArray(state.workItems) ? state.workItems : [];
  const decisions = Array.isArray(state.decisions) ? state.decisions : [];
  const handoffs = Array.isArray(state.handoffs) ? state.handoffs : [];
  const ledger = Array.isArray(state.ledger) ? state.ledger : [];

  let repositoryIds = new Set(), milestoneIds = new Set(), workItemIds = new Set();
  try { repositoryIds = uniqueById(repositories, 'repository'); } catch (error) { push('error', error.code, error.message); }
  try { milestoneIds = uniqueById(milestones, 'milestone'); } catch (error) { push('error', error.code, error.message); }
  try { workItemIds = uniqueById(workItems, 'workItem'); } catch (error) { push('error', error.code, error.message); }
  try { uniqueById(decisions, 'decision'); } catch (error) { push('error', error.code, error.message); }
  try { uniqueById(handoffs, 'handoff'); } catch (error) { push('error', error.code, error.message); }
  try { uniqueById(ledger, 'ledger'); } catch (error) { push('error', error.code, error.message); }

  for (const item of workItems) {
    if (!milestoneIds.has(item.milestoneId)) push('error', 'workItem.milestone', `${item.id} references missing milestone ${item.milestoneId}.`);
    for (const dependency of item.dependsOn || []) if (!workItemIds.has(dependency)) push('error', 'workItem.dependency', `${item.id} references missing dependency ${dependency}.`);
    if (item.status === 'complete' && !(item.evidence || []).length) push('error', 'workItem.evidence', `${item.id} is complete without evidence.`);
  }

  const active = state.active || {};
  if (!repositoryIds.has(active.repositoryId)) push('error', 'active.repository', 'Active repository does not exist.');
  if (!milestoneIds.has(active.milestoneId)) push('error', 'active.milestone', 'Active milestone does not exist.');
  if (!workItemIds.has(active.workItemId)) push('error', 'active.workItem', 'Active work item does not exist.');
  const activeItems = workItems.filter(item => item.status === 'active');
  if (activeItems.length !== 1) push('error', 'active.count', `Exactly one active work item is required; found ${activeItems.length}.`);
  if (activeItems[0] && activeItems[0].id !== active.workItemId) push('error', 'active.pointer', 'Active work item pointer does not match the active record.');

  for (const milestone of milestones) {
    const children = workItems.filter(item => item.milestoneId === milestone.id);
    if (milestone.status === 'complete' && children.some(item => !['complete', 'cancelled'].includes(item.status))) {
      push('error', 'milestone.incomplete-child', `${milestone.id} is complete while child work remains.`);
    }
  }

  return issues;
}

export class ProjectStateEngine {
  constructor({ initialState, actor = 'system', persist = null } = {}) {
    assert(initialState, 'initialState is required', 'state.required');
    this.state = clone(initialState);
    this.actor = actor;
    this.persist = persist;
    this.listeners = new Set();
    this.assertValid();
  }

  snapshot() { return clone(this.state); }
  subscribe(listener) { this.listeners.add(listener); return () => this.listeners.delete(listener); }
  emit(event) { for (const listener of this.listeners) listener(clone(event)); }
  assertValid() {
    const errors = validateProjectState(this.state).filter(issue => issue.severity === 'error');
    assert(!errors.length, errors.map(issue => `${issue.code}: ${issue.message}`).join('\n'), 'state.validation');
  }

  getWorkItem(id) { return this.state.workItems.find(item => item.id === id) || null; }
  getMilestone(id) { return this.state.milestones.find(item => item.id === id) || null; }
  getNextExecutableWorkItem() { return nextExecutableFrom(this.state); }

  async mutate({ operation, entityType, entityId, reason, evidence = [], apply }) {
    const before = this.snapshot();
    const beforeHash = await sha256(before);
    const draft = this.snapshot();
    const result = apply(draft);
    draft.project.updatedAt = now();
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
    this.state = draft;
    try {
      this.assertValid();
      if (this.persist) await this.persist(this.snapshot());
    } catch (error) {
      this.state = before;
      throw error;
    }
    const event = { operation, entityType, entityId, at: this.state.project.updatedAt, result: clone(result) };
    this.emit(event);
    return clone(result);
  }

  async transitionWorkItem(id, nextStatus, { reason, evidence = [], blocker = null } = {}) {
    const item = this.getWorkItem(id);
    assert(item, `Unknown work item ${id}`, 'workItem.missing');
    assert(STATUS_TRANSITIONS[item.status]?.has(nextStatus), `Invalid transition ${item.status} -> ${nextStatus}`, 'workItem.transition');
    if (nextStatus === 'complete') assert(evidence.length > 0, 'Completion requires evidence.', 'workItem.completion-evidence');
    if (nextStatus === 'active') {
      const unmet = (item.dependsOn || []).filter(dep => this.getWorkItem(dep)?.status !== 'complete');
      assert(!unmet.length, `Unmet dependencies: ${unmet.join(', ')}`, 'workItem.dependencies');
    }
    return this.mutate({
      operation: 'transition', entityType: 'workItem', entityId: id, reason, evidence,
      apply: draft => {
        const target = draft.workItems.find(entry => entry.id === id);
        if (nextStatus === 'active') {
          for (const other of draft.workItems) if (other.status === 'active' && other.id !== id) other.status = 'review';
          draft.active.workItemId = id;
          draft.active.milestoneId = target.milestoneId;
        }
        target.status = nextStatus;
        target.blocker = nextStatus === 'blocked' ? blocker || 'Unspecified blocker' : null;
        if (evidence.length) target.evidence = [...new Set([...(target.evidence || []), ...evidence])];
        if (nextStatus === 'complete') {
          const next = nextExecutableFrom(draft);
          assert(next, 'Completing this item would leave no active work item. Add or activate the next governed work item first.', 'workItem.no-successor');
          next.status = 'active';
          next.blocker = null;
          draft.active.workItemId = next.id;
          draft.active.milestoneId = next.milestoneId;
        }
        return target;
      }
    });
  }

  async recordDecision(decision, { reason = 'Record project decision', evidence = [] } = {}) {
    assert(decision?.id && decision?.title, 'Decision id and title are required.', 'decision.required');
    assert(!this.state.decisions.some(item => item.id === decision.id), `Decision ${decision.id} already exists.`, 'decision.duplicate');
    return this.mutate({
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
    return this.mutate({
      operation: 'create', entityType: 'handoff', entityId: id, reason: 'Create session handoff', evidence,
      apply: draft => {
        const handoff = { id, createdAt: now(), workItemId, summary, nextAction, evidence: [...evidence] };
        draft.handoffs.push(handoff);
        return handoff;
      }
    });
  }

  async reconcile(candidate, { reason = 'Reconcile canonical project state', evidence = [] } = {}) {
    const candidateErrors = validateProjectState(candidate).filter(issue => issue.severity === 'error');
    assert(!candidateErrors.length, candidateErrors.map(issue => issue.message).join('\n'), 'reconcile.invalid');
    return this.mutate({
      operation: 'reconcile', entityType: 'state', entityId: 'canonical', reason, evidence,
      apply: draft => {
        const preservedLedger = draft.ledger;
        Object.keys(draft).forEach(key => delete draft[key]);
        Object.assign(draft, clone(candidate));
        draft.ledger = [...preservedLedger, ...(candidate.ledger || [])];
        return { active: draft.active, workItems: draft.workItems.length };
      }
    });
  }
}

export { stableStringify, sha256, STATUS_TRANSITIONS };
