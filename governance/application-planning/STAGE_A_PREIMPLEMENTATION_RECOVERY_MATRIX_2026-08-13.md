# Stage A Preimplementation Recovery and Reconciliation Matrix

**Date:** 2026-08-13  
**Purpose:** preserve and classify previously prepared STAGE-A-A2 through STAGE-A-A12 work before new implementation/preparation is created.

## Recovery rule

These historical branches are **not canonical current implementation state** and must not be merged wholesale. They are also **not disposable drafts**. Each contains source-backed preimplementation material that must be reconciled against current `main`, later PPIA/CAPP authority, completed IA design, and the current application toolbelt.

Disposition vocabulary:

- **RETAIN / RECONCILE:** unique useful preparation exists; refresh assumptions against current authority before implementation.
- **PARTIAL SUPERSESSION REVIEW:** later work directly overlaps part of the package; preserve unaffected material and let newer authority control the overlap.
- **HISTORICAL EVIDENCE:** preserve for provenance but do not carry forward operational assumptions.

## Stage inventory

| Stage | Historical branch | Recovered unique package | Current disposition | Required reconciliation |
|---|---|---|---|---|
| A2 | `governance/stage-a-a2-detailed-design` | 26 handoffs from behavioral/screen refinement through real-data acceptance, privacy/performance, source promotion, hostile failure, repository compatibility, and v2.7.1 clean-room/Sunday-master preparation | **RETAIN / RECONCILE — highest priority** | Current app main/toolbelt, exact recovered v2.7.1 package, PPIA/CAPP provenance/privacy conventions, current A2 runner/preflight |
| A3 | `governance/stage-a-a3-preimplementation` | Identity, Dashboard, Workspace Selection preimplementation + repository compatibility/implementation contracts | **RETAIN / RECONCILE** | Current identity/auth/entitlement/session foundations; later privacy/hidden-information controls; A2 seam |
| A4 | `governance/stage-a-a4-preimplementation` | Character Workspace preimplementation + repository compatibility/implementation handoff | **PARTIAL SUPERSESSION REVIEW** | PPIA character/appearance decisions and CAPP production contracts are newer for appearance-specific surfaces; retain nonappearance Character workspace lifecycle/control material |
| A5 | `governance/stage-a-a5-preimplementation` | Campaign and Scene Workspace preimplementation + repository compatibility | **RETAIN / RECONCILE** | Current Campaign/session/event/recovery foundations; A2 picker/object seams; A3/A4 authority boundaries |
| A6 | `governance/stage-a-a6-preimplementation` | First Playable Action and GM Approval Loop + repository compatibility/implementation contracts | **RETAIN / RECONCILE** | Current authoritative command/event/reconnect contracts; A2 object/rule inspection; A3 role context; A4 control; A5 immutable launch snapshot |
| A7 | `governance/stage-a-a7-preimplementation` | Full Combat Interface + repository compatibility/implementation contracts | **RETAIN / RECONCILE** | Current action/result loop, combat-domain contracts, permission/hidden-information rules, IA combat design, responsive/accessibility standards |
| A8 | `governance/stage-a-a8-preimplementation` | Inventory, Crafting, Vehicles + repository compatibility/implementation handoff | **PARTIAL SUPERSESSION REVIEW** | CAPP equipment/wardrobe appearance projection and newer object/provenance contracts control appearance-related overlap; retain inventory/crafting/vehicle domain preparation |
| A9 | `governance/stage-a-a9-preimplementation` | Investigation and Social preimplementation + repository compatibility/implementation contracts | **RETAIN / RECONCILE** | IA relationship/social/investigation final designs, current hidden-information enforcement, object/provenance contracts |
| A10 | `governance/stage-a-a10-preimplementation` | World Builder and Content Creation + repository compatibility/implementation contracts | **RETAIN / RECONCILE** | Current canonical-object/content pipeline, source provenance, pack/install/uninstall authority, IA-D07 authoring contracts; resolve historical F018 label ambiguity using work-item identity |
| A11 | `governance/stage-a-a11-preimplementation` | Contextual AI Interfaces + repository compatibility | **RETAIN / RECONCILE** | Current optional-AI isolation, permission/redaction-before-retrieval rules, cost/provider neutrality, manual fallbacks, newer governance controls |
| A12 | `governance/stage-a-a12-preimplementation` | Internal-alpha hardening + repository compatibility + sequence-integrity addendum | **RETAIN / RECONCILE** | Current IA-D09 completed anchor, global adversarial/security corpus, current validators/CI, all-optionals-off behavior, final release/no-release boundaries |

## Recovered stage definitions and invariants

### A2 — Universal Object Experience

The branch contains 26 additive handoffs and is the deepest preparation package. It covers screen behavior, implementation contracts, real-data acceptance, search/filter/ranking, picker/Scene insertion, version/variant/conflict/provenance, privacy/performance, source-only promotion, record promotion, app-ready runtime corpus, hostile failure, repository compatibility, and final Sunday execution preparation. The later recovery checkpoint separately verified the v2.7.1 master and exact changed-path scope against application main `354e24007d2c453d090a2a6cdb31d3e3333c84c1`.

**Decision:** do not recreate A2 preparation. Reconcile this package against current repository state and use the existing mandatory runner before implementation.

### A3 — Identity, Dashboard, and Workspace Selection

Recovered package freezes provider-independent subject identity, separate workspace discovery/entry authorization, invitation safety, cache/context invalidation on revocation/switching, denial of protected-workspace existence leakage, and separation of role/membership/control/ownership/entitlement. It contains 10 preimplementation slices and 32 bounded fixtures.

**Decision:** retain. Later privacy/permission work strengthens rather than replaces these boundaries.

### A4 — Character Workspace

Recovered package is the Character workspace implementation-preparation layer. Later PPIA and CAPP work is newer authority for character appearance production, morphology, renderer metadata, wardrobe/equipment appearance projection, migration, accessibility description, export derivatives, and appearance QA.

**Decision:** preserve A4's Character lifecycle/control/workspace material; replace or amend appearance-specific assumptions with PPIA/CAPP authority during reconciliation.

### A5 — Campaign and Scene Workspace

Recovered package freezes immutable validated Session launch snapshots, separation of mutable Scene drafts from live Session authority, distinction among placement/source/snapshot/scene/session identities, preprojection permission filtering, durable-event recovery, and prohibition of offline authoritative mutation.

**Decision:** retain; refresh repository mappings only.

### A6 — First Playable Action and GM Approval Loop

Recovered package defines the full `Campaign -> Character -> Scene -> Action proposal -> GM decision -> authoritative Result -> synchronized persistent state` vertical slice, including exactly three final decision types (`approve`, `deny`, `modify-and-approve`), atomic committed results, durable decision receipts, idempotency/status lookup, revocation behavior, and offline prohibitions.

**Decision:** retain as the core playable-action seam; reconcile against current P9/A2-A5 implementation contracts when predecessors exist.

### A7 — Full Combat Interface

Recovered package adds the combat breadth intentionally deferred from A6 and includes a dedicated repository-compatibility/implementation-contract handoff.

**Decision:** retain; validate against the final IA combat packet and current responsive/accessibility standards before implementation.

### A8 — Inventory, Crafting, and Vehicles

Recovered package contains domain preparation and repository mapping for inventory/equipment, crafting, and vehicle systems.

**Decision:** retain domain preparation. CAPP is newer authority only where equipment/wardrobe data projects into character appearance/rendering; do not let appearance metadata become canonical inventory/equipment truth.

### A9 — Investigation and Social

Recovered package covers investigation/social runtime preparation and repository contracts.

**Decision:** retain; reconcile against completed IA relationship/social/investigation design and final hidden-information enforcement.

### A10 — World Builder and Content Creation

Recovered package validates 120 fixtures, 32 implementation slices, and 140 blocking source acceptance criteria. It preserves immutable published source/release/adventure versions, campaign-local overlay separation, owner-only canonical promotion, permission filtering before search/counts/graphs/previews/exports/AI context, and schema/dependency/processor/resource validation. It explicitly preserves a historical `F018` label ambiguity rather than silently resolving it.

**Decision:** retain. Current canonical-object/content conversion, provenance, pack installation/uninstallation, and source-governance work must control any overlapping implementation detail.

### A11 — Contextual AI Interfaces

Recovered package validates 72 fixtures, 24 implementation slices, 76 blocking source criteria, 12 independent AI permission dimensions, provenance/cost controls, all-optionals-off operation, and deterministic manual fallback. It requires redaction before retrieval/prompt/tool/cache/log/evaluation/export/response assembly and forbids AI canonical authority.

**Decision:** retain; reconcile provider/tool interfaces against current AIOC and optional-AI governance without introducing a provider dependency.

### A12 — Internal-alpha Hardening

Recovered package consumes rather than replaces IA-D09. It contains 12 hardening slices, 22 blocking gates, 8 owner-only decision gates, 17 evidence classes, and maps a 90-scenario/30-threat-family adversarial corpus into candidate validation. It preserves the state model `design_complete -> implementation_ready -> candidate_built -> candidate_validated -> release_approved`, with release approval remaining owner-only.

**Decision:** retain. Refresh its validator/CI mappings after A2-A11 implementation; do not treat preimplementation validation as a built or validated alpha candidate.

## Cross-program overlap rules

1. **PPIA/CAPP do not invalidate Stage A.** They sharpen Character/appearance production contracts consumed primarily by A4 and appearance-related A8 surfaces.
2. **IA-D09 is an upstream completed design anchor, not an implementation substitute.** A12 consumes it explicitly.
3. **Current canonical object/content work controls A10 data/provenance details** where historical preimplementation assumptions differ.
4. **The application repository controls implementation reality.** Every historical repository-compatibility mapping must be refreshed against current app main before activation.
5. **Historical package PASS results prove those packages against their recorded baselines only.** They do not prove compatibility with current main.

## Consolidation order

1. A2 exact-current compatibility review and runner readiness.
2. A3-A6 dependency-chain refresh.
3. A7-A9 runtime/domain refresh.
4. A10 content-authoring refresh against current canonical content pipeline.
5. A11 optional-AI/governance refresh.
6. A12 hardening/CI refresh.
7. Generate one current Stage A implementation-preparation index; preserve historical branches as provenance.

## Nonauthorization

This recovery matrix does not activate A2-A12, merge historical branches, authorize release/deployment/tester access/paid services/production credentials, or promote historical preparation to current implementation authority without reconciliation.
