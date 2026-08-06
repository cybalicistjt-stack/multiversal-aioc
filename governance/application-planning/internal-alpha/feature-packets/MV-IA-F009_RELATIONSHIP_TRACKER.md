# MV-IA-F009 — Relationship Tracker

**Feature ID:** MV-IA-F009  
**Feature version:** 0.1.0  
**Classification:** alpha-required  
**Design status:** implementation-ready  
**Owner:** John Brandon Turner  
**Primary roles:** Game Master, Player, Assistant GM, Observer  
**Stage A mapping:** A9  
**Historical module mapping:** Relationship Tracker  
**Prepared by:** OpenAI design agent under owner authority  
**Reviewed by:** deterministic package validation and final hosted gate  
**Date:** 2026-08-06

## 1. Problem and user outcome

### Problem

Relationship information is currently easy to reduce to scattered NPC notes, one universal attitude score, or an unsafe graph that leaks hidden counterpart identities. That cannot support Multiversal's directional, historical, permission-scoped social state.

### Required outcome

An authorized GM can create and update a Campaign-scoped directional relationship, use registry-defined dimensions and scale profiles, preserve the attributable Event history, configure Player-specific reveal layers, and inspect the same authorized state through graph, list/tree, inspector, and timeline views. Players see only revealed projections.

### Why this belongs in internal alpha

The Relationship Tracker supplies reusable typed-edge, graph/list, visibility, history, threshold, and accessible nonvisual components required by factions, social interaction, investigation, World Builder, adventure flow, and optional AI retrieval.

## 2. Alpha slice

### Included

- Directional `mv.object.relationship-edge` live state between supported social entities.
- Four explicit endpoint families: Character/Actor, NPC, faction, and organization, with registered extension adapters for other social entities.
- Fourteen source-defined relationship dimensions.
- Profile-defined scales, bands, and thresholds; no universal numeric range.
- Event-backed history and exact source/version provenance.
- Seven independently authorized reveal layers.
- GM graph, list/tree, edge editor, inspector, history, and reveal controls.
- Player revealed projection, mobile list fallback, and accessible nonvisual representation.
- Social Bonds, leverage, favors, promises, debts, oaths, and obligations as relationship context/records.
- Reload, second-device, stale-version, ambiguous-response, Event-gap, and revocation behavior.

### Explicitly excluded

- Detailed faction standing and influence rules, owned by MV-IA-F016.
- Structured social-action resolution, mood, intent, and stance runtime, owned by MV-IA-F010.
- Investigation truth/hypothesis behavior, owned by MV-IA-F011.
- Application implementation, provider activation, paid services, deployment, or release.

### Full long-term scope deferred

Very large graph optimization, advanced layout algorithms, broad cross-Campaign social networks, automatic narrative inference, and generalized relationship analytics remain later work. The graph is an optional visual enhancement on mobile; list/tree parity is required now.

## 3. Roles and authority

| Role | Allowed actions | Hidden information | Approval required |
|---|---|---|---|
| Player | Read revealed edges, bands, counterpart identities, and history; use downstream social Actions | Cannot read unrevealed edges, counterpart identities, exact values, hidden causes, or GM-only history | Relationship consequences proposed through governed downstream Actions require domain/GM authority |
| Game Master | Create/change edges, dimensions, reveal state, Bonds, leverage, and obligations within Campaign authority | May read authorized full Campaign truth | Destructive/cross-domain consequences still require their governing authority |
| Owner/Admin | Governance, schema, and support actions within explicit support authority | Account role does not automatically grant Player-private or Campaign-hidden content | Existing owner/security/release gates apply |
| Content Creator | Define reusable relationship types, dimensions, scale profiles, and bands | Cannot mutate live Campaign state or reveal hidden Campaign facts | Promotion remains owner-gated |
| Assistant GM/Observer | Assistant GM acts only within active delegation; Observer reads observer-safe projections | Delegation and audience filtering apply before serialization | Any mutation requires current delegated authority |
| Service actor or AI | Validate, project, index, or summarize only within typed service authority | No bypass of field visibility, search, export, or AI projection filters | AI has no relationship, reveal, Bond, romance, or canonical mutation authority |

Relationships are directional unless explicitly paired as mutual. Silence is not approval.

## 4. Dependencies

### Feature dependencies

- MV-IA-F002 — Universal Object Experience.
- MV-IA-F003 — Identity, Dashboard, and Workspace Selection.
- MV-IA-F005 — Campaign, Scene, and Session Builder.
- MV-IA-F020 — Permissions and Hidden Information.
- MV-IA-F021 — Autosave, Reconnect, Recovery, and Bounded Offline Use.
- MV-IA-F025 — Onboarding, Help, Diagnostics, and Issue Reporting.
- IA-D04-002 Proposal and Approval Shared Component when downstream Player actions propose relationship consequences.

### Shared systems

- SS-02 Universal Object Browser/Inspector/Picker.
- SS-03 stable references and provenance.
- SS-07 permission-safe search and selection.
- SS-08 persistence, Events, and history.
- SS-11 notifications and status lookup.
- SS-12 responsive/adaptive interface.
- SS-13 accessibility.
- SS-14 diagnostics and issue reporting.
- SS-19 reconnect/recovery.

### Service ports and adapters

- persistence and migration ports;
- identity, authorization, entitlement, visibility/reveal, Event, projection, search, export, realtime, and diagnostics ports;
- provider-neutral graph/list projection adapter.

### Canonical objects and packs

- `mv.object.relationship-edge`;
- `mv.object.relationship-type-definition`;
- `mv.object.visibility-profile`;
- `mv.object.social-leverage-state`;
- separate `mv.object.reputation-record` context owned in detail by F016;
- Character/Actor, NPC, faction, and organization references;
- source pack/version locks and snapshots.

### Schemas and migrations

The existing 8D-003 relationship-edge contract requires one numeric `strength`, while the later source requires multiple profile-scaled dimensions and explicitly rejects a universal attitude score. `strength` is therefore legacy/optional summary data, not sole authority. A compatible extension must preserve existing values without guessing their dimension. Ambiguous legacy values enter a governed migration disposition.

### Decisions and gates

Design work may proceed. Application implementation remains dependency-gated by P9-06, including the unfinished `P9-06-008-attempt-002`. Paid-service, credential, deployment, canonical-promotion, and release gates remain unchanged.

## 5. Object and state model

### Reusable Definitions

- relationship-type definition and version;
- relationship-dimension definition;
- relationship-scale profile supporting numeric, ordered-enum, band-only, or validated custom scalar values;
- profile-defined bands and thresholds;
- social Bond profile;
- leverage and obligation type definitions;
- visibility profile and reveal-field definitions.

### Campaign placements or bindings

- Campaign binding for definitions and exact pack versions;
- optional explicit mutual-pair binding between two directional edges;
- audience-specific reveal bindings;
- Scene/NPC Tracker shortcuts that reference, rather than duplicate, relationship state.

### Live instances and state

A relationship edge includes stable edge ID, Campaign ID, directional source/target references, relationship type/version, dimension states, optional mutual-pair ID, visibility profile, audience reveal states, history Event IDs, provenance, lifecycle status, aggregate version, and correlation ID.

Each dimension state includes definition/version, scale profile/version, current value, optional current band, visibility class, last Event ID, and aggregate version. The fourteen initial dimensions are trust, respect, affection, attraction, loyalty, fear, suspicion, hostility, admiration, dependence, obligation, rivalry, familiarity, and ideological alignment.

Relationship, reputation/standing, public status, mood, current intent, and interaction stance remain separate aggregates. Temporary mood or stance never silently becomes a permanent relationship change.

### Events and history

Source-defined Events are `RelationshipCreated`, `RelationshipChanged`, `BondCreated`, `BondXPAwarded`, `LeverageCreated`, `LeverageConsumed`, `FavorCreated`, `FavorSpent`, `PromiseCreated`, `PromiseFulfilled`, and `PromiseBroken`. Relationship-field reveals reuse the shared F020 reveal/audit Event rather than inventing private reveal history.

### Projections and indexes

- authorized GM relationship graph and list/tree;
- Player-specific revealed graph/list projection;
- edge inspector and history timeline;
- NPC Tracker relationship summary;
- Campaign/Scene relationship context;
- role-safe search, counts, exports, diagnostics, notifications, and realtime topics.

### Stable IDs

Display names never replace edge, endpoint, definition, profile, Event, operation, or audience IDs. Cross-Campaign endpoints are rejected unless a governed shared-scope contract explicitly permits them.

### Provenance

The reviewed relationship register has 154 NPC rows: four source-explicit relationship facts and 150 rows where no relationship was provided. Absence is preserved and is not synthesized. The 153-row visibility map supplies staged-reveal evidence. The 209-row social-mechanic register is provenance/context only and creates no executable mechanics automatically.

## 6. Primary user flow

1. The GM enters the Campaign Relationship Workspace and selects source and target entities through F002.
2. The GM chooses a relationship type and creates one directional edge using an idempotent command and expected Campaign/aggregate versions.
3. The GM selects a registered dimension and scale profile, changes its value or band, and supplies or selects the source/reason.
4. The server authorizes endpoints and fields, validates the profile/scale, commits the change, and appends the attributable Event.
5. The GM sets reveal layers for one or more audiences.
6. The server publishes separately filtered GM and Player projections.
7. The GM verifies the edge in graph, list/tree, inspector, and history views; the Player sees only authorized layers.
8. Reload/reconnect resolves authoritative status and ordered Events without duplicate changes.

## 7. Alternate and secondary flows

### Alternate flow A — explicit mutual relationship

1. The GM requests two directional edges and names both expected versions.
2. The server validates each edge independently and links them with a mutual-pair ID.
3. Future changes remain independent unless a command explicitly addresses both edges.

### Alternate flow B — social Bond

1. The GM selects a Bond profile and endpoints.
2. The system validates Campaign norms and any required human agreement receipts.
3. Bond XP changes append ledger entries and apply benefits only at configured profile thresholds.
4. Romantic, intimate, or emotionally controlling Bonds are denied without the configured participant/GM agreement.

### Alternate flow C — leverage or obligation

1. The GM records structured leverage or a promise/favor/debt/oath/obligation.
2. The record preserves source, scope, visibility, status, and consequences.
3. Concurrent `SpendFavor` attempts use expected version/idempotency so at most one succeeds.

### Alternate flow D — Player reveal

1. The GM reveals only selected layers: edge existence, counterpart, type, approximate band, exact value, history, or hidden cause.
2. The Player projection changes through the shared reveal Event.
3. Other Players retain their previous visibility.

## 8. Failure, empty, and recovery states

| State | User sees | Allowed action | Preserved data | Evidence |
|---|---|---|---|---|
| Loading | Skeleton/list placeholders without hidden counts | Cancel or continue other authorized work | Current projection | correlation ID |
| Empty | No authorized relationships; no claim that hidden edges do not exist | Create if authorized, change filters | Filter state | projection version |
| Validation error | Field-specific type/scale/source explanation | Correct draft | Safe draft | validation receipt |
| Forbidden | Not-found-or-unavailable style response | Return to authorized context | No protected payload | denial code |
| Restricted entitlement | Definition unavailable without leaking protected preview | Choose available definition | Draft references | entitlement decision |
| Offline | Cached data labeled nonauthoritative; local draft only | Inspect authorized cache, edit approved draft | Local draft/cache | manifest |
| Stale | Current version changed | Reload/compare/reapply | Draft and server version | conflict record |
| Conflict | Paired edge, reveal, or obligation changed elsewhere | Governed compare/resolve | Both safe versions | conflict receipt |
| Failed save | Status unknown, not success | Status lookup before retry | Operation ID and draft | command-status receipt |
| Recovery required | Explicit Event gap/revocation/schema or pack incompatibility | Guided reconnect/recovery | Durable server state | recovery receipt |

No pending, stale, cached, or status-unknown state is presented as completed.

## 9. Permissions and hidden information

### Authorization questions

- GM full read/write is limited to current Campaign authority.
- Assistant-GM mutations are limited by active delegation.
- Players receive only server-generated reveal projections.
- Owner/Admin status does not automatically grant Player-private or Campaign-hidden relationship data.
- Content Creators may define reusable types/profiles but cannot mutate live Campaign edges.
- Edge existence, counterpart, type, approximate strength/band, exact value, important history, and hidden causes are seven independently authorized reveal layers.
- Graph topology, node/edge counts, search suggestions, empty states, exports, diagnostics, notifications, realtime topics, and AI retrieval are filtered before serialization.
- Revocation immediately clears protected nodes, edges, inspectors, history, exports, subscriptions, diagnostics, and AI context from every device.

### Required denied-case tests

The matrix defines more than twenty-eight denied cases, including wrong Campaign, hidden endpoint enumeration, unauthorized role/delegation, unknown type/dimension, scale mismatch, universal-scale assumption, stale version, eventless change, automatic reciprocity, hidden counterpart/value/cause disclosure, relationship/reputation merge, hardcoded Bond thresholds, unapproved romantic/coercive Bond, duplicate favor spend, offline authoritative mutation, client authority, history deletion, pack rewrite/delete, and AI mutation/reveal authority.

## 10. Entitlements

- Access sources: installed/approved definitions, Campaign grants, free approved content, and explicit entitlements.
- Free-tier behavior: core local/approved profiles remain usable without paid services.
- Campaign grants: may permit use of definitions in that Campaign without broad library exposure.
- Sponsored access: follows the existing entitlement evaluator; no special relationship bypass.
- Expiry behavior: new use may be restricted, while authorized historical Campaign state remains readable through policy-safe snapshots.
- Historical-state behavior: exact definition/pack versions used by Events remain bound.
- Search and preview restrictions: unavailable definitions and hidden entities are not enumerated.
- Offline snapshot behavior: bounded authorized cache only; no authoritative create/change/reveal/spend operation offline.

## 11. Persistence and history

- Draft storage: local autosave for approved editor drafts, clearly nonauthoritative.
- Authoritative save: online server-authorized commands only.
- Aggregate boundary: directional edge; Bond, leverage, and obligation records retain separate versions and domain effects.
- Expected-version behavior: stale versions fail closed and return a safe comparison/recovery route.
- Idempotency: stable operation keys prevent duplicate edges, Events, XP, leverage consumption, and favor spending.
- Event types: the eleven source-defined Events plus shared reveal/audit Events.
- Snapshot or checkpoint behavior: preserves exact state, Event sequence, definition versions, and reveal state.
- Audit events: actor, authority, changed paths, prior/final values, reason/source, visibility, timestamp, and correlation.
- Migration behavior: preserve legacy `strength`; never guess a dimension; record explicit compatibility state.
- Export behavior: same role-safe projection as the interactive view.

Every meaningful change references a durable Event; current values do not replace history.

## 12. Realtime, interruption, and reconnect

- Before local submission: preserve draft; no authoritative change.
- After submission before acceptance: use operation ID and status lookup before retry.
- After acceptance before display: reconnect/status lookup returns the one committed result.
- During pending downstream approval: relationship state remains unchanged until accepted domain result.
- After missed Events: expose an Event gap and recover ordered Events or current snapshot plus sequence anchor.
- With a stale client: deny mutation and provide safe comparison/reapply.
- From a second device: stable IDs, expected versions, and idempotency prevent duplicate or silent last-write-wins behavior.
- After service restart: authoritative persistence and Event sequence control.
- After revocation: reauthorize before resubscribing and purge protected cache/projection data.

## 13. Interface and information hierarchy

### Desktop

Large graph canvas or list/tree with entity filters, typed edge editor, inspector, history timeline, reveal controls, and Bonds/leverage/obligations panels. Graph and list use the same projection and command contracts.

### Tablet

Graph or list primary pane with collapsible tree/inspector and named sheets for editor, history, and reveal controls.

### Mobile

Single-task list/tree fallback is required. Graph is optional enhancement. Edge detail, edit, history, and reveal actions use named drawers or sheets without losing source/target context.

### Player hierarchy

Known counterpart/type/band and important revealed history are foregrounded. Exact values and causes appear only when specifically revealed. Hidden counts or topology are never implied.

### GM hierarchy

Direction, type, dimensions, scale profile, current bands/values, source/history, audience visibility, stale/version state, and save result are available at decision time. Quick controls cannot bypass validation or history.

## 14. Accessibility

- Semantic structure: graph nodes/edges have equivalent list/table rows and headings.
- Keyboard flow: all select, create, edit, reveal, inspect, filter, and history actions are keyboard reachable.
- Focus behavior: opening/closing inspectors returns focus to the originating edge/entity.
- Screen-reader names and states: announce direction, endpoints as authorized, type, dimension, value/band, visibility, and stale/save state.
- Live announcements: save accepted/denied, reveal changed, conflict, Event gap, and revocation.
- Text scaling: no clipped dimensions, values, or action labels at supported scaling.
- Contrast and noncolor status: direction, hidden/revealed, positive/negative, stale, and conflict use text/icon labels.
- Reduced motion: graph movement and transitions can be disabled.
- Touch targets: meet shared target requirements.
- Nondrag alternatives: menus/forms for creating or linking edges and arranging focus.
- Map or graph alternative: complete list/tree/table representation.
- Error identification and recovery: field-specific messages and focusable recovery actions.

## 15. Notifications and queues

| Trigger | Recipient | Message content | Action | Resolution state |
|---|---|---|---|---|
| Relationship command accepted | authorized GM/Assistant GM | safe endpoints, changed field/dimension, status | Open edge/history | resolved |
| Downstream social proposal may change relationship | authorized decision-maker | shared proposal evidence and proposed consequence | Review through IA-D04-002 | pending/final |
| Reveal changed | affected audience and GM, role-filtered | user-safe newly available relationship context | Open revealed view | resolved |
| Stale/conflict | command issuer | current version and safe recovery route | Compare/reapply | recovery required |
| Event gap or reconnect | affected device | sequence/recovery status without hidden payload | Recover | pending/resolved |
| Revocation | affected subject/devices | access changed; protected content removed | Return to authorized context | revoked |

## 16. AI involvement

**AI mode:** read-only or proposed organization only

- Allowed action: summarize already visible relationship history, suggest filters/layout, or draft a nonauthoritative organizational note.
- Allowed sources: current server-generated role projection and explicitly included safe context.
- Permission and entitlement checks: identical to product retrieval before AI context construction.
- Provenance: summaries identify source projection/version and uncertainty.
- Uncertainty: AI must not infer hidden relationships or treat missing source facts as evidence.
- Cost boundary: zero-AI operation is complete; no paid model required.
- Non-AI fallback: all graph/list/editor/history/reveal functions work without AI.
- Prohibited behavior: reveal hidden edges/causes, decide NPC truth, create/change relationships, award Bond XP, spend favors, consume leverage, create romance/coercion, or mutate canonical lore.

## 17. Telemetry and diagnostics

- Operation IDs: stable command and status-lookup IDs.
- Correlation IDs: connect client draft, server validation, Event, projection, and UI result.
- Performance measurements: graph/list load, filter, inspector, history, save, reconnect, and projection latency.
- Error events: validation class and safe code, never unrestricted hidden prose.
- Permission denials: surface and decision reference without protected target details.
- Reconnect events: last acknowledged sequence, gap size, recovery outcome, and projection version.
- Privacy redaction: hidden endpoints, motives, causes, notes, exact values, and Player-private content excluded by default.
- Issue-report attachment: explicit preview/consent under F025.
- Cost signals: local/server resource usage only; no paid dependency required.

## 18. Test scenarios

### Unit

- Validate all fourteen dimensions and multiple scale-profile kinds without universal conversion.
- Validate explicit mutual pairing and independent edge versions.
- Validate Bond agreement gate and profile thresholds.

### Contract

- Existing `strength` value is preserved as legacy/summary and never guessed into a dimension.
- Relationship, reputation, status, mood, intent, and stance schemas remain distinct.
- All seven reveal layers serialize independently.

### Integration

- F002 selection, F020 field filtering, F021 recovery, F025 diagnostics, and shared Event/history paths work together.
- F016 reads relationship context without merging standing.
- F010 consumes relationship/leverage context without direct client mutation.

### End-to-end

- Create a one-way edge, change trust, reveal only a band to one Player, reload, and verify role-safe graph/list/history.
- Create paired mutual edges and change only one direction.
- Create/fulfill/break an obligation with attributable Events.

### Permission and hidden information

- Hidden counterpart is absent from graph API, counts, search, export, diagnostics, notification, and realtime payloads.
- Different Players receive different reveal layers.
- Assistant GM outside delegation is denied.

### Entitlement

- Unavailable definition is not enumerated.
- Pack expiry restricts new use without rewriting authorized history.

### Persistence and migration

- Legacy strength migration preserves value and flags ambiguity.
- Pack update does not rewrite live edge values.
- Pack removal preserves snapshot/history and enters explicit compatibility state.

### Reconnect and recovery

- Lost save response uses status lookup and creates one mutation/Event.
- Duplicate Event delivery creates one history row.
- Revocation clears protected content from two devices.

### Accessibility

- Screen reader can inspect direction, type, dimensions, reveal state, history, and errors in semantic order.
- Mobile list fallback completes every alpha task without graph interaction.

### Performance

- Bounded alpha graph/list remains responsive with fixture-scale data; large-graph optimization remains deferred.

### Golden or deterministic regression

- 8D-007J applies: twenty-four deterministic fixtures cover directionality, mutuality, scale profiles, reveal layering, history, graph/list parity, Bonds, leverage, obligations, migration, pack lifecycle, and recovery.

## 19. Acceptance criteria

1. **REL-AC-001:** Relationship edges are first-class and Campaign-scoped. **Blocking:** yes.
2. **REL-AC-002:** Directionality is default; reciprocal state is never implied. **Blocking:** yes.
3. **REL-AC-003:** Mutuality uses explicit paired edges with independent versions. **Blocking:** yes.
4. **REL-AC-004:** The engine does not use one universal attitude score. **Blocking:** yes.
5. **REL-AC-005:** All fourteen source-defined dimensions are registry-capable. **Blocking:** yes.
6. **REL-AC-006:** Scale and threshold behavior is profile-defined. **Blocking:** yes.
7. **REL-AC-007:** Legacy `strength` values are preserved without guessed migration. **Blocking:** yes.
8. **REL-AC-008:** Every meaningful change references a durable attributable Event. **Blocking:** yes.
9. **REL-AC-009:** History is not deleted when current values change. **Blocking:** yes.
10. **REL-AC-010:** Seven reveal layers are independently authorizable per audience. **Blocking:** yes.
11. **REL-AC-011:** Hidden counterpart identities cannot leak through graph/API side channels. **Blocking:** yes.
12. **REL-AC-012:** Relationship remains separate from reputation, status, mood, intent, and stance. **Blocking:** yes.
13. **REL-AC-013:** Bond thresholds come from profiles. **Blocking:** yes.
14. **REL-AC-014:** Romantic/intimate/coercive Bonds require configured human agreement. **Blocking:** yes.
15. **REL-AC-015:** Leverage preserves source, reliability, scope, visibility, use, and consequences. **Blocking:** yes.
16. **REL-AC-016:** Favors, promises, debts, oaths, and obligations are first-class records. **Blocking:** yes.
17. **REL-AC-017:** Concurrent favor spending yields at most one accepted spend. **Blocking:** yes.
18. **REL-AC-018:** GM graph/list/editor actions share server-authoritative validation. **Blocking:** yes.
19. **REL-AC-019:** Player projections contain only revealed fields. **Blocking:** yes.
20. **REL-AC-020:** Mobile provides a complete list/tree fallback. **Blocking:** yes.
21. **REL-AC-021:** Keyboard and screen-reader users can perform every authorized alpha task. **Blocking:** yes.
22. **REL-AC-022:** Lost responses use status lookup before retry; duplicate Events are suppressed. **Blocking:** yes.
23. **REL-AC-023:** Revocation clears protected projections from every device. **Blocking:** yes.
24. **REL-AC-024:** Pack update/removal cannot silently rewrite/delete live relationship state. **Blocking:** yes.
25. **REL-AC-025:** Missing source facts do not become synthetic relationships. **Blocking:** yes.
26. **REL-AC-026:** Optional AI has no reveal, decision, mutation, romance, or canonical authority. **Blocking:** yes.
27. **REL-AC-027:** Zero-paid-service and zero-AI core operation is possible. **Blocking:** yes.
28. **REL-AC-028:** The exact next design item is IA-D05-002 — MV-IA-F016 Factions, Reputation, and Organizations. **Blocking:** yes.

Evidence is the packet, matrix, provenance snapshot, deterministic fixtures, validator, final-head hosted CI, and squash merge.

## 20. Fixtures and approved alpha content

- Required identities: source-backed NPCs/relationships from the reviewed register plus synthetic noncanonical edge cases.
- Required Campaign: bounded alpha Campaign with GM, Assistant GM, Observer, and at least two Players.
- Required Characters: at least two controlled Characters to prove per-Player reveal differences.
- Required packs: relationship-type, dimension, scale, visibility, and source definition fixtures with exact versions.
- Required objects: directional edges, paired edges, Bond, leverage, favor, promise/obligation, reputation context, Event history.
- Required hidden information: hidden edge, hidden counterpart, hidden exact value, hidden cause, GM-only history.
- Required historical state: prior dimension values, fulfilled/broken promise, spent favor, pack-version snapshot.
- Required failure fixtures: stale version, duplicate operation/Event, wrong Campaign, expired delegation, entitlement restriction, revocation, Event gap, ambiguous legacy strength, unapproved romantic Bond.

The source relationship register contains only four explicit relationship facts; the alpha fixture suite must label all synthetic cases noncanonical.

## 21. Security, privacy, cost, and risk

### Security

- Default-deny server authorization for object, field, graph, query, search, export, realtime, and AI surfaces.
- Stable IDs, expected versions, idempotency, and append-only Events prevent duplicate or silent mutation.

### Privacy

- Filter before serialization; do not send hidden counterpart IDs and hide them in the UI.
- Diagnostics and issue reports exclude protected prose/relationships unless explicitly previewed and consented.

### Cost

- Core operation uses local/open components and existing provider-neutral ports.
- No paid graph, search, AI, or analytics service is required.

### Material risks

- topology/count side-channel leakage;
- legacy single-strength migration ambiguity;
- accidental relationship/reputation/mood merging;
- consent/agency violation through automated Bonds;
- pack lifecycle rewriting live state;
- large-graph usability and performance.

### Stop conditions

Stop for owner decision if a proposal would widen visibility, authorize romance/coercion automation, require paid services, alter canonical content, collect real-user data, or change release scope.

## 22. Owner review points

- Design approval required: final merge evidence records the implementation-ready design; no additional decision is required for the current bounded packet.
- Scope decision required: none within the source-backed alpha slice.
- Canon decision required: any promotion of new definitions or synthetic fixtures remains separate and owner-gated.
- Spending or provider decision required: none; paid services remain unauthorized.
- Alpha release decision required: yes, later under existing release gates.

Silence is not approval.

## 23. Implementation handoff

**Target repository:** `cybalicistjt-stack/Multiversal-app` after P9 prerequisites  
**Registered work type:** dependency-gated feature implementation  
**Decision level:** routine implementation within locked contracts; owner gate for scope/canon/spend/release changes  
**Risk class:** high for hidden information and live Campaign state  
**Suggested work-order title:** Implement MV-IA-F009 Relationship Tracker  
**Expected branches or files:** typed schemas/migrations, domain service/commands/Events, projections, graph/list/editor UI, tests/fixtures, accessibility, diagnostics  
**Required reviewers:** domain, permission/hidden-information, persistence/recovery, accessibility  
**Required gates:** P9 dependencies, deterministic validator, authorization/side-channel tests, migration/pack lifecycle tests, two-device recovery, final CI  
**Rollback or recovery:** reversible migration, preserved Events/snapshots, feature flag or route disable, no deletion of live history  
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
