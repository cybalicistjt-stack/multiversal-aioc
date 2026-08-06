# IA-D03-005 — Character/Campaign Integration Review

**Program:** MV-IA-001  
**Review ID:** IA-D03-005  
**Version:** 0.1.0  
**Status:** COMPLETE — DESIGN INTEGRATION REVIEW  
**Owner and final authority:** John Brandon Turner  
**Date:** 2026-08-06  
**Reviewed scope:** MV-IA-F004, MV-IA-F005, MV-IA-F012, and IA-D03-004  
**Companion matrix:** `IA-D03-005_CHARACTER_CAMPAIGN_CONTRACT_MATRIX.json`  
**Findings register:** `IA-D03-005_INTEGRATION_FINDINGS_REGISTER.json`

## 1. Purpose

This review closes Tranche IA-D03 by proving that Character creation and advancement, Campaign/Scene/Session preparation, Encounter composition and analysis, and the bounded deterministic fixture corpus form one coherent preparation path.

The review does not authorize application code, canonical content promotion, paid services, production credentials, real-user data collection, internal-alpha release, production deployment, or public release.

## 2. Reviewed authority and scope

The controlling sources are:

- MV-IA-F004 Character Creation and Advancement;
- MV-IA-F005 Campaign, Scene, and Session Builder;
- MV-IA-F012 Encounter Builder and Balance Lab;
- IA-D03-004 Internal Alpha Content and Deterministic Fixtures;
- IA-D02-006 Shared-Foundations Integration Review for cross-cutting identity, authority, projection, persistence, recovery, diagnostics, accessibility, and provider-neutral rules.

The review covers the complete preparation path up to, but not including, the first playable Action and GM Approval Loop.

## 3. Review method and blocking rule

The four sources were compared across authority, identity, lifecycle, policy binding, source provenance, placement, Character control, roster binding, Scene validation, Encounter analysis, launch snapshots, Events, projections, idempotency, conflict, reconnect, revocation, offline behavior, migration, export, diagnostics, accessibility, fixtures, cost, and implementation ordering.

A finding is blocking when two sources would permit different authority, expose different protected information, assign incompatible meaning to the same persisted field, mutate an immutable artifact, silently discard provenance or history, or hand IA-D04-001 an ambiguous contract.

## 4. Governing precedence

When reviewed contracts overlap, precedence is:

1. owner decisions and active Phase 9 architecture;
2. IA-D02-006 shared foundations for identity, authorization, projection, recovery, diagnostics, accessibility, and provider neutrality;
3. MV-IA-F005 for Campaign policy, membership, role, delegation, Character control, Scene authority, launch snapshots, and Session launch;
4. MV-IA-F004 for Character lifecycle, calculation, submission, activation, advancement, correction, retirement, history, and Character migration;
5. MV-IA-F012 for Encounter composition, analysis, uncertainty, warnings, approval, comparison, bounded simulation, and Scene attachment;
6. IA-D03-004 for fixture identity, provenance class, deterministic coverage, pack ordering, migration, cleanup, and checksum behavior.

A lower-precedence source may narrow its own domain. It may not widen authority, weaken projection safety, mutate source Definitions or immutable snapshots, or convert synthetic fixture behavior into canonical source truth.

## 5. Integrated actor and authority model

Authentication, Campaign membership, role, Assistant-GM delegation, observer grant, Character control, ownership, custody, entitlement, support access, and selected context remain separate decisions.

AI is an optional assistive service actor. It has no Campaign membership, Character control, approval, attachment, launch, migration, export, or support authority. It receives only an already-authorized, further-narrowed projection and is unnecessary for the core path.

Campaign authority controls current preparation policy. Character services consume that authority and persist exact historical bindings. Encounter analysis never creates authority.

## 6. Canonical identity, version, and policy bindings

The integrated path uses stable IDs rather than names, aliases, filenames, or provider identifiers.

Required cross-domain bindings include `campaignId`, `characterId`, `sceneId`, `encounterId`, `placementId`, `snapshotId`, `sessionId`, `operationId`, `eventId`, and `correlationId`.

Every protected mutation revalidates `permissionVersion`, `entitlementVersion`, `expectedVersion`, exact rules/creation/advancement/visibility policy versions, `packLockDigest`, and schema versions.

Compatibility aliases are normalized only at service boundaries and never become alternate persisted identities.

## 7. Character-to-Campaign lifecycle path

An authorized Campaign establishes rules, creation, advancement, visibility, entitlement, and pack policy. A Player may then create, save, submit, and—when policy permits—activate a Character.

Character state is controlled by accepted durable Character Events and current server projections. Local calculations, caches, drafts, realtime messages, and offline snapshots are nonauthoritative.

Character control is a Campaign-scoped grant. It is not inferred from ownership, membership, role, selected context, or prior access.

## 8. Definition, placement, instance, snapshot, and projection separation

Reusable source Definitions retain `definitionId`, version, pack identity, and provenance. Scene and Encounter placements reference a source Definition and add local identity, quantity, position, visibility, state, overrides, and notes.

Placements never mutate reusable source Definitions. Live Session instances are distinct from preparation placements. Immutable analysis and launch snapshots are distinct from mutable drafts. Projections are role-safe views, not stored authority.

Domain-qualified aggregate and Event envelopes prevent Scene placement and Encounter placement names from being treated as the same persisted aggregate.

## 9. Character control and roster binding

Scene and Encounter preparation bind stable Character identity and exact Character version through current membership, lifecycle, control, permission, entitlement, pack, and policy decisions.

Preparation surfaces receive a permission-safe roster projection or immutable roster snapshot. They do not copy the Character body, Player-private notes, GM-only fields, control history, or unrelated Campaign state.

Later Character advancement does not rewrite a prior launch snapshot or active Session. A new snapshot or governed amendment is required.

## 10. Scene validation and immutable launch snapshot

A Scene remains mutable preparation state until validation produces a receipt. Validation covers required fields, stable references, Campaign isolation, permissions, entitlement, pack/schema/rules compatibility, visibility, Character control and lifecycle, membership, role scope, observer and Assistant-GM grants, objectives, map alternatives, placement policy, and attachment readiness.

Session launch is exactly-once and uses an immutable launch snapshot containing exact Campaign, Scene, Character, placement, policy, pack, schema, visibility, validation, and content-digest bindings.

Later Scene edits do not mutate an active Session.

## 11. Encounter analysis, approval, and Scene attachment

Encounter composition uses governed stable IDs, source provenance, local placements, roster binding, objectives, environment, waves, assumptions, and overrides.

Analysis preserves twelve independent pressure dimensions and records inputs, assumptions, uncertainty, omitted variables, contradictions, warnings, policy version, and receipt integrity.

No output may claim that an Encounter is balanced, fair, safe, winnable, survivable, optimal, or guaranteed. Bounded simulations are deterministic, advisory, nonmutating, and are not predictions of actual Players.

Only an authorized approved Encounter snapshot may attach to a mutable Scene. Attachment changes require Scene revalidation and cannot mutate source Definitions, Character state, prior launch snapshots, or active Sessions.

## 12. Projection and hidden-information safety

Authorization and entitlement filtering occur before ranking, counts, suggestions, warnings, previews, relationship traversal, exports, diagnostics, AI retrieval, and serialization.

Player and observer previews are server-generated for a resolved subject and selected context. A client cannot select a role, visibility class, or preview mode that widens access.

GM-only notes, Player-private notes, hidden placements, secret objectives, hidden participant identities, source-license-sensitive content, and security-sensitive fields are removed before ordinary client delivery.

## 13. Commands, Events, idempotency, concurrency, and revocation

Every authoritative command has a stable operation identity, expected version, current authority decision, and correlation identity.

A lost response is resolved by status lookup using the original operation or command ID before retry. Duplicate use of the same identity returns the prior result or current status; conflicting reuse fails safely.

Stale writes preserve both local and authoritative versions. Silent last-write-wins is prohibited.

Accepted durable Events and current server projections are authoritative. Realtime messages are advisory.

Revocation ends affected subscriptions, invalidates selected-context and preparation receipts, partitions or clears protected caches, removes protected projections, and blocks further status lookup outside current authority.

## 14. Recovery, offline use, migration, checkpoint, and export

Offline behavior is manifest-bound read and local-draft preparation only. It cannot perform authoritative Character, Campaign, Scene, Encounter, approval, attachment, launch, migration, restore, or export-finalization mutations.

Recovery preserves local drafts, authoritative state, operation identities, Event sequences, receipts, warnings, and pre-change snapshots.

Migration ordering is Campaign authority and pack/schema state first, then dependent Character, Scene, Encounter, attachment, and any new launch snapshot. Historical snapshots remain immutable and may be marked incompatible rather than silently rewritten.

Authorized exports preserve stable IDs, versions, policy/pack/schema bindings, provenance, Events, receipts, warnings, uncertainty, and redaction decisions.

## 15. Fixture and provenance coverage

IA-D03-004 provides 155 exact fixture identities:

- 36 source-backed governed selectors;
- 119 explicitly synthetic noncanonical fixtures;
- five exact-version fixture packs;
- fifteen covered requirement families;
- nine deterministic pack-lifecycle scenarios;
- eleven accessibility stressors.

The corpus covers the bounded internal-alpha preparation contract. It does not cover the complete game and is not a canonical content release.

Synthetic fixtures cannot establish canonical source behavior, source completeness, canonical balance, or production content readiness. Unselected source material remains preserved.

## 16. Accessibility, diagnostics, support, provider, and cost boundaries

Authority, evidence, warnings, uncertainty, recovery choices, confirmation, and denial meaning remain equivalent across desktop, tablet, mobile, keyboard, touch, screen reader, high zoom, reduced motion, and noncolor presentation.

Graphs, maps, pressure views, rosters, and placement canvases require list, table, text, or single-focus alternatives.

Diagnostics default to exclude protected prose and hidden IDs. Issue submission and assignment never grant Campaign, Character, Scene, Encounter, or Session access.

Core operation and deterministic CI require zero AI and no paid identity, search, realtime, map, analytics, crash-reporting, ticketing, notification, or simulation provider.

## 17. Resolved integration findings

The review resolved twelve findings:

- CCI-F001 — Campaign policy precedence;
- CCI-F002 — Character control ownership;
- CCI-F003 — Character roster binding;
- CCI-F004 — Definition and placement Event overlap;
- CCI-F005 — launch snapshot versus live Character state;
- CCI-F006 — Encounter attachment lifecycle;
- CCI-F007 — Player preview authority;
- CCI-F008 — operation and Event naming normalization;
- CCI-F009 — recovery and migration order;
- CCI-F010 — fixture provenance boundary;
- CCI-F011 — diagnostics, export, and AI projection;
- CCI-F012 — implementation ordering.

The companion findings register records the source issue, decision, affected consumers, and required evidence for each finding.

No blocking integration finding remains open.

## 18. Implementation slice order

The dependency-safe implementation order is:

1. canonical IDs, policy bindings, and common command/Event envelopes;
2. authorization, projection, inference safety, and context revalidation;
3. Campaign authority, membership, roles, delegation, pack lock, and Character control;
4. Character draft, calculation, submission, activation, advancement, and history;
5. source Definition selection, Scene placement, roster binding, and validation;
6. Encounter composition, validation, analysis, comparison, and bounded simulation;
7. Encounter approval, Scene attachment, invalidation, and revalidation;
8. immutable launch snapshot and first-playable-loop handoff;
9. reconnect, offline, migration, checkpoint, recovery, and export;
10. deterministic fixtures, accessibility parity, diagnostics, and zero-service adapters.

Implementation remains dependency-gated by P9-06. This order is a design handoff, not authorization to begin production work.

## 19. Integrated acceptance criteria

- **CCI-AC-001:** Reviewed authority and precedence are explicit.
- **CCI-AC-002:** Campaign owns current rules, creation, advancement, visibility, entitlement, and pack policy.
- **CCI-AC-003:** Character identity, lifecycle, control, membership, role, and entitlement remain separate.
- **CCI-AC-004:** All dependent artifacts use stable IDs and exact versions.
- **CCI-AC-005:** Definitions, placements, instances, snapshots, Events, projections, and indexes remain distinct.
- **CCI-AC-006:** Scene and Encounter roster binding does not copy or mutate Character bodies.
- **CCI-AC-007:** Player and observer previews are server-generated permission-safe projections.
- **CCI-AC-008:** Encounter analysis remains advisory and never claims guaranteed balance, fairness, safety, victory, survival, or optimality.
- **CCI-AC-009:** An Encounter attachment cannot mutate an active Session or prior launch snapshot.
- **CCI-AC-010:** Scene validation includes current Encounter attachment and Character binding checks.
- **CCI-AC-011:** Session launch uses an immutable exact-version launch snapshot and exactly-once command identity.
- **CCI-AC-012:** Every protected command reauthorizes and revalidates expected version.
- **CCI-AC-013:** Ambiguous failure uses original operation status lookup before retry.
- **CCI-AC-014:** Stale writes preserve conflicts and never silently overwrite.
- **CCI-AC-015:** Revocation invalidates routes, caches, receipts, subscriptions, status lookup, and projections.
- **CCI-AC-016:** Offline use cannot perform authoritative preparation or launch mutations.
- **CCI-AC-017:** Migration and recovery follow dependency order and preserve historical snapshots and receipts.
- **CCI-AC-018:** Exports preserve provenance, redaction, versions, warnings, uncertainty, and receipt references.
- **CCI-AC-019:** Diagnostics exclude protected content by default and support access remains separate.
- **CCI-AC-020:** Fixture coverage is bounded, deterministic, checksum-backed, and provenance-labeled.
- **CCI-AC-021:** Synthetic fixtures remain noncanonical and do not establish complete-game coverage.
- **CCI-AC-022:** Accessible and responsive presentations preserve authority, evidence, warnings, and recovery choices.
- **CCI-AC-023:** Core operation requires no AI, paid provider, production credential, or external telemetry.
- **CCI-AC-024:** Implementation order and IA-D04-001 handoff are explicit, with zero blocking integration findings.

## 20. Conclusion and next action

MV-IA-F004, MV-IA-F005, MV-IA-F012, and IA-D03-004 form one coherent permission-safe, versioned, recoverable Character/Campaign preparation path.

The path preserves Campaign policy authority, Character lifecycle and control boundaries, Definition/placement/instance separation, advisory Encounter analysis, immutable launch snapshots, durable Event authority, conflict-safe recovery, bounded offline use, transparent fixture provenance, accessibility parity, and zero-service operation.

No blocking integration finding remains open.

IA-D03 is complete at design level. The exact next design item is **IA-D04-001 — MV-IA-F006 First Playable Action and GM Approval Loop**.

Silence is not approval. Implementation, internal-alpha release, production deployment, spending, credentials, and public release remain separately gated.
