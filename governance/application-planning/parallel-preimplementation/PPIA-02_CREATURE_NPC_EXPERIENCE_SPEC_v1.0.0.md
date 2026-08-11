# Multiversal PPIA-02 — Creature & NPC Experience Specification

**Version:** 1.0.0  
**Work item:** PPIA-02 — Creature & NPC Experience  
**Status:** IMPLEMENTATION-READY DESIGN CANDIDATE — SUBJECT TO EXACT-HEAD VALIDATION AND MERGE  
**Owner:** John Brandon Turner

## 1. Purpose

This specification defines how Multiversal presents, authors, places, compares, runs, discovers, relates, transforms, summons, and converts creatures and NPCs without creating a separate incompatible object system.

It specializes the existing Universal Object Experience, Campaign/Scene Builder, Encounter Builder, combat/runtime, investigation/social, exploration, inventory, relationship, and provenance contracts. It does **not** authorize implementation, A2 activation, canonical-content promotion, source mutation, or release.

## 2. Source and authority boundary

Creature-domain source truth is preserved in the retained original PDFs. PPIA-02 inventoried 23 dedicated Creature PDFs plus `Player Creatures.PDF` with exact SHA-256 evidence.

The later 8E-009 CSV-first registry remains authoritative for its own 20 datasets / 19,199 rows, but it contains no dedicated Creature catalog. The earlier 487-object semantic-parse database is therefore **not** restored as Creature/NPC content authority. Its sparse creature objects may be useful as compatibility fixtures only.

PPIA-01 controls the source-quality boundary:

- source text/facts remain distinguishable from inference/recommendation;
- source absence is not silently filled as source fact;
- same-name records are not automatically merged;
- conflicts remain visible until governed resolution;
- raw source is not rewritten to make presentation cleaner.

## 3. Core experience model

Creature/NPC experience is composed from seven distinguishable layers:

1. **Reusable Definition** — governed source/version identity.
2. **Presentation Profile** — information ordering/emphasis only; never a new canonical type.
3. **Variant / Template / Type-Modifier Relationship** — source-backed sibling, stage, form, modifier, or template relationship.
4. **Campaign / Scene Placement** — Campaign-local identity for quantity, visibility, local label, starting state, encounter role, and permitted override.
5. **Live Instance** — runtime HP/resources/conditions/location/initiative/control state.
6. **Playable Conversion** — governed relationship/handoff from creature source to playable species/Character construction.
7. **Source & Provenance** — source coordinates, transformations, recommendations, conflicts, validation, and history.

No context is allowed to collapse Definition, placement, and live instance into one identity.

## 4. Presentation profiles

PPIA-02 defines eight presentation profiles. They select section priority, not authority or object identity.

### 4.1 Creature

Foreground:
- encounter summary;
- actions/traits;
- defenses/resources;
- movement/senses;
- ecology/behavior.

Use for ordinary bestiary and combat/ecology-first creatures.

### 4.2 NPC Persona

Foreground:
- identity/persona;
- relationships/social context;
- motives/goals;
- statements/reliability where authorized;
- encounter summary.

Use when social identity and Campaign role matter more than raw stat density.

### 4.3 Sentient Creature / NPC Hybrid

Foreground both creature mechanics and persona/social information. This supports source patterns such as intelligent dragons, sapient animals, or other beings that are neither “monster stat block only” nor “humanoid NPC only.”

### 4.4 Swarm / Group

Foreground group identity, quantity/scale, group mechanics, movement/senses, and behavior while preserving member/source relationships.

A group profile does not erase member identity and does not equate source group scale with hidden Scene placement count.

### 4.5 Summon / Minion / Spawn

Foreground summoner/master/controller relationship, lifecycle/control rules, encounter summary, actions, and any resource/count/duration limit.

Summoner, controller, owner, source creator, placement, and live instance are separate concepts unless governed data explicitly makes them the same.

### 4.6 Stage / Variant / Form

Foreground variant identity, differences, stage requirements, encounter summary, and changed mechanics.

Source-specific stage models remain partial. For example, Dragon categories are not forced into one universal age ladder merely because several categories share stage names.

### 4.7 Type / Affinity Modifier

Foreground applies-to relationship and field-level effects such as resistance, vulnerability, abilities, environmental adaptation, and appearance.

This directly supports `Creature types.PDF`, where creature types can behave as adjustment layers. Conditional source language such as “may” remains conditional.

### 4.8 Playable Conversion

Foreground source creature, chosen base version, retained physical traits, unlockable abilities, normalization, XP/progression, exclusions, and conversion provenance.

The result is a playable species/Character draft, never the original monster instance under a new label.

## 5. Universal Creature/NPC Inspector

The specialized Inspector remains one implementation of the Universal Object Experience. It uses thirteen governed information groups when available and authorized:

1. Identity & status
2. Encounter summary
3. Attributes, saves, skills & proficiencies
4. Traits, Actions, Abilities, reactions & passives
5. Defenses, resistances, vulnerabilities, immunities & Conditions
6. Ecology, habitat & behavior
7. Persona, relationships, reputation & faction context
8. Assets, equipment, inventory & loot
9. Variants, templates, type modifiers, stages, forms & transformations
10. Summon/control relationships
11. Campaign/Scene placement context
12. Live runtime state
13. Source, provenance, conflict & validation

Optional source fields may be absent without placeholder invention. If a source has combat statistics but no ecology, ecology is omitted or explicitly unknown; if it has behavior but no formal stat, behavior remains source content rather than being discarded because the stat section is incomplete.

### Linked-object behavior

Where a governed Ability, Action, Effect, Condition, Item, Relationship, Faction, or other object owns a rule, the Creature/NPC experience prefers a stable reference plus quick Rule Inspector instead of copying and forking the rule text.

### Context overlays

The same source Definition may be viewed in different contexts:

- Library/reference: no placement/runtime state.
- GM authoring: Campaign-local authoring context.
- Scene placement: placement controls foregrounded.
- Encounter preparation: encounter role, quantity, wave, assumptions and warnings foregrounded.
- Live runtime: placement + current instance state foregrounded.
- Investigation/social: persona/relationships/statements foregrounded.
- Exploration/bestiary: ecology/behavior/discovery foregrounded.
- Comparison/variant: differences/source provenance foregrounded.
- Summon/minion: control/lifecycle foregrounded.
- Playable conversion: conversion inputs/results foregrounded.

Changing context never changes source truth or permission automatically.

## 6. Permission-safe projection

Authorization must occur before serialization and before search suggestions, counts, facets, relationships, variant lists, compare targets, provenance labels, or other derived data are computed.

### Player

May receive only authorized:
- revealed identity;
- visible mechanics;
- known ecology/lore;
- revealed relationships/reputation/statements;
- shared runtime state;
- permitted source detail.

Must not receive before reveal:
- hidden creature/NPC existence;
- hidden exact counts;
- reserve waves/reinforcements;
- secret motives;
- hidden relationships/faction ties;
- unrevealed weaknesses/immunities/forms;
- private GM tactics/notes;
- hidden inventory/loot/rewards;
- hidden source diagnostics or labels that reveal secret existence.

### GM

May receive authorized Campaign preparation/runtime truth and diagnostics, but GM status does not automatically grant other-Campaign private data or user-private notes.

### Assistant GM

Access is explicit delegation scope plus Campaign scope and expiry; Assistant GM is never an unrestricted alias for GM.

### Creator / Owner / Admin

May inspect source/governance information according to separate authority. Administration is not automatic entitlement to every Campaign-private or user-private field.

### Service / AI

Receives the minimum operation-specific role-safe projection. AI remains advisory/proposal-only, cannot reconstruct hidden state, and cannot turn unknown source fields into source facts.

## 7. GM NPC & Creature Manager

The GM core experience needs a dedicated manager composed from shared Library/Inspector/authoring patterns rather than a bespoke second database.

It supports:
- search/filter/open source Definitions;
- Campaign-local NPC/creature drafts;
- source-linked or Campaign-local persona information;
- linked Abilities/Actions/Items/Relationships/Factions;
- ecology/behavior references;
- equipment/inventory links;
- variants/templates/forms;
- private/revealable/public field classification;
- source/conflict/recommendation diagnostics;
- validation before save/use.

It must not:
- edit original PDF-derived source data through the Inspector;
- silently publish Campaign-local notes into a reusable Definition;
- copy linked rule text merely to make the NPC self-contained;
- expose hidden authoring data to Player projections early.

Autosave and recovery preserve the source/local distinction and revalidate target references before final commit/use.

## 8. Scene placement and quick-add

Quick-add is a governed handoff, not a direct mutation of the current Inspector object.

Flow:
1. authorize Scene editing;
2. authorize exact source Definition/version;
3. use constrained Picker or provisional Inspector selection;
4. revalidate selection;
5. set local label where allowed;
6. set quantity;
7. set visibility/reveal policy;
8. set encounter role/wave/starting assumptions;
9. apply permitted local overrides with provenance;
10. create distinct `placementId`;
11. persist through Scene/Campaign authoring.

A single Definition may have many placements. A placement never overwrites the Definition.

## 9. Encounter preparation

Encounter Builder consumes exact participant source/version/pack identity and any Campaign placement.

It supports:
- participant role;
- quantity;
- wave/reinforcement placement;
- starting assumptions;
- visible/hidden status;
- normalized analysis fields with provenance;
- missing/inferred/recommended value warnings;
- advisory encounter-pressure analysis;
- uncertainty and compatibility warnings;
- immutable launch-ready participant snapshot.

Balance output is advisory. It may not claim guaranteed difficulty or fabricate a missing creature mechanic merely to produce a score.

Player/Observer projections exclude hidden participant identities, counts, waves, tactics, secret objectives, and GM-only warnings.

## 10. Live runtime

A live Creature/NPC uses a distinct instance identity bound to the authorized Session launch snapshot and placement.

Runtime state may include:
- current HP/vitality;
- resources/charges;
- Conditions/Effects;
- initiative;
- current location;
- controller;
- action availability;
- revealed/current form where authorized.

Actions follow the authoritative Session/action pipeline:

inspect → choose/propose → validate → approve if required → authoritative event → update live instance → append timeline/provenance → reproject.

No runtime HP/resource/Condition change writes back into the reusable Definition.

Reconnect restores authoritative instance state; stale cache cannot fabricate Events, participants, forms, permissions, or expired summons.

## 11. Named NPC versus generic creature

The difference is presentation/context, not a hardcoded universal species boundary.

A named NPC may need:
- public identity and aliases;
- motives/goals;
- relationships/reputation;
- faction/organization links;
- statements/contradictions/reliability;
- timeline participation;
- inventory/equipment;
- combat actions.

A generic creature may emphasize:
- encounter role;
- behavior;
- ecology/habitat;
- traits/actions;
- defenses/resources;
- variants/stages.

A sentient creature can legitimately use both. A social NPC can become a combat participant without creating a second identity, while its live combat instance remains distinct from its reusable Definition.

## 12. Ecology, behavior and bestiary discovery

Source materials such as `Havalaea Creatures.PDF` establish Behavior as first-class content alongside combat statistics.

Bestiary/discovery views therefore support:
- habitat/biome;
- environmental adaptation;
- diet;
- activity pattern;
- behavior;
- social structure;
- territory/lifecycle where sourced;
- known sightings/discoveries;
- Campaign-known versus GM/source truth.

Player knowledge can differ from source truth without changing the source Definition. Discovery/reveal history belongs to the Exploration/Discovery workflow.

Previously authorized offline bestiary knowledge may remain readable, but offline state never reveals new hidden source material.

## 13. Relationships, factions and investigation/social use

NPC-capable entities integrate with Relationship, Reputation, Organization/Faction, Investigation, and Timeline systems through stable references.

Player-safe profile may show:
- revealed relationships;
- public/revealed reputation;
- permitted faction ties;
- visible testimony/statements;
- uncertainty/confidence cues.

GM-private layer may additionally contain:
- secret motives;
- hidden relationships/faction ties;
- reliability truth;
- hidden statements;
- reveal conditions.

Uncertainty can be shown without telling a Player whether hidden GM truth exists.

## 14. Equipment, carried assets and loot

Creature/NPC assets use the owning Item/Inventory contracts.

The experience can distinguish:
- visibly equipped item;
- carried but unrevealed inventory;
- container contents;
- currency;
- loot/reward bundle;
- ownership/control;
- source-provided natural weapon versus carried Item;
- Campaign-local reward placement.

Hidden inventory/loot does not contribute Player search/facet/count/provenance data before reveal.

PPIA-03 owns the deeper item/inventory semantics and receives all asset-related routed decisions.

## 15. Variants, templates, types, forms and transformations

PPIA-02 supports five related but distinct patterns:

1. **Sibling/source variant** — separate source-backed Definition/version/variant.
2. **Age/power stage** — ordered or partially ordered source relationship; not universally complete.
3. **Type/affinity modifier** — applies field effects to a base relationship without automatic identity replacement.
4. **Form/transformation** — a governed alternate form relationship that may change presentation/mechanics while preserving source/instance provenance.
5. **Campaign-local template/override** — local composition owned by Campaign authoring, never retroactively source truth.

Comparison is read-only and authorization-filtered before diffing. It identifies added/removed/changed/unknown/conflicted fields textually and never silently chooses a canonical winner.

A runtime transformation must be executed by the owning Ability/Action/Session workflow and changes authorized live-instance/form state—not the underlying Definition.

## 16. Summons, minions and spawned entities

Summon/minion/spawn experience must model:
- summoner/master source reference;
- controller;
- ownership where relevant;
- source Definition;
- placement;
- live instance;
- count/capacity limit;
- duration/resource limit;
- dismissal/destruction/release/control-break lifecycle;
- provenance.

Hidden spawn conditions, reserve counts, secret masters, or control-break conditions remain absent from unauthorized projections.

A stale reconnect cannot resurrect an expired/dismissed summon.

## 17. Playable creature conversion

`Player Creatures.PDF` establishes a source-backed conversion process. PPIA-02 treats conversion as a handoff to Character creation/progression.

Required experience:
- identify source creature and exact base version;
- show retained physical traits;
- identify unique/unlockable abilities;
- show XP/progression source rule where applicable;
- show HP/defense/attribute normalization;
- distinguish excluded monster-runtime state;
- link Ability references rather than copy them;
- create Character/species draft in the owning workflow;
- record retained/normalized/excluded/unlocked conversion provenance.

Source creature, playable species definition, and Character instance remain separate identities.

## 18. Search, filter, comparison and quick actions

Creature/NPC search may support authorized facets such as:
- category/type/tags;
- size;
- threat/CR or governed equivalent;
- habitat/environment;
- movement mode;
- sentience/persona relevance;
- faction/relationship context where authorized;
- variant/stage/form relationship;
- source/pack/version/status;
- Campaign placement state in authoring context.

Hidden objects contribute nothing to result counts or facet values.

Quick actions may include:
- inspect;
- open source/provenance;
- compare;
- open linked Ability/Item/Relationship;
- provisional select;
- quick-add through Scene Picker;
- add to Encounter draft;
- open bestiary/history;
- open NPC profile;
- start playable-conversion handoff where governed.

Every quick action retains its owning workflow and authority boundary.

## 19. Responsive and accessibility contract

Dense creature/NPC presentation must have a usable nonvisual equivalent.

### Required

- semantic headings and ordered reading sequence;
- summary before dense detail;
- keyboard section navigation;
- every linked Ability/Action/Item/Relationship/Variant/source target keyboard reachable;
- screen-reader status for Conditions, availability, validation, conflict, source/recommendation state;
- text/icon/pattern in addition to color for resistance, vulnerability, severity, hidden/revealed, validation and condition status;
- textual field-difference comparison;
- nonvisual relationship/variant traversal;
- touch alternatives for drag/reorder/quick-add;
- high-zoom reflow at 200% text without losing core action/status;
- tables become labeled records when compact/high zoom requires it;
- reduced-motion state changes retain static/text feedback;
- compact GM density does not reduce focus visibility or touch targets below accessibility rules.

### Desktop/expanded

May use persistent section navigation, pinned Rule Inspector, source/variant side-by-side compare, and compact GM layout.

### Medium

Use a primary Inspector with secondary drawers and stacked/column-adaptive comparison.

### Compact/mobile

Use one semantic column, sticky critical status/action region, full-height Rule/Provenance sheets, and no hover dependency.

## 20. Recovery and offline behavior

Recovery is authorization-preserving.

- Deep links/history/cache restore navigation identifiers only, not authority.
- Cached Player-safe bestiary/Inspector data may remain readable where product policy permits, but cache cannot reveal data the user never received.
- Draft authoring restores source/local distinction and revalidates linked references before commit.
- Missing or removed source becomes an explicit validation issue; it is never silently substituted by same name.
- Encounter drafts revalidate stale participants/source versions before analysis/launch.
- Runtime reconnect restores current authoritative instance/control/lifecycle state.
- Summons that expired while disconnected remain expired after reconnect.

## 21. Provenance and conflict behavior

Authorized provenance-capable views can show:
- source title and coordinate;
- source stable ID/version/pack;
- transformation/import summary;
- source versus recommendation/inference status;
- confidence;
- conflicts;
- validation/evidence history;
- Campaign-local override provenance;
- placement and runtime lineage where applicable.

Source-only diagnostics never become hidden-information side channels. A redaction must not reveal that another hidden variant/object exists merely through counts or labels.

## 22. Reference and acceptance cases

The PPIA-02 reference set includes source-grounded cases for:
- ordinary bestiary creature with Behavior;
- mobility/reaction creature;
- source-backed type/affinity modifier;
- Dragon stage chain;
- Dragon sentience spectrum;
- monster-to-playable-species conversion;
- Havalaean sapient-animal conversion.

Synthetic QA cases are explicitly noncanonical and cover:
- named NPC with visible testimony and hidden motive/relationship/inventory;
- hidden Scene placement and later reinforcement;
- summon/minion control/lifecycle;
- swarm/group projection;
- incomplete/conflicted source record;
- live alternate-form transformation and privacy boundary.

These cases are design/acceptance evidence, not new lore.

## 23. Implementation dependency map

PPIA-02 feeds later work without pre-implementing it:

- **STAGE-A-A2** — Universal Library/Inspector/Picker/provenance foundation.
- **PPIA-03** — equipment, inventory, loot, ownership and Taser/source-variant follow-up.
- **PPIA-05** — species, forms, biology, adaptations and playable conversion.
- **PPIA-08** — Campaign/Scene/Session authoring.
- **PPIA-09** — Investigation/mystery NPC evidence/statement use.
- **PPIA-10** — relationship/social/faction framework.
- **PPIA-11** — encounter/balance analysis and inferred numerical review.
- **PPIA-12** — world/ecology/setting authoring.
- **PPIA-15** — regression/edge-case test expansion.

PPIA-02 does not force those tranches to use a new canonical Creature schema. It supplies the experience contracts they must consume.

## 24. Completion boundary

PPIA-02 is complete only when the governed branch contains and validates:

- exact Creature-domain source/design inventory;
- object-layer and presentation taxonomy;
- permission-safe Inspector/projection contract;
- authoring/placement/encounter/runtime/social/bestiary/variant/summon/conversion workflow matrix;
- responsive/accessibility contract;
- source-grounded + synthetic QA reference cases;
- acceptance/traceability matrix;
- completion report/checkpoint with exact-head CI and canonical merge evidence.

Until those gates pass and the PR merges, this document is an implementation-ready **candidate**, not a canonical completion claim.
