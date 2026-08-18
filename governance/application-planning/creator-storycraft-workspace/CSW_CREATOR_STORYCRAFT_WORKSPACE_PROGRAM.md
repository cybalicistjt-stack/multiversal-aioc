# CSW — Creator Storycraft Workspace Program

**Program ID:** CSW  
**Version:** 0.1.0  
**Status:** OWNER-APPROVED PARALLEL PLANNING TRACK — PLANNED / NOT IMPLEMENTATION-ACTIVE  
**Owner and final authority:** John Brandon Turner  
**Approved planning direction:** 2026-08-18

## 1. Purpose

CSW defines the creative-workflow, project-memory, story-development, writing, continuity, and reuse layer that helps Multiversal users invent, develop, organize, remember, write, test, and reuse tabletop material.

The program is not a second World Builder, Adventure system, content database, or autonomous story generator. It orchestrates the existing governed World, Adventure, creator-content, Character, investigation, relationship, Campaign, visibility, provenance, and future Personal-workspace capabilities into a coherent creator experience.

The target product loop is:

`Capture → Develop → Connect → Structure → Write → Check → Use → Reuse`

Multiversal should remember the creator's work across that loop without silently converting ideas or drafts into Campaign truth, published content, or canonical source material.

## 2. Owner-approved product principles

The following are controlling CSW product decisions unless later superseded by explicit owner authority:

1. Multiversal should actively help creators with plot, ideas, hooks, backstories, adventures, worlds, characters, factions, mysteries, scenes, lore, and writing.
2. Creative assistance should reduce blank-page friction while preserving creator agency. The app should help a person create rather than replace the person as author.
3. The system should keep track of what a creator has made, where it came from, how it changed, where it is used, what references it, and what remains unfinished.
4. Scratch ideas, prompts, notes, possibilities, alternates, and creative fragments are first-class private creative material even when they are not yet valid game objects.
5. Creative material becomes a governed World, Adventure, Campaign-local object, Character fact, or other authoritative object only through an explicit incorporation, conversion, clone/propose, publish, install, or promotion action owned by the relevant domain.
6. The same creative material may be reused, remixed, adapted, or templated without destroying provenance or silently mutating the source.
7. The app should help creators discover forgotten material, unresolved threads, contradictions, missing payoffs, underused characters/locations, and useful connections.
8. Structured creation guidance is optional. Experienced creators must be able to work directly without being forced through a wizard.
9. Non-AI creative support remains important: prompts, tables, constraints, combinations, templates, checklists, structure tools, deterministic generators, and relationship/timeline analysis must provide useful value without an AI provider.
10. Optional AI may suggest, expand, transform, summarize, compare, critique, or draft from creator-authorized context, but it may not silently overwrite creator work, publish, reveal, promote, or mutate authoritative Campaign state.
11. AI-generated or AI-assisted material must remain attributable enough for the creator to understand what was suggested and what source context was used where practical under the governing AI architecture.
12. Private creative work, Campaign secrets, unrevealed Adventure material, and other hidden information remain subject to existing visibility and authorization rules before search, graphs, suggestions, exports, diagnostics, notifications, or optional-AI context.
13. CSW should integrate with APW's Personal Workspace and Creator Workshop but not depend on APW implementation in order to complete its own planning.
14. CSW should reuse A10's split World/Adventure/authoring-provenance ownership instead of creating monolithic storycraft persistence that bypasses owning domains.

## 3. Relationship to existing canonical architecture

CSW is additive over existing canonical work, especially:

- A2 stable object identity, versions, provenance and universal object behavior;
- A3 identity, contextual authorization and workspace selection;
- A4 Character persistence and advancement history;
- A5 Campaign, Scene and Session authority;
- A6 Action/proposal authority where a creative operation becomes Campaign-affecting;
- A9 investigation, clue, hypothesis, relationship, reputation and faction runtime state;
- A10 World/Location, Adventure/Module, creator-content and authoring-provenance architecture;
- D18 `world-location-map` as World/Location/semantic geography authority;
- D28 `adventure-travel` as Adventure/Module and Campaign run-local adventure authority;
- D29 `authoring-provenance` as draft/proposal/review/publication provenance authority;
- D05 `visibility-projection` for privacy-before-search/topology/cardinality/AI behavior;
- D07 reusable definition/version/variant/dependency identity;
- APW Personal Workspace, Creator Workshop, reusable library and Sandbox/Lab planning;
- PPIA-08 Campaign/Scene/Session authoring depth;
- PPIA-09 Investigation & Mystery Authoring Kit;
- PPIA-10 Relationship/Social/Faction content framework;
- PPIA-11 Encounter & Balance Design Laboratory;
- PPIA-12 World & Setting Authoring System;
- PPIA-13 onboarding/help/teaching content;
- PPIA-14 recovery/permission microcopy.

Published or installed content remains governed by its owning domain. CSW may coordinate and project across those domains but may not become an alternate source of mechanical, World, Adventure, Character, Campaign, relationship, investigation, Asset, or canonical-content truth.

## 4. Creative material classes

CSW planning must establish a bounded creative vocabulary that can represent useful pre-authoritative material. Candidate classes include:

- Idea;
- Premise;
- Hook;
- Theme;
- Question;
- Conflict;
- Secret;
- Twist;
- Foreshadow;
- Payoff;
- Beat;
- Arc;
- Thread;
- Rumor;
- Lore Fragment;
- Character Motivation;
- Backstory Element;
- Scene Seed;
- Encounter Seed;
- Mystery Seed;
- Location Seed;
- Faction Seed;
- NPC Seed;
- World Seed;
- Open Question;
- Constraint;
- Reference;
- Alternate;
- Scratch Note.

The exact normalized list belongs to CSW-01. These classes must not be confused with already-authoritative objects such as published Adventure nodes, actual Campaign clues, Character facts, World entries, or runtime Events.

## 5. Program boundaries

CSW planning does not itself authorize:

- application implementation;
- migration execution;
- a new AI provider or paid AI service;
- autonomous story generation or publication;
- silent AI mutation of creator content;
- ingestion of private user material for training;
- public marketplace/community publication;
- canonical promotion;
- release, deployment, tester access, or production credentials;
- replacement of A10, APW, or owning-domain persistence.

Those remain separately governed.

## 6. Tranche plan

### CSW-01 — Storycraft Vocabulary, Creative Object Model and Authority

**Goal:** define the pre-authoritative creative layer and its boundaries before building creator workflows.

**Deliverables:**

- normalized creative-fragment vocabulary;
- lifecycle states such as inbox/scratch/developing/ready/incorporated/superseded/archived;
- ownership, authorship, visibility, edit, link, convert, incorporate, archive, delete and reuse authority matrix;
- Personal versus Campaign-bound creative-material distinctions;
- explicit distinction between idea/hypothesis/possibility and authoritative fact;
- conversion/incorporation boundaries into D18 World, D28 Adventure, Character, Campaign, investigation, relationship and other owning domains;
- stable identity/version/provenance requirements;
- deletion/tombstone/reference integrity rules;
- traceability to A10 and APW.

**Completion gate:** no creative fragment can accidentally masquerade as Campaign truth, published content, canonical content, or another domain's authoritative object, and all conversion paths are explicit.

### CSW-02 — Creative Library, Story Bible and Project Memory

**Goal:** make creator work durable, findable and understandable over long projects.

**Deliverables:**

- creative-library information architecture;
- Story Bible model for Characters, NPCs, locations, factions, lore, terminology, themes, timeline facts and creator notes;
- project/collection/folder/tag and cross-project organization;
- relationship/reference graph between creative fragments and governed objects;
- backlinks, `used in`, `derived from`, `inspired by`, `replaced by`, and version relationships;
- creator timeline/history and change provenance;
- search, filters, saved views and creator-safe graph/outline projections;
- duplicate/near-duplicate discovery rules without silent merging;
- archive and rediscovery behavior;
- import/export and recovery requirements.

**Completion gate:** a creator can reliably answer what they made, where it is, how it changed, what uses it, and what related work exists without relying on memory or external notes.

### CSW-03 — Idea Inbox and Inspiration Engine

**Goal:** make capturing and developing inspiration almost frictionless.

**Deliverables:**

- rapid text-note capture and conversion-to-fragment flows;
- Idea Inbox and triage workflow;
- structured prompts and deterministic generators for hooks, conflicts, complications, rumors, motivations, secrets, locations and similar seeds;
- constraint-driven random tables and combination tools;
- `develop this`, `give alternatives`, `combine these`, `invert this`, and `find related unused material` interaction contracts;
- creator-controlled inspiration sources/references;
- deduplication/similarity suggestions;
- optional-AI suggestion contract with source/context boundaries;
- save/discard/branch suggestion workflow so generated suggestions never overwrite source material.

**Completion gate:** a one-line idea can be captured and developed into multiple attributable possibilities using both non-AI and optional-AI assistance without creating authoritative content automatically.

### CSW-04 — Guided Creation Workflows

**Goal:** provide optional structured assistance for common creator tasks without forcing a single creative method.

**Deliverables:**

- guided workflow framework and reusable question/step primitives;
- backstory creator;
- NPC/antagonist creator;
- faction creator;
- settlement/location creator;
- World/culture creator;
- mystery creator;
- adventure/quest creator;
- encounter creator;
- Campaign premise/arc creator;
- progressive disclosure, skip/revisit and freeform escape behavior;
- templates and creator-owned reusable workflow presets;
- context-aware suggestions from existing Story Bible material;
- accessibility/mobile/nonvisual parity.

**Completion gate:** novice users can reach a coherent usable draft through guidance, while expert users can bypass or customize the guidance without losing capabilities.

### CSW-05 — Plot, Adventure and Narrative Design Lab

**Goal:** give creators serious tools for structuring nonlinear tabletop stories rather than only linear prose outlines.

**Deliverables:**

- plot thread, beat, arc, scene, hook, revelation, choice, consequence and payoff projections;
- outline, board, timeline and graph views with semantic nonvisual alternatives;
- explicit links to D28 Adventure nodes/edges where material has been incorporated;
- branching and optional-content planning;
- prerequisite, clue/revelation, choice and consequence planning;
- pacing/pressure and spotlight notes;
- alternate-route and failure-state planning;
- player-agency warnings where structure becomes overly single-path, presented as advisory rather than enforced doctrine;
- Campaign-specific versus reusable Adventure planning boundary;
- safe transition from creative structure into governed Adventure definitions.

**Completion gate:** creators can plan a branching tabletop adventure from hooks through outcomes while maintaining a visible distinction between speculative structure and incorporated Adventure truth.

### CSW-06 — Continuity, Consistency and Open-Thread Tracker

**Goal:** help creators find what they forgot or contradicted before those problems become play friction.

**Deliverables:**

- open-thread registry;
- unresolved hook/question/secret/foreshadow/payoff tracking;
- unused and dormant Character/NPC/location/faction/idea detection;
- timeline/date inconsistency checks where sufficient structured data exists;
- name/term/style consistency checks;
- dangling reference and orphan detection;
- clue-purpose and mystery-coverage advisory analysis without treating hypotheses as objective truth;
- contradiction candidates with evidence links rather than automatic correction;
- `needs attention`, `possibly inconsistent`, `unused`, `resolved`, and `intentionally unresolved` states;
- creator dismissal/snooze/accept behavior;
- privacy-filtered analysis and optional-AI context.

**Completion gate:** the app can surface actionable continuity/open-thread candidates with traceable evidence while never silently rewriting creator or Campaign truth.

### CSW-07 — Writing Studio and Revision Workspace

**Goal:** make Multiversal a practical place to write and revise the prose that surrounds game content.

**Deliverables:**

- longform and shortform writing surfaces for backstories, lore, descriptions, scene text, handouts, rumors, letters, journals, summaries, pitches and GM notes;
- outline-to-draft and fragment-to-draft workflows;
- revision history, branches/alternates and comparison;
- reusable terminology/style/voice notes;
- fact/reference side panel sourced from creator-authorized Story Bible material;
- linkable prose references to governed objects without embedding duplicate truth;
- export/print/handout boundaries;
- optional assistance for expand/shorten/rephrase/tone/clarity while preserving factual constraints;
- explicit apply/reject/compare behavior for generated revisions;
- accessibility, autosave and recovery contracts.

**Completion gate:** creators can draft and revise prose with recoverable history and factual/context support while retaining control over every accepted change.

### CSW-08 — Reuse, Remix and Transformation

**Goal:** let one good creative artifact generate future value without destroying provenance.

**Deliverables:**

- clone/adapt/template/fork/remix relationships;
- transform Character/NPC/location/lore/history material into hooks, seeds, rumors, conflicts, scenes or Adventure candidates;
- Campaign-runtime-to-reusable clone/propose flow consistent with A10;
- World-to-World and Campaign-to-Campaign adaptation rules;
- reusable creator templates and starter kits;
- explicit source attribution and inherited-reference handling;
- conflict behavior when source versions change;
- compare/rebase/manual-adapt options where meaningful;
- cross-setting compatibility warnings as advisory projections;
- no silent propagation of source edits into derived work.

**Completion gate:** a creator can reuse and transform material across projects with clear provenance, independent versions and no unintended mutation of the source or live Campaign state.

### CSW-09 — Creator Command Center and Assistance Integration

**Goal:** make creative work easy to resume and easy to understand at a glance.

**Deliverables:**

- creator-focused Home/Command Center projection;
- `Continue Writing`, `Ideas to Develop`, `Open Threads`, `Needs Attention`, `Recently Created`, `Unused Material`, `Drafts`, `Story Bible`, and `Campaigns Using My Work` surfaces;
- deep links and return-to-context behavior;
- Personal/Campaign/project context indicators;
- creator task and reminder hooks where later scheduling capability exists;
- integrated search and universal creator command palette behavior;
- optional contextual assistant entry points with visible source/context scope;
- no-AI fallback parity for core organization/development workflows;
- APW Personal Workspace/Creator Workshop integration map;
- responsive/accessibility/empty/offline/recovery states.

**Completion gate:** a returning creator can immediately see what they were doing, what deserves attention, and where to continue without reconstructing project state manually.

### CSW-10 — Integration, Acceptance and Implementation Handoff

**Goal:** turn CSW into dependency-ordered application work without duplicating A10 or APW and without invalidating completed Stage A evidence.

**Deliverables:**

- implementation-ready packet set and cross-domain traceability matrix;
- exact persistence/change inventory, including what belongs in D29 versus a new bounded creative-support persistence seam if genuinely necessary;
- A10 World/Adventure/creator integration map;
- APW Personal Workspace/Creator Workshop integration map;
- Character, Campaign, investigation, relationship/faction and future-AI integration map;
- feature flags/fallback requirements where appropriate;
- deterministic fixtures and acceptance inventory;
- UI/screen/navigation contracts;
- migrations and compatibility plan where genuinely required;
- dependency-ordered implementation slices;
- Internal Alpha placement and scope recommendation;
- explicit non-reopening rule for completed Stage A milestones;
- end-to-end `haunted lighthouse` creator proof.

**Completion gate:** every planned application change has an owning domain, dependency, persistence boundary, acceptance gate, rollback/compatibility strategy and implementation destination, and the track can demonstrate the complete Capture → Develop → Connect → Structure → Write → Check → Use → Reuse loop.

## 7. Execution order

Planning order is strictly:

`CSW-01 → CSW-02 → CSW-03 → CSW-04 → CSW-05 → CSW-06 → CSW-07 → CSW-08 → CSW-09 → CSW-10`

A later tranche may collect references early, but it may not finalize contracts that depend on unfinished predecessors.

Within each tranche, complete the bounded substantive package first, run the smallest relevant deterministic checks during construction, batch repairs, then run the declared tranche gate. Do not substitute repeated roadmap/checkpoint rewrites for substantive design work.

## 8. Provisional downstream implementation handoff

CSW-10 must finalize implementation IDs and dependency placement. The provisional implementation handles are:

1. **CSW-I01 — creative-fragment identity, lifecycle, provenance and authority foundation**;
2. **CSW-I02 — Creative Library, Story Bible, links, search and project memory**;
3. **CSW-I03 — Idea Inbox, deterministic inspiration tools and optional suggestion seam**;
4. **CSW-I04 — guided creator workflows and templates**;
5. **CSW-I05 — Plot/Adventure Design Lab and continuity/open-thread analysis**;
6. **CSW-I06 — Writing Studio, revisions and factual-reference support**;
7. **CSW-I07 — reuse/remix/transformation and creator provenance flows**;
8. **CSW-I08 — Creator Command Center, APW integration and end-to-end creator acceptance**.

These are planning handles only until CSW-10 publishes the final implementation handoff and the governing application roadmap explicitly activates them.

## 9. Minimum end-to-end creator proof

The eventual first full proof should begin with the intentionally small seed **`haunted lighthouse`** and demonstrate that a creator can:

1. capture the phrase as a private idea without creating World or Campaign truth;
2. develop alternate hooks, conflicts, secrets and questions;
3. create or link an NPC, location, history/lore fragments and related references;
4. structure a branching Adventure candidate with scenes, revelations, choices and consequences;
5. receive evidence-backed continuity/open-thread warnings for missing or contradictory material;
6. draft usable location, NPC, hook and scene prose;
7. preserve revision history and choose which suggested edits to apply;
8. incorporate selected material into governed World/Adventure definitions through explicit owning-domain transitions;
9. preserve unused ideas and alternates in the creator library;
10. later discover and reuse/remix part of the lighthouse material in another project without mutating the original or losing provenance.

## 10. Relationship to APW and A10

**A10 owns governed authoring/content truth.** CSW does not replace World, Adventure or creator-content persistence. It adds the creative-development and project-memory workflows that lead into and surround those governed objects.

**APW owns the broader Personal/campaign-independent workspace direction.** CSW should appear naturally inside the APW Personal Workspace/Creator Workshop when those surfaces exist, but CSW remains a separately governed creative-product track because its vocabulary, memory, writing, continuity and storycraft requirements are broader than APW's asynchronous/persistent-use objective.

Neither track completes the other. Their implementation handoffs must reconcile dependencies before application activation.

## 11. AI boundary

CSW should be excellent without AI. Core capture, organization, Story Bible, linking, templates, deterministic generators, structured prompts, plot boards, continuity rules, writing/revision history and reuse workflows must function without an external AI provider.

Where optional AI is later enabled, it may:

- brainstorm alternatives;
- expand or condense creator material;
- suggest links and hooks;
- critique continuity or structure;
- transform material into candidate forms;
- assist with prose drafting/revision;
- summarize creator-authorized context.

It may not silently accept its own suggestions, publish, canonize, reveal hidden material, mutate live Campaign state, or override owner/creator decisions.

## 12. Program completion

CSW planning is complete only when CSW-01 through CSW-10 are `completed_verified`, their final implementation handoff is merged, roadmap/dependency projections are synchronized, and no required creator workflow depends on an unstated authority, provenance, privacy, persistence, or AI assumption.

Completion of CSW planning does not mean CSW application implementation is complete.
