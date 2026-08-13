# MXS-12 — Product Superset and Stage A Reconciliation

**Version:** 0.1.0  
**Status:** STRATEGY DESIGN / PREIMPLEMENTATION RECONCILIATION  
**Prepared:** 2026-08-13  
**Owner/final authority:** John Brandon Turner

## Purpose

MXS does not restart Multiversal planning. It sharpens a platform architecture that already contains substantial foundations.

The current Stage A program remains structurally sound: A2 Universal Object Experience is still the authorized next application item, and its work order explicitly forbids a later Stage A item from superseding it without satisfying the governed exit gate. MXS therefore attaches strategic requirements to existing stages and creates cross-cutting contracts only where necessary.

No new giant pre-A2 implementation phase is introduced.

## Existing source alignment

MXS is strongly aligned with retained Multiversal source design rather than being a late product pivot.

### UI Design Bible already establishes
- Player, GM, Live-session, Authoring, Reference and AI-assisted primary experience modes;
- a calm/fast long-session interface across desktop/tablet/phone;
- accessible use without dependence on color, motion or pointer;
- density suitable for both dense GM and simplified player workflows;
- proposal-first, explainable, provenance-visible AI;
- cognitive accessibility, undo where feasible, consequence explanation and progress feedback.

### Screen Design Bible already establishes
- Character, Inventory, Combat, Investigation, Social, Exploration, Crafting, Economy, Vehicles/Bases, Campaign/World Authoring and AI/Admin screen families;
- global search/provenance;
- responsive and accessibility requirements;
- permission handling;
- recovery/offline states;
- cross-screen traceability;
- primary journeys including onboarding, returning player, live session, investigation and GM authoring/runtime.

### Feature Bible already establishes
- Social Systems;
- Economy;
- Crafting;
- Exploration;
- Bases/Housing;
- Vehicles;
- cross-system governed events;
- global AI integration;
- implementation/readiness governance.

MXS changes the **product strategy and compositional layer**: those domains should not merely coexist as screens. They should participate in common play primitives, Play Experience Profiles, causal history, creator architecture and meaningful cross-domain consequence.

---

# Reconciliation vocabulary

Every MXS requirement is classified as:

- **SATISFIED FOUNDATION** — existing design/implementation is already structurally adequate; do not reopen completed work.
- **EXISTING STAGE ENHANCEMENT** — add requirements to a planned Stage A item.
- **RECOVERED / RECONCILE** — useful older Stage A preparation exists but must be refreshed against current authority.
- **CROSS-CUTTING CONTRACT** — define a reusable contract consumed by multiple stages; this is not a separate product phase unless implementation evidence later requires one.
- **POST-ALPHA EXPANSION** — strategically required but not necessary for initial internal-alpha completion.
- **NATIVE-SPATIAL DEFERRED** — bridge now; deeper native VTT maturity later.

---

# MXS program impact

## MXS-01 Industry Capability Baseline

**Classification:** CROSS-CUTTING PRODUCT GATE.

Existing Multiversal designs already cover much of the nonspatial baseline: Character, content, Campaign, world, social, investigation, crafting, economy, vehicle/base, AI, permissions, provenance and responsive interfaces.

New requirement:
Every major Stage A feature family should be evaluated through:
1. Parity Gate;
2. Integration Gate;
3. Multiversal Gate.

This should become an acceptance-template addition rather than a separate implementation stage.

## MXS-02 Playstyle Atlas

**Classification:** CROSS-CUTTING DESIGN AUTHORITY.

The atlas prevents combat-centric or D20-centric assumptions. Existing Feature Bible domain breadth strongly supports this goal, but the current Stage A sequence does not explicitly identify different kinds of play as profile-level concepts.

New requirement:
Affected stages must state which Play Experience Profiles they support and which they intentionally do not.

## MXS-03 Universal Play Primitive Model

**Classification:** CROSS-CUTTING CONTRACT + EXISTING STAGE ENHANCEMENTS.

Multiversal already contains many candidate primitives through game framework/domain architecture (Actions, Effects, Conditions, resources, relationships, clues, projects, etc.). MXS does **not** authorize rewriting those objects into a new generic engine.

Required work during implementation:
- create a semantic registry mapping existing canonical mechanics to the MXS primitive vocabulary;
- identify genuine missing primitives such as generic Play Experience Profile, Authority Profile, Clock/Track, KnowledgeState or Oracle only where existing canonical structures do not already cover them;
- preserve domain-specific types when abstraction would remove meaningful semantics.

## MXS-04 Human Experience Design

**Classification:** CROSS-CUTTING ACCEPTANCE STANDARD.

Do not create a “psychology subsystem.” Add the Human Experience acceptance questions to product/UX review: autonomy, competence, relatedness where relevant, cognitive load, feedback, safety/consent, progressive complexity, recovery, meaningful history and anti-manipulation.

## MXS-05 GM Cognitive Load

**Classification:** A5/A6/A7/A9/A10/A11 ENHANCEMENT.

The Contextual GM Cockpit should evolve incrementally across existing GM runtime surfaces rather than being built as a standalone dashboard before those domains exist.

## MXS-06 Social/Table Dynamics

**Classification:** A3/A5/A12 ENHANCEMENT, with POST-ALPHA expansion for advanced shared-authority modes.

Internal Alpha should establish:
- session-zero/table preference storage;
- privacy/consent boundaries;
- AI-use preference;
- table-display role;
- assistant-GM/co-GM authority where already supported.

Full GMless/solo/shared-facilitation orchestration may mature after the core Campaign model is stable, but its authority model must not be architecturally forbidden.

## MXS-07 Progressive Complexity

**Classification:** A2 onward CROSS-CUTTING UI CONTRACT.

A2 is the earliest practical proving ground: Universal Object search/inspection should demonstrate progressive disclosure without maintaining separate truth models.

## MXS-08 World Pulse / Campaign Memory

**Classification:** A5/A6/A9 + CROSS-DOMAIN EVENT FOUNDATION + post-A8/A10 enrichment.

Start small:
- structured recent activity;
- per-object history;
- session result/event digest;
- unresolved thread references.

World Pulse grows naturally as more domains become implemented.

## MXS-09 Creator Ecosystem

**Classification:** A10 MAJOR ENHANCEMENT with earlier A2/A3/A5 prerequisites.

A10 should become the primary implementation home for the creator capability ladder and declarative Rules/Play Experience Profile authoring.

Do not require executable plug-ins or marketplace launch for Internal Alpha.

## MXS-10 VTT Bridge / Spatial Strategy

**Classification:** A5/A7 CROSS-CUTTING + NATIVE-SPATIAL DEFERRED.

Internal Alpha should support S0/S1 and selected S2 behavior as evidence allows. Mature S3–S5 VTT behavior should not block the broader platform. External bridge/export contracts should preserve Multiversal as authority.

## MXS-11 Signature Experience Layer

**Classification:** DISTRIBUTED ACROSS A2–A12.

Signature experiences are cumulative outputs of existing stages; they are not a new giant stage after A12.

## MXS-12 Product Superset Reconciliation

**Classification:** CURRENT STRATEGY AUTHORITY once integrated and merged.

---

# Stage-by-stage sharpened implementation strategy

## STAGE-A-A2 — Universal Object Experience

**Current state:** AUTHORIZED CURRENT NEXT; recovered deep preimplementation package exists and must be reconciled, not rebuilt.

### Preserve existing objective
Find, filter, inspect, select and pass real governed objects into another workflow on desktop/mobile.

### Add MXS gates

#### A2-MXS-01 — Profile-neutral object identity
Object browsing/inspection cannot assume one game system, one genre, one Character schema or one play mode.

#### A2-MXS-02 — Capability-aware inspection
Inspector can surface registered capabilities such as Action provider, Resource carrier, equippable, relationship participant, clue/evidence, vehicle, location or other canonical capabilities without hard-coded domain forks where Generic presentation suffices.

#### A2-MXS-03 — Progressive complexity proof
At least one real object demonstrates Guided/Standard/Advanced-or-Diagnostic information depth over the same canonical data.

#### A2-MXS-04 — Permission-before-derivation
Search facets, counts, relationship graphs, provenance, variants and AI-compatible retrieval cannot leak hidden objects or fields.

#### A2-MXS-05 — Creator seam
Object identity/provenance/version model must be usable by later Campaign-local/community/publisher content without redesign.

#### A2-MXS-06 — External reference/export seam
Stable IDs and presentation derivatives can be referenced by later VTT/bridge adapters without making external IDs canonical.

### Do not add now
- full Rules Profile editor;
- full Play Experience Profile runtime;
- VTT map engine;
- World Pulse simulation;
- AI provider integration.

A2 should **enable** those later stages, not absorb them.

---

## STAGE-A-A3 — Identity, Dashboard and Workspace Selection

### Add MXS gates
- selected context can identify active Campaign/Character/Rules Profile and later Play Experience Profile without client-authoritative permission;
- dashboard supports returning-user re-entry rather than merely navigation;
- table/session preferences and AI consent have explicit ownership/privacy;
- a shared-display/table-display projection role can exist without inheriting GM permissions;
- role architecture must not prohibit future co-GM/rotating/solo profiles.

### Signature contribution
Begins Campaign Re-entry and Playstyle Compass foundations.

---

## STAGE-A-A4 — Character Workspace

### Reconciliation
Use recovered A4 lifecycle/control preparation; PPIA/CAPP are newer authority for appearance-specific contracts.

### Add MXS gates
- Character representation supports configurable Resources, Conditions, drives/goals/relationships and capability groups without forcing unused fields;
- Character history is queryable/provenance-preserving;
- Character builder uses progressive complexity;
- rules explanations are contextual to the actual choice;
- no Character optimization recommendation becomes implicit authority;
- appearance/personality/relationship/history are not secondary metadata if the active Rules/Profile treats them as mechanically meaningful.

### Signature contribution
Progressive Complexity, Character continuity and later Why Engine.

---

## STAGE-A-A5 — Campaign and Scene Workspace

### Add MXS gates
- Campaign declares Rules Profile(s) and enabled Play Experience Profile(s) when that contract exists;
- Scene can select a presentation/play profile without changing object identity;
- S0 theater-of-the-mind is complete and first-class;
- S1 abstract zones/range relations are representable;
- optional static visual/map references remain projection metadata;
- Session Zero/Table Contract/Playstyle Compass has a bounded home;
- Scene/Campaign history exposes structured recent changes;
- shared-table display uses permission-safe projection;
- GM cockpit begins with context-relevant cast, secrets, pending decisions and unresolved threads.

### Signature contribution
Play Experience Profiles, GM Cockpit, Hybrid Table, Campaign Re-entry.

---

## STAGE-A-A6 — First Playable Action and Approval Loop

### Existing architecture fit
The recovered A6 package already has a strong proposal/GM-decision/authoritative-result model.

### Add MXS gates
- result semantics must support more than binary success/failure where Rules Profile declares outcome bands;
- Action proposal can carry explicit stakes/position/effect or other profile-specific metadata without making those universal required fields;
- consequence/mitigation can be represented as governed optional stages;
- result explanation can expose Guided/Standard/Advanced depth;
- committed result emits structured events suitable for World Pulse/Why Engine;
- bounded consequence preview distinguishes deterministic rule effects from uncertain inference.

### Signature contribution
Governed Automation, consequence preview, causal history.

---

## STAGE-A-A7 — Full Combat Interface

### Strategic correction
Combat is **a** Play Experience Profile, not the universal session model.

### Add MXS gates
- tactical profile supports initiative/actions/resources/conditions/position;
- a cinematic/non-grid encounter path remains viable where Rules Profile permits;
- combat information density can be reduced progressively;
- spatial implementation respects S0–S5 maturity and cannot make unavailable high-end map features a blocker for nonspatial combat;
- complete event/result history feeds campaign memory.

### Signature contribution
Proof that one world can move into/out of a dense tactical profile without changing canonical object identities.

---

## STAGE-A-A8 — Inventory, Equipment, Crafting and Vehicles

### Add MXS gates
- generic Project/Clock/Procedure semantics are reused where appropriate rather than every crafting/research/repair workflow inventing progress tracking;
- Assets preserve ownership/custody/control/equipment/installation distinctions;
- vehicle scale can transition between Character, travel and tactical contexts;
- CAPP presentation/wardrobe projection never becomes equipment truth;
- project/crafting/vehicle changes emit causal history suitable for World Pulse.

### Signature contribution
Cross-scale continuity and living-world economic/crafting consequences.

---

## STAGE-A-A9 — Investigation and Social Workspaces

### Strategic importance
A9 is one of Multiversal's strongest near-term differentiators because deep investigation/social support does not depend on full native VTT maturity.

### Add MXS gates
- Clue/Evidence, Hypothesis and KnowledgeState semantics are explicit;
- core information cannot be accidentally blocked by a single perception-style failure unless Rules Profile explicitly defines that behavior;
- hypothesis does not become truth;
- graph/list/timeline views preserve hidden-information safety;
- social scenes consume relationship/reputation/faction state and produce persistent events;
- promises/debts/obligations can participate in Campaign Re-entry/World Pulse;
- contextual GM cockpit surfaces relevant motives/secrets/clues without broad searching.

### Signature contribution
Why Engine, World Pulse, Campaign Memory, cross-domain social consequences.

---

## STAGE-A-A10 — World Builder and Content Creation

### Strategic expansion
A10 should become **Creator Platform Alpha**, not merely a world editor.

### Add MXS gates
- creator capability ladder C0–C4 has an explicit architecture;
- content namespaces/stable IDs/version/dependencies/provenance are usable without executable code;
- bounded declarative Rules Profile creation/import can be exercised;
- Play Experience Profile creation/selection contract can be exercised for at least one nondefault profile;
- creator validation harness reports compatibility, permission, migration and Generic-fallback problems;
- private/Campaign/workspace/community/publisher authority tiers remain distinct;
- future marketplace is an optional distribution layer, not content identity.

### Deferred
C5 arbitrary/governed executable extension ecosystem unless a real use case cannot be expressed declaratively.

### Signature contribution
Universal Creator Layer and ecosystem defensibility.

---

## STAGE-A-A11 — Contextual AI Interfaces

### Existing architecture fit
Recovered A11 and Feature Bible already establish redaction-before-context, proposal-first behavior, provider independence, cost controls and deterministic manual fallback.

### Add MXS gates
- AI context includes active Rules/Play Experience/Authority profile when relevant;
- AI explanations cite structured source/provenance wherever possible;
- AI may query Why Engine/World Pulse evidence but must label inference;
- AI cannot turn simulation/consequence preview into canonical world progression;
- AI assistance level respects table/session consent;
- all signature workflows retain complete non-AI paths.

### Signature contribution
Governed AI over Structured Truth.

---

## STAGE-A-A12 — Internal-alpha Hardening

### Add MXS gates
Internal-alpha hardening must test not just features, but **breadth of play**.

At minimum validate representative journeys for:
1. guided beginner Character/reference use;
2. tactical encounter;
3. theater-of-the-mind Scene;
4. investigation/social Scene;
5. crafting/project or vehicle flow;
6. returning-user Campaign re-entry;
7. GM live decision queue/cockpit;
8. creator-defined content under Generic presentation;
9. optional AI on/off parity;
10. desktop/mobile/hybrid-table roles.

Add adversarial tests for:
- hidden information leaking through World Pulse/graphs/AI;
- profile transition losing state;
- creator package widening authority;
- unsupported primitive combination;
- stale Rules/Profile version;
- external spatial adapter identity collision;
- cognitive-depth view changing authority;
- offline/reconnect across a profile transition.

### Signature contribution
Proves the platform thesis under multiple kinds of play rather than proving one demo path.

---

# Cross-cutting contracts to add without a new stage

## MXC-01 — Product Value Gate Template
Every substantial Stage A package records Parity / Integration / Multiversal outcomes.

## MXC-02 — Play Experience Profile Contract
Define schema/authority/versioning for profile identity, active primitives, UI/pacing/spatial/authority requirements and incompatibilities.

Timing: design contract can be finalized before A5 uses it; A2/A3 need only reserve profile-neutral seams.

## MXC-03 — Human Experience Acceptance Standard
Attach the ten-question MXS human-experience review to screen/workflow acceptance.

## MXC-04 — Campaign Causal Event Contract
Clarify which existing events/relations are sufficient for per-object history, session digest and later causal paths.

Timing: evolve with A5/A6; do not build a graph database preemptively.

## MXC-05 — Creator Capability Manifest
Define what content/Rules/Profile packages may declare and what capabilities require stronger trust.

Timing: finalized before A10 implementation.

## MXC-06 — Spatial Bridge Contract
Stable IDs, placement identities, presentation derivatives and bounded external adapter data.

Timing: define by A5/A7; full adapter implementations may follow later.

---

# What MXS does NOT change

1. **A2 remains next.** Strategy is not a reason to bypass the existing work order.
2. **A1 is not reopened.** Existing shell/design-system work remains foundation; MXS requirements are consumed by later screens/components and future refinements.
3. **PPIA is not reopened.** Its completed artifacts remain upstream design authority.
4. **CAPP is not reopened.** Appearance production stays completed; later Character UI consumes it.
5. **IA-D01–D09 are not reopened.** MXS broadens product strategy but consumes completed IA design.
6. **DS-008 is not reconstructed.** Exact-byte Design Standards blocker remains separate.
7. **WP-011 remains separate.** Apple/Mac validation is not a dependency of MXS planning.
8. **Full VTT is not inserted before A2–A12.** Spatial maturity is staged.

---

# Product maturity horizons

## Horizon H1 — Internal Alpha / prove the operating model
Focus:
- A2–A12 current sequence;
- profile-neutral foundations;
- theater-of-the-mind + abstract spatial support;
- strong Character/Campaign/GM/noncombat workflows;
- guided/advanced presentation;
- creator alpha;
- basic Campaign Re-entry/World Pulse;
- optional governed AI architecture;
- bridge/export foundations.

## Horizon H2 — Play Superset expansion
Focus:
- more built-in Play Experience Profiles;
- stronger living-world projects;
- deeper World Pulse/Why Engine;
- richer solo/co-op/shared authority;
- advanced creator certification;
- external VTT adapters;
- native S2/S3 spatial maturity;
- community/package discovery.

## Horizon H3 — Native tabletop platform maturity
Focus:
- S4/S5 native spatial visibility/automation;
- broader publisher ecosystem;
- robust Rules/Profile SDK;
- large-scale campaign/world simulation;
- deep causal graph;
- marketplace/distribution if strategically justified;
- advanced spatial/3D adapters where demand supports them.

---

# Strategic acceptance conditions for Stage A as a whole

When Stage A reaches its eventual completion, the platform should be able to demonstrate:

1. **Breadth:** more than one kind of tabletop play is genuinely supported.
2. **Continuity:** the same governed objects survive transitions among workflows/play modes.
3. **Human fit:** beginner and expert can use the platform without separate truth models.
4. **GM leverage:** the system reduces retrieval/state/consequence burden rather than becoming another burden.
5. **Creator leverage:** creators reuse platform services rather than rebuild an app stack.
6. **Trust:** permissions, provenance, recovery and human authority remain inspectable.
7. **Memory:** users can recover what happened and why.
8. **Interoperability:** lack of full native VTT parity does not trap the Campaign.
9. **Differentiation:** at least several signature experiences are demonstrably stronger because multiple domains are connected.
10. **No dark-pattern dependency:** success is measured by quality/continuity of play and creation, not compulsive app engagement.

## Conclusion

MXS does not require a new development restart. It gives the existing architecture a more ambitious definition of success.

The central implementation strategy remains:

> Build A2 through A12 as connected vertical slices, but evaluate every slice not only for functional completion—also for parity with the best user value already available elsewhere, integration with the Multiversal canonical model, and the additional experience made possible by that integration.
