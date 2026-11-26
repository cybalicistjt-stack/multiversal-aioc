export const ARI10_SCHEMA_VERSION = "1.0.0" as const;

export type Ari10RawSourceMetadata = Readonly<Record<string, string>>;
export type Ari10CandidateStatus = "staged" | "accepted" | "rejected" | "committed" | "failed";
export type Ari10TransactionPhase = "staged" | "inspected" | "decided" | "cancelled" | "completed";
export type Ari10Decision = "accept" | "reject";

export interface Ari10BatchCandidateInput {
  readonly resourceId: string;
  readonly sourceRef: string;
  readonly rawSourceMetadata?: Ari10RawSourceMetadata;
}

export interface Ari10BatchCandidate extends Ari10BatchCandidateInput {
  readonly rawSourceMetadata: Ari10RawSourceMetadata;
  readonly status: Ari10CandidateStatus;
}

export interface Ari10BatchCursor {
  readonly transactionId: string;
  readonly nextCandidateIndex: number;
}

export interface Ari10BatchFailure {
  readonly resourceId: string;
  readonly reason: "commit-failed";
}

export interface Ari10BatchTransaction {
  readonly transactionId: string;
  readonly phase: Ari10TransactionPhase;
  readonly candidates: readonly Ari10BatchCandidate[];
  readonly cursor: Ari10BatchCursor | null;
  readonly committedResourceIds: readonly string[];
  readonly failures: readonly Ari10BatchFailure[];
  readonly findings: readonly string[];
  readonly cancelled: boolean;
  readonly sourceInputsMutated: false;
  readonly rightsGranted: false;
  readonly canonGranted: false;
  readonly ownershipGranted: false;
  readonly providerEntitlementGranted: false;
}

export interface Ari10StageRequest {
  readonly transactionId: string;
  readonly candidates: readonly Ari10BatchCandidateInput[];
}

export interface Ari10CandidateDecision {
  readonly resourceId: string;
  readonly decision: Ari10Decision;
}

export interface Ari10CommitOptions {
  readonly maxCandidates?: number;
  readonly failResourceIds?: readonly string[];
}

function cloneCandidate(candidate: Ari10BatchCandidateInput): Ari10BatchCandidate {
  return {
    ...candidate,
    rawSourceMetadata: { ...(candidate.rawSourceMetadata ?? {}) },
    status: "staged",
  };
}

function deriveCommittedResourceIds(candidates: readonly Ari10BatchCandidate[]): readonly string[] {
  return candidates.filter(candidate => candidate.status === "committed").map(candidate => candidate.resourceId);
}

function deriveFailures(candidates: readonly Ari10BatchCandidate[]): readonly Ari10BatchFailure[] {
  return candidates
    .filter(candidate => candidate.status === "failed")
    .map(candidate => ({ resourceId: candidate.resourceId, reason: "commit-failed" as const }));
}

function nextRetryableIndex(candidates: readonly Ari10BatchCandidate[], startIndex = 0): number | null {
  for (let index = Math.max(0, startIndex); index < candidates.length; index += 1) {
    const status = candidates[index]?.status;
    if (status === "accepted" || status === "failed") return index;
  }
  return null;
}

function withCandidateState(
  state: Ari10BatchTransaction,
  candidates: readonly Ari10BatchCandidate[],
  overrides: Partial<Pick<Ari10BatchTransaction, "phase" | "cursor" | "cancelled" | "findings">> = {},
): Ari10BatchTransaction {
  return {
    ...state,
    ...overrides,
    candidates,
    committedResourceIds: deriveCommittedResourceIds(candidates),
    failures: deriveFailures(candidates),
  };
}

export function stageAri10BatchImport(request: Ari10StageRequest): Ari10BatchTransaction {
  const findings: string[] = [];
  const seen = new Set<string>();
  const candidates: Ari10BatchCandidate[] = [];

  for (const candidate of request.candidates) {
    if (!candidate.resourceId) {
      findings.push("candidate-resource-id-empty");
      continue;
    }
    if (seen.has(candidate.resourceId)) {
      findings.push(`candidate-resource-duplicate:${candidate.resourceId}`);
      continue;
    }
    seen.add(candidate.resourceId);
    candidates.push(cloneCandidate(candidate));
  }

  return {
    transactionId: request.transactionId,
    phase: "staged",
    candidates,
    cursor: candidates.length > 0 ? { transactionId: request.transactionId, nextCandidateIndex: 0 } : null,
    committedResourceIds: [],
    failures: [],
    findings,
    cancelled: false,
    sourceInputsMutated: false,
    rightsGranted: false,
    canonGranted: false,
    ownershipGranted: false,
    providerEntitlementGranted: false,
  };
}

export function inspectAri10BatchImport(state: Ari10BatchTransaction): Ari10BatchTransaction {
  if (state.phase !== "staged") return state;
  return { ...state, phase: "inspected" };
}

export function decideAri10BatchImport(
  state: Ari10BatchTransaction,
  decisions: readonly Ari10CandidateDecision[],
): Ari10BatchTransaction {
  if (state.phase !== "inspected" && state.phase !== "decided") return state;

  const decisionById = new Map<string, Ari10Decision>();
  const findings = [...state.findings];
  const candidateIds = new Set(state.candidates.map(candidate => candidate.resourceId));

  for (const decision of decisions) {
    if (!candidateIds.has(decision.resourceId)) {
      findings.push(`decision-resource-missing:${decision.resourceId}`);
      continue;
    }
    decisionById.set(decision.resourceId, decision.decision);
  }

  const candidates = state.candidates.map(candidate => {
    const decision = decisionById.get(candidate.resourceId);
    if (!decision || candidate.status === "committed") return { ...candidate, rawSourceMetadata: { ...candidate.rawSourceMetadata } };
    return {
      ...candidate,
      rawSourceMetadata: { ...candidate.rawSourceMetadata },
      status: decision === "accept" ? "accepted" as const : "rejected" as const,
    };
  });
  const nextIndex = nextRetryableIndex(candidates);

  return withCandidateState(state, candidates, {
    phase: "decided",
    findings,
    cursor: nextIndex === null ? null : { transactionId: state.transactionId, nextCandidateIndex: nextIndex },
    cancelled: false,
  });
}

export function commitAri10BatchImport(
  state: Ari10BatchTransaction,
  options: Ari10CommitOptions = {},
): Ari10BatchTransaction {
  if (state.phase === "completed" || state.phase === "cancelled") return state;
  if (state.phase !== "decided") return state;

  const maxCandidates = options.maxCandidates === undefined
    ? Number.POSITIVE_INFINITY
    : Math.max(0, Math.floor(options.maxCandidates));
  if (maxCandidates === 0) return state;

  const failIds = new Set(options.failResourceIds ?? []);
  const candidates = state.candidates.map(candidate => ({
    ...candidate,
    rawSourceMetadata: { ...candidate.rawSourceMetadata },
  }));
  const startIndex = state.cursor?.transactionId === state.transactionId
    ? state.cursor.nextCandidateIndex
    : 0;
  let attempts = 0;
  let scanIndex = Math.max(0, Math.min(startIndex, candidates.length));

  for (; scanIndex < candidates.length && attempts < maxCandidates; scanIndex += 1) {
    const candidate = candidates[scanIndex];
    if (!candidate || (candidate.status !== "accepted" && candidate.status !== "failed")) continue;
    attempts += 1;
    candidates[scanIndex] = {
      ...candidate,
      status: failIds.has(candidate.resourceId) ? "failed" : "committed",
    };
  }

  const failedIndex = candidates.findIndex(candidate => candidate.status === "failed");
  const remainingIndex = nextRetryableIndex(candidates, scanIndex);
  const nextIndex = failedIndex >= 0
    ? failedIndex
    : remainingIndex;
  const hasRetryable = nextIndex !== null;

  return withCandidateState(state, candidates, {
    phase: hasRetryable ? "decided" : "completed",
    cursor: hasRetryable ? { transactionId: state.transactionId, nextCandidateIndex: nextIndex } : null,
    cancelled: false,
  });
}

export function cancelAri10BatchImport(state: Ari10BatchTransaction): Ari10BatchTransaction {
  if (state.phase === "completed" || state.phase === "cancelled") return state;
  return { ...state, phase: "cancelled", cancelled: true };
}

export function resumeAri10BatchImport(
  state: Ari10BatchTransaction,
  cursor: Ari10BatchCursor,
): Ari10BatchTransaction {
  if (state.phase !== "cancelled") return state;
  if (cursor.transactionId !== state.transactionId) {
    return { ...state, findings: [...state.findings, `resume-cursor-transaction-mismatch:${cursor.transactionId}`] };
  }
  if (!Number.isSafeInteger(cursor.nextCandidateIndex) || cursor.nextCandidateIndex < 0 || cursor.nextCandidateIndex > state.candidates.length) {
    return { ...state, findings: [...state.findings, `resume-cursor-invalid-index:${cursor.nextCandidateIndex}`] };
  }
  const nextIndex = nextRetryableIndex(state.candidates, cursor.nextCandidateIndex);
  return {
    ...state,
    phase: nextIndex === null ? "completed" : "decided",
    cancelled: false,
    cursor: nextIndex === null ? null : { transactionId: state.transactionId, nextCandidateIndex: nextIndex },
  };
}

export const ARI10_AUTHORITY_BOUNDARY = {
  rightsLicenseCapabilityMatrixImplemented: false,
  rightsInferenceAuthorized: false,
  canonInferenceAuthorized: false,
  ownershipInferenceAuthorized: false,
  providerEntitlementInferenceAuthorized: false,
  providerAccessAuthorized: false,
  externalScrapingAuthorized: false,
  testerDistributionAuthorized: false,
  releaseOrDeploymentAuthorized: false,
  realMoneySpentCents: 0,
} as const;
