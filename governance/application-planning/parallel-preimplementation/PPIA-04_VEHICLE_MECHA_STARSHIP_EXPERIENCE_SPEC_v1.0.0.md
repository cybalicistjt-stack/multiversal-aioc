# PPIA-04 — Vehicle, Mecha & Starship Experience Specification v1.0.0

**Work item:** PPIA-04  
**Status:** IMPLEMENTATION-READY DESIGN SPECIFICATION  
**Owner:** John Brandon Turner  
**Primary repository:** `cybalicistjt-stack/multiversal-aioc`  
**Application runtime mutation authorized by this document:** No  
**STAGE-A-A2 activation authorized by this document:** No

## 1. Purpose

PPIA-04 defines the implementation-ready Vehicle, Mecha & Starship experience without reopening completed Internal Alpha design. It binds reusable source Definitions, owned Campaign vehicle Assets, installed systems, crew/station authority, cargo and carried craft, Scene deployment, semantic movement, operational Actions, Resources, damage, repair, docking, boarding, launch, capture, salvage, provenance, privacy, recovery and accessible operation into one coherent contract.

The primary runtime authorities remain **MV-IA-F014 — Vehicle, Mecha, and Starship Operations**, **MV-IA-F013 — Bounded Maps, Zones, and Tactical Positioning**, **MV-IA-F007 — Action/proposal/approval**, **MV-IA-F020 — permission-safe projection**, and **MV-IA-F021 — recovery/idempotency**. Generic Item/Asset containment, transfer and lineage inherit PPIA-03 only where those semantics actually apply.

PPIA-04 does not authorize application implementation, release, deployment, tester access, paid services, credentials, production activation or deferred simulation work.

## 2. Authority and source basis

### 2.1 Structured content authority

The governed Vehicle domain is CSV-first and contains **three governed Vehicle-domain CSV datasets / 5,628 rows**: 1,200 Vehicles, 2,117 Mecha and 2,311 Spacecraft. The obsolete 487-object semantic database is not Vehicle-domain completeness authority.

The 8E-009 reconciliation rule remains binding: **name similarity cannot create** mecha/spacecraft component parentage or compatibility. Source-document grouping also cannot create such a relation without explicit evidence.

### 2.2 Retained source library

The retained source basis contains **24 retained Vehicle/Mecha/Spacecraft/Operations PDFs / 608 pages**. Exact source inventory and hashes are recorded in `PPIA-04_SOURCE_AND_DESIGN_INVENTORY.md`.

### 2.3 Recovered R1 evidence

PPIA-04 preserves **10 recovered R1 vehicle/system structural candidates** as source-review-only evidence. They receive zero automatic Definition promotion. A recovered heading is not a license to invent missing mechanics or runtime behavior.

### 2.4 Source-truth states

A field or relation may be source-backed, source-unspecified, conflicted, reference-only, inferred under governance, owner-delegated recommendation, Campaign-local state or live runtime state. These states stay distinguishable.

**Unknown is not zero.** Source-unspecified Resource quantity, capacity, compatibility, system presence or operating envelope is not zero, unlimited, empty, full, absent, compatible or available merely because the UI would otherwise look incomplete.

## 3. Fourteen semantic layers

PPIA-04 preserves fourteen identity/state layers. Implementations may package them differently internally, but may not collapse their meaning.

1. **Vehicle Definition** — stable reusable source identity, version, intrinsic mechanics and provenance.
2. **Definition configuration / variant** — source-backed class, variant, configuration alternative or conflict state.
3. **Component / system Definition** — reusable module, weapon, armor, drive, sensor or other system identity and compatibility evidence.
4. **Owned Campaign vehicle Asset instance** — one Campaign-scoped vehicle identity with ownership lineage.
5. **Installed configuration state** — installed component relationships, slots/hardpoints, readiness and configuration snapshot.
6. **Scene deployment / placement** — deployment state and semantic placement of the existing Asset.
7. **Live operational state** — encounter participation, operating mode, active conditions and expected version.
8. **Ownership / custody / control / access authority** — separate authority relations and grants.
9. **Crew / passenger / station state** — occupants, assignments, reservations, command policy and controller grants.
10. **Cargo / containment / carried craft** — cargo Assets, containers, passenger capacity where governed, hangar relations and attached/carried craft.
11. **Damage / condition / failure** — hull/frame, motive, power, sensors, weapons/systems, stations, seals and governed failure states.
12. **Resources / power / fuel / heat / maintenance** — current governed Resources, capacities when known, bounded allocation modes, heat/stress and service state.
13. **Movement / position / environment / docking** — semantic zone/anchor, range, adjacency, facing, altitude/depth, velocity band, environment constraints and docking/boarding relations.
14. **Provenance / history / recovery** — source coordinates, conflicts/recommendations, ownership/configuration/damage/crew history, operation IDs, versions and recovery receipts.

Definition inspection cannot mutate a Campaign vehicle. Scene deployment cannot clone one. Station assignment cannot transfer ownership. Installation cannot silently transfer component ownership.

## 4. Vehicle Inspector and projection model

`PPIA-04_VEHICLE_INSPECTOR_PROJECTION_MATRIX_v0.1.0.json` defines fourteen field groups matching the layers above and fourteen bounded action contracts:

- `inspect_compare`;
- `acquire_transfer_control`;
- `configure_install_uninstall`;
- `assign_station`;
- `load_unload_transfer`;
- `deploy_recall`;
- `move_navigate`;
- `attack_scan_operate`;
- `route_power_manage_resource`;
- `apply_damage_repair`;
- `dock_board_launch`;
- `capture_salvage`;
- `reveal_hide`;
- `history_export_recovery`.

Every projection authorizes before existence, fields, rosters, counts, totals, system lists, capability summaries, routes, Resource summaries, provenance, history, exports, diagnostics, notifications or AI/service context are serialized or aggregated.

Hidden occupants, cargo, carried craft, installed systems, routes, capabilities, Resources and provenance are removed before aggregates. An unauthorized viewer must not infer hidden state from a changed count, used/free capacity, vacancy indicator, readiness total, error string, comparison result or AI summary.

## 5. Contexts and surfaces

The same governed vehicle may appear across:

- Library/reference browse and compare;
- Vehicle Inspector;
- garage/hangar/fleet management;
- configuration/loadout and component installation;
- crew/passenger/station assignment;
- cargo/passengers/carried craft;
- Scene deployment and recall;
- Player station operation;
- GM/NPC vehicle operation and approval;
- semantic navigation/movement;
- combat systems and scanning;
- Resource/power/fuel/ammunition/heat/maintenance;
- damage/failure/repair/recovery;
- docking/boarding/launch;
- capture/salvage/transfer;
- provenance/history/export/recovery.

Context changes presentation and authorized commands, not source identity.

## 6. Integrated workflow set

`PPIA-04_WORKFLOW_AUTHORING_CONTRACT_MATRIX_v0.1.0.json` defines **15 integrated workflows**.

### VS-WF-001 — Library / Vehicle Definition reference
Read-only Definition, variant and component inspection/compare. Selection is provisional and revalidated by the destination workflow.

### VS-WF-002 — Garage / Hangar / Fleet authority
Manages explicit ownership, custody, control and access deltas. Ownership never silently grants pilot/station control.

### VS-WF-003 — Configuration / install / uninstall
Validates explicit parent/compatibility evidence, slot/hardpoint and current version. Name similarity and document grouping cannot create compatibility.

### VS-WF-004 — Crew / passenger / station assignment
Assigns, reserves, releases or revokes stations using explicit authority and declared command policy. UI arrival order is not authoritative.

### VS-WF-005 — Cargo / passengers / carried craft
Loads, unloads, transfers, attaches or detaches exact Assets. Generic containment/lineage inherit PPIA-03; vehicle carriage, hangar and deployment semantics remain PPIA-04.

### VS-WF-006 — Scene deploy / recall
Deploys an existing vehicle Asset into a Scene using semantic placement. Deployment never creates duplicate identity.

### VS-WF-007 — Player station operation
Presents only controls permitted by current station/control authority and submits commands through F007/F014.

### VS-WF-008 — GM / NPC vehicle operation and approval
Lets authorized GM/delegated Assistant GM inspect actor, vehicle, system, target and result, then approve, deny or perform governed adjustment under the shared Action contract.

### VS-WF-009 — Semantic movement / navigation
Uses authoritative semantic origin/destination, adjacency/range, facing, altitude/depth, velocity band and environment constraints. Canvas pixels are presentation unless a rules profile explicitly binds them.

### VS-WF-010 — Combat system attack / scan / operate
Routes system Actions through F007 and commits accepted output and governed Resource costs atomically.

### VS-WF-011 — Power / fuel / ammo / heat / maintenance Resources
Supports only bounded governed Resource operations. Source-unspecified capacities remain unknown and detailed circuit/power-grid simulation is not implied.

### VS-WF-012 — Damage / failure / repair / service
Applies profile-bound damage/failure consequences and service/repair without erasing Asset identity, ownership lineage or prior history.

### VS-WF-013 — Docking / boarding / launch / attach
Uses explicit semantic relations. Visual overlap is never sufficient evidence of docking or boarding.

### VS-WF-014 — Capture / salvage / custody / ownership transfer
Separates capture, custody and control from ownership lineage. Salvage does not erase provenance or prior damage history.

### VS-WF-015 — Provenance / history / export / recovery
Filters before export, preserves source/conflict/history distinctions and resolves ambiguous mutation outcomes by operation-status lookup before retry.

## 7. Cross-domain handoffs

The workflow matrix defines **10 cross-domain handoff contracts** (`VS-HO-001` through `VS-HO-010`). Handoffs carry stable IDs, exact semantic context and minimum authorized state. A receiving workflow does not inherit authority merely because another surface authorized a read or proposal.

Key boundaries are:

- Library/Inspector selection remains provisional until the destination reauthorizes.
- 8E-009 owns evidence requirements for parent/compatibility reconciliation.
- PPIA-03 owns generic Item/Asset containment, transfer and lineage where applicable.
- F007 owns shared Action proposal/approval/result behavior.
- F013 owns semantic positioning contracts.
- F014 owns vehicle-specific operational authority, stations and governed vehicle commands.
- F020 owns permission-safe projection and non-inference.
- F021 owns expected-version, idempotency, reconnect and ambiguous-network recovery.

## 8. Ownership, custody, control and station authority

Ownership, custody, possession/control, access, remote-operation grant, passenger status and station authority are independent. A vehicle owner is not automatically pilot/driver. A pilot does not become owner. A station assignment grants only the station authority declared by the governing policy.

Revocation immediately removes protected controls and invalidates protected caches/prefetched hidden route, system and Resource data. Conflicting authorized crew commands resolve through the declared command policy and current authoritative version, never client arrival order.

## 9. Components, systems and configuration

Component Definition identity is distinct from installed relation/state. Installation requires explicit governed compatibility evidence or an explicit unresolved/blocked result. Same names do not create parentage. Source-document proximity does not create parentage.

Installed-system projections filter unauthorized systems before counts, hardpoint summaries, readiness totals, capability tags, action menus, diagnostics, exports and AI context. Installation/uninstallation changes configuration state and history, not reusable source Definition identity and not component ownership unless a separate authorized transaction does so.

## 10. Cargo, passengers and carried craft

Cargo, passengers, containers and carried/attached craft retain stable identities. A carrier and carried craft remain separate Assets. Launch changes explicit carried/deployment relations and never clones the craft.

Capacity is enforced only where a governed capacity model exists. Unknown capacity is not zero or unlimited. Hidden children are filtered before used/free capacity, counts, weights, values, search facets, exports or summaries.

Containment must remain acyclic. All drag-oriented flows also provide semantic **Load**, **Unload**, **Move to**, **Attach**, **Detach** or equivalent non-drag commands.

## 11. Scene deployment and semantic movement

Deployment references the existing owned Asset. The authoritative movement model is semantic: zone/anchor, range band, adjacency, facing, altitude/depth, velocity band, movement mode and environment constraints as supported by the active rules profile.

Canvas coordinates, drawn path length and visual overlap are presentation unless explicitly rules-bound. Every movement flow has a list/table alternative exposing origin, destination, valid relations, constraints, costs and command outcome.

Accepted movement and applicable Resource costs commit atomically. A stale or denied command changes neither authoritative position nor Resources.

## 12. Operational Actions and GM approval

Vehicle attacks, scans, defenses and other governed system operations use F007/F014. The server reauthorizes actor/station/system/target immediately before mutation. System output and Resource costs share one authoritative operation boundary.

A denied or failed-before-commit operation consumes nothing. Failure text cannot reveal hidden system existence, target information or capability.

GM operation and approval surfaces show the authorized actor, vehicle, action/system, target, roll/result and pertinent governed context. Delegated Assistant GM authority cannot exceed the delegation.

## 13. Resources, power, fuel, ammunition, heat and maintenance

Current value, known governed maximum and unknown/source-unspecified maximum are distinct states. Supported operations may include bounded consumption, refuel/recharge/reload, maintenance/service and coarse power-allocation modes where explicitly defined.

Detailed topology is not inferred from coarse data. A source record that mentions power does not automatically create a circuit simulation. Accepted Resource mutations use expected-version/idempotency protection and append attributable history where required.

## 14. Damage, failure, repair and service

Damage surfaces are profile-bound and may distinguish hull/frame, motive, power, sensors, weapons/systems, stations and environmental seals. Disabled, immobilized, adrift, destroyed, captured and salvaged remain governed states rather than universal deletion instructions.

Zero hull/frame does not universally erase the Asset, Definition reference, ownership lineage or provenance. Repair/service modifies authorized instance/runtime state and appends history; it does not rewrite source facts or erase prior damage.

## 15. Docking, boarding, launch and attachment

Docked, boarded, carried/attached, interior/exterior and launched are explicit semantic relations. A visual token touching another token is not docking.

Before commit, the owning workflow revalidates vehicle/Scene authority, semantic relation, relevant station/boarding authority and current versions. Boarding, launch and detach operations update all governed relations atomically and preserve both vehicle identities.

## 16. Capture, salvage and transfer

A governed capture can change custody/control without silently rewriting historical ownership. Salvage can create explicit ownership/custody/Asset deltas under an authorized transaction, while provenance, source identity and prior damage history remain traceable.

Transaction-private details remain limited to authorized participants/GM scope. Hidden cargo, systems or occupants are not exposed merely because custody/control changed.

## 17. Privacy and service/AI projection

Authorization occurs before existence/search, roster construction, counts, readiness/capability summaries, cargo/occupancy totals, routes, Resources, history, provenance, exports, diagnostics, notifications and AI/service retrieval.

GM authority is Campaign-scoped, not universal access to user-private or other-Campaign data. Assistant GM projections are delegation-scoped. Creator/Owner/Admin authoring authority does not merge source authoring and live Campaign mutation paths. Service/AI actors receive the minimum authorized projection and no independent command, movement, attack, reveal, transfer, power-route or canonical-promotion authority.

## 18. Recovery, concurrency and reconnect

Every authoritative vehicle mutation uses an operation identity and expected-version or equivalent concurrency boundary. **No broad offline authoritative vehicle mutation** is permitted.

If the network result is ambiguous, the client queries operation status using the original operation ID before retry. A retry reuses the same idempotency identity. It cannot duplicate movement, Action output, Resource spend, damage, repair, docking, launch, deployment, load/unload, transfer or capture/salvage effects.

Reconnect reauthorizes current Campaign, role, grants, station authority, visible systems, vehicle version, Scene state and lifecycle. Cached revoked or hidden state cannot restore authority.

## 19. Responsive and accessible operation

Expanded layouts may show multi-column system, crew, Resource, cargo and history regions. Medium and compact layouts prioritize vehicle identity, current station, operational state, alerts and the primary command while collapsing secondary regions without losing meaning.

All core workflows support keyboard and touch. Screen-reader output announces vehicle identity, semantic layer/context, station authority, system readiness, Resources with units or unknown state, semantic position, damage/failure state, validation errors and authoritative operation result.

High zoom reflows tables to labelled rows/cards. Reduced-motion users receive state changes in text rather than requiring animation. Drag, hover, color, animation, map memory, spatial canvas and pointer precision are never the sole method for completing a vehicle workflow.

## 20. Reference-case acceptance corpus

`PPIA-04_REFERENCE_CASES_v0.1.0.json` contains **20 reference cases**: 9 contract-grounded, 8 synthetic QA and 3 guardrail cases, with zero canonical synthetic records.

The corpus covers Definition/instance separation, variants, explicit component evidence, no name-similarity auto-link, owner-versus-pilot separation, crew command conflicts, hidden aggregate protection, carried craft, semantic movement, Action/Resource atomicity, source-unspecified values, damage identity preservation, repair history, docking/boarding/launch, capture/salvage, hidden installed systems, ambiguous-network recovery, station revocation, nonvisual operation and deferred-feature isolation.

## 21. Explicitly deferred capabilities

PPIA-04 preserves the IA-D08-003 deferral boundary. The following are not activated by this specification:

- continuous Newtonian flight;
- full orbital mechanics;
- subsystem circuit simulation;
- real-time station concurrency at scale;
- detailed power-grid routing;
- structural finite-element damage;
- atmospheric transition simulation;
- carrier fleet command;
- autonomous drones;
- programmable vehicle AI;
- full synchronized interior/exterior geometry;
- unrestricted custom processors.

Unknown or extension data for these features may be preserved opaquely/versioned, but UI and validators must not claim operational support merely because such data exists.

## 22. Implementation boundary

An implementation conforming to PPIA-04 must preserve the fourteen semantic layers, fourteen action contracts, fifteen workflows, ten handoffs and twenty reference cases while enforcing permission-before-projection, server-authoritative mutation, expected-version/idempotency recovery, source-state distinctions, semantic movement and accessible equivalents.

PPIA-04 completion does **not** alter raw source CSVs, promote R1 candidates, activate deferred simulation, activate STAGE-A-A2, mutate application runtime, authorize production credentials or authorize release/deployment/tester operations.

The acceptance contract is `PPIA-04_ACCEPTANCE_TRACEABILITY_MATRIX_v0.1.0.json`. The completion gate is deterministic and must pass on the exact pull-request head before a `completed_verified` claim can be made.