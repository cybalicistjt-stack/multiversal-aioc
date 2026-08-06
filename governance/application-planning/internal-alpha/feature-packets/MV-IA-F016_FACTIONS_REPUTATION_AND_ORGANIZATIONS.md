# MV-IA-F016 — Factions, Reputation, and Organizations

**Feature ID:** MV-IA-F016  
**Feature version:** 0.1.0  
**Classification:** alpha-required  
**Design status:** implementation-ready  
**Owner:** John Brandon Turner  
**Primary roles:** Game Master, Player, Assistant GM, Observer, Content Creator  
**Stage A mapping:** A9/A10  
**Historical module mapping:** Factions, Reputation & Organizations  
**Prepared by:** OpenAI design agent under owner authority  
**Reviewed by:** deterministic package validation and final hosted gate  
**Date:** 2026-08-06

## 1. Problem and user outcome

### Problem

Factions can become unsafe or inconsistent when membership is inferred from a title, reputation is merged with personal relationships, rank silently grants permissions, or one universal standing scale is imposed on every organization. Multiversal requires persistent Campaign factions with explicit membership, standing, influence, assets, territory, agendas, operations, alert state, and role-safe history.

### Required outcome

An authorized GM can place a governed Faction Definition into a Campaign, manage explicit memberships and offices, record scoped standing and influence through attributable Events and plausible information paths, relate factions through the shared Relationship Tracker, bind existing Assets, Resources, Locations, Projects, and Contracts without duplicating ownership, and expose different public/hidden projections to Players and staff.

### Why this belongs in internal alpha

Factions are a core social and worldbuilding dependency for Social Interaction Mode, investigation, adventure flow, World Builder, reputation, contracts, Projects, and optional AI retrieval. The alpha needs one persistent faction path that changes through play and remains permission-safe.

## 2. Alpha slice

### Included

- Reusable `mv.object.faction-definition` refinement and Campaign-scoped `mv.object.faction` live state.
- Explicit first-class membership, office/rank assignment, standing, influence, alert, agenda, operation, and faction-service records.
- Profile-defined standing and influence scales; no universal scale.
- Faction-to-faction and faction-to-person relationship context through MV-IA-F009 directional edges.
- Public and hidden goals, agendas, leaders, members, Assets, Resources, territory, locations, allies/enemies, operations, and alert state.
- Event-backed standing and influence changes with plausible information-path evidence.
- Seven converted source faction profiles and their governed progression references.
- One Campaign path that changes standing, unlocks a bounded benefit or consequence, and survives save/reload/reconnect.
- Desktop, tablet, mobile, keyboard, screen-reader, graph/list, history, and nonvisual parity.

### Explicitly excluded

- General faction/Location authoring UI owned by MV-IA-F015.
- Personal relationship mechanics owned by MV-IA-F009.
- Structured social action resolution owned by MV-IA-F010.
- Inventory ownership/equipment implementation owned by MV-IA-F008.
- Full progression conversion or balance redesign of the 956 canonical faction/prestige records.
- Application implementation, provider activation, deployment, or release.

### Full long-term scope deferred

Large geopolitical simulation, autonomous faction turns, procedural faction generation, global economy, broad cross-Campaign federation, and AI-directed strategy remain deferred. Permanent political, economic, environmental, divine, or market changes remain Project-governed rather than instant faction commands.

## 3. Roles and authority

| Role | Allowed actions | Hidden information | Approval required |
|---|---|---|---|
| Player | Read authorized faction, membership, standing, influence, service, and history projections; use governed social Actions | Cannot read hidden factions, secret membership, covert leaders, operations, agendas, resources, exact standing, or GM-only causes unless revealed | Mutating outcomes flow through authoritative domain commands or shared proposal/approval |
| Game Master | Place and configure Campaign factions; manage membership, offices, standing, influence, alert, agendas, operations, and visibility | May read authorized Campaign truth | Destructive, cross-domain, Project, Asset, release, and canonical actions retain their own authority |
| Owner/Admin | Governance and explicit support actions | Account role alone does not grant Campaign-hidden or Player-private faction data | Existing security, support, canon, spend, and release gates apply |
| Content Creator | Define reusable faction, role, office, rank, standing/influence profile, service, and progression references | Cannot mutate live Campaign state or promote content silently | Canonical promotion remains owner-gated |
| Assistant GM/Observer | Assistant GM acts within active delegation; Observer reads observer-safe projection | Delegation and audience filtering apply before serialization | Mutation requires current delegated authority |
| Service actor or AI | Validate, project, index, summarize, or propose only within typed service authority | No bypass of object, field, graph, search, export, realtime, or AI filters | AI has no faction, membership, standing, influence, operation, lore, or canonical authority |

Membership, rank, office, reputation, influence, ownership, equipment, and permission are separate. Silence is not approval.

## 4. Dependencies

### Feature dependencies

- MV-IA-F009 — Relationship Tracker.
- MV-IA-F015 — World and Setting Builder, for reusable Faction Definition authoring and Location/territory authoring.
- MV-IA-F020 — Permissions and Hidden Information.
- MV-IA-F002 — Universal Object Experience.
- MV-IA-F003 — Identity, Dashboard, and Workspace Selection.
- MV-IA-F005 — Campaign, Scene, and Session Builder.
- MV-IA-F021 — Autosave, Reconnect, Recovery, and Bounded Offline Use.
- MV-IA-F025 — Onboarding, Help, Diagnostics, and Issue Reporting.
- IA-D04-002 — Proposal and Approval Shared Component for Player-proposed faction consequences.

### Shared systems

- SS-02 Universal Object Browser/Inspector/Picker.
- SS-03 stable references and provenance.
- SS-06 proposal and approval.
- SS-07 permission-safe search and selection.
- SS-08 persistence, Events, and history.
- SS-12 adaptive interface.
- SS-13 accessibility.
- SS-14 diagnostics and issue reporting.
- SS-19 reconnect and recovery.

### Service ports and adapters

- persistence, migration, identity, authorization, entitlement, Event, projection, relationship, Asset/Resource, Location, Project, Contract, search, export, realtime, and diagnostics ports;
- provider-neutral faction graph/list projection adapter.

### Canonical objects and packs

- `mv.object.faction-definition`;
- `mv.object.faction`;
- `mv.object.reputation-record`;
- `mv.object.reputation-scale-definition`;
- F009 relationship edges;
- membership, office/rank, influence, alert, agenda, operation, service/access, Project, Contract, Asset, Resource, and Location references.

### Schemas and migrations

Existing Faction Definition, Reputation Record, and Reputation Scale Definition are catalog shells requiring strict detailed refinement. The existing Faction live schema is specialized but stores member NPC IDs directly; implementation must introduce explicit membership records without deleting or guessing legacy membership. Existing arrays become compatibility indexes/projections, not sole authority.

### Decisions and gates

Design may complete while F015 and P9 dependencies remain unfinished. Application implementation remains dependency-gated, including the preserved `P9-06-008-attempt-002`. No paid service, credential, deployment, release, or canonical promotion is authorized.

## 5. Object and state model

### Reusable Definitions

- Faction Definition and exact version;
- membership policy and allowed subject types;
- rank and office definitions;
- standing/reputation scale definitions;
- influence scale definitions;
- reaction profiles and consequence mappings;
- service/access definitions;
- alert profiles;
- agenda and operation type definitions;
- progression-track references;
- visibility defaults and provenance.

### Campaign placements or bindings

- Faction placement/live instance bound to Campaign and exact definition version;
- public/hidden identity and alias bindings;
- Location and territory references;
- Relationship Edge references for allies/enemies;
- Asset, Resource, Project, Contract, and service references;
- Campaign-specific standing, influence, membership, office, agenda, operation, and alert records.

### Live instances and state

A Faction live instance includes faction ID, Campaign ID, definition/version, lifecycle status, public identity state, membership record IDs, office assignment IDs, relationship edge IDs, standing record IDs, influence record IDs, Asset/Resource references, territory/Location references, agenda/operation IDs, alert state ID, Project/Contract IDs, visibility profile, history Event IDs, provenance, aggregate version, and correlation ID.

Membership records include membership ID, faction ID, subject reference, status, rank reference, office references, joined/left Event IDs, obligations, granted service/access references, visibility, permission scope, provenance, and aggregate version. Initial statuses are invited, applicant, probationary, active, suspended, resigned, expelled, former, and honorary. Secret membership is a visibility decision, not a membership status.

Standing records include subject, faction/audience scope, scale definition/version, exact value or profile-valid state, current band, source Event, plausible information-path reference, visibility, decay/expiry policy if defined, history, and version.

Influence records remain separate from standing. They identify holder, target faction/scope, scale/profile, current value/band, spend/use policy, visibility, source Events, expiry/decay, and version.

Alert state remains temporary and scoped; it is not standing or a personal relationship. Agendas and operations identify public/hidden objectives, status, scope, responsible actors, related Projects/Contracts, visibility, and Event history.

### Events and history

Owned Events include `FactionPlaced`, `FactionStatusChanged`, `FactionMembershipInvited`, `FactionMembershipChanged`, `FactionOfficeAssigned`, `FactionOfficeVacated`, `FactionStandingChanged`, `FactionInfluenceChanged`, `FactionAlertChanged`, `FactionAgendaChanged`, `FactionOperationChanged`, `FactionServiceAccessChanged`, `FactionAssetOrResourceBound`, and `FactionContractOrProjectLinked`. Relationship changes reuse F009 `RelationshipChanged`; Project, Contract, Asset, and Resource domains retain their own Events.

### Projections and indexes

- GM faction workspace and graph/list;
- Player faction directory and faction detail;
- membership and office roster;
- standing/influence summary and history;
- agenda/operation/alert inspector;
- Asset/Resource/territory/service reference panels;
- relationship graph through F009;
- role-safe search, counts, exports, diagnostics, notifications, realtime, and AI context.

### Stable IDs

Do not create faction IDs from occupations, titles, species, role tags, display labels, or implied organizations. Cross-Campaign membership, standing, or resource binding is denied without an explicit shared-scope contract.

### Provenance

The reviewed NPC faction register has 153 rows: 152 `not-provided`, one role-implied civic label, and zero stable faction references. Every row repeats the policy not to create faction IDs from occupations, titles, species, or implied organizations. Seven converted source faction profiles and the 956-record progression corpus are valid governed source references, not permission or membership grants.

## 6. Primary user flow

1. The GM selects an installed Faction Definition through F002 and places it in a Campaign.
2. The server validates definition/version, Campaign authority, uniqueness, visibility, and initial status, then emits `FactionPlaced`.
3. The GM invites or records one explicit member and assigns a rank or office only through separate authorized commands.
4. A governed social outcome proposes or directly authorizes a scoped standing change with source Event and plausible information path.
5. The server validates the faction-specific scale/profile, commits one `FactionStandingChanged` Event, and evaluates profile-defined consequences.
6. The GM reveals only authorized faction layers to selected audiences.
7. Player and GM views refresh from separate server-filtered projections.
8. Reload/reconnect recovers ordered Events and current projections without duplicate standing, service, membership, or influence changes.

## 7. Alternate and secondary flows

### Alternate flow A — faction influence

1. The GM creates or changes a separate influence record.
2. The command names holder, faction/scope, profile, source Event, expected version, and use/spend policy.
3. Consequences occur only through profile/domain rules; influence never silently becomes standing or membership.

### Alternate flow B — faction-to-faction relationship

1. The GM creates a directional F009 relationship edge between two faction instances.
2. Allied, Neutral, or Hostile may be used by a bound reaction profile, not as universal constants.
3. Reciprocal state requires a second explicit edge.

### Alternate flow C — faction service or access

1. A standing band, office, contract, or explicit grant makes one service eligible.
2. The server rechecks current membership, standing, permission, entitlement, resource availability, and obligations.
3. The service/access record is granted or denied with an attributable receipt; it does not grant unrelated ownership or permissions.

### Alternate flow D — large permanent change

1. A proposed political, economic, territorial, environmental, divine, or market change is routed to a Project.
2. The faction may sponsor, oppose, resource, or monitor the Project.
3. Permanent state changes only after the Project’s authoritative completion Event.

## 8. Failure, empty, and recovery states

| State | User sees | Allowed action | Preserved data | Evidence |
|---|---|---|---|---|
| Loading | Safe placeholders without hidden counts | Cancel or use other authorized work | Current projection | correlation ID |
| Empty | No authorized factions; no statement that hidden factions do not exist | Create if authorized, adjust filters | Filter state | projection version |
| Validation error | Field-specific definition, scope, scale, membership, or source error | Correct draft | Safe draft | validation receipt |
| Forbidden | Not-found-or-unavailable response | Return to authorized context | No protected payload | denial code |
| Restricted entitlement | Definition/service unavailable without protected preview | Select permitted content | Draft references | entitlement decision |
| Offline | Cached projection labeled nonauthoritative; local draft only | Inspect cache, edit approved draft | Draft/cache | manifest |
| Stale | Aggregate or dependent record changed | Reload/compare/reapply | Draft plus safe versions | conflict record |
| Conflict | Membership, office, standing, influence, or operation changed elsewhere | Governed resolution | Both safe states | conflict receipt |
| Failed save | Status unknown, not success | Status lookup before retry | Operation ID/draft | command-status receipt |
| Recovery required | Event gap, revocation, pack/schema incompatibility, or dependency mismatch | Guided recovery | Durable server state | recovery receipt |

No cached, pending, stale, or status-unknown faction state is presented as completed.

## 9. Permissions and hidden information

### Authorization questions

- Faction existence, public identity, aliases, membership, leaders/offices, standing/influence, Assets/Resources/territory, goals/agendas, operations, alert, services, and history are independently filterable.
- Secret membership is server-filtered before serialization; roster counts and office vacancies cannot reveal hidden members.
- Hidden factions cannot leak through graph topology, searches, suggestions, counts, URLs, exports, notifications, realtime topics, diagnostics, or AI context.
- Player-specific standing may differ and remains scoped to the active identity/audience/faction.
- Assistant GM actions require active delegation and field-level scope.
- Owner/Admin account status does not automatically reveal Campaign-hidden or Player-private data.
- Revocation clears protected faction, membership, operation, standing, and history projections across every device.

### Required denied-case tests

The matrix covers more than thirty cases: unauthenticated/inactive context, wrong Campaign, hidden faction enumeration, inferred ID from role/title/species, duplicate placement, unknown definition/profile, stale version, unauthorized membership/rank/office, rank-as-permission, progression-as-membership, hidden membership/leader/operation/resource disclosure, cross-Campaign records, relationship/standing merge, influence/standing merge, universal scale, missing information path, eventless change, automatic member attitude, offline mutation, duplicate consequence, unfiltered export, pack rewrite/delete, AI authority, and permanent change without Project.

## 10. Entitlements

- Access sources: installed approved Faction Definitions, Campaign grants, free approved profiles, and explicit entitlements.
- Free-tier behavior: core Campaign faction tracking works without paid providers.
- Campaign grants: permit bounded use in that Campaign without broad source-library exposure.
- Sponsored access: uses existing entitlement evaluator; no faction-specific bypass.
- Expiry behavior: new use may be restricted while authorized historical Campaign state remains readable through snapshots/policy.
- Historical-state behavior: exact definition, standing scale, progression, Project, Contract, Asset, and source versions remain bound.
- Search and preview restrictions: unavailable or hidden faction definitions/instances are not enumerated.
- Offline snapshot behavior: bounded authorized reads/drafts only; no authoritative membership, standing, influence, service, alert, agenda, or operation mutation.

## 11. Persistence and history

- Draft storage: approved editor drafts autosave locally as nonauthoritative.
- Authoritative save: online server commands only.
- Aggregate boundary: faction live instance plus separate versioned membership, office, standing, influence, alert, agenda, operation, and access records.
- Expected-version behavior: stale commands fail closed with safe comparison/recovery.
- Idempotency: prevents duplicate faction placement, membership, office assignment, standing/influence change, service grant, and Event.
- Event types: fourteen owned Events plus delegated F009, Project, Contract, Asset, and Resource Events.
- Snapshot or checkpoint behavior: preserves exact definition/profile versions, hidden state, history sequence, and external refs.
- Audit events: actor, authority, changed paths, prior/final values, source/information path, visibility, timestamp, and correlation.
- Migration behavior: preserve direct member NPC arrays as compatibility indexes until explicit membership records are verified; never synthesize faction IDs.
- Export behavior: same role-safe projection as interactive views.

## 12. Realtime, interruption, and reconnect

- Before submission: preserve draft only.
- After submission before acceptance: use operation identity and status lookup before retry.
- After acceptance before display: reconnect/status lookup returns the single committed result.
- During pending shared approval: no standing/influence/operation consequence becomes authoritative until accepted.
- After missed Events: expose Event gap; recover ordered Events or current snapshot plus sequence anchor.
- With stale client: deny mutation and provide safe compare/reapply.
- From second device: expected versions and idempotency prohibit silent last-write-wins and duplicate consequences.
- After service restart: durable persistence and ordered Event sequence control.
- After revocation: reauthorize before subscriptions and purge protected faction data.

## 13. Interface and information hierarchy

### Desktop

Faction directory/graph, selected faction inspector, public/hidden identity, roster/offices, standing/influence, relationships, Assets/Resources, territory/Locations, agendas/operations/alert, services, Projects/Contracts, history, and reveal controls.

### Tablet

Directory or graph as primary pane with collapsible faction inspector and named sheets for roster, standing, operations, services, and history.

### Mobile

List/tree directory and single-faction detail are complete. Graph is optional. Roster, standing, influence, services, alert, and history use named sections/sheets without losing faction context.

### Player hierarchy

Public identity, authorized relationship/reaction band, personal standing, accessible services, visible leaders/membership, and important history are foregrounded. Hidden factions, exact values, resources, operations, or causes are not implied.

### GM hierarchy

Definition/version, Campaign status, public/hidden fields, membership and offices, standing/influence profile, relationship edges, Assets/Resources, territory, agendas/operations, alert, services, Projects/Contracts, visibility, version, and save/recovery status are available at decision time.

## 14. Accessibility

- Semantic structure: graph nodes/edges have equivalent list/tree/table rows and headings.
- Keyboard flow: all selection, creation, roster, standing, service, operation, reveal, history, and recovery actions are reachable.
- Focus behavior: drawers/inspectors restore focus to originating faction or record.
- Screen-reader names and states: announce authorized faction identity, status, membership/office, standing band/value, influence, visibility, save, and recovery state.
- Live announcements: accepted/denied change, service change, conflict, Event gap, and revocation.
- Text scaling: no clipped names, bands, roles, actions, or warnings.
- Contrast and noncolor status: faction status, relationship/reaction, standing, alert, hidden/revealed, stale, and conflict use text/icons.
- Reduced motion: graph movement and transitions can be disabled.
- Touch targets: shared minimum target sizes.
- Nondrag alternatives: menus/forms for graph links and ordering.
- Map or graph alternative: complete list/tree/table representation.
- Error identification and recovery: field-specific errors and focusable recovery actions.

## 15. Notifications and queues

| Trigger | Recipient | Message content | Action | Resolution state |
|---|---|---|---|---|
| Membership/office changed | authorized subject and GM, filtered | safe faction, role/status, effective state | Open faction/roster | resolved |
| Standing/influence proposal | authorized decision-maker | shared evidence, scope, profile, proposed consequence | Review through shared component | pending/final |
| Standing/influence committed | affected authorized subject and GM | safe band/value and unlocked/removed consequences | Open standing/history | resolved |
| Alert/operation changed | authorized staff only unless revealed | safe scope/status | Open operation | resolved |
| Stale/conflict | command issuer | current version and safe recovery route | Compare/reapply | recovery required |
| Event gap/reconnect | affected device | sequence/recovery status | Recover | pending/resolved |
| Revocation | affected subject/devices | access changed; protected data removed | Return to authorized context | revoked |

## 16. AI involvement

**AI mode:** read-only or proposed organization only

- Allowed action: summarize visible faction history, suggest organization/filtering, or draft nonauthoritative notes/proposals.
- Allowed sources: current server-generated role projection and explicitly included safe source context.
- Permission and entitlement checks: identical to product retrieval before context construction.
- Provenance: cite source projection/version and distinguish inference.
- Uncertainty: missing faction source facts remain missing; role tags do not become organizations.
- Cost boundary: zero-AI operation is complete; no paid model required.
- Non-AI fallback: every faction, roster, standing, operation, service, graph/list, and history function works without AI.
- Prohibited behavior: create faction IDs/lore, grant membership/rank/office/permission, change standing/influence, reveal secrets, decide operations, complete Projects, or promote canon.

## 17. Telemetry and diagnostics

- Operation IDs: stable command/status identities.
- Correlation IDs: connect draft, validation, Event, projection, notification, and UI result.
- Performance measurements: directory/graph, inspector, roster, standing, history, save, and reconnect latency.
- Error events: safe validation class/code without hidden names or operations.
- Permission denials: surface and decision reference without protected faction details.
- Reconnect events: sequence, gap size, recovery outcome, and projection version.
- Privacy redaction: secret factions/members/leaders/operations/resources/territory, exact standing, and hidden causes excluded by default.
- Issue-report attachment: explicit preview/consent under F025.
- Cost signals: local/server resource use; no paid dependency required.

## 18. Test scenarios

### Unit

- Validate nine membership statuses, office/rank separation, and standing/influence profile kinds.
- Validate consequence mappings without universal reaction or scale constants.

### Contract

- Definition, live faction, membership, standing, influence, alert, agenda, operation, and service schemas remain distinct.
- Existing member NPC arrays are compatibility indexes, not authoritative membership creation.
- Progression does not grant membership, rank, office, ownership, equipment, or unrestricted permission.

### Integration

- F009 relationship edges represent allies/enemies without merging faction standing.
- F015 supplies definitions/Locations without mutating live Campaign state.
- Asset/Resource/Project/Contract domains remain authoritative for their records.

### End-to-end

- Place one faction, invite/activate one member, change standing through an Event, unlock one service, reveal a Player-safe band, reload, and verify role-safe history.
- Link two factions with asymmetric F009 edges and preserve independent standing.
- Route a permanent territorial/economic outcome through a Project.

### Permission and hidden information

- Secret faction, member, leader, office, operation, resource, territory, exact standing, and cause are absent from unauthorized APIs, counts, search, export, diagnostics, notification, realtime, and AI context.
- Different Players receive different standing and reveal projections.

### Entitlement

- Unavailable definition/profile is not enumerated.
- Entitlement expiry restricts new use without rewriting authorized history.

### Persistence and migration

- Legacy member NPC IDs migrate to explicit records only with verified references.
- Pack update/removal does not rewrite/delete live memberships, standing, operations, or history.

### Reconnect and recovery

- Lost response uses status lookup and commits one Event/consequence.
- Duplicate Event creates one history row.
- Revocation clears protected faction data from two devices.

### Accessibility

- Screen reader can inspect faction status, personal standing, membership, offices, visible operations, services, and history.
- Mobile list/tree completes every alpha task without graph use.

### Performance

- Bounded alpha faction directory/graph remains responsive; broad simulation remains deferred.

### Golden or deterministic regression

- 8D-007J applies: twenty-four deterministic fixtures cover identity, membership, standing, influence, relationships, hidden operations, services, Projects, migration, pack lifecycle, and recovery.

## 19. Acceptance criteria

1. **FRO-AC-001:** Reusable Faction Definition and Campaign Faction live state remain separate. **Blocking:** yes.
2. **FRO-AC-002:** Occupations, titles, species, role tags, and implied organizations never create faction IDs automatically. **Blocking:** yes.
3. **FRO-AC-003:** Membership is an explicit first-class record. **Blocking:** yes.
4. **FRO-AC-004:** Secret membership is visibility, not a membership status. **Blocking:** yes.
5. **FRO-AC-005:** Rank, office, membership, ownership, equipment, permission, standing, and influence remain separate. **Blocking:** yes.
6. **FRO-AC-006:** Progression never grants membership, rank, office, ownership, equipment, or unrestricted permissions automatically. **Blocking:** yes.
7. **FRO-AC-007:** Faction standing uses profile-defined scales and bands, not a universal scale. **Blocking:** yes.
8. **FRO-AC-008:** Allied/Neutral/Hostile is a bindable default reaction profile, not a global constant. **Blocking:** yes.
9. **FRO-AC-009:** The 0–10/11–25/26–50/51+ track remains one draft profile only. **Blocking:** yes.
10. **FRO-AC-010:** Standing and influence are separate versioned records. **Blocking:** yes.
11. **FRO-AC-011:** Personal relationship and faction standing never become automatically identical. **Blocking:** yes.
12. **FRO-AC-012:** Faction-to-faction and faction-to-person relationships reuse F009 directional edges. **Blocking:** yes.
13. **FRO-AC-013:** Standing/influence changes require attributable Events and plausible information paths. **Blocking:** yes.
14. **FRO-AC-014:** Services/access revalidate current standing, membership, permission, entitlement, availability, and obligations. **Blocking:** yes.
15. **FRO-AC-015:** Alert is temporary scoped state, not standing or relationship. **Blocking:** yes.
16. **FRO-AC-016:** Public/hidden agendas and operations are server-filtered before serialization. **Blocking:** yes.
17. **FRO-AC-017:** Hidden faction topology, membership, leaders, operations, resources, territory, and exact standing cannot leak through side channels. **Blocking:** yes.
18. **FRO-AC-018:** Assets, Resources, Locations, Projects, and Contracts remain references to their authoritative domains. **Blocking:** yes.
19. **FRO-AC-019:** Permanent political/economic/environmental/divine/market effects require Projects. **Blocking:** yes.
20. **FRO-AC-020:** Large-scale source progression requires compatible live records, scale, active control, authority, and Campaign permission. **Blocking:** yes.
21. **FRO-AC-021:** Missing faction data remains missing; source role labels are not synthesized into factions. **Blocking:** yes.
22. **FRO-AC-022:** Pack update/removal cannot silently rewrite/delete live faction state or history. **Blocking:** yes.
23. **FRO-AC-023:** Lost responses use status lookup before retry and duplicate Events/consequences are suppressed. **Blocking:** yes.
24. **FRO-AC-024:** Revocation clears protected projections from every device. **Blocking:** yes.
25. **FRO-AC-025:** Mobile provides a complete list/tree path and graph has a nonvisual equivalent. **Blocking:** yes.
26. **FRO-AC-026:** Optional AI has no faction, membership, standing, influence, operation, reveal, or canonical authority. **Blocking:** yes.
27. **FRO-AC-027:** Zero-paid-service and zero-AI core operation is possible. **Blocking:** yes.
28. **FRO-AC-028:** The exact next design item is IA-D05-003 — MV-IA-F010 Social Interaction Mode. **Blocking:** yes.

Evidence is the packet, matrix, source-coverage record, deterministic fixtures, validator, exact final-head hosted CI, and squash merge.

## 20. Fixtures and approved alpha content

- Required identities: seven converted faction profiles plus synthetic noncanonical hidden/permission/migration cases.
- Required Campaign: bounded alpha Campaign with GM, Assistant GM, Observer, and at least two Players.
- Required Characters/NPCs: members, applicant, office holder, former member, hidden member, and nonmember agent.
- Required packs: faction definitions, standing/influence/reaction/alert/service profiles, progression references, exact versions.
- Required objects: faction instances, memberships, office assignments, standing, influence, relationship edges, services, alert, agendas, operations, Assets/Resources/Locations, Projects/Contracts, Events.
- Required hidden information: secret faction, hidden membership/leader/operation/resource/territory, hidden exact standing and cause.
- Required historical state: standing change, membership transition, office change, influence use, alert change, operation progression, Project outcome.
- Required failure fixtures: implied faction label, duplicate placement, stale version, expired delegation, entitlement restriction, missing information path, universal-scale misuse, offline mutation, pack incompatibility, revocation, Event gap.

The 153-row NPC faction register yields zero stable faction references. The seven converted faction profiles are separate governed source content.

## 21. Security, privacy, cost, and risk

### Security

- Default-deny server authorization for faction, membership, standing, graph, search, export, realtime, and AI surfaces.
- Stable IDs, expected versions, idempotency, and Events prevent duplicate/silent mutation.

### Privacy

- Filter before serialization; do not send hidden faction/member/operation/resource IDs and merely hide them in the UI.
- Diagnostics and issue reports exclude protected data unless explicitly previewed and consented.

### Cost

- Core operation uses local/open components and provider-neutral ports.
- No paid graph, simulation, search, AI, or analytics service is required.

### Material risks

- inferred-faction creation from role labels;
- hidden topology/count leakage;
- standing/relationship/influence merge;
- rank/progression accidentally granting authority;
- pack lifecycle rewriting live Campaign state;
- large-scale progression bypassing Project/scale/permission controls;
- broad simulation scope creep.

### Stop conditions

Stop for owner decision if a proposal widens visibility, grants automatic authority, requires paid services, changes canonical content, collects real-user data, or changes release scope.

## 22. Owner review points

- Design approval required: final merge evidence records the implementation-ready design; no additional decision is required for this bounded packet.
- Scope decision required: none within the source-backed alpha slice.
- Canon decision required: new definitions, ranks, offices, scales, progression, or synthetic fixtures remain separate and owner-gated for promotion.
- Spending or provider decision required: none; paid services remain unauthorized.
- Alpha release decision required: yes, later under existing release gates.

Silence is not approval.

## 23. Implementation handoff

**Target repository:** `cybalicistjt-stack/Multiversal-app` after P9 and F015 prerequisites  
**Registered work type:** dependency-gated feature implementation  
**Decision level:** routine within locked contracts; owner gate for scope/canon/spend/release changes  
**Risk class:** high for hidden information, membership authority, and live Campaign state  
**Suggested work-order title:** Implement MV-IA-F016 Factions, Reputation, and Organizations  
**Expected branches or files:** schemas/migrations, domain commands/Events, projections, faction/list/graph/roster/standing UI, tests/fixtures, accessibility, diagnostics  
**Required reviewers:** domain, permission/hidden-information, persistence/recovery, Asset/Resource/Project integration, accessibility  
**Required gates:** P9 dependencies, F015 definition contract, targeted validator, authorization/side-channel tests, migration/pack lifecycle tests, two-device recovery, final CI  
**Rollback or recovery:** reversible migration, preserved Events/snapshots, route/feature disable, no deletion of live history  
**Evidence outputs:** changed-path inventory, schema/contract versions, tests, fixture results, PR, exact final-head CI, squash merge

The implementation remains dependency-gated and does not resume or supersede `P9-06-008-attempt-002`.

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

**Final design status:** implementation-ready; dependency-gated  
**Reviewer:** deterministic package validator and hosted repository gate  
**Date:** 2026-08-06  
**Packet digest:** recorded by source-control merge evidence
