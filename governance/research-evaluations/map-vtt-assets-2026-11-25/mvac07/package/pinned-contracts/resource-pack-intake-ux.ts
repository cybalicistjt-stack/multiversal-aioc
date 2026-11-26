import type { Ari06MediaType } from "./recursive-discovery-media-classification";
import {
  evaluateAri11Capability,
  type Ari11Capability,
  type Ari11UseCapabilityMatrix,
} from "./rights-license-use-capability-matrix";

export const ARI20_SOURCE_SELECTION_METHODS = ["drop", "file-picker", "folder-picker"] as const;

export type Ari20SourceSelectionMethod = (typeof ARI20_SOURCE_SELECTION_METHODS)[number];

export interface Ari20IntakeSource {
  readonly kind: "archive" | "folder" | "files";
  readonly displayName: string;
}

export interface Ari20IntakeCandidate {
  readonly resourceId: string;
  readonly path: string;
  readonly mediaType: Ari06MediaType;
  readonly duplicateOf: string | null;
  readonly familyIds: readonly string[];
  readonly provenanceRef: string | null;
  readonly rights: Ari11UseCapabilityMatrix;
}

export interface Ari20IntakePreviewInput {
  readonly source: Ari20IntakeSource;
  readonly candidates: readonly Ari20IntakeCandidate[];
  readonly requiredCapability: Ari11Capability;
}

export interface Ari20IntakePreviewItem {
  readonly resourceId: string;
  readonly path: string;
  readonly mediaType: Ari06MediaType;
  readonly duplicateOf: string | null;
  readonly familyIds: readonly string[];
  readonly provenanceRef: string | null;
  readonly eligible: boolean;
  readonly blockers: readonly string[];
}

export interface Ari20FamilyPreview {
  readonly familyId: string;
  readonly resourceIds: readonly string[];
  readonly eligibleResourceIds: readonly string[];
}

export interface Ari20IntakeSummary {
  readonly discoveredCount: number;
  readonly eligibleCount: number;
  readonly blockedCount: number;
  readonly duplicateCount: number;
  readonly unsupportedCount: number;
  readonly rightsBlockedCount: number;
  readonly provenanceBlockedCount: number;
  readonly familyCount: number;
}

export interface Ari20IntakePreview {
  readonly source: Ari20IntakeSource;
  readonly requiredCapability: Ari11Capability;
  readonly items: readonly Ari20IntakePreviewItem[];
  readonly families: readonly Ari20FamilyPreview[];
  readonly summary: Ari20IntakeSummary;
  readonly canonicalAcceptancePerformed: false;
  readonly sourceTruthMutated: false;
}

export interface Ari20BulkAcceptancePlan {
  readonly selectedResourceIds: readonly string[];
  readonly findings: readonly string[];
  readonly canonicalAcceptancePerformed: false;
  readonly sourceTruthMutated: false;
}

export const ARI20_AUTHORITY_BOUNDARY = Object.freeze({
  archiveExtractionAuthorized: false,
  discoveryTruthMutationAuthorized: false,
  provenanceMutationAuthorized: false,
  rightsMutationAuthorized: false,
  canonicalAcceptanceAuthorized: false,
  providerEntitlementAuthorized: false,
  releaseOrDeploymentAuthorized: false,
} as const);

function compareText(a: string, b: string): number {
  return a < b ? -1 : a > b ? 1 : 0;
}

function blockersFor(candidate: Ari20IntakeCandidate, requiredCapability: Ari11Capability): string[] {
  const blockers: string[] = [];
  if (candidate.duplicateOf) blockers.push(`duplicate:${candidate.duplicateOf}`);
  if (candidate.mediaType === "unknown") blockers.push(`unsupported-media:${candidate.mediaType}`);
  if (!candidate.provenanceRef) blockers.push("provenance:missing");

  const capability = evaluateAri11Capability(candidate.rights, requiredCapability);
  if (!capability.allowed) blockers.push(`rights:${requiredCapability}:${capability.state}`);
  return blockers;
}

export function buildAri20IntakePreview(input: Ari20IntakePreviewInput): Ari20IntakePreview {
  const items: Ari20IntakePreviewItem[] = input.candidates.map(candidate => {
    const blockers = blockersFor(candidate, input.requiredCapability);
    return {
      resourceId: candidate.resourceId,
      path: candidate.path,
      mediaType: candidate.mediaType,
      duplicateOf: candidate.duplicateOf,
      familyIds: [...candidate.familyIds],
      provenanceRef: candidate.provenanceRef,
      eligible: blockers.length === 0,
      blockers,
    };
  });

  const familyMembers = new Map<string, Ari20IntakePreviewItem[]>();
  for (const item of items) {
    for (const familyId of item.familyIds) {
      const members = familyMembers.get(familyId) ?? [];
      members.push(item);
      familyMembers.set(familyId, members);
    }
  }

  const families = [...familyMembers.entries()]
    .sort(([left], [right]) => compareText(left, right))
    .map(([familyId, members]) => ({
      familyId,
      resourceIds: members.map(member => member.resourceId).sort(compareText),
      eligibleResourceIds: members.filter(member => member.eligible).map(member => member.resourceId).sort(compareText),
    }));

  const duplicateCount = items.filter(item => item.duplicateOf !== null).length;
  const unsupportedCount = items.filter(item => item.mediaType === "unknown").length;
  const rightsBlockedCount = items.filter(item => item.blockers.some(blocker => blocker.startsWith("rights:"))).length;
  const provenanceBlockedCount = items.filter(item => item.blockers.includes("provenance:missing")).length;
  const eligibleCount = items.filter(item => item.eligible).length;

  return {
    source: { ...input.source },
    requiredCapability: input.requiredCapability,
    items,
    families,
    summary: {
      discoveredCount: items.length,
      eligibleCount,
      blockedCount: items.length - eligibleCount,
      duplicateCount,
      unsupportedCount,
      rightsBlockedCount,
      provenanceBlockedCount,
      familyCount: families.length,
    },
    canonicalAcceptancePerformed: false,
    sourceTruthMutated: false,
  };
}

export function planAri20BulkAcceptance(
  preview: Ari20IntakePreview,
  requestedResourceIds: readonly string[],
): Ari20BulkAcceptancePlan {
  const byId = new Map(preview.items.map(item => [item.resourceId, item] as const));
  const selectedResourceIds: string[] = [];
  const findings: string[] = [];
  const seen = new Set<string>();

  for (const resourceId of requestedResourceIds) {
    if (seen.has(resourceId)) continue;
    seen.add(resourceId);
    const item = byId.get(resourceId);
    if (!item) {
      findings.push(`unknown-selection:${resourceId}`);
      continue;
    }
    if (!item.eligible) {
      findings.push(`blocked-selection:${resourceId}:${item.blockers.join("|")}`);
      continue;
    }
    selectedResourceIds.push(resourceId);
  }

  return {
    selectedResourceIds,
    findings,
    canonicalAcceptancePerformed: false,
    sourceTruthMutated: false,
  };
}
