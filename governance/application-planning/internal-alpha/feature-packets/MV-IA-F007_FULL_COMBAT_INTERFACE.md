# MV-IA-F007 Full Combat Interface

**Work item:** IA-D06-001  
**Program:** MV-IA-001  
**Owner:** John Brandon Turner  
**Status:** implementation-ready design; dependency-gated  
**Version:** 0.1.0

## 1. Purpose

Define the bounded internal-alpha combat runtime that extends the first playable Action/GM approval loop into a complete encounter with participants, order, movement, targeting, Resources, Conditions, reactions, hazards, NPC/enemy parity, authoritative results, recovery, and encounter completion.

## 2. Governing principle

Combat is an authoritative Session-scoped state machine. Clients propose intent and render role-safe projections. Only accepted decisions, validated consumer commits, ordered Events, and current server projections are authoritative.

## 3. Scope

The alpha slice supports one complete bounded encounter without development-only tools. It includes turn/phase order, participant control, Action selection, target validation, movement or zone changes, costs, rolls, Effects, Conditions, reactions, hazards, defeat/withdrawal, and completion.

## 4. Required dependencies

MV-IA-F003 identity/workspace, F004 Character, F005 Campaign/Scene/Session, F006 Action approval, F012 Encounter Builder, F020 permissions, F021 recovery, IA-D04 shared proposal/reconnect/history contracts, and IA-D05 role-safe semantic projection rules.

## 5. Core records

- Combat Encounter
- Combat Participant
- Participant Controller Assignment
- Initiative/Order Entry
- Turn/Phase Window
- Position/Zone State
- Action Proposal and Decision
- Reaction Window and Reaction Claim
- Target Set
- Resource Ledger Entry
- Condition Instance
- Effect Application
- Hazard Instance
- Defeat/Withdrawal State
- Encounter Completion Receipt

## 6. Encounter lifecycle

`draft`, `ready`, `starting`, `active`, `paused`, `resolving`, `ending`, `completed`, `aborted`, and `recovery-required` are distinct states. Launch snapshots exact participant, rule, source, environment, map/zone, and permission versions.

## 7. Participant model

Characters, NPCs, enemies, allies, summons, vehicles, hazards, and abstract groups may participate through typed participant adapters. A participant has one authoritative identity, current controller, role-safe display projection, current Resources, Conditions, position, and availability state.

## 8. Control and authority

Player control, GM control, delegated Assistant-GM control, and automation eligibility are explicit. Control does not imply ownership, visibility, authorship, or permission outside the encounter. NPC and enemy Actions use the same proposal, review, resolution, result, and history path as Player Actions, with configured GM review policy.

## 9. Order and timing

Order is profile-defined rather than universally initiative-only. Supported alpha timing types are round, turn, phase, free-action window, reaction window, interrupt window, simultaneous group, environmental pulse, and encounter-end window. Stable order IDs and sequence numbers survive reconnect.

## 10. Action flow

An Action proposal contains actor, controller, source Action/version, targets, timing, costs, requirements, position/range context, selected options, roll/seed request, visible modifiers, hidden-GM modifier slots, proposed Effects, warnings, and expected versions. GM review may approve, deny, or field-address modify-and-approve with final revalidation.

## 11. Targeting

Targets are validated by identity, encounter membership, visibility, reach/range, line/zone rules, eligibility, immunity, permission, and current state. Hidden targets cannot be enumerated through search, counts, area previews, diagnostics, exports, or AI context. Area and multi-target Actions use deterministic target-set snapshots.

## 12. Movement and positioning

Alpha supports abstract zones and optional uploaded maps without requiring advanced map authoring. Position authority is semantic: zone, adjacency, distance band, elevation band, cover, occupancy, and movement state. Pixel coordinates and token placement are presentation aids unless a bound rules profile explicitly maps them to semantic state.

## 13. Resources and costs

Costs reserve, validate, and commit atomically with accepted results. Health, stamina, mana, action points, ammunition, charges, durability, currency, and custom Resources use owning-domain ledgers. Denied or failed-before-commit proposals do not consume accepted costs. Refunds use attributable compensating Events.

## 14. Effects and Conditions

Damage, healing, movement, Resource change, Condition application/removal, summoning, transformation, equipment state, terrain/hazard change, and custom Effects are typed drafts validated by owning processors. Condition stacking, duration, source, save/check, immunity, suppression, and expiration follow versioned profiles.

## 15. Reactions and interrupts

Reaction windows are server-opened, bounded, ordered, and role-filtered. Claims are advisory until accepted. Expiry, pass, duplicate claim, conflicting claim, disconnect, and hidden eligibility are explicit. Exactly one accepted resolution path controls each reaction slot.

## 16. Hazards and environment

Hazards and environmental pulses act through typed participants or scheduled Event processors. Environment adaptations, resistances, movement limits, visibility effects, and terrain consequences remain source/version bound and cannot be inferred from UI appearance alone.

## 17. Resolution and atomicity

One accepted Action produces one authoritative result group. Every cost and Effect either commits atomically or the group fails without partial mutation. Cross-domain adapters preserve owning-domain Event identities and return one linked result receipt.

## 18. Defeat, withdrawal, and death boundaries

Defeated, incapacitated, dying, dead, destroyed, surrendered, fled, removed, and unavailable are separate profile-defined states. A zero Resource value does not universally imply death. Permanent Character death, destruction, or irreversible loss requires the bound rules profile and existing GM/owner authority.

## 19. Encounter completion

Completion requires an explicit GM-authorized or profile-authorized completion decision, final pending-window closure, authoritative participant outcomes, unresolved-effect disposition, loot/Asset handoff boundary, progression draft, and completion receipt. Combat completion does not itself grant Assets, XP, advancement, faction standing, or canonical changes without owning-domain commits.

## 20. Presentation

Player default view prioritizes current actor, available Actions, targets, Resources, Conditions, order, position, warnings, and authoritative result. Action log and proposals remain secondary. GM Combat Operations shows all authorized participants, queues, hidden modifiers, reactions, hazards, pending outcomes, and approve/deny/modify controls.

## 21. Accessibility and responsive behavior

Every combat operation has keyboard, screen-reader, touch, text-scaled, high-contrast, reduced-motion, and nonvisual alternatives. Color, animation, map position, drag, hover, and line shape are never the only meaning carrier. Mobile layouts preserve full action, targeting, reaction, approval, and recovery semantics.

## 22. Recovery and concurrency

Every submit uses idempotency keys and expected versions. Lost submit, decision, or commit responses require status lookup before retry. Reconnect restores current role-safe projections, active timing windows, claims, sequence gaps, and pending results. Offline authoritative combat mutation is prohibited.

## 23. Security, privacy, and optional AI

Server filtering precedes counts, search, range previews, target suggestions, notifications, exports, diagnostics, and AI context. AI may summarize authorized state or draft suggestions only. It cannot select Player Actions, reveal hidden state, approve decisions, choose NPC truth, commit Events, or determine canonical outcomes.

## 24. Implementation and acceptance boundary

Implementation proceeds through eight dependency-ordered slices and twenty-four deterministic fixtures. All twenty-eight acceptance criteria are blocking. Design completion does not authorize application activation, paid services, credentials, real-user data collection, internal-alpha release, deployment, public release, irreversible Character loss, or canonical promotion. `P9-06-008-attempt-002` remains unfinished and unmodified.

## Implementation slices

1. Combat encounter lifecycle and participant projections.
2. Order, timing windows, and controller assignments.
3. Action proposal, GM review, targeting, and movement context.
4. Resources, costs, Effects, Conditions, and atomic result groups.
5. Reactions, interrupts, hazards, environment, defeat, and withdrawal.
6. Player/GM responsive and accessible presentation.
7. Recovery, idempotency, revocation, exports, diagnostics, and optional-AI boundaries.
8. Deterministic fixtures, acceptance harness, and downstream Asset/combat handoff.

## Next work item

IA-D06-002 — MV-IA-F008 Inventory, Ownership, and Shared Assets.
