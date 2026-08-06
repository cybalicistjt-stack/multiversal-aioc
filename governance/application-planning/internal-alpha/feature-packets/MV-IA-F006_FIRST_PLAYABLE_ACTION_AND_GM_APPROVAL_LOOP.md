# MV-IA-F006 — First Playable Action and GM Approval Loop

**Program:** MV-IA-001  
**Work item:** IA-D04-001  
**Feature ID:** MV-IA-F006  
**Version:** 0.1.0  
**Design status:** implementation-ready  
**Owner and final authority:** John Brandon Turner  
**Owner:** John Brandon Turner  
**Date:** 2026-08-06  
**Companion matrix:** `MV-IA-F006_ACTION_APPROVAL_MATRIX.json`

## 1. Purpose

This packet defines the first complete internal-alpha tabletop loop:

> Campaign → Character → Scene → Action proposal → GM inspection, modification, and decision → authoritative result → synchronized persistent state.

It converts Stage A6, Journey IA-J03, shared proposal/approval systems, IA-D02-006 shared foundations, and IA-D03-005 Character/Campaign preparation contracts into one implementation-ready feature contract.

The design proves one complete Player-to-GM loop before full combat, inventory, social, investigation, adventure, vehicle, or AI breadth is added.

## 2. Scope and explicit boundaries

Included:

- Player Action draft, rule inspection, targets, costs, requirements, roll evidence, modifiers, computed result, proposed Effects, warnings, confirmation, and submission;
- authoritative validation;
- GM or delegated Assistant-GM notification, queue, inspection, approve, deny, and modify-and-approve;
- GM-controlled NPC and enemy Actions through the same governed review and result model;
- atomic authoritative result commit;
- role-filtered Player, GM, Assistant-GM, observer, notification, history, export, diagnostic, and optional-AI projections;
- idempotency, expected-version handling, reconnect, event-gap recovery, revocation, and bounded offline draft behavior;
- desktop, tablet, mobile, keyboard, touch, screen-reader, high-zoom, reduced-motion, and noncolor equivalents.

Excluded:

- full initiative, movement, reaction, interrupt, area-template, turn-order, encounter-end, reward, or defeat systems from MV-IA-F007;
- broad social, investigation, crafting, vehicle-station, map-authoring, or adventure-branch mechanics;
- AI decision authority;
- canonical content promotion;
- paid services, production credentials, real-user data collection, internal-alpha release, production deployment, or public release.

## 3. Governing sources and precedence

Precedence is:

1. owner decisions and active Phase 9 architecture;
2. IA-D02-006 shared-foundation contracts for identity, authorization, projections, state authority, recovery, diagnostics, accessibility, and provider neutrality;
3. IA-D03-005 preparation contracts for Campaign policy, Character control, exact launch snapshot, Session authority, Scene binding, source provenance, and fixture boundaries;
4. MV-IA-F021 for local draft, authoritative command, idempotency, status lookup, reconnect, revocation, and bounded offline behavior;
5. MV-IA-F020 for default-deny visibility and inference safety;
6. Stage A6, the MV-IA-F006 registry entry, Journey IA-J03, and shared systems SS-06, SS-07, SS-08, SS-11, SS-12, SS-13, SS-14, SS-15, SS-16, SS-18, and SS-19 for feature-specific presentation and evidence.

A lower-precedence source may narrow behavior. It may not widen authority, expose hidden information, bypass immutable Session bindings, or convert advisory calculation into authoritative state.

### Explicit compatibility anchors

MV-IA-F003, MV-IA-F004, and MV-IA-F005 are explicit controlling dependencies for identity/workspace, Character, and Campaign/Scene/Session authority.

Action history and My Proposals remain secondary. Offline authoritative mutation is prohibited. Realtime messages are advisory.

## 4. Actor, role, and authority model

Relevant actors are:

- Player subject;
- Player-controlled Character or other permitted actor;
- game-master;
- delegated assistant-gm;
- GM-controlled NPC or enemy actor;
- observer;
- owner-admin for operational evidence only;
- optional service actor.

Authentication, Campaign membership, active role, Assistant-GM delegation, Character control, actor control, entitlement, selected context, support access, and decision authority remain separate.

A Player may propose only for an actor they currently control in the active Session context.

A game-master may decide within the Campaign and Session. An assistant-gm may decide only inside an active, explicit delegation that includes the proposal type, Scene or Session scope, and permitted modification classes.

AI has no user role, actor control, decision, modification, approval, denial, commit, or support authority.

## 5. Stable identity and context contract

Stable IDs include:

- `proposalId`;
- `operationId`;
- `subjectId`;
- `campaignId`;
- `sceneId`;
- `sessionId`;
- `snapshotId`;
- `actorId`;
- optional `actorCharacterId`;
- `actionDefinitionId`;
- target IDs;
- `decisionId`;
- `eventId`;
- `correlationId`.

Display names, aliases, filenames, provider IDs, token labels, and current UI selections never replace stable IDs.

Every protected route and mutation revalidates the current subject, authentication session, Campaign membership, role, delegation, Character or actor control, permission, entitlement, Session lifecycle, launch snapshot, pack lock, schema versions, exact object versions, and expected Session version.

## 6. Integrated state vocabulary

The canonical Action-loop states are:

1. `local-draft`;
2. `local-autosaved`;
3. `validating`;
4. `validation-failed`;
5. `ready-to-submit`;
6. `submitted`;
7. `pending-gm-decision`;
8. `decision-in-review`;
9. `approved`;
10. `modified-and-approved`;
11. `denied`;
12. `commit-pending`;
13. `committed`;
14. `projection-pending`;
15. `completed`;
16. `stale`;
17. `revoked`;
18. `recovery-required`.

Only durable accepted Events and current server projections are authoritative. Local drafts, autosave receipts, calculations, notifications, realtime messages, cached rule summaries, pending requests, and AI output are nonauthoritative.

## 7. Player Action draft and available-Action projection

The Player view emphasizes:

- current Scene projection;
- current Character or actor summary;
- available Actions;
- target selection;
- costs and requirements;
- proposal confirmation;
- pending status;
- final result.

Action history and “My Proposals” remain accessible but secondary rather than default dominant panels.

The available-Action projection is server-generated after authorization, entitlement, actor-control, Session, launch-snapshot, pack, schema, and visibility filtering. A hidden or unavailable Action must not leak through counts, disabled labels, autocomplete, warnings, or rule links.

A local draft may preserve safe Player input. It does not reserve Resources, establish targets, create a proposal, or mutate Session state.

## 8. Quick rules inspection and source evidence

The Player and GM can inspect a quick rules explanation without leaving the active flow.

The inspection includes only authorized fields:

- Action name and stable source identity;
- source pack and version;
- short rule summary;
- prerequisites;
- target rules;
- costs;
- roll or deterministic resolution model;
- modifier order;
- proposed Effect vocabulary;
- relevant Conditions and Resources;
- warnings and known limitations;
- source/provenance link where permitted.

The GM inspection may include additional authorized adjudication detail. The Player projection must not receive GM-only notes, hidden target state, secret modifiers, concealed difficulty, private motives, or unrelated source-license-sensitive fields.

## 9. Target, cost, requirement, roll, modifier, and Effect preparation

Before submission, the client may display a nonauthoritative calculation preview using exact inputs and deterministic local adapters.

The proposal records:

- actor and actor version;
- Action Definition and version;
- target IDs and expected target versions;
- costs and affected Resources;
- requirements and their evidence;
- roll model and seed or roll evidence;
- ordered modifiers and sources;
- computed result;
- proposed Effects;
- warnings;
- exact Session, permission, entitlement, pack, schema, and policy versions.

The preview never claims that the result is accepted or that costs have been spent.

## 10. Authoritative validation and submission

Submission is an online authoritative command with a stable `operationId`.

The service validates, at minimum:

- authenticated subject and active Session;
- Campaign membership and role;
- actor control and lifecycle;
- launch-snapshot and Scene binding;
- Action Definition availability and exact version;
- pack, schema, rules, permission, and entitlement compatibility;
- target existence, visibility, eligibility, and exact versions;
- costs and requirements;
- roll evidence and modifier ordering;
- Effect schema;
- expected Session version;
- idempotency;
- current revocation state.

Validation failure creates no pending proposal and commits no costs or Effects. User-safe errors must not disclose protected existence.

A successful submit produces one durable proposal and a status receipt. The Player sees `pending-gm-decision` without receiving GM-only queue, warning, or adjudication data.

## 11. GM notification, queue, and inspection surface

An authorized decision-maker receives a permission-safe approval notification and queue entry.

The GM inspection must show:

- proposing Player or authorized proposer;
- actor;
- Action;
- source and quick rules summary;
- targets;
- costs;
- requirements;
- roll and seed or evidence;
- modifiers and ordering;
- computed result;
- proposed Effects;
- warnings;
- proposal, Session, Character, target, permission, entitlement, pack, and schema versions;
- current stale, conflict, revocation, or compatibility findings.

Notification counts and queue ordering are filtered before counting or ranking. Unauthorized users do not learn that a protected proposal exists.

Opening a review does not itself accept, reserve, or mutate anything.

## 12. Approve, deny, and modify-and-approve decisions

The only final decision types are:

- `approve`;
- `deny`;
- `modify-and-approve`.

Approve accepts the reviewed proposal values after current revalidation.

Deny records an attributable decision, user-safe reason, and no accepted costs or Effects.

Modify-and-approve allows an authorized GM or delegated Assistant-GM to change permitted final fields before commit. Modification rules are:

- preserve the original proposal;
- identify each changed field;
- record original and final values;
- record reasons;
- identify the decider and active role or delegation;
- revalidate authority, entitlement, compatibility, expected versions, costs, roll evidence, modifiers, result, and Effect schema;
- require an explicit final confirmation;
- commit nothing before confirmation.

A modification cannot silently replace the original evidence or disguise a new Action as the submitted Action.

## 13. Decision concurrency, review claims, and stale proposals

A review claim is advisory coordination, not authority.

Only one final decision may win for a proposal. Competing or stale decisions fail with current status.

Before final decision, the service revalidates:

- proposal version;
- Session and launch-snapshot state;
- actor and target versions;
- current role and delegation;
- permission and entitlement;
- pack and schema compatibility;
- current Resource and Condition state;
- revocation and expiration.

If material inputs changed, the decision surface enters `stale` or `recovery-required`. It preserves the proposal and new authoritative state instead of silently recalculating and accepting.

## 14. GM-controlled NPC and enemy Actions

GM-controlled NPC and enemy Actions use the same governed model.

The GM creates or selects the actor, Action, targets, costs, roll evidence, modifiers, result, Effects, and warnings. The system then displays the same inspection information and requires an attributable approve, deny, or modify-and-approve confirmation before authoritative commit.

This self-review path prevents hidden bypasses and gives the Session one consistent history model.

An Assistant-GM may propose or decide only within delegated actor, Scene, Session, and modification scope.

## 15. Atomic authoritative result commit

An approved or modified-and-approved decision is not final until the authoritative commit succeeds.

The commit atomically writes:

- final decision receipt;
- final costs;
- final Effects;
- Resource changes;
- Condition changes;
- target-state changes;
- Session sequence and version;
- Action history;
- required notifications;
- durable Events.

If any required write fails, no partial accepted result is exposed as complete. Recovery uses the original operation and decision identities.

The controlling authority statement is:

> Only an accepted durable decision and an atomic `ActionResultCommitted` Event make costs, Effects, Resources, Conditions, and target-state changes authoritative.

## 16. Role-filtered synchronized projections

After commit, the service publishes current role-safe projections.

Player projection includes permitted:

- final outcome;
- accepted costs;
- visible Effects, Conditions, Resource changes, and target changes;
- user-safe modification or denial explanation;
- current Character and Scene state;
- status and history reference.

GM projection may include authorized full adjudication evidence, warnings, hidden Effects, and decision details.

Observer projection contains only observer-visible Session results.

A client never receives protected fields and merely hides them. Server-side projection occurs before serialization, notification, export, diagnostics, and AI retrieval.

## 17. Durable Events, history, and replay evidence

Durable Events preserve:

- stable Event type and identity;
- aggregate identity and expected sequence;
- proposal and decision references;
- actor, Action, and target stable IDs and versions;
- final accepted costs, roll evidence, modifiers, result, and Effects;
- decider attribution and change reasons;
- permission, entitlement, pack, schema, and policy references;
- timestamps and correlation identity.

History is role-safe. It is sufficient to explain accepted results and diagnose duplicate or missed delivery. It is not a client-side source of authority and need not expose protected hidden state.

Full deterministic replay is not promised where game rules permit human adjudication. The record must still preserve the accepted evidence and attributable decision.

## 18. Idempotency and ambiguous failure

Every mutable command uses a stable operation identity.

If the submit, decision, or commit response is lost, the client queries status with the original identity before retrying.

A repeated request with the same identity and compatible payload returns the prior result or current status. Conflicting reuse fails safely.

Duplicate submit, duplicate decision, duplicate commit, delayed notification, reconnect replay, and repeated realtime delivery must not duplicate costs, Effects, Resources, Conditions, history, or notifications.

## 19. Reconnect, event-gap recovery, and revocation

Reconnect sends:

- last acknowledged Event sequence;
- current Session version;
- selected-context receipt;
- outstanding proposal, decision, and command IDs;
- safe local draft summary;
- permission and entitlement hints;
- pack, schema, client, and protocol versions;
- correlation ID.

The service returns current authority, command statuses, Event-gap plan, current projection, queue status where authorized, draft reconciliation, cache invalidation, and user-safe messages.

A Player disconnect after submit recovers the same pending or final proposal. A GM disconnect during review does not lose the proposal; a review claim may expire without making a decision.

Revocation invalidates routes, subscriptions, selected-context and proposal receipts, protected caches, queue entries, status lookup outside current authority, and optional-AI projections.

## 20. Bounded offline behavior

Permitted offline behavior may include:

- reading unexpired authorized Scene, Character, Action, and rules projections named by the offline manifest;
- creating or editing a local Action draft;
- reviewing local draft history;
- preparing targets and notes as explicitly nonauthoritative.

Offline behavior may not:

- submit a proposal;
- create a durable pending decision;
- approve, deny, or modify;
- reserve or spend Resources;
- apply Effects or Conditions;
- mutate target state;
- launch a Session command;
- perform authoritative restore, migration, or export finalization.

Reconnect revalidates all authority, versions, compatibility, and revocation before any local draft can be submitted.

## 21. Responsive and accessible behavior

Desktop may use Scene, Character, Action, and approval panels. Tablet may collapse inspectors. Mobile uses a single-focus sequence.

Layout changes may not change:

- authority;
- required evidence;
- decision options;
- warnings;
- modification reasons;
- confirmation;
- recovery choices;
- final outcome.

Keyboard and touch users can complete every step. Rules, targets, costs, modifiers, Effects, warnings, and decision differences have semantic labels and noncolor status.

Roll and modifier visualizations require ordered text or table alternatives. Focus returns predictably after rule inspection, target selection, submit, decision, conflict, reconnect, and result acknowledgement. Live-region announcements distinguish pending, approved, modified, denied, committed, stale, revoked, and recovery-required states.

## 22. Privacy, diagnostics, support, AI, provider, and cost boundaries

Diagnostic generation defaults to exclude proposal prose, hidden targets, secret modifiers, GM notes, private Character notes, credentials, and unrestricted source text.

Issue submission and assignment never grant Session, Character, proposal, decision, or hidden Scene access.

Optional AI may explain already-authorized rules or draft nonauthoritative wording. It cannot select hidden targets, calculate with hidden evidence, decide, modify, approve, deny, commit, or widen retrieval.

Core product and deterministic CI require zero AI and no paid identity, realtime, notification, analytics, crash-reporting, ticketing, dice, rules, or simulation provider. Provider SDKs remain behind application-owned ports.

## 23. Deterministic fixtures and test obligations

Fourteen explicitly synthetic, noncanonical F006 contract fixtures cover:

- Player happy path;
- GM modify-and-approve;
- GM denial;
- duplicate submit;
- stale Session version;
- Player disconnect before submission;
- Player disconnect after submission;
- GM disconnect during review;
- lost commit response;
- missed realtime Event;
- GM NPC or enemy self-review;
- Assistant-GM out-of-scope denial;
- observer-safe projection;
- revocation before decision.

Tests must prove:

- one durable outcome;
- no duplicate Effects;
- no partial atomic result;
- current authorization and expected-version enforcement;
- role-safe projection;
- original proposal preservation after modification;
- attributable decision receipt;
- recovery from status and Event history;
- accessible and responsive parity;
- zero-service deterministic execution.

The fixtures are test contracts, not canonical game content or claims about complete combat coverage.

## 24. Acceptance criteria, implementation order, and next handoff

- **FPA-AC-001:** The complete Campaign-to-persistent-result vertical slice is defined.
- **FPA-AC-002:** Player available Actions are authorized, entitled, actor-compatible, and launch-snapshot-compatible projections.
- **FPA-AC-003:** Player rules inspection is source-linked and excludes GM-only information.
- **FPA-AC-004:** Proposal evidence includes actor, Action, source, targets, costs, requirements, roll evidence, modifiers, computed result, proposed Effects, warnings, and exact versions.
- **FPA-AC-005:** Submission performs current authoritative validation and creates no partial costs or Effects on failure.
- **FPA-AC-006:** The GM notification and queue expose only authorized proposals and show every required inspection field.
- **FPA-AC-007:** Final decisions are approve, deny, or modify-and-approve.
- **FPA-AC-008:** Modification preserves the original proposal, records changed fields and reasons, and requires final confirmation.
- **FPA-AC-009:** Player, GM, Assistant-GM, observer, history, export, diagnostic, and AI projections are independently permission-safe.
- **FPA-AC-010:** GM-controlled NPC and enemy Actions use the same inspection, decision receipt, commit, and history model.
- **FPA-AC-011:** One atomic commit controls costs, Effects, Resources, Conditions, target changes, Session version, Events, history, and notifications.
- **FPA-AC-012:** Realtime delivery is advisory; durable Events and current projections are authoritative.
- **FPA-AC-013:** Stable operation identity prevents duplicate submit, decision, commit, costs, Effects, and history.
- **FPA-AC-014:** Ambiguous failure uses status lookup with the original identity before retry.
- **FPA-AC-015:** Stale writes and decisions preserve both proposal and current authoritative state; silent last-write-wins is prohibited.
- **FPA-AC-016:** Disconnect and missed-Event cases recover the same pending or final outcome.
- **FPA-AC-017:** Revocation invalidates routes, subscriptions, caches, receipts, queue entries, status lookup, and protected projections.
- **FPA-AC-018:** Offline behavior is limited to authorized reads and local drafts and cannot submit, decide, or commit.
- **FPA-AC-019:** Desktop, tablet, mobile, keyboard, touch, screen reader, high zoom, reduced motion, and noncolor presentations preserve authority and evidence.
- **FPA-AC-020:** Fourteen deterministic fixtures, ten dependency-ordered implementation slices, zero blocking findings, zero required AI, and explicit implementation/release holds are recorded.

Implementation order is defined in the companion matrix and begins with IDs, state, envelopes, and authority ports before Player drafting, validation, GM review, atomic commit, NPC/enemy self-review, recovery, history, accessibility, and deterministic fixtures.

No blocking design finding remains open.

The exact next design item is **IA-D04-002 — proposal and approval shared-component contract**.

Silence is not approval. Implementation remains dependency-gated by P9-06 and the concrete shared services.


### Canonical packet-template compatibility map

The packet is indexed under the canonical template labels `## 1. Problem and user outcome`, `## 2. Alpha slice`, `## 3. Roles and authority`, `## 4. Dependencies`, `## 5. Object and state model`, `## 8. Failure, empty, and recovery states`, `## 9. Permissions and hidden information`, `## 10. Entitlements`, `## 11. Persistence and history`, `## 14. Accessibility`, `## 18. Test scenarios`, `## 19. Acceptance criteria`, `## 21. Security, privacy, cost, and risk`, `## 22. Owner review points`, `## 23. Implementation handoff`, and `## 24. Readiness decision`. These labels map to the packet's more specific numbered sections without changing their content or order.

The governing conclusion remains: implementation remains dependency-gated.
