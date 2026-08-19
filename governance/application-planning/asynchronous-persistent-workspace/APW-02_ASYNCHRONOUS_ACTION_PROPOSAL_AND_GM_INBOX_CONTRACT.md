# APW-02 — Asynchronous Action, Proposal and GM Inbox Contract

**Work item:** APW-02  
**Program:** APW — Asynchronous Play & Persistent Workspace  
**Version:** 0.1.0  
**Status:** DESIGN CONTRACT — READY FOR GOVERNED REVIEW  
**Owner and final authority:** John Brandon Turner  
**Date:** 2026-08-18

## 1. Decision

Asynchronous play reuses the existing A6 Action/proposal/decision/Event architecture. It does **not** create a second asynchronous rules engine, an alternate Campaign truth store, a separate GM authority system, or a queue whose position grants authority.

An asynchronous Action proposal is an ordinary governed A6 proposal that remains durably pending across time, devices, disconnects and Sessions until it reaches a final decision, is revoked/withdrawn, expires, or requires explicit stale-state recovery.

The core invariant is:

> **One `proposalId` may produce at most one final authoritative outcome.**

Retries, reconnects, multiple GM devices, concurrent reviewers, delayed notifications, proposal revisions and ambiguous network failures must not create duplicate decisions or duplicate Events.

APW-02 consumes:

- APW-01 universal-user/contextual authority;
- A5 Campaign/Scene/Session ownership;
- A6 Action proposal, decision, status, atomic commit and reconnect contracts;
- MV-IA-F006 proposal/approval loop;
- MV-IA-F021 idempotency/recovery/bounded-offline rules;
- D05/permissions hidden-information projection boundaries;
- APM-01 nonhuman/AI nonauthority where automation later participates.

## 2. What is and is not asynchronous state

### 2.1 Local draft

A local/autosaved draft remains nonauthoritative and may be edited freely. It cannot enter a GM inbox until the normal A6 validation/submission path succeeds online.

### 2.2 Submitted proposal

A submitted asynchronous proposal is a durable, versioned proposal record. Submission freezes the exact evidence needed to explain what the proposer intended at that revision:

- stable `proposalId`;
- unique state-changing `operationId` and idempotency identity;
- proposer subject, Campaign, Scene, Session, actor and Character identities;
- Character/target/session expected versions;
- Action definition and source pack versions;
- costs, requirements, roll evidence, modifiers, computed result and proposed effects;
- permission/entitlement version hints;
- correlation/provenance identifiers;
- proposal version and submission timestamp;
- optional expiry/deadline policy reference.

The proposal is **not** an Event and does not mutate authoritative gameplay merely by waiting in the inbox.

### 2.3 Final decision

Final decision remains A6 `approve`, `deny`, or `modify-and-approve`, with current authority and final validation. An approved/modified decision only becomes authoritative gameplay through the existing atomic decision/Event commit path.

A denial is a final proposal decision but produces no gameplay effects.

### 2.4 Coordination state

Inbox assignment, review-open indicators, reminders, notification delivery, snooze and ordering are coordination/projection state. They do not alter Campaign truth, proposal legality or decision authority.

## 3. Stable identity and revision model

### 3.1 Proposal identity

`proposalId` identifies the durable intent thread that can produce at most one final decision.

### 3.2 Proposal revision

Before a final decision, a proposer may create a new `proposalVersion` only through an explicit governed revision operation when the proposal is in a revisable state.

A revision:

- keeps the same `proposalId`;
- increments `proposalVersion` monotonically;
- uses a new state-changing `operationId`/idempotency fingerprint;
- preserves every prior submitted revision for provenance;
- records who revised it, when, and why where applicable;
- freezes a new ActionProposal snapshot including fresh expected versions/evidence;
- invalidates any nonfinal review view of the superseded revision;
- cannot replace or mutate a final decision.

Reusing an old operation ID for different revision payload bytes is rejected under existing A6 ambiguous-retry rules.

### 3.3 When revision is allowed

Proposer revision is allowed only before a final decision and only if current authority still permits proposal authorship. A review coordination lock may temporarily require the proposer to request release/return rather than racing an active reviewer, but the lock is not itself authority.

### 3.4 Material stale refresh

When current Character, Session, target, Action definition, pack, permission or entitlement state makes the waiting revision stale, the system never silently recomputes Player intent and commits it.

The proposal becomes `stale/review-required` and the user receives a safe explanation. A fresh revision must be explicitly accepted/submitted by the proposer when the change could alter intent, cost, target, risk, outcome, resources or meaning.

Purely presentation-level refreshes may be regenerated without a proposal revision.

## 4. Withdrawal, revocation, expiry and cancellation

### 4.1 Proposer withdrawal

Before a final decision, an authorized proposer may withdraw the proposal. APW-02 maps withdrawal to an attributable proposal revocation/cancellation operation rather than inventing a gameplay Event.

Withdrawal:

- blocks new final decisions after the revocation barrier;
- does not erase proposal/review history;
- does not roll back an already committed Event;
- is idempotent;
- uses status lookup if the withdraw request races a decision or suffers an ambiguous failure.

If a final decision/commit won the race first, the user receives the already-final status. No second reversal Event is invented automatically.

### 4.2 Authority revocation

Permission, role, delegation, entitlement or Campaign lifecycle changes may revoke a pending proposal independently of proposer intent. Cached clients cannot override this.

### 4.3 Expiry

A proposal may have an explicit server-governed `expiresAt` or policy-derived expiry. Expiry is not determined by a client clock and cannot be inferred merely because a notification was old.

Expiry is a non-gameplay final disposition that prevents future approval unless the proposer creates a new/revised proposal under current state.

### 4.4 Campaign/Session closure

If the target Campaign/Scene/Session lifecycle no longer accepts the proposal, the proposal transitions to an explicit revoked/expired/stale disposition according to owning-domain policy. It is never silently applied to a later Session solely because actor/action labels still match.

## 5. Clarification loop

A GM/authorized decider may request clarification before making a final A6 decision.

Clarification is **nonfinal coordination state** and does not modify Player intent.

A clarification request contains:

- `clarificationRequestId`;
- proposal ID/version reviewed;
- requesting subject and current delegation evidence;
- bounded question/reason code;
- user-safe text;
- requested-at and optional response-by timestamp;
- correlation/provenance reference.

The proposer may:

- reply with explanatory text that does not change proposal semantics;
- create a new proposal revision when the answer changes action intent/evidence;
- withdraw the proposal;
- leave it pending until expiry/policy action.

A GM may not rewrite the proposer’s intent under the label “clarification.” If the desired final result requires changes, existing A6 modification-diff and confirmation rules apply.

## 6. GM inbox contract

The GM inbox is a permission-filtered work queue over pending proposals. It is not authoritative state by itself.

### 6.1 Inbox item safe projection

A list row/card contains only what the current reviewer is authorized to know, such as:

- safe proposal label/action summary;
- proposer/actor safe identity projection;
- Campaign/Session context label;
- submitted/updated timestamp;
- proposal version;
- current coordination state;
- deadline/age indicator where permitted;
- safe warning badges such as `stale`, `clarification`, `expiring`, `changed-since-open`;
- assignment/review indicator where permitted.

Hidden targets, effects, secret relationships, GM-only values, other Players’ private details and forbidden counts are filtered before inbox ranking/counting.

Opening the item performs fresh authorization and returns the current authorized review projection.

### 6.2 Ordering

Default deterministic ordering is a presentation concern, for example:

1. explicit Campaign-configured urgency/deadline class;
2. needs-review/clarification state;
3. submitted/last-updated time;
4. stable proposal ID tie-breaker.

Queue position never grants decision priority, ownership or authority. A Campaign may choose alternate presentation order without changing proposal semantics.

### 6.3 Review coordination lease

To reduce accidental duplicate work, the inbox may use a short-lived `reviewLease`/assignment indicator.

A lease:

- has reviewer subject, proposal/version, acquired/expiry timestamps;
- is coordination only;
- does not grant GM/Assistant-GM authority;
- cannot survive lost permission/delegation;
- does not make a final decision valid;
- may be released/expired/reclaimed;
- cannot override the authoritative at-most-one final-decision gate.

If two authorized reviewers race, only one final decision may succeed; the other receives `already-final`/current status.

## 7. Decision-time reauthorization

Opening an inbox item is not enough to authorize a later decision.

At final decision/commit time the system revalidates at minimum:

- reviewer subject and Campaign role/delegation;
- proposal still nonfinal and nonrevoked/nonexpired;
- exact proposal version being reviewed;
- current Session/Character/target versions;
- current Action definition/pack/schema compatibility;
- current permission and entitlement decisions;
- current resource/cost/requirement legality;
- current hidden-information rules;
- required final confirmation/modification diff;
- proposal/decision operation identity and existing final decision/commit status.

A successful read hours earlier creates no durable decision authority.

## 8. Stale-state matrix

A waiting proposal can become stale for different reasons; the response is explicit rather than one generic retry.

### 8.1 Session/target/Character version changed

If the changed state can affect legality, target, cost, result or intent:

- no approval occurs;
- current reviewer sees safe stale reason;
- proposer receives `refresh/revise required`;
- new revision revalidates from current state.

### 8.2 Action/rules/pack version changed

The proposal retains old source evidence for provenance, but a final decision requires current compatibility policy. If the old version is no longer legally executable, return/revise or deny; never silently substitute a new Action definition.

### 8.3 Permission/delegation changed

Reauthorize. Deny/revoke access as required; invalidate protected cache and notification deep links. No cached review lease survives.

### 8.4 Entitlement changed

Reauthorize. A proposal cannot commit content/mechanics no longer permitted at decision time merely because it was legal when submitted.

### 8.5 Harmless presentation changes

Labels, layout, localization and other nonsemantic projection changes may refresh without changing proposal version.

## 9. At-most-one final outcome

APW-02 relies on existing A6 invariants and strengthens the asynchronous orchestration around them.

For every final decision attempt:

1. use stable `decisionId` and operation/idempotency identity;
2. check existing final decision for `proposalId`;
3. bind decision to exact reviewed proposal version/current Session version;
4. run final validation/authorization;
5. atomically persist final decision and any approved gameplay Event/effects through the existing A6 commit path;
6. record resulting Event/result reference;
7. on ambiguous response, perform status lookup before any retry;
8. retries with same identity/payload return prior status;
9. conflicting identity reuse is rejected;
10. no notification, lease expiry or reconnect can create a second commit.

The authoritative uniqueness boundary is server/domain persistence, not client buttons being disabled.

## 10. Notification contract

Notifications are **attention signals**, never authority or complete truth projections.

### 10.1 Notification classes

Baseline asynchronous Action notifications:

- proposal submitted;
- proposal revised;
- clarification requested;
- clarification answered;
- review started/returned where useful;
- proposal stale and needs proposer action;
- proposal nearing expiry;
- proposal withdrawn/revoked/expired;
- final decision available;
- approved result committed/projected;
- recovery required.

### 10.2 Safe payload

External/push/OS notifications use minimal safe text by default:

- Multiversal account/app identity;
- safe Campaign label only if policy permits;
- generic work type such as “An Action needs review” or “Your Action has an update”;
- nonsecret deep-link token/reference;
- no raw hidden targets, secret effect text, GM-only reasons, private Character details or protected counts.

Opening a notification performs fresh authentication/context authorization before content is revealed.

### 10.3 Delivery semantics

Notification delivery is at-least-once/best-effort attention delivery. Duplicate or missing notifications must not duplicate or erase proposal state. Read/unread state is presentation metadata.

## 11. Offline and reconnect

### 11.1 Offline drafting

A user may continue an authorized local draft/cached safe draft under existing bounded-offline rules. Submission, revision of a durable pending proposal, withdrawal and final decision require authoritative connectivity unless a later owning-domain contract explicitly proves a safe queued command path.

### 11.2 Reconnect

On reconnect:

- reauthenticate and reauthorize selected context;
- lookup outstanding proposal/decision/operation IDs;
- recover missed Events from acknowledged sequence/checkpoint;
- re-evaluate permission/entitlement/pack/schema versions;
- invalidate revoked protected caches;
- show current pending/final/stale/revoked status;
- keep local drafts only when current policy permits;
- never blindly resend a state-changing command before status lookup.

## 12. AI and automation boundary

Optional AI may summarize an authorized proposal, explain rules/evidence, help draft clarification text or suggest questions. It cannot approve, deny, modify-and-approve, withdraw, revise Player intent, grant a review lease, expand delegation, bypass stale validation or commit an Event.

An APM automation controller may only interact with asynchronous proposals if a later explicit delegation/profile allows that exact operation class. APM-01 remains controlling; no automated-play mode flag grants GM inbox authority.

## 13. Minimum acceptance scenarios

1. Player submits proposal, closes app, GM approves tomorrow → one final decision and at most one resulting authoritative Event.
2. Player retries after submission timeout → status lookup returns existing proposal; no duplicate proposal/commit.
3. Two GM devices open same proposal → both may view if authorized; only one final decision can succeed.
4. Assistant GM review lease exists but delegation is revoked before decision → decision denied; lease grants no authority.
5. Player revises pending proposal → same proposal ID, higher proposal version, new operation identity; old version remains provenance and cannot be decided as current.
6. GM requests clarification → no Player intent mutation and no Event.
7. Clarification changes intended target → Player explicitly submits new revision.
8. Character/target/Session version changes while pending → proposal becomes stale/review-required; no silent recalculation or approval.
9. Action definition/pack changes incompatibly → final decision blocked until governed revise/deny path.
10. Player withdraws while GM decision is racing → status lookup establishes which final barrier won; never both withdrawal and a second contradictory commit.
11. Proposal expires while clients are offline → server-governed expiry prevents later approval; client clock is not authority.
12. Push notification leaks no hidden target/effect; opening it reauthorizes before detail.
13. User loses Campaign access → inbox/deep links/cache reveal no pending proposal content or hidden counts.
14. Approved decision response is lost → retry uses decision/operation status and returns prior result, not a duplicate Event.
15. AI provider unavailable → normal manual submit/review/decision loop remains usable.

## 14. Additive implementation touch points

APW-02 does not authorize implementation. A future handoff may require bounded additive changes to:

1. **A6 proposal record** — asynchronous timestamps/expiry and explicit revision/revocation metadata if current record is insufficient.
2. **A6 operation types** — proposer revision/clarification response and coordination operations as needed; reuse existing expire/revoke/status operations where sufficient.
3. **A6 decision/inbox ports** — permission-filtered durable queue and review projection, with coordination lease separate from authority.
4. **A6 atomic commit/status** — retain existing at-most-one final decision/Event and ambiguous retry behavior.
5. **A6 reconnect** — include delayed proposal revision/clarification/expiry status and deep-link recovery.
6. **Notifications** — safe event-to-notification projection and deep-link reauthorization.
7. **D05/permissions** — filter inbox counts/rankings/list rows before topology/cardinality.
8. **APW shell** — “Waiting on me / Waiting on GM / Needs clarification / Stale” work views.
9. **Tests** — multi-device race, revision race, withdrawal-vs-decision, stale-version, permission revocation, expiry, notification nonleakage and ambiguous-response fixtures.

Completed A5/A6/F006/F021 behavior remains authoritative and is extended rather than reopened.

## 15. Nonauthorization

APW-02 does not authorize:

- application implementation/migration;
- alternate asynchronous mechanics;
- automatic Player-intent rewriting;
- queue-position authority;
- notification-based authorization;
- AI/automation GM authority;
- unrestricted offline multi-writer mutation;
- release/deployment/tester access;
- paid services/production credentials;
- CCTI-12-T04 before September 2026.

## 16. Completion gate

APW-02 is substantively complete when:

- local draft/submitted proposal/final decision/Event distinctions are explicit;
- proposal identity/revision provenance is deterministic;
- withdrawal/revocation/expiry/race behavior is defined;
- clarification cannot mutate Player intent silently;
- GM inbox/lease/ordering are coordination, not authority;
- decision-time reauthorization/stale-state handling is explicit;
- notifications are safe attention signals with deep-link reauthorization;
- reconnect/status/idempotency guarantee at-most-one authoritative outcome;
- AI/automation cannot bypass owning-domain authority;
- implementation remains additive and unactivated.

Final `completed_verified` requires exact-head AIOC repository-health and merged PR evidence.
