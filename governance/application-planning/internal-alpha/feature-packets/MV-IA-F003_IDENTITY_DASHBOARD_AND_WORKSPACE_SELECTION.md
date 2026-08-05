# MV-IA-F003 — Identity, Dashboard, and Workspace Selection

**Feature ID:** MV-IA-F003  
**Feature version:** 0.1.0  
**Classification:** entry-critical  
**Design status:** implementation-ready  
**Owner:** John Brandon Turner  
**Primary roles:** Player, Game Master, Assistant GM, Content Creator, Observer, Owner/Admin, invited tester, service actor  
**Stage A mapping:** A3 — Identity, Dashboard, and Workspace Selection  
**Historical module mapping:** Content Library and Entitlements  
**Prepared by:** Lead Documentation Architect / Product Requirements and Identity Steward  
**Reviewed by:** architecture, security, privacy, QA, UX/accessibility, data, entitlement, and documentation roles required before implementation  
**Date:** 2026-08-05

## 1. Problem and user outcome

### Problem

Multiversal users may participate in several Campaigns, hold different roles in each Campaign, control different Characters, receive invitations, return to recent work, and enter live Sessions. The application must identify the user without binding the product to one identity provider, then show only workspaces the current subject may know about and enter.

A generic account home page is insufficient. Dashboard cards, recent work, invitation previews, notification counts, role selectors, Campaign names, Character names, Session status, and deep links can all disclose protected information. A client-side filter is also insufficient because an unauthorized subject could query the underlying service directly or reuse stale cached workspace data after revocation.

The system must also distinguish several concepts that are often incorrectly combined:

- external provider identity;
- stable Multiversal subject identity;
- authenticated session;
- Campaign membership;
- Campaign role;
- Character control;
- entitlement;
- invitation;
- selected workspace context;
- recent-work history.

### Required outcome

An approved alpha tester can establish or resume a provider-neutral identity session, accept or decline a valid invitation, see a role-aware dashboard containing only authorized workspaces, select a permitted Campaign or Session context, and enter the correct Player, GM, creator, observer, or Owner/Admin workspace without learning that hidden workspaces exist.

The selected workspace context is explicit, attributable, recoverable, and revalidated on entry and mutation. Switching roles or Campaigns changes the active authorization context rather than merely changing the visible navigation.

### Why this belongs in internal alpha

This feature is entry-critical because every primary Player and GM journey begins with identity and workspace entry. The two-device alpha cannot prove Campaign isolation, hidden-information safety, entitlements, invitations, Character control, or role-specific navigation until distinct subjects enter distinct authorized contexts.

## 2. Alpha slice

### Included

- local and test identity adapters that resolve stable internal subject IDs;
- provider-neutral session establishment, resume, expiry, revocation, and sign-out contracts;
- approved invitation lookup, acceptance, decline, expiry, revocation, and already-used handling;
- role-aware dashboard summaries for Player, GM, Assistant GM, creator, observer, and Owner/Admin contexts used by the alpha;
- authorized Campaign, Character, Scene, Session, content-draft, and operational workspace references;
- recent-work references that are permission-safe and revocation-aware;
- notification summaries and invitation notices that do not leak hidden details;
- explicit role and workspace selection;
- deep-link validation and safe fallback;
- selected-context receipt containing stable IDs, role, permissions version, entitlement version, and expiry metadata;
- reauthorization when opening a workspace and before every protected mutation;
- role and Campaign switching without cross-context cache leakage;
- empty, loading, expired, revoked, forbidden, stale, offline, and service-unavailable states;
- bounded account-recovery support for approved alpha testers;
- responsive desktop, tablet, and mobile behavior;
- keyboard, touch, screen-reader, high-zoom, reduced-motion, and noncolor status behavior;
- deterministic fixtures and two-subject acceptance scenarios.

### Explicitly excluded

- public self-registration;
- social-profile discovery;
- public user directory;
- production identity-provider selection;
- production credentials;
- password-storage implementation owned directly by the client;
- broad organization tenancy;
- enterprise single sign-on;
- public Campaign discovery;
- anonymous Campaign access;
- public friend or follower systems;
- production customer-support impersonation;
- billing-provider account linking;
- unbounded multi-account merging;
- automatic canonical contributor authority from account identity;
- internal-alpha release authorization.

### Full long-term scope deferred

Later work may add production identity providers, multiple linked providers, verified recovery channels, organization administration, guest links, public profiles, richer notification preferences, cross-device session management, regional policy controls, and self-service account deletion. Those additions must preserve stable internal subject identity, provider-neutral mappings, deny-by-default workspace discovery, reason codes, audit history, and explicit owner gates.

## 3. Roles and authority

| Role | Allowed actions in the alpha slice | Restricted behavior | Approval required |
|---|---|---|---|
| Invited tester | Establish approved alpha identity, inspect a safe invitation summary, accept or decline | Cannot enumerate Campaigns, users, roles, Characters, or Sessions | Invitation must be valid, unexpired, unrevoked, and bound to the intended subject or approved acceptance flow |
| Player | View Player dashboard, authorized Campaigns, controlled Characters, permitted Sessions, own notifications, and recent work | Cannot see GM-only Campaigns, other Players’ private work, hidden Session state, or unauthorized Characters | GM or owner-controlled membership and Character-control grants |
| Game Master | View and enter Campaigns where the subject is an active GM; see GM preparation and live-session entries | Cannot enter unrelated Campaigns or infer their existence | Campaign membership and active GM role |
| Assistant GM | Enter only delegated Campaign workspaces and delegated feature areas | No automatic full-GM access | Explicit delegation record |
| Content Creator | Enter own or assigned draft workspaces and permitted canonical library views | Cannot gain Campaign access or canonical authority from creator status | Assignment or proposal workflow; owner approval for canonical promotion |
| Observer | Enter only explicitly granted read-only Campaign or Session projection | Cannot control Characters, approve Actions, or inspect hidden GM state | Active observer grant |
| Owner/Admin | View program operations, alpha administration, release identity, and operational metadata | Owner status does not automatically expose Player-private or Campaign-private content | Governed Campaign role or time-bounded support-access record for protected play content |
| Service actor | Resolve identity, invitations, authorized workspace summaries, notifications, and session state within narrow service scope | Cannot expand subject authority or read unrelated protected content | Service credential and operation-specific authorization |

Identity, membership, role, entitlement, and ownership grants remain separate. Possessing one does not imply the others.

Silence is not approval.

## 4. Dependencies

### Feature dependencies

- **MV-IA-F001 — Application Shell and Workspace Navigation** supplies the responsive shell, global selectors, loading states, navigation regions, notifications entry, and user menu.
- **MV-IA-F019 — Content Library and Entitlements** supplies access decisions for content-backed dashboard entries and Campaign grants.
- **MV-IA-F020 — Permissions and Hidden Information** supplies deny-by-default workspace discovery, safe projections, reason codes, revocation, cache invalidation, and support-access boundaries.
- **MV-IA-F021 — Autosave, Reconnect, Recovery, and Bounded Offline Use** will consume the selected-context receipt and define later reconnect behavior; F003 defines the identity and workspace inputs that it requires.
- **MV-IA-F025 — Onboarding, Help, Diagnostics, and Issue Reporting** will consume first-entry, empty-dashboard, blocked-entry, and release-identity states.

### Architecture dependencies

- `IdentityPort` and stable subject identity;
- `EntitlementPort` for content access decisions;
- `PersistencePort` for invitation, membership, recent-work, and audit records;
- server authorization consistent with database isolation;
- provider-neutral error and reason-code contracts;
- backup, restore, and provider-exit treatment for identity mappings and membership state;
- telemetry that excludes protected Campaign content.

### Sequencing note

F003 and F020 form a coordinated identity/authorization boundary. A minimal identity bootstrap may be implemented before the complete dashboard, but no workspace list, recent-work entry, deep link, or selected context is trusted until F020 authorization contracts are available.

### Dependency hold

Application implementation remains dependency-gated by the active P9-06 sequence. This packet does not authorize implementation around unfinished identity, persistence, backup, restore, provider-exit, or authoritative-session dependencies.

## 5. Object and state model

### Stable subject

A Multiversal subject has a stable internal ID independent of:

- email;
- username;
- display name;
- provider user ID;
- device;
- current session;
- Campaign role.

### External identity mapping

An external identity mapping contains:

- internal subject ID;
- provider adapter ID;
- provider subject ID;
- environment;
- verification state;
- linked-at and revoked-at metadata;
- provider-neutral status.

The provider subject ID never replaces the internal subject ID in domain records.

### Authentication session

An authentication session contains:

- session ID;
- internal subject ID;
- issued-at and expiry;
- authentication assurance level where relevant;
- device or client label without invasive fingerprinting;
- revocation state;
- last validated permissions version;
- last validated entitlement version.

### Invitation

An invitation contains:

- invitation ID;
- opaque acceptance token or token digest;
- Campaign ID or bounded destination ID;
- intended role;
- intended recipient binding where available;
- inviter subject ID;
- created, expiry, accepted, declined, and revoked timestamps;
- single-use or bounded-use rule;
- safe preview fields;
- audit references.

The raw token is secret and must not be logged.

### Campaign membership

A membership contains:

- Campaign ID;
- subject ID;
- membership status;
- one or more scoped roles;
- effective and expiry times;
- inviter or granting authority;
- revocation state;
- permissions version.

### Role assignment

A role assignment is scoped and versioned. It may be:

- Campaign Player;
- Game Master;
- Assistant GM;
- observer;
- creator or reviewer;
- owner/admin operational role.

Role assignment does not imply Character control, content entitlement, or ownership.

### Character-control grant

A Character-control grant links:

- subject ID;
- Character ID;
- Campaign ID;
- allowed control actions;
- start and expiry;
- grantor;
- revocation.

### Workspace reference

A workspace reference is a safe projection containing only fields authorized for discovery, such as:

- workspace type;
- stable workspace ID;
- safe display label;
- role;
- safe status;
- permitted destination route;
- last-authorized activity time;
- unread or pending summary only when safe;
- current permissions and entitlement evaluation references.

A workspace reference is not proof that entry remains authorized.

### Recent-work reference

A recent-work reference contains:

- subject ID;
- workspace ID and type;
- last permitted route;
- last accessed time;
- safe display projection;
- permissions version at capture;
- invalidated-at metadata.

### Selected-context receipt

A selected-context receipt contains:

- receipt ID;
- subject ID;
- authentication session ID;
- selected Campaign, Character, Scene, Session, or creator workspace IDs where applicable;
- active role;
- permission decision reference;
- entitlement decision reference;
- permissions version;
- entitlement ruleset version;
- issued-at and expiry;
- correlation ID.

The receipt assists navigation and recovery. It is not a client-authoritative permission grant.

### Dashboard projection

The dashboard is a derived, permission-safe projection. It is not an independently editable canonical object.

## 6. Primary user flows

### Flow A — first approved alpha entry

1. Tester opens the alpha client.
2. Client requests available approved identity methods from the local or alpha adapter.
3. Tester authenticates or activates a bounded invitation flow.
4. Service resolves a stable internal subject.
5. Service establishes an expiring authentication session.
6. Service evaluates pending safe invitation summaries and authorized workspace discovery.
7. Client renders the role-aware dashboard.
8. Tester selects an authorized role and workspace.
9. Service reauthorizes the selected destination.
10. Service returns a selected-context receipt and permitted initial projection.
11. Client enters the workspace.

### Flow B — accept invitation

1. Tester opens an opaque invitation link or enters an invitation token.
2. Service validates token integrity without logging the raw token.
3. Before authentication, only the minimum safe invitation summary is shown.
4. Tester authenticates or establishes the intended subject identity.
5. Service verifies recipient binding, expiry, revocation, prior use, Campaign state, role grant, and entitlement implications.
6. Tester confirms acceptance.
7. Service atomically records acceptance and membership or grant creation.
8. Invitation becomes unavailable for unauthorized reuse.
9. Dashboard refreshes with the newly authorized workspace.
10. Audit event records the acceptance without hidden Campaign content.

### Flow C — return to recent work

1. Existing subject resumes or establishes a valid session.
2. Service retrieves recent-work candidates.
3. Every candidate is re-evaluated against current membership, role, permissions, entitlement, lifecycle, and revocation state.
4. Unauthorized candidates are omitted without revealing why they previously existed.
5. User selects a permitted recent-work card.
6. Service reauthorizes entry and issues a new context receipt.
7. Client restores only permitted navigation and state.

### Flow D — switch Campaign or role

1. User opens the workspace switcher.
2. Service returns only authorized alternatives.
3. User selects another role or Campaign.
4. Service reauthorizes the new context.
5. Client clears or partitions all prior-context caches, drafts, subscriptions, notifications, and AI context.
6. New context receipt and projection replace the old context.
7. History records the switch without exposing protected content.

### Flow E — deep link

1. User opens a bookmarked or shared route.
2. Client establishes or resumes identity.
3. Service resolves the target stable ID without revealing its existence to unauthorized subjects.
4. Service authorizes the route and context.
5. Authorized user enters the target.
6. Unauthorized, expired, or unknown target returns the approved user-safe state without enumeration.

### Flow F — sign out or session revocation

1. User signs out or service revokes the session.
2. Authentication tokens and selected-context receipt become invalid.
3. Realtime subscriptions end.
4. Protected client caches and in-memory state are cleared according to the client-security contract.
5. Public shell or approved sign-in state replaces the workspace.
6. Audit or security event records the action.

## 7. Alternate and exception flows

### Expired invitation

Show a neutral expired-or-unavailable message. Do not reveal whether the Campaign still exists, who participates, or whether another invitation was issued.

### Revoked invitation

Use the same user-safe unavailability family as an expired or invalid invitation unless the authenticated recipient is allowed a more specific reason.

### Already accepted invitation

When the authenticated subject already holds the resulting membership, route to the authorized dashboard. Another subject receives the safe unavailable state.

### Invitation recipient mismatch

Do not reveal the intended recipient identity. Provide a safe mismatch or unavailable state and a governed support path.

### No authorized workspaces

Render a useful empty dashboard with:

- pending safe invitations;
- onboarding guidance;
- issue-reporting access;
- sign-out;
- no global Campaign search.

### Membership pending approval

Show a bounded pending state only to the affected subject and authorized approvers. Do not create workspace access before approval.

### Role removed while dashboard is open

Invalidate affected cards and context receipts. Open protected routes transition to a safe revoked state and clear protected data.

### Entitlement changes

Re-evaluate content-backed cards and workspace capabilities. Preserve historical Campaign state without exposing newly restricted content.

### Identity service unavailable

Do not treat cached identity as current authority for protected entry. Show the approved unavailable or bounded offline state.

### Duplicate acceptance request

Invitation acceptance is idempotent. The same accepted request returns the prior authoritative result; a conflicting reuse rejects safely.

### Account recovery

Alpha recovery uses a governed manual or bounded adapter process. Recovery must preserve the internal subject, avoid creating duplicate subjects, and record the identity mapping change.

### Conflicting linked identities

Stop automatic linking. Preserve both records, create a conflict case, and require an authorized recovery decision. Do not merge Campaign history silently.

## 8. Failure, empty, and recovery states

### Required states

- initial loading;
- authentication required;
- authentication in progress;
- authentication failed;
- session expired;
- session revoked;
- identity-provider unavailable;
- invitation loading;
- invitation unavailable;
- invitation expired;
- invitation pending acceptance;
- invitation accepted;
- invitation declined;
- dashboard loading;
- no authorized workspaces;
- no recent work;
- workspace forbidden;
- workspace revoked;
- workspace archived;
- entitlement changed;
- stale context receipt;
- offline read-only boundary;
- reconnect and revalidation;
- generic service unavailable;
- recoverable account conflict;
- unrecoverable identity conflict requiring support.

### Recovery behavior

- authentication retries never duplicate subjects;
- invitation acceptance is idempotent;
- dashboard refresh replaces stale projections rather than merging unauthorized cards;
- recent-work cards are revalidated before display and entry;
- expired context receipts require reauthorization;
- revocation clears protected client state;
- interrupted role switching either remains in the prior authorized context or completes in the new context, never a mixed context;
- recovery does not reintroduce a revoked membership or role;
- user-safe errors do not reveal hidden workspace existence.

### Failure receipt

Operational failures may include an opaque correlation ID and safe retry guidance. Internal diagnostics record stable reason codes without protected Campaign content or secret tokens.

## 9. Permissions and hidden information

F003 consumes the MV-IA-F020 permission contract across every surface.

### Protected discovery surfaces

Authorization applies before returning:

- Campaign cards;
- Character cards;
- Scene or Session cards;
- role labels;
- workspace names;
- invitation previews;
- recent-work entries;
- unread counts;
- pending-approval counts;
- notification previews;
- activity timestamps;
- avatars or media;
- deep-link resolution;
- workspace suggestions;
- autocomplete;
- cross-device session lists;
- diagnostics;
- exports;
- AI dashboard summaries.

### No enumeration

An unauthorized subject must not infer protected workspaces through:

- different status codes;
- response timing where practical;
- total counts;
- pagination gaps;
- image URLs;
- cached titles;
- recent-route history;
- notification badges;
- invitation-token behavior;
- deep-link previews;
- analytics events.

### Reauthorization points

Reauthorize:

- dashboard load;
- invitation preview when subject-specific detail is shown;
- invitation acceptance;
- workspace selection;
- deep-link resolution;
- role switch;
- Campaign switch;
- protected navigation;
- notification open;
- recent-work open;
- every mutation;
- reconnect;
- permissions-version change;
- entitlement-version change.

### Owner/Admin boundary

Owner/Admin operational authority is not blanket permission to inspect Player-private or Campaign-private content. Protected access requires the F020 governed support-access record or a normal Campaign role.

### GM boundary

A GM sees GM information only for Campaigns where the subject holds an active GM or explicitly delegated Assistant GM role.

### Player-private data

Player-private notes and private drafts must not appear in GM, owner, notification, recent-work, diagnostic, or AI summaries without an explicit governed sharing rule.

## 10. Entitlements

Membership answers whether the subject belongs to a Campaign.

Role answers what the subject may do within that Campaign.

Entitlement answers whether the subject may use content or a capability.

These decisions remain separate.

### Dashboard behavior

- a Campaign card may remain visible when historical state exists but some content becomes restricted;
- restricted content details are not exposed through the card;
- the workspace may open in a bounded degraded mode when policy permits;
- Campaign grants apply only in their governed scope;
- free Ability tiers remain governed by F019;
- sponsored-month expiration does not delete historical Character or Campaign state;
- reason codes identify the decision internally without exposing private commercial or grant information to unrelated users.

### Invitation behavior

Invitation acceptance may create membership but must not fabricate entitlement. Required content access is evaluated separately and any limitation is presented accurately before or after acceptance according to policy.

### Zero billing dependency

The alpha identity dashboard must work with zero billing provider and zero paid identity or entitlement services.

## 11. Persistence and history

Persist authoritative records for:

- stable subjects;
- external identity mappings;
- authentication sessions or server-side session references;
- invitation lifecycle;
- Campaign membership;
- role assignment;
- Character-control grants;
- selected-context receipts or their authoritative validation inputs;
- recent-work references;
- notification state;
- revocations;
- account-recovery decisions;
- audit and security events.

### History rules

- accepted invitations are not deleted to make a retry pass;
- role and membership changes append attributable history;
- provider replacement preserves the internal subject ID;
- account recovery preserves Campaign and Character history;
- recent-work invalidation records reason and time without retaining protected display data longer than necessary;
- sign-out and revocation events are retained according to security policy;
- selected-context receipts are bounded and expiring, not permanent authority grants.

### Data minimization

Do not persist unnecessary device fingerprints, raw invitation tokens, protected dashboard snapshots, or private notification content in telemetry.

## 12. Offline, interruption, and reconnect behavior

### Offline boundary

The entry-critical alpha is online-authoritative.

When identity cannot be revalidated:

- protected workspace entry is blocked;
- cached public shell content may render;
- a previously authorized bounded read-only projection may render only under the later F021 offline contract;
- no invitation acceptance, membership change, role switch, entitlement change, or protected mutation is accepted offline.

### Interruption cases

- interruption before authentication leaves no authenticated session;
- interruption after authentication but before dashboard load resumes by revalidating the session;
- interruption during invitation acceptance queries the authoritative invitation result by idempotency key;
- interruption during workspace switch resumes in the last confirmed context or reauthorizes the requested target;
- interruption after revocation must not restore the revoked context from cache.

### Reconnect

Reconnect performs:

1. authentication-session validation;
2. permissions and entitlement version comparison;
3. selected-context validation;
4. subscription replacement;
5. permitted projection refresh;
6. stale protected cache removal;
7. navigation restoration only after authorization succeeds.

## 13. Responsive and platform behavior

### Desktop

- role-aware dashboard may use a left workspace rail, central recent-work area, and secondary invitation or notification panel;
- workspace switcher remains visible without dominating the task;
- keyboard users can traverse cards and switchers in a predictable order.

### Tablet

- navigation and dashboard panels collapse without hiding active role or Campaign context;
- cards maintain clear touch targets and status text;
- split views avoid exposing a previously selected protected preview after context switch.

### Mobile

- one primary column;
- active identity, role, and Campaign context remains visible near the top or in an accessible context control;
- role and Campaign switching uses a full-screen sheet or equivalent accessible pattern;
- invitation acceptance presents safe summary and explicit confirmation;
- notifications and recent work remain secondary to the main “continue” or “enter workspace” action.

### Platform consistency

Web, desktop, and later native shells share the same identity, invitation, dashboard projection, selected-context, permission, entitlement, and error contracts. Platform adapters may change sign-in presentation but not authority semantics.

## 14. Accessibility

### Required behavior

- sign-in methods have clear names and instructions;
- identity and role are announced when context changes;
- dashboard regions use semantic headings and landmarks;
- workspace cards expose name, role, status, and primary action in a logical accessible name;
- cards are not implemented as nested conflicting controls;
- keyboard users can accept or decline invitations, select roles, enter workspaces, and sign out;
- focus returns predictably after authentication, invitation dialogs, and switchers;
- session-expiry and revocation messages receive appropriate live announcement without flooding;
- status is never communicated by color alone;
- unread counts have textual equivalents;
- touch targets are adequate;
- high zoom does not hide identity, role, or sign-out;
- reduced motion removes decorative transitions;
- error messages identify the recoverable action without exposing hidden details;
- timeout warnings allow governed extension where the security policy permits;
- the mobile workspace switcher is fully operable by screen reader and keyboard.

### Privacy-aware accessibility

Accessible names, live regions, page titles, browser history, and notification text must not disclose protected Campaign or Character information beyond the current authorized projection.

## 15. Notifications and activity history

### Alpha notifications

The dashboard may show safe summaries for:

- invitation received;
- invitation expiring;
- membership approved or revoked;
- role changed;
- Character-control grant changed;
- Session available;
- GM approval item pending when the subject may know it;
- issue or recovery response;
- service maintenance.

### Notification safety

- notification generation uses current authorization context;
- notification opening reauthorizes the destination;
- revoked notifications become unavailable or are redacted;
- push notifications are deferred unless separately approved;
- lock-screen or OS-level notifications must use a separately approved privacy profile;
- counts must not leak hidden activity;
- Player-private or GM-only content is not copied into generic notification text.

### Activity history

The user may see a safe history of their own identity, invitation, membership, role, and workspace-entry events. Security-sensitive details remain internal.

## 16. Telemetry and diagnostics

Record structured operational signals for:

- authentication attempts and outcomes by adapter without secrets;
- subject resolution outcome;
- session establishment, expiry, revocation, and resume;
- invitation preview, acceptance, decline, expiry, and conflict outcome;
- dashboard latency and failure;
- authorized workspace count by coarse category only when safe;
- workspace-entry outcome;
- role-switch and Campaign-switch outcome;
- deep-link authorization outcome;
- permissions-version and entitlement-version mismatch;
- stale-context recovery;
- account-recovery case creation and resolution;
- accessibility interaction failures reported by tests;
- estimated provider and service cost.

### Redaction

Do not log:

- raw invitation tokens;
- authentication tokens;
- passwords or secret factors;
- private notes;
- GM-only content;
- hidden Campaign names when the logging subject is unauthorized;
- provider access credentials;
- full notification bodies;
- protected dashboard snapshots.

### Diagnostics bundle

A user-generated diagnostic bundle may contain:

- release ID;
- client version;
- coarse platform information;
- correlation IDs;
- user-safe error and reason codes;
- last successful authorization timestamp;
- selected adapter type;
- redacted feature flags.

It must exclude tokens and protected content.

## 17. Fixtures and content requirements

### Required subjects

- Player A;
- Player B;
- GM A;
- Assistant GM A;
- creator A;
- observer A;
- Owner/Admin A;
- service actor;
- unregistered subject;
- revoked subject;
- subject with conflicting provider mapping.

### Required Campaigns and workspaces

- Campaign Alpha, visible to Player A and GM A;
- Campaign Beta, visible to Player B and another GM fixture but hidden from Player A and GM A;
- one archived Campaign;
- one Campaign with pending membership;
- one creator draft workspace;
- one observer-only Session;
- one operational Owner/Admin workspace;
- one revoked membership;
- one expired role delegation.

### Required invitations

- valid invitation;
- expired invitation;
- revoked invitation;
- already accepted invitation;
- declined invitation;
- recipient-mismatch invitation;
- invitation to archived Campaign;
- duplicate acceptance request;
- token with invalid signature or digest;
- invitation requiring a content entitlement the subject lacks.

### Required recent-work references

- valid recent Character;
- valid recent Campaign;
- valid recent Session;
- revoked workspace;
- archived workspace;
- entitlement-changed workspace;
- hidden workspace belonging to another subject;
- stale route pointing to a removed object.

### Required devices

- desktop Player client;
- mobile GM client;
- keyboard-only path;
- screen-reader path;
- high-zoom path;
- interrupted network path.

## 18. Test scenarios

### Identity

1. New approved tester resolves exactly one stable internal subject.
2. Repeated sign-in through the same adapter resolves the same subject.
3. Provider display-name change does not change the subject ID.
4. Provider replacement preserves Campaign and Character references.
5. Revoked session cannot resume.
6. Sign-out clears protected client context.
7. Conflicting identity mapping does not auto-merge.

### Invitations

8. Valid invitation produces the correct membership and role exactly once.
9. Duplicate acceptance returns the authoritative prior result.
10. Expired, revoked, invalid, mismatched, and unauthorized invitations do not leak Campaign details.
11. Decline records the result without granting access.
12. Raw invitation token never appears in logs or diagnostics.

### Dashboard discovery

13. Player A sees only permitted Campaign Alpha and controlled Character entries.
14. Player A cannot infer Campaign Beta through counts, pagination, autocomplete, recent work, notifications, media, or timing-sensitive alternate responses where practical.
15. GM A sees only Campaigns with active GM or delegated roles.
16. Owner/Admin sees operational metadata but not protected play content without governed access.
17. No-workspace subject receives useful onboarding without global discovery.

### Workspace entry

18. Authorized Player and GM enter distinct projections of the same Campaign.
19. Workspace selection issues a bounded context receipt.
20. Direct deep link reauthorizes before resolving protected details.
21. Removed role invalidates dashboard card, deep link, recent work, and active context.
22. Role switch clears prior-context caches and subscriptions.
23. Character-control removal blocks Character workspace entry immediately after revocation propagation.

### Recovery and interruption

24. Interrupted invitation acceptance reconciles without duplicate membership.
25. Interrupted workspace switch never creates mixed context.
26. Reconnect revalidates session, permissions, entitlement, and context.
27. Cached protected cards do not reappear after revocation.
28. Identity-provider outage fails closed for protected entry.

### Accessibility and responsive behavior

29. Complete sign-in, invitation, dashboard, workspace selection, and sign-out with keyboard only.
30. Screen reader announces active identity, role, context, errors, and switch results.
31. Mobile and high-zoom layouts preserve context and sign-out controls.
32. Statuses and unread indicators remain understandable without color.

### Provider neutrality and cost

33. Local identity adapter passes the same contract tests as the provider-neutral port.
34. No domain object stores a named provider ID as primary identity.
35. Alpha flow runs with zero paid identity, notification, analytics, search, or billing service.

## 19. Acceptance criteria

All criteria are blocking for implementation-ready completion of the bounded alpha slice.

### IDW-AC-001 — Stable subject identity

Repeated approved sign-in resolves the same stable internal subject independent of display name, device, and provider-specific ID representation.

### IDW-AC-002 — Provider-neutral identity boundary

Domain records reference stable internal subject IDs; named provider SDKs and identifiers remain inside adapters and mapping records.

### IDW-AC-003 — Session lifecycle

Session establishment, resume, expiry, revocation, and sign-out behave deterministically and clear protected client context when authority ends.

### IDW-AC-004 — Invitation lifecycle

Valid, expired, revoked, declined, already-used, mismatched, and invalid invitations produce correct idempotent outcomes without leaking protected Campaign details.

### IDW-AC-005 — Role-aware dashboard

Each test subject receives only authorized workspace cards, roles, recent-work references, notifications, counts, and actions.

### IDW-AC-006 — No workspace enumeration

Unauthorized Campaigns, Characters, Sessions, creator drafts, and operational workspaces cannot be inferred through results, totals, pagination, aliases, autocomplete, media, deep links, recent work, or notifications.

### IDW-AC-007 — Explicit workspace context

Entering a workspace produces a bounded selected-context receipt containing stable subject, role, workspace, permission-version, entitlement-version, and expiry references.

### IDW-AC-008 — Entry reauthorization

Workspace cards, recent work, notifications, and deep links are reauthorized at open time and do not rely on stale client visibility.

### IDW-AC-009 — Context-switch isolation

Role and Campaign switching clears or partitions prior-context data, subscriptions, drafts, notification previews, and AI context so no protected data crosses contexts.

### IDW-AC-010 — Revocation

Membership, role, Character-control, invitation, and authentication revocation invalidate all affected discovery, entry, subscriptions, and cached context within the approved alpha propagation bound.

### IDW-AC-011 — Permission and entitlement separation

Membership, role, Character control, ownership, and entitlement decisions remain distinct and expose attributable internal reason codes.

### IDW-AC-012 — Player and GM separation

Distinct Player and GM subjects enter the same Campaign and receive different authorized projections without hidden-information leakage.

### IDW-AC-013 — Owner/Admin privacy boundary

Owner/Admin operational access does not automatically reveal Player-private or Campaign-private content; governed support access is required and audited.

### IDW-AC-014 — Recovery integrity

Interrupted sign-in, invitation acceptance, dashboard refresh, workspace entry, and role switching recover without duplicate subjects, duplicate memberships, mixed context, or restored revoked access.

### IDW-AC-015 — Accessibility

The primary identity, invitation, dashboard, workspace-selection, switch, and sign-out journeys pass keyboard, touch, screen-reader, high-zoom, reduced-motion, focus, and noncolor-status checks.

### IDW-AC-016 — Responsive behavior

Desktop, tablet, and mobile layouts preserve active identity, role, context, primary action, error recovery, and sign-out without hidden controls or protected stale previews.

### IDW-AC-017 — Privacy-safe telemetry

Logs, metrics, diagnostics, and audit records support troubleshooting without raw tokens, credentials, Player-private notes, GM-only content, or unauthorized workspace labels.

### IDW-AC-018 — Zero-service alpha operation

The bounded alpha identity and dashboard journey passes using local or test adapters with zero paid identity, billing, search, analytics, notification, or production service.

### IDW-AC-019 — Provider exit

Identity mappings, subject IDs, invitation history, membership, roles, Character-control grants, and relevant audit records are included in provider-neutral export and restore validation.

### IDW-AC-020 — Two-subject end-to-end proof

A distinct Player and GM authenticate on separate clients, select the same authorized Campaign, enter different role-safe workspaces, survive a role or membership change, and retain isolation through reconnect.

## 20. Performance and cost budgets

### Performance budgets for the bounded alpha fixture

- cached shell to identity-state determination: target at or below 300 ms excluding external human authentication;
- local/test session establishment after credential result: target at or below 500 ms;
- dashboard projection for the bounded alpha corpus: target at or below 700 ms server time and 1,200 ms usable client presentation on reference hardware;
- workspace switch: target at or below 800 ms to authorized usable projection;
- invitation validation after authentication: target at or below 700 ms;
- revocation propagation to active workspace and subscriptions: target at or below 5 seconds for the bounded online alpha;
- keyboard and screen-reader interaction must not be delayed by decorative animation;
- lists must remain usable with at least 100 authorized workspace references, while the alpha fixture may use fewer.

These are initial design budgets, not production service-level objectives.

### Cost controls

- zero paid identity provider required for local design and contract validation;
- zero billing provider;
- zero paid notification provider;
- zero paid search service;
- zero paid analytics service;
- no automatic provider upgrade;
- provider-specific cost signals remain observable;
- expected hosted alpha cost remains inside the separately approved project envelope;
- any spending requires owner approval.

## 21. Security, privacy, cost, and risk

### Security controls

- short-lived sessions or equivalent bounded session authority;
- protected refresh or resume credentials never exposed to logs;
- state and nonce validation for external-provider adapters when later used;
- invitation tokens are opaque, high-entropy, single-use or bounded-use, expiring, and stored as digests where practical;
- session fixation prevention;
- rate limits for sign-in, invitation lookup, and recovery;
- no account or Campaign enumeration;
- reauthorization on protected entry and mutation;
- revocation of sessions, memberships, roles, and control grants;
- least-privileged service actors;
- security event recording;
- dependency and secret scanning;
- provider-neutral contract tests.

### Privacy controls

- minimal identity profile;
- no public directory;
- no unnecessary device fingerprinting;
- no protected Campaign content in generic dashboard telemetry;
- no Player-private or GM-only data in notification summaries;
- explicit support-access boundary;
- retention and deletion behavior defined by later release policy;
- synthetic alpha fixtures rather than production personal data.

### Principal risks

- accidental workspace enumeration;
- provider ID becoming the domain identity;
- duplicate subject creation during recovery;
- stale permissions after role removal;
- cross-Campaign cache leakage during switching;
- invitation token exposure;
- confusing membership with entitlement;
- Owner/Admin access expanding beyond operational need;
- identity provider outage blocking testing;
- inaccessible sign-in or switcher;
- dashboard becoming a disconnected mock screen.

### Mitigations

- stable internal identity;
- deny-by-default discovery;
- selected-context receipts;
- server reauthorization;
- cache partition and clear rules;
- idempotent invitation acceptance;
- local/test adapter;
- deterministic fixtures;
- two-subject testing;
- accessibility requirements;
- provider-exit export;
- explicit implementation hold points.

## 22. Owner review points

Owner review is required before:

- selecting or paying for a production identity provider;
- enabling public self-registration;
- changing the internal-alpha invitation-only boundary;
- enabling production email, SMS, or push notification services;
- defining public profiles or Campaign discovery;
- enabling broad Owner/Admin support access to protected Campaign content;
- merging or splitting real user identities when evidence is ambiguous;
- changing the alpha role model materially;
- enabling anonymous access;
- activating production credentials;
- releasing internal alpha;
- public release.

The current packet does not require an immediate owner decision because it uses provider-neutral contracts and local/test adapters.

Silence is not approval.

## 23. Implementation handoff

### Recommended implementation decomposition

1. **Identity contracts**
   - stable subject;
   - provider mapping;
   - session lifecycle;
   - stable reason codes;
   - local/test adapter contract tests.

2. **Invitation contracts**
   - token validation;
   - safe preview;
   - acceptance and decline;
   - idempotency;
   - membership and role creation;
   - audit.

3. **Workspace-discovery service**
   - permission-safe Campaign, Character, Session, creator, observer, and operational references;
   - safe counts and recent work;
   - no enumeration;
   - entitlement integration.

4. **Dashboard projections**
   - role-aware sections;
   - loading, empty, blocked, stale, and revoked states;
   - responsive and accessible card/list patterns;
   - release identity and issue path.

5. **Selected-context contract**
   - explicit role and workspace;
   - permissions and entitlement versions;
   - expiry;
   - reauthorization;
   - route integration.

6. **Switch and deep-link flows**
   - role switch;
   - Campaign switch;
   - cache and subscription isolation;
   - safe fallback;
   - history replacement.

7. **Recovery and revocation**
   - interrupted acceptance;
   - session resume;
   - identity conflict;
   - revocation propagation;
   - stale recent-work cleanup.

8. **Telemetry and diagnostics**
   - redacted events;
   - correlation IDs;
   - performance and cost signals;
   - user-safe diagnostic bundle.

9. **Fixtures and acceptance suite**
   - distinct Player and GM;
   - hidden Campaign;
   - all invitation states;
   - role changes;
   - entitlement changes;
   - interruption and reconnect;
   - accessibility and responsive scenarios.

### Required implementation artifacts

- TypeScript or language-neutral schemas for subject, identity mapping, session, invitation, membership, role, Character-control grant, workspace reference, recent-work reference, and selected-context receipt;
- stable error and reason-code registry;
- local/test `IdentityPort` adapter;
- workspace-discovery contract;
- dashboard projection contract;
- invitation idempotency contract;
- role and workspace switch contract;
- client cache-partition and clearing contract;
- permission and entitlement integration tests;
- provider-exit export fixture;
- accessibility test evidence;
- two-device acceptance evidence;
- migration and rollback notes;
- security and privacy review.

### Required repository gates

- active P9-06 identity, persistence, migration, backup, restore, and provider-exit dependencies satisfied;
- F020 authorization contracts available;
- F019 entitlement contracts available for relevant content paths;
- provider-neutral contract tests pass;
- no production credentials;
- CI passes;
- independent security and accessibility review;
- owner approval only where a reserved decision is reached.

### Integration callers

This packet becomes the entry boundary for:

- Character creation and advancement;
- Campaign, Scene, and Session Builder;
- First Playable Action and GM Approval Loop;
- Relationship, social, and investigation workspaces;
- inventory and shared Assets;
- creator workspaces;
- onboarding and diagnostics;
- optional AI assistance.

## 24. Readiness decision

MV-IA-F003 is **implementation-ready as a design packet** when:

- all 24 required sections are present;
- IDW-AC-001 through IDW-AC-020 are traceable;
- the companion identity/workspace matrix validates;
- stable subject, session, invitation, membership, role, workspace, and context boundaries are explicit;
- Player/GM isolation, no-enumeration, revocation, recovery, provider-neutral, accessibility, responsive, cost, and provider-exit requirements are preserved;
- registry, packet index, backlog, and machine validation agree.

Implementation remains dependency-gated by the active P9-06 sequence and the concrete availability of identity, permission, entitlement, persistence, backup, restore, provider-exit, and caller-workflow foundations.

This packet does not authorize:

- paid identity or notification services;
- production credentials;
- public registration;
- production deployment;
- internal-alpha release;
- public release;
- blanket support access;
- irreversible provider coupling.

**Readiness result:** implementation-ready design; application implementation not started.
