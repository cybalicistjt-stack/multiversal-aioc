export const ARI02_SCHEMA_VERSION = "1.0.0" as const;

export type Ari02ByteState = "byte-present" | "reference-only";

export interface Ari02ByteIdentity {
  readonly algorithm: "sha-256";
  readonly digestHex: string;
  readonly contentAddress: string;
  readonly byteLength: number;
  readonly sourceByteRole: "original";
  readonly storageLocator: null;
}

export interface Ari02ResourceByteBinding {
  readonly resourceId: string;
  readonly byteState: Ari02ByteState;
  readonly byteIdentity: Ari02ByteIdentity | null;
}

export interface Ari02DuplicateGroup {
  readonly contentAddress: string;
  readonly resourceIds: readonly string[];
}

export interface Ari02DeduplicationIndex {
  readonly uniqueByteIdentityCount: number;
  readonly resourceBindingCount: number;
  readonly duplicateGroups: readonly Ari02DuplicateGroup[];
  readonly canonicalAssetLedgerCreated: false;
}

export interface Ari02ValidationResult {
  readonly accepted: boolean;
  readonly findings: readonly string[];
  readonly bytePresentCount: number;
  readonly referenceOnlyCount: number;
  readonly canonicalAssetLedgerCreated: false;
  readonly derivativeLineageImplemented: false;
  readonly archiveIngestionImplemented: false;
  readonly providerNetworkAccessPerformed: false;
  readonly realMoneySpentCents: 0;
}

const SHA256_DIGEST = /^[0-9a-f]{64}$/;

const bytesToHex = (bytes: Uint8Array): string =>
  Array.from(bytes, byte => byte.toString(16).padStart(2, "0")).join("");

async function sha256DigestHex(bytes: Uint8Array): Promise<string> {
  const originalBytes = Uint8Array.from(bytes);
  const digest = await globalThis.crypto.subtle.digest("SHA-256", originalBytes);
  return bytesToHex(new Uint8Array(digest));
}

export async function bindAri02BytePresent(
  resourceId: string,
  originalBytes: Uint8Array,
): Promise<Ari02ResourceByteBinding> {
  const digestHex = await sha256DigestHex(originalBytes);
  return {
    resourceId,
    byteState: "byte-present",
    byteIdentity: {
      algorithm: "sha-256",
      digestHex,
      contentAddress: `sha256:${digestHex}`,
      byteLength: originalBytes.byteLength,
      sourceByteRole: "original",
      storageLocator: null,
    },
  };
}

export function bindAri02ReferenceOnly(resourceId: string): Ari02ResourceByteBinding {
  return {
    resourceId,
    byteState: "reference-only",
    byteIdentity: null,
  };
}

export function buildAri02DeduplicationIndex(
  bindings: readonly Ari02ResourceByteBinding[],
): Ari02DeduplicationIndex {
  const grouped = new Map<string, string[]>();
  for (const binding of bindings) {
    const address = binding.byteIdentity?.contentAddress;
    if (!address) continue;
    const resourceIds = grouped.get(address) ?? [];
    resourceIds.push(binding.resourceId);
    grouped.set(address, resourceIds);
  }

  const duplicateGroups: Ari02DuplicateGroup[] = [];
  for (const [contentAddress, resourceIds] of grouped) {
    if (resourceIds.length > 1) {
      duplicateGroups.push({ contentAddress, resourceIds: [...resourceIds] });
    }
  }

  return {
    uniqueByteIdentityCount: grouped.size,
    resourceBindingCount: bindings.length,
    duplicateGroups,
    canonicalAssetLedgerCreated: false,
  };
}

export function validateAri02ResourceByteBindings(
  bindings: readonly Ari02ResourceByteBinding[],
): Ari02ValidationResult {
  const findings: string[] = [];
  let bytePresentCount = 0;
  let referenceOnlyCount = 0;

  for (const binding of bindings) {
    if (!binding.resourceId) findings.push("resource-id-missing");

    if (binding.byteState === "reference-only") {
      referenceOnlyCount += 1;
      if (binding.byteIdentity !== null) {
        findings.push(`reference-only-byte-identity-present:${binding.resourceId}`);
      }
      continue;
    }

    bytePresentCount += 1;
    const identity = binding.byteIdentity;
    if (identity === null) {
      findings.push(`byte-identity-missing:${binding.resourceId}`);
      continue;
    }

    if (identity.algorithm !== "sha-256") {
      findings.push(`unsupported-digest-algorithm:${binding.resourceId}`);
    }
    if (!SHA256_DIGEST.test(identity.digestHex)) {
      findings.push(`invalid-sha256-digest:${binding.resourceId}`);
    }
    if (identity.contentAddress !== `sha256:${identity.digestHex}`) {
      findings.push(`content-address-mismatch:${binding.resourceId}`);
    }
    if (!Number.isSafeInteger(identity.byteLength) || identity.byteLength < 0) {
      findings.push(`invalid-byte-length:${binding.resourceId}`);
    }
    if (identity.sourceByteRole !== "original") {
      findings.push(`non-original-byte-role:${binding.resourceId}`);
    }
    if (identity.storageLocator !== null) {
      findings.push(`storage-locator-not-neutral:${binding.resourceId}`);
    }
  }

  return {
    accepted: findings.length === 0,
    findings,
    bytePresentCount,
    referenceOnlyCount,
    canonicalAssetLedgerCreated: false,
    derivativeLineageImplemented: false,
    archiveIngestionImplemented: false,
    providerNetworkAccessPerformed: false,
    realMoneySpentCents: 0,
  };
}

export const ARI02_AUTHORITY_BOUNDARY = {
  canonicalAssetLedgerCreated: false,
  derivativeLineageImplemented: false,
  archiveIngestionImplemented: false,
  mediaClassificationImplemented: false,
  rightsMatrixExpansionImplemented: false,
  providerCredentialsStored: false,
  providerNetworkAccessAuthorized: false,
  realMoneySpentCents: 0,
} as const;
