# STAGE-A-A2 Implementation Contract Handoff v0.6.0

**Work item:** STAGE-A-A2 — Universal Object Experience  
**Design status:** implementation-contract tranche complete; application implementation not started by this handoff  
**Branch:** `governance/stage-a-a2-detailed-design`  
**Owner/final authority:** John Brandon Turner

## Completed design scope

An owner-visible package was produced:

`STAGE_A_A2_IMPLEMENTATION_CONTRACTS_v0.6.0.zip`

SHA-256:

`20c2eaa44ff1812809904496ec01a15554a2ea7801852b0e2278d163a8e7edc8`

The package contains 44 files / 3,870 lines and converts the A2 v0.2.0–v0.5.0 UX/presentation/behavior design into concrete implementation contracts.

### Contract coverage

- 14 JSON Schema 2020-12 contracts for summary/detail projections, query request/response, relationships, provenance, comparison, Picker invocation/receipt, presentation profiles, Scene placement adapter request/result, errors, and common definitions;
- dependency-free TypeScript reference contracts and provider-neutral ports;
- 18 deterministic positive/denied/stale/redacted/Scene-placement fixtures;
- component-to-contract matrix;
- 24-case service test matrix;
- repository target map;
- 24 blocking implementation-contract acceptance gates;
- deterministic package validator, manifest, and SHA-256 receipt.

## Repository compatibility decisions

The package was reconciled against the physical application repository rather than an abstract future architecture.

- Stage A A1 PR #69 establishes the React/Vite client in `apps/client-ui` and reusable semantic primitives in `packages/ui-system`.
- WP-006 PR #30 preserves the approved physical `schemas/` and `packages/contracts` roles and explicitly avoids creating conceptual duplicate packages.
- Existing provider-neutral IdentityServicePort and EntitlementServicePort patterns (PRs #74 and #75) establish dependency-free contracts + JSON schema + deterministic fixture/validator/CI patterns.
- Existing row/campaign authorization, entitlement evaluation, hidden-information projection, and structured telemetry work (including PRs #85, #86, #90, #92) are treated as composed dependencies rather than duplicated inside A2.

Recommended implementation destinations therefore remain:

- UI/route consumption → `apps/client-ui`;
- reusable UI primitives → `packages/ui-system`;
- A2 TypeScript contracts/ports → `packages/contracts`;
- JSON schemas → `schemas`;
- deterministic fixtures, focused verifier, and narrowly scoped CI following existing repository conventions.

No hosted search, AI, database, billing, or identity provider is required for the A2 contract path.

## Locked contract boundaries

- authorization precedes results, facets, suggestions, exact-ID resolution, relationship targets, provenance/source fragments, comparison sides, and Picker candidates;
- hidden records do not contribute exposed facet/relationship counts;
- explicit `presentationProfileId` and stable IDs cross A2 boundaries; the client never infers profile from names/IDs;
- Definition/Variant/Placement/Live Instance/Snapshot/Projection remain distinct;
- successful Picker receipts require final current revalidation and always set `authoritativeMutationPerformed: false`;
- the Scene/A5 caller, not A2, creates authoritative Campaign-local placements;
- Scene placement IDs are distinct from source Definition IDs and preserve the source version/selection receipt;
- generic structured fallback preserves permitted unmapped structured fields;
- comparison and provenance remain read-only;
- deep-link/local recovery state never grants authority;
- deterministic zero-service adapters are required for development and CI.

## Validation

- JSON Schema + fixture conformance: PASS — 14 schemas / 18 fixtures;
- cross-fixture authority/information-leak invariants: PASS;
- provider/framework dependency scan of reference TypeScript: PASS;
- unfinished-work marker scan: PASS;
- package SHA receipt: PASS;
- deterministic ZIP CRC: PASS;
- implementation-contract gates defined: 24.

## Preservation boundary

This handoff deliberately does **not** change `CURRENT_WORK_POINTER.json`. The owner-selected Content v2 Batch 8E governed-promotion attempt remains primary until separately completed or redirected. STAGE-A-A2 remains the authorized application work item and this package is preparatory/parallel design.

Do not claim A2 implementation, A2 exit-gate completion, A5 Scene Builder completion, production content migration, canonical promotion, internal-alpha release, production release, or deployment authority from this handoff alone.

## Exact next A2 design operation

Prepare the bounded **A2 implementation work order and Codex execution package** that maps v0.2.0–v0.6.0 into ordered repository changes, changed-path scope, deterministic fixtures, validation commands, test gates, preview/owner-review evidence, and rollback. Do not begin repository implementation until that work order is explicitly activated under the application repository's governance rules.
