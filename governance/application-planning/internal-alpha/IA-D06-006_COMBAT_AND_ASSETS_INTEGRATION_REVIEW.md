# IA-D06-006 — Combat and Assets Integration Review

**Owner:** John Brandon Turner  
**Status:** COMPLETE DESIGN / IMPLEMENTATION-READY  
**Boundary:** Internal-alpha design only; implementation remains dependency-gated by P9-06.

## 1. Review scope

This review integrates IA-D06-001 Full Combat Interface, IA-D06-002 Inventory/Ownership/Shared Assets, IA-D06-003 bounded Maps/Zones/Tactical Positioning, IA-D06-004 Vehicle/Mecha/Starship Operations, and IA-D06-005 Combat/Asset Integrity Matrix into one coherent runtime contract.

## 2. Integrated runtime model

The runtime preserves distinct authoritative aggregates for encounter state, participants and timing, Asset identity and lineage, reservations and quantities, semantic position and topology, Vehicle systems and stations, permissions, provenance, and recovery. Cross-domain operations commit through one atomic result coordinator with ordered owning-domain Events.

## 3. End-to-end journeys

1. Character equips, reserves, targets, moves, attacks, spends ammunition, applies Effects, and records history.
2. Shared Asset is reserved by one participant while a competing proposal is rejected without consumption.
3. Vehicle crew assumes stations, allocates power, moves semantically, fires mounted systems, accumulates heat, and receives damage.
4. Carried craft launches, changes location/control, enters a new tactical context, and preserves ownership and provenance.
5. Boarding changes participant location and custody without silently changing ownership.
6. Hidden cargo, systems, occupants, routes, and capabilities remain non-inferable in every projection.
7. Lost responses, reconnect, Event gaps, stale versions, revocation, and duplicate requests recover deterministically.
8. Pack removal preserves readable historical results through exact snapshots and tombstones.

## 4. Authority boundaries

Ownership, custody, possession, control, access, usage, equipment, station authority, command authority, and location remain separate. Encounter approval cannot grant Asset authority. Vehicle command cannot infer ownership. Position cannot infer custody. UI visibility cannot infer permission.

## 5. Atomicity and ordering

Accepted operations create a single authoritative result group. Resource costs, quantity changes, durability, movement, Conditions, Effects, Vehicle systems, station state, and history commit together or not at all. Domain Events are ordered and replayable. Denied, expired, stale, cancelled, or duplicated requests produce no hidden side effects.

## 6. Hidden information

Authorization filtering occurs before search, counts, totals, route generation, range and target previews, capacity calculations, exports, diagnostics, notifications, logs, and optional-AI context. Hidden topology and hidden Assets never influence unauthorized aggregate values.

## 7. Accessibility

Combat, inventory, maps, and Vehicle operations provide equivalent list, table, outline, detail, station-roster, semantic-position, keyboard, touch, screen-reader, high-contrast, reduced-motion, responsive, and nonvisual workflows. No essential operation depends on dragging, canvas precision, hover, color, or animation.

## 8. Recovery and concurrency

All mutations use idempotency keys and expected versions. Lost responses require status lookup before retry. Event gaps use bounded snapshot-plus-tail repair. Revocation invalidates pending operations. Compensating Events preserve history and lineage.

## 9. Implementation slices

- CAIR-S01 — integrated aggregate and command routing.
- CAIR-S02 — atomic result coordination and Event ordering.
- CAIR-S03 — Asset, quantity, reservation, durability, and lineage adapters.
- CAIR-S04 — semantic map, movement, targeting, and hazard adapters.
- CAIR-S05 — Vehicle, station, system, carried-craft, boarding, and docking adapters.
- CAIR-S06 — permission-safe projections and accessibility parity.
- CAIR-S07 — reconnect, status lookup, Event-gap repair, and compensating undo.
- CAIR-S08 — deterministic integrated journeys, observability, and handoff.

## 10. Findings

Seven findings are resolved: duplicated cost ownership, authority conflation, hidden aggregate leakage, nested-Asset ambiguity, Vehicle/map divergence, reconnect duplication, and destructive undo. Zero blocking findings remain.

## 11. Decision

IA-D06 is complete and implementation-ready after P9 dependency gates. The next work item is **IA-D07-001 — MV-IA-F015 World and Setting Management**. `P9-06-008-attempt-002` remains unfinished and unmodified.
