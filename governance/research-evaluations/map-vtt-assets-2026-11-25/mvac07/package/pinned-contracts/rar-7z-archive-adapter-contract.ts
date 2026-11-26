export const ARI05_SCHEMA_VERSION = "1.0.0" as const;

export type Ari05ArchiveFormat = "rar" | "seven_zip";

export interface Ari05RuntimeCapability {
  readonly available: boolean;
  readonly diagnostic: string;
}

export interface Ari05ArchiveCapability extends Ari05RuntimeCapability {
  readonly format: Ari05ArchiveFormat;
}

export interface Ari05ArchiveStageRequest {
  readonly format: Ari05ArchiveFormat;
  readonly bytes: Uint8Array;
  readonly signal?: AbortSignal;
}

export interface Ari05StagedArchiveEntry {
  readonly path: string;
  readonly bytes: Uint8Array;
}

export interface Ari05AdapterStageResult {
  readonly accepted: boolean;
  readonly findings: readonly string[];
  readonly stagedEntries: readonly Ari05StagedArchiveEntry[];
}

export interface Ari05ArchiveAdapter {
  readonly format: Ari05ArchiveFormat;
  readonly runtimeCapability: () => Ari05RuntimeCapability;
  readonly stage: (request: Ari05ArchiveStageRequest) => Promise<Ari05AdapterStageResult>;
}

export interface Ari05ArchiveAdapterRegistry {
  readonly capabilityFor: (format: Ari05ArchiveFormat) => Ari05ArchiveCapability;
  readonly adapterFor: (format: Ari05ArchiveFormat) => Ari05ArchiveAdapter | undefined;
}

export interface Ari05ArchiveStagingResult extends Ari05AdapterStageResult {
  readonly canonicalResourcesCreated: false;
  readonly canonicalAcceptancePerformed: false;
  readonly rightsGranted: false;
  readonly providerEntitlementGranted: false;
}

function unsupported(format: Ari05ArchiveFormat): Ari05ArchiveCapability {
  return { format, available: false, diagnostic: `unsupported-runtime-capability:${format}` };
}

export function createAri05ArchiveAdapterRegistry(adapters: readonly Ari05ArchiveAdapter[]): Ari05ArchiveAdapterRegistry {
  const byFormat = new Map<Ari05ArchiveFormat, Ari05ArchiveAdapter>();
  for (const adapter of adapters) {
    if (!byFormat.has(adapter.format)) byFormat.set(adapter.format, adapter);
  }
  return {
    adapterFor: format => byFormat.get(format),
    capabilityFor: format => {
      const adapter = byFormat.get(format);
      if (!adapter) return unsupported(format);
      const capability = adapter.runtimeCapability();
      return { format, available: capability.available, diagnostic: capability.diagnostic };
    },
  };
}

export async function stageAri05Archive(
  request: Ari05ArchiveStageRequest,
  registry: Ari05ArchiveAdapterRegistry,
): Promise<Ari05ArchiveStagingResult> {
  const capability = registry.capabilityFor(request.format);
  if (!capability.available) {
    return {
      accepted: false,
      findings: [capability.diagnostic],
      stagedEntries: [],
      canonicalResourcesCreated: false,
      canonicalAcceptancePerformed: false,
      rightsGranted: false,
      providerEntitlementGranted: false,
    };
  }
  const adapter = registry.adapterFor(request.format);
  if (!adapter) {
    return {
      accepted: false,
      findings: [`unsupported-runtime-capability:${request.format}`],
      stagedEntries: [],
      canonicalResourcesCreated: false,
      canonicalAcceptancePerformed: false,
      rightsGranted: false,
      providerEntitlementGranted: false,
    };
  }
  const staged = await adapter.stage(request);
  return {
    accepted: staged.accepted,
    findings: [...staged.findings],
    stagedEntries: [...staged.stagedEntries],
    canonicalResourcesCreated: false,
    canonicalAcceptancePerformed: false,
    rightsGranted: false,
    providerEntitlementGranted: false,
  };
}

export const ARI05_AUTHORITY_BOUNDARY = {
  canonicalAcceptanceAuthorized: false,
  rightsGranted: false,
  providerCredentialsStored: false,
  recursiveDiscoveryImplemented: false,
  mediaClassificationImplemented: false,
  realMoneySpentCents: 0,
} as const;
