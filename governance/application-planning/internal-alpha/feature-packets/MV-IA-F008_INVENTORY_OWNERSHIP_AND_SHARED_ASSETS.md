# MV-IA-F008 Inventory, Ownership, and Shared Assets

**Work item:** IA-D06-002  
**Program:** MV-IA-001  
**Owner:** John Brandon Turner  
**Status:** implementation-ready design; dependency-gated  
**Version:** 0.1.0

## 1. Purpose

Define the bounded internal-alpha Asset runtime for acquiring, storing, equipping, transferring, sharing, using, damaging, repairing, crafting, salvaging, and reloading Assets without duplication, loss, authority confusion, or hidden-information leakage.

## 2. Governing principle

Asset Definition, Asset Instance, ownership, custody, control, possession, access, equipment, location, container membership, reservation, and usage permission are distinct. Only accepted durable commands and owning-domain Events change authoritative Asset state.

## 3. Alpha scope

The alpha supports personal inventory, Character equipment, party/shared inventory, containers, Scene Assets, shops, shared vehicles, consumables, currency-like Resources, transfer, lending, reservation, repair, simple crafting/salvage handoff, and combat use.

## 4. Dependencies

MV-IA-F002 Universal Object Experience, F004 Character, F005 Campaign/Scene/Session, F006 proposal/approval, F007 combat, F019 entitlements, F020 permissions, F021 recovery, IA-D04 shared decision/history contracts, and P9 persistence/migration/backup foundations.

## 5. Core records

- Asset Definition and exact source/version snapshot
- Asset Instance
- Ownership Interest
- Custody Assignment
- Control Grant
- Access Grant
- Container and Containment Edge
- Equipment Slot Assignment
- Quantity Lot and Stack
- Reservation or Hold
- Transfer Proposal and Receipt
- Usage/Consumption Record
- Condition, Damage, Durability, and Repair State
- Crafting/Salvage Work Order boundary
- Asset History Entry

## 6. Asset identity

Every instance has a stable Campaign-scoped identity. Quantity stacks represent compatible lots, not fungible identity by default. Split, merge, consume, transform, repair, and salvage preserve lineage and exact source provenance.

## 7. Ownership model

Ownership may be sole, joint, fractional, organizational, Campaign, or explicitly unowned. Ownership grants no automatic custody, physical possession, control, equipment, access, secrecy, or right to transfer. Shared ownership records named interests and decision policy.

## 8. Custody, possession, and location

Custody identifies the responsible holder. Possession and location identify where the Asset currently is. A Character may carry an Asset without owning it; an owner may not possess it. Scene, vehicle, container, shop, vault, evidence, and transit locations are explicit.

## 9. Control and usage

Control grants permission to operate or direct an Asset. Usage permission may be narrower than control and may require role, station, key, credential, training, attunement, charge, or owner consent. Vehicle use by multiple Players uses explicit crew/station grants rather than inferred shared control.

## 10. Containers and containment

Containment is an acyclic authoritative graph. Capacity, weight, volume, slot, compatibility, lock, seal, concealment, and nesting rules are profile-defined. Hidden contents are filtered before counts, search, totals, previews, exports, diagnostics, and AI context.

## 11. Quantities, stacks, and currency

Stacking requires compatible Definition/version, state, quality, provenance, ownership, restrictions, and lot policy. Currency may use Resource ledgers or Asset lots according to the bound profile. Transfers never silently convert between models.

## 12. Equipment

Equipment assignments bind Asset Instances to Character, participant, vehicle, or station slots. Slot eligibility, handedness, layering, attunement, readiness, quick access, and conflict rules are versioned. Equipping does not change ownership unless a separate transfer commits.

## 13. Acquisition and creation

Loot, purchase, reward, crafting, summon, duplication-authorized creation, import, and GM grant are distinct creation reasons. Every new instance requires a provenance-bearing Event and idempotency key. Client-side copies or repeated delivery cannot create duplicate Assets.

## 14. Transfer, lending, and sharing

Transfers specify sender authority, recipient, instances/lots, quantities, ownership change, custody change, control/access changes, consideration, conditions, and expected versions. Lending may change custody and access without ownership. Shared-party deposits and withdrawals follow declared approval policy.

## 15. Reservations and conflicts

Assets may be reserved for trade, crafting, repair, loadout, combat Action, vehicle station, or pending transfer. Reservations are bounded and attributable. Competing reservations, stale quantities, disconnects, and expiry are explicit; advisory holds never override durable state.

## 16. Use, consumption, and combat integration

Combat Actions reference exact Asset Instances, quantities, equipment state, ammunition/charges, durability, and reservations. Costs and consumption commit atomically with accepted Action results. Denied or failed-before-commit Actions do not consume authoritative Assets.

## 17. Damage, durability, repair, and maintenance

Damage state, durability, breakage, disabled state, repairability, maintenance, quality, and destruction are separate profile-defined fields. Zero durability does not universally delete an Asset. Repair and replacement use attributable Events and cannot erase prior damage history.

## 18. Crafting and salvage boundary

F008 owns Asset inputs, reservations, transformations, outputs, byproducts, and lineage. Long-running Project timing and research remain owned by F018. Crafting cannot consume inputs or create outputs until the owning work order commits atomically.

## 19. Shops, trade, and economic boundaries

Shop inventory, price offers, availability, ownership, custody, and transfer are explicit. Displayed price is not an accepted transaction. Social modifiers may alter offers through versioned adapters but cannot transfer Assets or currency without accepted inventory/economic commits.

## 20. Security and hidden information

Server-side projection filtering applies to existence, identity, quantity, owner, custodian, location, contents, properties, restrictions, value, provenance, damage, reservations, and history. Unauthorized users cannot infer hidden Assets through aggregate weight, slot counts, capacity, search, notifications, exports, diagnostics, or optional AI.

## 21. Accessibility and responsive presentation

Inventory operations support list, table, grouped, container-tree, equipment, detail, and nonvisual views with identical semantics. Drag-and-drop, color, icons, spatial placement, hover, or precision pointer actions are never required. Keyboard, screen-reader, touch, text scaling, high contrast, reduced motion, and mobile parity are mandatory.

## 22. Recovery, concurrency, and offline boundary

Every mutation uses idempotency keys and expected versions. Lost transfer, consume, equip, repair, or creation responses require status lookup before retry. Reconnect restores current role-safe inventory and Event gaps. Offline authoritative Asset mutation is prohibited; private loadout drafts require revalidation.

## 23. Pack, entitlement, export, and optional-AI lifecycle

Pack updates cannot rewrite live Asset Instances. Pack removal preserves snapshots and tombstones while disabling unavailable executable behavior. Entitlement loss does not erase Campaign history or ownership, but may restrict Definition detail or future use according to policy. AI may summarize authorized inventory or draft proposals only; it cannot reveal, transfer, consume, create, destroy, price, or promote Assets.

## 24. Implementation and acceptance boundary

Implementation proceeds through eight slices and twenty-four deterministic fixtures. All twenty-eight acceptance criteria are blocking. Design completion authorizes no paid service, credential, real-user data collection, application activation, internal-alpha release, deployment, public release, irreversible destruction, or canonical promotion. `P9-06-008-attempt-002` remains unfinished and unmodified.

## Implementation slices

1. Asset identity, Definition snapshots, instances, and lineage.
2. Ownership, custody, possession, control, access, and locations.
3. Containers, quantities, stacks, currency, and hidden projections.
4. Equipment, reservations, combat usage, costs, and consumption.
5. Transfer, lending, sharing, shops, and economic adapters.
6. Damage, durability, repair, crafting/salvage boundary, and lifecycle.
7. Accessible responsive UI, recovery, exports, diagnostics, entitlement, and AI boundaries.
8. Deterministic fixtures, acceptance harness, and map/vehicle handoff.

## Next work item

IA-D06-003 — bounded MV-IA-F013 Maps, Zones, and Tactical Positioning.
