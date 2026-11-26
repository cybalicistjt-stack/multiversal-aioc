import type { Ari02ResourceByteBinding } from "./content-addressed-byte-identity-deduplication";

export const ARI03_SCHEMA_VERSION = "1.0.0" as const;

export interface Ari03DerivativeEdge {
  readonly relation: "derived-from";
  readonly sourceResourceId: string;
  readonly derivativeResourceId: string;
  readonly sourceContentAddressAtGeneration: string;
  readonly sourceTruthMutated: false;
}

export interface Ari03VersionEdge {
  readonly relation: "version-successor";
  readonly previousResourceId: string;
  readonly nextResourceId: string;
}

export interface Ari03SupersessionEdge {
  readonly relation: "superseded-by";
  readonly supersededResourceId: string;
  readonly replacementResourceId: string;
}

export interface Ari03LineageGraph {
  readonly derivativeEdges: readonly Ari03DerivativeEdge[];
  readonly versionEdges: readonly Ari03VersionEdge[];
  readonly supersessionEdges: readonly Ari03SupersessionEdge[];
}

export type Ari03DerivativeStaleness =
  | "current"
  | "stale"
  | "source-unavailable"
  | "source-mismatch";

export interface Ari03ValidationResult {
  readonly accepted: boolean;
  readonly findings: readonly string[];
  readonly derivativeEdgeCount: number;
  readonly versionEdgeCount: number;
  readonly supersessionEdgeCount: number;
  readonly sourceTruthMutationPerformed: false;
  readonly canonicalAssetLedgerCreated: false;
  readonly derivativeGenerationPerformed: false;
  readonly archiveIngestionImplemented: false;
  readonly providerNetworkAccessPerformed: false;
  readonly realMoneySpentCents: 0;
}

const SHA256_CONTENT_ADDRESS = /^sha256:[0-9a-f]{64}$/;

export function createAri03DerivativeEdge(
  source: Ari02ResourceByteBinding,
  derivativeResourceId: string,
): Ari03DerivativeEdge {
  if (source.byteState !== "byte-present" || source.byteIdentity === null) {
    throw new Error(`ari03-source-byte-identity-required:${source.resourceId}`);
  }
  if (!source.resourceId) {
    throw new Error("ari03-source-resource-id-required");
  }
  if (!derivativeResourceId) {
    throw new Error("ari03-derivative-resource-id-required");
  }
  if (source.resourceId === derivativeResourceId) {
    throw new Error(`ari03-self-derivation:${source.resourceId}`);
  }

  return {
    relation: "derived-from",
    sourceResourceId: source.resourceId,
    derivativeResourceId,
    sourceContentAddressAtGeneration: source.byteIdentity.contentAddress,
    sourceTruthMutated: false,
  };
}

export function createAri03VersionEdge(
  previousResourceId: string,
  nextResourceId: string,
): Ari03VersionEdge {
  if (!previousResourceId || !nextResourceId) {
    throw new Error("ari03-version-resource-id-required");
  }
  if (previousResourceId === nextResourceId) {
    throw new Error(`ari03-self-version:${previousResourceId}`);
  }
  return {
    relation: "version-successor",
    previousResourceId,
    nextResourceId,
  };
}

export function createAri03SupersessionEdge(
  supersededResourceId: string,
  replacementResourceId: string,
): Ari03SupersessionEdge {
  if (!supersededResourceId || !replacementResourceId) {
    throw new Error("ari03-supersession-resource-id-required");
  }
  if (supersededResourceId === replacementResourceId) {
    throw new Error(`ari03-self-supersession:${supersededResourceId}`);
  }
  return {
    relation: "superseded-by",
    supersededResourceId,
    replacementResourceId,
  };
}

export function evaluateAri03DerivativeStaleness(
  edge: Ari03DerivativeEdge,
  currentSource: Ari02ResourceByteBinding,
): Ari03DerivativeStaleness {
  if (currentSource.resourceId !== edge.sourceResourceId) {
    return "source-mismatch";
  }
  if (currentSource.byteState !== "byte-present" || currentSource.byteIdentity === null) {
    return "source-unavailable";
  }
  return currentSource.byteIdentity.contentAddress === edge.sourceContentAddressAtGeneration
    ? "current"
    : "stale";
}

export function validateAri03LineageGraph(graph: Ari03LineageGraph): Ari03ValidationResult {
  const findings: string[] = [];

  for (const edge of graph.derivativeEdges) {
    if (!edge.sourceResourceId) findings.push("derivative-source-id-missing");
    if (!edge.derivativeResourceId) findings.push("derivative-resource-id-missing");
    if (edge.sourceResourceId === edge.derivativeResourceId) {
      findings.push(`self-derivative-edge:${edge.sourceResourceId}`);
    }
    if (!SHA256_CONTENT_ADDRESS.test(edge.sourceContentAddressAtGeneration)) {
      findings.push(`invalid-source-content-address:${edge.derivativeResourceId}`);
    }
    if (edge.sourceTruthMutated !== false) {
      findings.push(`source-truth-mutation:${edge.sourceResourceId}`);
    }
  }

  for (const edge of graph.versionEdges) {
    if (!edge.previousResourceId) findings.push("version-previous-id-missing");
    if (!edge.nextResourceId) findings.push("version-next-id-missing");
    if (edge.previousResourceId === edge.nextResourceId) {
      findings.push(`self-version-edge:${edge.previousResourceId}`);
    }
  }

  for (const edge of graph.supersessionEdges) {
    if (!edge.supersededResourceId) findings.push("superseded-resource-id-missing");
    if (!edge.replacementResourceId) findings.push("replacement-resource-id-missing");
    if (edge.supersededResourceId === edge.replacementResourceId) {
      findings.push(`self-supersession-edge:${edge.supersededResourceId}`);
    }
  }

  return {
    accepted: findings.length === 0,
    findings,
    derivativeEdgeCount: graph.derivativeEdges.length,
    versionEdgeCount: graph.versionEdges.length,
    supersessionEdgeCount: graph.supersessionEdges.length,
    sourceTruthMutationPerformed: false,
    canonicalAssetLedgerCreated: false,
    derivativeGenerationPerformed: false,
    archiveIngestionImplemented: false,
    providerNetworkAccessPerformed: false,
    realMoneySpentCents: 0,
  };
}

export const ARI03_AUTHORITY_BOUNDARY = {
  sourceTruthMutationAuthorized: false,
  canonicalAssetLedgerCreated: false,
  derivativeGenerationPerformed: false,
  archiveIngestionImplemented: false,
  mediaClassificationImplemented: false,
  rightsMatrixExpansionImplemented: false,
  providerCredentialsStored: false,
  providerNetworkAccessAuthorized: false,
  realMoneySpentCents: 0,
} as const;
