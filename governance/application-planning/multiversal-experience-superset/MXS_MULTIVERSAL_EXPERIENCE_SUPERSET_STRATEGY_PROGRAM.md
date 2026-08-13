# Multiversal Experience Superset Strategy Program

**Program ID:** MXS  
**Version:** 0.1.0  
**Status:** OWNER-APPROVED STRATEGY / PREIMPLEMENTATION PROGRAM  
**Owner and final authority:** John Brandon Turner  
**Prepared:** 2026-08-13  

## Purpose

MXS defines what Multiversal must become before later Stage A implementation hardens product assumptions that are too narrow.

The strategic objective is not to clone one VTT, one character builder, one campaign manager, one worldbuilding service, or one rules engine. Existing products establish the minimum user value Multiversal must eventually cover. Multiversal must then exceed that floor through one connected canonical model of rules, content, characters, assets, campaigns, scenes, sessions, relationships, world state, provenance, permissions, history, creation and optional human-governed AI.

The governing product thesis is:

> Any important kind of tabletop role-playing experience available elsewhere should be expressible in Multiversal, while Multiversal should make the characters, worlds, rules, relationships, discoveries and consequences of that play more deeply connected, inspectable, persistent and reusable than a collection of separate tools can provide.

MXS is additive strategy and architecture work. It does not activate STAGE-A-A2, release, deployment, tester access, paid services, production credentials, public publication, autonomous AI authority or a full native VTT.

## Program operating model

MXS uses the owner-approved build-first execution pattern:

1. build the complete bounded research and design tranche;
2. use targeted source checks during construction;
3. synthesize the complete system;
4. run one or a few integrated adversarial review rounds;
5. repair contradictions in batches;
6. update the canonical roadmap and bootstrap once at the end;
7. do not create twelve isolated validation/roadmap loops.

Research must distinguish:
- current competitor capability;
- published TTRPG design patterns;
- empirical psychology/HCI evidence;
- Multiversal source authority;
- explicit design inference/recommendation.

No competitor feature is copied merely because it exists. Every adopted capability must pass three gates:

### Parity Gate
Does Multiversal provide the underlying user value people reasonably expect from strong current tools or play systems?

### Integration Gate
Does the capability use shared Multiversal identity, permission, provenance, recovery, accessibility, content and event contracts instead of becoming an isolated subsystem?

### Multiversal Gate
What additional value becomes possible because the capability is connected to the rest of the platform?

## Cross-program design laws

1. **The table is the product, not engagement metrics.** Optimize for better play, creation, learning, memory and group cohesion; never manufacture app-use compulsion.
2. **Gamify the adventure, mastery, creation and shared history—not software usage.** No daily streaks, arbitrary login XP, coercive FOMO, pay-to-win or attention traps.
3. **Support many kinds of play without forcing one universal play style.** Rules Profiles and Play Experience Profiles select and configure primitives while stable object identity remains intact.
4. **Human authority remains explicit.** AI may explain, retrieve, summarize, draft, compare, simulate proposals and assist; authoritative world changes remain governed.
5. **Progressive complexity is mandatory.** A beginner, expert and GM may see different cognitive depth over the same canonical action without creating separate truth models.
6. **Hybrid play is first-class.** Multiversal must support online, in-person and mixed tables even before a full native VTT exists.
7. **Interoperability precedes replacement.** Where Multiversal cannot yet match a mature spatial/VTT capability, it should provide clean companion/export/integration paths rather than block the broader platform.
8. **Permissions filter before projection.** Hidden information must not leak through search, counts, AI context, summaries, diagnostics, previews, graphs, maps or derived analytics.
9. **Campaign memory is structured.** History, relationships, discoveries, promises, consequences and world changes should be grounded in governed events and provenance rather than reconstructed from prose alone.
10. **Accessibility and cognitive-load budgets are architectural constraints.** They are not end-stage polish.

---

# Work items

## MXS-01 — Industry Capability Baseline

### Purpose
Establish a defensible product-floor inventory from current VTTs, digital companions, campaign/world tools, creator ecosystems, AI-assisted tools and hybrid-play products.

### Questions
- What jobs do current products perform exceptionally well for players, GMs and creators?
- Which capabilities are now table stakes?
- Which capabilities are specialist strengths rather than universal requirements?
- Which must Multiversal bridge before it can provide natively?
- What usability expectations exist for web, mobile, offline, collaboration, import/export, marketplaces, content sharing and extensibility?

### Required coverage
At minimum compare representative products across:
- full VTT / automation;
- lightweight browser VTT;
- cinematic/theater-of-the-mind VTT;
- 3D spatial tabletop;
- digital rules/character companion;
- campaign/world knowledge manager;
- creator/module ecosystem;
- AI-assisted campaign tooling;
- mobile/in-person companion workflows.

### Deliverables
- capability taxonomy;
- competitor-value matrix;
- `must match`, `should match`, `bridge now`, `native later`, `intentionally different` classification;
- parity risk register;
- interaction-cost comparison for common tasks;
- import/export/interoperability requirements.

### Acceptance gates
- no category is represented by only one competitor;
- features are translated into user jobs rather than copied UI;
- every table-stakes capability has a planned Multiversal disposition;
- full-native-VTT dependencies are separated from things Multiversal can provide earlier.

---

## MXS-02 — TTRPG Playstyle Atlas

### Purpose
Map the major families of tabletop play so Multiversal does not accidentally encode only tactical fantasy assumptions.

### Required play families
- tactical combat and positional optimization;
- rules-light and rulings-oriented play;
- fiction-first/narrative play;
- investigation and mystery;
- horror, fear, corruption and psychological pressure;
- heist/caper and flashback-driven play;
- survival, scarcity and expedition play;
- social, relationship and political play;
- faction/organization and domain-level play;
- crafting, downtime and long-term-project play;
- exploration, travel and discovery;
- vehicle/mecha/starship play;
- lifepath/career and generational play;
- character-belief/drive/passion-centered play;
- GMless/shared-authority play;
- solo and co-op oracle-driven play;
- episodic, one-shot, campaign, legacy and persistent-world structures;
- theater-of-the-mind, abstract-zone and spatial/grid modes.

### Method
For each family identify:
- what makes it fun;
- what decisions players make;
- what the GM/facilitator must do;
- what information must be visible or hidden;
- what state persists;
- what creates tension;
- what creates mastery;
- what failure means;
- what pacing structure is used;
- what digital support helps or harms.

### Deliverables
- playstyle taxonomy;
- exemplar mechanic/design-pattern index;
- play-family requirement matrix;
- gap analysis against current Multiversal primitives and Stage A plans.

### Acceptance gates
- no single system is treated as universal authority;
- patterns are abstracted without importing protected setting text or proprietary expression;
- each play family maps to Multiversal-compatible primitives or an explicit gap.

---

## MXS-03 — Universal Play Primitive Model

### Purpose
Define a minimal composable vocabulary capable of expressing the play families from MXS-02 without turning Multiversal into a monolithic rules soup.

### Candidate primitive families to test
- action/check/outcome and degree-of-success models;
- deterministic and random resolution;
- position, effect, difficulty and stakes;
- initiative, turns, phases and triggers;
- reactions/interrupts;
- resources and metacurrencies;
- tags/aspects/traits/descriptors;
- clocks/tracks/countdowns/progress meters;
- stress/fear/corruption/sanity/pressure tracks;
- beliefs/drives/passions/instincts/goals;
- bonds/relationships/reputation;
- clues/leads/hypotheses/truth/reveal;
- projects, crafting, research and downtime activities;
- faction projects and world clocks;
- flashbacks and retroactive preparation;
- consequences, resistance, mitigation and recovery;
- narrative permissions and authority tokens;
- exploration turns, travel legs, hazards and resource attrition;
- discovery/fog/knowledge state;
- tactical position, zones, ranges, templates and line of effect;
- solo/co-op prompts, oracles and uncertainty tables;
- lifepath/career/history generators;
- scene/session/campaign phase changes;
- advancement, transformation and legacy inheritance.

### Architectural target
Create **Play Experience Profiles** layered over Rules Profiles. A Play Experience Profile selects relevant primitives, pacing, UI surfaces, assistance, authority rules and presentation while preserving canonical object identities.

Example: a Campaign can use one Rules Profile while an investigation Scene exposes clue/hypothesis tools, a heist exposes clocks/flashback/stress tools, combat exposes tactical actions/position, and downtime exposes projects/crafting/relationships.

### Deliverables
- primitive registry proposal;
- composition rules;
- Play Experience Profile schema concept;
- primitive compatibility/interaction matrix;
- state/provenance rules;
- migration and fallback requirements;
- anti-combinatorial-explosion constraints.

### Acceptance gates
- every MXS-02 play family can be expressed without changing core object identity;
- primitives can be disabled without corrupting history;
- unsupported combinations fail explicitly;
- UI does not expose irrelevant mechanics merely because the engine supports them.

---

## MXS-04 — Player Motivation, Psychology and Experience Architecture

### Purpose
Turn evidence about autonomy, competence, relatedness, flow, curiosity, identity, agency and meaning into explicit product principles.

### Research dimensions
- self-determination theory: autonomy, competence, relatedness;
- flow: challenge/skill balance, clear goals, feedback and sense of control;
- curiosity and information gaps;
- identity experimentation and character attachment;
- perceived agency and meaningful choice;
- mastery and learning;
- belonging and group memory;
- uncertainty, tension, suspense and relief;
- failure as information/story rather than punishment;
- psychological safety and voluntary boundaries;
- risks of extrinsic reward substitution and coercive gamification.

### Deliverables
- Human Experience Design Standard;
- motivation-support matrix by workflow;
- anti-dark-pattern standard;
- meaningful-feedback taxonomy;
- campaign-memory and personal-arc requirements;
- research-confidence labels distinguishing well-supported principles from hypotheses.

### Acceptance gates
- every major UI/workflow can state which human need it supports and how it avoids undermining another;
- no retention mechanic is justified solely by time-in-app or frequency-of-return;
- competitive/social mechanics include opt-out and non-humiliating alternatives where appropriate.

---

## MXS-05 — GM Psychology, Facilitation and Cognitive-Load Architecture

### Purpose
Make Multiversal reduce the hardest parts of GMing without taking creative control away from the GM.

### Model the GM job in three loops
1. **Prepare:** recover context, select material, create/adapt content, anticipate possibilities.
2. **Facilitate live play:** track state, listen, improvise, adjudicate, distribute spotlight, protect secrets, pace scenes and answer questions.
3. **Recover/continue:** record what changed, identify unresolved threads, update the world, prepare next session.

### Research/design questions
- Which tasks cause context switching and working-memory overload?
- Which information is needed now versus merely available?
- Which decisions can be precomputed without pre-deciding the story?
- How can suggestions remain reversible and provenance-visible?
- How can the system surface forgotten NPCs, promises, clocks, clues and consequences at the right moment?
- How should GM uncertainty be represented rather than hidden?

### Deliverables
- GM cognitive-load budget;
- GM decision-support taxonomy;
- context-aware GM cockpit model;
- prep/live/aftermath information architecture;
- interruption/recovery patterns;
- bounded AI-assistance rules;
- improvisation support and consequence-preview concepts.

### Acceptance gates
- no live-play surface requires broad repository-like browsing for ordinary decisions;
- important hidden state is available to the GM without leaking to players;
- assistance shortens lookup/prep while preserving GM authorship.

---

## MXS-06 — Social Table Dynamics, Consent and Shared Authority

### Purpose
Treat the human group as a first-class system because group dynamics can matter more to tabletop experience than mechanical sophistication.

### Scope
- session-zero alignment;
- desired playstyle/tone/intensity;
- content boundaries and safety controls;
- spotlight preferences and participation styles;
- player/GM communication channels;
- shared creative authority;
- conflict/retcon/pause workflows;
- guest/observer/co-GM/assistant-GM roles;
- campaign commitments and schedule expectations;
- private player notes/secrets;
- table norms that are explicit but not policed by surveillance.

### Deliverables
- **Playstyle Compass** design;
- Table Contract / Session Zero profile;
- consent/boundary data model with privacy rules;
- spotlight-support concepts based on preferences rather than raw speaking-time scoring;
- shared-authority profiles for traditional GM, co-GM, rotating facilitator, GMless and solo/co-op modes;
- no-blame pause/rewind/skip interaction patterns.

### Acceptance gates
- sensitive preferences can remain private where appropriate;
- the platform never infers diagnoses/personality labels;
- no automatic behavior scoring becomes disciplinary authority;
- shared-authority modes cannot accidentally reveal GM-only truth.

---

## MXS-07 — Learning, Onboarding and Progressive Complexity

### Purpose
Allow a first-time player to participate quickly while preserving expert-level transparency and control.

### Design target
The same canonical operation may have multiple cognitive-depth presentations:
- **Guided:** intent-focused, minimal jargon;
- **Standard:** key choices, costs, probability/likely consequences where valid;
- **Advanced:** complete modifiers, dependencies and tactical options;
- **Diagnostic/GM:** full resolution chain, provenance, hidden rules and governance controls.

### Scope
- learn while building a Character;
- just-in-time rules explanations;
- contextual examples;
- guided first session;
- progressive disclosure;
- optional automation with explainability;
- recoverable mistakes/undo where authority permits;
- accessibility and neurodiversity considerations;
- expert speed paths and keyboard workflows;
- rule-learning history that never becomes a punitive score.

### Deliverables
- progressive-complexity contract;
- teaching moment taxonomy;
- contextual help architecture;
- beginner-to-expert transition model;
- expert bypass/speed requirements;
- onboarding acceptance journeys.

### Acceptance gates
- novice mode cannot hide consequential irreversible choices;
- expert mode cannot bypass permissions or validation;
- users may change assistance depth at any time.

---

## MXS-08 — Meaningful Gamification, Campaign Memory and World Pulse

### Purpose
Create compelling progress feedback from actual play rather than extrinsic app-engagement mechanics.

### Core concept: World Pulse
A permission-filtered projection of what changed and why, grounded in authoritative events and provenance.

Potential views:
- session changes;
- Character arc progress;
- relationships/reputation movement;
- faction and organization projects;
- unresolved clues/mysteries;
- promises/debts/obligations;
- discoveries and travel history;
- crafting/research/base projects;
- settlement/economy/world consequences;
- newly relevant NPCs/locations;
- cause/effect chains;
- player-visible versus GM-complete versions.

### Other meaningful progress concepts
- personal goals/arcs;
- mastery and discovered options;
- campaign milestones;
- world transformation;
- collection/provenance history where intrinsically relevant;
- creator completeness/validation rather than arbitrary XP.

### Deliverables
- World Pulse contract;
- causal-history graph concept;
- meaningful-progress taxonomy;
- anti-gamification-abuse rules;
- session recap/re-entry architecture;
- long-absence recovery design.

### Acceptance gates
- every displayed causal claim traces to governed evidence or is labeled inference;
- hidden causes remain hidden;
- no app-use streaks, FOMO pressure or pay-to-progress mechanics.

---

## MXS-09 — Creator, Publisher and Rules Ecosystem

### Purpose
Make Multiversal a platform others can build tabletop experiences on without recreating the infrastructure beneath them.

### Scope
- declarative Rules Profiles;
- Play Experience Profiles;
- content packs and dependencies;
- no-code/low-code object and rule authoring;
- validation and compatibility testing;
- creator namespaces and stable IDs;
- provenance/licensing/attribution;
- versioning/migration/deprecation;
- private, campaign-local, community and publisher content tiers;
- review/promotion workflows;
- entitlement/content-sharing rules;
- safe extensibility versus executable plug-ins;
- marketplace readiness without making marketplace launch an early dependency.

### Deliverables
- creator capability ladder;
- rules/content SDK conceptual contract;
- publisher ingestion path;
- compatibility certification levels;
- creator test harness requirements;
- migration/rollback expectations;
- ecosystem governance principles.

### Acceptance gates
- a creator can express a distinct game experience without forking core Multiversal;
- creator content cannot silently widen permissions or execute arbitrary code;
- installed content remains portable, attributable and recoverable.

---

## MXS-10 — VTT Bridge, Hybrid Table and Spatial Strategy

### Purpose
Provide excellent play before Multiversal can match mature full VTTs, while preserving a path to native spatial play.

### Near-term strategy
Multiversal acts as the authoritative campaign/rules/state companion while external or lightweight spatial tools can handle maps where necessary.

### Required bridge capabilities
- token/portrait export;
- encounter/scene participant manifests;
- initiative/state handoff where feasible;
- map/coordinate/location references;
- printable/in-person views;
- second-screen/table-display mode;
- mobile character/GM companion;
- shareable read-only projections;
- structured import/export rather than screenshots where possible.

### Native spatial maturity ladder
1. abstract/no-map scenes;
2. zones/range bands;
3. static map + tokens + manual fog;
4. grid/measurement/templates;
5. walls/vision/dynamic fog/lighting;
6. deeper tactical automation;
7. optional 3D/advanced spatial adapters where justified.

### Deliverables
- bridge/export contract;
- hybrid-table UX;
- spatial maturity roadmap;
- external-VTT interoperability boundary;
- native-map object model requirements.

### Acceptance gates
- lack of a full VTT never prevents Character, campaign, rules, investigation, social, creator or world features from delivering value;
- bridge formats do not become canonical truth.

---

## MXS-11 — Multiversal Unique Experience Layer

### Purpose
Define experiences competitors cannot easily replicate without Multiversal's interconnected object/event/provenance architecture.

### Candidate signature capabilities
- **World Pulse** — grounded world-change summary and causal explanation;
- **Causal Campaign Graph** — inspect how actions propagated through relationships, factions, economy, clues, settlements and other domains;
- **Play Experience Profiles** — change the active style of play without changing canonical world identity;
- **Progressive Complexity** — beginner through diagnostic views over the same action/state;
- **Living World Projects** — factions, settlements, organizations and other actors progress through governed world clocks/projects;
- **Campaign Memory / Why Engine** — answer when/why/how current state came to be;
- **Contextual GM Cockpit** — right information at the point of decision rather than static dashboards;
- **Cross-Domain Consequence Preview** — bounded preview of possible affected systems before authoritative commit;
- **Governed AI over structured truth** — AI works from permission-filtered canonical projections and cites provenance instead of inventing campaign reality;
- **Universal Creator Layer** — author once into shared structures that can participate in search, scenes, combat, economy, social systems, exports and AI safely.

### Deliverables
- signature-experience portfolio;
- defensibility analysis;
- required underlying capabilities;
- staged MVP/alpha/later maturity for each concept;
- failure modes that would reduce a signature feature to superficial marketing.

### Acceptance gates
- every claimed differentiator has a concrete implementation dependency chain;
- novelty claims are phrased as product strategy, not unverifiable universal market claims;
- at least several signature experiences can begin before a full VTT exists.

---

## MXS-12 — Product Superset Roadmap and Stage A Reconciliation

### Purpose
Convert MXS-01 through MXS-11 into actionable development architecture and reconcile it against work already completed.

### Required reconciliation targets
- Phase 8/9 foundations;
- A1 application shell;
- Developer Toolbelt DT-001–010;
- IA-D01–D09;
- PPIA-01–16;
- CAPP-01–12;
- recovered Stage A A2–A12 preparation;
- Feature Bible domains;
- current UI/Screen Design Bibles;
- DS-008 and WP-011 retained constraints.

### Classification for every MXS requirement
- already satisfied;
- partially satisfied;
- prepared but stale and must be reconciled;
- belongs inside an existing Stage A item;
- creates a new cross-cutting foundation;
- deferred until native spatial/VTT maturity;
- intentionally out of scope.

### Deliverables
- Stage A impact map;
- revised dependency order only where evidence demands it;
- parity/integration/Multiversal gates attached to affected Stage A items;
- pre-A2 foundation requirements if any;
- post-A12 expansion roadmap;
- research/validation backlog for unresolved hypotheses;
- canonical strategy summary for bootstrap recovery.

### Acceptance gates
- no previously completed program is reopened merely because MXS exists;
- no recovered A2–A12 preparation is discarded without explicit supersession rationale;
- A2 remains the application implementation item unless the owner explicitly changes it;
- roadmap changes reflect strategy without pretending unbuilt features already exist.

---

# Program completion gate

MXS planning is complete only when:

1. MXS-01 through MXS-12 have source-backed substantive outputs;
2. industry baseline, playstyle atlas, psychology, GM/social design, play primitives, creator ecosystem, spatial strategy and unique experience layer have been synthesized together;
3. contradictions and combinatorial-risk areas have been adversarially reviewed;
4. existing Multiversal programs are mapped rather than duplicated;
5. the canonical roadmap is updated once with the resulting product strategy and dependency impact;
6. the bootstrap is updated once so future conversations recover MXS as strategy authority without displacing repository evidence or active implementation state;
7. no release/runtime/tester/paid-service/publication authority is inferred from strategy completion.

## Intended result

When MXS is finished, Multiversal should have a defensible answer to four questions for every major feature or play capability:

1. What user value does the best existing tabletop ecosystem already provide?
2. Which kinds of tabletop play must this support?
3. How does Multiversal provide that value through one shared architecture?
4. What becomes possible because the capability is connected to everything else?
