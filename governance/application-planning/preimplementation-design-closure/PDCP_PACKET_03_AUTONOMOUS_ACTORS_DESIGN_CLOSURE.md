# PDCP Packet 03 — Autonomous Actors, Threats & Offscreen Action Design Closure

**Project:** PDCP — Preimplementation Design Closure Project  
**Packet:** PDCP-PACKET-03  
**Status:** DESIGN CLOSED  
**Date:** 2026-09-16  
**Implementation authority:** none  
**Roadmap-count mutation:** none

## 1. Purpose

Close the benchmark-derived design gap around autonomous NPC, faction, threat and world-process behavior without creating a second Character/NPC/Organization/Threat/Project/Action/Event ledger and without reopening completed ODL, SCL, MAS or other owner systems.

Packet 03 defines the reusable orchestration contract by which an owner-backed actor or process may evaluate an explicitly bounded goal context, actor-relative knowledge, available resources, authority and legal action set; select or propose a legal next operation; hand that operation to the canonical owner/runtime; expose authored telegraphs and interruption windows; and record deterministic provenance/replay evidence.

It is a coordination layer over existing owners. It is not an omniscient AI, world simulator, AutoGM, faction ledger, threat ledger, clock ledger, Project/time ledger or owner-state store.

## 2. Existing authority already sufficient

Packet 03 preserves and consumes the following completed or planned foundations rather than duplicating them.

### 2.1 ODL — organization authority

Completed ODL retains organization capacity, coordination, loyalty/cohesion/factionalism, delegation, roles, authority, communication, succession, resources, crisis/recovery, GM simulation-depth presentation and advisory-AI boundaries.

ODL-08 explicitly made AI advisory only and created no executable command or owner-mutation surface. Packet 03 does not weaken that boundary.

### 2.2 SCL — strategic command and order resolution

Completed SCL-03 owns strategic command relationships, roles, order intent and communication projections. Completed SCL-04 owns deterministic order coordination/classification and handoff into canonical Action/Combat/Event execution.

Packet 03 does not add a second strategic order resolver and does not grant an autonomous process permission to issue strategic orders it does not already have authority to issue.

### 2.3 MAS — prepared threats/clocks only

Completed MAS-08 owns prepared Threat, Clock, Pressure and Escalation authoring. MAS-08 explicitly does not create a scheduler, wall-clock timer, current-segment ledger, hidden trigger ledger or proof that a threat/clock progressed in live play.

Packet 03 may consume accepted MAS-authored threat/clock structures as preparation inputs where another runtime owner has lawful execution authority. It never reopens MAS and never turns prepared content into live truth by itself.

### 2.4 MNCS — actor construction and continuity

Future MNCS already plans persona/motive/goal/value/fear/contradiction; knowledge/belief/memory/suspicion; relationships/factions/reputation; profession/household/economy/schedule/project/life context; creature behavior; groups/populations; secrets; continuity/goals/events/change over time; resolution management; and runtime handoff.

Packet 03 specifies how those accepted actor facts can participate in bounded autonomous decision cycles without MNCS becoming a second live Action/Event authority.

### 2.5 Packet 01 — influence semantics

PDCP Packet 01 already closes command, delegated instruction, request, bargain, incentive, persuasion, social pressure, threat/coercion, deception and autonomous-choice distinctions.

Packet 03 consumes those semantics. Influence changes inputs, obligations, perceived options or willingness only through the appropriate owner contracts. It never becomes a magic override of autonomous actor choice.

### 2.6 Packet 02 — systemic evidence

PDCP Packet 02 already closes Event-to-trace emission, witness/record handoff, trace lifecycle and evidence-route semantics.

Packet 03 uses Packet 02 when autonomous actions leave observable evidence. It does not duplicate evidence truth or investigation state.

### 2.7 Canonical owner invariants

Character/NPC/Creature, Organization/Faction, World/Environment, Project/Time, Economy/Resource, Inventory/Asset, Relationship/Reputation, Knowledge/Visibility, Action/Event, Combat and other owner domains remain authoritative for their own state and mutations.

## 3. Benchmark capability interpretation

The useful benchmark lesson from Archmage Rises, Majesty, X4, Kenshi and Six Ages is not that Multiversal needs one universal NPC AI. The useful pattern is that actors and threats can continue to pursue bounded purposes when the Player is absent, while their actions remain constrained by what they know, possess, are allowed to do and can actually reach.

Packet 03 therefore adopts these capability goals:

1. actor-relative rather than omniscient decision context;
2. explicit legal action sets rather than unconstrained generation;
3. goals/agendas as inputs rather than a duplicate goal ledger;
4. deterministic or seed-governed selection where declared;
5. canonical owner operations for all consequential mutation;
6. explicit cadence tied to governed time/events rather than hidden wall-clock activity;
7. plan stages, telegraphs, interruption and recovery only when authored/configured;
8. offscreen execution that can remain abstract without fabricating unsupported detail;
9. deterministic replay/explanation receipts;
10. human/Player agency protected by explicit delegation requirements.

Protected benchmark code, formulas, assets, authored content, level design, UI expression and private protocols are not copied.

## 4. New reusable contracts closed by Packet 03

Packet 03 closes the following preimplementation contracts.

### 4.1 `AutonomyPolicyDefinition`

A reusable definition that controls whether and how a governed actor/process may autonomously evaluate next actions.

Required semantic fields:

- stable policy id and version;
- applicability selectors for owner domain / entity role / Campaign scope;
- actor/process owner reference requirements;
- explicit autonomy-enabled flag;
- permitted decision-trigger references;
- permitted action-set selector references;
- goal/agenda input selector references;
- knowledge-context selector references;
- resource/capability/authority constraint references;
- optional preference/priority rule references;
- selection-method declaration;
- deterministic seed policy where selection is stochastic;
- optional plan-template references;
- optional telegraph and interruption hooks;
- optional resolution-profile reference;
- failure/no-legal-action behavior;
- explanation/provenance visibility policy;
- optional human-delegation requirements.

There is no mandatory universal utility score, aggression score, personality score, strategic-value score or action priority scale.

### 4.2 `AutonomyDecisionTriggerDefinition`

A trigger declares when evaluation is allowed. Supported semantic trigger families are:

- explicit GM/owner tick;
- canonical time-window or schedule milestone;
- canonical Event occurrence;
- owner-state threshold/change;
- Project/plan milestone;
- newly perceived information;
- resource/capability availability change;
- communication/order receipt;
- interruption/counteraction;
- setting-specific governed trigger;
- custom governed trigger.

These are families, not a universal scheduler. APW/D26 Project/time and the relevant owner remain authoritative for time and scheduling.

No hidden wall-clock loop may mutate Campaign state merely because real time passed while nobody was playing.

### 4.3 `AutonomousDecisionContext`

A deterministic evaluation input assembled from current authorized owner projections.

It may contain references to:

- stable actor/process identity;
- current owner versions;
- applicable goals/agendas/motives;
- actor-relative known/believed facts;
- current resources/capabilities/inventory/position;
- current relationships/obligations/standing where authorized;
- current orders/authority/role constraints;
- applicable environmental/world conditions the actor can perceive or is entitled to know;
- applicable plan/project state;
- explicit legal candidate operation definitions;
- decision trigger and canonical time/event context;
- policy version and deterministic seed, if any.

It must not contain hidden Player/GM truth merely because the engine can access it. Information must be filtered into the actor's valid epistemic context before decision evaluation.

### 4.4 `LegalAutonomousOperationCandidate`

Each candidate is an attemptable owner-backed operation, not free-form prose.

Required semantics:

- candidate id;
- referenced governed Action/operation definition;
- intended target/scope references;
- preconditions and required owner versions;
- authority/permission requirements;
- resource/capability requirements;
- actor-relative knowledge prerequisites;
- expected handoff owner;
- optional estimated cost/risk/benefit annotations from explicit rules;
- optional plan-stage relationship;
- optional telegraph/interruption metadata;
- reason the candidate is eligible.

Candidates that fail legal, permission, knowledge, authority, resource or capability checks are excluded before selection. Hidden invalid candidates are not leaked through counts or explanations to unauthorized audiences.

### 4.5 `AutonomousSelectionPolicy`

Selection method is profile-defined. Permitted method classes include:

- deterministic ordered-rule selection;
- deterministic constraint/priority selection;
- weighted seeded selection;
- owner-domain resolver selection;
- GM choice from legal candidates;
- advisory-only recommendation;
- explicitly delegated human-agent policy;
- custom governed method.

A policy may choose no action. `wait`, `observe`, `seek information`, `request help`, `withdraw`, `escalate`, or any other behavior is available only if represented by a legal operation or owner-defined no-op semantics.

No language model is required for blocking behavior. Optional AI may propose/rank candidates only from authorized context and cannot bypass legal filtering or commit state.

### 4.6 `AutonomyEvaluationReceipt`

Every consequential autonomous evaluation produces an inspectable receipt appropriate to visibility.

Canonical audit fields include:

- evaluation id;
- actor/process owner reference;
- policy id/version;
- trigger reference;
- input owner versions;
- resolution-profile reference;
- candidate ids considered after authorization filtering;
- candidate exclusion reason codes in protected audit scope;
- selection method;
- deterministic seed where used;
- selected candidate or explicit no-action result;
- resulting handoff operation id;
- resulting Action/Event ids when committed;
- stale-input/revalidation outcome;
- plan-stage before/after references where applicable;
- telegraph/interruption receipts where applicable;
- provenance and timestamp in canonical time.

Player-facing explanation may be intentionally incomplete. Protected internal candidate counts, motives and hidden knowledge remain hidden.

### 4.7 `AutonomousPlanTemplateDefinition`

A plan template is optional. It does not create a universal fixed plan-stage vocabulary.

A template may define authored stage ids with:

- entry conditions;
- completion/exit conditions;
- permitted autonomous operations;
- required/reserved resources;
- dependency references;
- visible/hidden telegraph hooks;
- interruption windows;
- partial-disruption transitions;
- cancellation/abandonment rules;
- fallback/recovery transitions;
- escalation/de-escalation transitions;
- Project/clock references where separately owned;
- evidence/trace hooks;
- visibility rules.

Live plan/project state remains with the applicable Project/Time, Organization, Character/NPC, threat/runtime or other canonical owner. Packet 03 creates no generic plan-state ledger.

### 4.8 `AutonomousHandoffRequest`

A selected candidate becomes an owner-domain handoff request. The request is not proof that anything happened.

Required semantics:

- stable operation id;
- actor/process reference;
- target/scope references;
- selected action/operation definition;
- expected owner versions;
- authority and permission proof references;
- required resource/capability references;
- causal evaluation receipt;
- canonical owner endpoint/domain;
- optional plan-stage and trace hooks.

The canonical owner reauthorizes and revalidates at commit time. Stale versions, changed resources, revoked authority, moved targets or changed visibility invalidate/reclassify the request. No stale autonomous decision may blindly commit.

### 4.9 `AutonomousInterruptionReceipt`

When an authored plan/action exposes an interruption window, counterplay records:

- interrupted process/action/stage reference;
- interrupter/action/event reference;
- interruption rule/profile version;
- owner state versions;
- result classification;
- costs/resources consumed;
- resulting transition, if any;
- canonical owner Events;
- recovery/fallback availability;
- visibility/provenance.

Interruption does not universally cancel or reset progress. Result behavior is explicit in the governing profile/owner rules.

### 4.10 `OffscreenAutonomyBatchReceipt`

Offscreen advancement may batch evaluations only when the bound policy/runtime explicitly permits it.

The batch receipt records:

- canonical start/end time or event bounds;
- actor/process refs;
- policy/resolution-profile versions;
- deterministic seed stream where relevant;
- owner input versions/snapshots;
- evaluations/handoffs/events produced or aggregate summaries;
- skipped/blocked evaluations;
- refinement capability, if any;
- provenance.

Batching cannot invent individual actions merely to make the summary look plausible. If the owner/runtime only has aggregate authority, individual detail stays unresolved. Packet 06 will define broader aggregate ↔ individual refinement semantics.

## 5. Decision pipeline

The normative pipeline is:

`governed trigger → actor-relative context → legal candidate generation → authorization/resource/knowledge filtering → profile-defined selection → pre-commit owner revalidation → canonical owner handoff → Action/Event result → plan/project/owner updates → telegraph/evidence/consequence projections`

A failed stage does not silently skip to the next stage.

### 5.1 Actor-relative knowledge is mandatory

Autonomous evaluation uses what the actor/process legitimately knows, perceives, believes or is configured to access. The system may use GM truth only where the governing owner explicitly defines a non-character process that is entitled to that truth.

An NPC cannot target a hidden Character solely because the engine knows the Character's coordinates. A faction cannot respond to a secret alliance until an information path makes that fact available. An organization cannot spend a resource it does not own merely because the global Economy ledger contains it.

### 5.2 Legal-action filtering precedes ranking

No ranking model—rule based, weighted, solver-based or AI-assisted—may score illegal candidates into legality. Candidate legality, authority, permissions, resources, capability and epistemic prerequisites are hard filters.

### 5.3 Selection is not commitment

Selection creates an intent/handoff request. The canonical owner must revalidate current versions before committing. This prevents time-of-check/time-of-use errors and allows Player/GM counterplay or concurrent Events to invalidate a decision.

### 5.4 No-action is valid

An actor may have no legal operation that advances a goal. The correct result may be no action, delay, unresolved, or a separately authored information-seeking/help-seeking operation. The system must not invent capabilities to avoid inactivity.

## 6. Direct authority versus indirect influence

Packet 01 semantics are binding.

- `command` requires actual command authority;
- `delegated_instruction` requires valid delegation scope;
- `request` does not force compliance;
- `bargain` requires a governed exchange/obligation path;
- `incentive` changes decision context only through legitimate offered value;
- `persuasion` may change willingness/belief through owning social rules but is not mind control;
- `social_pressure` depends on applicable norms/audience/context;
- `threat_coercion` depends on perceived credibility and consequences;
- `deception` can change belief without changing truth;
- `autonomous_choice` remains the actor/process decision where no stronger authorized owner rule compels the outcome.

Autonomy policies consume resulting state. They do not re-resolve social interactions independently.

## 7. Human and Player agency boundary

A Player-controlled Character must never receive consequential autonomous action selection merely because an autonomy policy exists.

Autonomous control of a human-controlled entity requires explicit, scoped, revocable delegation stating at least:

- entity/role scope;
- permitted operation set;
- time/Event bounds;
- decision policy;
- resource limits;
- stop/escalation conditions;
- visibility/notification policy.

Revocation takes effect before the next autonomous commit and invalidates uncommitted handoff requests.

GM-controlled NPCs, creatures, organizations and threats may use configured autonomy under GM/Campaign policy, but GM authority and hidden-information rules remain unchanged.

## 8. Threat and clock relationship

A `Threat` is a prepared/adventure/runtime role, not a universal entity type that overrides owner identity. A threat may correspond to an NPC, organization, creature, hazard, Project, environmental process, military unit or other governed owner.

An authored MAS clock may be referenced by an autonomy policy, but Packet 03 does not own current clock progress. Progress occurs only through the runtime/owner operation that is already authorized to mutate the relevant state.

An autonomous threat may therefore:

1. evaluate a legal action;
2. hand that action to its owner/runtime;
3. produce canonical Events/outcomes;
4. cause an owner-authorized clock/project/threat-state mutation if applicable.

It may not directly increment a prepared MAS clock as hidden side state.

## 9. Telegraphing, observability and counterplay

Telegraphing is explicit content/runtime behavior, not an automatic fairness guarantee.

A plan/action may expose visible preparations, movement/deployment, resource acquisition, communications, rumors, environmental changes, economic activity, scouting/probing actions, public statements, ritual/technical setup, Packet-02 evidence traces or setting-specific clues.

High-impact actions with no authored precursor, interruption window, recovery route or discoverable consequence may trigger a **read-only authoring diagnostic** if the applicable content profile requests that warning. The diagnostic does not forbid surprise, hidden plans or unstoppable events where intentionally authored.

Counterplay must act through canonical operations. Merely discovering a plan does not cancel it.

## 10. Offscreen action and cadence

Autonomous processes advance only through governed triggers tied to canonical state/time/events.

### 10.1 No hidden real-time mutation

Closing the app for three real-world days does not itself advance a Campaign by three days. Any real-time-connected mode must be explicitly owned by a Campaign/time policy and produce ordinary canonical Events/receipts.

### 10.2 Catch-up

If canonical Campaign time advances across many due triggers, the runtime may evaluate each due trigger, batch them under a policy-declared deterministic aggregate method, defer them, request GM adjudication, or resolve them through an owner-domain bulk operation. The choice is profile-defined and receipt-backed.

### 10.3 Resolution depth

Packet 03 does not define a new universal simulation-depth taxonomy. It binds to an explicit owner/runtime `resolution_profile_ref`.

A lower-detail offscreen mode may summarize outcomes only if the relevant owner rules support that abstraction. It may not fabricate exact conversations, attacks, witnesses, item transfers or injuries when the aggregate resolver did not determine them.

Packet 06 will close the larger multi-resolution simulation/refinement contract.

## 11. Resources, commitments and concurrency

An autonomous process cannot spend, reserve, promise, transfer or consume owner resources merely by selecting an action.

Where planning requires reservations, the appropriate owner must create a governed reservation/commitment record. Selection receipts may reference that reservation but do not own it.

Multiple autonomous actors may race for the same resource/target. Pre-commit revalidation and expected-version/idempotent owner operations determine which requests remain legal. A losing request is blocked/recomputed; it is not silently force-applied.

## 12. Plan interruption, partial disruption and recovery

Plan templates may distinguish stage entry prevented, action interrupted before commit, action partially resolved, resource lost, target unavailable, communication/order broken, actor incapacitated/removed, objective already satisfied by another route, plan exposed, plan abandoned, fallback triggered, or escalation/de-escalation triggered.

The transition after disruption is authored/profile-governed. No universal rule says interruption resets a clock, consumes all resources, forces escalation or ends the threat.

## 13. Autonomous organizations and factions

ODL remains organization-life authority and SCL remains strategic command authority.

Packet 03 may orchestrate an organization/faction decision only from owner-approved projections such as goals/directives, authority structure, available resources, communication state, known world information, relationships/standing, Projects/commitments, legal organizational operations and strategic orders where SCL authority applies.

The autonomy layer cannot bypass internal politics, command hierarchy, communication delay, resource shortage, morale/cohesion or permission rules. A faction is not omniscient merely because its organization record exists.

## 14. Autonomous NPCs and creatures

MNCS may author/generate accepted motives, goals, values, fears, knowledge, routines, tactics, ecology and social structure. Packet 03 defines how future runtime evaluation can consume those facts.

Behavior remains constrained by current live state. A generated personality trait does not grant an unavailable Action. A creature instinct does not override a Condition that prevents movement. A schedule does not teleport an NPC through an inaccessible route.

Creature/ecology population-scale behavior may use aggregate owner rules; Packet 03 does not require per-individual simulation.

## 15. Autonomous world processes

Some governed processes are not sentient actors: hazards, spreading fires, storms, diseases, magical phenomena, economic mechanisms, construction Projects or setting-specific threats.

They may use the same trigger/legal-operation/handoff/receipt pattern if their owner exposes a deterministic process policy. They do not receive Character motives, beliefs or social-choice semantics unless the owner explicitly models those features.

This keeps the orchestration contract reusable without anthropomorphizing every world process.

## 16. Determinism, replay and recovery

Where a policy declares deterministic behavior, the same authoritative input versions, policy version, trigger and seed must reproduce the same legal candidate set and selection receipt.

Replay stores/refers to policy version, trigger, canonical input versions, actor-relative context identifiers, selection method, seed stream where applicable, candidate ids after filtering, selected/no-action result, handoff id and resulting Event ids.

If a policy changes later, historical receipts retain the old policy version. Replaying history does not silently reinterpret old decisions through current rules.

Ambiguous owner commit outcomes use ordinary operation-status/current-version recovery rather than blind retry.

## 17. Explainability and role-safe projections

Creator/GM diagnostic views may explain which policy fired, which trigger fired, which visible goals/constraints applied, which candidate was selected, visible reasons an action was blocked, resulting Events and plan-stage transitions, whether the evaluation was batched or detailed, and policy version/seed.

Protected motives, secrets, undiscovered relationships, hidden candidate actions, concealed resources and exact hidden plan stages remain filtered before counts/search/AI/export/diagnostics for unauthorized audiences.

A Player may see consequences without receiving the hidden reasoning that produced them.

## 18. Optional AI boundary

AI may summarize authorized actor/process state, propose candidates before ordinary hard filtering, rank already legal candidates when a policy explicitly uses advisory AI, explain a receipt from role-safe fields, or suggest missing plan transitions/authoring warnings.

AI may not see protected truth unavailable to the actor merely to improve its decision, invent owner capabilities/resources, bypass hard legal filters, issue commands without authority, commit Action/Event/world state, decide for Player-controlled Characters without explicit delegation, silently alter autonomy policies, fabricate offscreen detail, or serve as a required paid/cloud dependency for blocking behavior.

## 19. Authoring/diagnostic requirements

Future creator tooling should support policy inspector, trigger inspector, legal-action-set preview, actor-relative knowledge preview, resource/authority constraint preview, plan-stage graph/list view, telegraph/interruption coverage view, dry-run decision evaluation, seeded replay, role-safe explanation, stale-version/concurrency diagnostics, no-legal-action diagnostics, hidden-information leakage diagnostics, Packet-02 trace/evidence fan-out inspection and owner-handoff verification.

Graphical plan views are projections. Ordered semantic/nonvisual representations must expose equivalent meaning and operations.

## 20. Failure and edge-case semantics

- **No legal action:** explicit no-action/blocked receipt; do not invent an operation.
- **Goal conflict:** use explicit owner/policy rules; otherwise return unresolved/GM-required.
- **Unknown target:** cannot target hidden entity unless operation targets an area/search process rather than the hidden entity.
- **Resource lost after selection:** pre-commit revalidation blocks/falls back; no negative-resource commit.
- **Authority revoked after selection:** uncommitted request fails reauthorization; committed Events remain history.
- **Communication interrupted:** ODL/SCL communication semantics govern; no phantom receipt.
- **Actor removed/incapacitated:** future actions invalidate unless explicit succession/delegation permits transfer.
- **Duplicate trigger:** stable trigger/evaluation ids and idempotency prevent double commit.
- **Cyclic reactions:** receipt linkage supports future MSWI-17 loop detection; no hidden unbounded recursion.
- **Simultaneous actors:** ordering comes from owner/runtime policy, never arbitrary UI iteration order.

## 21. Implementation allocation to existing future families

Packet 03 creates **no new family and no standalone implementation tranche**.

### MNCS residual implementation

- `MNCS-06` — accepted motive/goal/value/fear/contradiction inputs;
- `MNCS-07` — actor-relative knowledge/belief/memory context;
- `MNCS-09` — schedule/Project/life-context trigger bindings;
- `MNCS-13` — creature behavior/instinct/tactics action-set authoring;
- `MNCS-15` — group/social actor bindings;
- `MNCS-20` — goals/Events/change-over-time continuity;
- `MNCS-21` — resolution-management hooks;
- `MNCS-22` — runtime handoff;
- `MNCS-24` — golden autonomy/continuity proof contribution.

### MRCS residual implementation

- `MRCS-04` — bounded predicates/selectors;
- `MRCS-05` — Action/Effect/Trigger and legal-operation bindings;
- `MRCS-08` — faction/social-package bindings;
- `MRCS-12` — NPC/creature behavior package authoring;
- `MRCS-14` — hazard/environment process policies;
- `MRCS-16` — scoped overrides/compatibility;
- `MRCS-17` — dependency/impact analysis;
- `MRCS-18` — dry-run/simulation evidence;
- `MRCS-20` — versioning/provenance/publication;
- `MRCS-21` — cross-domain proof.

### GPR residual implementation

- `GPR-05` — objective/world-route runtime bindings;
- `GPR-06` — party/strategy/social/stealth execution hooks;
- `GPR-07` — deterministic non-AI autonomous selection plus optional AI/Encounter integration;
- `GPR-08` — data-driven bounded autonomous process composition;
- `GPR-09` — delivery-mode autonomy policy differences;
- `GPR-12` — deterministic replay/Event trace/multiplayer authority;
- `GPR-13` — persistence/version recovery;
- `GPR-14` — GM dry-run/control UX;
- `GPR-16` — golden runtime proof.

### MSWI residual implementation

- `MSWI-03` — consequence routing from autonomous owner Events;
- `MSWI-09` — organization/doctrine/obligation consequences;
- `MSWI-10` — profession/enterprise/downtime autonomous adapters;
- `MSWI-13` — world Project/faction-opposition autonomous contributions;
- `MSWI-17` — interaction/reaction-loop/missing-route diagnostics;
- `MSWI-18` — golden systemic proof.

Completed/existing owners consumed rather than reopened: ODL, SCL, PPIA-02/Character/NPC/Creature, MIB-09, APW/D26 Project/time, Action/Event/Combat, Visibility/Permission/Knowledge, World/Environment/Economy/Inventory/Resource, PDCP Packets 01–02, and completed MAS as prepared-content input only.

MCS, MCCS, MSAS, MERA, MBES and MSLR receive no direct new Packet-03 implementation obligation.

## 22. Golden validation vectors

Future implementation must automate at least these 32 cases:

1. `PDCP-AUT-001` unknown hidden target is not targetable.
2. `PDCP-AUT-002` explicit search-area action is legal without omniscient target knowledge.
3. `PDCP-AUT-003` unavailable resource filters a candidate before ranking.
4. `PDCP-AUT-004` invalid command authority blocks strategic command.
5. `PDCP-AUT-005` interrupted communication does not become received truth.
6. `PDCP-AUT-006` deterministic ordered selection reproduces.
7. `PDCP-AUT-007` weighted seeded selection reproduces.
8. `PDCP-AUT-008` historical replay binds old policy version.
9. `PDCP-AUT-009` no legal action emits explicit blocked/no-action receipt.
10. `PDCP-AUT-010` moved target causes pre-commit revalidation failure/recompute.
11. `PDCP-AUT-011` two actors racing for one resource cannot both commit it.
12. `PDCP-AUT-012` revoked Player delegation blocks uncommitted autonomous Character action.
13. `PDCP-AUT-013` Player Character has no consequential autonomy by default.
14. `PDCP-AUT-014` configured GM NPC may execute through owner handoff.
15. `PDCP-AUT-015` MAS threat/clock data does not self-progress.
16. `PDCP-AUT-016` explicit interruption transition fires with attributable Events.
17. `PDCP-AUT-017` partial disruption need not reset the plan.
18. `PDCP-AUT-018` incapacitated actor blocks later stages absent valid succession.
19. `PDCP-AUT-019` organization owner constraints can block faction action.
20. `PDCP-AUT-020` Packet-01 request does not force compliance.
21. `PDCP-AUT-021` coercion affects context only through governed social state.
22. `PDCP-AUT-022` actor may act on false belief without changing objective truth.
23. `PDCP-AUT-023` authored telegraph emits owner Events/Packet-02 hooks.
24. `PDCP-AUT-024` hidden plan does not cause invented clues when no telegraph is authored.
25. `PDCP-AUT-025` autonomous committed action may generate Packet-02 evidence through ordinary rules.
26. `PDCP-AUT-026` offscreen catch-up follows canonical Campaign time, not real elapsed time.
27. `PDCP-AUT-027` aggregate batch does not fabricate exact individual detail.
28. `PDCP-AUT-028` duplicate trigger delivery does not double-commit.
29. `PDCP-AUT-029` Player diagnostics do not reveal hidden motives/candidate counts.
30. `PDCP-AUT-030` AI-proposed illegal action is discarded and cannot commit.
31. `PDCP-AUT-031` non-sentient hazard process uses trigger/legal-operation/handoff without fake Character psychology.
32. `PDCP-AUT-032` linked autonomous reactions remain traceable for MSWI loop diagnostics without inventing a fix.

## 23. Accessibility requirements

Autonomy/plan/decision tooling must provide semantic nonvisual equivalents for every graph/canvas surface. Users must be able to inspect actor/process, current stage, trigger, legal action set, selected/no-action result, constraints, causal Events and replay via ordered lists/tables/text.

Color, animation, graph position, hover state and audio cues cannot be the sole carrier of plan stage, danger, candidate legality, telegraphing or interruption opportunity.

Time-sensitive live intervention must expose accessible textual/semantic notification equivalents and configurable pacing where the gameplay mode permits.

## 24. Security, privacy and hidden-information requirements

Permission/visibility filtering occurs before actor-relative context assembly, candidate generation from protected records, candidate counts, ranking/scoring, explanations, diagnostics, AI context, export, realtime payloads and notifications.

The autonomy engine may need protected GM audit evidence internally, but unauthorized projections cannot infer hidden existence/cardinality from omitted candidates or changed ranking.

## 25. Provenance and recovery requirements

All definitions are versioned. Consequential evaluations/handoffs use stable ids and ordinary idempotency/expected-version rules.

Receipts link:

`trigger → policy/version → owner input versions → legal candidates → selection/no-action → handoff → canonical Events → owner consequences → Packet-02 traces where applicable`

Compensation/reversal occurs through owner-domain compensating Events. Historical decisions are not rewritten or deleted merely because a later policy changed.

## 26. Explicit non-goals

Packet 03 does not define one universal utility/AI model, universal NPC personality/aggression scores, a universal faction planner, a new threat/clock ledger, a new goal/motive ledger, a new scheduler/wall-clock simulation loop, hidden real-time Campaign progression, universal plan stages, universal fair-warning requirements, guaranteed Player counterplay for every Event, universal offscreen-detail levels, aggregate↔individual refinement beyond honest receipt boundaries, autonomous Player Character control without explicit delegation, AI command/GM/canonical mutation authority, or a paid/cloud dependency.

## 27. Roadmap reduction implication

Packet 03 requires **zero new roadmap tranches**.

Its design/research obligations are closed here and should not later reappear as standalone discovery/architecture tranches. Future family-reduction passes may merge or shorten existing MNCS/MRCS/GPR/MSWI tranches because their autonomy semantics are now implementation-ready, but no tranche count changes are made by Packet 03 itself.

Any eventual reduction receipt must preserve all implementation, integration, persistence, replay, permission, accessibility, provenance and golden-proof obligations identified here.

## 28. Closure decision

PDCP Packet 03 is **DESIGN CLOSED**.

No owner decision remains. No new family is required. No new standalone tranche is required. MAS remains outside PDCP and is not reopened.

The next open benchmark-derived packet is **PDCP Packet 04 — Semantic Affordances & Composable Effects**.
