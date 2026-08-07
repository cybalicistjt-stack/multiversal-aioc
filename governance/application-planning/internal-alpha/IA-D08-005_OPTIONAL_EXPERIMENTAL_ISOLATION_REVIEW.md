# IA-D08-005 — Optional and Experimental Isolation Review

**Owner:** John Brandon Turner  
**Status:** READY FOR TARGETED VALIDATION — DESIGN BOUNDARY  
**Boundary:** Internal-alpha design only; application implementation remains dependency-gated by P9-06.

## Purpose

Prove that optional, experimental, provider-dependent, advanced, deferred, and fallback-sensitive capabilities are isolated from the Internal Alpha core. The alpha must remain usable, deterministic, permission-safe, recoverable, testable, and supportable when every optional capability is disabled, unavailable, unsupported, revoked, or removed.

## Governing rule

**Optional means removable without breaking the core. Experimental means isolated without becoming authority.**

No optional or experimental capability may be a hidden prerequisite for authentication, Campaign/Character access, core authoring, live Actions, GM review, authoritative results, inventory/Asset operations, social/investigation flows, bounded maps/vehicles, recovery, accessibility, provenance, export, diagnostics, or manual operation.

## Scope reviewed

This review consolidates the isolation consequences of IA-D08-001 through IA-D08-004 and the previously completed IA design tranches. It covers:

- Optional AI Assistant and provider routing;
- AI-generated proposals, summaries, explanations, and recommendations;
- advanced map/canvas/vehicle capabilities deferred by IA-D08-003;
- broad offline capabilities deferred by IA-D08-004;
- experimental processors, feature flags, adapters, importers, renderers, and provider integrations;
- future optional modules whose data may be present before runtime support exists.

## Isolation classes

### I0 — Core-required

Capabilities necessary to satisfy the declared Internal Alpha contract. They may not depend on I1–I4 components for correctness.

### I1 — Optional supported

Supported during alpha but removable or disableable. Absence must produce a deterministic manual/core fallback.

### I2 — Experimental gated

Available only behind explicit capability/feature gates. Must have no canonical authority beyond already-approved owning-domain commands.

### I3 — Deferred preserved

Not executed in alpha. Data may be preserved opaquely with version/provenance metadata, compatibility reporting, and future migration seams.

### I4 — Prohibited coupling

Any dependency that would make a core workflow require an optional provider, hidden experimental processor, proprietary format, unsupported offline authority, or advanced visualization to remain correct. I4 coupling is a blocking defect.

## Core independence requirements

1. **No hard optional dependency:** core code paths must initialize and operate when optional services are absent.
2. **Manual fallback:** every AI-assisted core task has a complete non-AI path.
3. **Semantic fallback:** maps, graphs, tactical positioning, and relationship/investigation structures retain list/table/outline/nonvisual operation without advanced rendering.
4. **Online authority fallback:** broad offline features may be absent; reconnect-safe draft/cache/status behavior remains as defined by IA-D08-004.
5. **Provider neutrality:** provider IDs, SDK types, billing state, or provider-specific payloads may not become canonical domain identity.
6. **Feature-gate safety:** disabling a feature hides or disables only its optional surfaces and processors; it does not invalidate unrelated canonical records.
7. **No optional authority escalation:** optional processors may propose, render, analyze, or transform within allowed contracts but may not acquire approval, publication, ownership, entitlement, hidden-information, or commit authority.
8. **Failure containment:** timeout, quota, outage, malformed response, unsupported capability, or local optional-module failure cannot partially commit a core authoritative transaction.
9. **Data preservation:** unsupported optional extension data is preserved opaquely when safe and never silently executed or discarded.
10. **Permission equivalence:** optional views use the same server-authorized projection as core views and cannot infer hidden state through counts, topology, embeddings, previews, diagnostics, exports, or AI context.

## Optional AI isolation

The Optional AI Assistant is I1/I2 depending on capability. Core workflows must not require an AI provider or AI-generated object. When AI is unavailable:

- rules and source lookup remain available through deterministic search/reference paths;
- Character/Campaign authoring remains manual;
- Action proposal construction remains manual;
- GM approval remains human-controlled;
- summaries may be absent without blocking history access;
- provider failure returns a bounded unavailable/fallback state, not a canonical mutation failure;
- cached or delayed AI output is revalidated before any later proposal can enter governed review.

No AI response may be treated as authoritative evidence merely because a provider returned it successfully.

## Advanced map and vehicle isolation

Advanced spatial rendering, precision geometry, automated pathing, complex vehicle subsystems, or unsupported tactical processors are I2/I3. Core alpha retains semantic topology, zones/range bands, position, vehicle identity, ownership/control/stations, and accessible nonvisual/list alternatives. Unsupported advanced payloads are preserved without execution.

## Offline isolation

Broad offline authority is I3. The alpha may depend on an authoritative service for canonical mutation. Offline-safe cache, recoverable drafts, replay-safe intent, status lookup, Event-gap recovery, reconnect reauthorization, and explicit conflicts remain available without implying full offline hosting or mutation.

## Feature flags and capability negotiation

Every optional or experimental capability must expose a stable capability identifier and one of: enabled, disabled, unavailable, unsupported, revoked, or incompatible. Capability state affects presentation and allowed optional operations only. It must not silently change canonical meaning.

A client must not infer support from the presence of unknown fields. Unknown processors remain non-executable until an explicit compatible capability contract exists.

## Persistence and schema rules

- canonical core fields do not require optional provider schemas;
- optional metadata uses versioned extension namespaces or separately owned records;
- removing an optional module leaves core records valid;
- unknown extension data survives round trip where safe;
- migrations that promote optional data into core require explicit later governance and receipts;
- no optional feature may require destructive rewrite of unrelated canonical history.

## Runtime failure containment

Optional work runs outside the authoritative atomic commit boundary unless it is itself the governed command being committed by the owning domain. A failed optional suggestion, renderer, simulation, adapter, export enrichment, or provider call cannot cause a half-applied core result.

Where optional output is attached to a proposal, the owning core command performs fresh permission, version, dependency, and rule validation before commit.

## Accessibility isolation

No advanced graph, canvas, animation, voice, image generation, or AI interface may be the sole way to perform a required alpha task. Keyboard, touch, screen-reader, high-contrast, reduced-motion, text/list/table/outline, and nonvisual alternatives remain part of the core contract.

## Observability and privacy

Optional telemetry must be separately attributable, privacy-safe, bounded, and disableable where policy permits. Core diagnostics must distinguish optional-provider failures from authoritative service failures. Secrets, hidden content, and unauthorized projections must not be copied into optional telemetry or provider context.

## Removal test

A build/configuration with all I1–I3 capabilities disabled must still support the declared Internal Alpha core journeys through deterministic manual and semantic interfaces. Any failure is an isolation defect, not a reason to reclassify the optional capability as core after the fact.

## Implementation slices

- **ISO-S01 — Capability registry:** stable IDs, isolation class, state, owner, dependencies, fallback.
- **ISO-S02 — Dependency enforcement:** build/runtime guards preventing I4 coupling and provider-specific canonical identity.
- **ISO-S03 — Manual and semantic fallbacks:** complete non-AI, non-advanced-renderer, online-authority core paths.
- **ISO-S04 — Failure containment:** timeout/outage/quota/malformed/unsupported isolation and atomicity.
- **ISO-S05 — Extension preservation:** opaque namespaces, compatibility reports, non-execution, migration seams.
- **ISO-S06 — Permission/accessibility parity:** identical authorized projections and nonvisual operation.
- **ISO-S07 — Diagnostics and privacy:** typed optional failures, privacy-safe telemetry, no hidden-data leakage.
- **ISO-S08 — Removal and regression gate:** all-optionals-off fixture suite and exact IA-D09 handoff.

## Blocking acceptance criteria

1. Core alpha starts and runs with every optional/experimental capability disabled.
2. AI provider absence cannot block a core workflow.
3. Advanced rendering absence cannot block semantic gameplay or authoring.
4. Broad offline authority remains deferred without degrading reconnect-safe core behavior.
5. Optional failure cannot partially commit core authoritative state.
6. Optional providers never define canonical IDs or ownership.
7. Feature flags cannot widen permissions.
8. Unknown processors never execute implicitly.
9. Unsupported extension data is preserved or rejected explicitly, never silently reinterpreted.
10. Hidden information is filtered before optional processing.
11. Core exports and diagnostics remain usable without optional enrichments.
12. Accessibility does not depend on advanced rendering, AI, voice, or motion.
13. Manual fallback exists for every AI-assisted core task.
14. Removal of an optional module leaves unrelated records valid.
15. Optional outputs require fresh owning-domain validation before commit.
16. Provider quota/cost failure is contained to the optional operation.
17. Capability state is explicit and inspectable.
18. No I4 coupling remains.
19. Deterministic fixtures cover disabled, unavailable, incompatible, revoked, and failure states.
20. The next exact design item is IA-D09 — Internal-alpha release-design package.

## Decision

IA-D08-005 establishes the isolation boundary required to close IA-D08. Optional and experimental systems may enrich Internal Alpha but may not become hidden prerequisites, alternate authorities, accessibility dependencies, or canonical-schema traps. After verified completion, design proceeds to **IA-D09 — Internal-alpha release-design package**. `P9-06-008-attempt-002` remains unfinished, paused, and unmodified.
