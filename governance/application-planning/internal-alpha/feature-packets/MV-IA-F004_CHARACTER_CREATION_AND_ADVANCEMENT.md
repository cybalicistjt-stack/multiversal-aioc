# MV-IA-F004 — Character Creation and Advancement

**Feature ID:** MV-IA-F004  
**Feature version:** 0.1.0  
**Classification:** entry-critical  
**Design status:** implementation-ready  
**Owner:** John Brandon Turner  
**Primary roles:** Player, Game Master, Assistant GM, Owner/Admin, service actor  
**Stage A mapping:** A4 — Character Creation and Advancement  
**Historical module mapping:** Character Creation & Advancement  
**Prepared by:** Lead Documentation Architect / Character Systems and Progression Steward  
**Reviewed by:** product, game-system, architecture, canon, UX/accessibility, security, privacy, entitlement, persistence, recovery, QA, and documentation roles required before implementation  
**Date:** 2026-08-05

## 1. Problem and user outcome

### Problem

A Multiversal Character is not a flat form or a collection of display labels. It is a Campaign-scoped, governed record assembled from versioned content, rules-profile decisions, Player-authored identity, calculated values, control grants, Assets, Resources, Conditions, and an attributable advancement history.

Without a single authoritative Character workflow, later Session, combat, social, investigation, inventory, relationship, downtime, and AI features would each interpret Character state differently. Common failure modes include:

- selecting content by name instead of stable ID;
- mixing reusable Definitions with Character-owned state;
- trusting client-calculated prerequisites, costs, or derived values;
- losing the rules profile or pack versions used to create the Character;
- silently rewriting advancement history after respec, migration, or correction;
- allowing expired entitlements to destroy historical Character state;
- exposing Player-private notes or GM-only Character information;
- permitting two devices to overwrite one another;
- treating a local draft or offline edit as authoritative;
- granting control, ownership, or Campaign membership implicitly.

### Required outcome

An authorized Player can create, validate, save, reopen, and use a Character within an approved Campaign and rules profile. The Character can later receive an advancement award, prepare an advancement proposal, pass authoritative validation, obtain any required GM decision, commit exactly once, and show an understandable before-and-after record.

The Character remains usable across reconnects, pack updates, entitlement changes, migration, archival, and provider exit without silent loss, duplication, privilege expansion, or history rewriting.

### Why this belongs in internal alpha

Character creation is entry-critical because the first playable loop requires a real controlled Character with trustworthy Actions, Resources, derived values, permissions, entitlements, and history. It is also the first major domain feature that consumes the complete IA-D02 shared-foundation baseline.

## 2. Alpha slice

### Included

- [x] Create a Character draft from an authorized Campaign workspace.
- [x] Bind the draft to one approved Campaign, rules profile, creation policy, and pack-lock digest.
- [x] Record Player-authored identity fields separately from governed mechanical selections.
- [x] Select permitted species, form, background or equivalent origin components through the Universal Object Experience.
- [x] Select governed attributes, skills, proficiencies, Abilities, Actions, Effects, Resources, and initial equipment required by the bounded rules profile.
- [x] Display prerequisites, grants, conflicts, costs, limits, source links, and compatibility warnings before selection.
- [x] Calculate derived values through an authoritative, source-linked calculation contract.
- [x] Validate required fields, stable-ID references, prerequisite graphs, budgets, exclusivity, grants, Resource definitions, and Campaign compatibility.
- [x] Save, autosave, reopen, clone as a new draft where policy permits, and discard an unsubmitted draft.
- [x] Submit a Character for required GM review or activate immediately when the Campaign policy does not require review.
- [x] Record Character control grants separately from Campaign membership, role, and ownership.
- [x] Display a role-safe Character workspace with summary, build, Actions, Resources, Conditions, Assets, history, source links, validation, and save state.
- [x] Award advancement currency or an equivalent governed progression grant through an authoritative event.
- [x] Prepare, validate, approve when required, and commit one bounded advancement transaction.
- [x] Preserve the pre-advancement state, cost ledger, calculation evidence, and accepted result.
- [x] Support an explicit correction or respec proposal without deleting prior history.
- [x] Preserve historical selections when entitlement or pack access changes while blocking unauthorized new selection.
- [x] Support loading, empty, forbidden, restricted, stale, conflict, failed-save, migration-required, archived, and recovery-required states.
- [x] Provide desktop, tablet, mobile, keyboard, touch, screen-reader, high-zoom, reduced-motion, and noncolor-status behavior.
- [x] Provide deterministic fixtures and denied-case tests.

### Explicitly excluded

- [x] The entire unrestricted Multiversal content corpus.
- [x] Public Character marketplace, public profile directory, ratings, or monetized sharing.
- [x] Automatic AI-generated builds, biographies, portraits, or advancement decisions.
- [x] AI mutation of Character state.
- [x] Full appearance sculpting comparable to a 3D character creator.
- [x] Unbounded multicampaign Character transfer.
- [x] Automatic conversion between incompatible rules profiles.
- [x] Destructive history editing.
- [x] Silent last-write-wins.
- [x] Offline authoritative creation, activation, advancement, respec, ownership transfer, or control transfer.
- [x] Full inventory, crafting, vehicle, relationship, social, investigation, or combat interfaces; this packet exposes only the Character-facing summaries and references those features require.
- [x] Canonical publication of Player-created Character content.
- [x] Production identity, payment, analytics, hosted search, or AI provider selection.
- [x] Internal-alpha release authorization.

### Full long-term scope deferred

Later work may expand lifepath construction, deeply branching progression, visual appearance, cross-Campaign export and import, public or private sharing, richer companions and followers, organization membership, automated build comparison, localization, and optional governed AI explanation. Those additions must preserve this packet's stable IDs, rules snapshots, authority separation, advancement ledger, permission boundary, recovery behavior, and history-preserving migration.

## 3. Roles and authority

| Role | Allowed actions | Hidden information | Approval required |
|---|---|---|---|
| Player | Create and edit own authorized drafts; inspect permitted source-linked options; submit; use controlled active Characters; prepare advancement or correction proposals | Cannot read another Player's private fields, GM-only Character fields, hidden Campaign rules, unavailable content, or another Character's protected history | Campaign policy may require GM approval for activation, advancement, respec, or correction |
| Game Master | Define Campaign Character policy; review role-safe submissions; approve, deny, or return for revision; award progression; inspect GM-authorized Character data | Cannot read Player-private notes unless an explicit approved policy or support-access record permits it; cannot alter history silently | Owner gates remain for canon, paid services, production, and release |
| Assistant GM | Perform only explicitly delegated review, award, or inspection actions | No implicit full-GM access and no access outside delegation | Active scoped delegation |
| Owner/Admin | Manage alpha policy, fixtures, migrations, and operational evidence | Operational role does not automatically grant Player-private or Campaign-private content access | Governed Campaign role or time-bounded support access for protected play content |
| Service actor | Validate, calculate, persist, project, migrate, export, and notify within operation-specific capabilities | No independent membership, Character control, entitlement, or visibility authority | Service credential plus subject- and operation-scoped authorization |
| AI | Optional read-only explanation using a narrower projection derived from the initiating subject | No hidden content, no private notes, no GM truth, no independent retrieval or mutation | Explicit user request and policy; never required for the core path |

Identity, Campaign membership, active role, Character control, ownership, entitlement, and approval authority are separate decisions.

Silence is not approval.

## 4. Dependencies

### Feature dependencies

- **MV-IA-F002 — Universal Object Experience** supplies stable-ID browse, inspection, source, provenance, comparison, and constrained selection.
- **MV-IA-F003 — Identity, Dashboard, and Workspace Selection** supplies stable subject identity, Campaign entry, Character workspace discovery, control context, and selected-context receipts.
- **MV-IA-F019 — Content Library and Entitlements** supplies free, granted, sponsored, restricted, expired, and historical-use decisions.
- **MV-IA-F024 — Pack Lifecycle and Canonical Content Registry** supplies version-pinned content, pack locks, dependencies, migration maps, supersession, and removal safety.
- **MV-IA-F020 — Permissions and Hidden Information** controls read, write, search, projection, history, export, diagnostics, and AI visibility.
- **MV-IA-F021 — Autosave, Reconnect, Recovery, and Bounded Offline Use** controls drafts, idempotency, status lookup, conflict preservation, offline boundaries, and recovery.
- **MV-IA-F025 — Onboarding, Help, Diagnostics, and Issue Reporting** consumes Character routes, validation states, release identity, and safe diagnostic evidence.

### Shared systems

- SS-02 — Identity and role context.
- SS-03 — Authorization and visibility.
- SS-04 — Entitlement evaluation.
- SS-05 — Universal object experience.
- SS-06 — Proposal and approval framework.
- SS-07 — Persistence, drafts, and state versions.
- SS-08 — Realtime and reconnect.
- SS-10 — Ownership and Asset transfer, for initial equipment references and later inventory integration.
- SS-11 — Rules inspection and calculation presentation.
- SS-12 — Activity, history, and timeline.
- SS-13 — Notifications and work queues.
- SS-14 — Validation and issue presentation.
- SS-15 — Accessibility behavior.
- SS-16 — Responsive information hierarchy.
- SS-17 — Content pack lifecycle.
- SS-18 — Telemetry and diagnostics.
- SS-19 — Help and source-grounded explanation.

### Service ports and adapters

Required provider-neutral interfaces include:

- `CharacterDraftPort`;
- `CharacterRepositoryPort`;
- `CharacterProjectionPort`;
- `CharacterValidationPort`;
- `CharacterCalculationPort`;
- `CharacterAdvancementPort`;
- `CharacterControlPort`;
- `CharacterMigrationPort`;
- `CharacterExportPort`;
- `AuthorizationPort`;
- `EntitlementPort`;
- `ObjectCatalogPort`;
- `PackRegistryPort`;
- `NotificationPort`;
- `AuditEventPort`;
- `TelemetryPort`.

Deterministic local adapters are required for development and CI.

### Canonical objects and packs

The bounded alpha corpus must represent:

- species and forms;
- attributes and derived values;
- skills and proficiencies;
- Abilities across at least two tiers;
- Actions;
- Effects;
- Conditions;
- Resources;
- initial items and equipment;
- source and provenance records;
- rules profile, creation policy, advancement policy, and pack-lock records.

### Schemas and migrations

Required contracts include:

- Character draft and authoritative Character aggregate;
- Character identity profile;
- Character build selection;
- Character calculation input, trace, and result;
- Character validation finding;
- Character control grant;
- activation proposal and decision;
- advancement award, proposal, cost ledger, decision, and receipt;
- correction or respec proposal and receipt;
- Character projection;
- Character history Event;
- Character snapshot;
- migration plan and migration receipt;
- export manifest.

### Decisions and gates

- Stage A A4 exit condition.
- IA-D02-006 shared-foundation contract baseline.
- Campaign rules-profile and creation-policy approval.
- Alpha fixture and pack-lock approval.
- Security and privacy review before real user data.
- Owner approval before alpha-ready status or release.

Implementation remains dependency-gated by the active P9-06 sequence.

## 5. Object and state model

### Reusable Definitions

Species, forms, attributes, skills, proficiencies, Abilities, Actions, Effects, Conditions, Resources, equipment, rules, and progression options remain reusable governed Definitions. A Character stores stable references and accepted state; it does not copy Definitions into editable local truth.

### Campaign placements or bindings

A Character is bound to:

- `campaignId`;
- `rulesProfileId` and version;
- `creationPolicyId` and version;
- `advancementPolicyId` and version;
- `packLockDigest`;
- allowed source set;
- Character-control grants;
- Campaign-local labels, visibility, and status.

The Campaign binding may constrain available options without modifying their reusable Definitions.

### Live instances and state

The Character aggregate includes:

- `characterId`;
- lifecycle state;
- identity profile;
- controller grants;
- build selections;
- granted selections;
- calculated and derived values;
- current and maximum Resources;
- active Conditions;
- Asset references;
- progression balances;
- advancement ledger;
- validation state;
- current version;
- projection version;
- created, activated, retired, archived, and migrated metadata.

Player-authored descriptive fields are stored separately from governed mechanics. Current Resources, Conditions, and Assets are live state rather than build Definitions.

### Events and history

At minimum, the authoritative history supports:

- `CharacterDraftCreated`;
- `CharacterDraftSaved`;
- `CharacterSubmitted`;
- `CharacterReturnedForRevision`;
- `CharacterActivated`;
- `CharacterControlGranted`;
- `CharacterControlRevoked`;
- `AdvancementAwarded`;
- `AdvancementProposed`;
- `AdvancementApproved`;
- `AdvancementDenied`;
- `AdvancementCommitted`;
- `CharacterCorrectionProposed`;
- `CharacterCorrectionCommitted`;
- `CharacterMigrated`;
- `CharacterRetired`;
- `CharacterArchived`;
- `CharacterRestoredFromCheckpoint`.

Events are attributable and append-only. A correction adds new evidence and state; it does not erase the prior accepted event.

### Projections and indexes

Required projections include:

- Character card;
- Character workspace summary;
- Player Character sheet;
- GM Character review;
- build and prerequisites;
- calculation trace;
- advancement ledger;
- history timeline;
- validation summary;
- source and provenance links;
- portable export summary.

Indexes are derived and permission-filtered. Search results never reveal hidden Characters, controllers, Campaigns, or protected fields.

### Stable IDs

All governed selections use stable IDs and resolved versions or compatibility policies. The Character, draft, controller grant, proposal, advancement, decision, Event, snapshot, migration, and export records each have stable IDs. Display names, filenames, provider IDs, and array positions are not authoritative identities.

### Provenance

Every mechanical selection and calculated grant retains source and pack references sufficient to answer:

- which Definition and version supplied it;
- whether it was selected, granted, inherited, migrated, or corrected;
- which rule or policy permitted it;
- which accepted event introduced it;
- whether current access permits new use;
- which source coordinate explains the rule.

## 6. Primary user flow

1. Player enters an authorized Campaign workspace using a current selected-context receipt.
2. Player chooses **Create Character**.
3. Service verifies subject, Campaign membership, role, creation permission, entitlement policy, rules profile, and pack lock.
4. Service creates an empty Character draft with stable IDs and policy snapshots.
5. Player enters identity and descriptive fields.
6. Player uses constrained Universal Object pickers for species, form, background or equivalent origin, attributes, skills, proficiencies, Abilities, Resources, and initial equipment.
7. Each selection request is reauthorized and checked for entitlement, pack availability, lifecycle, version, prerequisites, exclusivity, budgets, and caller constraints.
8. Service returns calculation and validation updates with source-linked explanations.
9. Local autosave preserves the draft; authoritative save uses expected version and idempotency.
10. Player reviews the complete Character summary, unresolved findings, grants, costs, and source links.
11. Player submits the Character.
12. Service revalidates the entire aggregate against current policy and pack lock.
13. When Campaign policy requires review, a durable proposal enters the GM queue; otherwise the service activates the Character.
14. GM reviews the Player-safe submission plus authorized GM findings, then approves, denies, or returns it for revision.
15. Accepted activation commits exactly once, records the Character history, issues a receipt, and exposes the active Character workspace.
16. Later, an authorized progression award is recorded.
17. Player prepares an advancement proposal using the same stable-ID and calculation rules.
18. Service validates costs, prerequisites, limits, entitlement, policy, and expected Character version.
19. Required GM decision is recorded.
20. Accepted advancement commits exactly once, updates the projection, preserves before-and-after evidence, and adds an advancement-ledger entry.

## 7. Alternate and secondary flows

### Create from an approved template

A template supplies permitted starting selections and explanations. The service expands template references into a new draft, revalidates every grant and choice, and never shares another Character's identity or private state.

### Save and resume

A Player may close and reopen a draft. Resume revalidates Campaign membership, control, permissions, entitlements, rules profile, pack lock, and draft version before protected fields render.

### Clone as new draft

Where Campaign policy permits, an authorized Character or template may seed a new draft. The clone receives new IDs, no copied history, no copied private notes from another subject, and no implied control or ownership.

### Return for revision

A GM may return a submitted Character with role-safe findings. The proposal remains in history, the draft becomes editable, and previously submitted evidence is retained.

### Advancement denied or modified

A denied advancement records the decision without applying effects. A GM modification is represented as an explicit proposed delta that the Player can inspect where policy requires; it cannot silently change unrelated Character fields.

### Correction or respec

An authorized proposal identifies the original event, reason, affected selections, budget treatment, resulting state, and history impact. Accepted correction appends compensating events and a new snapshot. It never deletes the original record.

### Entitlement expires

Historical accepted selections remain visible and usable according to policy. New selection, replacement, or advancement into restricted content is denied until an active access source exists. No hidden paid catalog details are leaked.

### Pack or rule version changes

The Character stays pinned to its accepted references until a governed migration. The UI shows compatibility state and a migration preview. No silent substitution occurs.

### Character retirement or archival

Retirement blocks ordinary active use but preserves history and Campaign references. Archival is reversible only through an authorized workflow and never deletes accepted events.

### Export

An authorized subject may create a role-safe, provider-neutral export manifest containing the permitted Character state, stable references, pack and rules identities, history scope, and checksums. Player-private and GM-only material follow explicit export policy.

## 8. Failure, empty, and recovery states

| State | User sees | Allowed action | Preserved data | Evidence |
|---|---|---|---|---|
| Loading | Active Campaign, Character or draft context and progress | Cancel, wait, navigate safely | Local draft and route | Operation and correlation IDs |
| Empty | Guided first field or no permitted options | Continue identity fields, change category, inspect access reason | Draft | Safe reason code |
| Validation error | Field- and aggregate-level findings with source links | Correct, inspect, save draft, or abandon | Full draft | Finding IDs and policy version |
| Forbidden | Safe unavailable state | Return, switch authorized context, or use governed access request | Local nonprotected draft where permitted | User-safe denial code |
| Restricted entitlement | Limited explanation without catalog leakage | Choose permitted option or obtain access outside this workflow | Draft and previous accepted state | Entitlement decision reference |
| Offline | Read authorized snapshot and edit approved local draft fields only | Continue local draft, export local draft where allowed, reconnect | Local draft and manifest-bound snapshot | Offline manifest |
| Stale | Expected Character, draft, policy, or pack version changed | Refresh, compare, reconcile, or cancel | Local and authoritative versions | Conflict record |
| Conflict | Side-by-side safe comparison and allowed resolutions | Keep local as new draft, adopt server state, or create explicit merge proposal | Both states | Conflict ID |
| Failed save | Clear that authoritative acceptance is unknown or failed | Retry same operation ID or look up status | Local draft | Save operation status |
| Pending GM | Durable review state | Withdraw when policy permits, view status, continue unrelated work | Submitted snapshot | Proposal ID |
| Migration required | Current Character remains pinned and may be restricted | Preview migration, postpone where policy permits, or request review | Original state and history | Migration plan ID |
| Archived or retired | Read-only history and status | Restore through authorized workflow, export, or return | Entire retained history | Lifecycle event |
| Recovery required | Guided reconnect, checkpoint, or draft reconciliation | Resume, compare, restore verified checkpoint, or discard local draft | Draft, accepted events, snapshots | Recovery receipt |

## 9. Permissions and hidden information

Authorization and entitlement filtering occur before Character discovery, card counts, autocomplete, source lookup, build options, calculation inputs, history, exports, diagnostics, notifications, realtime subscriptions, or AI retrieval.

Character fields are classified independently:

- Campaign-shared identity and summary;
- controller-visible mechanics;
- Player-private notes;
- GM-only annotations or hidden Conditions;
- operational metadata;
- security-sensitive records;
- secret material that is never exposed.

The server generates role-safe projections. The client never receives hidden fields merely to conceal them visually.

Required denied-case tests include:

- wrong-Campaign Character lookup;
- noncontroller Player opening protected Character fields;
- revoked controller reusing a stale Character workspace;
- Assistant GM exceeding delegation;
- Owner/Admin reading Player-private notes without governed access;
- exact-ID lookup of a hidden Character;
- hidden Character counts through search or dashboard summaries;
- Player receiving GM-only Conditions or annotations;
- export containing another subject's private fields;
- diagnostics including Character prose, notes, or hidden mechanics without explicit selection and policy;
- AI retrieving hidden Character content;
- advancement after control revocation;
- self-awarded progression;
- client-supplied calculated values overriding server calculation;
- draft cloned from another Character carrying control, private notes, or history;
- guessed object-storage attachment access.

## 10. Entitlements

- **Access sources:** free policy, direct approved access, Campaign grant, sponsored access, owner-approved alpha fixture.
- **Free-tier behavior:** expose only content permitted by the active free policy; do not infer restricted catalog details.
- **Campaign grants:** scoped to the Campaign and subject or role policy; not transferable to unrelated Campaigns.
- **Sponsored access:** explicit source, scope, start, expiry, and reason.
- **Expiry behavior:** blocks unauthorized new selection, replacement, or advancement; does not silently erase accepted Character history.
- **Historical-state behavior:** accepted references remain preserved and explainable. Usability follows the approved historical-use policy.
- **Search and preview restrictions:** filtering occurs before counts, ranking, facets, aliases, and previews.
- **Offline snapshot behavior:** only manifest-listed, previously authorized Character projections and local draft fields are available; no offline authoritative mutation.

## 11. Persistence and history

- **Draft storage:** local autosave plus provider-neutral authoritative draft repository where online.
- **Authoritative save:** expected version, idempotency key, subject, selected context, Character or draft ID, policy versions, pack lock, and validation summary.
- **Aggregate boundary:** one Character aggregate controls identity profile, build, calculated grants, progression balances, lifecycle, and references to live subsystems. Inventory transactions and Session state retain their own aggregate boundaries.
- **Expected-version behavior:** stale writes fail safely and produce a conflict record; no silent last-write-wins.
- **Idempotency:** creation, save, submit, activation, award, advancement, correction, migration, retirement, archival, and restore use stable operation IDs.
- **Event types:** those defined in Section 5 plus policy-approved extension events.
- **Snapshot or checkpoint behavior:** snapshots accelerate projection and recovery but never replace append-only accepted events.
- **Audit events:** permission changes, control grants, approvals, denials, migrations, exports, support access, and protected diagnostics.
- **Migration behavior:** previewable, versioned, checksum-verified, reversible when defined, and history preserving.
- **Export behavior:** provider-neutral, permission-safe, manifest-bound, checksummed, and source linked.

## 12. Realtime, interruption, and reconnect

- Before local submission, only local draft state exists.
- After submission but before acceptance, the UI shows submitted or status-unknown and looks up the original operation ID.
- After acceptance but before display, reconnect retrieves current authoritative projection and the accepted receipt without duplicating effects.
- During pending approval, the durable proposal survives disconnect and service restart.
- After missed Events, the client resumes from the last acknowledged sequence and suppresses duplicates.
- A stale client receives current versions and a governed reconciliation path.
- A second device cannot silently overwrite the first; both states are preserved when needed.
- After service restart, idempotency and status lookup recover accepted operations.
- Permission, entitlement, control, policy, pack, and lifecycle changes invalidate affected subscriptions and projections.
- No offline authoritative mutation is permitted.

## 13. Interface and information hierarchy

### Desktop

Use a staged Character workspace with:

- persistent Character summary and save state;
- step navigation for identity, origin, attributes, skills, Abilities, Resources, equipment, review, and advancement;
- central editor;
- right-side inspector for source, prerequisites, grants, costs, conflicts, and validation;
- history and advancement ledger as secondary tabs;
- visible active Campaign, rules profile, pack lock, Character state, and controller context.

### Tablet

Use one primary editor with collapsible step navigation and a full-height inspector. Preserve selection, validation, and scroll position when the inspector opens.

### Mobile

Use a single-focus sequence:

1. step list;
2. field or picker;
3. inspector;
4. validation and summary;
5. save or submit.

Primary actions remain reachable without hover or drag. Long tables become grouped lists with equivalent information.

### Player hierarchy

Foreground:

- current step and completion;
- available budget or progression balance;
- prerequisites and conflicts;
- selected options and grants;
- Resource and Action consequences;
- save, submit, and advancement status.

Secondary:

- detailed source coordinates;
- full calculation trace;
- migration metadata;
- operational evidence.

### GM hierarchy

Foreground at review time:

- Character identity and controller;
- Campaign and policy versions;
- unresolved blocking findings;
- selected and granted mechanics;
- budgets and prerequisites;
- calculation differences;
- restricted or migrated content;
- before-and-after advancement delta;
- approve, deny, return, or policy-permitted modify.

## 14. Accessibility

- Semantic headings, landmarks, fieldsets, lists, tables, and status regions.
- Complete keyboard access to steps, pickers, inspectors, comparison, validation, and submission.
- Focus returns to the invoking field after inspector or picker close.
- Screen-reader names include field, selected value, source, state, and required action.
- Save, validation, submission, approval, and conflict changes use appropriately prioritized live announcements.
- Layout supports high zoom and text reflow without horizontal scrolling for ordinary content.
- Validation, entitlement, lifecycle, and conflict states never depend on color alone.
- Motion is optional and reduced-motion preferences are honored.
- Touch targets meet the approved target-size baseline.
- Every drag interaction has buttons, menus, or ordered-list alternatives.
- Build trees and prerequisite graphs have equivalent list or table views.
- Errors identify the field, reason, consequence, and permitted recovery.
- Dense Character sheets support logical region navigation and skip links.

## 15. Notifications and queues

| Trigger | Recipient | Message content | Action | Resolution state |
|---|---|---|---|---|
| Character submitted | Authorized GM or delegate | Safe Character label, controller, Campaign, blocking finding count | Open review | approved, denied, returned, withdrawn |
| Character returned | Controller | Safe reason summary and affected sections | Resume draft | resubmitted or abandoned |
| Character activated | Controller and permitted GM | Character and activation receipt | Open Character | acknowledged |
| Advancement awarded | Controller | Safe amount or grant and source | Prepare advancement | spent, expired, revoked, or retained |
| Advancement submitted | Authorized GM when required | Character, requested delta, warnings | Review | approved, denied, returned |
| Advancement committed | Controller and permitted GM | Safe before-and-after summary | Open ledger | acknowledged |
| Control revoked | Affected subject | Access ended without hidden detail | Return to dashboard | acknowledged |
| Migration required | Controller and authorized GM | Character, compatibility state, safe next action | Preview migration | migrated, postponed, blocked |
| Save or recovery failure | Current editor | Safe state and operation ID | Retry or inspect status | recovered or abandoned |

Counts and previews are generated from the authorized set.

## 16. AI involvement

**AI mode:** optional read-only or proposed explanation only

- **Allowed action:** explain visible rules, prerequisites, grants, validation findings, calculation traces, or compare permitted options.
- **Allowed sources:** the initiating subject's role-safe Character projection and permitted source records.
- **Permission and entitlement checks:** identical to non-AI retrieval, with a narrower AI policy.
- **Provenance:** every substantive explanation links to permitted stable IDs and source references.
- **Uncertainty:** clearly distinguish rule evidence, calculation output, and nonauthoritative suggestion.
- **Cost boundary:** zero AI is required for every creation and advancement path.
- **Non-AI fallback:** structured source-linked UI and deterministic validation.
- **Prohibited behavior:** automatic build creation, hidden content retrieval, independent Character control, award creation, approval, mutation, entitlement bypass, or canonical recommendation.

## 17. Telemetry and diagnostics

- Stable operation IDs for draft creation, save, submit, activation, advancement, correction, migration, export, and recovery.
- Correlation IDs across client, application service, persistence, calculation, authorization, entitlement, and notification adapters.
- Bounded timings for Character load, option query, validation, calculation, save, submit, and projection refresh.
- Safe error events using stable reason codes.
- Permission and entitlement denials recorded without protected payload.
- Reconnect, missed-Event, stale-version, conflict, duplicate, and status-unknown events.
- Diagnostic generation defaults to exclude.
- Character prose, Player-private notes, GM-only fields, source text, and full calculation inputs are excluded unless separately allowlisted, explicitly selected, previewed, redacted, and consented.
- Issue-report attachments follow F025 quarantine, checksum, and access rules.
- Cost signals include storage size, validation work, calculation duration, migration work, and optional AI usage.
- No credential, token, cookie, raw authorization header, or unrelated Campaign data.

## 18. Test scenarios

### Unit

- [x] Budget, prerequisite, exclusivity, grant, cost, and derived-value calculations.
- [x] Stable-ID normalization and supersession handling.
- [x] Advancement and correction ledger arithmetic.
- [x] Role-safe field classification.

### Contract

- [x] Character draft, save receipt, calculation trace, validation finding, activation proposal, advancement receipt, migration receipt, and export manifest.
- [x] Authorization, entitlement, object catalog, pack registry, and notification port behavior.
- [x] Idempotent status lookup after ambiguous failure.

### Integration

- [x] Universal Object picker to Character save.
- [x] Campaign policy and pack lock to full validation.
- [x] GM review to activation.
- [x] Advancement award to committed ledger.
- [x] Entitlement expiry and pack migration without history loss.

### End-to-end

- [x] Primary Player creates, saves, submits, receives approval, reopens, advances, disconnects, reconnects, and verifies history.
- [x] Second Player cannot discover or open the first Player's protected Character.
- [x] GM returns a Character, Player revises, and resubmits.
- [x] Correction appends compensating evidence instead of deleting history.

### Permission and hidden information

- [x] Every denied case from Section 9.
- [x] Search, counts, recent work, notifications, export, diagnostics, realtime, object storage, and AI surfaces.
- [x] Revocation while the Character workspace is open.

### Entitlement

- [x] Free content, Campaign grant, sponsored access, restricted option, expired access, and preserved historical selection.
- [x] No restricted count, alias, or prerequisite leakage.

### Persistence and migration

- [x] Duplicate create, save, submit, award, advancement, correction, and migration operations.
- [x] Stale expected version and second-device conflict.
- [x] Pack update, superseded stable ID, interrupted migration, verified retry, and provider-exit export.

### Reconnect and recovery

- [x] Interruption before submit, after send, after accept, during GM review, after event commit, during service restart, and from a second device.
- [x] Corrupted local draft and verified checkpoint recovery.
- [x] No duplicate advancement or activation effects.

### Accessibility

- [x] Keyboard-only complete creation and advancement.
- [x] Screen-reader creation, validation, review summary, conflict resolution, and history.
- [x] High zoom, narrow mobile, reduced motion, noncolor status, long names, many Conditions, and dense build fixtures.

### Performance

- [x] Bounded approved corpus option query and validation budgets.
- [x] Large but approved Character fixture with many selections, Conditions, Assets, and history.
- [x] Reopen and reconnect projection budgets.

### Golden or deterministic regression

- [x] 8D-007J applies. Golden Character fixtures must produce deterministic validation findings, calculation traces, accepted deltas, Events, projections, and migration results for the same pinned inputs.

## 19. Acceptance criteria

1. **CCA-AC-001 — Authorized draft creation**  
   **Condition:** An authorized Player creates a draft bound to the correct Campaign, rules profile, policies, subject, and pack lock.  
   **Evidence:** Draft record, authorization decision, selected-context reference, and creation receipt.  
   **Blocking:** yes

2. **CCA-AC-002 — Stable-ID selections**  
   **Condition:** Every governed mechanical selection uses a stable ID and resolved version or compatibility policy.  
   **Evidence:** Persisted build record and source-linked selection receipts.  
   **Blocking:** yes

3. **CCA-AC-003 — Authoritative validation**  
   **Condition:** The server rejects missing prerequisites, invalid budgets, exclusivity conflicts, unavailable packs, lifecycle-invalid objects, and incompatible rules.  
   **Evidence:** Deterministic validation matrix and denied operation receipts.  
   **Blocking:** yes

4. **CCA-AC-004 — Explainable calculations**  
   **Condition:** Derived values and grants are calculated authoritatively and provide an ordered source-linked trace.  
   **Evidence:** Calculation input digest, trace, result, and golden regression output.  
   **Blocking:** yes

5. **CCA-AC-005 — Draft persistence**  
   **Condition:** Local autosave and authoritative save clearly distinguish state, use expected versions, and never claim an unaccepted save succeeded.  
   **Evidence:** Draft autosave receipts, authoritative save receipts, and failure-injection results.  
   **Blocking:** yes

6. **CCA-AC-006 — Idempotent submission and activation**  
   **Condition:** Repeated submit or activation operations commit no duplicate Character or activation effect.  
   **Evidence:** Operation-status lookup and single accepted Event sequence.  
   **Blocking:** yes

7. **CCA-AC-007 — Governed approval**  
   **Condition:** Campaign policy determines whether activation or advancement requires GM approval, and the recorded decision is attributable.  
   **Evidence:** Policy snapshot, proposal, decision, and receipt.  
   **Blocking:** yes

8. **CCA-AC-008 — Separate control authority**  
   **Condition:** Character control is represented by explicit scoped grants and is not inferred from membership, role, ownership, identity, or device.  
   **Evidence:** Control-grant tests and denied cases.  
   **Blocking:** yes

9. **CCA-AC-009 — Role-safe projections**  
   **Condition:** Player, GM, Assistant GM, Owner/Admin, service, export, diagnostic, and AI surfaces receive only authorized fields.  
   **Evidence:** Projection snapshots and hidden-information tests.  
   **Blocking:** yes

10. **CCA-AC-010 — Revocation enforcement**  
    **Condition:** Control, membership, role, entitlement, or support-access revocation invalidates affected workspaces, caches, subscriptions, exports, and attachments.  
    **Evidence:** Open-screen revocation and stale-cache tests.  
    **Blocking:** yes

11. **CCA-AC-011 — Historical entitlement preservation**  
    **Condition:** Expired or removed access cannot enable new restricted selection but does not silently delete accepted Character references or history.  
    **Evidence:** Entitlement expiry fixture and before-and-after export.  
    **Blocking:** yes

12. **CCA-AC-012 — Advancement integrity**  
    **Condition:** An accepted advancement consumes the correct governed balance once, applies the approved delta once, and records before-and-after evidence.  
    **Evidence:** Advancement ledger, Event sequence, calculation trace, and duplicate-command test.  
    **Blocking:** yes

13. **CCA-AC-013 — Correction without erasure**  
    **Condition:** A correction or respec appends compensating records and retains the original accepted history.  
    **Evidence:** Correction proposal, accepted Events, snapshots, and history projection.  
    **Blocking:** yes

14. **CCA-AC-014 — Conflict preservation**  
    **Condition:** Concurrent or stale edits never use silent last-write-wins and preserve both local and authoritative state when user disposition is required.  
    **Evidence:** Second-device conflict record and recovery receipt.  
    **Blocking:** yes

15. **CCA-AC-015 — Reconnect safety**  
    **Condition:** Interruption at every defined point recovers status through stable IDs without duplicate activation, award, advancement, or correction effects.  
    **Evidence:** Failure-injection matrix and resulting Event counts.  
    **Blocking:** yes

16. **CCA-AC-016 — Offline boundary**  
    **Condition:** Offline use is limited to manifest-authorized reading and approved local drafting; no offline authoritative mutation is accepted.  
    **Evidence:** Offline capability tests and prohibited-operation receipts.  
    **Blocking:** yes

17. **CCA-AC-017 — Migration safety**  
    **Condition:** Pack or rules migration is previewable, versioned, checksum-verified, history preserving, and never silently substitutes incompatible content.  
    **Evidence:** Migration plan, interrupted retry, receipt, and export comparison.  
    **Blocking:** yes

18. **CCA-AC-018 — Accessible equivalent path**  
    **Condition:** Character creation, validation, submission, advancement, conflict resolution, and history are operable by keyboard, screen reader, touch, high zoom, and narrow mobile layouts.  
    **Evidence:** Accessibility test matrix and manual review receipt.  
    **Blocking:** yes

19. **CCA-AC-019 — Privacy-safe diagnostics**  
    **Condition:** Diagnostic generation excludes protected Character content by default and requires allowlisting, preview, redaction, consent, quarantine, and checksums for attachments.  
    **Evidence:** Diagnostic manifest and denied-case tests.  
    **Blocking:** yes

20. **CCA-AC-020 — Zero-service core and release boundary**  
    **Condition:** The complete alpha Character path works with deterministic local adapters, zero AI, and zero paid services, and no artifact claims implementation or release authorization.  
    **Evidence:** CI run, adapter configuration, cost review, and authorization flags.  
    **Blocking:** yes

## 20. Fixtures and approved alpha content

- **Required identities:** Owner/Admin, primary GM, Assistant GM, primary Player, second Player, revoked former controller, service actor, optional AI service actor.
- **Required Campaign:** IA-CAMPAIGN-01 with approved rules profile and pack lock; IA-CAMPAIGN-02 for isolation.
- **Required Characters:**
  - valid Player Character using free or Campaign-granted content;
  - valid higher-tier Character with approved access;
  - invalid Character with missing prerequisite;
  - Character with active Conditions and depleted Resources;
  - Character with personal and shared Asset references;
  - Character with relationship history;
  - retired or archived Character;
  - Character with migration history;
  - two-device conflicting draft fixture;
  - pending-approval Character;
  - advancement-ready Character with a deterministic balance and proposed delta.
- **Required packs:** version-pinned alpha rules and content packs with install, update, dependency, blocked-removal, reinstall, migration, export, and import fixtures.
- **Required objects:** representative species or forms, attributes, skills, proficiencies, Abilities across at least two tiers, Actions, Effects, Conditions, Resources, equipment, rules, sources, and provenance.
- **Required hidden information:** Player-private note, GM-only Character field, hidden Condition or annotation, restricted option, wrong-Campaign Character, revoked controller.
- **Required historical state:** creation, return for revision, activation, award, advancement, correction, migration, retirement, archival, and restore Events.
- **Required failure fixtures:** missing prerequisite, invalid stable ID, unavailable pack, stale version, failed save, status unknown, duplicate command, entitlement expiry, permission revocation, corrupted draft, interrupted migration, checksum mismatch, and provider-exit import mismatch.

Fixture IDs and exact approved object selections remain part of IA-D03-004.

## 21. Security, privacy, cost, and risk

### Security

- [x] Server authorization and field-safe projection.
- [x] Stable subject, Campaign, role, controller, entitlement, pack, policy, version, and lifecycle checks at every protected operation.
- [x] Idempotency, expected versions, audit Events, scoped object-storage access, and secret exclusion.
- [x] No client-calculated value is trusted as authoritative.

### Privacy

- [x] Player-private notes and descriptive fields follow explicit field classifications.
- [x] GM-only data is excluded from Player projections.
- [x] Diagnostics default to exclude and never silently capture Character screens or prose.
- [x] Support access is separate, purpose-bound, time-bounded, attributable, and revocable.

### Cost

- [x] Core creation and advancement require zero AI and zero paid identity, search, analytics, ticketing, or calculation service.
- [x] Storage, history, snapshot, and validation budgets are measured.
- [x] Optional provider or AI costs require separate owner approval.

### Material risks

- [x] Rules ambiguity or incomplete content coverage.
- [x] Hidden-information leakage through options, counts, prerequisites, history, diagnostics, or exports.
- [x] Character corruption through stale writes or migration.
- [x] Duplicate advancement or incorrect budget consumption.
- [x] Entitlement changes making historical Characters appear broken.
- [x] Excessive mobile complexity or inaccessible prerequisite graphs.
- [x] Provider coupling or paid-service creep.

### Stop conditions

- [x] Any unauthorized Character or private-field disclosure.
- [x] Any duplicate accepted activation, award, advancement, correction, or migration effect.
- [x] Any silent last-write-wins or destructive history rewrite.
- [x] Any migration without a verified plan, digest, and retained recovery path.
- [x] Any required paid service or production credential.
- [x] Any claim of implementation, internal-alpha release, production, or public release without owner approval.

## 22. Owner review points

- **Design approval required:** final Character field classes, lifecycle, review policy, advancement ledger, correction model, and alpha fixtures.
- **Scope decision required:** exact bounded rules profile, creation options, advancement options, and appearance fields.
- **Canon decision required:** any proposal to promote Character-created content or corrections into canonical content.
- **Spending or provider decision required:** any hosted identity, storage, search, analytics, support, AI, or calculation service.
- **Alpha release decision required:** separate owner gate after implementation and validation.

Silence is not approval.

## 23. Implementation handoff

**Target repository:** `cybalicistjt-stack/Multiversal-app` after active P9-06 dependencies and owner gates permit  
**Registered work type:** bounded Stage A vertical-slice implementation work order  
**Decision level:** Level 2 for ordinary implementation; Level 3 for schema, authority, migration, or release-impacting changes  
**Risk class:** medium by default; high for authorization, migration, progression integrity, or protected-data changes  
**Suggested work-order title:** Implement MV-IA-F004 Character Creation and Advancement vertical slice  
**Expected branches or files:** application-owned Character domain contracts, services, ports, adapters, projections, routes, components, fixtures, migrations, tests, and documentation  
**Required reviewers:** product, rules, architecture, security/privacy, entitlement, data/migration, UX/accessibility, QA, and documentation  
**Required gates:** P9-06 dependency readiness, IA-D02-006 conformance, schema and migration review, permission review, deterministic validation, CI, two-subject E2E, recovery tests, and owner review before alpha-ready status  
**Rollback or recovery:** reversible migrations where defined, verified backup and restore, feature flag or route disablement, retained Event history, and provider-neutral export  
**Evidence outputs:** test results, acceptance matrix, projection snapshots, calculation traces, Event and ledger evidence, migration receipt, accessibility report, diagnostic manifest, cost review, and implementation handoff receipt

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

**Final design status:** implementation-ready design; application implementation remains dependency-gated  
**Reviewer:** repository validation and pull-request review required  
**Date:** 2026-08-05  
**Packet digest:** calculated by repository tooling when implemented
