# IA-D04-002 — Proposal and Approval Shared-Component Contract

**Program:** MV-IA-001  
**Work item:** IA-D04-002  
**Version:** 0.1.0  
**Status:** implementation-ready design  
**Owner and final authority:** John Brandon Turner  
**Date:** 2026-08-06  
**Companion matrix:** `IA-D04-002_PROPOSAL_APPROVAL_COMPONENT_MATRIX.json`

## 1. Purpose

This contract extracts the proposal, inspection, decision, receipt, notification, history, and recovery model proven by MV-IA-F006 into one reusable shared component.

The component supports live Player Actions, GM-controlled NPC and enemy Actions, social outcomes, content submissions, optional AI suggestions, destructive changes, and canonical-promotion requests without allowing any consumer to widen authority or bypass its domain rules.

## 2. Governing sources and precedence

Precedence is:

1. owner decisions and active Phase 9 architecture;
2. IA-D02-006 shared-foundation contracts;
3. IA-D03-005 Character/Campaign preparation contracts;
4. MV-IA-F006 and its Action/approval matrix;
5. shared systems SS-06, SS-07, SS-08, SS-11, SS-12, SS-13, SS-14, SS-15, SS-16, SS-18, and SS-19;
6. consumer-specific extension profiles.

A consumer may narrow the component. It may not bypass authentication, authorization, entitlement, expected versions, idempotency, final confirmation, attribution, durable Events, or server-side projection.

## 3. Component boundary

The shared component owns:

- proposal envelope and immutable original evidence;
- validation finding presentation;
- permission-safe queue item and notification;
- inspection layout and source/rules evidence slots;
- approve, deny, and modify-and-approve controls;
- field-addressed modification diff;
- final confirmation;
- decision receipt;
- status lookup and ambiguous-failure recovery;
- role-safe history and projection contracts.

The consumer owns domain calculation, domain validation, permitted modification classes, authoritative commit adapter, domain Events, and domain-specific projection content.

## 4. Required consumer profile

Every consumer registers an exact versioned profile containing:

- `consumerType` and `consumerVersion`;
- proposal type and aggregate scope;
- proposer roles and actor-control rules;
- decision-maker roles and delegation rules;
- required evidence slots;
- allowed target types;
- allowed modification paths;
- denial reason codes;
- domain validator and commit adapter identifiers;
- projection policies;
- retention, export, diagnostic, and accessibility requirements.

An unknown, expired, incompatible, or widened profile is rejected.

## 5. Stable identities

Stable identities include:

- `proposalId`;
- `proposalVersion`;
- `operationId`;
- `consumerProfileId` and version;
- `subjectId`;
- `workspaceId` or `campaignId`;
- aggregate and actor IDs;
- target IDs;
- `decisionId`;
- `eventId`;
- `correlationId`.

Names, labels, provider IDs, filenames, queue positions, and UI selections never replace stable IDs.

## 6. Canonical proposal envelope

The proposal envelope contains:

- identity and consumer profile;
- proposer and active role;
- actor or aggregate context;
- source and rules evidence;
- targets and expected versions;
- costs, requirements, roll or calculation evidence where applicable;
- proposed result and Effects;
- warnings and validation findings;
- permission, entitlement, policy, pack, schema, and expected aggregate versions;
- timestamps, expiry, idempotency, and correlation data.

The original accepted proposal is immutable. Later decisions reference it and preserve all changes separately.

## 7. Evidence-slot contract

Standard evidence slots are:

- proposer;
- actor or affected aggregate;
- proposal type;
- source and rules summary;
- targets;
- costs;
- requirements;
- roll, seed, or calculation evidence;
- ordered modifiers;
- computed or proposed result;
- proposed Effects or mutations;
- warnings;
- versions and authority findings;
- attachments or source links where permitted.

A consumer can mark a slot required, optional, not applicable, or hidden-by-policy. It cannot relabel hidden information as absent.

## 8. State vocabulary

Canonical component states are:

1. `draft`;
2. `validating`;
3. `validation-failed`;
4. `ready-to-submit`;
5. `submitted`;
6. `pending-decision`;
7. `decision-in-review`;
8. `approved`;
9. `modified-and-approved`;
10. `denied`;
11. `commit-pending`;
12. `completed`;
13. `stale`;
14. `revoked`;
15. `recovery-required`.

Only durable accepted Events and current server projections are authoritative.

## 9. Proposal summary component

The summary presents the smallest complete decision context, not merely a title and buttons. It shows all required authorized evidence slots, warnings, current versions, stale or revoked state, and a source/rules inspection action.

Collapsed and mobile views preserve the same decision evidence and do not hide warnings or modification differences behind inaccessible interactions.

## 10. Queue and notification component

Queue entries and counts are filtered before counting, grouping, ranking, or delivery. Unauthorized users do not learn that a protected proposal exists.

A notification identifies the consumer, actor or aggregate, proposal type, urgency where governed, current status, and safe navigation target. It does not itself grant review or decision authority.

## 11. Review claim and concurrency

A review claim is advisory coordination. It may expire or be released. It does not make a decision and does not prevent an authorized server-side conflict check.

Only one final decision may win. Competing or stale decisions return the current status and preserve evidence. Silent last-write-wins is prohibited.

## 12. Approve, deny, and modify-and-approve

Final decision types are exactly:

- `approve`;
- `deny`;
- `modify-and-approve`.

Approve accepts the reviewed values after final revalidation.

Deny records an attributable reason code and user-safe explanation and commits no accepted mutation.

Modify-and-approve preserves the original proposal, records every changed path, original and final values, reasons, decider identity, active role or delegation, and the final revalidation result.

Silence is not approval.

## 13. Modification-path contract

Allowed changes are declared by exact field paths and modification classes. Wildcard mutation of the proposal body is prohibited.

The component renders a semantic diff with:

- changed field label;
- original value;
- final value;
- reason;
- downstream recalculation or revalidation impact;
- protected-field treatment.

A consumer must reject modifications outside its versioned profile.

## 14. Final confirmation and decision receipt

Final confirmation repeats decision type, affected aggregate, final result, accepted mutations, warnings, and any changed fields.

The durable receipt contains proposal and decision IDs, consumer profile, decider attribution, role or delegation, reviewed versions, final values, modification reasons, denial reason where applicable, permission and entitlement references, commit status, timestamp, and correlation identity.

## 15. Domain validation and commit adapter

The shared component never invents domain rules. It invokes the registered validator with the immutable proposal, proposed decision, current authority, and current aggregate versions.

The commit adapter must be atomic for the consumer's accepted state. A successful UI decision without a durable accepted domain Event is not complete.

## 16. Permission-safe projections

Server-side projection occurs before serialization for proposer, decision-maker, observer, notification, history, export, diagnostics, and optional AI surfaces.

Protected fields are omitted or replaced with governed user-safe findings. Counts, ordering, search, autocomplete, badges, and error wording cannot reveal protected existence.

## 17. Idempotency and status lookup

Submit, claim, release, decision, confirmation, commit, acknowledgement, and recovery commands use stable operation identities.

If a response is lost, the client queries status with the original identity before retrying. Compatible repeats return prior status; conflicting reuse fails safely.

## 18. Reconnect, revocation, and recovery

Reconnect carries acknowledged Event sequence, current aggregate version, outstanding proposal and decision IDs, profile and protocol versions, and correlation identity.

The service returns current authority, proposal and decision status, Event-gap plan, current role-safe projection, queue status where authorized, and user-safe recovery choices.

Revocation invalidates routes, subscriptions, review claims, protected caches, queue entries, status lookup outside current authority, exports, diagnostics, and optional AI projections.

## 19. Accessibility and responsive behavior

Every proposal, warning, evidence slot, decision option, modification, confirmation, and status has a semantic name and noncolor state.

Keyboard, touch, screen-reader, high-zoom, reduced-motion, and mobile users can complete the same decision. Ordered calculations and diffs have text or table alternatives. Focus returns predictably after inspection, decision, conflict, reconnect, and completion.

## 20. History, export, diagnostics, and AI

History is attributable and role-safe. It preserves enough evidence to explain the accepted result without exposing unrelated protected state.

Exports and diagnostics use the same projection policy and exclude credentials, unrestricted source text, hidden notes, and private fields by default.

AI is optional and proposal-only or read-only. It receives a narrowed authorized projection and has no approve, deny, modify, commit, or canonical-promotion authority.

## 21. Extension profiles

Initial governed extension profiles are:

- live Player Action;
- GM NPC or enemy Action;
- social outcome;
- content submission;
- optional AI suggestion;
- destructive change;
- canonical-promotion request.

Each profile must map its domain fields into standard evidence slots and define exact authority, allowed modifications, validation, commit, Events, projections, retention, and tests.

## 22. Implementation slices

1. component schemas, IDs, profile registry, and ports;
2. proposal summary, evidence slots, source/rules inspector, and findings;
3. queue, notifications, review claim, and concurrency;
4. approve, deny, modification diff, and final confirmation;
5. decision receipt, domain validator, and atomic commit adapter;
6. role-safe projections, history, export, diagnostics, and AI boundary;
7. idempotency, status lookup, reconnect, revocation, and recovery;
8. responsive accessibility, deterministic fixtures, and zero-service adapters.

## 23. Blocking acceptance criteria

- `PAC-AC-001` — consumer profiles are versioned and cannot widen shared authority.
- `PAC-AC-002` — original proposals remain immutable.
- `PAC-AC-003` — required evidence slots are complete and permission-safe.
- `PAC-AC-004` — queue counts and notifications do not leak protected existence.
- `PAC-AC-005` — review claims remain advisory.
- `PAC-AC-006` — only approve, deny, and modify-and-approve are final decisions.
- `PAC-AC-007` — silence is never approval.
- `PAC-AC-008` — modification paths are explicit and profile-bound.
- `PAC-AC-009` — semantic diffs preserve original and final values and reasons.
- `PAC-AC-010` — final authority and versions are revalidated.
- `PAC-AC-011` — durable receipts are attributable.
- `PAC-AC-012` — domain commits are atomic and Event-backed.
- `PAC-AC-013` — server-side projections precede serialization.
- `PAC-AC-014` — duplicate commands cannot duplicate accepted mutations.
- `PAC-AC-015` — ambiguous failures recover through status lookup.
- `PAC-AC-016` — reconnect and Event-gap recovery preserve one outcome.
- `PAC-AC-017` — revocation clears protected access and caches.
- `PAC-AC-018` — responsive and accessible paths preserve all evidence and controls.
- `PAC-AC-019` — exports, diagnostics, and AI reuse the same permission boundary.
- `PAC-AC-020` — the component operates with zero paid services and zero AI.

## 24. Readiness decision and next action

**Decision:** READY FOR IMPLEMENTATION HANDOFF — DEPENDENCY GATED.

The component is reusable without becoming a universal authority engine. Consumer-specific rules and commit adapters remain explicit and versioned.

Implementation remains dependency-gated by P9-06 and the concrete shared foundations. No paid service, production credential, real-user data collection, internal-alpha release, production deployment, public release, AI authority, or canonical promotion is authorized.

**Next:** IA-D04-003 — Two-Device Interruption and Reconnect Matrix.
