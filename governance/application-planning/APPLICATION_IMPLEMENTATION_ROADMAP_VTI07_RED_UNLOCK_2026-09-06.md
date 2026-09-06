# Application Implementation Roadmap — VTI-07 Matching RED Unlock

**Work item:** VTI-07 — Permissions, Hidden Information & GM Authority  
**Application branch:** `integration/vti-07-permissions-hidden-information-gm-authority`  
**Matching RED:** `5cb646cd4ea49e4ef82cc13d695c6450336c73ff` / run `34064038245` / receipt `3c405551b32804277945d4047a99786a2cf5a2dd6d513e0852aae48e8ea94f71`

## Authority unlocked

Implement only `packages/contracts/src/virtual-tabletop-interoperability/permissions-hidden-information-gm-authority-contract.ts` to satisfy the already-sealed VTI-07 acceptance package. The contract must consume canonical Multiversal `AuthorizationDecision`, ownership, consent, visibility and GM-authority decisions; omit hidden information entirely where even redaction would leak hidden existence/count; support identity redaction only for canonically visible records; require safe private channels for GM-only presentation; and make receipts depend only on safely disclosed material.

## Authority still closed

No parallel permission engine, provider schema/vendor commitment, credentials/accounts, adapters, live external/canonical mutation, persistence/migration, provider activation, tester distribution, release/deployment, VTI-08+ or SGC-01+ work is authorized.

## Required completion gate

The first production candidate after this unlock must pass exact-head current-family repository health, self-hosted Linux, self-hosted Windows and deterministic cross-platform comparison with zero historical predecessor fanout before application merge.
