import {
  ARI01_SCHEMA_VERSION,
  canAri01Use,
  validateAri01ResourceCatalog,
  type Ari01ResourceHandle,
} from "./universal-resource-handle-capability-contract";
import type { Ari02ResourceByteBinding } from "./content-addressed-byte-identity-deduplication";
import {
  createAri03DerivativeEdge,
  createAri03VersionEdge,
  type Ari03DerivativeEdge,
  type Ari03VersionEdge,
} from "./derivative-lineage-graph";

export const ARI18_SCHEMA_VERSION = "1.0.0" as const;

export type Ari18ProducerKind = "native" | "CAPP" | "PAPT";

export interface Ari18ProductionMetadata {
  readonly producerKind: Ari18ProducerKind;
  readonly toolOrRenderer: string | null;
  readonly recipeReference: string | null;
  readonly versionReference: string;
}

export interface Ari18RegisteredAsset {
  readonly resource: Ari01ResourceHandle;
  readonly production: Ari18ProductionMetadata;
  readonly derivativeEdge: Ari03DerivativeEdge | null;
  readonly versionEdge: Ari03VersionEdge | null;
}

export interface Ari18RegistrationInput {
  readonly resource: Ari01ResourceHandle;
  readonly production: Ari18ProductionMetadata;
  readonly existingRegistrations: readonly Ari18RegisteredAsset[];
  readonly parentSources?: readonly Ari02ResourceByteBinding[];
  readonly previousVersionResourceId?: string;
}

export type Ari18RegistrationStatus =
  | "registered"
  | "version-registered"
  | "already-registered"
  | "owner-reference-invalid"
  | "version-mismatch"
  | "production-metadata-invalid"
  | "producer-owner-mismatch"
  | "unsupported-source-class"
  | "reference-rights-not-allowed"
  | "unsupported-multi-parent-lineage"
  | "derivative-source-byte-identity-required"
  | "previous-version-not-found"
  | "previous-version-incompatible"
  | "resource-id-conflict"
  | "resource-invalid";

export interface Ari18RegistrationResult {
  readonly status: Ari18RegistrationStatus;
  readonly registration: Ari18RegisteredAsset | null;
  readonly registrations: readonly Ari18RegisteredAsset[];
  readonly sourceOwnerMutationPerformed: false;
  readonly sourceSemanticsCopied: false;
  readonly rightsInferred: false;
  readonly providerAuthenticationPerformed: false;
  readonly providerContentAcquired: false;
  readonly canonicalAssetLedgerCreated: false;
}

const fail = (
  status: Exclude<Ari18RegistrationStatus, "registered" | "version-registered" | "already-registered">,
  registrations: readonly Ari18RegisteredAsset[],
): Ari18RegistrationResult => ({
  status,
  registration: null,
  registrations,
  sourceOwnerMutationPerformed: false,
  sourceSemanticsCopied: false,
  rightsInferred: false,
  providerAuthenticationPerformed: false,
  providerContentAcquired: false,
  canonicalAssetLedgerCreated: false,
});

const success = (
  status: "registered" | "version-registered" | "already-registered",
  registration: Ari18RegisteredAsset,
  registrations: readonly Ari18RegisteredAsset[],
): Ari18RegistrationResult => ({
  status,
  registration,
  registrations,
  sourceOwnerMutationPerformed: false,
  sourceSemanticsCopied: false,
  rightsInferred: false,
  providerAuthenticationPerformed: false,
  providerContentAcquired: false,
  canonicalAssetLedgerCreated: false,
});

const sameJson = (left: unknown, right: unknown): boolean => JSON.stringify(left) === JSON.stringify(right);

function ownerReferenceIsValid(resource: Ari01ResourceHandle): boolean {
  const owner = resource.ownerReference;
  return Boolean(
    owner.ownerAuthority &&
      owner.stableId &&
      owner.versionReference &&
      owner.ari01MayMutate === false,
  );
}

function productionMatchesOwner(
  resource: Ari01ResourceHandle,
  production: Ari18ProductionMetadata,
): boolean {
  if (resource.sourceClass === "first-party-native") {
    return production.producerKind === "native";
  }
  if (resource.sourceClass !== "generated") return false;
  return (
    (production.producerKind === "CAPP" || production.producerKind === "PAPT") &&
    resource.ownerReference.ownerAuthority === production.producerKind
  );
}

export function registerAri18NativeOrGeneratedAsset(
  input: Ari18RegistrationInput,
): Ari18RegistrationResult {
  const { resource, production, existingRegistrations } = input;

  if (!ownerReferenceIsValid(resource)) {
    return fail("owner-reference-invalid", existingRegistrations);
  }
  if (resource.sourceClass !== "first-party-native" && resource.sourceClass !== "generated") {
    return fail("unsupported-source-class", existingRegistrations);
  }
  if (!production.versionReference || production.versionReference !== resource.ownerReference.versionReference) {
    return fail("version-mismatch", existingRegistrations);
  }
  if (
    (resource.sourceClass === "generated" && !production.toolOrRenderer) ||
    (resource.sourceClass === "first-party-native" && production.producerKind !== "native")
  ) {
    return fail("production-metadata-invalid", existingRegistrations);
  }
  if (!productionMatchesOwner(resource, production)) {
    return fail("producer-owner-mismatch", existingRegistrations);
  }
  if (!canAri01Use(resource, "reference")) {
    return fail("reference-rights-not-allowed", existingRegistrations);
  }

  const resourceValidation = validateAri01ResourceCatalog({
    schemaVersion: ARI01_SCHEMA_VERSION,
    resources: [resource],
  });
  if (!resourceValidation.accepted) {
    return fail("resource-invalid", existingRegistrations);
  }

  const parentSources = input.parentSources ?? [];
  if (parentSources.length > 1) {
    return fail("unsupported-multi-parent-lineage", existingRegistrations);
  }

  let derivativeEdge: Ari03DerivativeEdge | null = null;
  if (parentSources.length === 1) {
    const source = parentSources[0];
    if (source.byteState !== "byte-present" || source.byteIdentity === null) {
      return fail("derivative-source-byte-identity-required", existingRegistrations);
    }
    derivativeEdge = createAri03DerivativeEdge(source, resource.resourceId);
  }

  let versionEdge: Ari03VersionEdge | null = null;
  if (input.previousVersionResourceId) {
    const previous = existingRegistrations.find(
      row => row.resource.resourceId === input.previousVersionResourceId,
    );
    if (!previous) {
      return fail("previous-version-not-found", existingRegistrations);
    }
    if (
      previous.resource.ownerReference.ownerAuthority !== resource.ownerReference.ownerAuthority ||
      previous.resource.ownerReference.stableId !== resource.ownerReference.stableId
    ) {
      return fail("previous-version-incompatible", existingRegistrations);
    }
    versionEdge = createAri03VersionEdge(previous.resource.resourceId, resource.resourceId);
  }

  const candidate: Ari18RegisteredAsset = {
    resource,
    production,
    derivativeEdge,
    versionEdge,
  };

  const sameId = existingRegistrations.find(
    row => row.resource.resourceId === resource.resourceId,
  );
  if (sameId) {
    return sameJson(sameId, candidate)
      ? success("already-registered", sameId, existingRegistrations)
      : fail("resource-id-conflict", existingRegistrations);
  }

  const registrations = [...existingRegistrations, candidate];
  return success(versionEdge ? "version-registered" : "registered", candidate, registrations);
}

export const ARI18_AUTHORITY_BOUNDARY = {
  sourceOwnerMutationAuthorized: false,
  sourceSemanticMutationAuthorized: false,
  rightsInferenceAuthorized: false,
  providerAuthenticationAuthorized: false,
  providerContentAcquisitionAuthorized: false,
  canonicalAssetLedgerCreated: false,
  assetPickerImplemented: false,
  resourcePackIntakeUxImplemented: false,
  relinkRecoveryImplemented: false,
  releaseOrDeploymentAuthorized: false,
  migrationReserved: false,
} as const;
