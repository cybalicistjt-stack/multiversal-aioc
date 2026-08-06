# MV-IA-F012 — Encounter Builder and Balance Lab

**Feature ID:** MV-IA-F012  
**Feature version:** 0.1.0  
**Classification:** alpha-required  
**Design status:** implementation-ready  
**Owner:** John Brandon Turner  
**Primary roles:** Game Master, Assistant GM, Player preview, observer preview, Owner/Admin, service actor  
**Stage A mapping:** A5/A7 — Campaign preparation and full combat preparation  
**Historical module mapping:** Encounter Builder & Balance Lab  
**Prepared by:** Lead Documentation Architect / Encounter and Balance Systems Steward  
**Date:** 2026-08-05

## 1. Problem and user outcome

### Problem

Encounter preparation combines game-system content, Character capability, Scene conditions, hidden information, objectives, hazards, timing, and GM intent. A simple numerical “difficulty” value cannot safely represent that combination. Multiversal also supports many rules profiles, source variants, incomplete legacy data, Campaign-local overrides, unusual objectives, and mixed scales. A design that pretends to guarantee balance would mislead the GM and erase the uncertainty that actually matters.

Without one governed Encounter Builder and Balance Lab contract, later combat, action-resolution, map, vehicle, social-conflict, and adventure systems could each invent incompatible participant, pressure, simulation, and warning models. Common failures include:

- treating source Definitions as mutable encounter instances;
- counting enemies while ignoring action economy, control, terrain, objectives, reinforcements, or escape routes;
- silently filling missing source fields with invented values;
- comparing Characters or creatures across incompatible rules profiles, scales, or pack versions;
- leaking hidden participants, counts, tactics, or secret objectives through summaries or warnings;
- labeling an encounter “balanced,” “fair,” “safe,” or “winnable” without evidence;
- running opaque simulations that cannot be reproduced;
- mutating a Scene or live Session from an advisory analysis;
- losing GM edits or duplicating accepted operations after reconnect;
- requiring paid analytics, hosted simulation, AI, or production services for core preparation.

### Required outcome

An authorized GM can assemble a bounded Encounter draft from governed Characters, creatures, NPCs, hazards, environments, objectives, reinforcements, rewards, and Scene conditions. The system validates dependencies and compatibility, calculates transparent pressure dimensions, records assumptions and evidence quality, produces source-grounded warnings, compares explicit alternatives, and optionally runs deterministic bounded simulations.

Every result remains advisory. The tool must preserve uncertainty, show omitted or low-confidence inputs, avoid guaranteed-balance claims, protect hidden information, and attach only an explicitly approved immutable Encounter snapshot to a future Scene launch draft.

### Why this belongs in internal alpha

F012 is alpha-required because a GM needs a reliable way to compose and inspect an encounter before the full combat interface exists. It consumes the completed object, Character, Campaign, Scene, Session, permission, recovery, accessibility, and pack contracts and provides the preparation handoff for MV-IA-F006 and MV-IA-F007.

## 2. Alpha slice

### Included

- Create, save, reopen, duplicate, archive, and restore one Encounter draft within an authorized Campaign and Scene.
- Bind the draft to exact Campaign, Scene, rules-profile, schema, pack-lock, Character-roster, and analysis-policy versions.
- Select governed participants, hazards, environments, objectives, reinforcements, rewards, and support elements by stable ID.
- Create Encounter-local placements, quantities, starting-state assumptions, roles, waves, and analysis-only overrides without mutating source records.
- Validate references, pack and schema compatibility, scale, dependencies, exclusivity, required Actions, Effects, Conditions, Resources, and Character eligibility.
- Calculate transparent advisory pressure dimensions and confidence.
- Produce blocking errors, caution warnings, informational observations, and unresolved-data notices with source links.
- Compare explicit scenarios and preserve immutable analysis snapshots.
- Run bounded deterministic simulations against synthetic or approved fixture inputs.
- Preview GM, Assistant-GM, Player-safe, and observer-safe projections.
- Attach one approved immutable Encounter snapshot to a mutable Scene launch draft.
- Preserve drafts, commands, Events, receipts, analyses, and Scene attachment as separate states.
- Support desktop, tablet, mobile, keyboard, touch, screen reader, high zoom, reduced motion, and noncolor status.
- Provide deterministic fixtures, denied cases, and twenty blocking acceptance criteria.

### Explicitly excluded

- Guaranteed difficulty, fairness, safety, victory, survival, resource expenditure, or session-duration claims.
- Automatic encounter creation, optimization, or mutation by AI.
- Full combat execution, initiative, targeting, movement, damage, Conditions, or GM approvals.
- Full tactical map authoring, line-of-sight, dynamic lighting, or pathfinding.
- General-purpose Monte Carlo infrastructure, remote compute farms, or paid simulation services.
- Automatic canonical corrections to incomplete or contradictory source content.
- Live Session mutation or retroactive replacement of an immutable Scene launch snapshot.
- Public encounter publishing, marketplace features, ratings, or competitive ranking.
- Offline authoritative save, approval, analysis, or attachment.
- Production providers, credentials, real-user data collection, internal-alpha release, production deployment, or public release.

### Long-term scope deferred

Later work may add richer tactical geometry, vehicle-scale models, social or investigation pressure models, campaign attrition forecasting, encounter templates, batch comparison, community calibration, and optional governed AI proposals. These additions must retain transparent inputs, reproducibility, uncertainty, source provenance, permission-safe projection, and human approval.

## 3. Roles and authority

| Role | Allowed actions | Protected boundaries |
|---|---|---|
| Game Master | Create and edit Encounter drafts, run validation and bounded analysis, compare scenarios, approve snapshots, attach to Scene drafts | Cannot bypass pack, entitlement, schema, Character-control, owner, production, or canonical-promotion gates |
| Assistant GM | Perform explicitly delegated composition and analysis within scope and expiry | Cannot infer full GM authority, reveal excluded GM-private fields, approve outside delegation, or change delegation |
| Player | View a Player-safe preview only when the Campaign permits it | Cannot learn hidden participants, counts, waves, tactics, secret objectives, GM notes, or internal warnings |
| Observer | View an observer-safe projection when explicitly granted | No hidden or Player-private state and no analysis authority |
| Owner/Admin | Perform governed policy, recovery, and owner-reserved decisions | Administration is not automatic content access; purpose and scope remain required |
| Service actor | Validate, persist, project, compare, simulate fixtures, export, and recover within a scoped contract | No independent role, intent, approval, or content authority |
| AI assistive actor | Optional read-only explanation or proposal based on the initiating subject’s narrower projection | No mutation, approval, hidden-data expansion, guaranteed-balance claim, or autonomous simulation authority |

The server reauthorizes every authoritative save, analysis request, approval, and Scene attachment. Selected context, cached roles, client-side estimates, and prior previews are never authority.

## 4. Dependencies

### Feature dependencies

- IA-D02-006 shared-foundation contracts SFI-C001 through SFI-C024.
- MV-IA-F002 Universal Object Experience.
- MV-IA-F003 Identity, Dashboard, and Workspace Selection.
- MV-IA-F004 Character Creation and Advancement.
- MV-IA-F005 Campaign, Scene, and Session Builder.
- MV-IA-F019 Content Library and Entitlements.
- MV-IA-F020 Permissions and Hidden Information.
- MV-IA-F021 Autosave, Reconnect, Recovery, and Bounded Offline Use.
- MV-IA-F024 Pack Lifecycle and Canonical Content Registry.
- MV-IA-F025 Onboarding, Help, Diagnostics, and Issue Reporting.

### Provider-neutral ports

EncounterRepositoryPort, EncounterAnalysisPort, DeterministicSimulationPort, CampaignRepositoryPort, SceneRepositoryPort, CharacterProjectionPort, ObjectQueryAndSelectionPort, AuthorizationAndProjectionPort, EntitlementEvaluationPort, PackRegistryAndLockPort, ValidationAndCompatibilityPort, EventStoreAndProjectionPort, BackupRestoreExportPort, ClockPort, and IdGeneratorPort.

### Implementation gates

Application implementation remains blocked by the active P9-06 persistence, migration, deterministic seed/reset, compatibility, backup, restore, export, identity, entitlement, authorization, event, and observability sequence. Design completion does not authorize code or service activation.

## 5. Encounter object and state model

An Encounter Definition is not a source creature, Scene, or live combat. It is a Campaign-local preparation aggregate with:

- encounterId, campaignId, sceneId, version, lifecycle state, and optional template source;
- rulesProfileId and version, schema identities, packLockDigest, and exact pack versions;
- analysisPolicyId and version;
- intended party or Character snapshot references;
- participant, hazard, environment, objective, reinforcement, reward, and support placements;
- starting-state assumptions, quantities, roles, waves, arrival triggers, visibility, and local overrides;
- GM intent, target experience, acceptable failure paths, rest assumptions, and analysis notes;
- validation state, current analysis snapshot, approval state, and Scene attachment reference.

Separate immutable records are required for selection receipts, validation receipts, analysis snapshots, simulation receipts, comparison receipts, approval receipts, and Scene-attachment receipts. A live Session may later instantiate encounter content through the Scene launch snapshot, but F012 never mutates that Session.

## 6. Source definitions, placements, and provenance

Source creatures, NPCs, Characters, Actions, Abilities, Effects, Conditions, Resources, hazards, environments, objectives, items, vehicles, and rules remain immutable versioned Definitions or authoritative Character projections.

Each Encounter placement records:

- placementId distinct from sourceId;
- source stable ID, source version, source pack, and pack version;
- selection receipt and actor;
- quantity, role, wave, initial-state assumption, visibility, and optional local override;
- exact fields used in analysis;
- fields unavailable, contradictory, variant, or excluded;
- provenance for every derived normalized value.

Analysis-only normalization never changes the source. A local override must be visible, attributable, reversible, and excluded from any claim about the source Definition.

## 7. Primary GM flow

1. Enter an authorized Campaign and select a mutable Scene draft.
2. Create an Encounter draft bound to current Campaign, Scene, rules, schema, pack, and analysis-policy versions.
3. Select the intended Character roster or an approved synthetic roster snapshot.
4. Add opposition, hazards, environments, objectives, reinforcements, rewards, and escape or failure paths.
5. Inspect source rules and provenance before accepting each selection.
6. Save with expectedVersion and idempotencyKey.
7. Request validation; resolve blocking reference, permission, entitlement, dependency, scale, and compatibility findings.
8. Request advisory analysis.
9. Review pressure dimensions, evidence quality, assumptions, omitted variables, uncertainty, and warnings.
10. Create explicit alternatives by changing recorded variables.
11. Optionally run bounded deterministic fixture simulations.
12. Preview authorized projections.
13. Approve an immutable Encounter snapshot.
14. Attach the approved snapshot to the mutable Scene launch draft.
15. Revalidate during future Scene launch; do not silently update the approved snapshot.

## 8. Encounter composition model

Composition supports:

- friendly, hostile, neutral, environmental, summoned, allied, and conditional participants;
- single participants, groups, quantities, formations, and reinforcement waves;
- direct defeat, survival, escape, protection, delay, capture, retrieval, negotiation, investigation, and mixed objectives;
- environmental hazards, restricted movement, visibility, cover assumptions, resource drains, time pressure, and information asymmetry;
- alternative success, partial success, surrender, retreat, rescue, or failure paths;
- rewards and post-encounter recovery assumptions.

The model must not reduce every encounter to opposing hit points or damage. Objective structure and exit options are first-class inputs.

## 9. Validation model

Blocking validation covers stable IDs, versions, authorization, entitlements, pack locks, schema compatibility, missing dependencies, unsupported scale, invalid Character lifecycle, absent required Actions or Resources, illegal quantities, mutually exclusive properties, duplicate-exclusive roles, broken wave triggers, impossible objective references, and corrupted receipts.

Warnings cover incomplete data, low-confidence normalization, unusual action economy, extreme control or mobility differences, absent recovery paths, hidden information assumptions, high burst potential, unresolved immunities, unknown environmental interactions, excessive encounter duration assumptions, and fragile single-point objectives.

Validation is deterministic for an exact input digest and policy version.

## 10. Pressure-estimation model

The Balance Lab reports independent pressure dimensions rather than one authoritative difficulty score:

1. durability and recovery pressure;
2. sustained output pressure;
3. burst and spike pressure;
4. action-economy pressure;
5. control and denial pressure;
6. mobility and positional pressure;
7. environment and hazard pressure;
8. objective and time pressure;
9. information and surprise pressure;
10. attrition and resource pressure;
11. reinforcement and escalation pressure;
12. retreat, surrender, rescue, and failure-path availability.

Each dimension includes raw inputs, normalization method, source links, confidence, range, warnings, and omitted variables. An optional composite view may summarize relative pressure only when its weighting policy is shown and individually adjustable; it may not be presented as truth.

## 11. Uncertainty and evidence quality

Every analysis snapshot classifies evidence as complete-source, source-with-variants, partial-source, Campaign-override, synthetic-fixture, inferred-normalization, contradictory, or unavailable.

Confidence is reduced by:

- missing Actions, Effects, Conditions, Resources, defenses, or costs;
- incomplete Character loadouts or temporary state;
- unmodeled player tactics or GM choices;
- unusual objectives or terrain;
- cross-scale interactions;
- unverified source variants;
- unsupported local overrides;
- data that the current rules profile cannot interpret.

Unknown values remain unknown. The tool may show bounded sensitivity ranges, but it must label assumptions and may not silently choose a favorable midpoint.

## 12. Bounded deterministic simulation

The alpha simulation mode is a reproducible scenario exerciser, not a prediction engine.

A simulation receipt records inputDigest, analysisPolicyVersion, fixtureVersion, randomSeed, iterationLimit, stopConditions, abstract decision policy, omitted mechanics, outputs, and checksum. The same inputs produce the same outputs.

Allowed modes are deterministic scripted sequence, bounded seeded sampling, sensitivity sweep, and regression replay. Simulations use synthetic or approved fixture projections, never credentials or live private state. They do not call remote compute, mutate Campaign data, approve an Encounter, or claim actual player behavior.

## 13. Scenario comparison and versioning

A comparison requires two or more immutable analysis snapshots and an explicit delta set, such as participant quantity, roster, environment, objective, rest assumption, wave timing, or local override.

The comparison shows which pressure dimensions and warnings changed, which inputs did not change, whether confidence changed, and whether the snapshots remain compatible. Comparing incompatible rules, schema, pack, or analysis-policy versions is blocked or clearly separated through a migration-aware review.

## 14. Approval and Scene attachment

Encounter approval is a human GM action after current authorization and validation. Approval freezes an Encounter snapshot and its evidence digest; it does not certify balance.

Scene attachment:

- references the approved snapshot by stable ID and checksum;
- records the Scene draft version, actor, and receipt;
- does not mutate an earlier launch snapshot or live Session;
- becomes invalid when required Campaign, pack, schema, Character, or source dependencies change;
- must be revalidated during Scene launch.

A later edit creates a new Encounter draft version and analysis snapshot.

## 15. Permissions and hidden information

GM preparation projections may include hidden participants, tactics, waves, objectives, warnings, and source details only when authorized. Assistant-GM projections are delegation-scoped.

Player-safe and observer-safe views are generated server-side. They cannot reveal:

- hidden participant existence or counts;
- reinforcement timing or trigger details;
- secret objectives or failure conditions;
- GM notes, tactics, or private assumptions;
- exact internal pressure values when their shape would disclose hidden content;
- ungranted source content or provenance.

Counts, facets, autocomplete, comparisons, exports, notifications, diagnostics, and AI projections follow the same non-disclosure rules.

## 16. Persistence, concurrency, and recovery

Encounter drafts use expectedVersion and idempotencyKey. Commands have status lookup for ambiguous failure. Concurrent edits preserve both local and authoritative versions and require explicit resolution.

Accepted Events are append-only and include EncounterCreated, PlacementAdded, PlacementUpdated, EncounterValidated, AnalysisRequested, AnalysisCompleted, WarningAcknowledged, ScenarioCompared, EncounterApproved, SceneAttachmentCreated, EncounterArchived, EncounterRestored, MigrationApplied, and RecoveryCompleted.

Reconnect resumes from the last acknowledged Event sequence and current projection. Revocation immediately removes protected projections and blocks further saves or analysis. Recovery never duplicates accepted operations.

## 17. Offline boundary

Offline capability is limited to:

- viewing a manifest-bound permitted Encounter snapshot;
- viewing previously generated analysis and comparison snapshots;
- editing a local unsubmitted draft;
- preparing local notes that exclude ungranted source payloads.

Authoritative save, validation, analysis, simulation receipt creation, approval, Scene attachment, entitlement checks, and export require reconnection and reauthorization. There is no offline authoritative merge or last-write-wins.

## 18. Responsive and accessible interaction

Desktop may use side-by-side composition, evidence, pressure, warning, and comparison panes. Tablet and mobile use a persistent ordered workflow with preserved selection, filters, warnings, and draft state.

Requirements include:

- complete keyboard operation and visible focus;
- semantic headings, lists, tables, dialogs, and status regions;
- screen-reader names for placements, dimensions, warnings, confidence, and deltas;
- text alternatives for charts and any tactical visual;
- no color-only severity or confidence encoding;
- high-zoom reflow without hidden actions;
- touch targets and non-drag alternatives;
- reduced-motion support;
- equivalent authority and evidence on every form factor.

Charts are optional views of underlying accessible tables, never the only representation.

## 19. Diagnostics, privacy, security, and telemetry

Diagnostics use exact release, schema, pack, rules, analysis-policy, and fixture identities. Hidden participants, tactics, notes, private Character details, and raw source payloads are excluded by default.

Any diagnostic bundle is allowlisted, redacted, previewed, consented, checksummed, and separately attached. Issue reporting does not grant support access.

Security requires deny-by-default authorization, server-side projection, integrity-checked receipts, bounded input sizes, deterministic simulation limits, no arbitrary code or rule execution, no external endpoints in the zero-service path, and no model access to credentials.

## 20. Export, backup, restore, and migration

Encounter export includes authorized Encounter drafts and snapshots, placements, source/version references, assumptions, validation results, pressure dimensions, warnings, uncertainty, analysis and simulation receipts, comparison deltas, approval and Scene-attachment receipts, schema versions, and pack locks.

Backup and restore preserve immutable snapshots and Event order. Migration preserves stable IDs, source provenance, visibility, uncertainty, warnings, and historical readability. A migrated analysis is not silently treated as equivalent; compatibility is re-evaluated and recorded.

## 21. Cost, provider, and AI boundaries

Core composition, validation, analysis, comparison, deterministic simulation, export, and recovery must operate locally or through provider-neutral first-party services with no paid third-party requirement.

No hosted simulation vendor, analytics service, production database, credential, or paid AI is authorized. Optional AI may explain source-linked warnings or propose explicit changes, but it cannot access broader hidden information, run unbounded simulation, approve, attach, or guarantee balance. The same workflow remains usable with AI disabled.

## 22. Deterministic fixtures and test strategy

Required fixtures include:

- a valid mixed encounter with complete governed data;
- an invalid dependency and pack-lock case;
- an incomplete-source high-uncertainty case;
- a hidden reinforcement and Player-preview case;
- an extreme action-economy and control-warning case;
- a stale-version and concurrent-edit case;
- a reconnect and ambiguous-command case;
- a corrupted analysis-receipt case;
- a deterministic simulation replay case;
- a Scene attachment invalidated by a dependency change.

Tests cover authorization, stable-ID selection, provenance, validation, pressure dimensions, uncertainty, no-guarantee language, deterministic checksums, hidden-information non-disclosure, recovery, offline boundaries, accessibility, exports, provider neutrality, and zero-service operation.

## 23. Blocking acceptance criteria

- **EBL-AC-001 — Blocking:** An authorized GM can create an Encounter draft bound to one Campaign, Scene, rules profile, schema set, pack lock, and exact analysis-policy version.
- **EBL-AC-002 — Blocking:** The builder selects Characters, creatures, NPCs, hazards, environments, objectives, reinforcements, and rewards only by stable governed IDs with source and version receipts.
- **EBL-AC-003 — Blocking:** Encounter-local placements and analysis overrides never mutate source Definitions, Character records, Scene drafts, or active Session state.
- **EBL-AC-004 — Blocking:** Every save and analysis command reauthorizes the actor, Campaign role, Assistant-GM delegation, object visibility, entitlements, pack compatibility, and current versions.
- **EBL-AC-005 — Blocking:** The system validates required dependencies, unresolved references, incompatible scales, duplicate-exclusive traits, missing actions/resources, and illegal placement combinations before launch attachment.
- **EBL-AC-006 — Blocking:** Pressure estimates expose their dimensions, normalized inputs, assumptions, evidence sources, uncertainty, omitted variables, and analysis-policy version.
- **EBL-AC-007 — Blocking:** No output is labeled balanced, fair, safe, winnable, optimal, or guaranteed; the user receives source-grounded warnings and uncertainty-aware ranges instead.
- **EBL-AC-008 — Blocking:** The analysis distinguishes party capacity, opposition pressure, environment pressure, objective pressure, attrition, action economy, control, mobility, information, and escape or failure-path pressure.
- **EBL-AC-009 — Blocking:** Unknown, incomplete, variant, contradictory, or low-confidence object data lowers confidence and creates explicit warnings rather than being silently imputed as fact.
- **EBL-AC-010 — Blocking:** Bounded simulations are deterministic for an exact fixture, seed, policy, and input digest, remain advisory, and never execute live game authority or mutate Campaign state.
- **EBL-AC-011 — Blocking:** Scenario comparison changes one or more explicit variables, records the delta, and preserves separate immutable analysis snapshots and receipts.
- **EBL-AC-012 — Blocking:** Player and observer projections reveal no hidden participants, counts, reinforcements, tactics, secret objectives, GM notes, or warning details beyond their authorized projection.
- **EBL-AC-013 — Blocking:** The GM can attach an approved Encounter snapshot to a Scene launch draft without altering an existing launch snapshot or active Session.
- **EBL-AC-014 — Blocking:** Concurrent edits, stale expected versions, ambiguous failures, reconnects, and revocations preserve local drafts and authoritative state without silent overwrite or duplicate accepted effects.
- **EBL-AC-015 — Blocking:** Offline use is limited to manifest-bound reading, local draft edits, and previously generated analysis snapshots; authoritative save, analysis, approval, and attachment require reconnection.
- **EBL-AC-016 — Blocking:** Every warning and estimate is keyboard reachable, screen-reader understandable, noncolor encoded, high-zoom usable, and available in compact mobile and full desktop presentations with equivalent authority.
- **EBL-AC-017 — Blocking:** Diagnostics exclude hidden encounter content and raw private notes by default, use allowlists and redaction, and require separate governed support access.
- **EBL-AC-018 — Blocking:** Exports preserve encounter identity, source versions, assumptions, warnings, uncertainty, analysis snapshots, receipts, and pack/schema identities without exposing unauthorized content.
- **EBL-AC-019 — Blocking:** The core builder, validation, comparison, and deterministic bounded simulation path works without AI, paid services, hosted simulation vendors, production credentials, or external telemetry.
- **EBL-AC-020 — Blocking:** Deterministic fixtures cover valid, invalid, high-uncertainty, hidden-information, reconnect, stale-version, and corrupted-analysis cases, and all blocking tests pass before implementation handoff.

## 24. Implementation handoff, boundaries, and next action

### Implementation decomposition

1. Encounter aggregate and repository.
2. Stable-ID composition and placement receipts.
3. Validation and compatibility engine.
4. Pressure-dimension and uncertainty engine.
5. Warning and evidence projection.
6. Deterministic bounded simulation adapter.
7. Scenario comparison and snapshot store.
8. Approval and Scene-attachment command path.
9. Permission-safe projections.
10. Recovery, export, diagnostics, responsive, and accessibility integration.

### Completion boundary

This packet is an implementation-ready design artifact only. It does not implement the application, run live balance studies, authorize production data, certify encounter fairness, or permit internal-alpha release.

### Exact next design action

**IA-D03-004 — Define the internal-alpha content and deterministic fixture specification.**

That item must select and version the bounded Character, creature, NPC, Action, Ability, Effect, Condition, Resource, item, environment, hazard, objective, Scene, Encounter, and recovery fixtures needed by the first playable loop without pretending the selected corpus is the full game.
