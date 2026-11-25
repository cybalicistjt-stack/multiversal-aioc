export const ARI01_SCHEMA_VERSION = "1.0.0" as const;

export const ARI01_MEDIA_KINDS = [
  "map",
  "tileset",
  "sprite",
  "portrait",
  "token",
  "prop",
  "icon",
  "audio",
  "animation",
  "document",
  "future-3d",
  "unknown",
] as const;

export const ARI01_SOURCE_CLASSES = [
  "user-owned-local",
  "first-party-native",
  "generated",
  "imported-local",
  "provider-reference",
  "unknown",
] as const;

export const ARI01_AVAILABILITY_STATES = [
  "available-local",
  "reference-only",
  "missing",
  "denied",
  "revoked",
  "unsupported",
  "unknown",
] as const;

export const ARI01_USE_CAPABILITIES = [
  "reference",
  "private-use",
  "campaign-use",
  "transform",
  "export",
  "redistribute",
  "commercial-use",
] as const;

export type Ari01MediaKind = (typeof ARI01_MEDIA_KINDS)[number];
export type Ari01SourceClass = (typeof ARI01_SOURCE_CLASSES)[number];
export type Ari01AvailabilityState = (typeof ARI01_AVAILABILITY_STATES)[number];
export type Ari01UseCapability = (typeof ARI01_USE_CAPABILITIES)[number];
export type Ari01CapabilityState = "allowed" | "denied" | "unknown";

export interface Ari01OwnerReference {
  readonly ownerAuthority: string;
  readonly stableId: string;
  readonly versionReference: string | null;
  readonly ari01MayMutate: false;
}

export interface Ari01ProviderReference {
  readonly providerId: string;
  readonly externalId: string;
  readonly controlReference: string | null;
  readonly contentBytesOwnedByMultiversal: false;
  readonly entitlementImplied: false;
  readonly extractionAuthorized: false;
}

export interface Ari01CapabilityEvidence {
  readonly state: Ari01CapabilityState;
  readonly evidenceReference: string;
  readonly permissionsInferred: false;
}

export type Ari01CapabilityMatrix = Readonly<Record<Ari01UseCapability, Ari01CapabilityEvidence>>;

export interface Ari01ResourceHandle {
  readonly resourceId: string;
  readonly label: string;
  readonly mediaKind: Ari01MediaKind;
  readonly sourceClass: Ari01SourceClass;
  readonly availability: Ari01AvailabilityState;
  readonly ownerReference: Ari01OwnerReference;
  readonly providerReference: Ari01ProviderReference | null;
  readonly capabilities: Ari01CapabilityMatrix;
  readonly provenanceReference: string;
  readonly byteIdentityReference: null;
  readonly permissionsInferred: false;
  readonly canonicalAssetLedgerEntryCreated: false;
}

export interface Ari01ResourceCatalog {
  readonly schemaVersion: typeof ARI01_SCHEMA_VERSION;
  readonly resources: readonly Ari01ResourceHandle[];
}

export interface Ari01ValidationResult {
  readonly accepted: boolean;
  readonly findings: readonly string[];
  readonly resourceCount: number;
  readonly ownerMutationPerformed: false;
  readonly canonicalAssetLedgerCreated: false;
  readonly byteIdentityImplemented: false;
  readonly deduplicationImplemented: false;
  readonly ingestionRuntimeImplemented: false;
  readonly providerNetworkAccessPerformed: false;
  readonly realMoneySpentCents: 0;
}

const BLOCKED_AVAILABILITY: readonly Ari01AvailabilityState[] = [
  "missing",
  "denied",
  "revoked",
  "unsupported",
  "unknown",
];

const unique = (values: readonly string[]) => new Set(values).size === values.length;

export function canAri01Use(handle: Ari01ResourceHandle, capability: Ari01UseCapability): boolean {
  if (BLOCKED_AVAILABILITY.includes(handle.availability)) return false;
  return handle.capabilities[capability].state === "allowed";
}

export function validateAri01ResourceCatalog(catalog: Ari01ResourceCatalog): Ari01ValidationResult {
  const findings: string[] = [];
  const resourceIds = catalog.resources.map(row => row.resourceId);

  if (catalog.schemaVersion !== ARI01_SCHEMA_VERSION) findings.push("schema-version-mismatch");
  if (!unique(resourceIds)) {
    const seen = new Set<string>();
    for (const id of resourceIds) {
      if (seen.has(id)) findings.push(`duplicate-resource-id:${id}`);
      seen.add(id);
    }
  }

  for (const resource of catalog.resources) {
    if (!resource.resourceId || !resource.label) findings.push(`resource-identity-missing:${resource.resourceId || "unknown"}`);
    if (!resource.ownerReference.ownerAuthority || !resource.ownerReference.stableId) findings.push(`resource-owner-reference-missing:${resource.resourceId}`);
    if (resource.ownerReference.ari01MayMutate !== false) findings.push(`resource-owner-mutation:${resource.resourceId}`);
    if (!resource.provenanceReference) findings.push(`resource-provenance-missing:${resource.resourceId}`);
    if (resource.permissionsInferred !== false) findings.push(`resource-permission-inference:${resource.resourceId}`);
    if (resource.canonicalAssetLedgerEntryCreated !== false) findings.push(`resource-shadow-ledger:${resource.resourceId}`);
    if (resource.byteIdentityReference !== null) findings.push(`resource-byte-identity-boundary:${resource.resourceId}`);

    if (resource.sourceClass === "provider-reference") {
      if (resource.providerReference === null) findings.push(`provider-reference-missing:${resource.resourceId}`);
      if (resource.availability !== "reference-only" && resource.availability !== "unknown" && resource.availability !== "missing" && resource.availability !== "denied" && resource.availability !== "revoked" && resource.availability !== "unsupported") {
        findings.push(`provider-reference-availability-boundary:${resource.resourceId}`);
      }
    } else if (resource.providerReference !== null) {
      findings.push(`non-provider-resource-has-provider-reference:${resource.resourceId}`);
    }

    if (resource.providerReference !== null) {
      const provider = resource.providerReference;
      if (!provider.providerId || !provider.externalId) findings.push(`provider-reference-identity-missing:${resource.resourceId}`);
      if (provider.contentBytesOwnedByMultiversal !== false || provider.entitlementImplied !== false || provider.extractionAuthorized !== false) {
        findings.push(`provider-reference-authority-boundary:${resource.resourceId}`);
      }
    }

    for (const capability of ARI01_USE_CAPABILITIES) {
      const evidence = resource.capabilities[capability];
      if (!evidence || !evidence.evidenceReference) findings.push(`capability-evidence-missing:${resource.resourceId}:${capability}`);
      if (evidence?.permissionsInferred !== false) findings.push(`capability-permission-inference:${resource.resourceId}:${capability}`);
    }
  }

  return {
    accepted: findings.length === 0,
    findings,
    resourceCount: catalog.resources.length,
    ownerMutationPerformed: false,
    canonicalAssetLedgerCreated: false,
    byteIdentityImplemented: false,
    deduplicationImplemented: false,
    ingestionRuntimeImplemented: false,
    providerNetworkAccessPerformed: false,
    realMoneySpentCents: 0,
  };
}

export const ARI01_AUTHORITY_BOUNDARY = {
  canonicalAssetLedgerCreated: false,
  byteIdentityImplemented: false,
  deduplicationImplemented: false,
  derivativeLineageImplemented: false,
  archiveIngestionImplemented: false,
  providerCredentialsStored: false,
  providerNetworkAccessAuthorized: false,
  runtimeOwnerIntegrationImplemented: false,
  migrationReserved: false,
  rightsMatrixExpansionOwnedBy: "ARI-11",
  realMoneySpentCents: 0,
} as const;

