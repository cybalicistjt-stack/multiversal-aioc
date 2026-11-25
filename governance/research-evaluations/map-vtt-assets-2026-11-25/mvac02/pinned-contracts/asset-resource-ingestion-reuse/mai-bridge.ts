import {
  canAri01Use,
  type Ari01ProviderReference,
  type Ari01ResourceHandle,
  type Ari01UseCapability,
} from "./universal-resource-handle-capability-contract";
import type {
  Mai02AssetPackage,
  Mai02AssetRecord,
  Mai02PlaceableRecord,
  Mai02Transform,
} from "../map-asset-interoperability/canonical-map-asset-placeable-package-contracts";

export type Ari16MaiWorkflow = "map-asset" | "package" | "placeable" | "tileset";

export type Ari16BridgeStatus =
  | "resolved"
  | "resource-unavailable"
  | "capability-not-allowed"
  | "unsupported-media-kind"
  | "incompatible-media-kind"
  | "mai-target-not-found";

export type Ari16MaiBridgeTarget = Readonly<{
  workflow: Ari16MaiWorkflow;
  stableId: string;
}>;

export type Ari16MaiBridgeRequest = Readonly<{
  resource: Ari01ResourceHandle;
  maiPackage: Mai02AssetPackage;
  target: Ari16MaiBridgeTarget;
  requiredCapability: Ari01UseCapability;
}>;

export type Ari16MaiBridgeResult = Readonly<{
  status: Ari16BridgeStatus;
  resourceId: string;
  resourceMediaKind: Ari01ResourceHandle["mediaKind"];
  sourceClass: Ari01ResourceHandle["sourceClass"];
  availability: Ari01ResourceHandle["availability"];
  requiredCapability: Ari01UseCapability;
  maiPackageId: string;
  maiTargetId: string | null;
  maiAssetId: string | null;
  maiOwnedTransform: Mai02Transform | null;
  provenanceReference: string;
  providerReference: Ari01ProviderReference | null;
  contentBytesOwnedByMultiversal: false;
  providerEntitlementImplied: false;
  providerExtractionAuthorized: false;
  resourceIdentityMutationPerformed: false;
  provenanceMutationPerformed: false;
  rightsMutationPerformed: false;
  maiSemanticMutationPerformed: false;
  coordinatesSynthesized: false;
  layersSynthesized: false;
  importTranslationPerformed: false;
  findings: readonly string[];
}>;

export const ARI16_AUTHORITY_BOUNDARY = Object.freeze({
  resourceIdentityMutationAuthorized: false,
  provenanceMutationAuthorized: false,
  rightsMutationAuthorized: false,
  maiSemanticMutationAuthorized: false,
  coordinateMutationAuthorized: false,
  layerMutationAuthorized: false,
  importTranslationAuthorized: false,
  providerEntitlementAuthorized: false,
  contentOwnershipAuthorized: false,
  releaseOrDeploymentAuthorized: false,
  migrationReserved: false,
  aaiBridgeImplemented: false,
} as const);

const UNAVAILABLE_STATES = new Set<Ari01ResourceHandle["availability"]>([
  "missing",
  "denied",
  "revoked",
  "unsupported",
  "unknown",
]);

const VISUAL_MEDIA_KINDS = new Set<Ari01ResourceHandle["mediaKind"]>([
  "map",
  "tileset",
  "sprite",
  "portrait",
  "token",
  "prop",
  "icon",
  "animation",
]);

const PLACEABLE_MEDIA_KINDS = new Set<Ari01ResourceHandle["mediaKind"]>([
  "map",
  "sprite",
  "portrait",
  "token",
  "prop",
  "icon",
  "animation",
]);

function resultBase(request: Ari16MaiBridgeRequest) {
  const provider = request.resource.providerReference;
  return {
    resourceId: request.resource.resourceId,
    resourceMediaKind: request.resource.mediaKind,
    sourceClass: request.resource.sourceClass,
    availability: request.resource.availability,
    requiredCapability: request.requiredCapability,
    maiPackageId: request.maiPackage.packageId,
    provenanceReference: request.resource.provenanceReference,
    providerReference: provider,
    contentBytesOwnedByMultiversal: false as const,
    providerEntitlementImplied: false as const,
    providerExtractionAuthorized: false as const,
    resourceIdentityMutationPerformed: false as const,
    provenanceMutationPerformed: false as const,
    rightsMutationPerformed: false as const,
    maiSemanticMutationPerformed: false as const,
    coordinatesSynthesized: false as const,
    layersSynthesized: false as const,
    importTranslationPerformed: false as const,
  };
}

function unresolved(
  request: Ari16MaiBridgeRequest,
  status: Exclude<Ari16BridgeStatus, "resolved">,
  finding: string,
): Ari16MaiBridgeResult {
  return Object.freeze({
    ...resultBase(request),
    status,
    maiTargetId: null,
    maiAssetId: null,
    maiOwnedTransform: null,
    findings: Object.freeze([finding]),
  });
}

function resolveAssetTarget(
  pkg: Mai02AssetPackage,
  stableId: string,
  allowedKinds: readonly Mai02AssetRecord["kind"][],
): Mai02AssetRecord | null {
  const asset = pkg.assets.find(row => row.assetId === stableId) ?? null;
  if (!asset || !allowedKinds.includes(asset.kind)) return null;
  return asset;
}

function resolvePlaceableTarget(
  pkg: Mai02AssetPackage,
  stableId: string,
): Readonly<{ placeable: Mai02PlaceableRecord; asset: Mai02AssetRecord }> | null {
  const placeable = pkg.placeables.find(row => row.placeableId === stableId) ?? null;
  if (!placeable) return null;
  const asset = pkg.assets.find(row => row.assetId === placeable.assetId) ?? null;
  if (!asset) return null;
  return Object.freeze({ placeable, asset });
}

export function resolveAri16VisualResourceToMai(
  request: Ari16MaiBridgeRequest,
): Ari16MaiBridgeResult {
  const { resource, maiPackage, target } = request;

  if (UNAVAILABLE_STATES.has(resource.availability)) {
    return unresolved(request, "resource-unavailable", `resource-unavailable:${resource.resourceId}:${resource.availability}`);
  }

  if (!VISUAL_MEDIA_KINDS.has(resource.mediaKind)) {
    return unresolved(request, "unsupported-media-kind", `unsupported-media-kind:${resource.resourceId}:${resource.mediaKind}`);
  }

  if (!canAri01Use(resource, request.requiredCapability)) {
    return unresolved(request, "capability-not-allowed", `capability-not-allowed:${resource.resourceId}:${request.requiredCapability}`);
  }

  if (target.workflow === "map-asset") {
    if (resource.mediaKind !== "map") {
      return unresolved(request, "incompatible-media-kind", `incompatible-media-kind:${resource.mediaKind}:map-asset`);
    }
    const asset = resolveAssetTarget(maiPackage, target.stableId, ["map-asset", "battlemap"]);
    if (!asset) return unresolved(request, "mai-target-not-found", `mai-map-asset-not-found:${target.stableId}`);
    return Object.freeze({
      ...resultBase(request),
      status: "resolved",
      maiTargetId: asset.assetId,
      maiAssetId: asset.assetId,
      maiOwnedTransform: null,
      findings: Object.freeze([]),
    });
  }

  if (target.workflow === "tileset") {
    if (resource.mediaKind !== "tileset") {
      return unresolved(request, "incompatible-media-kind", `incompatible-media-kind:${resource.mediaKind}:tileset`);
    }
    const asset = resolveAssetTarget(maiPackage, target.stableId, ["terrain-set", "tile"]);
    if (!asset) return unresolved(request, "mai-target-not-found", `mai-tileset-not-found:${target.stableId}`);
    return Object.freeze({
      ...resultBase(request),
      status: "resolved",
      maiTargetId: asset.assetId,
      maiAssetId: asset.assetId,
      maiOwnedTransform: null,
      findings: Object.freeze([]),
    });
  }

  if (target.workflow === "placeable") {
    if (!PLACEABLE_MEDIA_KINDS.has(resource.mediaKind)) {
      return unresolved(request, "incompatible-media-kind", `incompatible-media-kind:${resource.mediaKind}:placeable`);
    }
    const resolved = resolvePlaceableTarget(maiPackage, target.stableId);
    if (!resolved) return unresolved(request, "mai-target-not-found", `mai-placeable-not-found:${target.stableId}`);
    return Object.freeze({
      ...resultBase(request),
      status: "resolved",
      maiTargetId: resolved.placeable.placeableId,
      maiAssetId: resolved.asset.assetId,
      maiOwnedTransform: resolved.placeable.transform,
      findings: Object.freeze([]),
    });
  }

  if (target.stableId !== maiPackage.packageId) {
    return unresolved(request, "mai-target-not-found", `mai-package-not-found:${target.stableId}`);
  }

  const linkedAsset = maiPackage.assets.find(row => row.assetId === resource.ownerReference.stableId) ?? null;
  return Object.freeze({
    ...resultBase(request),
    status: "resolved",
    maiTargetId: maiPackage.packageId,
    maiAssetId: linkedAsset?.assetId ?? null,
    maiOwnedTransform: null,
    findings: Object.freeze([]),
  });
}

