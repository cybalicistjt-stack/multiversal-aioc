# IA-D06-004 — MV-IA-F014 Vehicle, Mecha, and Starship Operations

**Owner:** John Brandon Turner  
**Status:** complete-design-implementation-ready  
**Boundary:** basic internal-alpha operations; advanced construction, fleet logistics, autonomous AI command, and canonical promotion are deferred.

## Purpose

Define one server-authoritative operational model for vehicles, mecha, starships, mounts, and other crewed mobile Assets while preserving ownership, custody, control, station authority, combat timing, semantic positioning, hidden information, recovery, and accessible operation parity.

## Core model

A Vehicle Operation binds an Asset Instance to an operational profile, current condition, crew manifest, station assignments, controller grants, movement profile, power/fuel state, installed systems, cargo, passengers, and current Scene position. Ownership never implies control; custody never implies station authority; a station assignment never transfers ownership.

## Operational classes

Ground, water, air, space, submersible, walker, mecha, mount, hybrid, and abstract conveyance profiles share one contract. Each profile declares movement modes, scale, capacity, stations, crew minimums, system slots, Resource models, damage tracks, and environment constraints.

## Stations and authority

Pilot/driver, commander, navigator, gunner, engineer, sensor, communications, defense, medical, cargo, passenger, and remote-operator stations are explicit. A Character may hold multiple stations only when the profile permits it. Conflicting commands resolve by declared command policy, never UI order.

## Actions and timing

Vehicle Actions use the shared proposal/approval contract and the Full Combat Interface timing model. Movement, attacks, scans, repairs, power routing, docking, boarding, launching, evasive maneuvers, ramming, towing, and emergency procedures are server-validated against station authority, current state, Resources, topology, and expected version.

## Movement and positioning

Semantic zone, range-band, adjacency, facing, altitude/depth, velocity band, docking state, and interior/exterior position are authoritative. Canvas coordinates and animation are presentation only. Large-Asset occupancy, passenger positions, carried Assets, attached craft, and interior zones remain distinct projections.

## Systems, power, fuel, and heat

Installed systems have stable identities, source/version snapshots, readiness states, dependencies, damage state, and station bindings. Power, fuel, ammunition, charge, heat, stress, and maintenance are explicit Resources. Accepted results mutate them atomically with movement, attacks, Effects, Conditions, and Asset damage.

## Damage and failure

Damage may affect hull/frame, motive systems, power, sensors, weapons, stations, cargo, passengers, or environment seals. Disabled, immobilized, uncontrolled, adrift, breached, destroyed, abandoned, captured, and salvaged are distinct states. Zero hull never universally deletes the Asset or its history.

## Crew, passengers, and shared Assets

Crew assignment, boarding, disembarking, transfer of control, remote operation, lending, shared ownership, organizational ownership, and station reservations follow MV-IA-F008. Hidden occupants, cargo, systems, routes, and capabilities cannot leak through counts, totals, previews, exports, diagnostics, notifications, or optional-AI context.

## Recovery and concurrency

Commands require idempotency keys and expected versions. Lost responses require status lookup before retry. Reconnect uses current role-safe projection plus ordered Events. Revocation immediately removes station controls and invalidates protected caches.

## Accessibility

Every operational task must be available through list, table, station roster, system detail, semantic movement outline, keyboard, touch, screen reader, high contrast, reduced motion, responsive, and nonvisual interfaces. Precision canvas manipulation is never required.

## Implementation slices

1. Vehicle profile and instance projection.
2. Crew, station, and control grants.
3. Semantic movement and navigation.
4. Systems, power, fuel, heat, and ammunition.
5. Combat Actions, attacks, scans, and defenses.
6. Damage, failure, repair, boarding, and capture.
7. Recovery, hidden information, pack lifecycle, and provenance.
8. Accessible Player and GM operational surfaces.

## Acceptance

Twenty-eight blocking criteria require distinct authority dimensions, deterministic station command resolution, atomic outcomes, semantic positioning, hidden-information protection, recovery, provenance, pack lifecycle behavior, accessible parity, and preservation of `P9-06-008-attempt-002` as unfinished and unmodified.

## Next

IA-D06-005 — combat/Asset integrity matrix.