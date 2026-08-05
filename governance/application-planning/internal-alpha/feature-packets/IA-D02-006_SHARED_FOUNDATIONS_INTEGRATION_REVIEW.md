# IA-D02-006 — Shared-Foundations Integration Review

**Program:** MV-IA-001  
**Review ID:** IA-D02-006  
**Version:** 0.1.0  
**Status:** COMPLETE — DESIGN INTEGRATION REVIEW  
**Owner and final authority:** John Brandon Turner  
**Date:** 2026-08-05  
**Reviewed packets:** MV-IA-F002, MV-IA-F020, MV-IA-F003, MV-IA-F021, MV-IA-F025  
**Companion matrix:** `IA-D02-006_SHARED_FOUNDATIONS_CONTRACT_MATRIX.json`

## 1. Purpose

This review closes Tranche IA-D02 by proving that the completed shared-foundation packets form one coherent implementation contract rather than five parallel specifications.

The review covers:

- Universal Object Experience;
- Permissions and Hidden Information;
- Identity, Dashboard, and Workspace Selection;
- Autosave, Reconnect, Recovery, and Bounded Offline Use;
- Onboarding, Help, Diagnostics, and Issue Reporting.

The result is a normalized contract baseline for every later Character, Campaign, Scene, Session, relationship, social, investigation, combat, inventory, vehicle, World, creator, and optional AI packet.

This document is an integration review. It does not authorize application code, paid services, production credentials, collection of real tester diagnostics, internal-alpha release, production deployment, or public release.

## 2. Review method

The review compared the five packets and their machine-readable companion matrices across eleven dimensions:

1. identity and actor classification;
2. role, membership, delegation, control, ownership, and entitlement;
3. workspace discovery, entry, selected context, and deep links;
4. object search, inspection, relationships, comparison, and selection;
5. authorization, projection, non-disclosure, counts, and inference safety;
6. local drafts, authoritative saves, commands, Events, projections, and receipts;
7. interruption, ambiguous failure, reconnect, conflict, revocation, and offline behavior;
8. onboarding, help, known limitations, release identity, diagnostics, issues, and support access;
9. responsive and accessible state behavior;
10. provider-neutral architecture, local deterministic adapters, cost, and provider exit;
11. downstream handoff and validation obligations.

A conflict is blocking when two packets would permit different authority, expose different protected information, create incompatible state transitions, or require mutually exclusive persisted field meanings. A naming difference is nonblocking only when this review provides one canonical value and a bounded compatibility alias.

## 3. Governing precedence

When the reviewed packets overlap, the following precedence applies:

1. owner decisions and active Phase 9 architecture;
2. MV-IA-F020 for authorization, visibility, inference safety, support-access authority, and protected projection;
3. MV-IA-F003 for stable subject identity, authentication session, membership, role, workspace discovery, entry, and selected-context receipts;
4. MV-IA-F021 for local versus authoritative state, idempotency, status lookup, realtime recovery, conflict, checkpoint, and offline behavior;
5. MV-IA-F002 for object browse, inspection, provenance, relationship traversal, comparison, picker constraints, and selection receipts;
6. MV-IA-F025 for onboarding, contextual help, release identity, diagnostic manifests, issue intake, attachments, receipts, and follow-up.

A lower-precedence packet may narrow behavior for its own domain. It may not widen authority, weaken projection safety, turn convenience state into authority, or create an implicit support-access path.

## 4. Canonical actor and role model

The canonical persisted role IDs are:

- `invited-tester`;
- `player`;
- `game-master`;
- `assistant-gm`;
- `content-creator`;
- `observer`;
- `owner-admin`;
- `service-actor`.

Display labels such as “Game Master,” “GM,” “Owner/Admin,” and localized equivalents are presentation values. They are not alternate persisted identities.

AI is not a user role. AI is an optional assistive service actor that:

- has no independent Campaign membership;
- has no Character control;
- has no ownership, custody, entitlement, delegation, or support authority;
- receives only the initiating subject’s already-authorized projection, narrowed again by AI policy;
- cannot expand a query, follow a hidden relationship, retrieve a private issue, or execute a mutation merely because a prompt requests it;
- is unnecessary for the core internal-alpha path.

Authentication, Campaign membership, role assignment, Character control, ownership, custody, entitlement, invitation state, selected context, and support access remain separate decisions.

## 5. Canonical identity and context contract

The stable identity key is `subjectId`. Provider subject IDs, email addresses, display names, usernames, device labels, and current roles never replace it in domain records.

The canonical selected-context contract uses:

- `selectedContextReceiptId`;
- `subjectId`;
- `authenticationSessionId`;
- `workspaceType`;
- `workspaceId`;
- `activeRole`;
- optional `campaignId`, `characterId`, `sceneId`, and `sessionId`;
- `permissionDecisionReference`;
- `entitlementDecisionReference`;
- `permissionVersion`;
- `entitlementVersion`;
- `issuedAt`;
- `expiresAt`;
- `correlationId`.

The selected-context receipt is a navigation and recovery aid. It is nonauthoritative. Every protected route and every protected mutation revalidates the current subject, session, role, membership, delegation, control, permission, entitlement, object lifecycle, pack state, and expected version.

Compatibility aliases are normalized at service boundaries:

- `permissionsVersion` → `permissionVersion`;
- `entitlementRulesetVersion` → `entitlementVersion`;
- `gameSessionId` → `sessionId`;
- `gm` → `game-master`.

No downstream packet may create another alias without recording migration and compatibility behavior.

## 6. Canonical workspace model

The canonical workspace types are:

- `player-dashboard`;
- `gm-dashboard`;
- `campaign`;
- `character`;
- `scene`;
- `game-session`;
- `creator-draft`;
- `observer-session`;
- `owner-admin-operations`.

“Session” remains the user-facing display term. `game-session` is the stable workspace type and `sessionId` is the stable identifier.

Workspace discovery and workspace entry are separate authorization decisions. Dashboard cards, recent work, notification counts, pending approval counts, autocomplete, deep-link resolution, media, labels, timestamps, and route availability are all protected projections. An unauthorized subject must not learn that a protected workspace exists.

## 7. Authorization and projection contract

The default decision is deny.

Unknown subject, invalid session, missing role, expired delegation, missing control, entitlement failure, unavailable pack, stale policy, invalid cursor, revocation, unavailable authorization service, and incomplete decision inputs fail closed.

Authorization and entitlement filtering occur before:

- ranking;
- pagination;
- facets;
- counts;
- autocomplete;
- suggestions;
- relationship traversal;
- comparison candidates;
- notifications;
- queue totals;
- activity summaries;
- exports;
- diagnostics;
- AI retrieval;
- serialization.

Protected fields are removed on the server before ordinary client delivery. A client must not receive GM truth, Player-private notes, unrevealed clues, secret motives, hidden object names, inaccessible provenance, unrelated Campaign labels, restricted issue contents, or raw authorization internals and merely hide them.

When a precise denial would disclose protected existence, the user-safe result is the approved not-found-or-unavailable family. Internal reason codes remain available to authorized operational evidence without being exposed as an inference channel.

## 8. Universal object integration

MV-IA-F002 controls the reusable object browse, inspector, provenance, relationship, comparison, and picker behavior.

Every downstream caller supplies typed constraints and current context. The object service returns only authorized, entitled, pack-compatible, lifecycle-compatible, and caller-compatible projections.

A selection receipt includes stable object identity, resolved version or compatibility policy, caller context, warnings, operation identity, and current decision references. The receipt does not mutate the caller.

The caller must separately validate:

- domain-specific prerequisites;
- Campaign and rules-profile compatibility;
- current role and control;
- costs and Resources;
- placement or instance rules;
- expected version;
- pack lock and schema;
- approval requirements;
- idempotency.

Display names, filenames, aliases, and provider identifiers are never authoritative references.

## 9. State and authority model

The integrated state model distinguishes:

1. local draft;
2. local autosave receipt;
3. queued intent;
4. submitted request or command;
5. received or processing state;
6. durable pending-GM proposal;
7. accepted or modified-and-accepted Event;
8. rejected Event or receipt;
9. current server projection;
10. stale, conflict, forbidden, restricted, or recovery-required state.

Only accepted durable Events, authoritative persistence records, and current server projections control product state.

The following are nonauthoritative:

- local drafts;
- local autosave receipts;
- caches;
- selected-context receipts;
- realtime messages;
- pending client requests;
- offline snapshots;
- diagnostic previews;
- issue drafts;
- AI output.

Authoritative mutation requires current authorization, current entitlement where applicable, valid pack and schema state, expected version, idempotency, and an online authoritative service.

## 10. Idempotency and ambiguous failure

Every mutable operation defines a stable operation or command identity.

When a response is lost, the client does not create a new command immediately. It queries status using the original operation or command ID.

This rule applies to:

- authoritative saves;
- invitation acceptance;
- role or control mutation;
- Session commands;
- GM decisions;
- issue submission;
- attachment finalization;
- checkpoint or recovery operations.

A duplicate retry with the same identity returns the prior result or current status. A conflicting reuse fails safely.

## 11. Realtime, reconnect, conflict, and revocation

Realtime delivery is advisory. Ordered durable Events and current server projections are authoritative.

Reconnect supplies the last acknowledged sequence, current projection version, selected-context receipt, outstanding command IDs, local draft summaries, permission and entitlement hints, schema versions, pack lock, client version, protocol version, and correlation ID.

The service returns:

- resolved subject and context;
- current authorization and entitlement decisions;
- command statuses;
- Event-gap plan;
- current sequence and projection;
- draft reconciliation plan;
- cache invalidation directives;
- offline snapshot state;
- user-safe messages.

Conflict resolution preserves both local and authoritative state. Silent last-write-wins is prohibited.

Revocation ends affected subscriptions, invalidates context receipts, removes protected dashboard and recent-work projections, clears or partitions protected caches, blocks status lookup outside current authority, and transitions open interfaces to a safe revoked state.

## 12. Bounded offline contract

Offline behavior is manifest-bound.

Permitted offline behavior may include:

- reading unexpired authorized projections named by the manifest;
- searching within an authorized local index;
- inspecting cached source-safe fields;
- creating and editing approved local draft types;
- viewing local draft history;
- preparing a nonauthoritative proposal.

Offline behavior may not:

- perform an authoritative save;
- accept a Session command;
- commit a GM approval;
- transfer ownership or Character control;
- change membership, role, permission, or entitlement;
- install, update, migrate, or remove packs;
- promote canonical content;
- perform checkpoint restore;
- create provider-exit exports;
- claim that local state is authoritative.

Reconnect revalidates subject, context, permissions, entitlement, pack lock, schema, lifecycle, versions, and revocation before any local work can be submitted.

## 13. Onboarding, help, diagnostics, and issue integration

Onboarding binds the tester to:

- exact release identity;
- approved role;
- permitted workspace;
- supported journey;
- known limitations;
- issue-reporting path.

Contextual help uses the same permission-safe route, role, selected context, object, and state projections as the product. Help search must not disclose hidden features, Campaigns, objects, roles, issues, or limitations scoped to another cohort.

Diagnostic generation defaults to exclude. The diagnostic manifest uses allowlisted fields, privacy-safe IDs, user-safe reason codes, bounded timings, safe sequence and version metadata, and explicit exclusions.

Redaction occurs before preview. The reporter explicitly selects attachments and can remove them before submission. Screenshots are never captured automatically. Attachments are classified, quarantined, checksummed, report-bound, scope-bound, and subject to revocation and expiry.

An issue report does not grant support access. Assignment, ownership, duplicate linkage, status, and follow-up do not authorize Campaign, Character, Scene, Session, Player-private, GM-only, secret, or credential access.

Protected support access requires a separate record with purpose, subject, Campaign, fields, duration, approval, attribution, and automatic expiry.

## 14. Accessibility and responsive integration

Every shared-foundation state must have equivalent behavior across desktop, tablet, mobile, keyboard, touch, screen reader, high zoom, reduced motion, and noncolor presentation.

Layout may change, but these may not change:

- authority;
- available evidence;
- denial meaning;
- state transition;
- recovery options;
- required confirmation;
- attachment consent;
- support-access boundary;
- acceptance result.

Graphs, relationship diagrams, and multi-panel layouts require list, table, or single-focus alternatives. Focus returns predictably after inspector close, route denial, reconnect, conflict resolution, and issue submission.

## 15. Provider-neutral and cost boundary

The integrated design consumes application-owned or provider-neutral ports for identity, entitlement, persistence, authorization, Session command, realtime, checkpoint, object storage, telemetry, diagnostics, issue intake, notification, search, and export.

Provider SDKs and provider subject IDs remain inside adapters.

Local deterministic adapters are required for development and CI.

The core path requires:

- zero paid identity provider;
- zero paid search provider;
- zero paid analytics provider;
- zero paid crash-reporting provider;
- zero paid ticketing provider;
- zero paid notification provider;
- zero AI.

Optional providers may be evaluated only through later owner-approved gates. No reviewed packet authorizes spending or irreversible provider coupling.

## 16. Resolved integration findings

### SFI-F001 — Role identifiers

**Disposition:** resolved.

Persisted role IDs use lowercase hyphenated values. Display labels remain presentation.

### SFI-F002 — AI classification

**Disposition:** resolved.

AI is an optional assistive service actor, not a user role or source of independent authority.

### SFI-F003 — Permission version field

**Disposition:** resolved.

`permissionVersion` is canonical. `permissionsVersion` is a compatibility alias normalized at the boundary.

### SFI-F004 — Entitlement version field

**Disposition:** resolved.

`entitlementVersion` is canonical. `entitlementRulesetVersion` is a compatibility alias normalized at the boundary.

### SFI-F005 — Session naming

**Disposition:** resolved.

`game-session` is the canonical workspace type, `sessionId` is the identifier, and “Session” is a display label.

### SFI-F006 — Support authority

**Disposition:** resolved.

Issue assignment and support workflow state never imply protected product-data access.

### SFI-F007 — State authority

**Disposition:** resolved.

Client convenience state remains nonauthoritative.

### SFI-F008 — Service dependency

**Disposition:** resolved.

All reviewed foundations retain local deterministic and zero-paid-service operation.

No blocking integration finding remains open.

## 17. Downstream packet obligations

Every packet beginning with IA-D03 must:

- name the shared-foundation contract IDs it consumes;
- use the canonical role and field values from the companion matrix;
- define stable IDs and distinguish Definition, placement, instance, Event, projection, and index where applicable;
- define authorization before counts, suggestions, relationships, and serialization;
- define local draft, authoritative save, submitted command, accepted Event, and current projection separately;
- define expected-version and idempotency behavior;
- define status lookup after ambiguous failure;
- define revocation effects on routes, caches, drafts, subscriptions, and notifications;
- define bounded offline behavior and explicitly prohibit offline authoritative mutation;
- define role-safe diagnostics, issue evidence, and support-access separation;
- define equivalent responsive and accessible behavior;
- define zero-service fallback and provider-neutral adapters;
- record dependencies, owner gates, implementation holds, tests, and acceptance evidence.

A downstream packet may extend a shared contract only by recording affected consumers, compatibility impact, migration impact, retest list, fallback, and documentation update.

## 18. Integrated acceptance criteria

- **SFI-AC-001:** The review identifies the five controlling packets and governing precedence.
- **SFI-AC-002:** Stable subject identity is independent of provider identity and current role.
- **SFI-AC-003:** Membership, role, control, ownership, entitlement, delegation, and support access remain separate.
- **SFI-AC-004:** Selected-context receipts are nonauthoritative and revalidated.
- **SFI-AC-005:** Unknown, stale, incomplete, or unavailable authorization fails closed.
- **SFI-AC-006:** Protected fields, counts, labels, relationships, and payloads are filtered before client delivery.
- **SFI-AC-007:** Object selection returns stable identity and requires caller validation before mutation.
- **SFI-AC-008:** Local drafts, requests, Events, and projections have distinct authority.
- **SFI-AC-009:** Mutable operations are idempotent and support status lookup after ambiguous failure.
- **SFI-AC-010:** Realtime is advisory and Event-gap recovery returns current authoritative projection.
- **SFI-AC-011:** Revocation invalidates affected context, subscriptions, projections, and caches.
- **SFI-AC-012:** Offline operation is manifest-bound and cannot perform authoritative mutation.
- **SFI-AC-013:** Diagnostics default to exclude and require allowlisting, redaction, preview, and consent.
- **SFI-AC-014:** Issue reporting never grants support access.
- **SFI-AC-015:** Attachments require explicit selection, quarantine, checksum, scoped retrieval, and revocation handling.
- **SFI-AC-016:** All shared states have equivalent responsive and accessible behavior.
- **SFI-AC-017:** Canonical fields and compatibility aliases are machine-readable and bounded.
- **SFI-AC-018:** Later packets must declare and test consumed shared contracts.
- **SFI-AC-019:** The integrated core path requires no paid service and no AI.
- **SFI-AC-020:** No blocking integration finding remains, while implementation and release remain unauthorized.

## 19. Readiness decision

**Decision: PASS — SHARED-FOUNDATION DESIGN INTEGRATION COMPLETE.**

The five shared-foundation packets agree after the bounded compatibility resolutions recorded here and in the companion matrix.

This decision means:

- Tranche IA-D02 is complete at design level;
- later packets have one shared contract baseline;
- naming and field aliases have a canonical normalization rule;
- no blocking authority, visibility, persistence, recovery, support, accessibility, provider, or cost contradiction remains.

This decision does not mean:

- application implementation has begun;
- P9-06 dependencies are bypassed;
- any provider has been activated;
- real tester diagnostics may be collected;
- internal alpha may be released;
- production or public release is approved.

Silence is not approval.

## 20. Next executable item

**IA-D03-001 — Design MV-IA-F004, Character Creation and Advancement.**

F004 is next because Character creation is the first major domain packet that consumes the complete shared-foundation baseline: identity and selected context, permission-safe object discovery, stable-ID selection, entitlement, local drafts, authoritative saves, recovery, onboarding, help, diagnostics, and issue reporting.
