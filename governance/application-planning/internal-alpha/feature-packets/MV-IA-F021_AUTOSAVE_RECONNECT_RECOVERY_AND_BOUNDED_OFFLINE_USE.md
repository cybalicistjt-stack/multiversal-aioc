# MV-IA-F021 — Autosave, Reconnect, Recovery, and Bounded Offline Use

**Feature ID:** MV-IA-F021  
**Feature version:** 0.1.0  
**Classification:** entry-critical  
**Design status:** implementation-ready  
**Owner:** John Brandon Turner  
**Primary roles:** Player, Game Master, Assistant GM, Content Creator, Observer, Owner/Admin, invited tester, service actor  
**Stage A mapping:** A6/A12 — First Playable Action, Internal-Alpha Hardening, and recovery foundations  
**Historical module mapping:** Offline Play and Synchronization  
**Prepared by:** Lead Documentation Architect / Reliability and Session-Recovery Steward  
**Reviewed by:** architecture, security, privacy, QA, UX/accessibility, data, identity, realtime, persistence, and documentation roles required before implementation  
**Date:** 2026-08-05

## 1. Problem and user outcome

### Problem

Multiversal must survive ordinary interruption without losing drafts, duplicating accepted effects, restoring hidden or revoked data, or asking the user to guess whether an action was accepted.

The primary internal-alpha journey spans identity, Campaign and role selection, Character and Scene state, Action proposals, GM decisions, authoritative Events, notifications, and multiple devices. Interruptions may occur:

- while editing a local draft;
- during an authoritative save;
- after a command leaves the client but before its result is displayed;
- while a proposal awaits GM action;
- after an Event commits but before a client receives it;
- after a role, invitation, permission, entitlement, or Character-control change;
- while a device uses a bounded offline snapshot;
- during service restart, restore, migration, or Session recovery.

A generic “save frequently” approach is not enough. Local autosave, authoritative persistence, command submission, Event acceptance, realtime delivery, checkpoints, backup/restore, and provider-exit exports are different operations with different evidence and safety rules.

### Required outcome

An approved internal-alpha user can reload, temporarily disconnect, reconnect, change devices, or resume after service restart and understand:

- what remains only a local draft;
- what was durably saved;
- what was submitted;
- whether a submitted command was accepted, rejected, modified, or still pending;
- which authoritative Event sequence is current;
- whether a conflict or permission change requires review;
- which offline information is cached and when it expires;
- which actions remain unavailable offline.

The system recovers the newest authorized state without applying an accepted business effect twice. It revalidates identity, selected context, permissions, entitlements, pack versions, schema versions, and object lifecycle before restoring sensitive state or permitting mutation.

### Why this belongs in internal alpha

This feature is entry-critical because every primary Player and GM journey depends on trustworthy continuity. Internal alpha cannot safely test the first playable loop when a disconnect can duplicate damage, lose a GM decision, expose a revoked workspace, or leave users uncertain about whether an action happened.

The alpha slice intentionally proves bounded recovery. It enforces **no offline authoritative mutation** and does not promise broad offline authoritative play or conflict-free multi-master synchronization.

## 2. Alpha slice

### Included

- local draft autosave for approved forms and proposals;
- explicit distinction among local draft, authoritative save, submitted command, accepted Event, and displayed projection;
- save receipts and stable client operation IDs;
- idempotent authoritative mutations;
- optimistic concurrency with expected versions;
- command-status lookup after ambiguous network failure;
- missed-Event recovery from the last acknowledged sequence;
- role-safe reconnect to Campaign and Session projections;
- selected-context revalidation after reload or reconnect;
- recovery after service restart from durable persistence and verified checkpoints;
- pending GM proposal and decision recovery;
- duplicate-tab and second-device detection;
- user-visible stale, conflict, revoked, expired, and recovery-required states;
- bounded read-only offline snapshots for approved content and workspace projections;
- bounded offline local drafts that are never represented as accepted state;
- reconnect reconciliation for offline drafts;
- permission, entitlement, pack, schema, and lifecycle revalidation before restore;
- privacy-safe recovery diagnostics and issue-report receipts;
- deterministic interruption and failure-injection fixtures;
- desktop, tablet, mobile, keyboard, touch, and screen-reader recovery behavior.

### Explicitly excluded

- broad offline authoritative gameplay;
- peer-to-peer authoritative synchronization;
- automatic last-write-wins for governed state;
- silent merging of conflicting Character, Scene, inventory, or Session changes;
- offline GM approval or acceptance represented as committed;
- client-generated authoritative Event sequence;
- restoration of revoked or hidden fields from cache;
- indefinite offline entitlement;
- restoring a Session from an unverified local snapshot;
- automatic destructive rollback of accepted Events;
- production disaster-recovery operations;
- provider-specific synchronization APIs as domain contracts;
- public multi-region active-active conflict resolution;
- paid synchronization, notification, or storage services;
- production credentials or production deployment.

### Full long-term scope deferred

Later work may add larger offline content libraries, richer draft collaboration, selective offline Campaign preparation, device trust management, background synchronization, conflict-assistance tools, production disaster recovery, and carefully governed offline mutation for limited object families.

Those additions must reuse the same stable operation IDs, expected-version checks, permission snapshots, expiry, reconciliation, audit, checkpoint, and Event-history contracts. They may not redefine a local draft as authoritative state.

## 3. Roles and authority

| Role | Allowed actions | Hidden information | Approval required |
|---|---|---|---|
| Player | Autosave own drafts; resume authorized Character and Session context; submit or retry idempotent commands; review conflicts affecting own work | Cannot restore GM-only state, another Player’s private drafts, revoked Characters, or hidden Event payloads | GM approval remains required for governed proposals; conflicts requiring game judgment route to GM |
| Game Master | Autosave Campaign and Scene drafts; recover authorized GM workspace; review pending proposals; resolve permitted conflicts; initiate bounded Session checkpoint requests | Cannot restore another Player’s private notes or unrelated Campaign state; cached Player preview remains projection-only | Owner approval for destructive recovery outside the bounded alpha runbook |
| Assistant GM | Recover only delegated Campaign areas and current delegation scope | Revoked or expired delegation removes cached and reconnect access | Active delegation and GM/Owner authority |
| Content Creator | Autosave own drafts and recover assigned review state | Cannot restore other creators’ private drafts or Campaign-private data without separate membership | Canonical promotion remains owner-gated |
| Observer | Resume only an active observer projection | No private drafts, hidden history, commands, or mutation recovery | GM or Owner grant; revocation ends access |
| Owner/Admin | Inspect operational recovery evidence and administer bounded alpha support | Owner status alone does not reveal Player-private or Campaign-private content | Explicit support-access record for protected content; production recovery remains separately gated |
| Service actor | Persist drafts, commands, Events, checkpoints, cursors, and recovery receipts within narrow service scope | May not broaden projection or bypass service authorization | Service identity and approved operation contract |
| AI service actor | Optional read-only explanation of a visible recovery state | No hidden cache inspection, conflict mutation, or autonomous resubmission | Explicit user request, same authorization, and zero-AI fallback |

## 4. Dependencies

### Feature dependencies

- MV-IA-F003 — Identity, Dashboard, and Workspace Selection;
- MV-IA-F020 — Permissions and Hidden Information;
- MV-IA-F001 — Application Shell and Workspace Navigation;
- MV-IA-F019 — Content Library and Entitlements;
- MV-IA-F024 — Pack Lifecycle and Canonical Content Registry;
- MV-IA-F002 — Universal Object Experience for stable object references and recovery inspection;
- MV-IA-F006 — caller for the first playable Action loop.

### Shared systems

- SS-01 application shell and navigation;
- SS-02 identity and subject context;
- SS-03 Campaign role and workspace context;
- SS-04 authorization and hidden-information projection;
- SS-05 entitlement evaluation;
- SS-06 persistence and transactions;
- SS-07 realtime and Session protocol;
- SS-08 notifications and approval queue;
- SS-09 drafts and autosave;
- SS-10 errors, recovery, and support;
- SS-11 telemetry and diagnostics;
- SS-12 accessibility and responsive behavior;
- SS-13 pack and schema version registry;
- SS-14 export and provider-exit evidence.

### Service ports and adapters

- IdentityPort;
- EntitlementPort;
- PersistencePort;
- MigrationPort;
- SessionCommandPort;
- RealtimePort;
- CheckpointPort;
- BackupPort;
- RestorePort;
- ProviderExitPort;
- ObjectStoragePort where approved draft attachments exist;
- TelemetryPort;
- clock and monotonic-sequence abstractions;
- local draft store adapter;
- bounded offline snapshot adapter.

### Canonical objects and packs

- stable subject;
- Campaign;
- Campaign membership and role;
- Character and controller binding;
- Scene;
- Session;
- Action proposal;
- GM decision;
- Event;
- snapshot;
- checkpoint;
- pack lockfile;
- rules profile;
- schema and migration registry;
- approved alpha content corpus.

### Schemas and migrations

Required contracts include:

- LocalDraftEnvelope;
- DraftAutosaveReceipt;
- AuthoritativeSaveRequest and SaveReceipt;
- ClientOperationId;
- SessionCommand and CommandStatus;
- EventCursor and EventGapRequest;
- ReconnectRequest and ReconnectReceipt;
- SelectedContextReceipt;
- OfflineSnapshotManifest;
- OfflineDraftReconciliationRequest;
- ConflictRecord;
- RecoveryPlan and RecoveryReceipt;
- CheckpointManifest;
- PermissionSnapshot;
- entitlement and pack-version snapshot;
- schema and migration versions.

Migration rules must preserve stable IDs, command IDs, Event sequence, draft ownership, permission scope, and receipt history.

### Decisions and gates

- P9-06 active implementation order;
- P9-06-008 backup, restore, and provider-exit ports;
- AG-03 Data Foundation;
- AG-04 Identity and Entitlements;
- AG-05 Authoritative Sessions;
- AG-06 Operations and Exit;
- AG-07 Two-Device Alpha;
- owner internal-alpha release gate;
- no paid services, production credentials, production deployment, or public release.

## 5. Object and state model

### Reusable Definitions

This feature does not redefine game-content Definitions. It references:

- command and Event type Definitions;
- rules profiles;
- schema Definitions;
- pack manifests;
- recovery-policy profiles;
- offline eligibility profiles.

### Campaign placements or bindings

Campaign-scoped bindings include:

- membership and role;
- Character control;
- active rules profile;
- installed pack lockfile;
- selected Scene and Session;
- participant visibility;
- offline eligibility;
- recovery retention policy.

### Live instances and state

#### LocalDraftEnvelope

Required fields:

- draft ID;
- subject ID;
- workspace type and stable workspace ID;
- selected-context ID;
- object or proposal type;
- base authoritative version;
- local revision;
- client operation ID;
- created and modified timestamps;
- device-local key;
- encrypted payload or protected storage reference;
- schema version;
- pack-lock digest;
- permission-version hint;
- sync state;
- expiry;
- attachment references;
- integrity digest.

A LocalDraftEnvelope is not authoritative state.

#### DraftAutosaveReceipt

Records:

- draft ID;
- local revision;
- persisted-at timestamp;
- storage adapter;
- integrity digest;
- encryption status;
- next retry time when degraded.

It must not use language such as “submitted,” “approved,” or “accepted.”

#### AuthoritativeSaveReceipt

Records:

- operation ID;
- aggregate ID;
- accepted version;
- Event IDs when applicable;
- persisted-at timestamp;
- server correlation ID;
- result digest.

#### SessionCommandStatus

Values:

- local-only;
- queued-for-submit;
- submitted;
- received;
- validating;
- pending-GM;
- accepted;
- modified-and-accepted;
- rejected;
- stale;
- forbidden;
- entitlement-restricted;
- cancelled-before-acceptance;
- status-unknown;
- recovery-required.

#### EventCursor

Contains:

- Session ID;
- last acknowledged authoritative sequence;
- projection version;
- checkpoint ID when used;
- permission version;
- schema version.

#### OfflineSnapshotManifest

Contains:

- snapshot ID;
- subject ID;
- selected-context ID;
- included stable IDs and field projections;
- visibility classes;
- permission and entitlement versions;
- pack lockfile and schema versions;
- created, expires, and last-online timestamps;
- read-only capability list;
- allowed local-draft types;
- prohibited operations;
- content and manifest digests;
- encryption status;
- device binding where approved.

#### ConflictRecord

Contains:

- conflict ID;
- subject and workspace;
- local draft ID;
- base authoritative version;
- current authoritative version;
- changed fields or object families;
- permission status;
- entitlement status;
- safe comparison projection;
- allowed resolutions;
- decision authority;
- created and resolved timestamps;
- resolution receipt.

### Events and history

Representative Events:

- DraftAutosavedLocal;
- DraftSyncAttempted;
- DraftReconciled;
- DraftConflictDetected;
- DraftDiscarded;
- CommandReceived;
- CommandStatusResolved;
- CommandAccepted;
- CommandRejected;
- CommandModifiedAndAccepted;
- EventGapDetected;
- EventGapRecovered;
- ReconnectStarted;
- ReconnectCompleted;
- ReconnectDenied;
- SelectedContextRevalidated;
- PermissionChangedDuringRecovery;
- EntitlementChangedDuringRecovery;
- OfflineSnapshotIssued;
- OfflineSnapshotExpired;
- OfflineSnapshotPurged;
- CheckpointCreated;
- CheckpointVerified;
- RecoveryStarted;
- RecoveryCompleted;
- RecoveryFailed.

Local-only draft events remain local diagnostics until explicitly submitted through an authorized contract.

### Projections and indexes

Required projections:

- draft status;
- save status;
- command status;
- pending approvals;
- connection status;
- sync and Event gap status;
- current authoritative version;
- conflict summary;
- recovery progress;
- offline snapshot status;
- expired or revoked state;
- safe recent-work restoration.

Indexes must be scoped by subject, Campaign, workspace, role, visibility, entitlement, lifecycle, and current permission version.

### Stable IDs

Stable identities are required for:

- drafts;
- client operations;
- commands;
- Events;
- Sessions;
- checkpoints;
- recovery operations;
- conflicts;
- offline snapshots;
- selected-context receipts;
- devices when a bounded device identity is used.

Retries reuse the same operation or command ID. A new user intent requires a new ID.

### Provenance

Recovery evidence records:

- source command or draft;
- service and adapter versions;
- schema and pack versions;
- prior and resulting state versions;
- checkpoint and backup references;
- permission and entitlement versions;
- tests or drill IDs;
- failure and retry history.

## 6. Primary user flow

1. The user establishes or resumes an authenticated subject session.
2. The dashboard resolves only authorized workspaces and selected contexts.
3. The user enters a permitted Campaign, Character, Scene, or Session.
4. Editable work starts in a LocalDraftEnvelope with an explicit draft indicator.
5. Autosave writes the local draft and shows a DraftAutosaveReceipt state.
6. When the user performs an authoritative save or submits an Action, the client sends one stable operation or command ID with the expected version.
7. The trusted service revalidates identity, role, permissions, entitlements, pack state, schema version, and object lifecycle.
8. The service commits accepted state and outbox records transactionally or rejects without partial mutation.
9. The client receives a SaveReceipt, command status, or accepted Event and advances its cursor.
10. If the connection drops, the client preserves local drafts and operation IDs but does not guess the authoritative result.
11. On reconnect, the client reauthenticates, revalidates selected context, asks for command status, and requests Events after the last acknowledged sequence.
12. The service returns a role-safe projection and reconciliation instructions.
13. The client marks accepted, rejected, pending, stale, conflict, revoked, or recovery-required state visibly.
14. The user continues from the newest authorized state without duplicate accepted effects.

## 7. Alternate and secondary flows

### Alternate flow A — reload before submission

1. The user edits a proposal.
2. Local autosave succeeds.
3. The app reloads before submission.
4. Identity and selected context revalidate.
5. The draft is restored only when the same subject still has access.
6. The user may continue, discard, or create a copy when the base version changed.

### Alternate flow B — ambiguous submit

1. The client sends a command with a stable command ID.
2. The network fails before the response.
3. The client displays `status unknown`, not failed or accepted.
4. On reconnect, the client queries command status using the same ID.
5. The server returns prior accepted, rejected, pending, or unknown result.
6. The client never automatically creates a second command ID for the same intent.

### Alternate flow C — missed accepted Events

1. An Event commits.
2. The client disconnects before display.
3. On reconnect, the client sends its last acknowledged sequence.
4. The service supplies the permitted Event gap or a verified projection/checkpoint.
5. The client applies Events once and acknowledges the new sequence.

### Alternate flow D — pending GM decision

1. A Player proposal reaches `pending-GM`.
2. Player or GM disconnects.
3. The queue remains durable.
4. Reconnected clients receive role-safe pending status.
5. The GM decision uses the original proposal identity and current authorization.
6. The Player receives the final permitted result.

### Alternate flow E — permission or role revoked

1. Access changes while a client is offline.
2. The offline snapshot remains bounded by expiry but cannot authorize mutation.
3. On reconnect, authorization fails or returns reduced scope.
4. Protected cache entries and drafts are locked or purged according to policy.
5. The client does not reveal prior hidden labels, counts, previews, or attachments.
6. A privacy-safe recovery receipt records the action.

### Alternate flow F — conflict

1. The authoritative object changes after the draft base version.
2. Reconnect detects a version mismatch.
3. The service creates a safe ConflictRecord.
4. Automatic merge occurs only for explicitly commutative, schema-approved fields.
5. Other conflicts require user, GM, or owner-authorized resolution.
6. The original draft and authoritative state remain recoverable until disposition.

### Alternate flow G — second device

1. The user opens the same workspace on a second device.
2. Both devices receive current authoritative versions and device-local draft identities.
3. Accepted mutations remain server-idempotent.
4. Conflicting drafts do not silently overwrite each other.
5. The UI identifies the other active edit when the approved presence contract supports it.

### Alternate flow H — service restart or checkpoint recovery

1. Realtime delivery stops.
2. Durable command, Event, outbox, and checkpoint state survives.
3. Services restart.
4. Checkpoint and Event continuity verify.
5. Clients reconnect from their last acknowledged sequence.
6. A recovery Event records any restore operation.
7. No accepted history is erased.

### Alternate flow I — bounded offline preparation

1. An authorized user explicitly downloads an eligible offline snapshot.
2. The manifest records expiry, permitted read operations, and allowed draft types.
3. Offline, the user reads cached projections and edits local drafts.
4. Authoritative mutation controls remain disabled.
5. On reconnect, permissions, entitlement, versions, and lifecycle revalidate.
6. Drafts reconcile or become conflicts; the snapshot does not overwrite current state.

## 8. Failure, empty, and recovery states

| State | User sees | Allowed action | Preserved data | Evidence |
|---|---|---|---|---|
| Loading | “Checking saved work and current access” | Cancel navigation or wait | Existing local draft and last acknowledged cursor | load correlation ID |
| Empty | “No recoverable draft or recent workspace” | Start new work or return | No fabricated prior state | empty-state reason |
| Validation error | Specific invalid draft field or incompatible version | Correct, copy safe text, or discard | Draft and validation details | validation receipt |
| Forbidden | “This workspace is no longer available” | Return to authorized dashboard; request access outside app workflow | Protected payload locked or purged | user-safe denial and internal reason |
| Restricted entitlement | “Access changed; saved draft remains unavailable for submission” | Review permitted summary or return | Draft retained according to policy without exposing restricted content | entitlement decision |
| Offline | Persistent offline banner with snapshot expiry and disabled authoritative actions | Read eligible cache; edit allowed local drafts; reconnect | encrypted local snapshot and drafts | offline manifest |
| Stale | Current version changed | Reload, compare safe changes, or open conflict flow | Local draft and authoritative version refs | stale receipt |
| Conflict | Safe conflict summary and authority for resolution | choose approved merge, copy, discard, or route to GM | both versions and conflict record | conflict ID |
| Failed save | “Local autosave failed” or “authoritative save failed,” explicitly distinguished | retry, copy content, download safe draft where allowed | in-memory or prior local revision | save attempt ID |
| Recovery required | Guided recovery panel with exact operation status | resume, inspect, retry safe lookup, or report issue | operation IDs, receipts, cursor, draft | recovery ID |
| Status unknown | “Submission may have reached the server” | query status; do not resubmit as new intent | command ID and payload digest | command-status lookup |
| Pending approval | Durable pending state | wait, withdraw only when allowed, or GM decides | proposal and queue record | proposal ID |
| Revoked during recovery | Generic access-changed state | return to dashboard | no protected fields displayed | revocation receipt |
| Expired offline snapshot | “Reconnect required” | reconnect or purge | manifest only until safe purge | expiry record |
| Corrupt local cache | Safe reset guidance | quarantine cache; recover from authoritative service | diagnostic digest, not protected content | integrity failure |
| Service restart | Reconnecting status | wait, cancel local navigation, report issue after timeout | draft, command IDs, cursor | restart/reconnect receipt |

## 9. Permissions and hidden information

### Authorization questions

Every recovery request asks:

- Is the subject session current?
- Is the selected context still valid?
- Is Campaign membership active?
- Is the requested role active and delegated?
- Does the subject still control the Character or Asset?
- Are object, field, relationship, Event, and attachment projections permitted?
- Is entitlement current?
- Are required packs installed and permitted?
- Has the object been archived, withdrawn, superseded, or deleted?
- Does the offline snapshot remain unexpired and bound to the same subject and context?
- Does the operation attempt mutation, and if so, has authorization been rechecked at execution time?
- Would status, count, label, preview, or error wording reveal hidden information?

### Recovery projection rules

- Recovery returns current authorized projection, not the bytes the client previously cached.
- A local draft may be restored only to the subject and context that owns it.
- GM-only data cannot be restored into a Player context.
- Player-private notes cannot be restored to Owner/Admin or GM merely because operational support is active.
- Permission and entitlement versions are advisory hints on the client; the server makes the decision.
- Revocation invalidates active subscriptions, selected-context receipts, protected caches, and offline mutation capability.
- Hidden Event payloads are filtered before gap delivery.
- Checkpoints and backups are never sent directly to ordinary clients.
- Status lookup must not reveal whether an unauthorized command, Campaign, Character, or Session exists.
- Denials use user-safe reasons while retaining internal reasons in restricted audit evidence.

### Required denied-case tests

- Player reconnects to another Campaign’s Session ID.
- Former GM reconnects after role revocation.
- Assistant GM restores outside delegated scope.
- Observer attempts to recover a local mutation draft.
- Player requests GM-only Event gap.
- Owner/Admin attempts to open Player-private notes without support access.
- Expired invitation deep link attempts workspace restore.
- Entitlement expires while offline.
- Character control transfers while a Player is offline.
- Pack is removed or version changes before draft reconciliation.
- Offline snapshot belongs to a different subject or device binding.
- Command-status lookup uses an unauthorized Session ID.
- Cached autocomplete or recent work would expose a hidden workspace.
- Realtime reconnect subscribes before authorization.
- AI recovery explanation requests hidden diagnostics.
- Export or issue report attempts to attach protected draft bytes.
- Revoked subject reuses an old selected-context receipt.
- Local clock manipulation attempts to extend offline expiry.
- Corrupt manifest attempts to broaden offline capability.
- Second device attempts last-write-wins over a protected current version.

## 10. Entitlements

- **Access sources:** free tier, owned content, Campaign grants, sponsored access, alpha tester grant, owner-approved fixtures.
- **Free-tier behavior:** cached and restored content remains limited to the currently entitled projection.
- **Campaign grants:** valid only inside the Campaign and do not become global ownership when cached.
- **Sponsored access:** expiration prevents new authoritative use and triggers revalidation; history remains preserved.
- **Expiry behavior:** offline snapshots stop being usable at server-verified expiry on reconnect and at locally enforced expiry offline.
- **Historical-state behavior:** accepted Events and references remain historically intact even when content can no longer be opened in full.
- **Search and preview restrictions:** recovered recent work and object labels cannot expose restricted content.
- **Offline snapshot behavior:** manifest records entitlement version, access source, expiry, and allowed content IDs; it never authorizes a broader tier.
- **Draft behavior:** an entitlement change may allow safe text export or copy according to policy, but not submission using restricted mechanics.

## 11. Persistence and history

- **Draft storage:** encrypted or platform-protected local store; optionally synchronized to an approved private draft service later.
- **Authoritative save:** trusted service transaction with expected version and idempotency key.
- **Aggregate boundary:** defined by the caller domain; recovery does not create cross-aggregate partial mutation.
- **Expected-version behavior:** mismatch produces stale or conflict state, not silent overwrite.
- **Idempotency:** same operation ID and same payload returns prior result; same ID with different payload rejects.
- **Event types:** command, save, conflict, reconnect, gap recovery, checkpoint, restore, and offline lifecycle Events.
- **Snapshot or checkpoint behavior:** verified server checkpoints accelerate recovery but do not replace Event history.
- **Audit events:** material restore, access change, conflict disposition, support access, checkpoint, and provider-exit operations.
- **Migration behavior:** local drafts and offline snapshots carry schema and pack versions; incompatible drafts enter guided recovery.
- **Export behavior:** provider-exit export preserves authoritative state, Events, checkpoints, operation receipts, and necessary draft metadata where policy permits.
- **Retention:** local drafts expire according to object type and privacy policy; accepted history follows domain retention.
- **Deletion:** local purge does not delete authoritative state; account or Campaign deletion follows separate governance.

## 12. Realtime, interruption, and reconnect

### Before local submission

The client preserves a local draft. Reload restores it only after identity and context revalidation. No server command status exists.

### After submission but before acceptance

The client retains the same command ID and payload digest. On reconnect it queries status. It does not automatically resend with a new ID.

### After acceptance but before display

The accepted Event is recovered through command status, Event gap delivery, or current projection. Applying the Event twice must be harmless or prevented by sequence tracking.

### During a pending approval

The proposal remains durable. Player and GM receive role-safe pending projections. A reconnect does not create a duplicate queue item.

### After missed Events

The client submits the last acknowledged sequence. The service returns permitted Events or instructs the client to replace its projection from a verified checkpoint/current state.

### With a stale client

Mutations carry expected version. Stale requests reject or enter a governed revalidation flow.

### From a second device

Both devices use separate connection IDs and local-draft IDs but share stable subject and authoritative object identities. Accepted operations remain idempotent.

### After service restart

Durable state, outbox, Event history, command status, and verified checkpoints restore. Realtime presence may rebuild, but accepted state is not reconstructed from transient presence.

### Reconnect handshake

The request includes:

- stable subject session;
- selected-context receipt ID;
- Campaign, role, Character, Scene, and Session IDs as applicable;
- last acknowledged Event sequence;
- last known projection version;
- outstanding command IDs;
- local draft summaries, not protected full payload unless requested;
- permission, entitlement, schema, and pack version hints;
- client and protocol version;
- correlation ID.

The receipt includes:

- resolved subject and context;
- current authorization result;
- current versions;
- accepted/rejected/pending command statuses;
- Event-gap plan;
- draft reconciliation plan;
- cache invalidation directives;
- offline snapshot state;
- safe user messages;
- recovery receipt ID.

## 13. Interface and information hierarchy

### Desktop

Primary areas:

1. current workspace and role;
2. connection and save state;
3. active content or proposal;
4. pending authoritative status;
5. recovery actions;
6. secondary history and diagnostics.

A recovery drawer shows:

- local draft revision;
- last local autosave;
- last authoritative save;
- outstanding operation or command;
- last acknowledged Event;
- current connection state;
- conflict or permission status;
- safe next action.

### Tablet

Use the same hierarchy with a collapsible recovery panel. Save and connection state remain visible without covering the primary task.

### Mobile

Use a persistent compact status region and one focused recovery sheet. Critical distinctions must fit without hover:

- saved locally;
- saved to Campaign;
- submitted;
- awaiting GM;
- accepted;
- rejected;
- offline;
- reconnecting;
- conflict;
- access changed.

### Player hierarchy

Foreground:

- current Character and Session;
- draft or proposal;
- submission status;
- current permitted result;
- direct recovery action.

Secondary:

- detailed Event history;
- connection diagnostics;
- technical receipt IDs;
- issue-report attachment.

### GM hierarchy

Foreground:

- current Campaign, Scene, and Session;
- pending proposals;
- decision state;
- authoritative save status;
- participant reconnect status where permitted;
- conflicts requiring GM judgment.

Secondary:

- technical checkpoint and gap details;
- operational recovery logs;
- nonblocking local-draft metadata.

## 14. Accessibility

- **Semantic structure:** status regions, recovery steps, conflict summaries, and action groups use correct landmarks and headings.
- **Keyboard flow:** every recovery action, draft comparison, status lookup, and conflict option is keyboard reachable.
- **Focus behavior:** focus moves to the recovery summary after a blocking interruption and returns to the initiating control after resolution.
- **Screen-reader names and states:** save, submit, pending, accepted, offline, stale, conflict, and revoked states have explicit names.
- **Live announcements:** announce material state transitions once; do not repeatedly announce every retry.
- **Text scaling:** recovery details remain usable at high zoom without horizontal dependency.
- **Contrast and noncolor status:** icon, label, and text distinguish local, authoritative, pending, failed, and offline states.
- **Reduced motion:** reconnect and recovery progress avoids continuous animation.
- **Touch targets:** retry, copy, discard, compare, reconnect, and report controls meet target requirements.
- **Nondrag alternatives:** conflict and draft selection never require drag.
- **Map or graph alternative:** Event and recovery timelines have ordered list or table views.
- **Error identification and recovery:** errors identify whether data remains local, authoritative, or unknown and name the safe next action.
- **Cognitive clarity:** avoid ambiguous “saved” language; use exact state labels.
- **Timeouts:** offline expiry and session expiry are explained with accessible warnings and no color-only countdown.

## 15. Notifications and queues

| Trigger | Recipient | Message content | Action | Resolution state |
|---|---|---|---|---|
| Local autosave degraded | Draft owner | Draft remains in memory or prior revision; copy recommended | retry or copy | recovered / unresolved |
| Authoritative save accepted | Requesting subject | Saved to Campaign at version N | open receipt | acknowledged |
| Command status unknown | Requesting Player or GM | Submission may have reached service | check status | accepted / rejected / pending / unknown |
| Proposal pending after reconnect | Player and assigned GM | Proposal identity and permitted summary | Player views status; GM reviews | decided / withdrawn |
| Event gap detected | Affected participant | Reconnecting and checking missed updates | wait or report after timeout | recovered / failed |
| Permission changed | Affected subject | Access changed; protected data removed | return to dashboard | acknowledged |
| Entitlement changed | Affected subject | Content access changed | review permitted options | acknowledged |
| Conflict detected | Draft owner and decision authority | Safe object and field summary | compare or route | resolved / deferred |
| Offline snapshot nearing expiry | Snapshot owner | Reconnect required by time | reconnect | refreshed / expired |
| Recovery failed | Affected subject and authorized support | User-safe failure and receipt ID | retry or report | resolved / escalated |
| Checkpoint verification failed | Owner/Admin operations only | Operational failure without protected payload | stop and investigate | repaired / owner-gated |

## 16. AI involvement

**AI mode:** optional read-only explanation; zero-AI core workflow

- **Allowed action:** explain a visible recovery state, summarize user-visible conflict options, or help format a privacy-safe issue report.
- **Allowed sources:** current user-safe projection, public help, and user-visible receipts.
- **Permission and entitlement checks:** identical to other reads; no direct cache, checkpoint, backup, or hidden diagnostic access.
- **Provenance:** cite the relevant visible receipt, help rule, or status.
- **Uncertainty:** state when command status or recovery outcome remains unknown.
- **Cost boundary:** core save, reconnect, conflict, and recovery behavior requires zero AI and zero paid AI service.
- **Non-AI fallback:** all recovery states and actions have deterministic labels and help.
- **Prohibited behavior:** resubmit commands autonomously, choose a conflict outcome, reveal hidden data, alter Event history, fabricate acceptance, or promote local drafts to authoritative state.

## 17. Telemetry and diagnostics

- **Operation IDs:** stable for autosave, save, command, reconnect, gap recovery, conflict, checkpoint, and recovery.
- **Correlation IDs:** connect client attempt, service request, transaction, outbox, realtime delivery, and issue report.
- **Performance measurements:** local autosave latency, authoritative save latency, reconnect time, gap size, checkpoint load time, conflict-detection time.
- **Error events:** storage failure, integrity failure, status unknown, gap failure, incompatible schema, expired snapshot, restore failure.
- **Permission denials:** internal reason code and policy version without protected payload.
- **Reconnect events:** start, authentication, context revalidation, command-status resolution, gap recovery, completion.
- **Privacy redaction:** no draft body, private note, hidden clue, GM truth, token, credential, or unrestricted Event payload.
- **Issue-report attachment:** release ID, client version, operation IDs, safe state machine, timestamps, adapter versions, and user-approved diagnostics.
- **Cost signals:** storage use, Event-gap volume, checkpoint frequency, offline snapshot size; no automatic paid upgrade.
- **Retention:** diagnostic retention follows alpha policy and excludes sensitive content by default.

## 18. Test scenarios

### Unit

- autosave state machine distinguishes local and authoritative states;
- command ID retry behavior;
- expected-version conflict classification;
- offline expiry calculation resists local clock rollback where possible;
- cache invalidation directives;
- safe user-message mapping.

### Contract

- LocalDraftStore contract;
- PersistencePort idempotency and expected-version behavior;
- SessionCommandPort command-status lookup;
- RealtimePort Event-gap and reconnect contract;
- CheckpointPort create, verify, read, and compatibility behavior;
- Backup, Restore, and ProviderExit port relationships;
- permission and entitlement revalidation.

### Integration

- draft to authoritative save;
- ambiguous submit to status lookup;
- accepted Event before disconnect to gap recovery;
- pending proposal across Player and GM reconnect;
- permission revocation during recovery;
- pack or schema version change during draft reconciliation;
- service restart with durable command and Event state.

### End-to-end

- Player edits, reloads, restores draft, submits, disconnects, reconnects, and sees one accepted result;
- GM receives one pending proposal, disconnects, reconnects, modifies and accepts, and both clients synchronize;
- two devices edit the same object and receive a governed conflict rather than silent overwrite;
- bounded offline snapshot permits read and draft but blocks authoritative mutation.

### Permission and hidden information

- all denied cases in the companion matrix;
- no hidden names, counts, aliases, relationships, attachments, or Event payloads in recovery;
- caches and selected context invalidate on revocation;
- Player-private and GM-only material remain separated.

### Entitlement

- free, Campaign-granted, sponsored, expired, and revoked access;
- offline expiry;
- historical Event references remain without protected detail;
- restricted draft cannot submit.

### Persistence and migration

- local draft schema migration;
- incompatible draft recovery;
- idempotent save retry;
- command ID reuse with different payload rejects;
- checkpoint and Event count reconciliation;
- provider-exit export preserves IDs and history.

### Reconnect and recovery

- interruption at every state boundary;
- Event gaps of zero, one, many, and beyond direct replay threshold;
- status unknown;
- service restart;
- corrupt local cache;
- corrupt checkpoint;
- restore appends recovery Event;
- duplicate realtime delivery.

### Accessibility

- keyboard-only recovery;
- screen-reader announcements;
- high zoom;
- touch;
- reduced motion;
- noncolor state identification;
- Event timeline list alternative.

### Performance

- local autosave does not block typing;
- reconnect completes within the approved alpha budget for representative gaps;
- large draft and offline snapshot remain bounded;
- repeated network flapping uses backoff and does not storm services;
- checkpoint recovery meets the approved alpha target.

### Golden or deterministic regression

- 8D-007J applies when recovery changes rules inputs, accepted Event ordering, random seeds, Resources, Conditions, or results;
- pure presentation recovery uses deterministic product regression instead of a balance claim.

## 19. Acceptance criteria

1. **REC-AC-001 — Local versus authoritative clarity**  
   **Condition:** Every supported edit displays whether it is in memory, saved locally, saved authoritatively, submitted, pending, or accepted.  
   **Evidence:** interaction tests, accessibility audit, screenshots, and state-machine tests.  
   **Blocking:** yes.

2. **REC-AC-002 — Local draft recovery**  
   **Condition:** A same-subject reload restores an eligible local draft only after current context authorization.  
   **Evidence:** end-to-end reload test and denied cross-subject test.  
   **Blocking:** yes.

3. **REC-AC-003 — Idempotent authoritative save**  
   **Condition:** Retrying the same operation ID and payload applies one business effect and returns the prior receipt.  
   **Evidence:** persistence contract test.  
   **Blocking:** yes.

4. **REC-AC-004 — Ambiguous command resolution**  
   **Condition:** A dropped response leads to status lookup using the original command ID, not an automatic duplicate command.  
   **Evidence:** failure-injection test.  
   **Blocking:** yes.

5. **REC-AC-005 — Event-gap recovery**  
   **Condition:** A reconnecting client recovers every permitted committed Event after its last acknowledged sequence exactly once.  
   **Evidence:** realtime integration test with duplicate and reordered delivery.  
   **Blocking:** yes.

6. **REC-AC-006 — Pending approval continuity**  
   **Condition:** One proposal remains one durable queue item across Player and GM disconnects and reconnects.  
   **Evidence:** two-device end-to-end test.  
   **Blocking:** yes.

7. **REC-AC-007 — Selected-context revalidation**  
   **Condition:** Reconnect revalidates identity, Campaign, role, Character control, permission, entitlement, pack, schema, and lifecycle state.  
   **Evidence:** matrix-driven integration tests.  
   **Blocking:** yes.

8. **REC-AC-008 — Revocation safety**  
   **Condition:** Revocation invalidates subscriptions and protected cache access without revealing hidden workspace existence or fields.  
   **Evidence:** revocation and inference tests.  
   **Blocking:** yes.

9. **REC-AC-009 — Conflict without silent overwrite**  
   **Condition:** Noncommutative version conflicts preserve both states and require an authorized disposition.  
   **Evidence:** concurrent-device test and ConflictRecord receipt.  
   **Blocking:** yes.

10. **REC-AC-010 — Bounded offline read**  
    **Condition:** An approved offline snapshot exposes only listed, unexpired, authorized projections.  
    **Evidence:** offline manifest and expiry tests.  
    **Blocking:** yes.

11. **REC-AC-011 — Offline mutation boundary**  
    **Condition:** Offline users may create allowed local drafts but cannot produce accepted authoritative mutation.  
    **Evidence:** UI and service denied-case tests.  
    **Blocking:** yes.

12. **REC-AC-012 — Offline reconciliation**  
    **Condition:** Reconnecting drafts revalidate and either reconcile safely, become a conflict, or remain unavailable with a user-safe reason.  
    **Evidence:** offline-to-online integration suite.  
    **Blocking:** yes.

13. **REC-AC-013 — Service restart continuity**  
    **Condition:** Durable commands, Events, pending approvals, outbox entries, and checkpoints survive a service restart.  
    **Evidence:** restart drill.  
    **Blocking:** yes.

14. **REC-AC-014 — Checkpoint integrity**  
    **Condition:** A checkpoint is used only after digest, schema, pack, Event cursor, and compatibility verification.  
    **Evidence:** CheckpointPort contract and corrupt-checkpoint tests.  
    **Blocking:** yes.

15. **REC-AC-015 — History-preserving restore**  
    **Condition:** A restore or recovery appends attributable recovery history and does not erase prior accepted Events.  
    **Evidence:** restore drill and Event audit.  
    **Blocking:** yes.

16. **REC-AC-016 — Safe diagnostics**  
    **Condition:** Recovery telemetry and issue reports contain operation metadata but no protected draft body, private note, hidden clue, GM truth, token, or credential.  
    **Evidence:** telemetry fixture scan and privacy review.  
    **Blocking:** yes.

17. **REC-AC-017 — Accessible recovery**  
    **Condition:** The complete primary recovery journey works by keyboard and touch and passes a screen-reader review with noncolor status labels.  
    **Evidence:** manual and automated accessibility evidence.  
    **Blocking:** yes.

18. **REC-AC-018 — Provider-neutral contracts**  
    **Condition:** Domain code depends on Multiversal ports and portable manifests rather than one provider’s sync, storage, or realtime format.  
    **Evidence:** architecture review and contract tests.  
    **Blocking:** yes.

19. **REC-AC-019 — Zero-service local testability**  
    **Condition:** Draft, reconnect state machine, conflict classification, and recovery fixtures run locally without paid services, production credentials, AI, or network access.  
    **Evidence:** CI and local runbook.  
    **Blocking:** yes.

20. **REC-AC-020 — Primary two-device proof**  
    **Condition:** Distinct Player and GM clients complete proposal, interruption, reconnect, GM decision, persistent result, and synchronized recovery without duplicate effect or hidden-information leak.  
    **Evidence:** AG-07-style two-device acceptance record.  
    **Blocking:** yes.

## 20. Fixtures and approved alpha content

- **Required identities:** Player A, Player B, GM, Assistant GM with bounded delegation, Observer, Owner/Admin support actor, service actor.
- **Required Campaign:** one active Campaign plus a second forbidden Campaign for isolation tests.
- **Required Characters:** Player-controlled Character, transferred Character, unauthorized Character, and retired Character.
- **Required packs:** version-pinned alpha pack set, one upgraded pack fixture, one removed or unavailable pack fixture.
- **Required objects:** Character draft, Scene draft, Action proposal, pending GM decision, accepted Event, rejected command, inventory or relationship object for conflict tests.
- **Required hidden information:** GM-only NPC motive, unrevealed clue, Player-private note, hidden Scene participant, protected attachment.
- **Required historical state:** Events before and after checkpoint, prior selected-context receipt, expired entitlement, revoked role, completed proposal.
- **Required failure fixtures:** local storage full, corrupt draft digest, dropped response, duplicated delivery, reordered Event, Event gap, service restart, corrupt checkpoint, expired offline snapshot, schema mismatch, pack mismatch, permission change, entitlement change, second-device conflict.
- **Required offline fixtures:** eligible read-only snapshot, ineligible workspace, allowed local draft, prohibited mutation, clock-skew case.
- **Required accessibility fixtures:** long status text, high zoom, screen-reader announcement order, keyboard conflict resolution.

## 21. Security, privacy, cost, and risk

### Security

- local drafts and offline snapshots use platform-protected storage or encryption appropriate to the environment;
- no production credentials or tokens are stored in draft payloads;
- manifests and checkpoints use integrity digests;
- server reauthorizes every mutation;
- reconnect subscriptions authorize before data delivery;
- operation IDs resist accidental collision and cannot be used to enumerate other subjects’ status;
- cache purge and lock behavior is tested on sign-out, revocation, expiry, and subject switch;
- retries use bounded exponential backoff;
- archive and attachment paths prevent traversal and unauthorized file access.

### Privacy

- protected payloads remain out of telemetry;
- Player-private and GM-only content stay separated;
- old cached labels, thumbnails, counts, and previews are purged or locked after revocation;
- issue reports require user review before attaching diagnostics;
- offline retention and purge are visible;
- support actors receive operational metadata only unless an explicit, time-bounded support-access record permits more.

### Cost

- the core alpha slice works with local adapters and repository-owned fixtures under a **zero paid service** validation requirement;
- no paid sync, notification, storage, database, AI, or realtime service is required to validate contracts;
- snapshot size, checkpoint frequency, retry traffic, and Event-gap volume are measured;
- automatic provider upgrades or paid enrollment are prohibited.

### Material risks

- ambiguous terminology could make a local draft appear committed;
- retry bugs could duplicate accepted effects;
- stale caches could reveal revoked data;
- automatic conflict merge could corrupt governed state;
- large offline snapshots could increase privacy exposure;
- checkpoint misuse could hide missing Events;
- client clock manipulation could affect offline expiry;
- cross-device drafts could overwrite each other;
- recovery diagnostics could leak protected content.

### Stop conditions

Stop implementation or release when:

- accepted effects can duplicate;
- command status cannot be resolved safely;
- hidden information appears in cache, recovery, Event gap, notification, diagnostic, or issue-report output;
- a restore erases accepted history;
- a corrupt checkpoint is accepted;
- offline mutation is represented as authoritative;
- revocation does not invalidate protected state;
- provider-specific semantics leak into domain contracts;
- a paid service, production credential, production deployment, or public-release action would be required;
- owner approval is required by an A3 gate.

## 22. Owner review points

- **Design approval required:** packet may be implemented after program review and dependency readiness.
- **Scope decision required:** any promotion of broad offline authoritative mutation, automatic conflict merge, or collaborative multi-master editing.
- **Canon decision required:** none for this platform behavior unless recovery would alter canonical rules or content.
- **Spending or provider decision required:** any paid sync, notification, database, storage, realtime, AI, or disaster-recovery provider.
- **Alpha release decision required:** exact integrated recovery evidence is part of the owner internal-alpha release decision.
- **Production decision required:** production backup, restore, multi-region recovery, and credential ceremony.
- **Privacy decision required:** support access to protected drafts or Campaign-private content beyond the bounded policy.

Silence is not approval.

## 23. Implementation handoff

**Target repository:** `cybalicistjt-stack/Multiversal-app`  
**Registered work type:** application feature foundation / reliability / realtime / persistence / recovery  
**Decision level:** A2 for bounded provider-neutral implementation; A3 for owner-reserved scope, spending, production, or release  
**Risk class:** high for state integrity and hidden information; bounded by contract and destructive-test gates  
**Suggested work-order title:** Implement MV-IA-F021 autosave, reconnect, recovery, and bounded offline foundation  
**Expected branches or files:**

- shared contracts for drafts, receipts, reconnect, command status, Event cursor, conflicts, checkpoints, and offline manifests;
- local draft and offline snapshot adapters;
- authoritative persistence and Session integration;
- recovery UI primitives and status vocabulary;
- fixtures and failure-injection harness;
- contract, integration, accessibility, and two-device tests;
- documentation and runbook.

**Required reviewers:** architecture, data, realtime, security, privacy, QA, accessibility, product, and documentation; independent reviewer separate from material author  
**Required gates:** current P9-06 dependencies, AG-03 through AG-07 as applicable, feature-packet validation, contract tests, denied-case suite, restart drill, checkpoint verification, two-device acceptance  
**Rollback or recovery:** revert code and schemas through governed migration; preserve failed evidence; never destructively remove accepted Events; local drafts remain exportable or safely quarantined where policy permits  
**Evidence outputs:**

- implementation receipt;
- port and schema contracts;
- migration and fixture receipts;
- idempotency and expected-version results;
- interruption matrix results;
- checkpoint and restart drill;
- offline boundary tests;
- permission and entitlement denied cases;
- accessibility review;
- two-device acceptance record;
- provider-exit compatibility evidence.

### Implementation decomposition

1. Define contracts and state vocabulary.
2. Implement local draft storage and integrity.
3. Implement authoritative save receipts and idempotency.
4. Implement command-status lookup and outstanding-operation recovery.
5. Implement Event cursor, gap recovery, and duplicate suppression.
6. Implement selected-context, permission, entitlement, pack, and schema revalidation.
7. Implement conflict records and safe resolution contracts.
8. Implement checkpoint verification and restart recovery.
9. Implement bounded offline manifest, expiry, read-only cache, and local drafts.
10. Implement recovery UI and accessible notifications.
11. Add telemetry and privacy-safe issue evidence.
12. Execute failure injection and two-device acceptance.

### Dependency hold points

Implementation remains dependency-gated until the active P9-06 sequence provides the required persistence, migration, realtime, authoritative Session, backup, restore, provider-exit, and checkpoint foundations.

Design completion does not authorize coding around missing contracts or representing temporary mock behavior as alpha-ready.

## 24. Readiness decision

- [x] All required sections complete.
- [x] Dependencies identified.
- [x] Shared-system impacts identified.
- [x] Permissions complete.
- [x] Persistence and recovery complete.
- [x] Accessibility complete.
- [x] Tests and acceptance criteria measurable.
- [x] Explicit exclusions complete.
- [x] Owner decisions identified.
- [x] Implementation handoff complete.

**Final design status:** implementation-ready; implementation remains dependency-gated  
**Reviewer:** independent architecture, security/privacy, QA, accessibility, data/realtime, and documentation review required through repository PR and CI  
**Date:** 2026-08-05  
**Packet digest:** calculated from the merged repository artifact and retained in implementation traceability
