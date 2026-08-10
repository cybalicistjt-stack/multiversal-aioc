# STAGE-A-A3 Repository Compatibility + Implementation Contracts Handoff v0.2.0

**Stage:** STAGE-A-A3 — Identity, Dashboard, and Workspace Selection  
**Status:** PREIMPLEMENTATION ONLY — NOT ACTIVATED  
**Prepared against application main:** `dced7f92163050690c807c1fda937146bb8dce85`  
**Artifact:** `STAGE_A_A3_REPOSITORY_COMPATIBILITY_AND_IMPLEMENTATION_CONTRACTS_v0.2.0.zip`  
**Artifact SHA-256:** `b0396d3945a0c200a2b7d3821bb851c06c57fbc83a29373fc0a5758df32bf1b7`  
**Nested base package:** `STAGE_A_A3_PREIMPLEMENTATION_DESIGN_PACKAGE_v0.1.0.zip`

## Completion state

The v0.2.0 compatibility/contract package validates PASS.

Package metrics:

- 22 current application-repository anchors;
- 10 blocking compatibility gaps/risks;
- 10 planned A3 implementation contracts;
- 37 exact repository path actions across A3-01 through A3-10;
- 12 existing-foundation reuse decisions;
- 12 blocking validation/CI lanes;
- zero new runtime dependencies required;
- zero production identity-provider requirement;
- zero A3 application activation.

## Reuse boundary

Future A3 implementation must reuse rather than rebuild the existing provider-neutral foundations:

- `packages/contracts/src/identity-device/identity-service-port.ts`;
- `packages/contracts/src/identity-device/provider-independent-identity-mapping.ts`;
- `packages/contracts/src/authorization/campaign-authorization-policy.ts`;
- `packages/entitlements/src/entitlement-service-port.ts`;
- `packages/contracts/src/identity-device/entitlement-evaluator.ts`;
- `packages/contracts/src/session/authoritative-session-command-handler.ts`;
- `packages/contracts/src/session/hidden-information-response-filter.ts`;
- `packages/contracts/src/session/ordered-realtime-event-delivery.ts`;
- `packages/contracts/src/session/checkpoint-reconnect-restoration.ts`;
- `database/migrations/0001_initial_logical_schema.json`;
- the current A1 React/Vite/Vitest/axe shell and UI-system foundation.

The existing P9-06-012 through P9-06-018 focused validators remain regression gates for A3.

## Confirmed additive A3 work

Current repository evidence does **not** show a concrete runtime implementation for the following A3 requirements, so future implementation is additive rather than replacement work:

- provider-neutral alpha identity/session runtime adapter;
- invitation lifecycle service/contract/schema;
- authorized dashboard projection service;
- separate workspace discovery and entry services;
- selected-context receipt contract;
- recent-work service;
- A3-bounded safe notification summaries;
- Assistant-GM delegation and purpose/time-bounded support-access records;
- A3 context-switch/deep-link/revocation cache-isolation layer.

## Important role boundary

Do not broaden the existing Campaign role model merely to fit every A3 application role.

Campaign/play authority and application/operational workspace role are distinct. Global Owner/Admin, content creator, invited tester, Assistant GM delegation, or support access must never silently become Campaign owner/private-play authority. Existing Campaign authorization should be composed with A3 workspace, delegation, entitlement and control decisions rather than weakened.

## Nonclaims

- `STAGE-A-A2` remains the authorized current next application work item.
- A3 remains sequential and not current.
- No A3 application branch is created by this preparation work.
- No production identity provider, provider SDK, hosted service, paid service, production credential, public registration, deployment, tester access, or release is authorized.
- No lockfile or application source mutation is authorized by this handoff.
- This handoff does not modify `CURRENT_WORK_POINTER` or the parallel Design Standards attempt.

## Exact next preparation work

Proceed to the next approved ahead-of-Codex tranche: **STAGE-A-A4 — Character Workspace preimplementation package**, using the completed Internal Alpha character-creation/advancement design and the same nonactivation rule. A4 remains behind A3 and must not be activated out of sequence.
