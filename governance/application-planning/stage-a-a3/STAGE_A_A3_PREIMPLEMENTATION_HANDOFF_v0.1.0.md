# STAGE-A-A3 Preimplementation Handoff v0.1.0

**Stage:** STAGE-A-A3 — Identity, Dashboard, and Workspace Selection  
**Status:** PREIMPLEMENTATION PREPARATION ONLY — NOT ACTIVATED  
**Owner/final authority:** John Brandon Turner  
**Prepared:** 2026-08-10

## Authority boundary

The canonical Stage A program defines A3 as identity entry, role-aware dashboards, Player/GM/Content Creator/Owner-Admin workspaces, and service/action-level permissions. A3 remains sequentially behind STAGE-A-A2 and is not current implementation work.

Current application preparation anchor: `dced7f92163050690c807c1fda937146bb8dce85` (`Prepare governed Stage A A2 work order (#104)`).

IA-D09 is already completed and merged in PR #187 at merge SHA `e0ddb253007ed42874d1b3061f19d0bb0e8c13db`; its dedicated `Validate Internal Alpha Release Design` gate passed on the exact PR head.

Current application task-queue evidence records P9-06-001 through P9-06-022 as `COMPLETED_VERIFIED`, P9-06-023/AG-07 as `COMPLETED_VERIFIED`, P9-06-024 owner decision recorded, STAGE-A-A2 as `AUTHORIZED CURRENT NEXT`, and STAGE-A-A3–A12 as sequential/not current.

## Prepared artifact

External working artifact:

`STAGE_A_A3_PREIMPLEMENTATION_DESIGN_PACKAGE_v0.1.0.zip`

SHA-256:

`61affc377d57b941af40ae82b736b44ceb869103ca7bf8691833a92e1e5daa4f`

Validator result:

`STAGE-A-A3 PREIMPLEMENTATION DESIGN v0.1.0: PASS`

Validated dimensions:

- 8 role classes;
- 9 workspace types;
- 13 identity/state object classes;
- 6 primary entry flows;
- 10 invitation states;
- 20 protected-discovery surfaces;
- 26 required user/recovery states;
- 20 canonical denied cases from the F003 machine-readable matrix;
- 12 additional positive acceptance fixtures;
- 32 total bounded fixture cases;
- 10 preimplementation slices A3-01 through A3-10;
- 12 blocking A3 acceptance gates;
- 72 deny-by-default role/workspace matrix rows;
- 15-field selected-context receipt schema.

## Core invariants frozen by the package

1. Stable Multiversal subject identity is independent of provider identity, email, display name, device, and active role.
2. Workspace discovery and workspace entry are separate authorization decisions.
3. Campaign membership, role, Character control, ownership, and entitlement remain separate decisions.
4. A selected-context receipt supports navigation/recovery but is never client-authoritative permission.
5. Protected workspace existence must not be disclosed through cards, labels, counts, notifications, recent work, autocomplete, deep links, diagnostics, exports, or AI dashboard summaries.
6. Invitations are inference-safe, atomic, idempotent, recipient/expiry/revocation aware, and cannot be accepted offline.
7. Campaign/role switching and revocation clear or partition prior protected caches, drafts, subscriptions, notifications, and AI context before the new projection continues.
8. Owner/Admin operational authority is not blanket access to private Campaign or Player content.
9. Cached/offline identity or context cannot authorize protected entry or mutation.
10. A3 activation remains blocked on canonical A2 completion even though the P9 backend foundations are now completed_verified.

## Source authority used

- `governance/application-planning/STAGE_A_UI_IMPLEMENTATION_PROGRAM.md`
- `governance/application-planning/internal-alpha/feature-packets/MV-IA-F003_IDENTITY_DASHBOARD_AND_WORKSPACE_SELECTION.md`
- `governance/application-planning/internal-alpha/feature-packets/MV-IA-F003_IDENTITY_WORKSPACE_MATRIX.json`
- `governance/application-planning/internal-alpha/feature-packets/MV-IA-F003_IMPLEMENTATION_TRACEABILITY.json`
- `governance/application-planning/internal-alpha/feature-packets/MV-IA-F020_PERMISSIONS_AND_HIDDEN_INFORMATION.md`
- `governance/application-planning/internal-alpha/IA-D09_IMPLEMENTATION_QUEUE.json`
- application `.ai/task-queue.md`

The canonical `IDW-AC-001` through `IDW-AC-020` identifiers are retained for implementation traceability. Their exact criterion wording is not fabricated or replaced in the preimplementation artifact.

## Nonclaims

This handoff does not activate A3, create an application A3 branch, change the application current-work pointer, modify A2, select a production identity provider, authorize public registration, production credentials, paid services, tester access, release, deployment, or public exposure.

## Exact next preimplementation work

Without activating A3, the next preparation tranche is the **A3 repository compatibility and implementation-contract package**: map A3-01 through A3-10 onto the actual existing identity, authorization, entitlement, session, persistence, shell, test, and CI modules in `Multiversal-app`, then produce the exact file/reuse/validator plan and hostile acceptance package.