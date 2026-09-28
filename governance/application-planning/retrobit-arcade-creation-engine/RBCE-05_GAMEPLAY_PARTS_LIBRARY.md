# RBCE-05 — Gameplay Parts Library

**Program:** Retrobit Arcade & Creation Engine (RBCE)  
**Work item:** RBCE-05  
**Status:** OWNER-DIRECTED DESIGN BASELINE  
**Operational authority:** none; this artifact does not select implementation and cannot override OPS3  
**Consumes:** RBCE-01, RBCE-03, GPR-01, GPR-06, GPR-08, MRCS governed definitions and canonical owner operations

## 1. Purpose

RBCE-05 defines the creator-facing **Gameplay Parts Library**. It lets a Retrobit creator browse and insert understandable gameplay building blocks without hand-entering runtime IDs or writing scripts.

A Gameplay Part is a presentation/composition projection over already governed gameplay definitions, primitives, operations, asset roles and owner references. It never becomes a second rules engine.

## 2. Authority

Authority remains outside RBCE-05:

- **GPR** owns runtime registry, deterministic execution and runtime binding status.
- **MRCS** owns governed reusable pattern/definition semantics.
- **MAL-01..10** remains primitive source authority where GPR identifies it as such.
- **Canonical owner domains** own operations and all canonical mutations.
- **ARI/PCA** owns governed asset-role authority.
- **RBCE-01** owns Retrobit project composition records.
- **RBCE-03** owns the Studio authoring interaction that browses, configures, previews and inserts parts.

RBCE-05 may not mint runtime IDs, create canonical definitions, execute gameplay, mutate owner state or infer unsupported semantics.

## 3. Source vocabulary

RBCE-05 reflects the current GPR-01 registry kinds exactly:

- `pattern` → `gpr.pattern` → definition authority `MRCS`;
- `primitive` → `gpr.primitive` → primitive authority `MAL-01..10`;
- `operation` → `gpr.operation` → source authority `canonical-owner`;
- `asset-role` → `gpr.asset-role` → source authority `ARI/PCA`.

A source binding is `ready`, `unsupported` or `unresolved` according to the governing source. RBCE-05 does not upgrade an unresolved or unsupported binding.

## 4. Exactly two part forms

### `part-form:binding`

A binding part is one human-readable card over one governed source binding. It may expose creator parameters, compatibility evidence and one deterministic expansion target.

Examples: Player Role, Move, Interact, Collect Objective, Score Resource.

### `part-form:recipe`

A recipe is a deterministic bundle of two or more governed source bindings expanded into ordinary RBCE/GPR authoring fields. A recipe is convenience, not hidden behavior.

Every recipe must expose its sources, parameters, expansion steps and resulting authoring delta before insertion. Missing required sources block insertion.

## 5. Creator categories

The initial library taxonomy is:

- `part-category:game-loop`
- `part-category:objective`
- `part-category:participant-role`
- `part-category:action`
- `part-category:resource`
- `part-category:rule`
- `part-category:reward`
- `part-category:specialist`
- `part-category:interaction`
- `part-category:composite`

Categories are discovery metadata only. They do not create semantics.

## 6. Binding kinds

A part may reference only these governed binding classes in v1:

- `binding-kind:gpr-pattern`
- `binding-kind:gpr-primitive`
- `binding-kind:gpr-operation`
- `binding-kind:gpr-asset-role`
- `binding-kind:mrcs-definition`
- `binding-kind:owner-reference`

Each binding records source authority, exact source reference/version, owner domain, required/optional state and resolution status.

## 7. Parameters

Creator-facing parameters are bounded data, never executable code. Supported v1 value types are:

`boolean`, `integer`, `number`, `string`, `enum`, `stable-ref`.

Every parameter names its target path and validator (`RBCE-01`, `GPR`, `MRCS` or `owner-domain`). A default value is legal only when the governing contract supports it; the library may not invent a semantic default.

## 8. Deterministic expansion

Expansion steps target existing authoring structures only:

- `target:gpr-pattern`
- `target:gpr-participant`
- `target:gpr-objective`
- `target:gpr-operation`
- `target:gpr-resource`
- `target:gpr-rule`
- `target:gpr-reward`
- `target:rbce-variable`
- `target:rbce-outcome`
- `target:rbce-actor-binding`
- `target:rbce-scene-reference`

Given the same part version, parameter values and target project state, normalized expansion must produce the same authoring delta. Catalog ordering, search ranking, UI layout and optional AI suggestions may not change the result.

## 9. Duplicate policy

Every part declares one policy:

- `duplicate-policy:allow`
- `duplicate-policy:singleton`
- `duplicate-policy:merge-by-stable-id`
- `duplicate-policy:replace-explicitly`

A collision never causes silent replacement. The Studio must preview the exact result and require the policy-defined action.

## 10. Compatibility

Delivery and projection compatibility are evidence-driven. Supported delivery vocabulary remains GPR-08's seven modes:

`direct-play`, `cozy-low-pressure`, `gm-led`, `world-map-ttrpg-bridge`, `embedded-minigame`, `user-authored-loop-mini`, `roster-injection`.

Projection families are the RBCE-02 families: `top-down-2d`, `side-scroll-2d`, `fixed-room-2d`.

Compatibility state is explicit-compatible, explicit-incompatible or unknown. Unknown is not permission to insert when compatibility is required by the target context.

## 11. Specialist parts

GPR-06 specialist families remain one governed runtime family rather than Retrobit forks:

`puzzle`, `sports`, `vehicle-mount`, `party-companion`, `tactical-strategy`, `social-investigation`, `stealth-detection`.

RBCE-05 may surface them as parts only when their GPR pattern/operation bindings and required owner capabilities resolve. Owner receipts remain required wherever GPR requires them.

## 12. MRCS definitions

MRCS remains definition authority. Relevant domains may include advancement, abilities, species/forms, items/loadouts, magic, creatures, vehicle/mount/companion/construct, environment/hazard, encounter/reward/economy and scoped rules.

RBCE-05 presents accepted governed definitions; it does not duplicate their rules or infer compatibility. Version changes are explicit migrations, never silent rewrites.

## 13. Studio authoring flow

The normative Studio flow is:

`Browse → Inspect → Configure → Validate dependencies → Preview authoring delta → Insert → Revalidate project`.

Insertion mutates only the editable RBCE project draft. It does not execute gameplay, commit campaign state, publish `.pack`, create MRCS definitions or register GPR runtime IDs.

Removing a part removes only authoring state proven to belong to that insertion. Dependent project state must block removal or require explicit repair; unrelated state is never cascade-deleted silently.

## 14. Search and accessibility

The library supports local deterministic search/filter by text, category, form, readiness, authority, delivery compatibility, projection compatibility, version and required capability. Search ranking is presentation-only.

The full workflow must work without a visual card grid: list/tree view, keyboard navigation, screen-reader labels, textual authority/source descriptions, non-color readiness indicators, accessible parameter forms, textual recipe expansion summaries and no drag-only insertion.

## 15. Local-first and AI

Normal authoring is provider-off and local-first. AI and paid cloud are not required.

Optional AI may suggest search terms, explain governed parts, propose recipes composed only from available governed parts, or suggest parameter values. AI cannot mint a missing runtime binding, mark unresolved content ready, invent owner compatibility, bypass validation or silently insert project changes.

## 16. Validation and failures

RBCE-05 fails closed. Representative diagnostics include:

`part-id-invalid`, `part-source-binding-missing`, `part-source-binding-unresolved`, `part-source-binding-unsupported`, `part-owner-domain-mismatch`, `part-owner-capability-unavailable`, `part-parameter-invalid`, `part-expansion-target-invalid`, `part-required-dependency-missing`, `part-duplicate-policy-conflict`, `part-delivery-incompatible`, `part-projection-incompatible`, `part-version-migration-required`, `part-authority-violation`, `part-arbitrary-script-forbidden`, `part-canonical-mutation-forbidden`.

Diagnostics normalize by code, semantic path, then stable part/source reference.

## 17. Verified golden bindings

The RBCE-05 golden fixture is restricted to runtime IDs already evidenced by the current application contract tests:

- `gpr.pattern:pattern/loop-mini@1.0.0`
- `gpr.pattern:objective/collect@1.0.0`
- `gpr.asset-role:asset-role/player@1.0.0`
- `gpr.operation:operation/interact@1.0.0`
- `gpr.operation:operation/move@1.0.0`
- `gpr.primitive:resource/score@1.0.0`
- `gpr.pattern:pattern/specialist-social-investigation@1.0.0`
- `gpr.operation:operation/specialist-social-investigation@1.0.0`
- `gpr.pattern:multiversal/golden/environment-hazard@1.0.0`

The negative fixture uses the application-tested unresolved reference `gpr.pattern:pattern/missing-specialist@1.0.0` and must remain visibly non-insertable.

These are verification anchors, not authority for RBCE-05 to invent additional runtime IDs.

## 18. Acceptance

RBCE-05 is design-complete when the machine fixture proves: human-readable browse, governed-source inspection, binding insertion, bounded parameter configuration, recipe insertion, deterministic expansion, fail-closed unresolved/unsupported bindings, delivery/projection filtering, explicit version migration, preserved owner authority, accessible nonvisual authoring, provider-off completion and Four-Engine gameplay coverage.

The golden catalog includes direct parts for loop host, player role, collect objective, move, interact, score, social/investigation pattern/operation and environment hazard; recipes demonstrate multi-part composition; a negative diagnostic part proves unresolved behavior.

## 19. Machine identifiers and activation boundary

- schema ID: `RBCE05.GAMEPLAY_PARTS.v1`
- semantic version: `1.0.0`
- library authority: `projection-only`
- runtime authority: `GPR`
- definition authority: `MRCS`
- default skin: `retrobit-classic-arcade`

This is durable content/design only. Product implementation begins only when OPS3 explicitly selects and authorizes RBCE-05 or equivalent governed implementation work. The live PCV-03F selector remains unaffected.
