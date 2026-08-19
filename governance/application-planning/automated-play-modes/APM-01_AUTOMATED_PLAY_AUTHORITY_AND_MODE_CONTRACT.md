# APM-01 — Automated-Play Authority and Mode Contract

**Work item:** APM-01  
**Program:** APM — Automated Play Modes  
**Version:** 0.1.0  
**Status:** DESIGN CONTRACT — READY FOR GOVERNED REVIEW  
**Owner and final authority:** John Brandon Turner  
**Date:** 2026-08-18

## 1. Decision

Automated play is a governed way of operating ordinary Multiversal state. It is **not** a second rules engine, a second Campaign type, a permanent account role, a global Game Master role, or an authority shortcut.

APM-01 defines a nonhuman automation controller that may perform only explicitly delegated operations inside one Personal, Campaign, or Session context. The controller is always subordinate to the initiating human authority, the selected automated-play profile, the owning domain, current permissions, current state, and explicit delegation limits.

`AutoGM` therefore means **bounded automated orchestration**, not “AI becomes the GM.” `CozyMode` means a low-pressure automated-play experience, not a genre and not a new state engine. Optional AI may help present, narrate, converse, summarize, transform, or propose, but deterministic/domain-owned systems remain responsible for legality and authoritative mutation.

This contract consumes APW-01 as controlling account/context authority and preserves completed Identity, Campaign, Session, Action/proposal, Event, permission, recovery, hidden-information, provenance, and optional-AI architecture.

## 2. Terminology and orthogonal dimensions

Automated play must not collapse the following dimensions into one mode flag.

### 2.1 Context

From APW-01:

- **Personal** — independent user-owned workspace and governed personal resources.
- **Campaign** — one governed collaborative Campaign scope.
- **Session / active encounter** — one Campaign-subordinate live or resumable Session/encounter scope.

### 2.2 Cadence

From APW-01:

- **Live**
- **Asynchronous**
- **Hybrid**

### 2.3 Connectivity

From APW-01:

- **Connected**
- **Temporarily offline/cached**
- **Recovering/reconnecting**

Offline status never expands automated-play authority. No APM mode creates broad offline authoritative mutation.

### 2.4 Participation topology

- **Solo** — one human participant is the active player/user for the automated-play experience. Solo is a participation topology, not an authority role.
- **Connected / invited participants** — multiple known participants share an authorized scope. Initial APM uses invited/known participants only; public stranger matchmaking is outside scope.

### 2.5 Automated-play experience/profile

- **AutoGM** — bounded controller-led orchestration of an AutoGM-enabled scenario/encounter/adventure profile. The controller can perform only the scenario, domain, and operation classes explicitly delegated to it.
- **CozyMode** — bounded low-pressure automation centered on downtime, projects, relationships, crafting, research, journaling, light exploration, personal/campaign progression, and similar owning-domain activities.
- **Connected Cozy** — CozyMode using invited authorized participants and shared governed resources. It is Cozy plus connected participation, not a separate authority model.

A subject may therefore be, for example: Personal context + CozyMode + Solo + Connected connectivity; or Campaign context + AutoGM + Live cadence + Solo; or Campaign context + CozyMode + Asynchronous cadence + invited participants.

## 3. Controller identity model

An automation controller is a **nonhuman service actor**, never a human account role.

Each execution uses stable identities:

- `automationControllerId` — stable registered controller implementation/profile identity;
- `automationRunId` — one bounded execution/run instance;
- `initiatingSubjectId` — the human subject who started or requested the run;
- `contextKind` — Personal, Campaign, or Session;
- `contextId` — stable resource scope where applicable;
- `modeProfileId` and version;
- `delegationGrantId` and version;
- optional scenario/activity package IDs and exact versions;
- policy, rules, pack, schema, permission, entitlement, and visibility versions;
- correlation/provenance identifiers.

The controller does not acquire `Player`, `Game Master`, `Campaign Owner`, `Assistant GM`, `Owner/Admin`, or creator status. If a bounded operation resembles something a human GM normally performs, the operation remains authorized by the controller’s explicit capability grant and owning-domain policy rather than by assigning the controller a GM role.

## 4. Automation delegation grant

Every state-affecting automated run requires an explicit `AutomationDelegationGrant` or equivalent governed record. The grant contains at minimum:

- grant ID/version;
- granting subject and the authority evidence that permits the grant;
- controller ID/profile and mode profile;
- exact Context and resource scope;
- allowed capability/operation classes;
- prohibited capability/operation classes;
- allowed object families and selectors where needed;
- scenario/activity package and version boundaries where applicable;
- allowed automatic-resolution classes;
- mandatory human-choice classes;
- maximum run duration, step/event budget, and any bounded background window;
- optional resource/cost limits;
- hidden-information projection policy;
- AI-assistance policy and provider/cost class when enabled;
- created, effective, expiry, paused, stopped, and revoked metadata;
- policy/permission/entitlement versions;
- audit/provenance references.

### Delegation invariants

1. A subject can delegate only authority the subject or owning domain is permitted to delegate.
2. A Player cannot delegate GM-only Campaign authority merely by starting AutoGM.
3. A Campaign owner/GM cannot delegate authority over another user’s Personal resources.
4. A controller cannot widen, renew, copy, transfer, or regrant its own delegation.
5. Tool availability, model capability, scenario content, or a mode flag cannot widen the grant.
6. Revocation, expiry, permission change, entitlement change, lifecycle change, policy change, or context invalidation may narrow or terminate effective authority immediately.
7. Every authoritative command is reauthorized at execution time; the grant is necessary but not sufficient evidence.

## 5. AutoGM scenario authority package

AutoGM may need bounded access to scenario truth that is intentionally hidden from the human player. This is handled by a **scenario authority package**, not by giving an AI or controller unrestricted GM access.

An AutoGM-enabled package may contain:

- exact scenario/adventure/encounter definition and version;
- machine-private hidden state required for deterministic scenario progression;
- allowed controller operations and owning domains;
- player-visible projection rules;
- deterministic choice/branch rules;
- NPC/world response policies;
- seed/entropy requirements;
- start/end conditions;
- fail-safe behavior for undefined situations;
- provenance and compatibility requirements.

The deterministic automation controller may receive only the package fields needed for permitted orchestration. Optional AI does **not** automatically receive raw scenario-private truth. AI context remains subject to the existing authorized/redacted AI projection contract and receives only presentation inputs explicitly produced for the AI task.

This separation allows hidden AutoGM scenario state without redefining AI as a privileged GM actor.

## 6. Responsibility partition

### 6.1 Deterministic / owning-domain responsibility

The following remain owned by deterministic or domain-governed systems:

- authorization and hidden-information filtering;
- entitlement and pack/schema compatibility;
- Action legality, costs, requirements, targets, rolls/seeds, modifier order, Effects, and mechanical resolution;
- Character, inventory, crafting, vehicle, relationship, project, research, travel, encounter, world, and other domain state transitions;
- Event acceptance, ordering, idempotency, expected-version checks, and authoritative persistence;
- scenario branch eligibility and required state prerequisites;
- automatic timer/progress ticks where the owning domain explicitly permits them;
- reward/resource mutation;
- proposal/approval requirements;
- run lifecycle, delegation, revocation, expiry, and audit evidence;
- canonical promotion, publication, release, deployment, spending, and owner-reserved gates.

### 6.2 Automation-controller responsibility

Within an explicit grant, the controller may:

- choose the next permitted scenario/activity operation from a deterministic eligible set;
- invoke owning-domain commands using exact current state and expected versions;
- schedule or advance bounded timers/progress where authorized;
- control scenario-owned NPC/world response operations within the package;
- select deterministic/randomized opportunities using governed seed/entropy evidence;
- pause at mandatory player-choice points;
- request clarification when no authorized operation safely applies;
- produce role-safe state summaries from authorized projections;
- maintain run bookkeeping and provenance.

### 6.3 Optional-AI responsibility

Optional AI may, when separately enabled and permission/cost safe:

- narrate an already-determined result;
- render NPC dialogue or descriptive presentation from a filtered prompt projection;
- summarize authorized history or current state;
- propose flavor, names, hooks, choices, wording, or nonauthoritative drafts;
- transform presentation for tone, accessibility, or brevity;
- suggest a candidate from an already-authorized eligible set when the controller/domain still performs final deterministic validation;
- explain rules, provenance, choices, and consequences using permitted evidence.

Optional AI may not:

- make an authoritative mechanical result legal;
- bypass a required proposal/approval or human-choice gate;
- choose for the human where `human_required` applies;
- alter permission, delegation, visibility, entitlement, policy, or ownership;
- silently publish generated content as canonical/Campaign truth;
- receive unrelated private data or unrestricted hidden GM state;
- grant itself tools or broaden its context;
- resolve ambiguity by inventing authoritative state.

AI failure never blocks a core deterministic/manual path where the owning domain otherwise supports one.

## 7. Automatic-resolution versus mandatory human choice

Every candidate operation is classified by the owning domain and mode profile as one of:

- `automatic_permitted` — controller may execute when current authority/state checks pass;
- `automatic_with_bounds` — controller may execute only within declared numeric/time/object/step bounds;
- `proposal_required` — controller may prepare/submit a governed proposal but another authorized decision-maker must decide;
- `human_required` — an authorized human must explicitly choose/confirm before state can advance;
- `prohibited` — controller cannot perform the operation in this mode/profile.

### Mandatory human-choice baseline

Unless a later owning-domain contract explicitly and safely narrows the rule, a human is required for:

- choosing the Player character’s intentional Action when it is not an explicitly preauthorized repeated/routine action;
- accepting a materially different plan after stale/conflict recovery;
- consent, privacy, safety, social-boundary, or participation decisions;
- entering/leaving a Campaign, accepting invitations, or accepting material role/control/ownership transfers;
- irreversible or high-impact Character advancement/build choices;
- spending real money, paid credits, or changing provider/budget policy;
- canonical promotion, publication, public sharing, release, or deployment;
- destructive deletion or irreversible migration;
- granting, widening, transferring, or renewing automation authority;
- any action marked human-required by its owning domain;
- any ambiguous/out-of-model situation where the controller cannot prove a permitted deterministic path.

A later CozyMode design may define narrow repeat/routine preferences (for example “continue this project until the next decision point”) but those preferences themselves are explicit bounded human instructions and cannot become general-purpose autonomy.

## 8. Run lifecycle

### 8.1 Start

Starting automated play is an authoritative command that:

1. revalidates the initiating subject and target Context;
2. validates the mode profile and scenario/activity compatibility;
3. validates/creates an explicit delegation grant;
4. freezes or records exact relevant versions and limits;
5. creates an `automationRunId` and initial run receipt;
6. records the current authoritative Event/projection sequence;
7. selects foreground/background behavior explicitly;
8. enters `running` only after all required checks pass.

Starting a mode never creates a new Campaign merely because the cadence or automation style changes.

### 8.2 Pause

Pause creates a deterministic execution barrier.

- Operations accepted before the pause barrier may complete according to idempotency/status-lookup rules.
- No new state-affecting automated command may be accepted after the barrier until resume.
- Pending human choices and nonauthoritative drafts remain recoverable.
- Pause does not roll back committed Events.

### 8.3 Exit/disconnect

Closing the client or losing connectivity is **not** equivalent to permission for background automation.

Each run declares one of:

- `foreground_only` — default for initial AutoGM; disconnect/exit causes safe pause/recovery-required behavior;
- `bounded_background` — allowed only for profiles such as approved Cozy progression, with explicit duration/step/event limits, notification policy, and stop conditions.

There is no silent indefinite background play.

### 8.4 Resume

Resume revalidates identity, Context, delegation, permissions, entitlements, lifecycle, mode/scenario versions, pack/schema compatibility, pending human choices, and last authoritative Event sequence.

If a material version or authority change cannot be safely reconciled, the run enters `review_required` rather than guessing or silently migrating.

### 8.5 Stop

Stop ends the run and prevents new automated operations. It preserves all already-committed ordinary Multiversal state and Event history. Stop is not rollback.

A stopped run may later be resumed only through a new governed start/resume decision allowed by its profile and current authority.

### 8.6 Revoke / expire

Revocation or expiry immediately invalidates effective delegation for new operations.

- accepted/committed Events remain historical truth;
- pending unaccepted commands are cancelled or rejected where possible;
- ambiguous in-flight commands use status lookup before retry or cleanup;
- cached/controller state cannot authorize a mutation;
- user-visible recovery explains the safe next action without exposing hidden state.

## 9. Run state vocabulary

Minimum APM-01 run states:

1. `draft`;
2. `validating`;
3. `ready`;
4. `running`;
5. `awaiting_human_choice`;
6. `awaiting_governed_approval`;
7. `pausing`;
8. `paused`;
9. `background_bounded`;
10. `stopping`;
11. `stopped`;
12. `expired`;
13. `revoked`;
14. `stale`;
15. `recovery_required`;
16. `review_required`;
17. `completed`;
18. `failed_safe`.

Only ordinary accepted domain Events and their current projections are authoritative game/workspace state. The automation-run record governs automation execution but is not a parallel game-state ledger.

## 10. Persistence, provenance, and deterministic replay evidence

Each run records enough evidence to explain what automation did without making the run record the authority for domain state:

- controller/run/mode/delegation IDs and versions;
- initiating subject and Context;
- scenario/activity package versions;
- exact commands proposed/invoked and owning domain;
- operation IDs and expected versions;
- resulting Event IDs/sequences or rejection/status receipts;
- random seed/entropy evidence where used;
- pending human-choice IDs;
- pause/resume/stop/revoke/expiry receipts;
- optional-AI request/result provenance, citations, model/provider class, cost/fallback evidence;
- policy/permission/entitlement/visibility versions;
- timestamps and correlation IDs.

Replay/diagnostics may reconstruct why a controller selected an operation and verify the resulting deterministic mechanical path. Replaying evidence does not independently reapply Events.

## 11. Save, exit, resume, and continuity

Automated play reuses ordinary persistence and recovery:

- authoritative Character/Campaign/Session/world state is reconstructed from ordinary durable state and Events;
- local drafts remain drafts;
- ambiguous commands use operation-status lookup;
- missed Events recover from sequence/checkpoint evidence;
- permissions and hidden-information projections are regenerated on resume;
- run bookkeeping restores the controller to the last proven Event sequence and pending decision point;
- no separate “AutoGM save universe” or “Cozy save universe” exists.

A Character or Campaign may move between ordinary play, asynchronous play, CozyMode, AutoGM, and later back to ordinary live play so long as each transition is explicitly authorized and uses the same governing state/history.

## 12. Cozy-specific baseline established by APM-01

APM-02 owns the detailed Cozy loop. APM-01 establishes these authority rules now:

- Cozy is setting-independent and cannot assume a farming/life-sim genre;
- automatic progress occurs only through owning-domain operations classified as automatic and explicitly bounded by user/profile preferences;
- background progress, if enabled, is bounded and stops at mandatory choices, exhaustion of limits, stale/conflict state, permission change, or profile stop condition;
- relationship/social automation cannot silently consent on behalf of a human participant;
- resource/crafting/project automation cannot exceed explicit budgets or ownership/custody authority;
- no-AI fallback remains available for the core loop where the owning domains support it.

## 13. AutoGM-specific baseline established by APM-01

APM-03/APM-04 own encounter and mini-campaign detail. APM-01 establishes:

- initial AutoGM is a bounded scenario/activity controller, not an unrestricted world simulator;
- Single Encounter and bounded Short Adventure/Mini-Campaign are the first designed targets;
- scenario-private truth is held by governed package/controller projection, not by a global GM account role;
- the human Player retains mandatory Player-intent decisions;
- NPC/world operations are controller-owned only when the selected package explicitly allows them;
- mechanical state is deterministic/domain-owned;
- optional AI supplies presentation/proposals, never authority;
- out-of-scope or undefined situations fail safe to a human choice, alternate permitted path, or stop/review state.

## 14. Connected Cozy baseline established by APM-01

APM-05 owns detailed Connected Cozy behavior. APM-01 establishes:

- invited/known participants only for initial scope;
- every participant has ordinary subject identity and independent contextual authority;
- one participant cannot delegate another participant’s Personal authority;
- shared projects/resources use their owning-domain contribution/ownership/control rules;
- leaving/revocation removes future authority without rewriting committed shared history;
- a controller never becomes a blanket authority over all participants merely because the space is automated.

## 15. Required denial and recovery scenarios

APM-01 requires future implementation/acceptance to cover at minimum:

1. Player starts AutoGM in a Campaign where the Player lacks authority to delegate GM-only operations → deny without leaking hidden GM state.
2. Authorized AutoGM package performs an allowed NPC operation → domain reauthorization passes and one Event is committed.
3. Controller attempts an operation outside the grant → deny and preserve run with safe diagnostic.
4. Mode flag is changed client-side to AutoGM/Cozy → no authority change.
5. Optional AI recommends an illegal or hidden-state-dependent operation → deterministic/domain gate rejects or strips it; no mutation.
6. Human-required choice is reached during background Cozy progression → run pauses and notifies; it does not choose silently.
7. Delegation is revoked while an operation is in flight → status lookup determines whether an Event committed; no duplicate effect.
8. Permission/entitlement changes while paused → resume revalidates and enters safe review/denial state where needed.
9. Client disconnects during foreground AutoGM → run safely pauses/recovery-resumes from proven sequence.
10. Bounded background Cozy reaches duration/step limit → stops/pauses with summary; no indefinite progression.
11. User stops AutoGM → committed Campaign/Character state remains ordinary state and later live play can continue.
12. Same deterministic scenario state, command inputs, rules versions, and seed evidence → same governed mechanical outcome irrespective of optional-AI wording.
13. AI provider is unavailable → deterministic/manual path remains usable where supported.
14. Controller can access bounded scenario-private truth but optional AI receives only task-filtered presentation context.
15. Owner/Admin, service tool access, or controller registration alone cannot create Campaign/private authority.

## 16. Additive implementation touch points

APM-01 does not authorize implementation. It identifies successor touch points for APM-06 handoff:

1. **Authority contracts** — add explicit automation-controller/service-principal and delegation records without broadening human role unions.
2. **APW context successor** — automated runs bind to APW Personal/Campaign/Session context and current subject authority.
3. **Campaign/Session authorization** — support explicit delegated controller capabilities rather than mapping controllers to global GM.
4. **Action/proposal system** — reuse operation IDs, expected versions, proposal/approval, decision receipts, and Event commit semantics.
5. **Recovery** — reuse status lookup, sequence recovery, revocation invalidation, bounded offline rules, and stale/conflict handling.
6. **Optional AI** — consume existing consent, redaction, provenance, provider abstraction, cost/fallback, and nonauthoritative proposal boundaries.
7. **Scenario/Adventure contracts** — add AutoGM-enabled package metadata, machine-private scenario projection, deterministic choice/branch rules, and safe out-of-model behavior.
8. **Downtime/project/social/crafting/research domains** — expose explicit automatic-resolution classifications and preference/budget boundaries for CozyMode.
9. **Notifications/work queues** — surface pending human choices, bounded-background summaries, errors, revocation, and return-to-context links without leaking hidden state.
10. **Diagnostics/export** — expose attributable automation provenance and deterministic evidence without secrets/raw hidden content.
11. **Testing** — add mode-flag-no-authority, over-delegation denial, AI-unavailable fallback, same-seed deterministic outcome, human-choice pause, revoke-in-flight, and ordinary-live-resume fixtures.

Completed Stage A milestones remain valid and are not reopened by these planned additive successor contracts.

## 17. Nonauthorization

APM-01 does not authorize:

- application implementation;
- global AI or automation GM authority;
- autonomous canonical promotion/publication;
- public matchmaking;
- unrestricted autonomous/open-ended campaigns;
- paid AI/provider use;
- production credentials;
- broad offline authoritative play;
- release, deployment, or tester distribution;
- CCTI-12-T04 resumption before September 2026.

## 18. Completion gate

APM-01 is substantively complete when:

- Solo/AutoGM/Cozy/Connected Cozy terminology is unambiguous and orthogonal to Context/Cadence/Connectivity/role;
- controller identity and explicit delegation are defined;
- no controller/mode/AI flag can imply global GM authority;
- automatic versus proposal/human/prohibited operation classes are defined;
- lifecycle start/pause/exit/resume/stop/revoke behavior is deterministic;
- domain-owned mechanical authority and optional-AI presentation/proposal responsibility are separated;
- hidden scenario truth has a bounded non-AI authority path without exposing it to optional AI by default;
- ordinary Event/persistence/recovery/provenance remains the single state/history model;
- additive successor touch points are identified without reopening completed work.

Final `completed_verified` requires the governed AIOC repository-health/PR evidence recorded in the work-state checkpoint and review receipt.