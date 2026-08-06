# MV-IA-F012 — Encounter Builder and Balance Lab

**Feature ID:** MV-IA-F012  
**Feature version:** 0.1.0  
**Classification:** alpha-required  
**Design status:** implementation-ready  
**Owner:** John Brandon Turner  
**Primary roles:** Game Master, delegated Assistant GM, Player preview, observer preview, Owner/Admin, service actor  
**Stage A mapping:** A5/A7  
**Historical module mapping:** Encounter Builder & Balance Lab  
**Prepared by:** Lead Documentation Architect / Encounter and Balance Systems Steward  
**Date:** 2026-08-05

## 1. Problem and user outcome

### Problem

Encounter preparation combines Characters, creatures, NPCs, hazards, environments, objectives, hidden information, timing, Resources, source variants, Campaign-local overrides, and GM intent. A single difficulty number cannot safely represent that combination. Missing or contradictory legacy data, incompatible rules profiles, mixed scales, and unusual objectives make guaranteed-balance claims especially misleading.

### Required outcome

An authorized GM can assemble a bounded Encounter draft from governed stable-ID content, validate dependencies and compatibility, inspect source-grounded warnings, compare explicit alternatives, and optionally run deterministic bounded simulation. Every result exposes assumptions, evidence quality, uncertainty, omitted variables, and versions. The tool never certifies that an encounter is balanced, fair, safe, winnable, optimal, or guaranteed.

### Why this belongs in internal alpha

F012 is alpha-required because the GM needs a reliable preparation and analysis handoff before MV-IA-F006 and MV-IA-F007 can provide the first playable action loop and full combat interface. It consumes IA-D02-006, MV-IA-F004, and MV-IA-F005 rather than redefining their authority, Character, Campaign, Scene, Session, recovery, or accessibility contracts.

## 2. Alpha slice

### Included

- Create, save, reopen, duplicate, archive, restore, validate, analyze, compare, approve, and attach one Encounter draft.
- Bind it to exact Campaign, Scene, rules-profile, schema, pack-lock, Character-roster, and analysis-policy versions.
- Select participants, hazards, environments, objectives, reinforcements, rewards, and support elements by stable ID.
- Preserve source Definitions separately from Encounter-local placements and overrides.
- Report twelve independent pressure dimensions, evidence quality, uncertainty, warnings, and omitted variables.
- Run deterministic scripted, bounded seeded, sensitivity, and regression-replay simulations.
- Generate GM, Assistant-GM, Player-safe, and observer-safe projections.
- Attach one approved immutable Encounter snapshot to a mutable Scene launch draft.
- Support persistence, reconnect, revocation, bounded offline use, export, migration, diagnostics, accessibility, and zero-service operation.

### Explicitly excluded

- Guaranteed difficulty, fairness, safety, victory, survival, resource expenditure, duration, or optimality claims.
- Automatic AI mutation, approval, optimization, or Scene attachment.
- Full combat execution, initiative, targeting, movement, damage, Conditions, or Action approval.
- Full tactical map authoring, line-of-sight, dynamic lighting, pathfinding, or vehicle-scale analysis.
- Paid simulation services, remote compute farms, production credentials, real-user data collection, internal-alpha release, production deployment, or public release.
- Offline authoritative save, validation, analysis, approval, or attachment.
- Canonical correction of incomplete or contradictory source content.

### Full long-term scope deferred

Richer tactical geometry, campaign attrition, social or investigation pressure, vehicle-scale models, templates, batch comparison, and optional governed AI proposals remain later work. They must retain source provenance, permission-safe projection, reproducibility, uncertainty, and human approval.

## 3. Roles and authority

| Role | Allowed actions | Hidden information | Approval required |
|---|---|---|---|
| Game Master | Compose, validate, analyze, compare, approve, attach, archive, restore, and export | May see authorized GM-private content | Human approval required for snapshot approval and Scene attachment |
| Assistant GM | Delegated composition and analysis within scope and expiry | Only delegation-authorized GM fields | Cannot approve beyond delegation or alter delegation |
| Player | View an explicitly permitted Player-safe preview | Hidden participants, counts, waves, tactics, secret objectives, notes, and internal warnings excluded | No preparation authority |
| Observer | View an explicitly granted observer projection | Player-private and GM-private state excluded | No preparation authority |
| Owner/Admin | Govern policy, recovery, and owner-reserved decisions | Administration is not automatic content access | Owner gates remain explicit |
| Service actor or AI | Service actor validates and projects; optional AI explains or proposes from the narrower authorized projection | No independent authority or broader retrieval | AI cannot mutate, approve, attach, or guarantee outcomes |

The server reauthorizes every authoritative command. Selected context, cached roles, client estimates, and prior projections are never authority.

## 4. Dependencies

### Feature dependencies

- IA-D02-006 shared-foundation contracts SFI-C001 through SFI-C024.
- MV-IA-F002, F003, F004, F005, F019, F020, F021, F024, and F025.

### Shared systems

Stable identity, authorization, field-safe projections, governed object selection, Character control, Campaign policy, Scene placements, launch snapshots, Events, recovery, diagnostics, accessibility, and provider-neutral operation.

### Service ports and adapters

EncounterRepositoryPort, EncounterAnalysisPort, DeterministicSimulationPort, CharacterProjectionPort, CampaignRepositoryPort, SceneRepositoryPort, ObjectSelectionPort, AuthorizationAndProjectionPort, EntitlementEvaluationPort, PackRegistryAndLockPort, ValidationAndCompatibilityPort, EventStoreAndProjectionPort, BackupRestoreExportPort, ClockPort, and IdGeneratorPort.

### Canonical objects and packs

Characters, creatures, NPCs, Actions, Abilities, Effects, Conditions, Resources, hazards, environments, objectives, items, vehicles, rules profiles, source variants, and pack manifests remain immutable governed Definitions or authoritative projections.

### Schemas and migrations

Encounter, placement, validation, analysis, simulation, comparison, approval, attachment, Event, projection, export, and migration schemas must be versioned and checksum-bound.

### Decisions and gates

Application implementation remains dependency-gated by the active P9-06 persistence, migration, deterministic seed/reset, compatibility, backup, restore, export, authorization, Event, and observability work. Design completion does not authorize code or service activation.

## 5. Object and state model

### Reusable Definitions

Source content remains immutable and versioned. Analysis cannot rewrite missing fields, reconcile variants, or promote Encounter-local normalization into canon.

### Campaign placements or bindings

Each EncounterPlacement has its own placementId, source stable ID and version, source pack and version, role, quantity, wave, visibility, starting-state assumptions, optional local override, selection receipt, and field-level analysis provenance.

### Live instances and state

EncounterDraft is a Campaign-local preparation aggregate. It is distinct from a Scene launch snapshot and any live Session or combat instance.

### Events and history

Accepted Events include EncounterCreated, PlacementAdded, PlacementUpdated, EncounterValidated, AnalysisRequested, AnalysisCompleted, ScenarioCompared, EncounterApproved, SceneAttachmentCreated, EncounterArchived, MigrationApplied, and RecoveryCompleted.

### Projections and indexes

GM, delegated Assistant-GM, Player, observer, export, diagnostic, Scene-attachment, and optional-AI projections are generated server-side and permission-filtered before counts, facets, relationships, warnings, or serialization.

### Stable IDs

Encounter, placement, source, Character snapshot, analysis snapshot, simulation receipt, comparison, approval, attachment, operation, Event, schema, rules, pack, and policy identities are stable and independent of display names or provider IDs.

### Provenance

Every normalized input and pressure result records the exact source fields, source versions, local overrides, unavailable fields, variants, contradictions, assumptions, analysis policy, and checksum used.

## 6. Primary user flow

1. Enter an authorized Campaign and mutable Scene draft.
2. Create an Encounter draft bound to current rules, schemas, packs, roster, and analysis policy.
3. Add governed participants, hazards, environment, objectives, reinforcements, rewards, and failure paths.
4. Inspect source rules and provenance before accepting each selection.
5. Save with expectedVersion and idempotencyKey.
6. Resolve blocking dependency, permission, entitlement, pack, scale, compatibility, and integrity findings.
7. Request advisory analysis.
8. Review twelve pressure dimensions, evidence quality, assumptions, omitted variables, uncertainty, and source-grounded warnings.
9. Compare explicit alternatives and optionally run deterministic bounded simulation.
10. Preview authorized projections.
11. Approve an immutable Encounter snapshot through a human GM action.
12. Attach the approved snapshot to the Scene launch draft.
13. Revalidate dependencies at launch without silently changing the approved snapshot.

## 7. Alternate and secondary flows

### Objective-first composition

The GM may begin with survival, escape, protection, delay, capture, retrieval, negotiation, investigation, or a mixed objective before selecting opposition. Exit and partial-success paths remain first-class inputs.

### Reinforcement and wave composition

Participants may arrive in recorded waves with explicit triggers, visibility, assumptions, and provenance. Broken triggers block approval; hidden triggers never appear in Player-safe projections.

### Scenario comparison

Two or more immutable analysis snapshots may be compared only through an explicit delta set, such as roster, quantity, environment, objective, rest assumption, wave timing, or local override. Incompatible rules, schemas, packs, scales, or analysis policies are blocked or clearly separated.

### Incomplete-source analysis

Incomplete or contradictory content may remain in a draft, but confidence is reduced, unknowns remain unknown, and blocking dependencies still prevent approval or attachment.

## 8. Failure, empty, and recovery states

| State | User sees | Allowed action | Preserved data | Evidence |
|---|---|---|---|---|
| Loading | Current operation and nonauthoritative progress | Cancel safely or continue waiting | Draft and last authoritative projection | operation and correlation IDs |
| Empty | No composition and no pressure claim | Add governed content | Campaign, Scene, rules, schema, and pack binding | draft receipt |
| Validation error | Affected stable IDs, source links, and blocking reason | Inspect, replace, remove, or revise | All draft inputs and receipts | validation receipt |
| Forbidden | Safe unavailable response without existence or count leakage | Return to authorized workspace | Local nonprotected edits | denial receipt |
| Restricted entitlement | Safe missing-access reason | Remove selection or use separately approved access | Permitted draft reference | entitlement receipt |
| Offline | Manifest-bound snapshot and local-draft state | Read or edit local unsubmitted draft | Permitted snapshot, local draft, prior analyses | offline manifest |
| Stale | Attempted and current versions | Refresh or reconcile explicitly | Both local and authoritative versions | conflict receipt |
| Failed save | Retry and command-status lookup | Query before retry | Local draft and idempotency key | command receipt |
| Recovery required | Last acknowledged Event and recovery phase | Resume, inspect, or export diagnostics | Accepted Events and snapshots | recovery receipt |
| Analysis unavailable | Exact missing or incompatible inputs | Repair inputs or retain draft | Composition and validation state | refusal receipt |
| Corrupted receipt | Integrity error and blocked approval | Restore verified history or rerun | Prior immutable receipts and Events | checksum evidence |

Unknown values are never silently replaced. Reconnect, conflict, revocation, and restore must not duplicate accepted placements, analyses, approvals, or attachments.

## 9. Permissions and hidden information

Authorization is deny-by-default for reads, writes, search, counts, facets, relationships, comparisons, analysis, simulation, approval, attachment, export, diagnostics, notifications, and AI retrieval.

GM projections may include hidden participants, waves, tactics, objectives, assumptions, and warnings only when authorized. Assistant-GM views are delegation-scoped. Player and observer projections cannot reveal hidden existence, counts, wave timing, trigger details, secret objectives, GM notes, exact internal pressure shapes that disclose hidden content, or ungranted source details.

Required denied-case tests cover unauthenticated access, nonmember enumeration, Player and observer leakage, expired delegation, stale context, unentitled selection, pack mismatch, hidden warning leakage, unauthorized export, diagnostic leakage, revoked subscriptions, offline authority, AI mutation, and corrupted receipts.

## 10. Entitlements

- **Access sources:** free content, owned or subscribed content, sponsored access, Campaign grants, and explicitly approved alpha fixtures.
- **Free-tier behavior:** only permitted content may be discovered, selected, analyzed, previewed, or exported.
- **Campaign grants:** evaluated at each authoritative save, analysis, approval, attachment, and launch revalidation; they do not transfer ownership.
- **Sponsored access:** versioned, attributable, revocable, and not permanent ownership.
- **Expiry behavior:** blocks new protected reads and operations while preserving authorized historical receipts.
- **Historical-state behavior:** expiry never rewrites accepted Events or approved historical snapshots.
- **Search and preview restrictions:** counts, facets, suggestions, IDs, relationships, warnings, and source detail are filtered before serialization.
- **Offline snapshot behavior:** manifests contain only previously authorized fields and must revalidate after expiry or reconnect.

Entitlement failure never substitutes a different object, variant, or synthetic value.

## 11. Persistence and history

- Drafts use expectedVersion and idempotencyKey.
- Submitted commands support status lookup after ambiguous failure.
- Accepted Events are append-only and ordered.
- Analysis, simulation, comparison, approval, and attachment receipts are immutable and checksum-bound.
- Concurrent edits preserve local and authoritative versions for explicit resolution; there is no silent last-write-wins.
- Approval freezes an Encounter snapshot but does not certify balance.
- Scene attachment references the approved snapshot ID and checksum without mutating earlier launch snapshots or live Sessions.
- Backup and restore preserve snapshots, Events, receipts, provenance, visibility, uncertainty, and warning history.
- Migration preserves stable IDs and historical readability, re-evaluates compatibility, and never silently calls a migrated analysis equivalent.
- Authorized export preserves composition, source versions, assumptions, warnings, uncertainty, analyses, simulations, comparisons, approvals, attachments, schemas, rules, and pack locks.

## 12. Realtime, interruption, and reconnect

Realtime delivery is advisory. Ordered accepted Events and the current server projection remain authority.

- Before submission, local edits remain an unsubmitted draft.
- After submission but before acceptance, query command status before retrying.
- After acceptance but before display, reconnect resumes from the last acknowledged Event and suppresses duplicates.
- During analysis, one idempotency key resolves to one accepted receipt or an explicit failed/unknown status.
- During approval or attachment, ambiguous results require status lookup; the client never assumes success.
- Missed Events are fetched in order before the current projection.
- A stale client preserves both versions.
- A second device reauthorizes role, delegation, and draft access.
- Service restart restores from durable Events and snapshots.
- Revocation immediately invalidates protected projections and blocks further authoritative commands.

## 13. Interface and information hierarchy

### Desktop

Composition, Encounter outline, source inspector, validation findings, pressure dimensions, uncertainty, warnings, and comparison may appear side by side. Save, validate, analyze, approve, and attach remain distinct explicit actions.

### Tablet

The same surfaces use ordered split or tabbed layouts with persistent Encounter identity, save state, validation severity, analysis version, and selected placement.

### Mobile

A single-focus sequence uses accessible lists, drawers, or sheets. Mobile retains the same evidence and authority; it is not a shortcut around review.

### Player hierarchy

Only revealed objectives and Scene information are foregrounded. Hidden content is absent from the client projection rather than visually concealed.

### GM hierarchy

Composition state, blocking validation, assumptions, evidence quality, pressure dimensions, uncertainty, warnings, snapshot identity, and attachment status are visible at decision time.

## 14. Accessibility

- Semantic headings, lists, tables, dialogs, and status regions.
- Complete keyboard flow and visible focus.
- Screen-reader names for placements, dimensions, warning severity, confidence, deltas, and save state.
- Live announcements for validation, analysis completion, conflicts, and revocation without hidden leakage.
- High-zoom reflow and text scaling without lost actions.
- No color-only severity, confidence, or comparison encoding.
- Reduced-motion behavior.
- Touch targets and nondrag alternatives.
- Text alternatives for charts, tactical visuals, or graphs.
- Accessible error identification, source links, and recovery actions.

Charts are optional views of accessible underlying tables and are never the only representation.

## 15. Notifications and queues

| Trigger | Recipient | Message content | Action | Resolution state |
|---|---|---|---|---|
| Blocking validation | Requesting GM or delegated Assistant GM | Encounter, safe finding, affected placement, and version | Open finding | unresolved, acknowledged, resolved |
| Analysis completed | Authorized requester | Snapshot ID, confidence class, warning counts, advisory label | Review analysis | reviewed or superseded |
| Approval invalidated | Authorized GM team | Snapshot ID and changed dependency category | Revalidate | repaired, replaced, archived |
| Scene attachment changed | Authorized Scene editors | Encounter and Scene versions | Review attachment | current or stale |
| Delegation revoked | Affected subject | Safe revocation and local-draft guidance | Return to authorized workspace | acknowledged |

Queues deduplicate by material fingerprint and never reveal hidden participants or counts through badges or message text.

## 16. AI involvement

**AI mode:** optional read-only explanation or proposed change; core operation uses zero AI.

- Allowed actions: explain source-linked warnings or propose explicit draft changes for human review.
- Allowed sources: only the initiating subject’s authorized projection and governed source records.
- Permission and entitlement checks: before retrieval and before display or save.
- Provenance: cite inputs, rules, versions, uncertainty, and omitted variables.
- Uncertainty: AI cannot increase evidence confidence or replace unknown source data.
- Cost boundary: no paid model is required.
- Non-AI fallback: every operation has a deterministic first-party path.
- Prohibited behavior: autonomous mutation, approval, attachment, hidden-data expansion, credentials, unbounded simulation, or guaranteed-balance claims.

## 17. Telemetry and diagnostics

Diagnostics include exact release, schema, pack, rules, analysis-policy, fixture, operation, correlation, Encounter, snapshot, and receipt identities. They record performance, validation failures, authorization denials, reconnects, conflicts, simulation bounds, and checksum failures.

Hidden participants, tactics, notes, private Character fields, and raw source payloads are excluded by default. Any diagnostic bundle is allowlisted, redacted, previewed, consented, checksummed, and separately attached. Issue reporting does not grant support access. Telemetry is optional and provider-neutral; core operation does not require external analytics.

## 18. Test scenarios

### Unit

Pressure dimensions preserve independent inputs, normalization, confidence, and omissions. Unknowns stay unknown. Forbidden guarantee language is rejected.

### Contract

Encounter, validation, analysis, simulation, comparison, approval, attachment, Event, export, and migration receipts validate and checksum correctly.

### Integration

Object selection, Character projections, Campaign and Scene binding, pack locks, entitlements, authorization, and persistence agree across ports.

### End-to-end

A GM creates, validates, analyzes, compares, approves, and attaches one bounded Encounter. Reconnect after ambiguous analysis completion yields one accepted receipt.

### Permission and hidden information

Player and observer projections reveal no hidden participants, counts, waves, tactics, objectives, warnings, facets, or diagnostic fields. Delegated Assistant-GM access stops at scope and expiry.

### Entitlement

Free, expired, Campaign-granted, sponsored, and historical access paths preserve correct discovery and history behavior.

### Persistence and migration

Expected-version conflicts preserve both drafts. Migration retains IDs, provenance, uncertainty, warnings, Events, and snapshots without asserting equivalence.

### Reconnect and recovery

Missed Events, service restart, revocation, corrupted receipt, restore, and second-device cases recover without duplicate accepted effects.

### Accessibility

Keyboard, touch, screen reader, zoom, noncolor status, reduced motion, and text alternatives cover every warning and pressure result.

### Performance

Input, placement, scenario, and iteration bounds fail safely and explain the limit.

### Golden or deterministic regression

8D-007J applies to validation, pressure normalization, simulation replay, comparison deltas, hidden-information projection, and warning regressions.

## 19. Acceptance criteria

- **EBL-AC-001 — Blocking:** An authorized GM can create an Encounter draft bound to one Campaign, Scene, rules profile, schema set, pack lock, roster, and analysis-policy version.
- **EBL-AC-002 — Blocking:** Every Character, creature, NPC, hazard, environment, objective, reinforcement, and reward uses governed stable IDs and source/version receipts.
- **EBL-AC-003 — Blocking:** Placements and local overrides never mutate source Definitions, Character records, Scene drafts, launch snapshots, or live Session state.
- **EBL-AC-004 — Blocking:** Every save, validation, analysis, approval, and attachment reauthorizes role, delegation, visibility, entitlement, pack, and versions.
- **EBL-AC-005 — Blocking:** Dependencies, scale, exclusivity, required Actions and Resources, objective references, and integrity validate before attachment.
- **EBL-AC-006 — Blocking:** Pressure estimates expose dimensions, normalized inputs, assumptions, evidence sources, uncertainty, omitted variables, and analysis-policy version.
- **EBL-AC-007 — Blocking:** No output is labeled balanced, fair, safe, winnable, optimal, or guaranteed; only source-grounded warnings and uncertainty-aware ranges are allowed.
- **EBL-AC-008 — Blocking:** Analysis independently represents durability, sustained output, burst, action economy, control, mobility, environment, objectives, information, attrition, reinforcements, and failure paths.
- **EBL-AC-009 — Blocking:** Unknown, incomplete, variant, contradictory, or low-confidence data lowers confidence and warns rather than being silently imputed.
- **EBL-AC-010 — Blocking:** Bounded simulations are deterministic for an exact fixture, seed, policy, and digest, remain advisory, and never mutate authoritative state.
- **EBL-AC-011 — Blocking:** Scenario comparison records explicit deltas and preserves separate immutable snapshots and receipts.
- **EBL-AC-012 — Blocking:** Player and observer projections reveal no hidden participants, counts, waves, tactics, secret objectives, GM notes, or internal warning details.
- **EBL-AC-013 — Blocking:** An approved Encounter snapshot attaches to a Scene draft without altering an existing launch snapshot or active Session.
- **EBL-AC-014 — Blocking:** Concurrency, stale versions, ambiguous failures, reconnects, and revocations preserve local and authoritative state without duplicate accepted effects.
- **EBL-AC-015 — Blocking:** Offline use is limited to manifest-bound reading, local draft edits, and previous analysis snapshots; authoritative operations require reconnection.
- **EBL-AC-016 — Blocking:** Every warning and estimate is keyboard reachable, screen-reader understandable, noncolor encoded, zoom-safe, and equivalent on desktop, tablet, and mobile.
- **EBL-AC-017 — Blocking:** Diagnostics exclude hidden Encounter content and private notes by default and require allowlists, redaction, consent, and separate support access.
- **EBL-AC-018 — Blocking:** Authorized exports preserve identity, source versions, assumptions, warnings, uncertainty, snapshots, receipts, schemas, rules, and pack locks without unauthorized content.
- **EBL-AC-019 — Blocking:** Core composition, validation, comparison, and deterministic bounded simulation work without AI, paid services, production credentials, or external telemetry.
- **EBL-AC-020 — Blocking:** Deterministic fixtures cover valid, invalid, uncertain, hidden-information, reconnect, stale-version, corruption, simulation-replay, and attachment-invalidation cases.

## 20. Fixtures and approved alpha content

Required fixtures:

- EBL-FIX-VALID-MIXED — complete governed mixed encounter.
- EBL-FIX-PACK-INVALID — dependency and pack-lock failure.
- EBL-FIX-UNCERTAIN — partial-source high-uncertainty analysis.
- EBL-FIX-HIDDEN-WAVE — hidden reinforcement and Player preview.
- EBL-FIX-ACTION-ECONOMY — extreme action-economy and control warning.
- EBL-FIX-STALE — stale version and concurrent edits.
- EBL-FIX-RECONNECT — ambiguous failure and reconnect.
- EBL-FIX-CORRUPT — corrupted analysis receipt.
- EBL-FIX-SIM-REPLAY — deterministic simulation replay.
- EBL-FIX-ATTACHMENT-INVALIDATED — Scene attachment invalidated by dependency change.

Each fixture records exact identities, rules, schemas, packs, Characters, source versions, Events, receipts, checksums, expected warnings, and denied projections. Synthetic fixtures are labeled synthetic and never represented as complete game canon.

## 21. Security, privacy, cost, and risk

### Security

Deny-by-default authorization, server projections, integrity-checked receipts, bounded input sizes and simulations, no arbitrary code execution, and fail-closed provider boundaries are mandatory.

### Privacy

Hidden Encounter content, private Character fields, notes, raw sources, diagnostics, exports, notifications, and AI projections are minimized and filtered before serialization.

### Cost

Core composition, validation, analysis, comparison, simulation, export, and recovery require no paid third-party service. No hosted simulator, analytics provider, production database, credential, or paid AI is authorized.

### Material risks

- A single score can create false confidence.
- Incomplete legacy data can distort analysis.
- Counts or warning shapes can leak hidden information.
- Simulation can be mistaken for prediction.
- Cross-profile or cross-scale comparison can be invalid.

### Stop conditions

Stop approval or attachment for authorization failure, missing dependency, incompatible rules/schema/pack/scale, corrupted receipt, stale version, unbounded simulation, hidden-information leakage, unavailable zero-service path, or any claim that certifies actual play outcomes.

## 22. Owner review points

- Design approval required for material scope changes.
- Broader tactical, vehicle, social, investigation, attrition, community, or public-sharing scope requires a later governed decision.
- Encounter-local overrides, synthetic fixtures, normalization, and analysis never promote canon.
- Paid providers, credentials, spending, and production services require explicit owner approval.
- Internal-alpha release remains owner-only.
- Advisory estimates cannot be converted into guaranteed fairness, safety, victory, survival, or optimality without a separately governed evidence standard.

Silence is not approval.

## 23. Implementation handoff

**Target repository:** `cybalicistjt-stack/Multiversal-app` after dependency gates  
**Registered work type:** governed application implementation  
**Decision level:** reversible implementation; owner-only for providers, spending, release, and scope expansion  
**Risk class:** high  
**Suggested work-order title:** Implement MV-IA-F012 Encounter Builder and Balance Lab alpha slice  
**Expected branches or files:** Encounter contracts, schemas, repositories, analysis engine, fixtures, projections, UI, tests, CI, receipts, and documentation  
**Required reviewers:** product, game-system, architecture, canon, security/privacy, accessibility, recovery, QA, and documentation  
**Required gates:** P9-06 dependencies, exact-head tests, permission review, deterministic replay, accessibility verification, and owner release gate  
**Rollback or recovery:** revert implementation PR, restore prior schema/checkpoint, retain immutable history, and disable the feature without data loss  
**Evidence outputs:** commits, PR, CI, fixture checksums, permission denials, recovery results, accessibility evidence, and merge evidence

Implementation slices:

1. Encounter aggregate and repository.
2. Stable-ID composition and placement receipts.
3. Authorization and projection safety.
4. Validation and compatibility.
5. Pressure and uncertainty analysis.
6. Warnings and evidence UI.
7. Deterministic bounded simulation.
8. Scenario comparison and snapshots.
9. Human approval and Scene attachment.
10. Recovery, export, diagnostics, accessibility, and CI.

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
**Reviewer:** governed multi-role design review; owner remains final authority  
**Date:** 2026-08-05  
**Packet digest:** generated and verified through repository CI

Application implementation remains dependency-gated by the active P9-06 sequence. This packet is design-only and does not authorize balance certification, paid simulation, production credentials, real-user data, internal-alpha release, production deployment, or public release.

**Exact next design action:** IA-D03-004 — Define the internal-alpha content and deterministic fixture specification.
