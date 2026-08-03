const clone = value => globalThis.structuredClone ? globalThis.structuredClone(value) : JSON.parse(JSON.stringify(value));
const now = () => new Date().toISOString();

function invariant(condition, message, code = 'orchestration.invalid') {
  if (!condition) {
    const error = new Error(message);
    error.code = code;
    throw error;
  }
}

function compareJobs(a, b) {
  return (b.priority - a.priority) || (a.sequence - b.sequence) || a.id.localeCompare(b.id);
}

export class GovernedOrchestrationService {
  constructor({ canonicalState, certification, capabilityEvidence = [], persist = null, actor = 'system' } = {}) {
    invariant(canonicalState, 'canonicalState is required', 'state.required');
    this.state = clone(canonicalState);
    this.certification = clone(certification || { result: 'FAIL', executionAllowed: false });
    this.capabilityEvidence = clone(capabilityEvidence);
    this.persist = persist;
    this.actor = actor;
    this.queue = [];
    this.dispatchLedger = [];
    this.leases = new Map();
  }

  executionAllowed() {
    return this.certification?.executionAllowed === true && this.certification?.result !== 'FAIL';
  }

  enqueue({ id, workItemId, agentRole, operation, priority = 50, sequence = 0, requires = [], evidence = [] }) {
    invariant(this.executionAllowed(), 'Continuity certification blocks orchestration.', 'orchestration.frozen');
    invariant(id && workItemId && agentRole && operation, 'Queue item fields are required.', 'queue.required');
    invariant(!this.queue.some(item => item.id === id), `Duplicate queue item ${id}`, 'queue.duplicate');
    const workItem = this.state.workItems.find(item => item.id === workItemId);
    invariant(workItem, `Unknown work item ${workItemId}`, 'queue.work-item');
    invariant(workItem.status === 'active', `Work item ${workItemId} is not active`, 'queue.not-active');
    const missing = requires.filter(required => !this.capabilityEvidence.some(item => item.capability === required && item.available === true));
    invariant(missing.length === 0, `Missing capabilities: ${missing.join(', ')}`, 'queue.capability');
    const record = { id, workItemId, agentRole, operation, priority, sequence, requires: [...requires], evidence: [...evidence], status: 'queued', queuedAt: now(), attempts: 0 };
    this.queue.push(record);
    this.queue.sort(compareJobs);
    return clone(record);
  }

  nextDispatchable() {
    if (!this.executionAllowed()) return null;
    return clone(this.queue.find(item => item.status === 'queued') || null);
  }

  async dispatchNext({ workerId, leaseSeconds = 900 } = {}) {
    invariant(workerId, 'workerId is required', 'dispatch.worker');
    invariant(this.executionAllowed(), 'Continuity certification blocks dispatch.', 'orchestration.frozen');
    const job = this.queue.find(item => item.status === 'queued');
    if (!job) return null;
    const before = clone({ queue: this.queue, ledger: this.dispatchLedger });
    const lease = { workerId, acquiredAt: now(), expiresAt: new Date(Date.now() + leaseSeconds * 1000).toISOString() };
    job.status = 'dispatched';
    job.attempts += 1;
    job.dispatchedAt = lease.acquiredAt;
    this.leases.set(job.id, lease);
    const event = { id: `dispatch-${job.id}-${job.attempts}`, at: lease.acquiredAt, actor: this.actor, operation: 'dispatch', queueItemId: job.id, workItemId: job.workItemId, workerId, evidence: [...job.evidence] };
    this.dispatchLedger.push(event);
    try {
      if (this.persist) await this.persist(this.snapshot());
    } catch (error) {
      this.queue = before.queue;
      this.dispatchLedger = before.ledger;
      this.leases.delete(job.id);
      throw error;
    }
    return { job: clone(job), lease: clone(lease), event: clone(event) };
  }

  async acknowledge(queueItemId, { workerId, outcome, evidence = [], error = null } = {}) {
    invariant(['complete', 'failed', 'blocked'].includes(outcome), 'Invalid dispatch outcome', 'dispatch.outcome');
    const job = this.queue.find(item => item.id === queueItemId);
    invariant(job, `Unknown queue item ${queueItemId}`, 'queue.missing');
    const lease = this.leases.get(queueItemId);
    invariant(lease?.workerId === workerId, 'Worker does not own this lease', 'dispatch.lease');
    invariant(evidence.length > 0 || outcome !== 'complete', 'Completion requires evidence', 'dispatch.evidence');
    job.status = outcome;
    job.completedAt = now();
    job.resultEvidence = [...evidence];
    job.error = error;
    this.leases.delete(queueItemId);
    const event = { id: `ack-${job.id}-${job.attempts}`, at: job.completedAt, actor: this.actor, operation: 'acknowledge', queueItemId: job.id, workItemId: job.workItemId, workerId, outcome, evidence: [...evidence], error };
    this.dispatchLedger.push(event);
    if (this.persist) await this.persist(this.snapshot());
    return clone(event);
  }

  reclaimExpired(at = new Date()) {
    const reclaimed = [];
    for (const [jobId, lease] of this.leases.entries()) {
      if (new Date(lease.expiresAt) <= at) {
        const job = this.queue.find(item => item.id === jobId);
        if (job?.status === 'dispatched') {
          job.status = 'queued';
          job.dispatchedAt = null;
          reclaimed.push(jobId);
        }
        this.leases.delete(jobId);
      }
    }
    this.queue.sort(compareJobs);
    return reclaimed;
  }

  snapshot() {
    return clone({ queue: this.queue, dispatchLedger: this.dispatchLedger, leases: [...this.leases.entries()].map(([id, lease]) => ({ id, ...lease })) });
  }
}

export { compareJobs };