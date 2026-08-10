# STAGE-A-A2 Implementation Contracts Handoff v0.6.0

**Work item:** STAGE-A-A2 — Universal Object Experience  
**Design status:** implementation-contract design complete; application implementation not started by this handoff  
**Branch:** `governance/stage-a-a2-detailed-design`  
**Owner/final authority:** John Brandon Turner

## Completed design scope

An owner-visible package was produced:

`STAGE_A_A2_IMPLEMENTATION_CONTRACTS_v0.6.0.zip`

SHA-256:

`38a9973aae676e243c04d91ef9845837d90d06e996adfe27269948fb1233c8ec`

The package converts the approved A2 v0.2.0–v0.5.0 design series into implementation-ready provider-neutral contracts aligned to the existing application repository architecture.

Package status: `IMPLEMENTATION_CONTRACT_DESIGN_COMPLETE_NOT_IMPLEMENTED`.

## Repository alignment

A2 implementation is explicitly mapped onto the existing repository surface rather than creating a parallel architecture:

- `apps/client-ui` — React/Vite client consuming A2 projections and ports;
- `packages/ui-system` — reusable Library/card/list/Inspector/Picker/status/focus/responsive primitives;
- `packages/contracts` — dependency-free TypeScript value types, projections, receipts and provider-neutral service ports;
- `schemas` — JSON Schema 2020-12 wire/fixture contracts;
- deterministic local fixtures/adapters — zero-service development and CI path.

Existing authorization, entitlement, hidden-information filtering, persistence and telemetry boundaries remain authoritative and must be composed/reused rather than duplicated by A2.

## Contract set

The package contains 14 JSON Schemas covering:

1. Object summary projection;
2. Object detail projection;
3. Object query request;
4. Object query response;
5. Relationship projection;
6. Provenance projection;
7. Comparison projection;
8. Picker invocation;
9. Picker selection receipt;
10. Presentation profile;
11. Scene placement adapter request;
12. Scene placement adapter result;
13. A2 service error;
14. shared common definitions.

Reference TypeScript contracts define the same shapes plus provider-neutral ports for catalog query, detail, relationships, provenance, comparison, Picker, presentation-profile registry and a caller-owned Scene placement boundary.

## Deterministic fixtures

The package contains 18 fixtures exercising positive, negative, stale, denied, redacted, relationship, provenance, comparison, Picker and Scene-placement behavior, including:

- authorized-only query/facet projection;
- non-disclosing not-found-or-forbidden error;
- full and redacted provenance;
- relationship targets after authorization filtering;
- successful Picker selection receipt;
- restricted/stale Picker revalidation failure;
- Item and Species projections;
- generic structured-source fallback preserving unknown structured data;
- caller-owned Scene placement request/result.

## Locked implementation invariants

1. Authorization occurs before discovery, counts, suggestions, exact-ID results, relationships, provenance/source fragments, comparison sides and Picker candidates are projected.
2. Forbidden existence is not leaked through alternate error shapes or hidden totals.
3. Stable IDs cross workflow boundaries; display names/aliases never become selected identity.
4. `presentationProfileId` is explicit metadata and must not be inferred from names, filenames or ID prefixes.
5. Definition, Variant, Placement, Live Instance, Snapshot and Projection remain distinct record layers.
6. A2 browsing, comparison and selection remain nonauthoritative; successful Picker receipts state `authoritativeMutationPerformed: false`.
7. Picker finalization must revalidate permission, entitlement, pack/version availability and compatibility immediately before issuing a receipt.
8. Scene placement remains caller-owned: the Scene/A5 boundary creates new Campaign-local placement IDs referencing selected Definition stable IDs/versions.
9. Comparison is read-only and cannot silently resolve variants/conflicts.
10. Provenance is read-only evidence and cannot edit original source material.
11. Generic structured fallback is lossless for permitted unmapped fields.
12. Deterministic zero-service adapters are required for development and CI; no hosted search/AI provider is required.

## Validation

Final local validation passed:

- package validator: PASS;
- JSON Schemas: 14;
- deterministic fixtures: 18;
- blocking implementation-contract gates: 24;
- ZIP CRC/integrity: PASS;
- package SHA-256 verified: `38a9973aae676e243c04d91ef9845837d90d06e996adfe27269948fb1233c8ec`;
- no TODO/TBD/FIXME/PLACEHOLDER unfinished markers;
- TypeScript reference contracts contain no React/Vite/database/provider imports.

The 24 gates cover schema/fixture validity, repository architecture fit, explicit projection identity/profile/layer fields, authorized-only counts, hidden relationship/provenance protection, read-only comparison, Picker selection/revalidation semantics, Scene placement boundary, generic lossless fallback, component/service test coverage, deterministic local adapters, checksums and non-claim boundaries.

## Recommended implementation destinations

- `schemas/*.schema.json` → `schemas/a2/*.schema.json`;
- `reference-types/a2-object-contracts.ts` → `packages/contracts/src/a2/object-contracts.ts`;
- `reference-types/a2-object-ports.ts` → `packages/contracts/src/a2/object-ports.ts`;
- fixtures → the repository-standard contracts fixture path;
- focused validator → repository-standard `tools/` verifier path;
- presentation-profile registry → explicit mapping contract plus app-owned static registry adapter;
- Scene placement adapter contract → `packages/contracts`, implementation owned by the Scene/A5 caller service.

These paths are implementation recommendations only; actual implementation must follow the active application branch/toolchain and repository conventions at implementation time.

## Preservation boundary

This handoff deliberately does **not** change `CURRENT_WORK_POINTER.json`. The owner-selected Content v2 Batch 8E governed-promotion attempt remains primary until separately completed or redirected. STAGE-A-A2 remains the authorized application work item and this package is preparatory/parallel design.

Do not claim A2 application implementation, A2 exit-gate completion, A5 Scene Builder implementation, production content migration, canonical promotion, internal-alpha release or deployment authority from this handoff alone.

## Exact next A2 step

The design/contract package is now sufficiently concrete for a governed A2 implementation work order. The next A2 tranche should convert these contracts and the v0.3–v0.5 screen/behavior matrices into an implementation sequence for Codex, beginning with dependency-free contracts/schemas + deterministic adapters, followed by Library/search, Inspector shell, presentation profiles, relationships/provenance, Picker, and the Scene Builder Add Object reference integration with focused CI and acceptance evidence.
