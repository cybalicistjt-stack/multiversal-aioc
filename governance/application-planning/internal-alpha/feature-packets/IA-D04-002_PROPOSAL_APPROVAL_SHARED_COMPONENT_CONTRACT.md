# IA-D04-002 — Proposal and Approval Shared-Component Contract

**Program:** MV-IA-001  
**Work item:** IA-D04-002  
**Version:** 0.1.0  
**Status:** COMPLETE — DESIGN CONTRACT  
**Owner and final authority:** John Brandon Turner  
**Date:** 2026-08-06  
**Shared system:** SS-06 — Proposal and approval framework  
**Primary proven consumer:** MV-IA-F006 — First Playable Action and GM Approval Loop  
**Companion matrix:** `IA-D04-002_PROPOSAL_APPROVAL_COMPONENT_MATRIX.json`  
**Consumer mapping:** `IA-D04-002_CONSUMER_MAPPING.json`

## 1. Purpose and user outcome

This contract normalizes the reusable proposal-and-approval mechanics demonstrated by MV-IA-F006 so later domains do not independently invent incompatible proposal states, reviewer decisions, receipts, notifications, history, reconnect behavior, or accessibility semantics.

A proposer can prepare and submit a governed request, an authorized reviewer can inspect the evidence and approve, deny, or explicitly modify and approve it, and every participant receives a permission-safe authoritative outcome with durable history and interruption recovery.

The component is infrastructure for governed requests. It does not become the authority for any domain.

## 2. Scope and explicit boundaries

The shared component controls:

- proposal envelope and lifecycle;
- proposal author, actor, subject, target scope, and proposal type references;
- domain evidence attachment slots;
- reviewer queue and notification projections;
- reviewer inspection shell;
- approve, deny, and modify-and-approve decision capture;
- decision receipt structure and attribution;
- operation identity, expected version, idempotency, status lookup, and reconnect state;
- role-safe proposal, queue, notification, decision, result, history, export, diagnostic, and optional-AI projections;
- accessible and responsive state presentation.

The shared component does not:

- decide Campaign membership, Character control, ownership, entitlement, or support access;
- calculate domain results, costs, Effects, transfers, migrations, deletions, or promotions;
- select an approver without a domain authority decision;
- widen visibility or reveal protected proposal existence;
- commit domain state without a domain commit adapter;
- convert AI output into authority;
- make offline authoritative decisions;
- authorize paid services, production credentials, release, deployment, or publication.

## 3. Governing sources and precedence

Precedence is:

1. owner decisions and active Phase 9 architecture;
2. IA-D02-006 shared-foundation contracts;
3. IA-D03-005 Character/Campaign preparation integration;
4. MV-IA-F006 for the proven live-Action proposal/decision/result path;
5. SS-06 responsibilities in `INTERNAL_ALPHA_SHARED_SYSTEMS.md`;
6. each consumer domain's own authority, validation, commit, projection, and history contract;
7. this shared component for common orchestration and presentation only.

When a domain rule conflicts with generic convenience behavior, the domain rule wins. A consumer may narrow the common component but may not weaken default-deny authorization, projection safety, idempotency, attribution, history, or recovery.

## 4. Common actor and authority model

The common roles are:

- `proposal-author` — creates and may edit or withdraw a permitted proposal before final decision;
- `represented-actor` — Character, NPC, enemy, service actor, content author, asset controller, or other domain actor named by the proposal;
- `proposal-subject` — object or state expected to change if accepted;
- `reviewer` — subject currently authorized by the consumer domain to make the configured decision;
- `observer` — subject allowed a read-only projection, if the domain permits one;
- `service-actor` — deterministic calculation, validation, notification, indexing, or optional-AI adapter with no independent authority.

Authentication, membership, role, delegation, Character control, ownership, custody, entitlement, support access, selected context, reviewer authority, and owner-only authority remain separate decisions.

Reviewer identity is resolved at inspection and again at decision. Being notified, assigned, previously authorized, or able to view a queue does not itself grant decision authority.

## 5. Consumer adapter contract

Every consumer registers a versioned adapter defining:

- `consumerType` and `consumerContractVersion`;
- allowed `proposalType` values;
- stable aggregate and subject identity fields;
- author and represented-actor eligibility rules;
- reviewer authority resolver;
- proposal required-field schema;
- domain evidence schema;
- target-scope rules;
- calculation or preview adapter, when applicable;
- submission validator;
- decision validator;
- modifiable-field allowlist and patch validator;
- approval policy;
- domain commit adapter;
- domain Event and projection adapters;
- visibility and inference-safety policy;
- notification and queue policy;
- expiry, withdrawal, cancellation, and supersession rules;
- offline policy;
- export, diagnostic, retention, and deletion policy;
- accessibility-specific labels and alternatives;
- migration and compatibility behavior.

A missing, unknown, incompatible, or unavailable consumer adapter fails closed.

## 6. Canonical proposal envelope

Every durable proposal includes:

- `proposalId`;
- `proposalType`;
- `consumerType`;
- `consumerContractVersion`;
- `campaignId` or another explicit isolation scope where applicable;
- `authorSubjectId`;
- optional `representedActorId` and actor type;
- `subjectType` and `subjectId`;
- typed target scope;
- source and rules summary references;
- structured costs or consequences, when applicable;
- calculated or preview result reference, when applicable;
- proposed Effects or mutations as domain-owned structured data;
- warnings, uncertainty, omitted variables, and required confirmations;
- visibility classification;
- required approval policy reference;
- current proposal state and version;
- `operationId`, `idempotencyKey`, and `correlationId`;
- exact permission, entitlement, policy, pack, schema, and expected-version bindings required by the consumer;
- created, submitted, updated, expired, withdrawn, decided, and committed timestamps as applicable;
- provenance and source references;
- redaction and retention classifications.

Display labels, names, filenames, email addresses, provider IDs, and queue positions are never authoritative identities.

## 7. Proposal lifecycle

Canonical states are:

1. `local-draft`;
2. `saved-draft`;
3. `validation-required`;
4. `ready-to-submit`;
5. `submitting`;
6. `submitted`;
7. `pending-review`;
8. `changes-requested` when the consumer explicitly supports it;
9. `decision-in-progress`;
10. `approved-pending-commit`;
11. `modified-approved-pending-commit`;
12. `denied`;
13. `committed`;
14. `withdrawn`;
15. `expired`;
16. `superseded`;
17. `conflict`;
18. `recovery-required`;
19. `forbidden-or-unavailable`;
20. `commit-failed`.

Only durable server state controls the canonical lifecycle. Local drafts, cached queue entries, realtime messages, notification badges, and optional-AI suggestions are nonauthoritative.

A proposal cannot return from a terminal state to a mutable state. A renewed request creates a new proposal with an explicit predecessor reference.

## 8. Submission validation

Submission revalidates:

- current subject and authentication session;
- isolation scope and selected context;
- author eligibility and represented-actor authority;
- subject existence and lifecycle;
- target existence and visibility;
- consumer adapter and schema compatibility;
- required fields and evidence;
- current permission and entitlement decisions;
- current policy, pack, schema, and feature-flag versions;
- costs, prerequisites, target rules, and domain invariants;
- expected aggregate and proposal versions;
- idempotency and duplicate-submit status;
- expiry and revocation;
- owner-only or irreversible gate requirements;
- warning acknowledgement and confirmation;
- attachment safety and provenance;
- offline prohibition for authoritative submit.

Validation findings are typed as error, warning, information, owner decision, or unavailable. Errors block submit. Warnings require an explicit domain-approved acknowledgement policy and remain in the proposal evidence.

## 9. Reviewer queue and notification contract

A queue entry or notification is a permission-safe projection generated after current authorization and entitlement filtering.

It may include only the minimum fields required for the reviewer to identify priority, domain, proposer-safe label, represented actor when authorized, submission time, expiry, warning severity, and current state.

Counts, badges, sorting, filtering, assignment, reminders, read/unread state, and escalation are projections. They cannot reveal hidden proposal existence, protected author identity, secret target identity, GM-only content, Player-private content, license-sensitive source text, or owner-only reasons.

Assignment is routing metadata, not reviewer authority. A reviewer must reauthorize when opening and deciding.

## 10. Reviewer inspection contract

The inspection shell displays a consumer-provided, permission-safe evidence projection containing, as applicable:

- proposal author and represented actor;
- proposal type and domain purpose;
- source-linked rules or policy summary;
- subject and target scope;
- costs, consequences, or destructive impact;
- deterministic calculation or preview evidence;
- proposed Effects or mutations;
- warnings, uncertainty, omitted variables, conflicts, and owner gates;
- exact relevant versions and receipts;
- prior related decisions or predecessor proposal references;
- permitted decision options;
- modifiable-field allowlist;
- expiry and retention state;
- accessible source links and alternatives.

The inspection shell never sends hidden fields to an unauthorized client merely to conceal them visually.

## 11. Decision vocabulary and receipt

The common reviewer decisions are:

- `approve`;
- `deny`;
- `modify-and-approve`.

A consumer may additionally support `request-changes`, but it is not a final approval and cannot commit domain state.

Every final decision receipt contains:

- `decisionReceiptId`;
- `proposalId` and proposal version;
- consumer and proposal type;
- reviewer subject and active authority reference;
- decision type;
- submitted evidence digest;
- original and final structured proposal digests;
- explicit field-addressed patch for `modify-and-approve`;
- reason code and optional permission-safe explanation;
- warnings acknowledged or introduced;
- permission, entitlement, policy, pack, schema, and expected-version references;
- decision operation ID, idempotency key, and correlation ID;
- decision timestamp;
- commit status and domain result reference when available;
- supersession, expiry, or owner-approval references when applicable;
- redaction and projection classifications.

Decision receipts are immutable and attributable.

## 12. Modify-and-approve safety

Modification is never an unrestricted replacement of the proposal.

The reviewer may change only fields on the consumer's explicit allowlist. Each patch operation names the field, original value digest, final structured value, reason, and reviewer attribution.

The service then:

1. applies the patch to a new final proposal representation;
2. reruns submission and decision validation;
3. recalculates domain previews where required;
4. shows the reviewer the final changed values, resulting costs, Effects, warnings, and consequences;
5. requires final confirmation;
6. creates the immutable decision receipt;
7. invokes the domain commit adapter exactly once.

A modification that changes authority, reviewer identity, isolation scope, subject identity, protected visibility classification, owner-only gate, or nonmodifiable domain invariant is denied and must become a new proposal where permitted.

## 13. Approval policies

The internal-alpha common policies are:

- `single-authorized-reviewer` — used by the F006 GM approval loop;
- `sequential-required-reviewers` — bounded ordered approvals where a domain explicitly requires more than one authority;
- `owner-only` — irreversible, canonical-promotion, release, spending, production credential, or other owner-gated decisions;
- `no-approval-required` — not processed through this framework and therefore cannot masquerade as an approved proposal.

Quorum voting, public voting, marketplace review, and unbounded workflow automation are deferred.

Every policy has explicit reviewer resolution, expiry, revocation, replacement, and partial-decision behavior. A partial approval never grants final authority.

## 14. Atomic commit and domain Event boundary

Approval does not itself mutate domain state. The immutable accepted decision authorizes one invocation of the consumer's domain commit adapter.

The commit adapter revalidates current authority and versions, applies all accepted mutations atomically, emits the domain's durable Event or Events, stores the result reference, and updates the proposal to `committed`.

If commit cannot complete atomically, no partial accepted mutation is presented as success. The proposal enters `commit-failed` or `recovery-required` with preserved decision evidence and status lookup using the original operation ID.

The shared component emits only proposal-orchestration Events. Domain Events remain owned by the consumer.

## 15. Idempotency, concurrency, and ambiguous failure

Every submit, withdraw, decision, request-changes, expiry, supersession, and commit operation has a stable operation identity and expected version.

A duplicate request with the same identity returns the prior receipt or current status. Conflicting reuse fails safely.

A stale proposal or subject version preserves both submitted and current evidence and enters conflict or revalidation state. Silent last-write-wins is prohibited.

After a lost response, the client queries status using the original operation ID before retry. It does not create a new proposal or decision merely because the response was interrupted.

## 16. Realtime, reconnect, revocation, and offline behavior

Realtime messages are advisory. Durable proposal Events, decision receipts, domain Events, and current server projections are authoritative.

Reconnect supplies last acknowledged sequence, proposal and subject versions, outstanding operation IDs, selected context, permission and entitlement hints, and local draft summaries. The service returns current authority, operation statuses, Event-gap plan, proposal state, queue invalidation, and safe recovery choices.

Revocation removes queue and notification projections, ends subscriptions, invalidates cached evidence, prevents decision and status lookup outside current authority, and moves open interfaces to a safe unavailable state.

Offline use may create and edit permitted local proposal drafts and inspect unexpired authorized cached evidence. Offline authoritative submit, decision, approval, denial, modification, commit, owner decision, promotion, deletion, or transfer is prohibited.

## 17. Projection, history, export, diagnostics, and support

Authorization and entitlement filtering occur before proposal discovery, queue counts, notifications, sorting, search, history, exports, diagnostics, optional-AI retrieval, and serialization.

History records durable lifecycle Events, decision receipts, domain result references, patches, reasons, failures, recovery actions, and supersession links. History is role-safe and append-oriented.

Exports preserve stable IDs, consumer versions, proposal evidence digest, decisions, patches, result references, provenance, warnings, redaction decisions, and compatibility metadata.

Diagnostics default to exclude proposal content and protected identities. Issue assignment does not grant proposal or domain-data access. Separate time-bound support authority is required.

## 18. Consumer mapping and nonflattening rule

The initial consumers are:

- F006 live Player Actions;
- GM-controlled NPC and enemy Actions;
- social-play proposals;
- content submission and review;
- optional-AI proposals;
- destructive changes;
- canonical content promotion;
- bounded Asset transfer or custody requests where SS-10 requires acceptance.

The consumer mapping records which common fields and states apply and which domain-specific authority, evidence, modification, commit, history, and owner-gate rules remain outside the shared component.

No consumer may treat the common `approve` value as proof that another domain's mutation is valid.

## 19. Accessibility and responsive behavior

Every proposal state, warning, decision option, patch, confirmation, conflict, recovery choice, and result has text and semantic structure.

Keyboard, touch, screen reader, high zoom, reduced motion, and noncolor presentations preserve the same evidence and authority. Focus moves predictably between notification, queue, inspector, patch review, confirmation, and result.

Tables, diff views, target maps, graphs, and structured Effects have list or linear alternatives. Modify-and-approve presents before/after values and consequences without relying on color. Live-region announcements distinguish advisory updates from authoritative decisions.

Mobile presentation may use a single-focus sequence, but it cannot hide required evidence, warnings, attribution, or final confirmation.

## 20. Security, privacy, cost, and provider boundary

The default authorization decision is deny. Unknown subject, invalid session, missing consumer adapter, stale policy, unavailable authority service, missing entitlement, incompatible schema, expired proposal, revocation, or incomplete evidence fails closed.

Sensitive proposal payloads are encrypted and access-controlled through application-owned ports. Raw credentials, secret tokens, unrestricted source text, hidden Player or GM fields, and unrelated Campaign data are prohibited.

The core path requires zero AI and zero paid queue, notification, workflow, identity, analytics, ticketing, or realtime provider. Local deterministic adapters support development and CI.

Provider SDKs remain behind adapters. Provider subject IDs, queue IDs, workflow IDs, or notification IDs never become domain authority.

## 21. Deterministic fixture and test contract

The contract defines deterministic fixtures for:

- ordinary approve;
- ordinary deny;
- valid modify-and-approve;
- forbidden field modification;
- request changes and resubmission;
- duplicate submit;
- duplicate decision;
- stale proposal version;
- lost decision response with status recovery;
- reviewer revocation after notification;
- hidden proposal nonenumeration;
- owner-only proposal blocked for nonowner;
- commit failure without partial mutation;
- offline draft with authoritative submit denied;
- reconnect with missed queue and decision Events;
- consumer adapter unavailable.

Fixtures use synthetic, noncanonical data unless a separate source-backed selector is explicitly named.

## 22. Integrated acceptance criteria

- **PAC-AC-001:** The common component never becomes domain authority.
- **PAC-AC-002:** Every consumer registers a versioned adapter and fails closed when it is unavailable or incompatible.
- **PAC-AC-003:** Proposal authorship, represented actor, subject, reviewer, observer, and service actor remain separate.
- **PAC-AC-004:** Proposal identities, versions, operation IDs, and correlation IDs are stable and provider-neutral.
- **PAC-AC-005:** Queue and notification assignment never implies reviewer authority.
- **PAC-AC-006:** Reviewer inspection is server-generated and permission-safe.
- **PAC-AC-007:** Approve, deny, and modify-and-approve create immutable attributable receipts.
- **PAC-AC-008:** Modification is field-addressed, allowlisted, revalidated, recalculated where required, and finally confirmed.
- **PAC-AC-009:** Owner-only and irreversible decisions cannot be downgraded to ordinary reviewer approval.
- **PAC-AC-010:** Accepted decisions invoke exactly one domain commit adapter and never partially present success.
- **PAC-AC-011:** Domain Events remain owned by the consumer and proposal Events remain orchestration evidence.
- **PAC-AC-012:** Duplicate operations are idempotent and conflicting identity reuse fails safely.
- **PAC-AC-013:** Stale versions preserve conflict evidence and silent last-write-wins is prohibited.
- **PAC-AC-014:** Ambiguous failure uses original-operation status lookup before retry.
- **PAC-AC-015:** Realtime is advisory and reconnect restores durable state from Events and projections.
- **PAC-AC-016:** Revocation invalidates queues, notifications, caches, subscriptions, decisions, and unauthorized status lookup.
- **PAC-AC-017:** Offline authoritative submit, decision, commit, promotion, deletion, and transfer are prohibited.
- **PAC-AC-018:** History, export, diagnostics, support, and optional-AI projections are independently permission-safe.
- **PAC-AC-019:** Accessibility and responsive layouts preserve evidence, authority, warnings, patches, confirmations, and recovery choices.
- **PAC-AC-020:** Deterministic fixtures cover approval, denial, modification, duplication, conflict, revocation, hidden existence, owner gate, failure, offline, reconnect, and adapter unavailability.

## 23. Implementation ordering and handoff

Dependency-safe slices are:

1. common envelope, state vocabulary, IDs, and adapter registry;
2. authority resolver, permission-safe projection, and nonenumeration;
3. submit validation, idempotency, and status lookup;
4. queue, notification, assignment, and inspection shell;
5. approve, deny, modify-and-approve, request-changes, and receipts;
6. domain commit adapter and proposal/domain Event boundary;
7. history, exports, diagnostics, support, and optional-AI projections;
8. reconnect, revocation, offline, conflict, expiry, withdrawal, and supersession;
9. accessibility and responsive parity;
10. deterministic fixtures and consumer conformance harness.

Implementation remains dependency-gated by P9-06 and concrete shared-foundation services.

## 24. Readiness decision and next action

The shared-component design is complete when its matrix, consumer mapping, traceability, deterministic validator, review receipt, readiness record, completion record, CI, and repository merge evidence all pass with zero blocking findings.

The exact next design item after verified completion is **IA-D04-003 — Two-Device Interruption and Reconnect Matrix**.

Silence is not approval. No implementation activation, paid service, production credential, real-user data collection, internal-alpha release, production deployment, or public release is authorized.
