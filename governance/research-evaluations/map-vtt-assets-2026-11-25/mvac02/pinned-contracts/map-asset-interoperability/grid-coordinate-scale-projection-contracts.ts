import type {
  Mai02Anchor,
  Mai02Dimensions,
  Mai02GridDescriptor,
  Mai02Transform,
} from "./canonical-map-asset-placeable-package-contracts";

export const MAI03_SCHEMA_VERSION = "1.0.0" as const;
export const MAI03_PREDECESSOR_AUTHORITY = "MAI-02" as const;
export const MAI03_WORLD_AUTHORITY = "MIB-11/D18" as const;
export const MAI03_PROVENANCE_AUTHORITY = "D29-authoring-provenance" as const;
export const MAI03_ROUND_TRIP_TOLERANCE = 1e-9 as const;

export type Mai03CoordinateSpace =
  | "asset-local-pixel"
  | "map-pixel"
  | "grid-coordinate"
  | "normalized-map";

export type Mai03ProjectionOrientation = "square" | "gridless" | "hex" | "isometric" | "staggered";
export type Mai03HexAxisOrientation = "flat" | "point";
export type Mai03StaggerAxis = "x" | "y";
export type Mai03StaggerIndex = "odd" | "even";

export interface Mai03Point {
  readonly x: number;
  readonly y: number;
}

export interface Mai03GridCoordinate {
  readonly x: number;
  readonly y: number;
}

export interface Mai03ProjectionDescriptor {
  readonly projectionId: string;
  readonly orientation: Mai03ProjectionOrientation;
  readonly originPx: Mai03Point;
  readonly cellWidthPx: number | null;
  readonly cellHeightPx: number | null;
  readonly hexAxisOrientation: Mai03HexAxisOrientation | null;
  readonly staggerAxis: Mai03StaggerAxis | null;
  readonly staggerIndex: Mai03StaggerIndex | null;
  readonly mapDimensions: Mai02Dimensions;
  readonly sourceGridReference: Mai02GridDescriptor;
  readonly canonicalVendorOrEditor: null;
  readonly createsWorldTruth: false;
  readonly createsCombatIdentity: false;
  readonly connectivityGrammarApplied: false;
  readonly runtimeGeometryApplied: false;
}

export interface Mai03ScaleDescriptor {
  readonly scaleId: string;
  readonly pixelsPerUnit: number;
  readonly unitLabel: string;
  readonly authorityReference: string | null;
  readonly worldDistanceAuthority: false;
}

export interface Mai03ValidationResult {
  readonly accepted: boolean;
  readonly findings: readonly string[];
  readonly ownerMutationPerformed: false;
  readonly worldTruthCreatedFromCoordinates: false;
  readonly combatIdentityCreatedFromCoordinates: false;
  readonly vendorCanonicalized: false;
  readonly licensePermissionInferred: false;
  readonly unsupportedMetadataDiscarded: false;
  readonly autotileConnectivityImplemented: false;
  readonly runtimeGeometryImplemented: false;
  readonly importerFrameworkImplemented: false;
  readonly resolverAutomationImplemented: false;
  readonly workbenchUiImplemented: false;
  readonly runtimeOwnerIntegrationImplemented: false;
  readonly migration0022Reserved: false;
  readonly realMoneySpentCents: 0;
}

export interface Mai03ProjectionResult<T> {
  readonly accepted: boolean;
  readonly value: T | null;
  readonly findings: readonly string[];
  readonly ownerMutationPerformed: false;
  readonly worldTruthCreatedFromCoordinates: false;
  readonly runtimeStateChanged: false;
}

const finite = (value: number) => Number.isFinite(value);
const positive = (value: number | null): value is number => value !== null && finite(value) && value > 0;

export function validateMai03ProjectionDescriptor(descriptor: Mai03ProjectionDescriptor): Mai03ValidationResult {
  const findings: string[] = [];
  if (!descriptor.projectionId) findings.push("projection-id-missing");
  if (!finite(descriptor.originPx.x) || !finite(descriptor.originPx.y)) findings.push("projection-origin-invalid");
  if (!(descriptor.mapDimensions.widthPx > 0) || !(descriptor.mapDimensions.heightPx > 0)) findings.push("map-dimensions-invalid");
  if (descriptor.canonicalVendorOrEditor !== null) findings.push("vendor-canonicalization-forbidden");
  if (descriptor.createsWorldTruth !== false || descriptor.createsCombatIdentity !== false) findings.push("owner-authority-boundary");
  if (descriptor.connectivityGrammarApplied !== false) findings.push("mai04-connectivity-boundary");
  if (descriptor.runtimeGeometryApplied !== false) findings.push("mai05-runtime-geometry-boundary");

  if (descriptor.orientation === "gridless") {
    if (descriptor.cellWidthPx !== null || descriptor.cellHeightPx !== null) findings.push("gridless-cell-dimensions-must-be-null");
    if (descriptor.hexAxisOrientation !== null || descriptor.staggerAxis !== null || descriptor.staggerIndex !== null) findings.push("gridless-orientation-metadata-forbidden");
  } else {
    if (!positive(descriptor.cellWidthPx) || !positive(descriptor.cellHeightPx)) findings.push("cell-dimensions-invalid");
  }

  if (descriptor.orientation === "hex") {
    if (descriptor.hexAxisOrientation === null) findings.push("hex-axis-orientation-required");
  } else if (descriptor.hexAxisOrientation !== null) {
    findings.push("hex-axis-orientation-not-applicable");
  }

  if (descriptor.orientation === "staggered") {
    if (descriptor.staggerAxis === null || descriptor.staggerIndex === null) findings.push("stagger-metadata-required");
  } else if (descriptor.staggerAxis !== null || descriptor.staggerIndex !== null) {
    findings.push("stagger-metadata-not-applicable");
  }

  if (descriptor.sourceGridReference.orientation === "unknown") findings.push("source-grid-orientation-unresolved");

  return {
    accepted: findings.length === 0,
    findings,
    ownerMutationPerformed: false,
    worldTruthCreatedFromCoordinates: false,
    combatIdentityCreatedFromCoordinates: false,
    vendorCanonicalized: false,
    licensePermissionInferred: false,
    unsupportedMetadataDiscarded: false,
    autotileConnectivityImplemented: false,
    runtimeGeometryImplemented: false,
    importerFrameworkImplemented: false,
    resolverAutomationImplemented: false,
    workbenchUiImplemented: false,
    runtimeOwnerIntegrationImplemented: false,
    migration0022Reserved: false,
    realMoneySpentCents: 0,
  };
}

function result(value: null, findings?: readonly string[]): Mai03ProjectionResult<never>;
function result<T>(value: T, findings?: readonly string[]): Mai03ProjectionResult<T>;
function result<T>(value: T | null, findings: readonly string[] = []): Mai03ProjectionResult<T> {
  return {
    accepted: findings.length === 0,
    value,
    findings,
    ownerMutationPerformed: false,
    worldTruthCreatedFromCoordinates: false,
    runtimeStateChanged: false,
  };
}

const gridCellDimensions = (descriptor: Mai03ProjectionDescriptor) => {
  if (!positive(descriptor.cellWidthPx) || !positive(descriptor.cellHeightPx)) return null;
  return { width: descriptor.cellWidthPx, height: descriptor.cellHeightPx };
};

export function projectGridCoordinateToMapPixel(
  descriptor: Mai03ProjectionDescriptor,
  coordinate: Mai03GridCoordinate,
): Mai03ProjectionResult<Mai03Point> {
  const validation = validateMai03ProjectionDescriptor(descriptor);
  if (!validation.accepted) return result(null, validation.findings);
  if (!finite(coordinate.x) || !finite(coordinate.y)) return result(null, ["grid-coordinate-invalid"]);
  if (descriptor.orientation === "gridless") return result(null, ["grid-coordinate-not-defined-for-gridless"]);
  const cell = gridCellDimensions(descriptor);
  if (!cell) return result(null, ["cell-dimensions-invalid"]);
  const { x: ox, y: oy } = descriptor.originPx;
  const gx = coordinate.x;
  const gy = coordinate.y;

  switch (descriptor.orientation) {
    case "square":
      return result({ x: ox + gx * cell.width, y: oy + gy * cell.height });
    case "hex":
      if (descriptor.hexAxisOrientation === "point") {
        return result({ x: ox + cell.width * (gx + gy / 2), y: oy + cell.height * 0.75 * gy });
      }
      return result({ x: ox + cell.width * 0.75 * gx, y: oy + cell.height * (gy + gx / 2) });
    case "isometric":
      return result({ x: ox + (gx - gy) * cell.width / 2, y: oy + (gx + gy) * cell.height / 2 });
    case "staggered": {
      const sign = descriptor.staggerIndex === "odd" ? 1 : -1;
      if (descriptor.staggerAxis === "y") {
        return result({ x: ox + gx * cell.width + gy * cell.width * 0.5 * sign, y: oy + gy * cell.height * 0.5 });
      }
      return result({ x: ox + gx * cell.width * 0.5, y: oy + gy * cell.height + gx * cell.height * 0.5 * sign });
    }
    default:
      return result(null, ["projection-orientation-unsupported"]);
  }
}

export function unprojectMapPixelToGridCoordinate(
  descriptor: Mai03ProjectionDescriptor,
  point: Mai03Point,
): Mai03ProjectionResult<Mai03GridCoordinate> {
  const validation = validateMai03ProjectionDescriptor(descriptor);
  if (!validation.accepted) return result(null, validation.findings);
  if (!finite(point.x) || !finite(point.y)) return result(null, ["map-pixel-invalid"]);
  if (descriptor.orientation === "gridless") return result(null, ["grid-coordinate-not-defined-for-gridless"]);
  const cell = gridCellDimensions(descriptor);
  if (!cell) return result(null, ["cell-dimensions-invalid"]);
  const dx = point.x - descriptor.originPx.x;
  const dy = point.y - descriptor.originPx.y;

  switch (descriptor.orientation) {
    case "square":
      return result({ x: dx / cell.width, y: dy / cell.height });
    case "hex":
      if (descriptor.hexAxisOrientation === "point") {
        const gy = dy / (cell.height * 0.75);
        return result({ x: dx / cell.width - gy / 2, y: gy });
      } else {
        const gx = dx / (cell.width * 0.75);
        return result({ x: gx, y: dy / cell.height - gx / 2 });
      }
    case "isometric":
      return result({ x: dx / cell.width + dy / cell.height, y: dy / cell.height - dx / cell.width });
    case "staggered": {
      const sign = descriptor.staggerIndex === "odd" ? 1 : -1;
      if (descriptor.staggerAxis === "y") {
        const gy = (2 * dy) / cell.height;
        return result({ x: (dx - gy * cell.width * 0.5 * sign) / cell.width, y: gy });
      }
      const gx = (2 * dx) / cell.width;
      return result({ x: gx, y: (dy - gx * cell.height * 0.5 * sign) / cell.height });
    }
    default:
      return result(null, ["projection-orientation-unsupported"]);
  }
}

export function projectAssetLocalToMapPixel(
  point: Mai03Point,
  dimensions: Mai02Dimensions,
  anchor: Mai02Anchor,
  transform: Mai02Transform,
): Mai03ProjectionResult<Mai03Point> {
  if (![point.x, point.y, dimensions.widthPx, dimensions.heightPx, anchor.xRatio, anchor.yRatio, transform.offsetXPx, transform.offsetYPx, transform.rotationDegrees, transform.scaleX, transform.scaleY].every(finite)) {
    return result(null, ["asset-transform-input-invalid"]);
  }
  if (dimensions.widthPx <= 0 || dimensions.heightPx <= 0 || transform.scaleX === 0 || transform.scaleY === 0) return result(null, ["asset-transform-noninvertible"]);
  const anchorX = dimensions.widthPx * anchor.xRatio;
  const anchorY = dimensions.heightPx * anchor.yRatio;
  const flipX = transform.flipX ? -1 : 1;
  const flipY = transform.flipY ? -1 : 1;
  const sx = (point.x - anchorX) * transform.scaleX * flipX;
  const sy = (point.y - anchorY) * transform.scaleY * flipY;
  const radians = transform.rotationDegrees * Math.PI / 180;
  const cos = Math.cos(radians);
  const sin = Math.sin(radians);
  return result({
    x: transform.offsetXPx + sx * cos - sy * sin,
    y: transform.offsetYPx + sx * sin + sy * cos,
  });
}

export function unprojectMapPixelToAssetLocal(
  point: Mai03Point,
  dimensions: Mai02Dimensions,
  anchor: Mai02Anchor,
  transform: Mai02Transform,
): Mai03ProjectionResult<Mai03Point> {
  if (![point.x, point.y, dimensions.widthPx, dimensions.heightPx, anchor.xRatio, anchor.yRatio, transform.offsetXPx, transform.offsetYPx, transform.rotationDegrees, transform.scaleX, transform.scaleY].every(finite)) {
    return result(null, ["asset-transform-input-invalid"]);
  }
  if (dimensions.widthPx <= 0 || dimensions.heightPx <= 0 || transform.scaleX === 0 || transform.scaleY === 0) return result(null, ["asset-transform-noninvertible"]);
  const dx = point.x - transform.offsetXPx;
  const dy = point.y - transform.offsetYPx;
  const radians = -transform.rotationDegrees * Math.PI / 180;
  const cos = Math.cos(radians);
  const sin = Math.sin(radians);
  const rx = dx * cos - dy * sin;
  const ry = dx * sin + dy * cos;
  const flipX = transform.flipX ? -1 : 1;
  const flipY = transform.flipY ? -1 : 1;
  return result({
    x: rx / (transform.scaleX * flipX) + dimensions.widthPx * anchor.xRatio,
    y: ry / (transform.scaleY * flipY) + dimensions.heightPx * anchor.yRatio,
  });
}

export function mapPixelToNormalized(point: Mai03Point, dimensions: Mai02Dimensions): Mai03ProjectionResult<Mai03Point> {
  if (!finite(point.x) || !finite(point.y) || dimensions.widthPx <= 0 || dimensions.heightPx <= 0) return result(null, ["normalized-map-input-invalid"]);
  return result({ x: point.x / dimensions.widthPx, y: point.y / dimensions.heightPx });
}

export function normalizedToMapPixel(point: Mai03Point, dimensions: Mai02Dimensions): Mai03ProjectionResult<Mai03Point> {
  if (!finite(point.x) || !finite(point.y) || dimensions.widthPx <= 0 || dimensions.heightPx <= 0) return result(null, ["normalized-map-input-invalid"]);
  return result({ x: point.x * dimensions.widthPx, y: point.y * dimensions.heightPx });
}

export function mapPixelsToScaleUnits(pixels: number, scale: Mai03ScaleDescriptor): Mai03ProjectionResult<number> {
  if (!finite(pixels) || !finite(scale.pixelsPerUnit) || scale.pixelsPerUnit <= 0 || !scale.unitLabel || scale.worldDistanceAuthority !== false) {
    return result(null, ["scale-descriptor-invalid"]);
  }
  return result(pixels / scale.pixelsPerUnit);
}

export function scaleUnitsToMapPixels(units: number, scale: Mai03ScaleDescriptor): Mai03ProjectionResult<number> {
  if (!finite(units) || !finite(scale.pixelsPerUnit) || scale.pixelsPerUnit <= 0 || !scale.unitLabel || scale.worldDistanceAuthority !== false) {
    return result(null, ["scale-descriptor-invalid"]);
  }
  return result(units * scale.pixelsPerUnit);
}

export function withinMai03Tolerance(a: number, b: number, tolerance = MAI03_ROUND_TRIP_TOLERANCE) {
  return finite(a) && finite(b) && finite(tolerance) && tolerance >= 0 && Math.abs(a - b) <= tolerance;
}

export const MAI03_AUTHORITY_BOUNDARY = {
  predecessorAuthority: MAI03_PREDECESSOR_AUTHORITY,
  worldAuthority: MAI03_WORLD_AUTHORITY,
  provenanceAuthority: MAI03_PROVENANCE_AUTHORITY,
  coordinateSpaces: ["asset-local-pixel", "map-pixel", "grid-coordinate", "normalized-map"] as const,
  projectionOrientations: ["square", "gridless", "hex", "isometric", "staggered"] as const,
  hexAxisOrientations: ["flat", "point"] as const,
  canonicalVendorOrEditor: null,
  worldTruthFromCoordinatesAllowed: false,
  combatIdentityFromCoordinatesAllowed: false,
  ownerMutationAllowed: false,
  licensePermissionInferenceAllowed: false,
  unsupportedMetadataDiscardAllowed: false,
  autotileConnectivityImplemented: false,
  runtimeGeometryImplemented: false,
  importerFrameworkImplemented: false,
  resolverAutomationImplemented: false,
  workbenchUiImplemented: false,
  runtimeOwnerIntegrationImplemented: false,
  migration0022Reserved: false,
  realMoneySpentCents: 0,
} as const;

