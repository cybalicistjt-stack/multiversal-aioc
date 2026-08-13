# MXS-02 / MXS-03 — TTRPG Playstyle and Universal Play Primitive Atlas

**Version:** 0.1.0  
**Status:** STRATEGY DESIGN / PREIMPLEMENTATION  
**Prepared:** 2026-08-13

## Purpose

This atlas prevents Multiversal from encoding one preferred RPG tradition as the universal definition of tabletop play. It identifies recurring families of play and the generic primitives Multiversal must be able to compose through Rules Profiles and Play Experience Profiles.

This document abstracts design patterns. It does not import proprietary setting expression or claim that one published game is the only way to produce a given experience.

## Core architecture

Multiversal should separate three concepts:

1. **Canonical world/object truth** — Characters, Assets, Locations, Factions, relationships, Campaign state, provenance and history.
2. **Rules Profile** — which mechanics govern a game and how resolution works.
3. **Play Experience Profile** — which subset of relevant mechanics, pacing structures, authority patterns and UI surfaces are active for the current mode/Scene/session.

A Play Experience Profile may change without changing the identity of the objects being played.

Example: the same Campaign can move from social free play to a clue-driven investigation, then to tactical combat, then to downtime projects. The UI and active primitives change; the Character, Location, NPC, Faction and event history do not become unrelated copies.

---

# Playstyle families

## 1. Tactical / positional problem solving

### Player value
Mastery, build expression, meaningful action economy, teamwork, positioning and transparent consequences.

### Representative patterns
- bounded action economy;
- initiative/turn order;
- movement/range/area;
- reactions/triggers;
- typed effects/conditions;
- resource management;
- degrees of success;
- tactical information and encounter state.

### Multiversal requirements
Actions, costs, triggers, Effects, Conditions, position, zones/ranges, initiative/time, target rules, reaction windows, deterministic calculation, inspectable modifiers, fast result history.

## 2. Fiction-first / narrative play

### Player value
Fictional intent drives mechanics; dramatic consequences matter more than exhaustive simulation.

### Representative patterns
- moves/actions triggered by fictional circumstances;
- partial success / success-at-cost;
- scene/situation tags;
- player-authored details within bounded authority;
- mechanics that deliberately redirect fiction.

### Multiversal requirements
fictional triggers, intent/action mapping, outcome bands, complications, narrative permissions, tags/aspects, consequence proposals, flexible scene facts with provenance.

## 3. Character-identity / dramatic play

### Player value
Who the Character is matters mechanically, not just what numeric skills they possess.

### Representative patterns
- beliefs, drives, passions, instincts;
- relationships and obligations;
- descriptive aspects/tags;
- complications generated from identity;
- goals/arcs and personal transformation.

### Multiversal requirements
Drive/Belief/Passion objects, Character arcs, relationship state, identity tags, voluntary complications, goal tracking, value conflicts, history-driven changes.

## 4. Investigation / mystery play

### Player value
Discover, connect, interpret and act on information without a single failed perception check collapsing the scenario.

### Representative patterns
- core clues versus optional depth;
- leads connecting scenes;
- known/unknown/hidden truth;
- hypotheses;
- timelines/evidence;
- information permissions;
- deduction rather than information starvation.

### Multiversal requirements
Clue/Evidence objects, truth/reveal state, confidence, provenance, leads, hypothesis board, graph/list/timeline views, GM source-of-truth model, player-safe projection, no-leak counts and AI summaries.

## 5. Heist / caper / high-agency action

### Player value
Fast momentum, competence, flexible preparation, escalating risk and clever reversals.

### Representative patterns
- operation phases;
- flashbacks;
- stress/pressure;
- clocks;
- position/effect;
- resistance/mitigation;
- heat/attention;
- downtime fallout.

### Multiversal requirements
phase profiles, retroactive preparation with constraints, progress/danger clocks, pressure resources, consequence resistance, attention/heat tracks, project/faction follow-up.

## 6. Horror / psychological pressure

### Player value
Vulnerability, uncertainty, dangerous knowledge, escalating cost and atmosphere.

### Representative patterns
- fear/stress/corruption/sanity-like tracks;
- knowledge at a price;
- hidden or uncertain reality;
- long-term scars/changes;
- player safety boundaries distinct from Character distress.

### Multiversal requirements
PressureTrack primitive, exposure events, irreversible/recoverable transformation profiles, uncertainty/reality-check patterns, safety profile separation, tone-aware presentation.

## 7. Survival / scarcity / expedition

### Player value
Preparation, risk management, exploration, resource tradeoffs and meaningful environmental pressure.

### Representative patterns
- travel legs/turns;
- food/water/fuel/ammunition/load;
- encumbrance/capacity;
- hazard/weather/exposure;
- shelter/rest;
- route choices;
- discoveries;
- attrition and recovery.

### Multiversal requirements
travel, environment, inventory, capacity, consumption, hazards, route graph, discoveries, time progression, vehicle/base integration.

## 8. Social / relationship / political play

### Player value
People remember; alliances, trust, reputation, factions and obligations matter.

### Representative patterns
- relationship dimensions;
- reputation domains;
- organizations/factions;
- influence;
- promises/debts;
- social consequences;
- political projects.

### Multiversal requirements
existing social Feature Bible architecture plus scene-level negotiation, social stakes, permission-aware motives/secrets, relationship history and faction/world consequence links.

## 9. Domain / faction / settlement play

### Player value
The party acts on organizations, settlements, kingdoms, territory and institutions rather than only individual encounters.

### Representative patterns
- faction turns/projects;
- holdings/resources;
- diplomacy;
- laws/policies;
- settlement metrics;
- territory and world events.

### Multiversal requirements
organization/faction/settlement/kingdom objects, projects/clocks, resource ledgers, governed event propagation, macro dashboards and drill-down to individual causes.

## 10. Crafting / research / project play

### Player value
Long-term creation, experimentation, investment, planning and visible progress.

### Representative patterns
- recipes/processes;
- materials/resources;
- workstations/facilities;
- progress tracks;
- quality;
- failure/recovery;
- automation queues.

### Multiversal requirements
existing crafting/base/economy architecture plus generic Project and Progress primitives reusable by research, rituals, training, construction and faction goals.

## 11. Vehicle / mecha / starship play

### Player value
Shared complex assets, crew roles, mobility, subsystem tradeoffs, cargo and tactical/strategic identity.

### Representative patterns
- crew stations/roles;
- power/fuel;
- systems/damage;
- cargo;
- upgrades;
- movement/navigation;
- combat support;
- mobile-base functions.

### Multiversal requirements
PPIA-04/Feature Bible vehicle contracts, role/action authority, nested Assets, spatial abstraction levels and transition between Character-scale and vehicle-scale play.

## 12. Exploration / discovery / fog-of-knowledge

### Player value
Unknown spaces become known through action; the world feels larger than what is currently visible.

### Representative patterns
- hidden/rumored/discovered/surveyed states;
- navigation;
- landmarks;
- route choices;
- encounter generation;
- map/fog state;
- player-specific knowledge.

### Multiversal requirements
Discovery/KnowledgeState primitive, map/location graph, player/campaign projections, reveal events and robust separation of truth from knowledge.

## 13. Lifepath / career / generational play

### Player value
Character history and world connections emerge through structured life events; legacy matters.

### Representative patterns
- careers/terms/ages;
- life events;
- family/lineage;
- acquired relationships/resources/scars;
- retirement/inheritance;
- generational consequences.

### Multiversal requirements
LifeEvent timeline, career/phase profiles, lineage links, inherited Assets/relationships/obligations, historical provenance and migration-safe aging.

## 14. Solo / co-op / GMless play

### Player value
Play without a permanent GM; uncertainty is externalized through prompts/oracles/shared authority.

### Representative patterns
- oracles/random tables;
- prompts;
- progress tracks;
- explicit narrative authority;
- shared interpretation;
- scene framing;
- uncertainty questions.

### Multiversal requirements
Oracle primitive, AuthorityProfile, prompt tables, scene/question logs, truth-creation rules, optional facilitator rotation and strong distinction between generated suggestion and accepted canon.

## 15. Rules-light / rulings-oriented play

### Player value
Speed, flexibility and imaginative problem solving with minimal mechanical overhead.

### Representative patterns
- small resolution core;
- tags/fictional positioning;
- GM/table rulings;
- fewer explicit exception rules;
- rapid Character creation.

### Multiversal requirements
Rules Profiles may intentionally omit detail. Generic fallback must not force unused schemas or expose irrelevant controls. Rulings can be recorded as local Campaign rules with provenance.

## 16. Theater-of-the-mind / cinematic play

### Player value
Atmosphere, imagination and pace without spatial micromanagement.

### Representative patterns
- evocative Scene state;
- image/audio/ambience;
- abstract ranges/zones;
- spotlighted Characters/NPCs;
- scene notes and narrative prompts.

### Multiversal requirements
Scene Presentation Profile, zone/range abstraction, media/ambience, GM notes, current-cast panel, fast actions and no dependency on tactical-map readiness.

---

# Universal play primitive registry proposal

The following primitives should be evaluated as reusable engine-level concepts rather than recreated per feature.

| Primitive family | Purpose |
|---|---|
| `Action` | declared attempt/intention with actor, targets, costs, requirements and authority |
| `OutcomeModel` | binary, degree, partial-success, opposed, deterministic or custom result interpretation |
| `Effect` | governed state consequence |
| `Condition` | persistent/temporary modifier or state |
| `Resource` | spendable/recoverable quantity or capacity |
| `MetaCurrency` | player/table-facing influence resource distinct from in-fiction possessions |
| `TagAspect` | meaningful descriptive fact usable by rules or presentation |
| `Trigger` | condition that enables reaction/move/effect |
| `ClockTrack` | generic bounded progress, danger, countdown, race or project state |
| `PressureTrack` | stress/fear/corruption/sanity/heat-like escalating cost model |
| `DriveBeliefPassion` | identity-linked motivation/obligation value |
| `Relationship` | directed entity-to-entity social state |
| `Reputation` | domain-level collective perception |
| `ClueEvidence` | discoverable information with truth/provenance/visibility |
| `Hypothesis` | player/GM proposition linked to evidence but not automatically truth |
| `KnowledgeState` | who knows what and at what certainty/reveal level |
| `Project` | long-running goal with inputs, progress and outcome |
| `Phase` | current toolbox/pacing state such as encounter, downtime, score or travel |
| `Flashback` | bounded retroactive preparation that cannot rewrite established truth |
| `Consequence` | negative/complicating result before or after mitigation |
| `ResistanceMitigation` | governed reduction/avoidance of consequence with cost |
| `AuthorityProfile` | who may frame, propose, decide, reveal, create truth or control actors |
| `Oracle` | governed uncertainty/prompt source for solo/co-op/GM support |
| `LifeEvent` | historical transition with persistent Character/world consequences |
| `Discovery` | transition from unknown/hidden to authorized knowledge |
| `SpatialRelation` | point/grid/zone/range/relative-position abstraction |
| `TurnWindow` | initiative/round/turn/reaction opportunity |
| `Procedure` | ordered multi-step rules process such as travel, crafting or downtime |

## Primitive design rules

1. A primitive is reusable only if at least two play families need the same semantic behavior.
2. Primitive configuration belongs in Rules/Play Experience Profiles, not global hard-coded defaults.
3. Unknown or unsupported semantics remain explicit; the platform does not silently approximate with a familiar D20-style equivalent.
4. Every authoritative primitive mutation emits provenance/history suitable for replay or explanation.
5. Visibility applies before derived state. A hidden clock, clue or relationship cannot leak through counts, AI summaries, progress totals or graph structure.
6. Primitive state should be portable even when a renderer/UI is not available.
7. Profiles may hide irrelevant primitives completely.
8. A Campaign may combine compatible profiles, but combinations require declared conflict resolution.

# Play Experience Profile concept

A Play Experience Profile should define at minimum:
- profile ID/version;
- applicable Rules Profiles;
- active primitive families;
- required/optional object capabilities;
- resolution/pacing structure;
- active UI surfaces;
- GM/player authority pattern;
- information/visibility model;
- recommended cognitive depth defaults;
- accessibility presentation requirements;
- offline behavior;
- bridge/spatial requirements;
- incompatibilities;
- fallback behavior;
- provenance of the profile definition.

Potential built-in profile families are not game systems; they are experience configurations such as:
- `free-play`;
- `tactical-encounter`;
- `cinematic-encounter`;
- `investigation`;
- `social-political`;
- `heist-operation`;
- `survival-expedition`;
- `downtime-projects`;
- `world-domain-turn`;
- `vehicle-operation`;
- `solo-oracle`;
- `collaborative-worldbuilding`.

# Anti-combinatorial-explosion strategy

Multiversal must not attempt to validate every possible primitive combination.

Use:
- capability declarations;
- profile-defined allowed combinations;
- explicit incompatibility rules;
- shared foundational invariants;
- profile-specific conformance suites;
- Generic fallback for unknown content presentation, not unknown mechanics execution;
- bounded extension points;
- declared nonapplicability evidence.

# Stage A implications

- **A2 Universal Object Experience:** object inspectors/search must expose capabilities generically and remain profile-aware.
- **A3 Identity/Workspaces:** selected context should include active Rules/Play Experience Profile references and authority profile.
- **A4 Character:** Character UI must support variable resource/drive/condition/action primitives without rigid D20 assumptions.
- **A5 Campaign/Scene:** Scene should select/override play profiles and presentation modes.
- **A6 First Playable Loop:** Action proposal/result must be generic enough for outcome models beyond binary pass/fail.
- **A7 Combat:** tactical combat becomes one play profile, not the universal session model.
- **A8 Inventory/Crafting/Vehicles:** Project/Resource/Procedure/vehicle primitives must interoperate.
- **A9 Investigation/Social:** Clue/Hypothesis/KnowledgeState/Relationship primitives are first-class.
- **A10 World/Creator:** creators must be able to define compatible profiles/primitives declaratively.
- **A11 AI:** AI must be aware of active profile/authority and never invent unsupported mechanics.
- **A12 Hardening:** conformance testing must include multiple play profiles and all-optionals-off behavior.

# Research basis

The atlas was informed by current/public rules documentation and SRDs representing different design approaches, including Pathfinder 2e modes/action economy, Fate aspects/compels, Powered by the Apocalypse fiction-triggered moves and play-to-find-out models, Blades in the Dark phase structure/clocks/flashbacks/resistance, GUMSHOE core-clue investigation, Call of Cthulhu horror pressure, and Pendragon Traits/Passions. These are exemplars for pattern discovery, not source authority for Multiversal mechanics.
