# MV-IA-F005 — Campaign, Scene, and Session Builder

**Feature ID:** MV-IA-F005  
**Feature version:** 0.1.0  
**Classification:** entry-critical  
**Design status:** implementation-ready  
**Owner:** John Brandon Turner  
**Primary roles:** Game Master, Assistant GM, Player, observer, Owner/Admin, service actor  
**Stage A mapping:** A5 — Campaign, Scene, and Session Builder  
**Historical module mapping:** Campaign, Scene & Session Builder  
**Prepared by:** Lead Documentation Architect / Campaign and Session Systems Steward  
**Reviewed by:** product, game-system, architecture, canon, UX/accessibility, security, privacy, entitlement, persistence, recovery, QA, and documentation roles required before implementation  
**Date:** 2026-08-05

## 1. Problem and user outcome

### Problem

A Multiversal Campaign is not a folder of notes, a Scene is not merely a page, and a Session is not merely a timestamp. Together they form the governed preparation and launch path that binds participants, Characters, rules, packs, locations, environments, objects, hidden information, objectives, and retained history into playable state.

Without one authoritative design, later action, combat, social, investigation, inventory, encounter, map, relationship, and story-flow features would each create incompatible Campaign and Scene concepts. Common failures include:

- confusing reusable Definitions with Campaign-local placements and live Session state;
- launching against mutable drafts rather than a versioned launch snapshot;
- exposing GM notes, hidden creatures, unrevealed clues, secret objectives, or exact hidden counts;
- trusting client-side permissions, entitlements, pack compatibility, or Character control;
- silently changing rules or pack versions for an active Session;
- losing edits after reconnect or overwriting concurrent GM work;
- inviting a person without defining membership, role, Character control, or expiry separately;
- treating realtime delivery as the authority for Session state;
- allowing archived or invalid Scenes to launch;
- making mobile or accessible use a reduced-authority experience.

### Required outcome

An authorized Game Master can create a Campaign, bind an approved rules profile and pack lock, configure Character and participation policy, invite participants, create and organize Scenes, select real governed objects, write role-scoped notes, preview Player-visible projections, validate dependencies, save and reopen work, and launch one versioned Session snapshot.

Authorized Players can accept invitations, see only permitted Campaign and Session information, select or receive control of eligible Characters, and enter the launched Session. The resulting state remains recoverable, attributable, versioned, permission-safe, and portable.

### Why this belongs in internal alpha

The feature is entry-critical because every playable journey requires an authorized Campaign, at least one prepared Scene, participant and Character bindings, and a launchable Session. It is the GM preparation counterpart to MV-IA-F004 and the immediate prerequisite for MV-IA-F006, the first playable action and approval loop.

## 2. Alpha slice

### Included

- [x] Create, name, describe, save, reopen, archive, and restore one bounded Campaign.
- [x] Bind the Campaign to one approved rules profile, schema set, entitlement policy, and versioned pack-lock digest.
- [x] Configure Campaign Character creation, activation, advancement, and control policies without redefining MV-IA-F004.
- [x] Invite participants with explicit role, scope, expiry, and single-use or reusable policy.
- [x] Accept, decline, revoke, expire, and reissue invitations idempotently.
- [x] Maintain separate Campaign membership, active role, Character-control grants, ownership, and observer access.
- [x] Create Scene drafts from blank state or an approved template.
- [x] Organize Scenes into a bounded Campaign outline without requiring a full story-flow engine.
- [x] Select Locations, environments, hazards, creatures, NPCs, items, vehicles, clues, objectives, and other governed objects by stable ID.
- [x] Create Campaign-local placements and overrides without mutating source Definitions.
- [x] Write Player-visible, GM-only, Assistant-GM, and private-author notes with explicit visibility.
- [x] Add a map or visual reference and provide a required accessible nonvisual Scene description.
- [x] Configure participants, eligible Characters, initial placement, Scene visibility, objectives, entry conditions, and basic launch settings.
- [x] Validate references, permissions, entitlements, pack versions, required dependencies, Character eligibility, and launch readiness.
- [x] Preview the server-generated Scene and Campaign projection for a selected Player or observer.
- [x] Save, autosave, reopen, duplicate as a new draft, reorder, retire, and archive Scenes while preserving history.
- [x] Create a versioned launch snapshot and launch exactly one Session from it.
- [x] Enter, pause, resume, close, and review a bounded Session shell; action resolution is delegated to MV-IA-F006.
- [x] Preserve draft edits, authoritative saves, launch records, Session Events, and current projections as distinct states.
- [x] Support desktop, tablet, mobile, keyboard, touch, screen-reader, high-zoom, reduced-motion, and noncolor-status use.
- [x] Provide deterministic fixtures, denied cases, recovery paths, and twenty blocking acceptance criteria.

### Explicitly excluded

- [x] Full combat, initiative, movement, targeting, damage, and Condition resolution.
- [x] Full Encounter Builder and Balance Lab; MV-IA-F012 owns composition analysis and bounded simulation.
- [x] Full map authoring, fog-of-war drawing, dynamic lighting, measurement, or advanced tactical positioning.
- [x] Full social, relationship, investigation, faction, world-building, inventory, vehicle, crafting, and adventure-flow interfaces.
- [x] Public Campaign discovery, marketplace, ratings, paid hosting, or public invitations.
- [x] Automatic AI Campaign, Scene, NPC, encounter, map, or story generation.
- [x] AI mutation or Session launch authority.
- [x] Offline authoritative Campaign, Scene, invitation, membership, permission, pack, or Session mutation.
- [x] Silent rules-profile, schema, pack-lock, Character, or Scene migration.
- [x] Destructive deletion of launched or historically referenced state.
- [x] Production provider selection, production credentials, real-user data collection, internal-alpha release, production deployment, or public release.

### Full long-term scope deferred

Later work may add reusable campaign templates, richer calendars, branching story graphs, clocks, automated encounter recommendations, shared GM teams, campaign transfer, public or private publishing, advanced maps, media pipelines, localization, and optional governed AI assistance. These additions must preserve stable IDs, source-versus-placement separation, launch snapshots, role-safe projections, Event history, recovery, and explicit owner gates.

## 3. Roles and authority

| Role | Allowed actions | Hidden information | Approval required |
|---|---|---|---|
| Player | Accept invitation; view authorized Campaign and Session projections; select an eligible controlled Character where policy permits; enter launched Session | Cannot read GM notes, hidden placements, secret objectives, unrevealed clues, hidden counts, other Players' private notes, or restricted source content | Character activation or control may require GM approval under Campaign policy |
| Game Master | Create and configure Campaign; manage ordinary invitations and memberships; create and validate Scenes; assign visibility; preview as Player; launch, pause, resume, and close Session | Cannot read Player-private notes unless separately authorized; cannot bypass owner-only gates | Canon, paid services, production, release, destructive migration, and owner-reserved administration require Owner approval |
| Assistant GM | Perform explicitly delegated preparation and Session actions within scope and expiry | Cannot infer full GM authority, alter delegation, access excluded private fields, or perform owner-only actions | Delegation must be explicit and current; sensitive actions may require GM approval |
| Observer | View an observer-safe Campaign or Session projection when explicitly granted | No hidden GM state, Player-private state, ungranted Character state, or protected counts | Observer access must be explicitly granted and may expire |
| Owner/Admin | Perform governed administrative recovery and policy actions | Ordinary access remains purpose- and scope-bound; administration is not automatic access to all private content | Owner remains final authority for owner-reserved decisions |
| Content Creator | Inspect permitted source-linked objects and create separate creator drafts | Cannot mutate Campaign or Session state without a separate Campaign role | Canonical promotion remains a separate governed process |
| Service actor | Validate, persist, project, notify, recover, and export within a scoped service contract | Receives only fields necessary for the operation | No independent membership, role, ownership, entitlement, or launch authority |
| AI assistive actor | Optional read-only or proposal-only assistance from a narrower initiating-subject projection | No hidden state beyond the initiating subject, no credentials, no independent authority | Every mutation or launch remains human-initiated and server-authorized |

## 4. Dependencies

### Feature dependencies

- MV-IA-F002 — Universal Object Experience.
- MV-IA-F003 — Identity, Dashboard, and Workspace Selection.
- MV-IA-F004 — Character Creation and Advancement.
- MV-IA-F019 — Content Library and Entitlements.
- MV-IA-F020 — Permissions and Hidden Information.
- MV-IA-F021 — Autosave, Reconnect, Recovery, and Bounded Offline Use.
- MV-IA-F024 — Accessibility and Adaptive Interface.
- MV-IA-F025 — Onboarding, Help, Diagnostics, and Issue Reporting.

### Shared-foundation contracts consumed

SFI-C001 through SFI-C024 apply. The most direct controls are:

- SFI-C001 stable subject identity;
- SFI-C003 role and membership separation;
- SFI-C004 nonauthoritative selected-context receipts;
- SFI-C005 deny-by-default authorization;
- SFI-C006 field-safe projection;
- SFI-C007 safe non-disclosure;
- SFI-C008 permission-filtered object query;
- SFI-C009 stable-ID selection receipts;
- SFI-C010 local draft separation;
- SFI-C011 authoritative save and command;
- SFI-C012 ambiguous-failure lookup;
- SFI-C013 durable Event recovery;
- SFI-C014 revocation invalidation;
- SFI-C015 bounded offline use;
- SFI-C016 exact release identity;
- SFI-C017 safe diagnostics;
- SFI-C019 separate support access;
- SFI-C021 accessibility equivalence;
- SFI-C022 responsive context preservation;
- SFI-C023 provider-neutral ports;
- SFI-C024 zero-service core path.

### Service ports and adapters

- CampaignRepositoryPort
- SceneRepositoryPort
- SessionRepositoryPort
- MembershipAndInvitationPort
- CharacterControlPort
- AuthorizationAndProjectionPort
- EntitlementEvaluationPort
- PackRegistryAndLockPort
- ObjectQueryAndSelectionPort
- ValidationAndCompatibilityPort
- RealtimeAdvisoryPort
- EventStoreAndProjectionPort
- NotificationPort
- MediaReferencePort
- BackupRestoreExportPort
- ClockPort and IdGeneratorPort

### Canonical objects and packs

Campaign, rules profile, pack lock, membership, invitation, role grant, Character-control grant, Scene, Scene placement, Scene note, map/media reference, Location, environment, hazard, creature, NPC, item, vehicle, clue, objective, Session launch snapshot, Session, Event, checkpoint, and projection.

### Schemas and migrations

Campaign, Scene, placement, note, invitation, membership, role grant, Character-control, launch snapshot, Session, Event, projection, media-reference, pack-lock, and export schemas must be versioned. Migration must preserve stable IDs, visibility, source references, launch snapshots, Event order, and historical readability.

### Decisions and gates

- Active P9-06 dependencies remain implementation gates.
- Owner approval is required for production providers, spending, credentials, real tester-data collection, internal-alpha release, production, public release, canonical promotion, and destructive migration.
- Campaign-local creation does not create canonical content.

## 5. Object and state model

### Reusable Definitions

Rules profiles, content-pack records, Scene templates, Locations, environments, hazards, creatures, NPCs, items, vehicles, clues, objectives, map metadata, and other governed source objects remain immutable versioned Definitions from the Campaign builder's perspective.

### Campaign placements or bindings

A Campaign aggregate records:

- campaignId and version;
- owner subject and authorized GM team;
- rulesProfileId and rulesProfileVersion;
- creationPolicyId and advancementPolicyId;
- packLockDigest and exact pack versions;
- entitlement-policy reference;
- membership, role, observer, and Character-control bindings;
- Campaign-local labels, descriptions, notes, flags, and settings;
- Scene order and archived-state references;
- current schema versions and migration state.

A Scene aggregate records:

- sceneId, campaignId, version, lifecycle state, and optional template source;
- title, summary, accessible description, and role-scoped notes;
- stable-ID placements with placementId, source definition version, local overrides, quantity, visibility, and initial state;
- Location and environment bindings;
- map or media references plus nonvisual alternative;
- participants, eligible Characters, objectives, entry conditions, launch configuration, and dependency evidence;
- validation status and latest launch-snapshot reference.

### Live instances and state

A Session is created from an immutable launch snapshot. It records sessionId, campaignId, sceneId, snapshotId, lifecycle state, participant and Character bindings, authoritative Event sequence, current projection version, checkpoints, and close record.

The live Session never reads mutable Scene draft fields as authority. Post-launch Scene edits affect only a later launch or explicit governed amendment.

### Events and history

Required Event families include CampaignCreated, CampaignPolicyChanged, PackLockChanged, InvitationIssued, InvitationAccepted, MembershipChanged, RoleGrantChanged, CharacterControlChanged, SceneCreated, SceneUpdated, PlacementAdded, PlacementUpdated, NoteVisibilityChanged, SceneValidated, LaunchSnapshotCreated, SessionLaunched, SessionPaused, SessionResumed, SessionClosed, CampaignArchived, SceneArchived, MigrationApplied, and RecoveryCompleted.

### Projections and indexes

Separate projections are required for GM preparation, Assistant-GM scope, Player Campaign view, Player Session entry, observer view, preview-as-subject, dashboard cards, invitation lookup, notifications, export, diagnostics, and optional AI. Every projection is generated after authorization and entitlement evaluation.

### Stable IDs

Display names, email, provider IDs, file names, map labels, and Scene order never replace stable IDs. Placement IDs are distinct from source Definition IDs. Launch snapshot IDs are distinct from Scene IDs. Session IDs are distinct from launch snapshot IDs.

### Provenance

Every placement and policy binding records source identity, version, pack identity, pack version, selection receipt, actor, timestamp, and local-override provenance. Synthetic fixtures are explicitly marked synthetic.

## 6. Primary user flow

1. An authenticated subject enters an authorized GM dashboard and selects or creates a Campaign.
2. The server resolves subject, active role, membership, selected context, permissions, entitlements, schema versions, and release identity.
3. The GM binds an approved rules profile, pack set, Character policy, visibility defaults, and participant policy.
4. The GM saves the Campaign with expectedVersion and idempotencyKey and receives an authoritative receipt.
5. The GM issues invitations with explicit role, scope, expiry, and policy.
6. Invitees accept through an idempotent server command; membership and role are created separately.
7. The GM creates a Scene draft and adds title, accessible description, notes, objectives, entry settings, and eligible participants.
8. The GM browses authorized content and selects source objects by stable ID.
9. The caller validates each selection and creates Campaign-local placements without changing source Definitions.
10. The GM adds a map or visual reference and a required nonvisual alternative.
11. The server validates references, permissions, entitlements, pack compatibility, Character eligibility, required dependencies, visibility, and launch configuration.
12. The GM previews the server-generated projection for a selected Player or observer.
13. The GM resolves blocking findings and requests a versioned launch snapshot.
14. The server reauthorizes, revalidates, freezes the launch inputs, records the snapshot, and returns a receipt.
15. The GM launches with a separate idempotent command referencing the snapshot.
16. The server creates the Session, emits SessionLaunched, initializes the Event sequence and projections, and notifies authorized participants.
17. Players enter the Session through current authorization and Character-control checks.
18. Realtime delivery is advisory; durable Events and current projections control recovery.

## 7. Alternate and secondary flows

### Assistant-GM preparation

An Assistant GM edits only within an explicit delegation scope and expiry. Every save revalidates delegation. Losing delegation preserves permitted local draft metadata but blocks further authoritative saves and removes protected projections.

### Player invitation and Character selection

A Player accepts an invitation, sees the Campaign's safe entry projection, and selects from Characters they control and that the Campaign currently accepts. Selection does not grant control. The server revalidates Character lifecycle, pack compatibility, entitlements, and control at Session entry.

### Duplicate Scene

Duplicating a Scene creates a new sceneId and draft history. Placements receive new placementIds while retaining source Definition provenance. Launch snapshots and Session history are never copied as live authority.

### Edit after launch

Editing the Scene after launch creates a new draft version. The active Session remains bound to its launch snapshot. A later change requires a governed amendment or a new Session; silent mutation is prohibited.

### Preview as Player

Preview is generated server-side from the selected subject's actual or simulated authorized context. It cannot grant permission, cannot reveal fields withheld from that subject, and is labeled nonauthoritative for final launch checks.

### Archive and restore

Archiving removes ordinary discovery and blocks new launch while preserving history, references, exports, and authorized review. Restore requires authorization, compatibility validation, and a new version.

## 8. Failure, empty, and recovery states

| State | User sees | Allowed action | Preserved data | Evidence |
|---|---|---|---|---|
| Loading | Semantic progress and current workspace identity | Cancel navigation where safe | Local draft and selected context | correlationId |
| Empty Campaign | Guided first Campaign or Scene action | Create, import permitted template, or leave | No invented data | empty-state reason |
| Validation error | Grouped blocking and warning findings linked to fields and sources | Correct, inspect source, or save draft | All draft edits | validation receipt |
| Forbidden | Safe unavailable state without protected existence details | Return to dashboard | Permitted local metadata only | user-safe reason code |
| Restricted entitlement | Accessible explanation and permitted alternatives | Request grant, replace object, or save draft | Existing historical references | entitlement decision reference |
| Missing pack | Exact permitted dependency problem | Install through governed path, replace, or defer | Draft and prior launch history | pack-lock evidence |
| Offline | Offline banner and authority limits | Read manifest-bound cache and edit approved local notes/draft fields | Local draft only | offline manifest |
| Stale | Current server version and changed-area summary where permitted | Reload, compare, or preserve copy | Both versions | expected/current version |
| Conflict | Non-destructive comparison | Merge permitted fields or save a new draft copy | Both drafts | conflict receipt |
| Failed save | Clear unsaved state and retry/status action | Query operation status before new retry | Local draft | operationId |
| Revoked | Immediate removal of protected projection and controls | Leave workspace or request new authorization | Only permitted local metadata | revocation record |
| Migration required | Read-only status with compatibility details | Run approved migration or export | Pre-migration state and backup reference | migration plan ID |
| Launch blocked | Readiness checklist with blocking findings | Resolve or return to draft | Draft and validation history | launch-readiness receipt |
| Ambiguous launch | Session status lookup, never a second blind launch | Query by operationId and snapshotId | Snapshot and operation identity | launch receipt or status |
| Event gap | Reconnecting state | Fetch Events from last acknowledged sequence and current projection | Local UI context | sequence evidence |
| Recovery required | Last verified checkpoint and safe options | Resume, restore approved checkpoint, or export | Event history and checkpoint | recovery receipt |

## 9. Permissions and hidden information

Authorization occurs before query, ranking, counts, notifications, realtime subscription, export, diagnostics, media retrieval, and AI projection.

Protected surfaces include:

- GM notes and Assistant-GM-only notes;
- unrevealed placements, clues, objectives, motives, hazards, and creatures;
- exact hidden counts, hidden labels, hidden relationship edges, and hidden source IDs;
- Player-private notes and private Character fields;
- invitation existence and recipient details;
- membership, observer, and Character-control records outside authorized scope;
- unpublished Scenes, archived Scenes, launch snapshots, checkpoints, and migration evidence;
- map layers, media metadata, attachment URLs, and storage identifiers;
- exports, diagnostics, logs, caches, and optional AI context.

Required denied cases include wrong Campaign, wrong Scene, wrong Session, unaccepted invitation, expired invitation, revoked member, wrong role, expired delegation, uncontrolled Character, archived Scene launch, hidden placement lookup, exact hidden-count query, unauthorized map retrieval, stale permission version, stale pack lock, client-forged preview, client-forged launch snapshot, duplicate launch, offline launch, and support actor without separate support access.

## 10. Entitlements

- Access sources: free content, Campaign grants, approved account grants, owner-approved test fixtures, and historical state.
- Campaign grants never replace permission, membership, role, or Character control.
- Entitlement filtering occurs before object results, facets, counts, suggestions, previews, and serialization.
- Historical launched Sessions retain readable source identity and safe historical projections even after new selection rights expire.
- Expired access blocks new placement or replacement but does not silently delete historical placement or Session evidence.
- Offline snapshots are bound to subject, Campaign, permission version, entitlement version, pack lock, digest, and expiry.

## 11. Persistence and history

- Draft storage: local drafts are nonauthoritative and partitioned by subject, workspace, campaignId, sceneId, and release identity.
- Authoritative save: online, expected-version, idempotent, reauthorized, validated, and receipted.
- Aggregate boundaries: Campaign, Scene, invitation/membership grant, launch snapshot, and Session are separately versioned aggregates with explicit cross-aggregate validation.
- Expected-version behavior: stale writes never silently overwrite.
- Idempotency: create, save, invitation, acceptance, role grant, Character control, snapshot, launch, pause, resume, close, archive, restore, migration, and recovery operations require stable operation identity.
- Snapshot behavior: launch snapshots are immutable; recovery checkpoints are integrity-checked and do not erase Event history.
- Audit events: actor, subject, role, scope, decision references, operation, version, timestamp, correlation, and safe reason.
- Migration: preflight, backup reference, dry-run evidence where practical, atomic or resumable execution, validation, rollback or forward recovery, and provider-exit compatibility.
- Export: provider-neutral Campaign package with schemas, stable IDs, pack references, visibility labels, Scene versions, launch snapshots, Session Event history, checksums, and redaction policy.

## 12. Realtime, interruption, and reconnect

- Before local submission: retain local draft and show unsaved state.
- After submission before response: query by operationId before retry.
- After accepted save before display: fetch current aggregate projection and receipt.
- During invitation acceptance: lookup invitation-operation status before repeating.
- During launch: query by operationId and snapshotId; never create a second Session blindly.
- During pending GM work: preserve draft, delegation evidence, and current authoritative version separately.
- After missed Events: resume from lastAcknowledgedSequence, then fetch current projection.
- With stale client: block mutation until schema, protocol, permission, entitlement, pack lock, and expected version are current.
- From a second device: expose conflict rather than last-write-wins.
- After service restart: rebuild from durable state and Event history; realtime messages are not authority.

## 13. Interface and information hierarchy

### Desktop

Use a three-region GM workspace: Campaign/Scene outline, primary editor or Session view, and contextual inspector/validation panel. Persistent global controls show Campaign, role, save state, preview target, and launch readiness. Dense data remains progressively disclosed.

### Tablet

Use a collapsible outline and inspector around a full-width editor. Preserve selected Scene, validation location, unsaved state, preview target, and launch state when panels close.

### Mobile

Use a single-focus sequence with Campaign/Scene switcher, editor sections, object picker, notes, validation, preview, and launch review as separate screens or sheets. Critical actions require clear confirmation and never depend on hover or drag.

### Player hierarchy

Foreground Campaign identity, invitation state, controlled Character choice, Session status, visible Scene summary, objectives, and entry action. GM preparation tools and hidden-information indicators are absent, not merely visually concealed.

### GM hierarchy

Foreground current Campaign and Scene, save state, validation blockers, participant and Character eligibility, hidden-information controls, preview-as-Player, pack-lock identity, and launch readiness. Rules and source inspection are one action away.

## 14. Accessibility

- Semantic headings, landmarks, forms, outlines, lists, dialogs, tabs, and status regions.
- Full keyboard creation, reordering, selection, validation, preview, and launch flow.
- Nondrag alternatives for Scene order, placements, map markers, and participant arrangement.
- Predictable focus after save, error, drawer, preview, and launch transitions.
- Screen-reader names for visibility, lifecycle, validation severity, save state, role scope, and Session state.
- Live announcements for save result, validation change, invitation result, launch state, reconnect, revocation, and conflict.
- Text scaling and reflow without loss of action or evidence.
- Status never communicated by color alone.
- Reduced-motion alternatives for transitions and map movement.
- Touch targets and spacing suitable for mobile and tablet.
- Every map or visual requires an equivalent structured nonvisual description and object list.
- Errors identify the field, reason, source, and recovery action.

## 15. Notifications and queues

| Trigger | Recipient | Message content | Action | Resolution state |
|---|---|---|---|---|
| Invitation issued | Invitee | Campaign-safe identity, inviter, proposed role, expiry | Accept or decline | accepted, declined, expired, revoked |
| Character review required | GM queue | Character-safe summary and policy findings | Review | approved, denied, revision requested |
| Scene validation blocked | Authorized editor | Scene and safe blocker summary | Open validation | resolved or waived only where policy permits |
| Launch snapshot ready | GM | Snapshot identity, Scene version, participant count, warnings | Review and launch | launched, expired, superseded |
| Session launched | Authorized participants | Campaign, Session, visible Scene summary, entry action | Enter | entered, missed, revoked |
| Permission or role revoked | Affected subject | Safe access-change message | Return to dashboard | acknowledged |
| Session paused/resumed/closed | Authorized participants | Current safe state | Return or review | current Session state |
| Migration required | Authorized GM/Owner | Scope and safe compatibility summary | Review plan | migrated, deferred, blocked |

Notifications are projections, not authority. Opening them revalidates current access.

## 16. AI involvement

**AI mode:** none required; optional read-only explanation or proposal support only.

Allowed future assistance may summarize visible Scene structure, identify unresolved validation findings, or propose draft text from sources already visible to the initiating subject. AI receives a narrower permission- and entitlement-safe projection, explicit source references, uncertainty, and cost boundary.

AI may not discover hidden information, infer denied counts, accept invitations, change membership or roles, grant Character control, mutate Campaign or Scene state, create launch snapshots, launch or control Sessions, approve migration, spend money, publish content, or authorize release. The complete alpha path works with zero AI.

## 17. Telemetry and diagnostics

Allowlisted operational evidence may include operationId, correlationId, release identity, schema versions, aggregate type, safe lifecycle state, duration, result class, validation-class counts, reconnect count, Event-gap size, and user-safe reason codes.

Exclude by default Campaign prose, notes, secrets, map contents, Character details, invitation recipient data, hidden object IDs, raw authorization policies, tokens, credentials, storage URLs, provider payloads, and private content. Diagnostic attachment requires redaction, preview, explicit consent, checksum, and issue-report handling under MV-IA-F025.

## 18. Test scenarios

### Unit

- Campaign and Scene lifecycle transition rules.
- Placement source-versus-instance separation.
- visibility label evaluation.
- invitation expiry and idempotency.
- launch-readiness rule evaluation.

### Contract

- provider-neutral repository and Event ports.
- authorization and entitlement projections.
- object-selection receipts and caller validation.
- Character-control verification.
- launch snapshot immutability.

### Integration

- Campaign creation through Scene save.
- invitation through membership.
- Character eligibility through Session entry.
- Scene validation through launch snapshot and Session creation.
- pack update, migration, export, restore, and provider-exit round trip.

### End-to-end

- GM creates Campaign, invites two Players, creates a Scene, adds governed objects and hidden notes, previews each Player, launches, and both Players enter with controlled Characters.
- reconnect after launch recovers from durable Events without duplicate Session creation.

### Permission and hidden information

- wrong-Campaign, wrong-role, revoked, observer, Player, Assistant-GM, support, and AI denied cases.
- no hidden counts, labels, source IDs, map layers, or note content leak through search, errors, notifications, exports, diagnostics, or caches.

### Entitlement

- free, Campaign-granted, restricted, expired, historical, offline-manifest, and pack-removal cases.

### Persistence and migration

- expected-version conflict, duplicate operation, checkpoint integrity, interrupted migration, backup checksum mismatch, export/import, and historical launch readability.

### Reconnect and recovery

- interruption before save, after save before response, during invitation acceptance, during snapshot creation, during launch, after Event gap, after revocation, and after service restart.

### Accessibility

- complete GM and Player flows with keyboard and screen reader; 200% and 400% zoom; narrow mobile; touch; reduced motion; noncolor state; nondrag ordering; map alternative.

### Performance

- bounded Campaign and Scene open, object picker, validation, preview, snapshot, launch, and reconnect budgets measured with deterministic fixtures.

### Golden or deterministic regression

- 8D-007J applies to launch-readiness validation, placement compatibility, visibility projection, invitation transitions, snapshot identity, Event ordering, and recovery results.

## 19. Acceptance criteria

1. **CSS-AC-001 — Campaign authority:** Campaign creation and every mutation are online, reauthorized, expected-versioned, idempotent, validated, and receipted. **Blocking:** yes.
2. **CSS-AC-002 — Policy binding:** A Campaign records exact rules profile, Character policies, schema versions, entitlement version, and pack-lock digest. **Blocking:** yes.
3. **CSS-AC-003 — Role separation:** Membership, role, delegation, observer access, ownership, entitlement, and Character control remain separate versioned decisions. **Blocking:** yes.
4. **CSS-AC-004 — Invitation lifecycle:** Issue, accept, decline, expire, revoke, and reissue are safe, attributable, and idempotent. **Blocking:** yes.
5. **CSS-AC-005 — Stable selection:** Scene objects are selected by stable ID with permission and entitlement filtering before ranking, counts, and serialization. **Blocking:** yes.
6. **CSS-AC-006 — Source separation:** Campaign placements and local overrides never mutate reusable source Definitions. **Blocking:** yes.
7. **CSS-AC-007 — Hidden information:** Unauthorized notes, placements, counts, relationships, objectives, map data, and identifiers never reach ordinary client state. **Blocking:** yes.
8. **CSS-AC-008 — Player preview:** Preview is server-generated, subject-scoped, nonauthoritative, and contains no fields unavailable to the previewed subject. **Blocking:** yes.
9. **CSS-AC-009 — Scene validation:** Launch blocks on invalid references, permissions, entitlements, packs, Character eligibility, required dependencies, or unsafe visibility. **Blocking:** yes.
10. **CSS-AC-010 — Snapshot immutability:** Every Session launches from an immutable versioned snapshot, never directly from a mutable Scene draft. **Blocking:** yes.
11. **CSS-AC-011 — Exactly-once launch:** Ambiguous or duplicate launch requests resolve by operation and snapshot identity without duplicate Sessions. **Blocking:** yes.
12. **CSS-AC-012 — Session entry:** Entry revalidates current membership, role, permission, entitlement, Character control, Character lifecycle, pack lock, and protocol compatibility. **Blocking:** yes.
13. **CSS-AC-013 — Event authority:** Realtime remains advisory; durable ordered Events and current server projections recover Session state. **Blocking:** yes.
14. **CSS-AC-014 — Concurrency:** Concurrent Campaign or Scene edits preserve both versions and never silently overwrite. **Blocking:** yes.
15. **CSS-AC-015 — Revocation:** Revocation ends subscriptions, invalidates selected context, removes protected projections and counts, and blocks new mutations immediately. **Blocking:** yes.
16. **CSS-AC-016 — Bounded offline:** Offline permits only manifest-bound reading and approved local drafts; no authoritative invitation, membership, permission, pack, snapshot, launch, or Session mutation. **Blocking:** yes.
17. **CSS-AC-017 — History and migration:** Archive, restore, migration, correction, backup, restore, and export preserve stable IDs, visibility, snapshots, Events, checksums, and historical readability. **Blocking:** yes.
18. **CSS-AC-018 — Accessibility and responsive parity:** Desktop, tablet, mobile, keyboard, touch, screen reader, zoom, reduced motion, and noncolor paths preserve authority, evidence, and recovery. **Blocking:** yes.
19. **CSS-AC-019 — Diagnostics and support:** Diagnostics are allowlisted and redacted; an issue never grants Campaign access; support access is separate, scoped, attributed, and expiring. **Blocking:** yes.
20. **CSS-AC-020 — Provider and cost boundary:** Core operation uses provider-neutral ports, deterministic local adapters, zero paid services, and zero AI; implementation and release gates remain explicit. **Blocking:** yes.

## 20. Fixtures and approved alpha content

- Identities: Owner/Admin, primary GM, Assistant GM, two Players, observer, revoked former participant, content creator, service actor, AI actor without authority.
- Campaigns: IA-CAMPAIGN-01 core Campaign and IA-CAMPAIGN-02 isolation Campaign.
- Characters: two valid controlled Characters, one invalid, one restricted, one archived, one migration-required.
- Scenes: social, investigation, combat-preparation, travel/vehicle, and recovery Scenes.
- Objects: representative Location, environments, hazards, creatures, NPCs, items, vehicle, clues, objectives, notes, map reference, and hidden placements.
- History: prior Scene versions, one launch snapshot, Session Event history, checkpoint, archived Scene, invitation history, role change, and Character-control change.
- Failures: missing dependency, invalid stable ID, stale object, expired invitation, duplicate acceptance, revoked member, wrong Campaign, failed save, conflict, stale pack lock, corrupted draft, ambiguous launch, Event gap, migration interruption, backup checksum mismatch, provider-exit mismatch.

## 21. Security, privacy, cost, and risk

### Security

Deny by default; authorize every read and mutation; use safe non-disclosure; isolate Campaigns; validate storage and media access; revalidate at launch and Session entry; preserve audit evidence; prevent client-forged roles, preview, placement, snapshot, or Session state.

### Privacy

Minimize personal data in invitations and logs. Keep Player-private notes, GM notes, maps, Campaign prose, and hidden content out of diagnostics and ordinary support access. Provide portable deletion and retention controls only through later approved policy.

### Cost

The core path requires no paid identity, search, analytics, crash-reporting, ticketing, realtime, map, notification, media, or AI service. Local deterministic adapters and repository fixtures must support design validation.

### Material risks

Hidden-information leakage, duplicate Sessions, stale launch inputs, cross-Campaign access, implicit Character control, lost preparation, incompatible pack changes, destructive migration, inaccessible dense interfaces, and accidental provider coupling.

### Stop conditions

Stop implementation or release on any unresolved blocking acceptance criterion, hidden-information leak, duplicate authoritative operation, cross-Campaign access, destructive history loss, unverifiable launch snapshot, nonrecoverable migration, missing accessibility path, owner-only gate, or unapproved spending/provider requirement.

## 22. Owner review points

- Design approval required before implementation work order.
- Owner decision required for production providers, spending, credentials, real tester-data collection, retention, external media hosting, internal-alpha release, production, and public release.
- Canon approval required before Campaign-local creator material becomes canonical.
- Scope approval required before advanced maps, public Campaigns, broad offline mutation, or AI generation is promoted.
- Silence is not approval.

## 23. Implementation handoff

**Target repository:** `cybalicistjt-stack/Multiversal-app` after dependencies and gates are ready.  
**Registered work type:** bounded Stage A feature implementation work order.  
**Decision level:** owner-approved design; implementation remains governed.  
**Risk class:** high because it controls permissions, hidden information, Campaign isolation, preparation persistence, launch authority, and Session creation.  
**Suggested work-order title:** Implement MV-IA-F005 Campaign, Scene, and Session Builder vertical slice.  
**Expected branches or files:** domain contracts, schemas, migrations, ports, local adapters, authorization projections, Campaign and Scene UI, launch service, Session shell, fixtures, tests, and documentation.  
**Required reviewers:** architecture, security/privacy, game systems, UX/accessibility, persistence/recovery, QA, and owner-design review.  
**Required gates:** P9-06 dependencies, IA-D02-006 conformance, MV-IA-F004 contracts, schema and migration validation, permission tests, recovery tests, accessibility tests, CI, and owner release gate.  
**Rollback or recovery:** versioned migration rollback or forward recovery, verified backup reference, immutable launch snapshots, Event replay, and provider-neutral export.  
**Evidence outputs:** test reports, permission matrix results, launch idempotency evidence, recovery evidence, accessibility evidence, performance measurements, migration evidence, and implementation completion record.

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

**Final design status:** implementation-ready; application implementation remains dependency-gated and has not started.  
**Reviewer:** governed multidisciplinary review required at implementation entry.  
**Date:** 2026-08-05  
**Packet digest:** generated and recorded by repository validation at implementation handoff.

## Next design action

**IA-D03-003 — Design MV-IA-F012, Encounter Builder and Balance Lab.**
