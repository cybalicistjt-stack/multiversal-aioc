import { stableStringify, sha256 } from '../project-state/project-state-engine.mjs';

const clone = value => globalThis.structuredClone ? globalThis.structuredClone(value) : JSON.parse(JSON.stringify(value));
const now = () => new Date().toISOString();

function assert(condition, message, code = 'repository.invalid') {
  if (!condition) { const error = new Error(message); error.code = code; throw error; }
}

export function normalizeRepositorySnapshot(input) {
  assert(input?.fullName, 'fullName is required', 'repository.fullName');
  return {
    fullName: input.fullName,
    defaultBranch: input.defaultBranch || 'main',
    visibility: input.visibility || (input.private ? 'private' : 'public'),
    permissions: {
      read: Boolean(input.permissions?.read ?? true),
      push: Boolean(input.permissions?.push),
      admin: Boolean(input.permissions?.admin)
    },
    head: input.head ? {
      sha: input.head.sha,
      message: input.head.message || '',
      committedAt: input.head.committedAt || null
    } : null,
    openPullRequests: [...(input.openPullRequests || [])].map(pr => ({
      number: pr.number,
      title: pr.title || '',
      head: pr.head || null,
      base: pr.base || null,
      draft: Boolean(pr.draft),
      updatedAt: pr.updatedAt || null
    })).sort((a,b) => a.number - b.number),
    capabilityEvidence: [...(input.capabilityEvidence || [])].sort(),
    observedAt: input.observedAt || now()
  };
}

export async function fingerprintSnapshot(snapshot) {
  const canonical = clone(snapshot);
  delete canonical.observedAt;
  return sha256(stableStringify(canonical));
}

export function compareRepositoryState(canonicalRepository, liveSnapshot) {
  const drift = [];
  if (canonicalRepository.fullName !== liveSnapshot.fullName) drift.push({severity:'error',code:'repository.identity',expected:canonicalRepository.fullName,actual:liveSnapshot.fullName});
  if (canonicalRepository.defaultBranch !== liveSnapshot.defaultBranch) drift.push({severity:'warning',code:'repository.defaultBranch',expected:canonicalRepository.defaultBranch,actual:liveSnapshot.defaultBranch});
  if (!liveSnapshot.permissions.read) drift.push({severity:'error',code:'repository.read',message:'Repository read capability is unavailable.'});
  if (canonicalRepository.canonical && !liveSnapshot.permissions.push) drift.push({severity:'warning',code:'repository.push',message:'Canonical repository is currently read-only.'});
  return drift;
}

export class RepositoryStateSynchronizer {
  constructor({ provider, persistObservation = null } = {}) {
    assert(provider?.getRepository, 'provider.getRepository is required', 'provider.required');
    this.provider = provider;
    this.persistObservation = persistObservation;
  }

  async observe(fullName) {
    const raw = await this.provider.getRepository(fullName);
    const snapshot = normalizeRepositorySnapshot(raw);
    snapshot.fingerprint = await fingerprintSnapshot(snapshot);
    return snapshot;
  }

  async synchronize(projectState, { destructive = false } = {}) {
    assert(!destructive, 'Destructive synchronization is prohibited in observation mode.', 'sync.destructive');
    const next = clone(projectState);
    next.repositoryObservations = Array.isArray(next.repositoryObservations) ? next.repositoryObservations : [];
    const results = [];
    for (const repository of next.repositories) {
      const snapshot = await this.observe(repository.fullName);
      const drift = compareRepositoryState(repository, snapshot);
      const previous = [...next.repositoryObservations].reverse().find(item => item.repositoryId === repository.id);
      const stale = previous ? previous.fingerprint !== snapshot.fingerprint : false;
      const observation = {
        id: `repo-observation-${repository.id}-${Date.now()}-${results.length + 1}`,
        repositoryId: repository.id,
        observedAt: snapshot.observedAt,
        fingerprint: snapshot.fingerprint,
        previousFingerprint: previous?.fingerprint || null,
        changed: stale,
        drift,
        snapshot
      };
      next.repositoryObservations.push(observation);
      results.push(observation);
    }
    next.project.updatedAt = now();
    if (this.persistObservation) await this.persistObservation(clone(next), clone(results));
    return { state: next, observations: results, hasBlockingDrift: results.some(r => r.drift.some(d => d.severity === 'error')) };
  }
}
