# GCL-03 — Situation & Scene Template Library: Library and Authority Report

**Work item:** GCL-03  
**Attempt:** GCL-03-attempt-001  
**State:** candidate for exact-head governed validation

## What this tranche adds

GCL-03 adds 100 production reusable situation/scene templates across ten scene families, ten records per family:

- social negotiation;
- investigation/discovery;
- exploration/navigation;
- travel/transition;
- survival/environment;
- stealth/infiltration;
- technical/problem-solving;
- downtime/community;
- confrontation/standoff;
- mixed-pressure/choice.

Each template is parameterized and carries an opening state, replaceable governed-reference slots, at least two open questions, pressure prompts, turning-point prompts, at least two possible exit vectors, discovery metadata and downstream composition targets. The template corpus is intentionally genre-neutral at the structural level so GCL-15 can later own richer genre/tone transformation rather than forcing duplicated scene prose now.

## Why these are templates, not live Scenes

MV-IA-F005 establishes Scene templates as reusable Definitions and separately owns real Scene aggregates, Campaign-local placements and overrides, participants, objectives, visibility, launch configuration and immutable Session snapshots. PPIA-08 further separates reusable source references from Campaign-local placement, map/grid state, hidden/reveal state, launch packaging, live amendments and post-session history.

GCL-03 therefore owns only reusable construction material. It does not create:

- a Campaign or Scene aggregate;
- a Campaign-local placement or override;
- a real objective, participant, actor, Location, clue, Hazard, Item, Vehicle, Encounter or other governed object binding;
- map image/grid calibration, cell/zone placement or dungeon geometry;
- hidden/reveal or knowledge-state truth;
- launch readiness, launch snapshot or Session state;
- a durable Event or post-session history;
- a canonical outcome, mandatory player choice or guaranteed resolution.

When a GM later chooses a template, an authorized F005/PPIA-08 consumer may bind stable governed references and create Campaign-local state through its own permission, entitlement, versioning, recovery and launch rules.

## Nonlinear scene grammar

GCL-03 intentionally avoids a golden-path scene model. A scene template supplies:

- a situation worth engaging;
- an opening state;
- questions the GM can answer or leave open;
- pressure that can move the situation;
- possible turning points;
- multiple exit vectors.

Exit vectors are possible continuations, not predictions. They may lead to another scene, an objective, a complication, a mystery lead, a later adventure structure, a relationship change, or—where force actually begins—an owning GCL-04/F012 Encounter path. The template never asserts that any exit occurred.

## Encounter boundary

The confrontation/standoff family is intentionally combat-adjacent rather than Encounter-authoritative. It covers situations such as a tense standoff, blocked passage, crowd on the edge, hostile demand or intervention between others while meaningful nonviolent continuations still exist. If actual tactical conflict begins, the structure hands off to GCL-04 and MV-IA-F012/PPIA-11 rather than defining combat composition, threat or balance itself.

## Storage and materialization

The corpus uses five columnar JSON shards. Every shard declares the same compact field columns and every row supplies every field explicitly. `GCL-03_SITUATION_SCENE_MATERIALIZATION_PROFILE_v0.1.0.json` maps those compact records deterministically into the completed GCL-01 shared template grammar.

There are no hidden defaults. Materialization preserves:

- runtime authority = none;
- owning-domain acceptance required;
- unresolved Campaign/world bindings;
- provenance and authority labels;
- ready-to-use and construction-material projections;
- deterministic/manual composition without AI;
- optional AI only as proposal material from authorized context.

## Downstream use

GCL-03 is designed to compose with:

- GCL-02 hooks/premises;
- GCL-04 Encounter archetypes;
- GCL-05 objectives/stakes/outcomes;
- GCL-06 complications/escalations;
- GCL-09 mystery/clue kits;
- GCL-10 adventure structures;
- GCL-13 NPC dramatic roles;
- CSW-05 storycraft planning;
- MV-IA-F005/PPIA-08 Campaign/Scene authoring.

Those consumers remain authoritative for their own domains. Composition never promotes GCL-03 material automatically.

## Validation gate

The current AIOC repository-health validator now verifies GCL-03 by checking:

- exactly 100 production records;
- exactly ten scene families with ten records each;
- unique stable IDs and family-prefix agreement;
- required compact fields;
- controlled slot vocabulary and declared placeholders;
- at least two open questions and at least two exit vectors per record;
- pressure and turning-point coverage;
- structural genre-neutrality;
- scene-only production scope;
- deterministic materialization and no hidden defaults;
- runtime/canon nonauthority;
- no Campaign-local placement authority;
- no hidden/reveal authority;
- no launch/Session authority;
- no resolved-outcome fields;
- broad play-emphasis and construction-need coverage.

Completion remains contingent on successful exact-head repository-health validation and recorded merge evidence.
