# MXS-04 through MXS-08 — Human Experience Architecture

**Version:** 0.1.0  
**Status:** STRATEGY DESIGN / RESEARCH SYNTHESIS  
**Prepared:** 2026-08-13

## Purpose

Multiversal should not merely make TTRPG mechanics computationally available. It should preserve and amplify the psychological qualities that make tabletop role-playing worth doing: agency, mastery, belonging, imagination, identity exploration, collaborative creativity, suspense, discovery, memory and meaning.

This document converts research and TTRPG practice into product constraints for MXS-04 Player Psychology, MXS-05 GM Psychology/Cognitive Load, MXS-06 Social Table Dynamics, MXS-07 Learning/Progressive Complexity and MXS-08 Meaningful Gamification/Campaign Memory.

It does not diagnose users, infer personality types, manipulate retention, or claim therapeutic outcomes.

---

# MXS-04 — Player Motivation and Experience Architecture

## Evidence-backed motivational model

A useful baseline comes from Self-Determination Theory work on games: engagement and well-being are strongly related to experiences of **autonomy, competence and relatedness**. Flow research adds **challenge-skill balance, clear goals and sense of control**, with clear feedback also a recurring design factor.

These are design lenses, not a formula that guarantees fun. MXS treats them as requirements to examine, not scores to maximize mechanically.

## 1. Autonomy — “My choices are mine and they matter”

### Product principles
- present meaningful alternatives rather than decorative choices;
- explain consequences when the Character/table could reasonably know them;
- distinguish rule restriction from GM decision from missing information;
- permit reversible exploration before irreversible commit where rules allow;
- support multiple valid approaches rather than optimizing every user toward one build/play style;
- allow the table to choose which optional systems and Play Experience Profiles matter.

### Failure modes
- automation silently chooses for the user;
- recommendation becomes de facto mandatory;
- UI hides valid options because they are statistically uncommon;
- AI drafts become canonical automatically;
- onboarding funnels every table into the same style.

## 2. Competence — “I understand more and can do more than before”

### Product principles
- make rules discoverable at the moment they matter;
- show why an action succeeded/failed;
- expose improvement through meaningful Character/world capability, not app-use points;
- preserve expert fast paths;
- provide comparison/preview before commitment;
- allow users to learn from consequences and previous similar events.

### Failure modes
- opaque automation;
- overwhelming full-detail views for novices;
- patronizing simplified modes that remove meaningful control;
- public ranking that makes lower-skill players feel deficient;
- rewarding clicks rather than mastery.

## 3. Relatedness — “What I do matters to people I care about”

### Product principles
- emphasize party, relationships, shared history and collaborative creation;
- make contributions attributable without turning them into competition;
- preserve memories of joint decisions and accomplishments;
- enable private and shared notes/communication;
- show how Character choices affect relationships and the world when authorized;
- support co-GM/shared-authority tables.

### Failure modes
- social leaderboards;
- artificial popularity scores;
- engagement nudges that pressure attendance;
- exposing private player activity;
- using automated participation scores as authority.

## 4. Flow and cognitive fit

### Product principles
- expose only the relevant toolbox for the current Play Experience Profile;
- keep current goals/stakes visible without forcing quest-marker logic onto open-ended play;
- make feedback timely and unambiguous when the fiction permits;
- prevent UI/search/lookup work from becoming the dominant challenge;
- allow tables to tune mechanical depth and assistance level.

### Product implication
Multiversal should measure success primarily by **friction removed from intended play**, not by time spent in software.

## 5. Curiosity, uncertainty and discovery

### Product principles
- preserve unknown information as genuinely unknown;
- support rumor, uncertainty and partial knowledge states;
- reveal through play, not through accidental UI leakage;
- make discoveries link into larger world context;
- allow players to form hypotheses without the system signaling whether they are true.

## 6. Identity and character attachment

TTRPG research and practice suggest role-play can provide a bounded space for identity exploration and perspective taking.

### Product principles
- Character identity is more than optimized statistics;
- appearance, beliefs, drives, relationships, history and accomplishments deserve equal representational status;
- users control presentation and privacy of identity-relevant material;
- Character arcs can be recorded without the platform judging psychological meaning;
- the platform never infers real-world identity from fictional Character choices.

## 7. Failure should create information, cost or story—not user shame

### Product principles
- distinguish Character failure from player error;
- make recoverability clear;
- preserve partial success, success-at-cost and complication-based outcome models;
- use failure history to explain consequences, not to produce public performance rankings.

---

# MXS-05 — GM Psychology, Facilitation and Cognitive Load

## The GM is a real-time orchestration role

Research on GM practice describes dynamic co-creation and improvisation as central, while recent TTRPG group research links facilitation with clarity, support, cohesion and creativity. Multiversal should therefore optimize the GM's **attention**, not simply provide more information.

## Three-loop GM model

### Loop A — Prepare
The GM needs to:
- recover where the Campaign left off;
- inspect unresolved threads;
- select/create adaptable material;
- understand Characters, motivations and table preferences;
- stage likely Scenes without predicting player decisions;
- test content/rules before the session.

### Loop B — Facilitate live play
The GM simultaneously:
- listens to players;
- portrays the world/NPCs;
- protects secrets;
- adjudicates uncertain actions;
- tracks mechanical/world state;
- manages pacing and transitions;
- distributes opportunities for participation;
- improvises around unexpected decisions;
- handles rules questions;
- manages interruptions/reconnects;
- remembers consequences.

### Loop C — Recover and continue
After play the GM needs to:
- know what actually changed;
- distinguish canonical events from notes/ideas;
- identify unresolved promises, threats, clues and projects;
- understand downstream effects;
- prepare the next session without rereading the campaign.

## GM cognitive-load budget

A live GM surface should minimize five expensive forms of load:

1. **Search load** — where is the thing?
2. **Context-switch load** — which subsystem/app/tab must I move to?
3. **State-reconstruction load** — what is currently true?
4. **Rule-reconstruction load** — why does this mechanic apply?
5. **Consequence-memory load** — what did I promise/change and what should follow from it?

### Design standard
For an ordinary current-scene decision, the GM should not need broad exploratory navigation. The system should assemble a **decision context packet** containing only authorized, relevant information and links to deeper detail.

## Contextual GM Cockpit

Not one giant dashboard. A cockpit is a context-sensitive composition.

### Persistent strip
- Campaign/Scene/session identity;
- current Play Experience Profile;
- active participants/roles;
- time/state/reconnect health;
- urgent pending decisions.

### Current-scene context
- visible and GM-hidden scene facts;
- current cast;
- active Conditions/Effects/clocks;
- relevant relationships/reputation;
- current threats/projects;
- scene notes;
- likely rules references derived from actual state.

### Decision queue
- player proposals;
- required GM decisions;
- modifications and previews;
- hidden-information warnings;
- version conflicts;
- unresolved network-operation status.

### Memory cues
- promises/debts;
- unresolved clues;
- dormant NPC/faction threads now relevant;
- prior related decisions;
- source/provenance on demand.

## Assistance boundary

AI/system assistance may:
- retrieve;
- summarize authorized context;
- propose consequences;
- draft NPC dialogue;
- compare options;
- identify potentially forgotten threads;
- simulate bounded noncanonical outcomes;
- flag contradictions.

It may not silently:
- decide what the GM intends;
- reveal hidden state;
- advance factions/world state;
- approve player actions;
- rewrite canon;
- resolve ambiguity by invention.

---

# MXS-06 — Social Table Dynamics, Consent and Shared Authority

## Group experience is a core product dimension

Research on multiplayer RPG experience indicates group dynamics are integral to play quality, and recent TTRPG research connects facilitation, clarity, support, cohesion and creativity. Therefore Multiversal should support **table formation and calibration**, not merely individual accounts connected to the same Campaign.

## Playstyle Compass

A transparent session-zero tool allowing a group to express preferences without personality typing.

### Candidate dimensions
- tactical detail ↔ narrative abstraction;
- rules-light ↔ mechanically detailed;
- heroic competence ↔ dangerous vulnerability;
- planned ↔ improvisational;
- combat / social / investigation / exploration / creation emphasis;
- scarcity ↔ abundance;
- episodic ↔ long-form persistence;
- Character drama ↔ world/domain drama;
- GM-directed ↔ shared creative authority;
- theater-of-the-mind ↔ spatial play;
- casual discovery ↔ optimization/mastery;
- low ↔ high intensity for horror, interpersonal conflict and Character loss.

### Outputs
The Compass may recommend:
- Rules/Play Experience Profiles;
- UI defaults;
- optional subsystem activation;
- session-zero questions;
- content packs;
- GM prep emphasis.

It does **not** automatically change Campaign authority or expose private answers.

## Table Contract

A Campaign may maintain explicit agreements about:
- play goals and tone;
- attendance/scheduling expectations;
- PvP boundaries;
- Character death/retirement expectations;
- content lines/veils/other agreed boundaries;
- pause/rewind/skip controls;
- player versus Character secrets;
- house-rule authority;
- recording/streaming consent;
- use of AI assistance;
- public/private sharing;
- expected rules-learning burden;
- spotlight/participation preferences.

## Spotlight support without surveillance

Multiversal should never assign a “good participant” score from microphone time, chat volume or click frequency.

Useful support can instead be **opportunity-based and preference-aware**:
- GM marks or privately notes desired spotlight opportunities;
- Character goals/relationships produce contextual hooks;
- the system can remind the GM that a relevant Character connection exists;
- players may set preferences such as `actively invite me`, `let me volunteer`, or `low spotlight today`;
- group retrospectives can be voluntary and qualitative.

## Shared authority profiles

Support should eventually include:
- traditional GM;
- GM + assistant GM;
- co-GM;
- rotating scene facilitator;
- player-authorized narrative contributions;
- GMless collaborative;
- solo with oracle;
- co-op with oracle.

Authority remains explicit per operation: frame Scene, control Character/NPC, reveal truth, establish new canon, approve Action, edit rules, advance world state, publish content.

---

# MXS-07 — Learning and Progressive Complexity

## Principle

Do not create separate “easy Multiversal” and “real Multiversal.” Create different presentations of the same authoritative operations.

## Four cognitive-depth layers

### Guided
Intent-first language.

Example:
`Convince the guard to let us through.`

System surfaces only relevant choices, important risk and necessary costs.

### Standard
Shows the selected Action, likely governing factors, important alternatives and meaningful resource use.

### Advanced
Shows full available tactical/mechanical options, modifiers, dependencies, interactions and exact source links.

### Diagnostic / GM
Shows resolution pipeline, hidden modifiers when authorized, versions, provenance, validation and intervention controls.

## Learning architecture

### Learn in context
Rules help is attached to:
- current Character choice;
- current Action;
- current Condition/Effect;
- current Scene mechanic;
- actual source/rule version.

### Explain “why now”
When surfacing a rule, state why it is relevant to current context rather than dumping the entire rulebook.

### Teach through reversible exploration
Builders/editors should support preview, compare, undo and “what changes if…” where no authoritative state has yet committed.

### Preserve expert velocity
- keyboard shortcuts;
- direct search;
- bulk/advanced editing;
- compact views;
- fewer confirmations for non-destructive repeatable actions where policy permits;
- ability to pin preferred detail level per workflow.

### Mistake design
Distinguish:
- invalid according to rules;
- allowed but risky;
- not permitted by authority;
- unavailable because content is missing;
- unknown because the source does not specify;
- blocked because current state changed.

Those are different learning experiences and require different messages.

---

# MXS-08 — Meaningful Gamification, Campaign Memory and World Pulse

## Anti-dark-pattern standard

Multiversal must not use:
- login streaks;
- arbitrary XP for opening screens;
- loot-box/gambling-style engagement loops;
- artificial time scarcity intended only to drive return frequency;
- public usage leaderboards;
- social-pressure attendance scores;
- pay-to-win mechanics;
- hidden engagement optimization that conflicts with table goals.

Research on gamification shows small average effects on intrinsic motivation in some contexts and identifies autonomy/competence problems; negative-effects reviews especially warn about points, badges, leaderboards and competition when poorly aligned with the actual activity.

### Governing rule
**Progress indicators must represent meaningful progress in the game, creation process or learning task itself.**

## World Pulse

World Pulse is a signature projection of governed change.

### Session Pulse
Possible authorized sections:
- what the party accomplished;
- Character state/arc changes;
- relationships/reputation movement;
- new/updated clues;
- faction/project movement;
- discoveries;
- Asset/crafting/base changes;
- unresolved promises/debts;
- world/location/settlement changes;
- newly relevant threads.

### Player Pulse
Filtered to what that player/Character is allowed to know, potentially including personal goals and private notes.

### GM Pulse
Complete authorized operational summary including hidden clocks, consequences and unresolved design/prep cues.

### Creator Pulse
What content changed, failed validation, gained dependencies, or requires migration.

## Causal Campaign Graph / “Why Engine”

A graph/query system should eventually answer grounded questions such as:
- Why is this NPC hostile?
- What events changed this faction relationship?
- When did we acquire this Asset?
- Which decision caused this debt?
- Why is this route unavailable?
- What changed after the warehouse burned?
- Which clues support this hypothesis?
- Which rule/version produced this result?

### Evidence classes
Answers should distinguish:
- direct authoritative event;
- current canonical state;
- explicit relationship/dependency;
- rules-derived explanation;
- AI/system inference;
- player/GM-authored interpretation.

Inference may be useful but must never be presented as recorded fact.

## Meaningful progress families

### Character
- goals/arcs;
- advancement;
- relationships;
- discoveries;
- scars/transformations;
- mastery/unlocked capabilities.

### Party
- shared accomplishments;
- reputation;
- bases/assets;
- mysteries;
- alliances/rivals;
- campaign milestones.

### World
- faction projects;
- settlement changes;
- wars/diplomacy;
- economic consequences;
- discoveries;
- world events.

### Creator
- content validation;
- dependency completeness;
- coverage;
- migration readiness;
- accessibility/provenance completion.

## Re-entry after absence

A major competitive requirement should be **return without rereading everything**.

After a week, month or year, an authorized user should be able to request:
- what happened since I last played;
- where my Character is;
- what I was trying to accomplish;
- relationships that matter now;
- unresolved clues/promises;
- relevant rules/abilities I may have forgotten;
- what the GM needs to prepare next.

This should derive from structured history and notes, with AI summarization optional rather than required.

---

# Human Experience acceptance standard

Every major Stage A workflow should eventually answer:

1. **Autonomy:** What meaningful choice does the user control?
2. **Competence:** How does the system help them understand/master the task?
3. **Relatedness:** How does this connect to the table, Characters or shared world where relevant?
4. **Cognitive load:** What information is hidden until it is useful?
5. **Feedback:** What makes the result understandable?
6. **Safety/consent:** What sensitive boundary or authority could be crossed and how is it prevented?
7. **Progressive complexity:** How can beginner and expert use the same operation?
8. **Recovery:** What happens after mistake, interruption, ambiguity or absence?
9. **Meaning:** What campaign/Character/world history should persist?
10. **Anti-manipulation:** Is any interaction designed to increase app engagement rather than improve the tabletop activity? If yes, redesign it.

# Research basis

Research reviewed includes Self-Determination Theory/game engagement work on autonomy, competence and relatedness; flow meta-analysis emphasizing challenge-skill balance, clear goals and sense of control; 2024 gamification meta-analysis; systematic work on negative gamification effects; studies/reviews of TTRPG social connectedness, identity exploration, group dynamics, facilitation/psychological safety/cohesion/creativity, GM co-creation and computational support for GMs. Research findings are used as design evidence, not guarantees of individual psychological outcomes.
