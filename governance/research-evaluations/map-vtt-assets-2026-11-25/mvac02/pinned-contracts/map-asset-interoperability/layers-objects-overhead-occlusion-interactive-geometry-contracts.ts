import type { Mai02LayerKind, Mai02Transform } from "./canonical-map-asset-placeable-package-contracts";
import { validateMai03ProjectionDescriptor, type Mai03ProjectionDescriptor } from "./grid-coordinate-scale-projection-contracts";

export const MAI05_SCHEMA_VERSION = "1.0.0" as const;
export const MAI05_PREDECESSOR_AUTHORITY = "MAI-04" as const;
export const MAI05_SCENE_AUTHORITY = "Scene/Tabletop" as const;
export const MAI05_VISIBILITY_AUTHORITY = "Visibility/Permissions" as const;
export const MAI05_GAMEPLAY_AUTHORITY = "Combat/Exploration" as const;
export const MAI05_WORLD_AUTHORITY = "MIB-11/D18" as const;
export const MAI05_PROVENANCE_AUTHORITY = "D29-authoring-provenance" as const;

export type Mai05GeometryPrimitiveKind = "point" | "segment" | "polyline" | "polygon" | "rectangle" | "ellipse";
export type Mai05OcclusionClass = "none" | "opaque-candidate" | "mask-candidate" | "overhead-candidate";
export type Mai05InteractionHint = "none" | "door-candidate" | "trigger-candidate" | "region-candidate" | "portal-candidate" | "generic-candidate";
export type Mai05InteractionOwnerAuthority = "Scene/Tabletop" | "Combat/Exploration" | "Visibility/Permissions" | "MIB-11/D18";

export interface Mai05Point {
  readonly x: number;
  readonly y: number;
}

export interface Mai05GeometryDescriptor {
  readonly geometryId: string;
  readonly projectionId: string;
  readonly kind: Mai05GeometryPrimitiveKind;
  readonly points: readonly Mai05Point[];
  readonly widthPx: number | null;
  readonly heightPx: number | null;
  readonly sourceMetadataReference: string;
  readonly unsupportedSourceMetadata: Readonly<Record<string, unknown>>;
  readonly unsupportedMetadataPreserved: true;
  readonly createsWorldTopology: false;
  readonly createsCollisionTruth: false;
  readonly createsVisibilityTruth: false;
}

export interface Mai05LayerDescriptor {
  readonly layerId: string;
  readonly kind: Mai02LayerKind;
  readonly order: number;
  readonly elevation: number;
  readonly visibilityPolicyReference: string;
  readonly sceneOwnerReference: string;
  readonly sourceMetadataReference: string;
  readonly runtimePlacementMutationPerformed: false;
  readonly visibilityAuthorizationPerformed: false;
}

export interface Mai05PlaceableDescriptor {
  readonly placeableId: string;
  readonly layerId: string;
  readonly assetId: string;
  readonly transform: Mai02Transform;
  readonly elevation: number;
  readonly geometryReferences: readonly string[];
  readonly sourceMetadataReference: string;
  readonly runtimePlacementMutationPerformed: false;
  readonly worldIdentityCreated: false;
}

export interface Mai05OcclusionCandidate {
  readonly occlusionId: string;
  readonly geometryId: string;
  readonly occlusionClass: Mai05OcclusionClass;
  readonly visibilityPolicyReference: string;
  readonly sourceMetadataReference: string;
  readonly visibilityDecisionPerformed: false;
  readonly lineOfSightCalculated: false;
}

export interface Mai05InteractiveGeometryCandidate {
  readonly interactionId: string;
  readonly geometryId: string;
  readonly hint: Mai05InteractionHint;
  readonly ownerAuthority: Mai05InteractionOwnerAuthority | null;
  readonly ownerReference: string | null;
  readonly sourceMetadataReference: string;
  readonly runtimeStateOwnedByMai: false;
  readonly collisionDecisionPerformed: false;
  readonly movementDecisionPerformed: false;
  readonly combatEffectApplied: false;
}

export interface Mai05PresentationPackage {
  readonly packageId: string;
  readonly projection: Mai03ProjectionDescriptor;
  readonly layers: readonly Mai05LayerDescriptor[];
  readonly placeables: readonly Mai05PlaceableDescriptor[];
  readonly geometries: readonly Mai05GeometryDescriptor[];
  readonly occlusionCandidates: readonly Mai05OcclusionCandidate[];
  readonly interactiveGeometry: readonly Mai05InteractiveGeometryCandidate[];
  readonly provenanceReference: string;
  readonly unsupportedPackageMetadata: Readonly<Record<string, unknown>>;
  readonly unsupportedMetadataPreserved: true;
}

export interface Mai05ValidationResult {
  readonly accepted: boolean;
  readonly findings: readonly string[];
  readonly layerCount: number;
  readonly placeableCount: number;
  readonly geometryCount: number;
  readonly occlusionCandidateCount: number;
  readonly interactionCandidateCount: number;
  readonly sceneMutationPerformed: false;
  readonly visibilityAuthorizationPerformed: false;
  readonly lineOfSightCalculated: false;
  readonly collisionDecisionPerformed: false;
  readonly movementDecisionPerformed: false;
  readonly coverDecisionPerformed: false;
  readonly combatEffectApplied: false;
  readonly worldTopologyCreated: false;
  readonly canonicalInteractionStateCreated: false;
  readonly importerFrameworkImplemented: false;
  readonly resolverAutomationImplemented: false;
  readonly workbenchUiImplemented: false;
  readonly runtimeOwnerIntegrationImplemented: false;
  readonly licensePermissionInferred: false;
  readonly unsupportedMetadataDiscarded: false;
  readonly migration0022Reserved: false;
  readonly realMoneySpentCents: 0;
}

export interface Mai05AuthorizedProjectionInput {
  readonly visibilityProjectionReceiptId: string;
  readonly authorizedLayerIds: readonly string[];
}

const unique = (values: readonly string[]) => new Set(values).size === values.length;
const finitePoint = (point: Mai05Point) => Number.isFinite(point.x) && Number.isFinite(point.y);

export function validateMai05Geometry(geometry: Mai05GeometryDescriptor): readonly string[] {
  const findings: string[] = [];
  if (!geometry.geometryId || !geometry.projectionId || !geometry.sourceMetadataReference) findings.push("geometry-identity-or-source-missing");
  if (!geometry.points.every(finitePoint)) findings.push(`geometry-non-finite-point:${geometry.geometryId}`);
  if (geometry.unsupportedMetadataPreserved !== true) findings.push(`geometry-unsupported-metadata-boundary:${geometry.geometryId}`);
  if (geometry.createsWorldTopology !== false || geometry.createsCollisionTruth !== false || geometry.createsVisibilityTruth !== false) findings.push(`geometry-owner-boundary:${geometry.geometryId}`);

  if (geometry.kind === "point" && geometry.points.length !== 1) findings.push(`geometry-point-cardinality:${geometry.geometryId}`);
  if (geometry.kind === "segment" && geometry.points.length !== 2) findings.push(`geometry-segment-cardinality:${geometry.geometryId}`);
  if (geometry.kind === "polyline" && geometry.points.length < 2) findings.push(`geometry-polyline-cardinality:${geometry.geometryId}`);
  if (geometry.kind === "polygon" && geometry.points.length < 3) findings.push(`geometry-polygon-cardinality:${geometry.geometryId}`);
  if ((geometry.kind === "rectangle" || geometry.kind === "ellipse") && geometry.points.length !== 1) findings.push(`geometry-origin-cardinality:${geometry.geometryId}`);
  if (geometry.kind === "rectangle" || geometry.kind === "ellipse") {
    if (geometry.widthPx === null || geometry.heightPx === null || !Number.isFinite(geometry.widthPx) || !Number.isFinite(geometry.heightPx) || geometry.widthPx <= 0 || geometry.heightPx <= 0) findings.push(`geometry-dimensions:${geometry.geometryId}`);
  } else if (geometry.widthPx !== null || geometry.heightPx !== null) {
    findings.push(`geometry-unexpected-dimensions:${geometry.geometryId}`);
  }
  return findings;
}

export function validateMai05PresentationPackage(pkg: Mai05PresentationPackage): Mai05ValidationResult {
  const findings: string[] = [];
  const projectionValidation = validateMai03ProjectionDescriptor(pkg.projection);
  const layerIds = pkg.layers.map(row => row.layerId);
  const placeableIds = pkg.placeables.map(row => row.placeableId);
  const geometryIds = pkg.geometries.map(row => row.geometryId);
  const occlusionIds = pkg.occlusionCandidates.map(row => row.occlusionId);
  const interactionIds = pkg.interactiveGeometry.map(row => row.interactionId);

  if (!pkg.packageId || !pkg.provenanceReference) findings.push("package-identity-or-provenance-missing");
  if (!projectionValidation.accepted) findings.push("projection-invalid");
  if (pkg.unsupportedMetadataPreserved !== true) findings.push("package-unsupported-metadata-boundary");
  if (!unique(layerIds)) findings.push("duplicate-layer-id");
  if (!unique(placeableIds)) findings.push("duplicate-placeable-id");
  if (!unique(geometryIds)) findings.push("duplicate-geometry-id");
  if (!unique(occlusionIds)) findings.push("duplicate-occlusion-id");
  if (!unique(interactionIds)) findings.push("duplicate-interaction-id");

  pkg.layers.forEach(layer => {
    if (!layer.layerId || !layer.visibilityPolicyReference || !layer.sceneOwnerReference || !layer.sourceMetadataReference || !Number.isFinite(layer.order) || !Number.isFinite(layer.elevation)) findings.push(`layer-invalid:${layer.layerId || "unknown"}`);
    if (layer.runtimePlacementMutationPerformed !== false || layer.visibilityAuthorizationPerformed !== false) findings.push(`layer-owner-boundary:${layer.layerId}`);
  });

  pkg.geometries.forEach(geometry => {
    findings.push(...validateMai05Geometry(geometry));
    if (geometry.projectionId !== pkg.projection.projectionId) findings.push(`geometry-projection-mismatch:${geometry.geometryId}`);
  });

  pkg.placeables.forEach(placeable => {
    if (!placeable.placeableId || !layerIds.includes(placeable.layerId) || !placeable.assetId || !placeable.sourceMetadataReference || !Number.isFinite(placeable.elevation)) findings.push(`placeable-invalid:${placeable.placeableId || "unknown"}`);
    if (!placeable.geometryReferences.every(id => geometryIds.includes(id))) findings.push(`placeable-geometry-reference-missing:${placeable.placeableId}`);
    if (placeable.runtimePlacementMutationPerformed !== false || placeable.worldIdentityCreated !== false) findings.push(`placeable-owner-boundary:${placeable.placeableId}`);
  });

  pkg.occlusionCandidates.forEach(candidate => {
    if (!candidate.occlusionId || !geometryIds.includes(candidate.geometryId) || !candidate.visibilityPolicyReference || !candidate.sourceMetadataReference) findings.push(`occlusion-invalid:${candidate.occlusionId || "unknown"}`);
    if (candidate.visibilityDecisionPerformed !== false || candidate.lineOfSightCalculated !== false) findings.push(`occlusion-owner-boundary:${candidate.occlusionId}`);
  });

  pkg.interactiveGeometry.forEach(candidate => {
    if (!candidate.interactionId || !geometryIds.includes(candidate.geometryId) || !candidate.sourceMetadataReference) findings.push(`interaction-invalid:${candidate.interactionId || "unknown"}`);
    if (candidate.hint === "none" && (candidate.ownerAuthority !== null || candidate.ownerReference !== null)) findings.push(`interaction-none-owner-must-be-null:${candidate.interactionId}`);
    if (candidate.hint !== "none" && (!candidate.ownerAuthority || !candidate.ownerReference)) findings.push(`interaction-owner-reference-required:${candidate.interactionId}`);
    if (candidate.runtimeStateOwnedByMai !== false || candidate.collisionDecisionPerformed !== false || candidate.movementDecisionPerformed !== false || candidate.combatEffectApplied !== false) findings.push(`interaction-owner-boundary:${candidate.interactionId}`);
  });

  return {
    accepted: findings.length === 0,
    findings,
    layerCount: pkg.layers.length,
    placeableCount: pkg.placeables.length,
    geometryCount: pkg.geometries.length,
    occlusionCandidateCount: pkg.occlusionCandidates.length,
    interactionCandidateCount: pkg.interactiveGeometry.length,
    sceneMutationPerformed: false,
    visibilityAuthorizationPerformed: false,
    lineOfSightCalculated: false,
    collisionDecisionPerformed: false,
    movementDecisionPerformed: false,
    coverDecisionPerformed: false,
    combatEffectApplied: false,
    worldTopologyCreated: false,
    canonicalInteractionStateCreated: false,
    importerFrameworkImplemented: false,
    resolverAutomationImplemented: false,
    workbenchUiImplemented: false,
    runtimeOwnerIntegrationImplemented: false,
    licensePermissionInferred: false,
    unsupportedMetadataDiscarded: false,
    migration0022Reserved: false,
    realMoneySpentCents: 0,
  };
}

export function orderMai05Presentation(pkg: Mai05PresentationPackage) {
  const layers = [...pkg.layers].sort((left, right) => left.order - right.order || left.elevation - right.elevation || left.layerId.localeCompare(right.layerId));
  const layerRank = new Map(layers.map((layer, index) => [layer.layerId, index] as const));
  const placeables = [...pkg.placeables].sort((left, right) => (layerRank.get(left.layerId) ?? Number.MAX_SAFE_INTEGER) - (layerRank.get(right.layerId) ?? Number.MAX_SAFE_INTEGER) || left.elevation - right.elevation || left.placeableId.localeCompare(right.placeableId));
  const geometries = [...pkg.geometries].sort((left, right) => left.geometryId.localeCompare(right.geometryId));
  return {
    layers,
    placeables,
    geometries,
    sceneMutationPerformed: false as const,
    visibilityAuthorizationPerformed: false as const,
    gameplayDecisionPerformed: false as const,
  };
}

export function projectMai05AuthorizedDescriptors(pkg: Mai05PresentationPackage, input: Mai05AuthorizedProjectionInput) {
  const authorized = new Set(input.authorizedLayerIds);
  const layers = orderMai05Presentation(pkg).layers.filter(layer => authorized.has(layer.layerId));
  const layerIds = new Set(layers.map(layer => layer.layerId));
  const placeables = orderMai05Presentation(pkg).placeables.filter(placeable => layerIds.has(placeable.layerId));
  const referencedGeometryIds = new Set(placeables.flatMap(placeable => placeable.geometryReferences));
  const geometries = pkg.geometries.filter(geometry => referencedGeometryIds.has(geometry.geometryId)).sort((left, right) => left.geometryId.localeCompare(right.geometryId));
  return {
    visibilityProjectionReceiptId: input.visibilityProjectionReceiptId,
    layers,
    placeables,
    geometries,
    visibilityAuthorizationPerformed: false as const,
    lineOfSightCalculated: false as const,
    hiddenCardinalityReported: false as const,
    sceneMutationPerformed: false as const,
  };
}

export const MAI05_AUTHORITY_BOUNDARY = {
  predecessorAuthority: MAI05_PREDECESSOR_AUTHORITY,
  sceneAuthority: MAI05_SCENE_AUTHORITY,
  visibilityAuthority: MAI05_VISIBILITY_AUTHORITY,
  gameplayAuthority: MAI05_GAMEPLAY_AUTHORITY,
  worldAuthority: MAI05_WORLD_AUTHORITY,
  provenanceAuthority: MAI05_PROVENANCE_AUTHORITY,
  canonicalVendorOrEditor: null,
  descriptiveGeometryOnly: true,
  sceneMutationAllowed: false,
  visibilityAuthorizationAllowed: false,
  lineOfSightCalculationAllowed: false,
  collisionDecisionAllowed: false,
  movementDecisionAllowed: false,
  coverDecisionAllowed: false,
  combatEffectAllowed: false,
  worldTopologyCreationAllowed: false,
  canonicalInteractionStateAllowed: false,
  importerFrameworkImplemented: false,
  resolverAutomationImplemented: false,
  workbenchUiImplemented: false,
  runtimeOwnerIntegrationImplemented: false,
  migration0022Reserved: false,
  realMoneySpentCents: 0,
} as const;

