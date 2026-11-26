export const ARI11_CAPABILITIES = [
  "private-use",
  "transform",
  "campaign-use",
  "export",
  "redistribution",
  "commercial-use",
] as const;

export type Ari11Capability = (typeof ARI11_CAPABILITIES)[number];
export type Ari11CapabilityState = "unknown" | "allowed" | "denied" | "revoked";

export type Ari11CapabilityEvidence = Readonly<{
  evidenceId: string;
  capability: Ari11Capability;
  state: Ari11CapabilityState;
  source: string;
  rawMetadata?: unknown;
}>;

export type Ari11CapabilityMatrixInput = Readonly<{
  resourceId: string;
  evidence: readonly Ari11CapabilityEvidence[];
  resourceExists?: boolean;
  priorImportAccepted?: boolean;
}>;

export type Ari11CapabilityRow = Readonly<{
  capability: Ari11Capability;
  state: Ari11CapabilityState;
  evidenceIds: readonly string[];
}>;

export type Ari11UseCapabilityMatrix = Readonly<{
  resourceId: string;
  capabilities: readonly Ari11CapabilityRow[];
  evidence: readonly Ari11CapabilityEvidence[];
  findings: readonly string[];
  rightsInferredFromExistence: false;
  rightsInferredFromImportAcceptance: false;
}>;

export const ARI11_AUTHORITY_BOUNDARY = Object.freeze({
  visualDerivativeWorkerImplemented: false,
  providerAccessAuthorized: false,
  redistributionAuthorizedByTheSystem: false,
  releaseOrDeploymentAuthorized: false,
} as const);

const STATE_RESTRICTIVENESS: Readonly<Record<Ari11CapabilityState, number>> = Object.freeze({
  allowed: 0,
  unknown: 1,
  denied: 2,
  revoked: 3,
});

function compareEvidence(a: Ari11CapabilityEvidence, b: Ari11CapabilityEvidence): number {
  return (
    a.evidenceId.localeCompare(b.evidenceId) ||
    a.capability.localeCompare(b.capability) ||
    a.state.localeCompare(b.state) ||
    a.source.localeCompare(b.source)
  );
}

function resolveCapabilityState(evidence: readonly Ari11CapabilityEvidence[]): Ari11CapabilityState {
  if (evidence.length === 0) return "unknown";

  let resolved: Ari11CapabilityState = "allowed";
  for (const row of evidence) {
    if (STATE_RESTRICTIVENESS[row.state] > STATE_RESTRICTIVENESS[resolved]) {
      resolved = row.state;
    }
  }
  return resolved;
}

export function buildAri11UseCapabilityMatrix(input: Ari11CapabilityMatrixInput): Ari11UseCapabilityMatrix {
  const evidence = [...input.evidence].sort(compareEvidence);
  const findings: string[] = [];

  const capabilities = ARI11_CAPABILITIES.map<Ari11CapabilityRow>(capability => {
    const relevant = evidence.filter(row => row.capability === capability);
    const distinctStates = new Set(relevant.map(row => row.state));
    if (distinctStates.size > 1) findings.push(`conflicting-capability-evidence:${capability}`);

    return Object.freeze({
      capability,
      state: resolveCapabilityState(relevant),
      evidenceIds: Object.freeze(relevant.map(row => row.evidenceId)),
    });
  });

  return Object.freeze({
    resourceId: input.resourceId,
    capabilities: Object.freeze(capabilities),
    evidence: Object.freeze(evidence),
    findings: Object.freeze(findings),
    rightsInferredFromExistence: false,
    rightsInferredFromImportAcceptance: false,
  });
}

export function evaluateAri11Capability(
  matrix: Ari11UseCapabilityMatrix,
  capability: Ari11Capability,
): Readonly<{ capability: Ari11Capability; state: Ari11CapabilityState; allowed: boolean }> {
  const state = matrix.capabilities.find(row => row.capability === capability)?.state ?? "unknown";
  return Object.freeze({ capability, state, allowed: state === "allowed" });
}

export function filterAri11Actions(
  matrix: Ari11UseCapabilityMatrix,
  actions: readonly Ari11Capability[],
): Ari11Capability[] {
  return actions.filter(action => evaluateAri11Capability(matrix, action).allowed);
}
