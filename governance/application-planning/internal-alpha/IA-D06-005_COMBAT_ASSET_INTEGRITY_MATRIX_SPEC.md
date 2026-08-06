# IA-D06-005 — Combat/Asset Integrity Matrix

**Program:** MV-IA-001  
**Owner:** John Brandon Turner  
**Status:** COMPLETE DESIGN / IMPLEMENTATION-READY  
**Boundary:** Internal-alpha design only; implementation remains dependency-gated by P9-06.

## 1. Purpose

Prove that Full Combat Interface, Inventory/Ownership/Shared Assets, bounded Maps/Zones/Tactical Positioning, and Vehicle/Mecha/Starship Operations can execute together without double-spend, partial mutation, authority drift, hidden-information leakage, or unrecoverable divergence.

## 2. Governing invariants

1. Every accepted combat operation produces one atomic authoritative result group.
2. Asset identity, quantity, lineage, ownership, custody, control, equipment, location, durability, and reservation are never conflated.
3. Proposal approval does not itself mutate Assets; only committed authoritative results do.
4. Denied, expired, cancelled, stale, superseded, or duplicated proposals consume nothing.
5. Costs, ammunition, charges, fuel, heat, stress, durability, damage, movement, Conditions, Effects, and history commit together or not at all.
6. Server authority validates controller, station, equipment, reservation, target, timing, range, topology, Resource availability, expected versions, and idempotency.
7. Hidden Assets, cargo, systems, occupants, routes, quantities, capabilities, and modifiers are filtered before search, counts, totals, previews, exports, diagnostics, notifications, and optional-AI context.
8. Reconnect uses status lookup, versioned snapshots, ordered Events, Event-gap repair, and idempotent replay.
9. Reversal uses compensating Events and lineage-preserving restoration; history is never silently rewritten.
10. `P9-06-008-attempt-002` remains unfinished and unmodified.

## 3. Integrity domains

The matrix covers Action proposals, approval decisions, combat timing, participant control, Asset reservations, equipment eligibility, stack quantities, ammunition and charges, consumables, fuel and power, heat and stress, durability and damage, movement and position, vehicles and stations, carried craft, docking and boarding, hidden information, pack lifecycle, provenance, reconnect, and undo.

## 4. Atomic result contract

An accepted operation creates a single `CombatAssetResultGroup` containing:

- stable result-group and idempotency identifiers;
- proposal and decision references;
- expected aggregate versions;
- precondition evidence;
- ordered domain mutations;
- owning-domain Events;
- role-filtered projections;
- provenance snapshots;
- recovery status.

No client may directly decrement quantities, move an Asset, change durability, assign control, or publish history before the server commits the result group.

## 5. Reservation and contention

Reservations are typed, scoped, versioned, expiring, and visible only to authorized roles. Competing proposals cannot both reserve the same exclusive Asset quantity, station, weapon, vehicle control slot, or carried craft. Partial stack reservations identify exact lots. Expiry produces an authoritative release Event.

## 6. Combat cost timing

Costs are classified as proposal-time hold, commit-time spend, sustained-period spend, reaction-window spend, or post-resolution consequence. Proposal-time holds are reservations, not consumption. Commit-time spend occurs only in the accepted result group. Sustained costs are separate authoritative ticks with stable correlation identifiers.

## 7. Vehicles and nested Assets

Vehicle operations validate station authority, command policy, system state, mounted equipment, ammunition feed, fuel/power, heat/stress, semantic position, docking/boarding state, carried-craft attachment, and interior/exterior participant position. Damage to a carrier does not silently mutate cargo or occupants unless an explicit Effect processor does so.

## 8. Destruction, defeat, salvage, and capture

Zero durability is not universal deletion. Profiles determine disabled, broken, wrecked, destroyed, abandoned, captured, salvageable, or tombstoned outcomes. Ownership and provenance survive unless an explicit governed transfer occurs. Irreversible destruction is outside internal-alpha authorization.

## 9. Hidden-information boundary

Unauthorized users receive stable opaque references or absence according to policy, never inferential counts. Redaction occurs before aggregation, pathfinding, eligibility previews, resource totals, combat logs, exports, diagnostics, notifications, and optional-AI context construction.

## 10. Accessibility and nonvisual parity

Every integrity operation is possible through list, table, detail, semantic position outline, station roster, keyboard, touch, screen reader, reduced-motion, high-contrast, responsive, and nonvisual workflows. Dragging, canvas precision, color, hover, or animation is never required.

## 11. Recovery and concurrency

Every mutating request uses idempotency keys and expected versions. Lost responses require status lookup before retry. Conflicts return current versions and safe refresh instructions. Event gaps trigger bounded snapshot-plus-tail repair. Revocation invalidates pending authority immediately.

## 12. Pack lifecycle and provenance

Committed history stores exact source identifiers, versions, checksums, and bounded snapshots needed for later interpretation. Pack disablement or removal blocks new use but does not erase prior results. Missing definitions produce governed tombstones rather than silent substitution.

## 13. Implementation slices

- CAI-S01 — aggregate/version and idempotency foundations.
- CAI-S02 — reservation and contention service.
- CAI-S03 — atomic cost/effect/result coordinator.
- CAI-S04 — equipment, quantity, durability, and lineage adapters.
- CAI-S05 — map, position, vehicle, station, and nested-Asset adapters.
- CAI-S06 — hidden-information projection and accessibility parity.
- CAI-S07 — reconnect, status lookup, Event-gap repair, and compensating undo.
- CAI-S08 — deterministic fixtures, observability, and implementation handoff.

## 14. Acceptance criteria

CAI-AC-001 through CAI-AC-028 are blocking and are enumerated in the integrity matrix. Zero blocking findings remain.

## 15. Explicit exclusions

No deployment, release, paid service, production credential, real-user data, canonical content promotion, autonomous AI authority, irreversible Asset destruction, or modification of `P9-06-008-attempt-002` is authorized.

## 16. Decision

IA-D06-005 is implementation-ready. The next work item is **IA-D06-006 — combat and Assets integration review**.