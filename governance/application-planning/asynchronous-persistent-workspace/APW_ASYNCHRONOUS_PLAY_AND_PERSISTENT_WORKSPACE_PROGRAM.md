# APW — Asynchronous Play & Persistent Workspace Program

**Program ID:** APW  
**Version:** 0.1.0  
**Status:** OWNER-APPROVED PARALLEL PLANNING TRACK — PLANNED / NOT IMPLEMENTATION-ACTIVE  
**Owner and final authority:** John Brandon Turner  
**Approved planning direction:** 2026-08-18

## 1. Purpose

APW defines the product and implementation-ready architecture required for Multiversal to remain useful before, during, between, and independently of campaigns while adding first-class asynchronous campaign play.

The program does not create a second game engine. Live and asynchronous play use the same governed Campaign, Action, proposal/approval, Event, permission, persistence, provenance, and recovery architecture. APW adds cadence-aware workflows, personal workspaces, campaign-independent creation, and explicit contextual authority.

## 2. Owner-approved product principles

The following are controlling APW product decisions unless later superseded by explicit owner authority:

1. A subscribed Multiversal account is a universal user account, not permanently a Player account or GM account.
2. Player, Game Master, Assistant GM, Observer, creator, owner, and similar capabilities are contextual roles/authorities bound to Campaigns, workspaces, resources, ownership, delegation, entitlement, visibility, and current state.
3. A GM has authority over the Campaigns and Campaign-bound resources they govern; being a GM does not grant global authority over another user's Campaign or personal workspace.
4. Being a Player in a Campaign does not remove the user's normal independent Multiversal capabilities outside that Campaign.
5. Campaign membership must not reduce access to general/reference content that the user's entitlement otherwise allows. Campaign-specific hidden truth remains permission-protected.
6. Live, asynchronous, and hybrid play are cadences of the same Campaign rather than separate Campaign types or separate rules engines.
7. A Player may submit one durable Action/proposal with optional written intent/explanation for later GM review and resolution.
8. The GM may inspect and resolve queued proposals later through the governed proposal/approval architecture.
9. Multiversal should remain useful when no other participant is connected and when the user has no active Campaign.
10. Personal creation, experimentation, reference, organization, and reusable assets are first-class product activities.
11. Optional spoiler shielding may reduce accidental metagame exposure, but it is a user-experience aid rather than a security boundary. Campaign-private truth remains the actual authorization boundary.
12. AI remains optional and non-authoritative under existing governance unless later explicitly changed.

## 3. Three-axis product model

APW separates three concepts that must not be collapsed into one mode flag.

### Context

- Personal
- Campaign
- Session/active encounter

### Cadence

- Live
- Asynchronous
- Hybrid

### Connectivity

- Connected
- Temporarily offline/cached
- Recovering/reconnecting

A Campaign may move between live and asynchronous cadence without changing Campaign identity or creating a forked rules/state engine. Connectivity is independent of cadence: an asynchronous action can be submitted while connected, and offline behavior remains governed by the existing bounded offline/recovery policy.

## 4. Existing architecture APW must reuse

APW is additive over existing canonical work, especially:

- provider-neutral identity and workspace selection;
- contextual authorization, ownership, delegation, entitlement, and hidden-information filtering;
- Campaign/Scene/Session authority;
- Action proposal and GM approve/deny/modify-and-approve flow;
- immutable proposal evidence and durable decision receipts;
- notifications and role-safe queues;
- authoritative Events and projections;
- autosave, reconnect, status lookup, idempotency, stale-version handling, and recovery;
- downtime/project concepts;
- Character, inventory, crafting, vehicle, investigation, social, relationship, world, adventure, and authoring domains;
- universal object browsing/picking and provenance;
- responsive/accessibility requirements;
- campaign-local versus reusable/canonical content boundaries.

No APW tranche may bypass an owning domain's authority or reopen completed Stage A work merely to rename existing concepts. Additive successor implementation must preserve prior closure evidence.

## 5. Program boundaries

APW planning does not itself authorize:

- application implementation;
- migration execution;
- production identity/provider activation;
- paid services;
- release, deployment, tester access, or public publication;
- autonomous AI mutation;
- unrestricted offline multi-writer synchronization;
- a public creator marketplace or community-sharing platform.

Those remain separately governed.

## 6. Tranche plan

### APW-01 — Authority, Account, Context and Terminology Canonicalization

**Goal:** establish one unambiguous authority model before feature-specific design.

**Deliverables:**

- universal-user account contract;
- contextual-role and resource-authority matrix;
- Personal/Campaign/Session context definitions;
- Live/Async/Hybrid cadence definitions;
- Connected/Offline/Recovering connectivity definitions;
- campaign-private versus entitlement-available information boundary;
- terminology reconciliation against older simplified global GM/Player matrices;
- traceability map to identity, permissions, entitlements, workspaces, Campaign authority and creator ownership.

**Completion gate:** no global `isGM`-style assumption can grant authority outside governed context; existing completed implementation remains valid and future additive change points are explicit.

### APW-02 — Asynchronous Action, Proposal and GM Inbox Contract

**Goal:** turn the existing proposal/approval system into a durable delayed interaction workflow without creating a parallel resolution engine.

**Deliverables:**

- asynchronous Action consumer profile;
- single-action packet with optional written intent/explanation;
- subject, actor, target, Campaign, expected-version and provenance binding;
- draft/submit/pending-review/clarification/resolve/deny/withdraw/stale/recovery states;
- GM inbox, queue ordering, safe counts and notifications;
- clarify-and-resubmit behavior without silently mutating original evidence;
- GM approve/deny/modify-and-approve mapping;
- decision receipt and Player return notification;
- stale-state, duplicate-submit, conflicting-decision and reconnect handling;
- live-to-async and async-to-live continuation rules.

**Completion gate:** one proposal has one attributable authoritative outcome, survives disconnect/time separation, preserves hidden information, and reuses the shared proposal/approval contract.

### APW-03 — Between-Session Campaign Activity and Bounded Downtime

**Goal:** make active Campaigns useful between live sessions without requiring continuous GM presence.

**Deliverables:**

- Campaign Activity workspace model;
- bounded first-alpha activity classes;
- downtime/project submission and progress model;
- Character advancement/choice requests where governed;
- research, investigation/hypothesis, journal, preparation, relationship/social, crafting/repair and travel-preparation integration boundaries;
- GM-created prompts/tasks and Player responses;
- automatic versus GM-reviewed activity classification;
- activity expiration, cancellation, dependency and consequence rules;
- campaign timeline/history integration.

**Completion gate:** the program defines a narrow useful alpha slice while explicitly preserving full downtime/crafting/project breadth as separately expandable.

### APW-04 — Personal Workspace and No-Campaign Home

**Goal:** ensure Multiversal remains a coherent product for a user with no active Campaign and while no other user is online.

**Deliverables:**

- Personal workspace authority and ownership model;
- no-Campaign Home/Dashboard information architecture;
- `What needs you`, `Continue`, `Create`, and `Your Library` workspace groupings;
- personal Characters and drafts;
- recent work, favorites, collections, notes and saved references;
- Campaign role labels as contextual metadata rather than account identity;
- transitions between Personal and Campaign contexts without authority bleed;
- mobile/desktop/accessibility states including empty, offline and recovery states.

**Completion gate:** a subscribed user can obtain meaningful value and perform governed personal work with zero Campaign memberships.

### APW-05 — Creator Workshop, Reusable Assets and Sandbox/Lab

**Goal:** expose creation as a general user capability while keeping reusable definitions, Campaign variants, live instances and canonical promotion distinct.

**Deliverables:**

- Creator Workshop navigation and authority model;
- reusable asset ownership/library rules;
- supported creation entry points for Characters, worlds, locations, NPCs/creatures, items/abilities, encounters, adventures, vehicles/bases and templates as owning domains permit;
- draft/template/variant/live-instance boundary;
- import/link/copy/instantiate rules into a Campaign;
- personal Sandbox/Lab for disposable/noncanonical experimentation;
- save-as-template and explicit promotion paths;
- rules/build/loadout/encounter/configuration comparison seams;
- provenance, validation and content-origin presentation.

**Completion gate:** personal creation or experimentation cannot silently mutate Campaign truth or global canonical content, and Campaign authority does not control another user's independent library.

### APW-06 — Shell, Navigation, Notifications, Visibility and Spoiler UX

**Goal:** make the new model understandable rather than exposing users to raw authority/cadence complexity.

**Deliverables:**

- global shell/context-switching updates;
- contextual role presentation;
- pending-response and pending-review surfaces;
- Player waiting-state UX;
- GM `things need you` inbox UX;
- async activity notification taxonomy;
- return-to-context/deep-link rules;
- campaign-private information treatments;
- optional Spoiler Shield behavior and limitations;
- search/filter projection rules across Personal and Campaign contexts;
- keyboard, touch, screen-reader, reduced-motion and mobile acceptance paths.

**Completion gate:** users can always identify where they are, which authority applies, what is waiting, and whether information is personal, Campaign-local, reusable, hidden or merely spoiler-filtered.

### APW-07 — Persistence, Recovery, Security and Hybrid Acceptance Architecture

**Goal:** prove the concept remains deterministic and safe across time-separated and mixed-cadence use.

**Deliverables:**

- persistence/data-contract delta map;
- idempotency and optimistic/stale-version rules;
- event ordering and history requirements;
- asynchronous notification durability;
- reconnect/status lookup and ambiguous-failure recovery;
- permission revocation between submission and decision;
- entitlement change handling;
- hidden-information nonleakage through counts/search/notifications/history;
- cross-device and long-delay test matrix;
- live → async → live hybrid continuity scenarios;
- accessibility, performance, export, diagnostics and zero-paid-service test requirements.

**Completion gate:** deterministic fixtures demonstrate no duplicate accepted mutation, no stale silent overwrite, no protected-information leak, and one coherent Campaign history across mixed cadence.

### APW-08 — Implementation Handoff and Stage/Alpha Integration

**Goal:** convert APW design into dependency-ordered application work without invalidating completed Stage A closure evidence.

**Deliverables:**

- implementation-ready packet set and traceability matrix;
- migration/change inventory;
- exact additive touch-point map for identity/dashboard, Campaign/Scene, Action/approval, recovery, downtime/crafting, investigation/social and world/creator systems;
- feature flags and compatibility/fallback requirements where appropriate;
- deterministic fixture and validator inventory;
- dependency-ordered application implementation slices;
- Internal Alpha scope/acceptance amendments;
- roadmap placement recommendation for implementation;
- explicit non-reopening rule for completed Stage A milestones.

**Completion gate:** every planned application change has an owning domain, dependency, acceptance gate, rollback/compatibility boundary and implementation destination.

## 7. Execution order

Planning order is strictly:

`APW-01 → APW-02 → APW-03 → APW-04 → APW-05 → APW-06 → APW-07 → APW-08`

A later tranche may collect source references early, but it may not finalize authority or implementation contracts before its dependencies are complete.

Within each tranche, complete the bounded substantive package first, run the smallest relevant deterministic checks during construction, batch repairs, then run the declared tranche gate. Do not substitute repeated roadmap/checkpoint rewrites for substantive work.

## 8. Downstream implementation handoff model

APW-08 must produce additive application slices rather than retroactively reopening A3/A5/A6/A8/A9/A10 closures. The provisional implementation sequence is:

1. **APW-I01 — contextual account/role projection and personal-context authority extensions**;
2. **APW-I02 — Personal Home and workspace switching**;
3. **APW-I03 — asynchronous Action submission, durable GM inbox and delayed resolution**;
4. **APW-I04 — bounded Campaign Activity/downtime integration**;
5. **APW-I05 — Creator Workshop, reusable library and Sandbox/Lab integration**;
6. **APW-I06 — notification, visibility, recovery and hybrid cross-device integration**;
7. **APW-I07 — end-to-end hybrid acceptance: live → async → GM resolution → Player return → live continuation**.

These IDs are planning handles only until APW-08 publishes the final implementation handoff and the governing application roadmap activates them.

## 9. Minimum end-to-end product proof

The first implementation proof must demonstrate:

1. two ordinary subscribed users exist without global Player/GM caste;
2. User A is GM of a Campaign and User B is a Player in that Campaign;
3. User B submits one asynchronous Character Action with optional explanation and disconnects;
4. User A later opens the Campaign GM inbox, reviews authorized evidence and resolves the proposal;
5. one authoritative Event-backed result is committed;
6. User B later returns and sees the durable result and updated role-safe Campaign projection;
7. both users can leave the Campaign context and use their independent Personal workspaces and entitled creator/reference capabilities;
8. neither user's Campaign role grants authority over the other's independent resources;
9. Campaign-hidden information remains protected throughout;
10. the Campaign can subsequently resume live play from the same authoritative history.

## 10. Relationship to current execution

APW is a parallel planning track. Creating or completing APW planning does not select it as the conversational primary attempt and does not interrupt or supersede the current CCTI-12 attempt, ordinary Stage A work, DS-008, WP-011/Apple, or any preserved deferred track.

The runtime pointer must change only through the normal owner-selected/work-recovery process when APW execution itself is selected.

## 11. Program completion

APW planning is complete only when APW-01 through APW-08 are `completed_verified`, their implementation handoff is merged, roadmap/dependency projections are synchronized, and no acceptance gate depends on an unstated authority or data-flow assumption.

Completion of APW planning does not mean APW application implementation is complete.
