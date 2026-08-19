# APM-04 — AutoGM Mini-Campaign Director

**Work item:** APM-04  
**Program:** APM — Automated Play Modes  
**Version:** 0.1.0  
**Status:** DESIGN CONTRACT — READY FOR GOVERNED REVIEW  
**Owner and final authority:** John Brandon Turner  
**Date:** 2026-08-19

## 1. Decision

APM-04 extends the verified APM-03 single-encounter model across a **bounded short multi-scene Adventure graph**. It is a director for a finite governed scenario package, not an unlimited autonomous Campaign generator and not a second game engine.

The controlling loop is:

`Start Mini-Campaign → Evaluate Current Node/Committed State → Present Player-Safe Situation → Human Choice or Bounded Automatic Transition → Run Scene / APM-03 Child Encounter → Commit Owning-Domain Effects → Update Route/Open-State Evidence → Repeat → Explicit Endpoint / Abort / Fail-Safe`

Mechanics, authoritative state transitions, permissions, hidden-information filtering and persistence remain owned by their existing domains. Optional AI may narrate, converse, summarize or offer candidate phrasing from player-safe resolved projections. It never owns route legality, mechanical resolution, unrevealed truth or completion authority.

## 2. Bounded MiniCampaignPackage

A `MiniCampaignPackage` is an exact-version scenario authority package derived from a governed Adventure definition or an explicitly incorporated CSW-05 plan. CSW planning material is not executable merely because it exists.

Required package content includes:

- package ID/version and compatibility manifest;
- source Adventure/version and authoring/incorporation provenance;
- bounded graph node/edge IDs and exact versions;
- entry nodes and explicit allowed endpoints;
- node kinds and scene/encounter package references;
- route prerequisites and eligibility predicates;
- optional-content, convergence/divergence and failure-route semantics;
- machine-private hidden scenario state required for deterministic progression;
- revelation/open-state rules and player-visible projection rules;
- exact controller operation families allowed outside child encounters;
- APM-03 encounter package IDs/versions allowed for encounter nodes;
- deterministic route-policy and seed/entropy requirements;
- reward/result/end-state rules;
- maximum scene count, route-transition count, child-run count, Event/step budget and any other hard package bounds;
- undefined/out-of-scope fail-safe behavior;
- optional AI presentation policy;
- package provenance and compatibility evidence.

The package must be finite and inspectable. No runtime AI call may append new authoritative nodes/edges to escape package bounds.

## 3. Parent run state

Conceptual `AutoGMMiniCampaignRun` fields:

- parent `automationRunId`;
- controller/profile/delegation IDs and versions;
- initiating subject and Context;
- MiniCampaignPackage ID/version;
- starting and current authoritative Event sequence;
- current graph node/scene ID and version;
- visited/completed/skipped/failed node receipts;
- committed route-choice receipts;
- current eligible route-set version;
- parent deterministic seed/entropy stream and per-child derivation evidence;
- child APM-03 run references/statuses;
- package-owned revelation/open-state reference;
- player-visible revealed-state projection version;
- pending human route/scene choice;
- CSW-06 continuity/open-thread advisory references where configured;
- active resource/Character/world reference versions required by route predicates;
- run budget counters;
- pause/recovery state;
- endpoint/end-reason;
- summary/reward/provenance receipts.

Parent lifecycle:

`draft → validating → ready → running → awaiting-player-choice → running-scene → awaiting-child-result → between-scenes → paused/recovery-required → ending → completed | abandoned | failed | failed-safe`

## 4. Package creation boundary

A CSW-05 Lab plan becomes eligible input only after explicit governed Adventure incorporation/proposal/review creates or updates an owning-domain Adventure definition. The AutoGM package builder then validates that governed source against APM requirements.

Therefore:

- a CSW node is not directly executable;
- a CSW relationship is not automatically an AutoGM edge;
- a continuity suggestion does not rewrite the package;
- optional AI output cannot become a package node without the normal creator/Adventure governance path;
- package generation records exact Adventure/source versions and compatibility evidence.

This preserves the authoring → governed Adventure → executable scenario boundary.

## 5. Route eligibility

At every route decision, the director computes an eligible set from **committed current state** using the exact package/version and route-policy version.

Inputs may include:

- current node completion/end receipt;
- authoritative Character/resources/conditions;
- committed investigation/relationship/world/Campaign state permitted by the package;
- package-owned revelation flags and bounded hidden scenario state;
- prior committed player choices;
- completed/failed/skipped node receipts;
- explicit prerequisite predicates;
- package seed/entropy stream when a route policy uses governed randomness.

Route eligibility may never rely on uncommitted narration, AI inference or a stale client projection.

If a prerequisite changes because an owning-domain Event was committed, eligibility is recomputed before transition.

## 6. Player route choice and anti-railroading

When two or more **meaningfully distinct player-facing eligible routes** are available, route selection is human-required unless the package explicitly models the transition as non-choice/automatic.

The director may:

- explain currently visible options;
- show known consequences where the package allows them;
- summarize the recent context;
- allow retreat/backtrack when a legal route exists;
- accept a freeform player intention and map it only to an actually eligible governed option after validation.

It may not:

- invent an edge absent from the package;
- reveal a hidden branch before its reveal conditions;
- silently select among meaningful player choices merely for pacing;
- pretend a blocked route is available;
- fabricate a mechanical prerequisite to force the intended story;
- treat an AI-suggested branch as executable.

A deliberately linear package is allowed. The contract requires truthful route representation, not mandatory branching.

## 7. Node execution

Each package node has an exact execution class.

### 7.1 Encounter node

An encounter node launches an **APM-03 child run** with:

- parent run/node/correlation identity;
- exact allowed encounter package/version;
- current committed Character/world/resource inputs;
- derived or allocated deterministic seed stream evidence;
- parent delegation constrained by the child package;
- expected parent Event/version boundary.

The child remains governed by APM-03. Its completion/abort/fail-safe receipt is incorporated into the parent exactly once.

### 7.2 Choice/presentation node

May present player-safe context and wait for explicit human choice. It creates no mechanical mutation merely by being viewed.

### 7.3 Bounded transition/event node

May invoke only package-declared owning-domain commands classified `automatic_permitted` or `automatic_with_bounds`. Every command receives fresh authorization and expected-version validation.

### 7.4 Proposal/human-required node

Stops at the relevant proposal or human decision boundary. The director does not impersonate the missing decision-maker.

### 7.5 Unsupported/undefined node

Enters safe pause/fail-safe rather than improvising a new authoritative behavior.

## 8. Parent/child exactly-once semantics

An APM-03 child run has its own run identity and Event history. Parent advancement depends on an exact child terminal receipt.

Rules:

1. starting a child stores a durable parent→child correlation before the child may affect parent progression;
2. retry/status recovery resolves the existing child before creating another;
3. the same child completion receipt can advance the parent at most once;
4. duplicate delivery returns the already-recorded parent transition status;
5. aborted/failed-safe child results follow package-defined failure/retreat/recovery routes rather than being coerced into success;
6. parent summaries reference child history instead of duplicating its mechanical Event source of truth.

## 9. Between-scene state

After each node/child run, the director re-reads committed owning-domain state. Character health/resources, inventory, relationship/investigation state, World/Campaign effects and other route inputs carry forward only through their authoritative domains.

The parent run may retain package-local orchestration state such as:

- visited-node receipts;
- selected routes;
- package-specific revealed/unrevealed flags;
- bounded scenario counters;
- package-local unresolved objectives.

It does not create a parallel Character, inventory, relationship, investigation or World state engine.

## 10. Revelations, secrets and hidden information

The package may know unrevealed routes, NPC motives, encounter tactics, secrets and future revelations. The protection pipeline is:

`machine-private package state → deterministic eligibility/resolution → player-safe revealed projection → optional AI presentation projection`

Player-visible route lists, summaries, accessibility text, notifications, logs and AI prompts must not leak hidden-node existence or cardinality before permitted.

A revealed fact becomes player-visible only through the package/owning-domain rule that governs its reveal. AI fluency cannot reveal it early.

## 11. Open threads and CSW-06 integration

APM-04 consumes CSW-06 in two deliberately separated ways.

### Creator-side advisory continuity

Package authors/reviewers may use CSW-06 ContinuityCandidates/OpenThreads before or after a run to notice missing setups/payoffs, fragile clue coverage, unresolved branches or inconsistencies. These remain advisory creator evidence.

### Runtime package open state

The running package maintains its own finite machine-readable objectives/revelation/branch state required for route progression.

A CSW-06 candidate cannot mutate runtime package state. The director cannot “fix” a detected continuity issue mid-run by creating a new scene, retconning a fact or altering a route. If a material package defect makes safe progression impossible, the run pauses/fails safe and preserves evidence for author review.

## 12. Continuity across scenes

At each transition the director verifies:

- current node terminal receipt;
- exact Event sequence/version;
- relevant Character/resource/world/investigation/relationship projections;
- route prerequisite evidence;
- package-local reveal/objective state;
- child-run receipt consistency;
- current permission/delegation/entitlement state;
- package/rules compatibility;
- run budget remaining.

This prevents narration from becoming state and prevents stale scenes from selecting later routes.

## 13. Deterministic route/mechanical replay

The determinism claim is bounded to package-declared deterministic behavior.

For fixed:

- starting authoritative state/versions;
- MiniCampaignPackage/route-policy versions;
- controller/delegation/rules/pack/schema versions;
- ordered human route choices;
- ordered child APM-03 player Actions;
- parent and child seed/entropy streams;
- deterministic domain inputs;

the same route eligibility/selected automatic transitions and owning-domain mechanical Event results must reproduce where the package promises deterministic selection.

Human choices are inputs, not predicted outputs. Narration/dialogue/UI wording are excluded from replay identity.

If an eligible set is intentionally randomized, the exact seed/stream position is part of replay evidence.

## 14. Run bounds and no endless generation

Every package declares hard limits. At minimum:

- maximum scene/node transitions;
- maximum child encounters;
- maximum automatic steps/Events;
- explicit endpoints or fail-safe bound behavior.

Optional provider/token/cost bounds follow existing AI policy and do not replace mechanical bounds.

When a hard bound is reached without a legal endpoint, the run enters a package-defined open ending or `failed-safe`. It does not synthesize more authoritative story indefinitely.

## 15. End states

A bounded run can terminate as:

- `completed-success` — package-valid success endpoint;
- `completed-failure` — package-valid failure endpoint;
- `completed-open` — explicit package endpoint intentionally leaving threads unresolved;
- `retreated` — legal retreat/escape endpoint;
- `abandoned` — player explicitly ends the run before a package endpoint;
- `failed-safe` — undefined/out-of-scope/version/authority condition prevents safe continuation.

All committed owning-domain Events remain valid according to their domains. End-state labeling cannot roll them back or invent rewards.

Open/unresolved thread summary is presentation/project evidence, not a promise that APM will autonomously continue later.

## 16. Rewards and post-run results

The package may define endpoint rewards/results, but each mutation remains owning-domain governed. Parent/child rewards are reconciled so the same result cannot be granted twice.

The director may produce:

- final mechanical/history summary;
- completed/failed objectives;
- discovered/revealed player-safe facts;
- unresolved player-safe threads;
- reward receipts;
- advancement eligibility/proposals;
- creator-facing run provenance where authorized.

Irreversible Character choices remain human-required.

## 17. Pause, disconnect and recovery

Initial APM-04 remains **foreground-only**. Disconnect or app exit creates a safe pause/recovery boundary rather than background story progression.

Persist:

- parent package/controller/delegation versions;
- current node and route-set version;
- last authoritative Event sequence;
- parent seed stream position;
- visited/completed/skipped/failed nodes;
- route-choice receipts;
- package-local hidden/revealed state versions;
- pending human choice;
- active/latest child APM-03 run ID/status;
- exactly-once parent/child completion receipt IDs;
- budget counters;
- player-visible projection version.

Resume reauthorizes identity/context/delegation and validates package/rules compatibility. If a child may have completed while the client lost confirmation, status is resolved before any new child or transition is created.

Package/graph/version drift that cannot be proven compatible pauses for explicit recovery/abort; no silent reinterpretation occurs.

## 18. Optional AI presentation

Optional AI may:

- narrate committed scene/encounter outcomes;
- render dialogue from player-safe resolved state;
- summarize prior revealed events;
- phrase currently eligible player-visible choices;
- explain rules/results using authorized evidence;
- create nonauthoritative flavor suggestions outside live mutation.

It may not:

- compute route eligibility;
- select a human-required branch;
- invent a new executable node/edge;
- see unrevealed package-private truth without an explicitly safe task projection;
- resolve mechanics;
- mark continuity findings as truth;
- decide package completion;
- award resources/advancement;
- rewrite the package during the run.

If AI is unavailable, deterministic templates/manual presentation support the complete run.

## 19. Accessibility and player control

The director must expose route/scene state without requiring a visual graph. Player-facing navigation includes semantic headings, clear current objective/context, named choices, consequence knowledge only where allowed, progress stated without hidden-cardinality leaks, and keyboard/screen-reader/mobile parity.

“Progress” must not reveal that hidden scenes remain. Prefer known objectives/visited history over “3 of 7 scenes” when the total itself is secret.

Pause, save/exit, review revealed history and abort are always discoverable controls.

## 20. Acceptance contract

APM-04 is design-complete when it defines:

- finite MiniCampaignPackage identity/version/bounds;
- parent run graph/node/route/open-state bookkeeping;
- governed Adventure/package creation boundary from CSW-05;
- committed-state route eligibility and human route-choice rules;
- APM-03 child encounter composition with exactly-once parent advancement;
- bounded non-encounter node operation classes;
- hidden/revealed projection separation;
- CSW-06 advisory continuity integration without runtime rewriting;
- cross-scene authoritative state carry-forward;
- deterministic route/mechanical replay inputs;
- explicit success/failure/open/retreat/abandon/fail-safe endings;
- endpoint reward reconciliation;
- foreground pause/recovery/version-drift behavior;
- optional AI presentation-only boundary and no-AI path;
- accessible player-facing route/control semantics.

No application implementation, migration, unlimited autonomous Campaign generation, AI GM/mechanical/canonical authority, release/deployment, canonical promotion or CCTI-12-T04 work is authorized.