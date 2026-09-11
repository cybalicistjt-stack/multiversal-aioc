# MNCS — Multiversal NPC & Creature Studio

**Program ID:** MNCS  
**Program name:** Multiversal NPC & Creature Studio  
**Version:** 0.1.0  
**Status:** OWNER-APPROVED — PLANNED INTERSTITIAL; NOT STARTED  
**Activation:** after MCCS-21  
**Successor:** MAS-01  
**Owner and final authority:** John Brandon Turner  
**Approved:** 2026-09-11  
**Implementation authority:** none

## Purpose

MNCS turns Multiversal's existing Character/NPC/Creature, Species/Form, Profession/Life, Relationship/Reputation, World/Environment, Encounter, inventory, progression and presentation foundations into one coherent **TTRPG NPC and creature generation/construction studio**.

This program is specifically about fictional TTRPG NPCs and creatures. It is **not** a digital-human reproduction, avatar-scanning, photoreal-person reconstruction or real-person simulation program.

The product target is broader than a random NPC generator or stat-block editor. A GM or creator must be able to create anything from a five-second improvised passerby or roadside animal to a recurring NPC, major antagonist, intelligent nonhuman, creature family, household, crew, herd, settlement population or ecosystem cohort, then deepen that same identity only when play makes it important.

## Placement

MNCS is a future interstitial program:

`SMB-07 → CNI-01..13 → PCA-01..16 → MCS-01..21 → MCCS-01..21 → MNCS-01..24 → MAS-01..21 → MSAS-01..21 → MRCS-01..21 → MBES-01..24 → SMB-08 → SMB-09`

Rationale:

1. MCCS supplies optional appearance/presentation outputs for generated NPCs and creatures without becoming identity authority.
2. MNCS then constructs governed NPC/creature identities, groups and populations from existing owner-domain definitions.
3. MAS can consume actual constructed casts, agendas, relationships and creature populations rather than inventing a parallel Adventure-only NPC generator.
4. Later MRCS can author additional reusable NPC/creature roles, behaviors, species, templates and generation definitions without being a prerequisite for MNCS.
5. MNCS does not change the current ARI family, current work pointer or implementation authority.

## Core design doctrine

### One identity, progressive generation resolution

NPCs and creatures must be able to gain or shed detail without being replaced by new identities.

NPC/person resolution:

`population member → passing extra → minor NPC → recurring NPC → full NPC → major Character-grade NPC`

Creature resolution:

`population → group/herd/pack/swarm → encounter member → persistent individual → named/sapient/major entity`

Moving between levels changes authored/simulated detail, not identity. A bartender improvised in five seconds can become a recurring ally without copying the bartender into a second Character record. A wolf from a summarized pack can become a persistent named animal without losing provenance to the pack/population it came from.

### Fast first, deep when useful

The studio must support two equally valid entry patterns:

- **instant improv:** one action produces the minimum playable result for the current context;
- **deep construction:** a guided studio exposes identity, persona, relationships, knowledge, mechanics, ecology, behavior, life context, secrets and presentation handoffs.

Every generated field can expose its source/recipe and, where applicable, be locked before selective regeneration. Regenerating one field family must not silently overwrite locked or accepted fields.

### Context before randomness

Generation must consume authorized Campaign/World/Location/Environment/Species/Culture/Faction/Profession/Encounter context before selecting candidates. A native NPC, local profession, language, name, creature or ecological adaptation should come from eligible context rather than from an undifferentiated global table.

Unknown or unsupported context remains unknown/unresolved. Generation may propose candidates but cannot invent source truth simply to fill every field.

### Deterministic procedural core; optional AI enrichment

Blocking generation, rerolling, selection, mechanical composition and validation must work without a paid/cloud AI provider. Seeded/table/weighted/constraint-based generation exposes deterministic receipts where determinism is claimed.

Optional AI may help with prose, surprising combinations, dialogue cues, secrets or expansion, but it receives visibility-safe context and returns candidate material only. It cannot silently canonize, publish or mutate live state.

### Definition, generated candidate, placement and live instance remain distinct

MNCS consumes PPIA-02's distinction among reusable Definition, presentation profile, variant/template relationship, Campaign/Scene placement, live instance, playable conversion and provenance. A generated NPC/creature candidate is not a live participant until accepted and handed to the owning system.

## Campaign-scoped party-association reputation requirement

MIB-09 remains authoritative for deterministic relationship/reputation mutation. MNCS exposes and composes that authority for generated/constructed NPCs and factions.

In a Campaign, another player Character's actions **may affect how a specific group/faction regards your Character because you are associated through the party** when the owning reputation definition says that association matters.

This is not one universal shared-party score. The engine must preserve separately inspectable components such as:

- direct reputation earned by the Character;
- association-derived influence from party membership or joint activity;
- faction/group-specific weighting and exceptions;
- source Event/actor/party/campaign attribution;
- trend/history/provenance receipts;
- visibility/reveal state.

Required behavior:

1. association spillover is Campaign-scoped and cannot leak across Campaigns or become account-global reputation;
2. individual reputation remains distinct even when a faction applies collective responsibility, fame, suspicion, gratitude or guilt-by-association;
3. factions may weight positive/negative party association differently, ignore it entirely, or apply it only under authored conditions;
4. not every party member must receive the same change;
5. joining/leaving a party changes future association context but does not automatically erase past reputation consequences unless the owning rule says so;
6. every propagated reputation effect must remain attributable to the initiating Event/actor and replayable where MIB-09 supports replay;
7. hidden identities, secret faction knowledge and unrevealed reputation data remain filtered before summaries/counts/AI context;
8. MNCS does not mint a second reputation ledger or mutate reputation outside MIB-09/Relationship owner operations.

## Existing authorities MNCS consumes

- **PPIA-02 / Character-NPC-Creature owners:** reusable Definition, persona/profile, placement, live instance, variants/forms, conversion and visibility boundaries.
- **MIB-09:** deterministic relationship/reputation dimensions, modifier/event application, organization projection and provenance.
- **DPL:** profession, business, research, household/family, education, cultural practice, health/stress and other life-context systems.
- **Species/Form and progression owners:** biology/topology, eligible traits/forms and advancement truth.
- **World / Environment / Reality / Branch / Settlement:** location, culture/environment constraints, demographics/ecology and world truth.
- **Inventory/Asset / Ability / Action / Effect / Condition / Resource:** mechanics and owned reusable records.
- **Encounter / Scene / Combat / Investigation / Dialogue / Exploration:** usage contexts and live runtime authority.
- **ODL / Faction / Organization:** organization, crew, household, business, faction and leadership seams.
- **MCCS:** optional appearance/portrait/token/sprite handoff only.
- **MAS:** downstream Adventure cast/creature consumption.
- **ARI:** resource identity, provenance, rights and derivative lineage.
- **MRCS (later):** reusable authored roles, behavior packages, templates and generator/content definitions when available.

## Benchmark provenance and clean-room boundary

Planning benchmarks include the owner-supplied references UNE (Universal NPC Emulator), GameMaster's Apprentice, Perchance's Ambitious NPC Generator, World Wizard NPC Builder, MonsterShuffler, and other public TTRPG NPC/monster generators and VTT-integrated generators including Kassoon and Foundry ecosystem generators.

The owner also supplied the label `NPC Suite`; exact product identity was not unambiguously resolved during the benchmark, so MNCS records no vendor-specific capability claim for that label until an exact source is identified.

The detailed synthesis is recorded in `MNCS_BENCHMARK_CAPABILITY_MATRIX.md`.

MNCS follows PCM clean-room rules: public documentation and lawful ordinary-use behavior may establish capability classes and workflow requirements, but protected source, proprietary tables, authored NPC libraries, distinctive UI expression, private prompts, private protocols or vendor implementation details are not copied.

## Program tranches

### MNCS-01 — NPC/Creature Studio Workspace, Authority Contract & Resolution Ladder

Define the studio workspace, stable generated-candidate identity, owner references, NPC/creature resolution ladders, accepted/locked/unresolved dispositions, summary↔detail rules, history/undo and no-duplicate-identity invariants.

### MNCS-02 — Generation Recipe, Seed, Weight, Lock, Reroll & Selective-Regeneration Engine

Implement provider-neutral generation recipes, deterministic seeds where requested, weighted tables/choices, exclusions, locks, selective reroll, conflict handling and provenance receipts. Regeneration must never silently replace accepted/locked facts.

### MNCS-03 — Campaign/World/Location/Environment Constraint Resolver

Build the authorized context projection used before generation: Campaign, World, location, era, environment, settlement, faction, culture, species/form eligibility, profession/economy context and other available owner constraints. Unknowns remain explicit.

### MNCS-04 — Identity, Naming, Culture, Language, Demographic & Origin Construction

Generate or author identity/origin layers using eligible naming/cultural/language/species/location records, aliases and titles. Preserve source/proposal distinction and support beings without human-style personal names.

### MNCS-05 — Instant Improv, Role-First & Situation-First Generator

Provide the five-second GM surface: role/function, current situation, memorable cue, demeanor, immediate want, relation to the scene and minimum mechanics/context needed now. Support prompts such as merchant, witness, guard, neighbor, scholar, roadside animal, local predator or "who answers the door?" without forcing full dossiers.

### MNCS-06 — Persona, Motive, Goal, Value, Fear, Habit & Contradiction Studio

Construct playable personality handles: goals, desires, fears, values, loyalties, habits, limits, contradictions, stressors and memorable traits. Avoid deterministic mind-control equations; persona guides portrayal and owner-authored behavior.

### MNCS-07 — Knowledge, Belief, Memory, Suspicion, Reliability & Misinformation Model

Track what an NPC knows, believes, suspects, misunderstands, remembers, was told or intentionally misrepresents, with source/time/confidence where governed. Knowledge projection remains visibility-safe and does not imply omniscience.

### MNCS-08 — Relationships, Factions, Reputation & Party-Association Influence

Integrate MIB-09 and relationship/faction owners for family, friendship, rivalry, debt, mentorship, employment, loyalty, reputation and organization ties. Implement Campaign-scoped party-association reputation projection with direct-vs-associated decomposition, faction-specific weighting, event attribution, join/leave semantics and visibility-safe provenance. MNCS never becomes the reputation ledger.

### MNCS-09 — Profession, Household, Economy, Schedule, Project & Life-Context Construction

Compose DPL, Economy, household, organization and Project owners to give relevant NPCs actual work/life context: profession, competence, workplace, household, dependents, obligations, ordinary schedule, ongoing Projects, services and economic role without requiring this depth for passing extras.

### MNCS-10 — Mechanics-on-Demand, Rules Profile, Threat & Encounter-Role Expansion

Expand the same identity from minimal competence tags to owner-valid rules profiles only when needed. Use governed species/profession/ability/action/effect/condition/resource records, advisory threat/encounter roles and CAB/domain validation where applicable; never invent missing numeric mechanics merely to finish a sheet.

### MNCS-11 — Ability, Equipment, Inventory, Resource & Capability Composition

Bind existing abilities, actions, equipment, natural weapons, inventory, resources and services to generated beings. Hidden inventory and loot remain permission-filtered; linked mechanics are referenced rather than copied.

### MNCS-12 — Creature Ecology, Habitat, Diet, Lifecycle & Environmental Adaptation

Generate/author creature ecological context from governed environment/species inputs: habitat, range, diet, activity cycle, reproduction/lifecycle where appropriate, adaptations, predator/prey/resource relationships and environmental constraints. Ecology is first-class, not flavor appended after a stat block.

### MNCS-13 — Creature Behavior, Instinct, Social Structure, Territory & Tactics

Provide behavior packages for solitary, herd, pack, swarm, colonial, territorial, predatory, scavenging, guardian, parasitic, constructed, sapient and extensible patterns. Separate ecological/behavior guidance from live GM adjudication and combat Action authority.

### MNCS-14 — Species, Form, Stage, Template, Variant, Mutation & Role Composition

Compose base species/creature, Form, age/stage, role/profession, template/modifier, environmental adaptation, equipment and unique traits with compatibility checks. Preserve base/variant provenance and do not flatten every difference into a second full copied stat block.

### MNCS-15 — Household, Crew, Court, Team, Crowd & Social-Group Generation

Generate related groups together so members have coherent roles, relationships, skills and context: households, tavern occupants, ship crews, work shifts, courts, squads, guild teams, businesses and similar groups. Group generation must create explicit references rather than isolated unrelated NPCs.

### MNCS-16 — Settlement, Organization & Population Generation / Individualization

Generate population distributions and representative cohorts from owner-supplied settlement/organization/demographic context without materializing every person. Promote a summarized population member into a stable NPC identity when encountered or selected, preserving population provenance.

### MNCS-17 — Herd, Pack, Swarm, Colony & Ecosystem Population Generation

Provide creature population/group generation with ecological constraints, group composition, age/stage/role distributions and individual promotion. A herd/pack/swarm may remain summarized until play needs individual instances.

### MNCS-18 — Secrets, Public/Private Layers, Aliases, Disguises & Reveal Conditions

Author public identity, player-known facts, GM-private motives, hidden relationships, secrets, lies, unknown forms, aliases/disguises and reveal conditions through existing visibility owners. Hidden existence cannot leak through search counts, facets, diagnostics or optional-AI context.

### MNCS-19 — Conversation Prep, Speech/Voice Cues, Topics, Bargaining & Roleplay Card

Provide concise at-table cues: greeting, demeanor, speech description, sample phrases, likely topics, knowledge, evasions, tells, bargaining position, social triggers and reactions. This is GM-facing preparation; MNCS does not make autonomous NPC dialogue or AI impersonation authoritative.

### MNCS-20 — Continuity, Goals, Events, Advancement & Life/Ecology Change Over Time

Consume authoritative Events and owner-domain changes so recurring NPCs/creatures can accumulate history, relationships, injuries, reputation, goals, Projects, location changes, progression and ecological/lifecycle change. Regeneration never overwrites lived history.

### MNCS-21 — Promotion, Demotion, Retirement & Simulation-Resolution Management

Implement safe transitions among population, extra, minor, recurring, full and major resolutions (and creature equivalents), including dormant/retired/archive state. Reducing active simulation detail preserves identity, accepted facts and event history rather than deleting them.

### MNCS-22 — Runtime Handoff: Scene, Encounter, Social, Investigation, Exploration & MAS Cast

Provide governed acceptance and handoff into Scene/Encounter/Combat, Relationship/Investigation, Exploration/Bestiary, Dialogue/Social and MAS cast/adventure workflows. Placement/live instances remain distinct and exact source/version/provenance accompanies handoff.

### MNCS-23 — Batch Generation, Presets, Import/Export, Review, Sharing, Provenance & Optional AI Enrichment

Support creator presets/generation recipes, batch NPC/creature/group generation, structured import/export, diff/review, clone/fork, Pack/ARI provenance, reusable generation profiles and optional visibility-safe AI enrichment. Imported/generative material remains candidate content until accepted.

### MNCS-24 — Golden Progressive NPC/Creature Generation & Campaign-Continuity Proof

Create an original golden suite proving at least:

1. five-second passing NPC promoted to recurring full NPC without identity replacement;
2. role-first merchant/witness/antagonist construction;
3. settlement population member promoted to an individual NPC;
4. household or crew generated as a coherent relationship group;
5. ordinary animal plus herd/pack population;
6. nonhumanoid creature with ecology and behavior;
7. sapient nonhuman or intelligent animal using NPC/social systems;
8. staged/template creature variant;
9. campaign NPC with knowledge/belief/secret/reveal layers;
10. party-association reputation case where one PC's attributed action changes another PC's faction reputation in the same Campaign without erasing individual reputation;
11. equivalent second Campaign proving no reputation spillover across Campaign boundaries;
12. NPC accepted into MAS/Scene/Encounter and later changed by authoritative Events without regeneration erasing history.

The proof must also demonstrate deterministic generation receipts where claimed, field locking/selective reroll, constraint-aware generation, visibility-before-search/AI, mechanics-on-demand, owner-bound runtime handoff, ARI provenance, offline/local-first blocking workflows and optional-AI-off success.

## Cross-cutting requirements

Every MNCS tranche must preserve:

- definition/candidate/placement/live-instance separation;
- authorization filtering before search/counts/facets/graphs/AI context/export;
- source facts versus generated proposals versus accepted Campaign-local facts;
- stable identity across resolution changes;
- selective regeneration with accepted/locked-field protection;
- owner-domain references rather than copied rule text where possible;
- exact provenance and deterministic receipts where determinism is claimed;
- explicit unknown/unresolved/unsupported states rather than invention;
- keyboard/touch/screen-reader alternatives for essential creator operations;
- local-first blocking workflows without paid/cloud AI;
- optional AI candidate-only authority;
- no autonomous GM, consent, permission, canon or live-event authority.

## Explicit non-goals

MNCS does not:

- reproduce or scan real people or build a digital-human/avatar-reconstruction product;
- replace Character, NPC, Creature, Species/Form, Relationship/Reputation, Faction, Profession, World, Inventory, Encounter or Action/Event canonical owners;
- replace MCCS visual appearance creation;
- replace MRCS reusable rules/content authoring;
- replace MAS Adventure assembly;
- create one global shared-party reputation score;
- make random output canonical merely because generation completed;
- fabricate missing source mechanics, demographics, ecology or knowledge as fact;
- require autonomous LLM roleplay for NPC operation;
- require a paid/cloud generation provider;
- copy proprietary generator tables, NPC libraries, source code, prompts or distinctive UI.

## Family execution rule

When MNCS is eventually selected, it receives its own sealed family preflight. Every execution unit must target 24 active minutes or less under a healthy governed environment with protected closeout reserve. Any unit that cannot credibly fit is split before governed start.

No MNCS implementation authority exists now.

## Completion standard

MNCS is complete only when all 24 tranches are `completed_verified`, the golden suite proves progressive identity-preserving resolution, context-aware generation, NPC and creature group/population workflows, MIB-09 party-association reputation attribution, visibility-safe knowledge/secrets, mechanics-on-demand, ecology/behavior, event-driven continuity and governed runtime/MAS handoff, while all blocking generation works without a paid/cloud AI provider.