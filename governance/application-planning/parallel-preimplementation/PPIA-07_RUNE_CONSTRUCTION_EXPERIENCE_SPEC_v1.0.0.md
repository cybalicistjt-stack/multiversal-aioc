# PPIA-07 — Rune Construction Experience Specification v1.0.0

**Work item:** PPIA-07 — Rune Construction RPG System  
**Version:** 1.0.0  
**State:** COMPLETION CANDIDATE — implementation-ready design only after exact-head validation and merge  
**Owner and final authority:** John Brandon Turner

## 1. Purpose

This specification defines the implementation-ready Multiversal Rune Construction RPG System.

The system is a compositional magic language rather than a catalog of one-rune-per-spell effects. Players and GMs combine a compact vocabulary of Operation Runes, Essence Runes, connection types and typed modifiers into deterministic constructions that can be parsed, explained, inspected, crafted, proposed, approved, countered, recovered and replayed.

The final design must support both:

1. **standard rune play**, where authorized users may receive permitted semantic previews; and
2. **blind rune-play**, where a player constructs and submits runes without receiving the interpreted magical effect before adjudication, while an authorized GM receives the resolved effect and explicitly chooses whether it goes through.

Blind rune-play is a first-class Campaign/Session policy, not a separate magic engine.

## 2. Verified design lineage

The final specification integrates the following verified PPIA-07 milestones:

- foundation PR #241 / merge `183d199d69f5cce121d4b971f33fe6c0145a6c45`;
- deterministic grammar/reference PR #242 / merge `15202626a0ba96d7675ee4ab4cbec4923158cd63`;
- cost/complexity/stability/progression PR #243 / merge `210ca8f13eaba7c1ea295c280368c68a13a300f3`;
- integrated Rune Builder workflows PR #244 / merge `f6ed3a71cf5dc01b14f85879e9acbdf5152af437`;
- owner-directed 34-rune expansion PR #245 / merge `86617eb2b9a823950708a88e1a049d5ec72e56d0`.

Retained source review established compositional precedent through Scripts, Macros, Sigilcrafting, rune engraving/enchanting, mana/charge/crafting/resource rules, resistance/counterspell, fatigue/Overreach and Resonance, but did not provide a canonical universal rune catalog or arbitrary-rune cost formula. The 34-rune vocabulary and deterministic construction language are therefore governed design, not recovered source canon.

## 3. Authority and downstream boundaries

PPIA-07 owns:

- Rune Construction vocabulary and semantic roles;
- deterministic syntax, parsing, grouping and serialization;
- Rune Construction Definition/extension semantics;
- SCI structural-complexity calculation;
- CSL composition-stability calculation;
- rune-specific validation, inspection, workflow and reference cases;
- rune-specific consumer profile for blind GM-adjudicated play;
- rune-specific inscription/enchanting extension data.

PPIA-07 does **not** absorb:

- PPIA-03 Item Definition/instance ownership;
- PPIA-08 Campaign, Scene and Session current-state ownership;
- PPIA-11 final encounter/power/balance calibration;
- PPIA-12 setting-local rule scope;
- MV-IA-F006/F007 authoritative Action/combat resolution;
- MV-IA-F020 permission/hidden-information authority;
- MV-IA-F021 recovery/idempotency authority;
- owning Ability, spell, resistance, counterspell, mana, crafting, progression or source-specific magic rules.

## 4. Final rune vocabulary — 34 core runes

### 4.1 Operation Runes — 16

Operation Runes describe **what the magic does**.

1. `SOURCE` — manifest, emit, generate or introduce an effect/substance/energy.
2. `MOVE` — move, push, pull, redirect, propel, relocate or transport.
3. `SHAPE` — impose geometry, area, boundary, path, volume or topology.
4. `BIND` — anchor, restrain, hold, seal, attach, stabilize or impose stasis.
5. `CHANGE` — transform a target, property, state, substance, form or relation.
6. `SENSE` — detect, reveal, identify, locate, measure or remotely perceive.
7. `WARD` — block, resist, suppress, absorb, shield from or exclude.
8. `LINK` — route, couple, synchronize, share, relay or transfer.
9. `RESTORE` — heal, repair, cleanse, replenish or return toward a governed prior/healthy state.
10. `UNMAKE` — damage, break, erode, unravel, negate, dispel, disintegrate or destroy under owning rules.
11. `VEIL` — hide, obscure, disguise, misdirect, mask or produce illusory sensory presentation.
12. `CALL` — summon, conjure, invite, draw or instantiate an allowed referenced creature/spirit/construct/object/effect.
13. `BANISH` — dismiss, exile, eject, return or sever a valid target from the current context.
14. `COMMAND` — influence, compel, soothe, frighten, confuse, inspire or alter behavior/emotion/intention under resistance rules.
15. `DRAIN` — reduce, suppress, siphon, exhaust, weaken or transfer a resource/energy/essence/capability.
16. `IMBUE` — infuse, enchant, empower, charge, bless, curse or persistently attach a magical property.

### 4.2 Essence Runes — 18

Essence Runes describe **what magical domain, medium or essence the operation acts through or upon**.

1. `FIRE`
2. `COLD`
3. `LIGHTNING`
4. `AIR`
5. `WATER`
6. `EARTH`
7. `ACID`
8. `FORCE`
9. `LIGHT`
10. `VOID`
11. `LIFE`
12. `MIND`
13. `SPIRIT`
14. `NATURE`
15. `SPACE`
16. `TIME`
17. `SOUND`
18. `ARCANE`

Essence Runes are typed payload/domain glyphs rather than standalone executable AST nodes. Canonical payload syntax is:

`payload=rune:ESSENCE_ID`

This preserves a readable verb-plus-domain mental model and prevents every elemental or metaphysical noun from becoming its own executable grammar branch.

## 5. Connection grammar — 4 explicit connectors

The final connection set is:

- `THEN` / `>` — ordered flow;
- `WITH` / `&` — explicit sibling/parallel composite;
- `WHEN` / `@` — trigger gate;
- `IF` / `?` — condition gate.

Mixed connector types never receive guessed precedence. Explicit grouping is mandatory whenever multiple connector kinds would otherwise be ambiguous.

Visual topology is supplemental. The canonical authoritative representation is an ordered linear serialization that round-trips to the same AST.

## 6. Typed modifier slots

The implementation-ready modifier vocabulary includes:

- `payload`;
- `target`;
- `geometry`;
- `direction`;
- `range_ref`;
- `area_ref`;
- `duration_ref`;
- `timing`;
- `condition`;
- `trigger`;
- `channel`;
- `anchor`;
- `to`;
- `destination_ref`;
- `state_ref`;
- `resource_ref`;
- `sense_ref`;
- `intent_ref`;
- `magnitude_ref`;
- `count_ref`;
- `persistence_ref`.

A modifier reference does not create a value that the owning rules do not define.

## 7. Canonical Rune Construction data model

A versioned Rune Construction carries at minimum:

- `runeConstructionId`;
- `version`;
- canonical linear expression;
- parsed AST;
- Operation Rune references;
- Essence Rune references;
- connector nodes and explicit groups;
- typed modifiers and external references;
- execution context;
- source/provenance and authoring authority;
- SCI and factor breakdown;
- CSL and factor breakdown;
- typed resource-adapter states;
- progression guidance;
- counterplay hooks;
- permission/reveal metadata;
- creation/update identities and timestamps.

Authoritative mutation also carries:

- `expected_version`;
- `operation_id`.

## 8. Deterministic parse and semantic evaluation pipeline

The implementation pipeline is:

1. authorize and permission-filter the construction context;
2. tokenize the canonical linear expression;
3. validate registered Operation Rune IDs, Essence Rune payload IDs, modifiers and references;
4. validate parentheses/grouping and connector legality;
5. build the AST;
6. normalize the AST without reordering semantically meaningful branches;
7. serialize canonically and verify round-trip identity;
8. calculate SCI;
9. calculate CSL;
10. resolve the execution profile;
11. request typed resource/capacity/crafting/progression/counterplay values from owning rules;
12. classify semantic resolution as `deterministic-supported`, `governed-adjudication-required`, `unresolved-owning-rule` or `invalid`;
13. construct a role-safe effect proposal;
14. route authoritative execution through the owning Action/approval/commit system.

A syntactically valid construction is not automatically affordable, successful, legal, unresisted or balanced.

## 9. Open-combination adjudication

The 34-rune vocabulary intentionally permits more combinations than the retained spell catalog explicitly enumerates.

When a valid combination has a registered deterministic semantic route, the evaluator produces a typed effect proposal.

When syntax is valid but the owning rules do not define enough information to produce an authoritative result, the evaluator marks the construction `governed-adjudication-required` or `unresolved-owning-rule`. It must not hallucinate a missing damage value, duration, creature template, resistance rule, destination, healthy state, crafting DC or other authoritative game fact.

A GM may use the existing modify-and-approve path to adjudicate permitted unresolved result fields while preserving the player's original construction and a complete semantic diff.

## 10. Standard rune-play mode

`rune_resolution_visibility_mode = standard-preview`

An authorized standard-mode player may receive permitted:

- rune meanings;
- parsed structure;
- semantic effect summary;
- SCI/CSL factors;
- known resource requirements;
- target/range/area/duration information;
- counterplay warnings;
- crafting/inscription compatibility;
- owning-rule references.

Permission filtering still occurs before any preview or aggregate is produced.

Whether a standard Rune Action still requires GM approval is controlled by the owning Action/Campaign policy. PPIA-07 never converts a preview into authoritative execution.

## 11. Blind rune-play mode — required capability

`rune_resolution_visibility_mode = blind-gm-adjudicated`

Blind rune-play is defined by the following invariant:

> The player constructs the runes; the system resolves the construction without exposing the interpreted effect to that player; an authorized GM is notified of the interpreted effect and explicitly chooses whether it goes through.

### 11.1 Player construction surface

The player may use the same Rune Builder to:

- choose permitted Rune glyphs;
- connect and group them;
- enter declared modifiers and visible targets;
- inspect canonical syntax;
- receive non-semantic syntax errors;
- save a local or permitted server draft;
- submit the construction.

The player must **not** receive predecision:

- interpreted effect summary;
- predicted damage/healing/conditions/movement/control/summon/banish/dispel result;
- hidden compatibility outcome;
- target secret state or hidden resistance;
- secret modifiers/difficulty;
- GM-only warnings;
- counterplay outcome;
- hidden setting-local magic rules;
- AI-generated effect decoding or GM-approval prediction.

Blindness is enforced through server-side role projection, not by sending effect data to the client and visually hiding it.

### 11.2 Blind submission states

The governed blind flow uses:

`local-draft` → `validating` → `ready-to-submit` → `submitted` → `pending-gm-decision` → `decision-in-review` → (`approved` | `modified-and-approved` | `denied`) → `commit-pending` → `completed`

with `stale`, `revoked` and `recovery-required` available when authoritative inputs change.

An invalid grammar construction does not create a GM proposal.

### 11.3 GM effect notification and approval card

The authorized GM or delegated Assistant-GM receives a permission-safe queue item and inspection card containing the complete decision context permitted to that decider, including:

- proposing player and actor;
- Campaign, Scene, Session and snapshot identities;
- visual construction and canonical linear serialization;
- decoded Operation/Essence sequence;
- interpreted effect summary;
- targets and expected target versions;
- range, area, duration, geometry, timing, triggers and conditions;
- resolved owning-rule resources/costs;
- SCI, band and factors;
- CSL, band and factors;
- counterspell, resistance, sever-link, disable-trigger, dispel/remove and other adopted counterplay hooks;
- crafting/inscription/item-bound data when applicable;
- unresolved adapters and ambiguity findings;
- source/provenance and setting-local scope;
- predicted authoritative Effects, Conditions, Resource changes, movement, summon/bind/banish state and other mutations;
- current permission, entitlement, pack, schema, rule and object versions;
- stale/conflict/revocation findings.

Opening the card does not approve or commit the construction.

### 11.4 Blind decision types

Final decision types are exactly:

- `approve`;
- `deny`;
- `modify-and-approve`.

Silence is never approval.

Approve revalidates and commits the reviewed resolved result.

Deny commits no accepted Rune Effect and records an attributable user-safe reason.

Modify-and-approve preserves:

- the immutable player construction;
- the original resolved proposal;
- every changed field;
- original and final values;
- reasons;
- decider identity and active authority;
- final revalidation evidence.

The GM may not silently rewrite the player's Rune Construction. If the expression is altered, the original and final expressions are both recorded and the changed expression is identified as a GM adjustment.

### 11.5 Post-resolution reveal policy

Blind play supports:

- `outcome-only`;
- `observed-details`;
- `full-after-resolution`.

Default blind policy is `observed-details`.

A successful construction does not automatically teach every Rune meaning or reveal GM-only mechanics. Rune discovery/identification may be layered on later only through explicit Campaign/progression rules.

## 12. GM-controlled rune actions

GM-controlled NPC/enemy Rune Actions use the same governed Action-result model and attributable confirmation path as other GM-controlled Actions.

The GM sees the full construction/result and must confirm the final decision before commit when the Campaign requires governed approval. This keeps one history/recovery model instead of creating a hidden bypass for GM actors.

## 13. Resource, cost and capacity contract

Rune Construction never defines one universal mana/cost equation.

Typed adapters are:

- `mana_ref`;
- `charge_ref`;
- `material_ref`;
- `time_ref`;
- `crafting_dc_ref`;
- `capacity_ref`;
- `fatigue_ref`;
- `overreach_ref`;
- `resonance_rule_ref`;
- `counterspell_ref`;
- `resistance_ref`;
- `progression_ref`.

Adapter states are `not_applicable`, `unresolved` or `resolved`.

If an owning rule requires an adapter and it is unresolved, authoritative execution may not substitute a guessed default.

## 14. Structural Complexity Index — SCI

SCI exists to measure authoring/cognitive complexity, not power.

`SCI = atom_count + connector_points + group_nesting_points + modifier_density_points`

Bands:

- `simple` — 1–3;
- `standard` — 4–6;
- `advanced` — 7–10;
- `expert` — 11+.

SCI may drive explanation depth, decomposition suggestions and progression guidance. It does not set damage, mana, success chance or balance.

## 15. Composition Stability Load — CSL

CSL is an explainable structural stability-attention signal informed by Scripts/Macros Resonance and crafting-failure precedent.

Bands:

- `baseline` — 0;
- `watch` — 1–2;
- `strained` — 3–4;
- `high-attention` — 5+.

CSL is not a failure probability, backlash table or damage formula. Final Resonance/failure calibration remains with adopted owning rules and PPIA-11.

## 16. Progression and teachability

Proposal-stage progression bands are:

- Band 0 — literacy: single-operation reading/inspection/validation;
- Band 1 — composition: small sequences, shaping, movement, binding and basic inscription;
- Band 2 — logic: explicit grouping, parallel composition, triggers, conditions and prepared logic;
- Band 3 — architecture: advanced/expert, LINK-heavy and deeply composed constructions.

The final experience uses progressive disclosure:

Starter Operations:
`SOURCE`, `MOVE`, `SHAPE`, `SENSE`, `WARD`, `RESTORE`

Starter Essences:
`FIRE`, `COLD`, `AIR`, `WATER`, `EARTH`, `FORCE`, `LIGHT`, `LIFE`

Advanced Operations:
`LINK`, `UNMAKE`, `VEIL`, `CALL`, `BANISH`, `COMMAND`, `DRAIN`, `IMBUE`, `CHANGE`, `BIND`

Advanced Essences:
`LIGHTNING`, `ACID`, `VOID`, `MIND`, `SPIRIT`, `NATURE`, `SPACE`, `TIME`, `SOUND`, `ARCANE`

Exact XP/perk prices remain source-scoped or future governed values. These bands do not silently choose between conflicting Scripts & Macros progression values.

## 17. Counterplay

Rune Constructions expose typed hooks without replacing owning rules:

- recognize;
- resist;
- counter;
- sever-link;
- disable-trigger;
- dispel-or-remove.

`UNMAKE`, `COMMAND`, `CALL`, `BANISH`, `SPACE` and `TIME` never bypass saves, resistance, counterspell, permissions, source/destination validity or setting-local restrictions.

Blind mode hides protected counterplay evidence from the player before adjudication but does not remove it from GM/authoritative resolution.

## 18. Crafting, enchanting and inscription

PPIA-07 supplies Rune extension semantics to the PPIA-03 Item model and the V08/SD-707 enchanting workbench.

Required inscription fields include:

- construction reference;
- substrate/item reference;
- execution context;
- compatibility state;
- resource adapters;
- predicted effect summary for authorized views;
- SCI;
- CSL;
- provenance;
- version.

Mutation uses expected-version and operation-ID recovery.

Blind-play inscription may hide the interpreted effect from the player while still giving the GM/crafter-authority projection needed for approval. It may not hide resource consumption from an actor when owning rules require that actor to know or authorize the expenditure.

## 19. Campaign, Scene, Session and setting integration

PPIA-08 owns placement, activation, current Scene/Session state and Campaign policy.

PPIA-12 owns setting-local magic scope.

A Campaign may select `standard-preview` or `blind-gm-adjudicated`; a Session may narrow but not silently widen the Campaign's visibility policy.

Setting-specific Rune limitations, cosmology, summon lists, planar destinations or local magic behaviors remain setting-scoped. Same-name Rune use in another setting does not universalize those rules.

## 20. Permission and hidden-information contract

Authorization and projection occur before:

- hidden rune meanings;
- hidden targets;
- anchors/channels;
- costs and resource values;
- effect previews;
- result interpretation;
- counts/badges/search/autocomplete;
- GM queue/notifications;
- history;
- exports;
- diagnostics;
- AI context.

A protected fact does not become inferable through error wording, count changes, disabled options or timing-visible metadata.

Blind mode adds an additional projection boundary: even otherwise-valid semantic interpretation is intentionally unavailable to the player before GM decision.

## 21. Idempotency, concurrency and recovery

Every authoritative Rune mutation, proposal submit, GM decision and commit uses stable operation identity.

If a response is ambiguous:

1. query status using the original operation/decision identity;
2. obtain current authoritative version/status;
3. retry only with the original identity and compatible payload;
4. never create duplicate proposal, cost, inscription, Effect, Condition or notification.

Only one final GM decision may win.

Stale actor, target, resource, permission, Session or rule versions cause revalidation/stale/recovery-required behavior, not silent acceptance.

## 22. Offline behavior

Offline users may:

- read unexpired authorized cached rune/library projections;
- create/edit local drafts;
- use deterministic syntax parsing that does not require protected semantic resolution;
- inspect canonical linear serialization.

Offline users may not:

- submit a Rune Action;
- obtain server-hidden blind effect resolution;
- approve/deny/modify;
- spend resources;
- apply Effects/Conditions;
- create authoritative inscription;
- mutate Session state.

Reconnect reauthorizes before submission or semantic projection.

## 23. Accessibility and adaptive interaction

Every visual rune graph has an equivalent ordered text representation.

Keyboard, touch, screen-reader, high-zoom/reflow and reduced-motion users can:

- select runes;
- edit typed payloads/modifiers;
- create groups/connectors;
- reorder constructions;
- parse/validate;
- inspect SCI/CSL where permitted;
- submit;
- review GM approval cards where authorized;
- approve/deny/modify where authorized;
- recover from conflicts.

Blind gameplay never means visual-only gameplay. A screen-reader player can be mechanically blind to the interpreted effect while still receiving all permitted construction controls and syntax feedback.

Color, drag, hover, animation and geometric placement are never required for authoritative meaning.

## 24. AI boundary

AI is optional and advisory.

In standard mode an AI may receive only the user's authorized projection.

In blind mode player-facing AI may help with:

- syntax;
- accessibility;
- organization;
- explaining already-known Rune concepts.

It may not:

- decode or predict the suppressed effect;
- use hidden source/target state to infer the outcome;
- predict whether the GM will approve;
- approve, deny, modify or commit.

GM-side AI may inspect an authorized GM decision projection only as an advisory assistant. It has no decision authority.

## 25. Retained spell-catalog compatibility

The verified coverage audit examined 385 retained spells across:

- 10 primary magic schools;
- 7 gameplay roles;
- 14 normalized effect families;
- 22 normalized subtype families.

All 14 effect-family tokens route to the 16 Operation Runes and all 22 subtype tokens route to the 18 Essence Runes, with zero vocabulary-level unroutable spell IDs.

This is a vocabulary-routing guarantee, not an automatic exact-spell reconstruction guarantee. Source-specific spell fields remain authoritative owning-rule inputs.

## 26. Representative constructions

These examples demonstrate language expressiveness, not final balance values.

- fire cone: `SOURCE[payload=rune:FIRE]>SHAPE[geometry=cone]`
- force push: `SOURCE[payload=rune:FORCE]>MOVE[direction=away]`
- healing: `RESTORE[payload=rune:LIFE,target=ally]`
- dispel: `UNMAKE[payload=rune:ARCANE,target=effect-ref]`
- invisibility/concealment: `VEIL[payload=rune:LIGHT,target=self]`
- charm/compulsion: `COMMAND[payload=rune:MIND,target=creature]`
- summon spirit: `CALL[payload=rune:SPIRIT,target=spirit-ref]`
- banishment: `BANISH[payload=rune:SPACE,target=outsider]`
- life drain: `DRAIN[payload=rune:LIFE,target=creature]`
- flaming weapon: `IMBUE[payload=rune:FIRE,target=item-ref]`
- temporal bind: `BIND[payload=rune:TIME,target=creature]`
- teleport: `MOVE[payload=rune:SPACE,target=self,destination_ref=marker]`
- arcane detection: `SENSE[payload=rune:ARCANE,target=area]`
- conditional ward: `SENSE[payload=rune:ARCANE]@WARD[payload=rune:ARCANE]`
- mixed storm: `(SOURCE[payload=rune:LIGHTNING]&SOURCE[payload=rune:AIR])>SHAPE[geometry=storm-field]`

The same expression can be used in standard or blind mode; only the role-safe semantic projection and decision requirement differ.

## 27. Reference and acceptance corpus

The final completion contract preserves and validates:

- 20 deterministic grammar/reference cases `PPIA07-RC-001..020`;
- 34 expanded-rune cases `PPIA07-ER-001..034`;
- 16 cost/stability/progression benchmarks `PPIA07-CSP-001..016`;
- 16 Rune Builder workflows;
- 18 Rune Builder actions;
- 10 cross-domain handoffs;
- 16 blind rune-play cases `PPIA07-BR-001..016`;
- 48 final acceptance requirements across 16 categories.

No final completion claim is valid if any required set is missing or if blind-mode effect suppression/GM approval can be bypassed.

## 28. Completion boundaries

PPIA-07 completion does **not**:

- claim the 34-rune catalog came verbatim from source;
- turn every spell into a rune;
- define one universal mana/cost/damage/healing/XP equation;
- convert SCI to power or CSL to failure probability;
- guarantee balance;
- bypass resistance, counterspell, saves, target validity, crafting requirements or setting-local rules;
- let blind-mode players recover hidden effect semantics through client payloads, AI, diagnostics, exports or notifications;
- permit silence/timeout to become GM approval;
- permit a GM to erase or silently rewrite the player's submitted construction;
- permit offline authoritative rune execution;
- activate STAGE-A-A2;
- mutate application runtime;
- authorize release, deployment, tester access, paid services or production credentials.

## 29. Implementation slices

1. 34-rune registry, metadata and icon/glyph slots;
2. canonical parser, AST and round-trip serializer;
3. Rune Builder visual + linear editors;
4. semantic evaluator and owning-rule adapters;
5. SCI/CSL/resource/progression inspector;
6. standard preview projection;
7. blind Rune Action consumer profile and GM effect card;
8. approve/deny/modify-and-approve + atomic commit adapter;
9. counterplay and Action/combat integration;
10. inscription/enchanting integration;
11. Campaign/Session visibility policy and setting-local scope;
12. permissions, history, export, diagnostics and AI filtering;
13. recovery/idempotency/reconnect/offline draft support;
14. accessibility and adaptive interaction;
15. regression corpus and completion acceptance gates.

## 30. Readiness statement

This specification is ready to become the implementation-ready PPIA-07 completion contract only after the exact completion-candidate head passes the dedicated PPIA-07 completion validator plus every applicable repository regression gate and merges into canonical `main`.

Until that merge occurs, PPIA-07 remains `started` and this document remains a completion candidate.
