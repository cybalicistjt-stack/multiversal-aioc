# MV-IA-F020 — Permissions and Hidden Information

**Feature ID:** MV-IA-F020  
**Feature version:** 0.1.0  
**Classification:** entry-critical  
**Design status:** implementation-ready  
**Owner:** John Brandon Turner  
**Primary roles:** Player, Game Master, Assistant GM, Content Creator, Owner/Admin, Observer, service actor, optional AI service actor  
**Stage A mapping:** A3/A5/A6/A12  
**Historical module mapping:** none; cross-cutting platform boundary  
**Prepared by:** Lead Documentation Architect / Security and Product Requirements Steward  
**Reviewed by:** architecture, security, privacy, QA, UX/accessibility, data, and documentation roles required before implementation  
**Date:** 2026-08-05

## 1. Problem and user outcome

### Problem

Multiversal combines public canonical content, Campaign-private state, Player-private notes, Character-controller data, GM-only truth, hidden clues and motives, unrevealed maps and encounters, restricted content, creator drafts, operational metadata, and security-sensitive records. The same object may expose different fields, relationships, actions, histories, counts, and source details to different subjects.

A UI-only permission system would be unsafe. Hiding a button or panel does not prevent disclosure through search results, counts, facets, exact stable-ID lookup, aliases, relationship traversal, comparison candidates, realtime messages, exports, cached state, diagnostics, backups, or AI retrieval. It also does not prevent an unauthorized mutation sent directly to a service.

### Required outcome

Every read, search, count, relationship, subscription, export, AI retrieval, and mutation is evaluated by a deny-by-default server policy using stable subject identity, Campaign membership, scoped role, delegation, object ownership or control, field classification, entitlement, pack state, lifecycle state, and current revocation status.

Player, GM, Assistant GM, creator, observer, Owner/Admin, and service actors receive distinct authorized projections. Hidden information is removed before publication. A client never receives protected fields and is never trusted to hide them.

### Why this belongs in internal alpha

This feature is entry-critical because the primary alpha journeys intentionally contain hidden NPC motives, unrevealed clues, private notes, GM-only Scene configuration, distinct Player and GM projections, Campaign isolation, approval queues, and optional AI retrieval. Internal alpha cannot begin safely until these boundaries work across the entire supported journey.

## 2. Alpha slice

### Included

- deny-by-default authorization for reads, writes, searches, subscriptions, exports, and AI retrieval;
- stable subject and service-actor context;
- Campaign membership and role resolution;
- Character controller and Asset ownership or custody checks where applicable;
- object-, action-, field-, relationship-, and event-level projection rules;
- Player-safe, GM-only, Player-private, Character-controller, creator-draft, operational, and security-sensitive classifications;
- safe search results, counts, facets, aliases, exact IDs, rankings, pagination, and autocomplete;
- safe Universal Object inspection, source views, provenance, comparison, and relationship traversal;
- server-generated “view as Player” preview for GMs;
- permission-safe realtime subscriptions, notifications, activity history, exports, diagnostics, and optional AI context;
- immediate mutation recheck and bounded revocation propagation;
- signed or verifiable bounded offline permission snapshots for approved read-only use;
- audit and security events that record decisions without logging protected content;
- desktop, tablet, mobile, keyboard, touch, and screen-reader behavior;
- deterministic denied-case, inference, revocation, and cross-Campaign fixtures.

### Explicitly excluded

- public self-service role creation;
- enterprise organization administration;
- production support impersonation;
- legal-discovery or law-enforcement workflows;
- public community moderation;
- anonymous public Campaign access;
- broad offline authoritative mutation;
- client-defined custom policy language;
- provider-specific row-security policy as the only authorization layer;
- Owner/Admin blanket access to Player-private or Campaign-private content without an explicit governed role and purpose;
- production identity-provider selection or credentials.

### Full long-term scope deferred

Later work may add organization tenancy, public sharing, moderated community content, richer delegation, time-bounded guest links, production support-access ceremonies, data-residency controls, and jurisdiction-specific privacy workflows. Those extensions must reuse the same subject, scope, field classification, reason-code, audit, revocation, and projection contracts.

## 3. Roles and authority

| Role | Allowed actions in the alpha slice | Hidden information | Approval required |
|---|---|---|---|
| Player | Read Player-safe Campaign and Session projections; control assigned Characters; maintain own private notes; submit permitted proposals | Cannot read GM-only truth, other Players’ private notes, unrevealed objects, unauthorized Characters, or hidden source extensions | GM approval for governed proposals; explicit acceptance for ownership or control transfers |
| Game Master | Read and manage GM-authorized Campaign state; configure visibility; reveal information; preview Player projection; adjudicate proposals | May read GM-only Campaign content only in Campaigns where the subject is an active GM | Destructive or canonical actions follow their separate gates |
| Assistant GM | Read and modify only delegated Campaign areas and fields | No automatic access to all GM-only content; delegation scope controls access | GM or Owner-approved delegation record |
| Content Creator | Read permitted canonical content and own or assigned drafts; submit proposals | No Campaign-private access unless separately a member; cannot see other creators’ private drafts | Owner approval for canonical promotion |
| Observer | Read the explicitly granted projection for one Campaign or Session | No control actions, private notes, hidden GM state, or ungranted history | GM or Owner grants and may revoke observation scope |
| Owner/Admin | Administer project and alpha operations; inspect operational metadata and authorization evidence | Owner status is not automatic permission to read Player-private or Campaign-private content; access requires a governed Campaign role or explicit support-access record | Owner-only support access must be attributable, time-bounded, purpose-bound, and audited |
| Service actor | Execute one narrow background capability under service identity | Receives only fields required for its job | Service registration and least-privilege policy |
| AI service actor | Optional read-only assistance using the initiating user’s already-authorized projection plus narrower tool policy | Never receives hidden content outside the initiating user’s projection; no silent role elevation | User invocation; mutation remains separately approval-gated |

### Authority invariants

1. Authentication does not imply authorization.
2. Entitlement does not imply Campaign membership.
3. Campaign membership does not imply access to every field.
4. Owner or technical administrator status does not silently imply access to private play content.
5. A UI state is not authority.
6. Cached permission data cannot authorize a mutation after revocation.
7. Service and database isolation must agree; neither replaces the other.
8. Silence, tool access, prior access, or a copied URL is not approval.

## 4. Dependencies

### Feature dependencies

- MV-IA-F001 — Application Shell and Workspace Navigation;
- MV-IA-F002 — Universal Object Experience;
- MV-IA-F003 — Identity, Dashboard, and Workspace Selection as the primary caller and role-context surface;
- MV-IA-F019 — Content Library and Entitlements for access-source decisions;
- MV-IA-F021 — Autosave, Reconnect, Recovery, and Bounded Offline Use for revocation, stale state, and permission snapshots;
- MV-IA-F024 — Pack Lifecycle and Canonical Content Registry for installed-version and object-lifecycle context.

F020 and F003 are co-designed. F020 depends on stable identity and membership contracts, not on a completed dashboard implementation. F003 consumes the F020 decision and projection contract.

### Shared systems

- SS-02 — Identity and role context;
- SS-03 — Authorization and visibility;
- SS-04 — Entitlement evaluation;
- SS-05 — Universal object experience;
- SS-07 — Persistence, drafts, and state versions;
- SS-08 — Realtime and reconnect;
- SS-09 — Relationship and graph model;
- SS-12 — Activity, history, and timeline;
- SS-13 — Notifications and work queues;
- SS-15 — Accessibility behavior;
- SS-16 — Responsive information hierarchy;
- SS-17 — Content pack lifecycle;
- SS-18 — Telemetry and diagnostics;
- SS-19 — Help and source-grounded explanation;
- SS-20 — Feature flags and experimental isolation.

### Service ports and adapters

- `IdentityPort` — resolve stable subject and identity assurance;
- `EntitlementPort` — evaluate content access separately from authorization;
- `PersistencePort` — transactional memberships, roles, delegations, classifications, versions, and audit events;
- `SessionCommandPort` — reauthorize every authoritative command;
- `RealtimePort` — authorize connection and each subscription or publication;
- `CheckpointPort` — produce role-safe checkpoint projections;
- `ObjectStoragePort` — issue scoped access to permitted media or artifacts;
- `TelemetryPort` — record privacy-safe denial and security evidence;
- proposed provider-neutral `AuthorizationPolicyPort` or equivalent domain service — evaluate actions and produce reasoned decisions without exposing provider-specific policy types.

### Canonical objects and packs

- subject, identity, Campaign, membership, role, delegation, Character controller, ownership, visibility classification, field policy, object relationship, content pack, pack installation, canonical object, Scene, clue, note, Session participant, event, projection, export, and AI request records;
- the version-pinned internal-alpha corpus;
- synthetic permission, revocation, inference, and Campaign-isolation fixtures.

### Schemas and migrations

- authorization request and decision schemas;
- role and capability schema;
- membership and delegation schema;
- field-classification and visibility schema;
- projection and redaction schema;
- permission snapshot schema;
- audit and security-event schemas;
- policy-version migration and cache-invalidation contracts.

### Decisions and gates

- P9-04 deny-by-default server authority and database-isolation contract;
- P9-06 identity, persistence, session, backup, restore, and provider-exit sequence;
- AG-02 provider-neutral boundaries;
- AG-04 identity and entitlements;
- AG-05 authoritative Sessions;
- AG-07 two-device alpha;
- owner release decision before internal alpha.

## 5. Object and state model

### Reusable Definitions

- `RoleDefinition` — named role with bounded capabilities and prohibited capabilities;
- `CapabilityDefinition` — stable action such as `object.read`, `scene.edit`, `session.approve`, `export.create`;
- `VisibilityClassDefinition` — semantic class and default disclosure behavior;
- `FieldPolicyDefinition` — object family and field-path classification;
- `DecisionReasonDefinition` — stable internal and user-safe reason codes;
- `DelegationProfileDefinition` — allowed scope, duration, grantor, and revocation rules.

### Campaign placements or bindings

- Campaign membership;
- Campaign role assignment;
- Assistant GM delegation;
- Character controller assignment;
- observer grant;
- Campaign-local visibility override where the governing schema permits it;
- Campaign grant and installed-pack context.

### Live instances and state

- active subject session;
- active Campaign, Character, and Session context;
- current membership and revocation state;
- current role and delegation set;
- current object lifecycle and reveal state;
- pending proposal or approval context;
- realtime connection and subscription set;
- bounded offline permission snapshot;
- support-access session when explicitly owner-approved.

### Events and history

- membership granted, changed, revoked, or expired;
- role assigned or removed;
- delegation created, narrowed, revoked, or expired;
- Character control transferred;
- visibility revealed, concealed where policy permits, or corrected;
- private-note ownership changed only through explicit workflow;
- permission denied at a security-relevant boundary;
- export authorized or denied;
- AI retrieval authorized or denied;
- support access started and ended;
- permission snapshot issued or invalidated.

Authorization decisions are not all persisted as full audit events. High-volume benign denials may be aggregated in privacy-safe telemetry. Material changes and security-sensitive denials are append-only events.

### Projections and indexes

- `AuthorizedObjectProjection`;
- `AuthorizedSearchResultProjection`;
- `AuthorizedRelationshipProjection`;
- `AuthorizedSessionProjection`;
- `AuthorizedNotificationProjection`;
- `AuthorizedActivityProjection`;
- `AuthorizedExportProjection`;
- `AuthorizedAIContextProjection`;
- permission-aware search and relationship indexes;
- subject-scoped cache entries with policy version and expiry.

### Stable IDs

Stable IDs are required for subjects, identities, Campaigns, memberships, roles, capabilities, delegations, Characters, objects, fields or policy paths, relationships, Sessions, commands, events, permission snapshots, exports, and audit records.

Provider user IDs, email addresses, display names, URLs, and client cache keys never replace internal stable IDs.

### Provenance

Every policy and projection rule records:

- governing policy or schema version;
- owner or source decision;
- object family and field path;
- default behavior;
- allowed scope;
- exception or delegation source;
- migration history.

## 6. Primary user flow

### Player and GM projection proof

1. The Player authenticates and resolves to a stable subject.
2. The service resolves active Campaign membership, Player role, controlled Character, installed packs, entitlement context, and current policy version.
3. The Player opens the Universal Object Experience within the Campaign.
4. The service filters candidate objects before counting, faceting, ranking, or pagination.
5. The Player receives only permitted result records and permitted fields.
6. The Player opens an object. The service returns a Player-safe inspector projection; GM-only extension fields, hidden relationships, and protected source material are absent.
7. The Player selects a permitted object into the Character or Scene caller. The service rechecks selection scope and returns an attributable selection receipt.
8. The GM opens the same object in the same Campaign and receives the GM-authorized projection.
9. The GM chooses “Preview as Player.” The server creates the selected Player projection; the client does not merely hide GM fields.
10. The GM reveals a previously hidden clue through an authorized action.
11. The reveal commits an event, invalidates affected caches, and publishes role-filtered realtime updates.
12. The Player receives the newly permitted clue without receiving unrelated GM truth.
13. Audit and telemetry record the policy version, operation ID, subject, scope, decision, and reason without logging hidden content.

## 7. Alternate and secondary flows

### Alternate flow A — Assistant GM delegation

1. A GM creates a bounded delegation for encounter preparation but excludes private Player notes and unrevealed investigation truth.
2. The Assistant GM accepts the delegation.
3. The subject receives only the delegated capabilities and fields.
4. Expiry or revocation immediately prevents new mutations and closes affected subscriptions.
5. Existing screens move to a stale or forbidden state and offer a safe return path.

### Alternate flow B — Character controller transfer

1. A GM or authorized controller proposes transfer of Character control.
2. The recipient accepts when required.
3. The authoritative controller record changes transactionally.
4. Old-controller caches and subscriptions invalidate.
5. Private Player notes do not transfer unless the separate note-ownership workflow explicitly allows it.

### Alternate flow C — Revoked participant

1. A Player is removed from a Campaign while a screen is open.
2. The next command is denied after authoritative recheck.
3. Realtime subscriptions close or reduce to a permitted neutral state.
4. Cached Campaign content becomes unavailable after bounded revocation propagation.
5. Local unsent personal draft content remains available only when policy permits and cannot be committed to the Campaign.

### Alternate flow D — Restricted content

1. A subject can see that a permitted workflow requires an object but lacks entitlement.
2. The service returns only the approved restricted preview and a user-safe reason.
3. Hidden mechanics, source text, relationships, and exact protected metadata remain absent.
4. A Campaign grant or other valid access source changes the entitlement decision without changing Campaign authorization.

### Alternate flow E — Owner support access

1. A tester requests help and explicitly supplies an issue record.
2. The Owner approves a purpose-bound, time-bounded support-access request.
3. The system grants only the required Campaign fields and records start, purpose, scope, and expiry.
4. Every support read is attributable.
5. Access expires automatically and a closure event is retained.

## 8. Failure, empty, and recovery states

| State | User sees | Allowed action | Preserved data | Evidence |
|---|---|---|---|---|
| Loading | Neutral loading state without protected labels or counts | Cancel or navigate away | Existing authorized local view | Operation ID and duration |
| Empty | “No available results” after authorization and entitlement filtering | Change safe filters or return | Filter state | Query shape and permitted result count |
| Validation error | Field-specific safe explanation | Correct request | Local draft | Stable reason code |
| Forbidden | Generic unavailable or insufficient-permission message appropriate to inference risk | Return, request access where allowed, or switch authorized context | Own unsent draft only | Internal denial reason and user-safe reason |
| Restricted entitlement | Approved restricted preview or generic unavailable response | Use Campaign grant workflow or return | Current authorized state | Entitlement decision ID |
| Offline | Bounded read-only projection with expiry and offline indicator | Read cached permitted data; create local personal draft where allowed | Signed snapshot and local draft | Snapshot ID and expiry |
| Stale | “Access or state changed; refresh required” | Refresh or return | Unsaved personal draft | Policy version and state version |
| Conflict | Safe conflict summary without exposing the other actor’s protected data | Reload, compare own draft, or abandon | Own draft and base version | Conflict ID |
| Failed save | No claim that state changed | Retry after reauthorization or retain draft | Local draft | Operation and error code |
| Recovery required | Safe recovery screen identifying lost authorization, invalid cache, or interrupted operation | Reauthenticate, select another workspace, or export own local draft where allowed | Only user-owned permitted local data | Recovery receipt |
| Revoked | Access-ended message without protected details | Return to dashboard | Personal local material governed by policy | Revocation event and cache invalidation |
| Policy unavailable | Fail closed; no protected data | Retry or return | Previously rendered data is covered or cleared according to risk | Dependency health and denial event |

A denial must not confirm that a hidden object, user, clue, relationship, Campaign, or source exists when the subject is not allowed to know that fact.

## 9. Permissions and hidden information

### 9.1 Visibility classes

The alpha uses these semantic classes:

1. `public-canonical` — approved public project content within entitlement boundaries;
2. `campaign-shared` — visible to active permitted Campaign participants;
3. `participant-restricted` — visible only to named participants or roles;
4. `character-controller` — visible to current authorized controller set and GM where policy permits;
5. `player-private` — visible only to the owning Player unless explicitly shared;
6. `gm-only` — visible only to active GM roles and bounded Assistant GM delegations;
7. `creator-draft` — visible to author, assigned reviewers, and owner authority;
8. `operational-metadata` — visible to authorized administrators without revealing protected play content;
9. `security-sensitive` — restricted to narrowly authorized security or service roles;
10. `secret-material` — credentials, tokens, keys, and equivalent data; never sent to ordinary clients or AI.

Classification may apply to an object, field, relationship, event, source coordinate, media derivative, count, or derived claim.

### 9.2 Authorization request

Each decision includes:

- stable subject ID and actor type;
- identity assurance and session state;
- service identity where applicable;
- requested capability;
- resource type and stable ID;
- Campaign, Character, Session, pack, or owner scope;
- membership, role, delegation, control, ownership, and custody inputs;
- field or relationship classification;
- entitlement result and reason;
- installed pack and object lifecycle state;
- expected version for mutations;
- policy version;
- client or operation correlation ID;
- current time for expiry checks.

### 9.3 Authorization decision

The internal result includes:

- allow or deny;
- stable internal reason codes;
- user-safe reason code;
- permitted projection profile;
- permitted fields, relationships, and actions;
- cacheability and expiry;
- reauthentication requirement;
- audit or security-event requirement;
- policy version and evaluated-at time.

External responses may intentionally use `not-found-or-unavailable` instead of a precise denial when precision would reveal protected existence.

### 9.4 Read and query safety

- authorization filters candidates before pagination, counts, facets, ranking, grouping, autocomplete, and export;
- an unauthorized row is never fetched into an ordinary client response and then hidden by the UI;
- exact stable-ID lookup, aliases, legacy names, slugs, and direct URLs follow the same rule;
- relationship edges are returned only when the edge and required endpoint projections are permitted;
- comparison candidates cannot reveal hidden versions, variants, conflicts, or supersession records;
- provenance and original-source views are separately authorized from object summary access;
- query suggestions and recent searches are subject-scoped;
- pagination cursors bind subject, scope, policy version, filters, and expiry;
- result counts and facet values are computed from the authorized set;
- timing and error behavior should avoid simple existence inference where practical;
- caches include subject, Campaign, role context, entitlement context, policy version, and projection profile.

### 9.5 Mutation safety

- every mutation reauthenticates or verifies the current trusted subject;
- every mutation rechecks current authorization at execution time;
- stale membership, role, delegation, control, ownership, entitlement, or object version rejects safely;
- action-level permission and field-level permission both apply;
- a subject cannot set their own role, visibility, ownership, or approval state unless an explicit workflow allows it;
- administrative writes require the same or stronger controls as administrative reads;
- accepted mutations append attributable events and invalidate affected projections.

### 9.6 Realtime safety

- connection authentication is insufficient; every subscription is authorized;
- publication uses a server-generated projection for the recipient context;
- topic names, participant lists, presence, unread counts, and notification badges cannot reveal hidden membership or activity;
- revocation closes or narrows subscriptions within the defined propagation target;
- reconnect reauthorizes and fetches a permitted projection plus permitted events;
- duplicate delivery is safe and contains no hidden fields.

### 9.7 Export, backup, diagnostics, and AI

- exports are generated from authorized projections, not raw database dumps exposed to users;
- Campaign exports require Campaign authority and exclude Player-private material unless policy and owner of that material permit inclusion;
- provider-exit and disaster-recovery backups remain operationally restricted and encrypted;
- diagnostics contain identifiers and reason codes but not hidden game text, tokens, or private notes by default;
- AI receives the initiating subject’s authorized projection plus narrower AI tool policy;
- AI cannot infer broader access from a pasted stable ID, quoted hidden name, or prompt instruction;
- AI output is checked before display and cannot silently mutate visibility or permissions.

### Required denied-case tests

- wrong Campaign;
- revoked participant;
- expired delegation;
- Player exact-ID lookup of unrevealed clue;
- Player alias lookup of hidden NPC;
- Player facet count inference;
- Player relationship traversal to hidden endpoint;
- Player comparison against hidden version;
- Content Creator access to unrelated Campaign;
- Assistant GM access outside delegation;
- Owner/Admin without Campaign or support-access role;
- service actor using another service’s capability;
- AI query requesting hidden motive;
- export containing another Player’s private note;
- stale open screen after revocation;
- replayed pagination token under a different subject;
- cached result after policy-version change;
- unauthorized realtime subscription;
- unauthorized object-storage URL reuse;
- mutation submitted after control transfer.

## 10. Entitlements

Authorization and entitlement remain separate decisions.

- **Access sources:** free policy, owned access, Campaign grant, sponsored month, explicit alpha grant, or another approved immutable grant.
- **Free-tier behavior:** the first two Ability-tree tiers follow the approved P9-01 policy.
- **Campaign grants:** permit content use only in the granted Campaign and do not create global ownership.
- **Sponsored access:** expires predictably without deleting historical state.
- **Expiry behavior:** new restricted use is denied; existing historical records remain renderable only through an approved historical projection.
- **Search and preview restrictions:** results, counts, facets, source text, relationships, and comparison obey both entitlement and authorization.
- **Offline snapshot behavior:** entitlement and permission snapshots are versioned, bounded, signed or otherwise verifiable, and expire.
- **Reason preservation:** the user-safe response may say unavailable or restricted, while the internal decision retains distinct entitlement and authorization reason codes.

## 11. Persistence and history

- **Draft storage:** Player-private local drafts remain subject-owned and are not Campaign state until submitted through an authorized action.
- **Authoritative save:** membership, role, delegation, visibility, control, support access, and reveal changes commit transactionally.
- **Aggregate boundary:** Campaign authority records, Character control, and Session participation use explicit aggregate and version boundaries.
- **Expected-version behavior:** stale permission mutations fail without partial change.
- **Idempotency:** repeated grant, revoke, reveal, transfer, or support-access commands return the prior result or reject incompatible reuse.
- **Event types:** membership, role, delegation, control, visibility, reveal, support access, permission snapshot, export authorization, and security denial events.
- **Snapshot behavior:** projections and checkpoints record policy version, subject context, source event sequence, and digest.
- **Audit events:** store who, what capability, which scope, when, result, reason, policy version, and correlation—not protected content unless a separately governed forensic record requires it.
- **Migration behavior:** expand–migrate–contract; preserve stable subject IDs, role semantics, visibility classes, reason codes, and historical attribution.
- **Export behavior:** portable policy, membership, delegation, classification, and audit metadata remain provider-neutral.

## 12. Realtime, interruption, and reconnect

- **Before local submission:** an unsent personal draft remains local; no Campaign mutation exists.
- **After submission but before acceptance:** the client tracks command ID; reconnect asks for authoritative command status under current authorization.
- **After acceptance but before display:** the committed event remains authoritative; reconnect returns only currently permitted projection and events.
- **During pending approval:** proposal author and authorized GM queue recipients receive distinct projections; revocation removes queue access.
- **After missed events:** the client supplies last acknowledged sequence; server reauthorizes and returns permitted gap events or a permitted checkpoint.
- **With a stale client:** server rejects unauthorized or stale mutations; the client moves to stale or forbidden state.
- **From a second device:** both devices use the same subject but independently authorized sessions and subscriptions; revocation affects both.
- **After service restart:** authoritative membership, policy version, event history, and outbox restore subscription state; no client cache becomes authority.
- **After role change:** new reads use the new projection; prior rendered protected data is covered or cleared according to risk and platform capability.

Target for internal alpha: a membership or role revocation blocks new authoritative mutations immediately and removes affected realtime access within 10 seconds under normal connected conditions. The final implementation work order may tighten this target after measurement.

## 13. Interface and information hierarchy

### Desktop

- persistent active identity, Campaign, role, and Character context;
- permission-safe navigation generated from authorized capabilities;
- object and Scene inspectors use server projections;
- role switch is explicit and never implied by opening another workspace;
- access-state panel shows user-safe reason and permitted recovery action;
- GM preview opens a clearly labeled server-generated Player projection;
- administrative evidence is separated from protected game content.

### Tablet

- context header remains visible;
- inspectors use drawers or split panels without preloading forbidden fields;
- role and Campaign switch require explicit confirmation when unsaved work exists;
- permission changes announce and move focus safely.

### Mobile

- single-focus screen with explicit context chip;
- forbidden or revoked states replace protected content rather than leaving it behind under an overlay;
- details, source views, and relationships load only when opened and authorized;
- action sheets show only permitted actions but services still enforce every action;
- reauthentication and return-to-dashboard paths are reachable with touch and keyboard.

### Player hierarchy

Foreground:

1. current Campaign and Character context;
2. permitted Scene, Action, object, and result information;
3. own private notes and permitted history;
4. clear but nonrevealing unavailable state;
5. recovery action.

Secondary:

- technical reason ID for issue reporting;
- access request where policy permits;
- detailed permission explanation that does not reveal hidden facts.

### GM hierarchy

Foreground:

1. current Campaign and GM authority;
2. object or Scene visibility state;
3. who can currently see each governed field or reveal group;
4. Player-preview action;
5. reveal, delegate, revoke, or correct controls permitted by policy;
6. consequences and affected participants before a change commits.

## 14. Accessibility

- semantic headings identify current identity, Campaign, role, and access state;
- keyboard users can reach context controls, permitted content, reason explanation, and recovery action without traversing hidden placeholders;
- focus moves to the access-state heading after revocation or permission loss;
- screen-reader labels distinguish unavailable, restricted, revoked, stale, and offline without exposing hidden object names;
- live announcements prioritize role change, revocation, reveal, and restored access;
- badges use text and icons, not color alone;
- high zoom and text scaling preserve context and recovery actions;
- reduced motion removes animated conceal/reveal effects;
- touch targets meet the selected alpha standard;
- graphs and maps provide permission-filtered list or table alternatives;
- errors identify the action that failed and the safe next step;
- server-generated Player preview has a persistent “Preview” label and cannot be mistaken for the GM’s own view;
- hidden content is not left in the accessibility tree, DOM, page source, or client state merely with visual concealment.

## 15. Notifications and queues

| Trigger | Recipient | Message content | Action | Resolution state |
|---|---|---|---|---|
| Campaign invitation | invited subject | Campaign-safe invitation summary | accept or decline | pending/accepted/declined/expired |
| Role changed | affected subject | new user-safe role and effective time | open workspace | unread/read/acknowledged |
| Access revoked | affected subject | access ended; no hidden reason detail | return to dashboard | delivered/acknowledged |
| Delegation request | Assistant GM | bounded scope, grantor, expiry | accept or decline | pending/active/declined/expired/revoked |
| Visibility revealed | newly authorized participants | Player-safe reveal summary | open revealed object | unread/read |
| Access request | authorized GM or owner | requester, requested scope, user-safe reason | approve, deny, or narrow | pending/approved/denied/expired |
| Support access | tester and Owner | purpose, scope, start, expiry | inspect or end | requested/active/ended/expired |
| Permission failure | initiating subject | safe failure and issue ID | retry, switch context, or report | open/resolved |
| Security-relevant denial | authorized security queue | subject, capability, scope, reason code, correlation | review | new/triaged/closed |

Notification existence, count, sender, preview, and deep link are themselves permission-filtered.

## 16. AI involvement

**AI mode:** optional read-only for alpha; future proposed or approval-gated mutations remain separate.

- **Allowed action:** explain a permitted access state, search permitted content, summarize permitted information, or suggest a safe next action.
- **Allowed sources:** only the initiating subject’s authorized projection and approved public governance help.
- **Permission and entitlement checks:** run before retrieval and again before output-linked actions.
- **Provenance:** cite stable source or object identity only when that identity is permitted.
- **Uncertainty:** distinguish policy explanation from inferred user intent.
- **Cost boundary:** zero AI is required for core authorization; policy evaluation must be deterministic and local/provider-neutral.
- **Non-AI fallback:** every permission explanation and recovery path works without AI.
- **Prohibited behavior:** role elevation, hidden-data retrieval, prompt-directed bypass, silent mutation, support impersonation, canon promotion, or exposure of internal security details.

## 17. Telemetry and diagnostics

- operation and correlation IDs for authorization-sensitive workflows;
- policy version, capability, resource type, scope type, result, internal reason code, and latency;
- no raw private note, hidden clue text, token, credential, or protected object body in ordinary logs;
- metrics for allow, deny, not-found-or-unavailable, stale, reauthentication, revocation propagation, cache invalidation, realtime closure, and export denial;
- alerts for repeated cross-Campaign attempts, service-capability misuse, invalid pagination tokens, expired delegation use, and hidden-field serialization failures;
- issue attachments include release, route, safe object type, operation ID, and user-safe reason;
- audit access is itself authorized and audited;
- cost is limited to local policy evaluation and existing provider-neutral storage or telemetry contracts.

## 18. Test scenarios

### Unit

- decision precedence and default deny;
- visibility-class inheritance and explicit override constraints;
- role, delegation, controller, ownership, and expiry evaluation;
- user-safe reason mapping;
- projection field removal;
- policy-version cache key and invalidation;
- pagination-token binding;
- support-access expiry.

### Contract

- authorization request and decision schemas;
- projection schema rejects unclassified protected fields;
- every adapter passes identical decision fixtures;
- service errors remain provider-neutral;
- database isolation and service decisions agree for representative cases;
- object-storage access is scoped and expires.

### Integration

- identity plus Campaign membership plus role resolution;
- Universal Object search, counts, facets, inspector, provenance, relationships, comparison, and picker;
- entitlement and authorization composition;
- Character controller and Scene visibility changes;
- activity, notification, export, realtime, and AI projection filtering;
- audit and telemetry redaction.

### End-to-end

- distinct Player and GM open the same Campaign and receive different correct projections;
- GM preview matches the Player’s actual server projection;
- GM reveals one clue and only that clue appears for the Player;
- Player proposal and GM approval expose only required information;
- removed Player loses workspace, search, realtime, and mutation access;
- support access starts, operates in scope, and expires.

### Permission and hidden information

- all denied cases in Section 9;
- unauthorized counts, aliases, exact IDs, relationships, comparison, and timing do not disclose protected existence;
- private Player note remains unavailable to GM unless a separate approved policy explicitly grants it;
- Owner/Admin without Campaign or support role cannot read private play content;
- Assistant GM delegation cannot broaden itself;
- hidden fields never appear in network payload, client store, DOM, accessibility tree, export, logs, or AI context.

### Entitlement

- authorized but unentitled;
- entitled but unauthorized;
- Campaign grant;
- sponsored access expiry;
- historical projection after expiry;
- restricted search and preview.

### Persistence and migration

- role and visibility changes are transactional and attributable;
- idempotent grant and revoke commands;
- policy migration preserves stable IDs and historical reason codes;
- backup and provider-exit export preserve policy records without exposing them to ordinary users.

### Reconnect and recovery

- disconnect before and after revocation;
- missed reveal event;
- stale cached object after policy change;
- second device closes access;
- policy service unavailable fails closed;
- signed offline snapshot expires;
- unsent personal draft recovery after Campaign removal.

### Accessibility

- keyboard-only role/context and recovery flows;
- screen-reader announcements for reveal, revocation, and restored access;
- 200% and 400% zoom;
- mobile touch flow;
- noncolor badges;
- permission-safe graph/list alternatives;
- hidden content absent from accessibility tree.

### Performance

- permission-filtered search over the bounded real corpus;
- high-density relationship and inventory queries;
- two-device Session publication;
- revocation propagation within target;
- cache invalidation fan-out;
- denial paths do not become materially slower than allow paths in a way that trivially reveals existence.

### Golden or deterministic regression

- 8D-007J does not govern policy semantics directly;
- deterministic authorization fixtures and exact projection baselines are blocking product regressions;
- 8D-007J applies when a permission change alters executable rules availability or approved gameplay-result baselines.

## 19. Acceptance criteria

1. **PHI-AC-001 — Default deny**  
   Unknown subject, role, capability, resource, field classification, or policy state denies safely.  
   **Evidence:** deterministic decision fixtures.  
   **Blocking:** yes.

2. **PHI-AC-002 — Campaign isolation**  
   A subject in IA-CAMPAIGN-01 cannot read, count, search, subscribe to, export, or mutate IA-CAMPAIGN-02.  
   **Evidence:** service, database, search, realtime, export, and AI tests.  
   **Blocking:** yes.

3. **PHI-AC-003 — Field-safe projections**  
   Player, GM, Assistant GM, creator, observer, Owner/Admin, and service actors receive exactly their permitted fields.  
   **Evidence:** exact projection baselines.  
   **Blocking:** yes.

4. **PHI-AC-004 — Hidden existence safety**  
   Results, counts, facets, aliases, exact IDs, rankings, pagination, relationships, and comparison do not reveal unauthorized objects.  
   **Evidence:** inference test matrix.  
   **Blocking:** yes.

5. **PHI-AC-005 — Universal Object integration**  
   Browser, inspector, source view, provenance, relationship traversal, comparison, and picker all use the shared authorization contract.  
   **Evidence:** integration suite.  
   **Blocking:** yes.

6. **PHI-AC-006 — Mutation reauthorization**  
   Every authoritative mutation rechecks current role, delegation, control, ownership, entitlement, object version, and policy version as applicable.  
   **Evidence:** stale and revoked mutation tests.  
   **Blocking:** yes.

7. **PHI-AC-007 — Realtime projection safety**  
   Connections, subscriptions, notifications, presence, counts, events, and reconnect projections remain permission-safe.  
   **Evidence:** two-device tests.  
   **Blocking:** yes.

8. **PHI-AC-008 — Revocation**  
   Revocation blocks new mutations immediately and removes affected connected access within the approved alpha propagation target.  
   **Evidence:** measured revocation tests.  
   **Blocking:** yes.

9. **PHI-AC-009 — GM Player preview**  
   The preview is generated by the same server projection used for the selected Player and contains no GM-only fields.  
   **Evidence:** exact comparison against real Player response.  
   **Blocking:** yes.

10. **PHI-AC-010 — Private-note boundary**  
    Player-private notes are unavailable to other Players, GMs, Owner/Admin, exports, diagnostics, and AI unless a separately approved policy explicitly permits the exact operation.  
    **Evidence:** denied-case and export tests.  
    **Blocking:** yes.

11. **PHI-AC-011 — Entitlement separation**  
    Entitlement and authorization decisions remain distinct and compose without one bypassing the other.  
    **Evidence:** four-way access matrix.  
    **Blocking:** yes.

12. **PHI-AC-012 — Owner/Admin boundary**  
    Administrative status alone cannot read Campaign-private or Player-private content.  
    **Evidence:** owner-without-role denied tests and support-access tests.  
    **Blocking:** yes.

13. **PHI-AC-013 — Service and AI least privilege**  
    Service and AI actors cannot use another service’s capability or retrieve fields outside their bounded projection.  
    **Evidence:** service-capability and prompt-injection tests.  
    **Blocking:** yes.

14. **PHI-AC-014 — Offline boundary**  
    Bounded offline state is read-only, verifiable, subject-scoped, policy-versioned, and expired or invalidated predictably.  
    **Evidence:** snapshot tests.  
    **Blocking:** yes.

15. **PHI-AC-015 — Audit without disclosure**  
    Material decisions are attributable while ordinary logs and issue attachments contain no hidden content or secrets.  
    **Evidence:** log and audit inspection.  
    **Blocking:** yes.

16. **PHI-AC-016 — Accessibility**  
    Permission, revoked, stale, reveal, and recovery flows pass keyboard, screen-reader, touch, zoom, contrast, and noncolor-status review.  
    **Evidence:** automated and manual accessibility report.  
    **Blocking:** yes.

17. **PHI-AC-017 — Provider neutrality**  
    Domain services and tests do not depend on a named identity, database, search, realtime, or AI provider policy type.  
    **Evidence:** dependency and adapter-contract review.  
    **Blocking:** yes.

18. **PHI-AC-018 — Fail closed**  
    Policy, identity, membership, entitlement, or classification dependency failure does not publish or mutate protected state.  
    **Evidence:** failure-injection tests.  
    **Blocking:** yes.

19. **PHI-AC-019 — Performance**  
    Authorized search, Session projection, and revocation meet approved alpha budgets on the bounded corpus and device matrix.  
    **Evidence:** performance report.  
    **Blocking:** yes.

20. **PHI-AC-020 — Complete journey**  
    Player onboarding, GM preparation, object selection, Scene launch, Action proposal, GM decision, result, reconnect, reveal, and revocation preserve correct distinct projections.  
    **Evidence:** end-to-end journey receipt.  
    **Blocking:** yes.

## 20. Fixtures and approved alpha content

- **Required identities:** Owner/Admin without Campaign role, GM, Assistant GM with bounded delegation, two Players, creator, observer, revoked former participant, service actor, AI service actor.
- **Required Campaigns:** IA-CAMPAIGN-01 and IA-CAMPAIGN-02 isolation Campaign.
- **Required Characters:** controlled Character, shared-control Character where policy permits, unassigned Character, archived Character.
- **Required packs:** version-pinned alpha corpus, one uninstalled pack, one restricted pack, one Campaign-granted pack.
- **Required objects:** public object, Campaign-shared object, GM-only object, Player-private note, restricted object, unrevealed clue, hidden NPC motive, private creator draft, security-sensitive record.
- **Required relationships:** visible edge, hidden edge, visible endpoint with hidden edge, hidden endpoint, cross-Campaign edge attempt.
- **Required historical state:** membership change, role change, reveal, control transfer, delegation expiry, support-access session, entitlement expiry.
- **Required failure fixtures:** invalid stable ID, stale policy version, expired pagination token, revoked subject, policy-service failure, corrupted permission snapshot, unauthorized export, object-storage URL reuse, AI hidden-data request.
- **Companion matrix:** `MV-IA-F020_PERMISSION_SURFACE_MATRIX.json` defines surfaces, classifications, decisions, reason codes, and required denied cases.

## 21. Security, privacy, cost, and risk

### Security

- deny by default;
- service and database isolation agree;
- privileged credentials never reach clients;
- parameterized queries and schema validation;
- signed, scoped, expiring object-storage access;
- rate and command-size limits;
- policy-versioned caches;
- revocation invalidation;
- append-only security events;
- dependency and secret scanning;
- prompt-injection resistance for AI retrieval;
- no hidden data in client source, DOM, logs, telemetry, or ordinary error payloads.

### Privacy

- Player-private notes remain subject-controlled;
- Campaign content is not support-accessible by default;
- data minimization applies to every projection;
- issue reports are privacy-safe;
- exports and deletion workflows respect ownership and historical requirements;
- lower environments use synthetic fixtures;
- backup and provider-exit access are operationally restricted.

### Cost

- core policy evaluation requires zero AI and zero paid authorization service;
- alpha implementation should use repository-owned rules and existing provider-neutral persistence/search contracts;
- no paid search, identity, policy, or monitoring provider is authorized by this packet;
- performance and telemetry must remain inside the approved alpha cost envelope.

### Material risks

- hidden existence leaked through counts or timing;
- stale cache after revocation;
- mismatch between service authorization and database isolation;
- overbroad GM, Assistant GM, Owner/Admin, or service role;
- accidental Player-private note inclusion in exports or support access;
- relationship or provenance traversal bypass;
- AI retrieval bypass;
- policy migration changing meaning;
- offline snapshot remaining valid too long;
- authorization latency degrading search or Session play.

### Stop conditions

- unresolved path that publishes hidden fields to a client;
- service/database policy disagreement;
- Owner/Admin blanket-content access introduced without owner decision and privacy review;
- Player-private material included in Campaign export by default;
- AI or service actor granted broader authority than initiating subject or registered service role;
- policy dependency fails open;
- revocation cannot block new authoritative mutation;
- implementation requires paid provider, production credential, or irreversible vendor coupling;
- ambiguous owner decision about support access, private notes, or public sharing.

## 22. Owner review points

- **Design approval required:** owner review of role semantics, private-note boundary, support-access boundary, and the internal-alpha visibility classes before implementation begins.
- **Scope decision required:** any proposal to add public sharing, anonymous access, broad offline mutation, custom policy language, or organization administration.
- **Canon decision required:** none for the permission mechanism; visibility changes to canonical source content remain separate canon decisions.
- **Spending or provider decision required:** any paid identity, policy, search, monitoring, or AI provider.
- **Alpha release decision required:** exact candidate, two-device evidence, denied-case report, private-note test, GM preview test, revocation measurement, backup/restore, provider exit, and owner approval.
- **Support-access decision required:** exact purpose, scope, duration, subject, Campaign, audit, and revocation behavior.

Silence is not approval.

## 23. Implementation handoff

**Target repository:** `cybalicistjt-stack/Multiversal-app`  
**Registered work type:** material cross-cutting security and product implementation  
**Decision level:** A2 for bounded implementation; A3 for owner-reserved visibility, support-access, spending, provider, or release decisions  
**Risk class:** high — security, privacy, hidden information, data isolation, and alpha-entry critical  
**Suggested work-order title:** Implement MV-IA-F020 provider-neutral authorization, projection, and hidden-information foundation  
**Expected branches or files:** contracts and schemas; authorization domain package; local adapter; persistence and database-isolation adapter; projection utilities; search filtering; realtime authorization; export and AI guards; client access states; fixtures; tests; CI  
**Required reviewers:** architecture, security, privacy, data, QA, UX/accessibility, application integration, and documentation  
**Required gates:** AG-02, AG-04, AG-05 where Session behavior is affected, internal-alpha design validation, adapter contracts, denied-case suite, two-device suite, accessibility, backup/export review, and owner release gate  
**Rollback or recovery:** feature-flag new policy adapter in nonproduction environments; retain prior compatible schema during expand–migrate–contract; fail closed; restore policy data from verified backup; invalidate all affected caches and sessions after rollback or correction  
**Evidence outputs:** schemas, policy and reason-code catalog, exact projection baselines, denied-case matrix, service/database agreement report, revocation measurements, accessibility report, security review, migration receipt, CI, implementation receipt, and handoff

### Suggested implementation decomposition

1. authorization request, decision, classification, role, capability, and reason-code schemas;
2. deterministic local policy engine and fixtures;
3. subject, membership, role, delegation, controller, and ownership persistence;
4. service authorization middleware and provider-neutral port;
5. database-isolation adapter and agreement tests;
6. projection builder and serialization guard;
7. Universal Object query, count, facet, relationship, source, comparison, and picker integration;
8. realtime connection, subscription, publication, and reconnect integration;
9. export, object storage, diagnostics, and AI retrieval guards;
10. client context, forbidden, restricted, stale, revoked, and recovery states;
11. revocation, cache, offline snapshot, and two-device tests;
12. owner review and alpha-entry evidence.

### Dependency hold

The design is complete, but implementation remains dependency-gated by the active P9-06 sequence, concrete identity and persistence foundations, database-isolation capability, backup/restore/provider-exit readiness, and coordinated caller integration. No part of this packet authorizes implementation around those gates.

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

**Final design status:** implementation-ready  
**Reviewer:** independent implementation review remains required at work-order execution  
**Date:** 2026-08-05  
**Packet digest:** generated and recorded by repository commit and pull-request evidence
