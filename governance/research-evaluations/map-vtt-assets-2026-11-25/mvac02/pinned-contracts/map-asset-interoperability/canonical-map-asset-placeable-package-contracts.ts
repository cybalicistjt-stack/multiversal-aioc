export const MAI02_SCHEMA_VERSION = "1.0.0" as const;
export const MAI02_PREDECESSOR_AUTHORITY = "MAI-01" as const;
export const MAI02_WORLD_AUTHORITY = "MIB-11/D18" as const;
export const MAI02_PROVENANCE_AUTHORITY = "D29-authoring-provenance" as const;

export type Mai02AssetKind =
  | "map-asset"
  | "tile"
  | "terrain-set"
  | "object-asset"
  | "module"
  | "battlemap";

export type Mai02LicenseEvidenceClass =
  | "explicit_public_domain"
  | "explicit_open_license"
  | "explicit_commercial_license"
  | "explicit_personal_use_only"
  | "explicit_noncommercial"
  | "attribution_required"
  | "share_alike"
  | "no_derivatives"
  | "permission_unknown"
  | "permission_unverified";

export type Mai02PermissionState = "granted" | "denied" | "unknown";
export type Mai02GridOrientation = "square" | "gridless" | "hex" | "isometric" | "staggered" | "unknown";
export type Mai02LayerKind = "background" | "terrain" | "object" | "overhead" | "annotation" | "gm-only";
export type Mai02IncompletePackOutcome =
  | "exact-compatible"
  | "cross-pack-permitted"
  | "manual-selection"
  | "approved-placeholder"
  | "visibly-unresolved";

export interface Mai02PermissionMatrix {
  readonly ingest: Mai02PermissionState;
  readonly useInExperience: Mai02PermissionState;
  readonly transform: Mai02PermissionState;
  readonly substitute: Mai02PermissionState;
  readonly redistribute: Mai02PermissionState;
}

export interface Mai02SourceProvenance {
  readonly sourceId: string;
  readonly sourceReference: string;
  readonly checksumSha256: string;
  readonly licenseEvidenceClass: Mai02LicenseEvidenceClass;
  readonly licenseEvidenceReference: string;
  readonly permissions: Mai02PermissionMatrix;
  readonly importLineage: readonly string[];
  readonly unsupportedMetadata: Readonly<Record<string, unknown>>;
  readonly unsupportedMetadataPreserved: true;
  readonly permissionsInferred: false;
}

export interface Mai02Dimensions {
  readonly widthPx: number;
  readonly heightPx: number;
}

export interface Mai02Transform {
  readonly offsetXPx: number;
  readonly offsetYPx: number;
  readonly rotationDegrees: number;
  readonly scaleX: number;
  readonly scaleY: number;
  readonly flipX: boolean;
  readonly flipY: boolean;
}

export interface Mai02Anchor {
  readonly xRatio: number;
  readonly yRatio: number;
}

export interface Mai02GridDescriptor {
  readonly orientation: Mai02GridOrientation;
  readonly cellWidthPx: number | null;
  readonly cellHeightPx: number | null;
  readonly sourceMetadataReference: string | null;
  readonly projectionEngineApplied: false;
}

export interface Mai02AnimationDescriptor {
  readonly frameReferences: readonly string[];
  readonly frameDurationMs: readonly number[];
  readonly looping: boolean;
  readonly runtimeControllerImplemented: false;
}

export interface Mai02VariantReference {
  readonly variantId: string;
  readonly label: string;
  readonly sourceAssetId: string;
}

export interface Mai02DependencyReference {
  readonly dependencyId: string;
  readonly dependencyKind: "asset" | "package" | "external-owner";
  readonly required: boolean;
  readonly resolutionAutomated: false;
}

export interface Mai02OwnerReference {
  readonly ownerAuthority: "MIB-11/D18" | "Scene/Tabletop" | "Combat/Exploration" | "Visibility/Permissions" | "D29-authoring-provenance";
  readonly stableId: string;
  readonly versionReference: string | null;
  readonly mai02MayMutate: false;
}

export interface Mai02AssetRecord {
  readonly assetId: string;
  readonly kind: Mai02AssetKind;
  readonly label: string;
  readonly dimensions: Mai02Dimensions;
  readonly anchor: Mai02Anchor;
  readonly grid: Mai02GridDescriptor;
  readonly elevationReference: number | null;
  readonly variants: readonly Mai02VariantReference[];
  readonly animation: Mai02AnimationDescriptor | null;
  readonly dependencies: readonly Mai02DependencyReference[];
  readonly provenance: Mai02SourceProvenance;
  readonly ownerReferences: readonly Mai02OwnerReference[];
  readonly semanticWorldIdentityOwnedByMai: false;
}

export interface Mai02LayerRecord {
  readonly layerId: string;
  readonly battlemapAssetId: string;
  readonly kind: Mai02LayerKind;
  readonly order: number;
  readonly visibilityReference: string;
  readonly transform: Mai02Transform;
  readonly sourceMetadata: Readonly<Record<string, unknown>>;
  readonly runtimeOcclusionImplemented: false;
}

export interface Mai02PlaceableRecord {
  readonly placeableId: string;
  readonly layerId: string;
  readonly assetId: string;
  readonly transform: Mai02Transform;
  readonly elevationReference: number | null;
  readonly ownerReferences: readonly Mai02OwnerReference[];
  readonly interactionRuntimeImplemented: false;
  readonly worldIdentityCreated: false;
}

export interface Mai02SemanticRequirementBinding {
  readonly requirementId: string;
  readonly semanticReference: string;
  readonly outcome: Mai02IncompletePackOutcome;
  readonly selectedAssetId: string | null;
  readonly evidenceReference: string;
  readonly resolverAutomationPerformed: false;
}

export interface Mai02AssetPackage {
  readonly packageId: string;
  readonly version: string;
  readonly sourceReferences: readonly Mai02SourceProvenance[];
  readonly assets: readonly Mai02AssetRecord[];
  readonly layers: readonly Mai02LayerRecord[];
  readonly placeables: readonly Mai02PlaceableRecord[];
  readonly semanticBindings: readonly Mai02SemanticRequirementBinding[];
  readonly unsupportedPackageMetadata: Readonly<Record<string, unknown>>;
  readonly unsupportedMetadataPreserved: true;
}

export interface Mai02ValidationResult {
  readonly accepted: boolean;
  readonly findings: readonly string[];
  readonly assetCount: number;
  readonly layerCount: number;
  readonly placeableCount: number;
  readonly semanticBindingCount: number;
  readonly ownerMutationPerformed: false;
  readonly worldTruthCreatedFromArtwork: false;
  readonly licensePermissionInferred: false;
  readonly unsupportedMetadataDiscarded: false;
  readonly projectionEngineImplemented: false;
  readonly autotileEngineImplemented: false;
  readonly occlusionRuntimeImplemented: false;
  readonly importerFrameworkImplemented: false;
  readonly resolverAutomationImplemented: false;
  readonly workbenchUiImplemented: false;
  readonly runtimeOwnerIntegrationImplemented: false;
  readonly migration0022Reserved: false;
  readonly realMoneySpentCents: 0;
}

const EXPECTED_ASSET_KINDS: readonly Mai02AssetKind[] = [
  "map-asset",
  "tile",
  "terrain-set",
  "object-asset",
  "module",
  "battlemap",
];

const EXPECTED_OUTCOMES: readonly Mai02IncompletePackOutcome[] = [
  "exact-compatible",
  "cross-pack-permitted",
  "manual-selection",
  "approved-placeholder",
  "visibly-unresolved",
];

const isSha256 = (value: string) => /^[a-f0-9]{64}$/i.test(value);
const unique = (values: readonly string[]) => new Set(values).size === values.length;
const inUnitRange = (value: number) => Number.isFinite(value) && value >= 0 && value <= 1;

export function validateMai02AssetPackage(pkg: Mai02AssetPackage): Mai02ValidationResult {
  const findings: string[] = [];
  const assetIds = pkg.assets.map(row => row.assetId);
  const layerIds = pkg.layers.map(row => row.layerId);
  const placeableIds = pkg.placeables.map(row => row.placeableId);
  const assetKinds = pkg.assets.map(row => row.kind);
  const outcomes = pkg.semanticBindings.map(row => row.outcome);

  if (!pkg.packageId || !pkg.version) findings.push("package-identity-missing");
  if (!unique(assetIds)) findings.push("duplicate-asset-id");
  if (!unique(layerIds)) findings.push("duplicate-layer-id");
  if (!unique(placeableIds)) findings.push("duplicate-placeable-id");
  if (!EXPECTED_ASSET_KINDS.every(kind => assetKinds.includes(kind))) findings.push("canonical-asset-kind-coverage-missing");
  if (!EXPECTED_OUTCOMES.every(outcome => outcomes.includes(outcome))) findings.push("incomplete-pack-outcome-coverage-missing");
  if (pkg.unsupportedMetadataPreserved !== true) findings.push("package-unsupported-metadata-boundary");

  pkg.sourceReferences.forEach(source => {
    if (!source.sourceId || !source.sourceReference || !isSha256(source.checksumSha256) || !source.licenseEvidenceReference) findings.push(`source-provenance-incomplete:${source.sourceId || "unknown"}`);
    if (source.unsupportedMetadataPreserved !== true || source.permissionsInferred !== false) findings.push(`source-boundary:${source.sourceId}`);
  });

  pkg.assets.forEach(asset => {
    if (!asset.assetId || !asset.label || asset.dimensions.widthPx <= 0 || asset.dimensions.heightPx <= 0) findings.push(`asset-identity-or-dimensions:${asset.assetId}`);
    if (!inUnitRange(asset.anchor.xRatio) || !inUnitRange(asset.anchor.yRatio)) findings.push(`asset-anchor-range:${asset.assetId}`);
    if (asset.grid.projectionEngineApplied !== false) findings.push(`asset-projection-boundary:${asset.assetId}`);
    if (asset.animation?.runtimeControllerImplemented !== false && asset.animation !== null) findings.push(`asset-animation-runtime-boundary:${asset.assetId}`);
    if (asset.dependencies.some(dep => dep.resolutionAutomated !== false)) findings.push(`asset-dependency-resolution-boundary:${asset.assetId}`);
    if (asset.ownerReferences.some(ref => ref.mai02MayMutate !== false)) findings.push(`asset-owner-mutation-boundary:${asset.assetId}`);
    if (asset.semanticWorldIdentityOwnedByMai !== false) findings.push(`asset-world-authority-boundary:${asset.assetId}`);
    if (!pkg.sourceReferences.some(source => source.sourceId === asset.provenance.sourceId)) findings.push(`asset-source-reference-missing:${asset.assetId}`);
  });

  pkg.layers.forEach(layer => {
    if (!assetIds.includes(layer.battlemapAssetId)) findings.push(`layer-battlemap-reference-missing:${layer.layerId}`);
    if (!layer.visibilityReference || layer.order < 0 || layer.runtimeOcclusionImplemented !== false) findings.push(`layer-boundary:${layer.layerId}`);
  });

  pkg.placeables.forEach(placeable => {
    if (!layerIds.includes(placeable.layerId) || !assetIds.includes(placeable.assetId)) findings.push(`placeable-reference-missing:${placeable.placeableId}`);
    if (placeable.ownerReferences.some(ref => ref.mai02MayMutate !== false) || placeable.interactionRuntimeImplemented !== false || placeable.worldIdentityCreated !== false) findings.push(`placeable-owner-boundary:${placeable.placeableId}`);
  });

  pkg.semanticBindings.forEach(binding => {
    if (!binding.requirementId || !binding.semanticReference || !binding.evidenceReference || binding.resolverAutomationPerformed !== false) findings.push(`semantic-binding-boundary:${binding.requirementId}`);
    if (binding.selectedAssetId !== null && !assetIds.includes(binding.selectedAssetId)) findings.push(`semantic-binding-asset-missing:${binding.requirementId}`);
    if (binding.outcome === "visibly-unresolved" && binding.selectedAssetId !== null) findings.push(`unresolved-binding-must-not-select-asset:${binding.requirementId}`);
  });

  return {
    accepted: findings.length === 0,
    findings,
    assetCount: pkg.assets.length,
    layerCount: pkg.layers.length,
    placeableCount: pkg.placeables.length,
    semanticBindingCount: pkg.semanticBindings.length,
    ownerMutationPerformed: false,
    worldTruthCreatedFromArtwork: false,
    licensePermissionInferred: false,
    unsupportedMetadataDiscarded: false,
    projectionEngineImplemented: false,
    autotileEngineImplemented: false,
    occlusionRuntimeImplemented: false,
    importerFrameworkImplemented: false,
    resolverAutomationImplemented: false,
    workbenchUiImplemented: false,
    runtimeOwnerIntegrationImplemented: false,
    migration0022Reserved: false,
    realMoneySpentCents: 0,
  };
}

export function previewMai02Package(pkg: Mai02AssetPackage, authorizedVisibilityReferences: readonly string[]) {
  const visibleLayers = pkg.layers.filter(layer => authorizedVisibilityReferences.includes(layer.visibilityReference));
  const visibleLayerIds = new Set(visibleLayers.map(layer => layer.layerId));
  const visiblePlaceables = pkg.placeables.filter(placeable => visibleLayerIds.has(placeable.layerId));
  return {
    packageId: pkg.packageId,
    visibleLayers,
    visiblePlaceables,
    semanticBindings: pkg.semanticBindings,
    ownerMutationPerformed: false as const,
    worldTruthCreatedFromArtwork: false as const,
    resolverAutomationPerformed: false as const,
    runtimeStateChanged: false as const,
  };
}

export const MAI02_AUTHORITY_BOUNDARY = {
  predecessorAuthority: MAI02_PREDECESSOR_AUTHORITY,
  worldAuthority: MAI02_WORLD_AUTHORITY,
  provenanceAuthority: MAI02_PROVENANCE_AUTHORITY,
  canonicalVendorOrEditor: null,
  canonicalAssetKinds: EXPECTED_ASSET_KINDS,
  incompletePackOutcomes: EXPECTED_OUTCOMES,
  permissionInferenceAllowed: false,
  unsupportedMetadataDiscardAllowed: false,
  artworkOrCoordinatesAreWorldTruth: false,
  ownerMutationAllowed: false,
  projectionEngineImplemented: false,
  autotileEngineImplemented: false,
  occlusionRuntimeImplemented: false,
  importerFrameworkImplemented: false,
  resolverAutomationImplemented: false,
  workbenchUiImplemented: false,
  runtimeOwnerIntegrationImplemented: false,
  migration0022Reserved: false,
  realMoneySpentCents: 0,
} as const;

