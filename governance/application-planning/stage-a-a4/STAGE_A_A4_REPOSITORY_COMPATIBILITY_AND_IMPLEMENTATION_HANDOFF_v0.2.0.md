# STAGE-A-A4 Repository Compatibility + Implementation Contract Handoff v0.2.0

**Status:** PREIMPLEMENTATION ONLY — A4 NOT ACTIVATED  
**Owner/final authority:** John Brandon Turner  
**Prepared:** 2026-08-10  
**Application repository snapshot:** `cybalicistjt-stack/Multiversal-app` main `dced7f92163050690c807c1fda937146bb8dce85`

## Artifact

External preparation artifact:

`STAGE_A_A4_REPOSITORY_COMPATIBILITY_AND_IMPLEMENTATION_CONTRACTS_v0.2.0.zip`

SHA-256:

`340791f2eae9f1db50904d455aa18de8246463b08d0394da02b3a38f91ae8439`

Validator result:

`STAGE-A-A4 REPOSITORY COMPATIBILITY + CONTRACTS v0.2.0: PASS`

Validated package dimensions:

- current repository/foundation anchors: 20
- blocking compatibility gaps/risks: 12
- planned provider-neutral Character contracts: 12
- future repository path actions: 37
- existing/future foundation reuse decisions: 12
- blocking validation/CI lanes: 15
- new runtime dependencies required: 0
- production provider selection required: 0

## Repository compatibility finding

The current application repository is compatible with A4 through additive Character contracts and a future governed persistence design.

Existing foundations to compose rather than rewrite include:

- `packages/contracts/src/persistence.ts` — provider-neutral optimistic persistence, transactions and migration port;
- `database/migrations/0001_initial_logical_schema.json` — current immutable 17-table logical-schema baseline;
- deterministic P9-06-009 seed/reset fixtures;
- P9-06-011 backup/restore/provider-exit rehearsals;
- canonical subject identity;
- Campaign authorization;
- entitlement evaluation and transitions;
- authoritative mutation/idempotency/version patterns;
- hidden-information filtering;
- reconnect/restoration;
- A1 client/UI/test/CI foundations.

The current 17-table logical schema does **not** contain a Character aggregate, Character draft, Character control-grant, Character event/history, Character snapshot, or other Character-specific persistence family. That absence is a real A4 implementation dependency, not a reason to rewrite the existing initial migration.

## Persistence design rule

`database/migrations/0001_initial_logical_schema.json` is preserved.

This preparation deliberately does **not** pre-freeze a permanent Character table decomposition before A2 and A3 are actually implemented. MV-IA-F004 freezes Character identities, policy bindings, operations, Events, validation, history, projections, offline boundaries and migration behavior; it does not require one provider-specific physical layout.

When A4 becomes current, A4-01 must:

1. inspect the then-current migration/schema registry;
2. install/finalize provider-neutral Character record contracts;
3. select the smallest additive logical persistence migration satisfying those contracts;
4. prove optimistic concurrency and transactional mutation;
5. prove migration/checkpoint/backup/restore/provider-exit integrity before later Character slices depend on it.

## Dependency rule

A4 remains sequentially dependent on verified implementation of both predecessor programs:

- A2 supplies the Universal Object Experience used for governed Character mechanical selection; A4 must not create duplicate Character-specific selectors.
- A3 supplies stable subject/workspace entry and selected context; A4 must not create a second identity/dashboard/workspace authority layer.

If A2 or A3 implementation materially changes the prepared integration paths, this compatibility map must be reconciled against the then-current repository before A4 activation.

## Planned A4 contract families

The package defines future paths for:

1. Character persistence record set;
2. Character draft port;
3. Character repository port;
4. Character projection port;
5. Character validation port;
6. Character calculation port;
7. Character control port;
8. Character advancement port;
9. Character migration port;
10. Character export port;
11. bounded Character-to-Scene reference;
12. Character operation-status lookup.

These compose the existing P9 provider-neutral foundations rather than replacing them.

## Preserved Character authority rules

- Character control is separate from Campaign membership, role, ownership and entitlement.
- Mechanical selections remain stable-ID/version governed references.
- Player-authored descriptive fields remain separate from governed mechanics.
- Local draft/autosave/calculation/cache/realtime/offline state is nonauthoritative.
- All authoritative Character writes require operation identity, current authorization and expected version.
- All 18 canonical validation classes remain blocking where applicable.
- Seven Character field classes are projected before list/search/sheet/history/export/diagnostics/AI delivery.
- Advancement/correction/migration history is append-only.
- Historical accepted restricted selections may remain representable while unauthorized new restricted selection stays denied.
- Offline authoritative Character creation/save/activation/control transfer/advancement/correction/migration/retirement/archive is forbidden.
- The A4 Scene proof remains a reference/projection handoff only and does not implement A5/A6.

## Stage sequencing and nonauthorizations

A4 is **not current**.

Current application sequence remains:

1. STAGE-A-A2 — current authorized next implementation work.
2. STAGE-A-A3 — preimplementation preparation only.
3. STAGE-A-A4 — preimplementation preparation only.

This handoff does not:

- create an A4 application branch;
- modify application code or database migrations;
- activate A4 out of sequence;
- alter the application current-work pointer;
- alter or complete the parallel Design Standards attempt;
- authorize a database vendor, identity provider, hosted search, AI or payment provider;
- authorize a new runtime dependency, credential, paid service or production data;
- authorize internal-alpha release, deployment, production or public release.

## Exact next non-Codex preparation step

Prepare **Stage A5 — Campaign and Scene Workspace** preimplementation inputs from the completed Campaign/Scene/Session Builder design, keeping A5 sequential and unactivated.