# OARC — Operational Asset Readiness Closure

**Program ID:** OARC  
**Lane:** `oarc`  
**Status:** ACTIVE — OARC-02 SELECTED_NOT_STARTED  
**Approved:** 2026-09-20  
**Purpose:** bounded game-readiness integration and certification for vehicles, mecha, spacecraft/starships, bases/platforms and their modular content  
**Operational authority:** only through `operations/CURRENT.json`

## Mission

Make the existing operational-asset content genuinely game-ready without creating a second vehicle, engineering, construction, inventory, crafting, project, economy, combat or rules system.

OARC is a readiness/coverage closure lane, not a new canonical runtime family. It consumes existing owners and proves that their handoffs are complete enough for real source-backed content.

The governing chain is:

`MRCS definitions → MIB-14 operational configuration → D17 live Asset → MERA engineering/refit → MBES built-environment use`

Shared Action/Effect/Condition/Resource, Combat, Crafting/MIB-12, Economy/MIB-13, Project/APW-D26, World/Environment and other owner domains retain their existing authority.

## Authority boundaries

### MRCS / MRCS-13

MRCS owns reusable definition authoring for items, equipment, vehicles, constructs and modular components, including explicit/versioned slot, component and compatibility references. OARC may identify a narrow integration gap, but it does not create a parallel definition schema or silently reopen completed MRCS-13.

### MIB-14 + PPIA-04/F014 + D17

These remain the operational-asset foundation and live authority for vehicle/platform/base/mecha/ship definitions, configuration/operation foundations, Asset identity, ownership/custody, location, containment, condition and history.

OARC may close missing bridges, validators, source normalization and representative proofs around these contracts. It does not replace them.

### MERA

MERA owns engineering/refit orchestration and the engineering-resolution ladder:

`Asset → system → assembly → subassembly → component → interface/connection → governed network`

MERA also owns engineering topology inspection, interface/dependency/network/failure interpretation, diagnosis, disassembly planning, repair/refit orchestration, calibration, test/acceptance and target-specific Vehicle/Mecha/Starship engineering adapters.

OARC must not pre-implement those systems. Where game readiness reaches an engineering concern, OARC proves the handoff or records a MERA dependency.

### MBES

MBES owns built-environment and settlement gameplay, including:

`settlement/district → site/parcel → structure → level/zone → space/room → component/fixture → connection/network`

MBES owns construction, structural assembly, room/zone capability, infrastructure/facility networks, habitation and settlement development. OARC must not create a competing room topology, building construction engine, utility/network runtime or settlement system.

### Shared-owner rule

If a required fact belongs to another governed domain, OARC references or consumes that owner. It never creates a convenience duplicate ledger.

## Execution doctrine

One owner `Continue` carries one selected OARC tranche through the complete bounded tranche, required validation, durable closeout and successor selection unless an OPS3 owner-only boundary or genuine external blocker is reached.

Preload only the selected tranche and its declared dependency closure. Do not reopen unrelated roadmap work.

Unknown or source-unspecified semantics remain unresolved rather than inferred merely to improve coverage.

## Strict order

`OARC-01 → OARC-02 → OARC-03 → OARC-04 → OARC-05 → OARC-06 → OARC-07`

### OARC-01 — Authority & Handoff Contract

Freeze the ownership matrix and handoff semantics among MRCS-13, MIB-14/PPIA-04/F014/D17, MERA and MBES. Every new field or capability proposed by later OARC work must have one existing owner before implementation.

Acceptance includes explicit prevention of duplicate modular grammar, engineering topology/runtime and built-environment topology/runtime.

### OARC-02 — MRCS-13 ↔ MIB-14 Definition Bridge

Prove that authored reusable definitions, modular components, slots, compatibility profiles, unresolved states and owner references compile cleanly into MIB-14 operational definitions/configurations without duplicating records or inventing compatibility.

Explicitly verify whether the current MRCS-13 package-kind/owner-reference model already represents vehicle/platform/base/mecha/ship needs. If it does not, record only the narrowest owner-compatible integration requirement.

### OARC-03 — Catalog Normalization

Normalize the real source-backed Vehicles, Mecha, Spacecraft/Starship, Bases/Facilities and associated component/item catalogs into existing governed contracts with stable identity and provenance.

Classify incomplete source records without inventing missing game facts.

### OARC-04 — Operational Specialization Profiles

Establish and validate the minimum source-backed profile data required for ordinary vehicles, mecha, ships and bases to be playable through existing owners.

Specialized concerns such as mecha heat/energy, ship life support/hangars and base facility capability remain owner-backed profile data or explicit future-owner hooks, not new OARC runtimes.

### OARC-05 — Containment & Large-Asset Relationships

Prove stable-identity large-asset relationships such as carrier → craft, base → docked mecha, vehicle → cargo, and nested container → item.

Loading, docking, boarding, launching, transfer and removal change explicit relationships without implying ownership transfer. Arbitrary containment cycles and duplication must fail closed through the owning Asset/containment layer.

### OARC-06 — Game-Ready Golden Cases

Run source-backed golden cases for:
- ordinary vehicle;
- mecha;
- spacecraft/starship or carrier;
- fixed base;
- mobile base;
- nested carrier/craft or base/mecha relationship.

Each proof covers definition/configuration, live identity, crew/control where applicable, cargo/resources, operation/travel/combat participation, damage state, repair/project handoff, save/reload/reconnect and provenance without crossing MERA/MBES authority.

### OARC-07 — Coverage & Gap Certification

Audit all relevant source records and classify each as:
- game-ready;
- normalization needed;
- waiting on an existing owner;
- waiting on MERA;
- waiting on MBES;
- source-insufficient.

Produce the durable coverage ledger and final golden certification. Coverage percentage may never be improved by fabricated semantics.

## Initial golden references

Known source-backed reference cases include the existing ordinary MIB-14 vehicle/base proofs, Mecha records such as Hollowstep / Primax RX-07 and Veil Dancer / Falconex Skyray, and spacecraft records such as the Orrukhal Bastion-Class Carrier. Their use remains bounded by actual source fields; for example, installed modules are not automatically treated as salvage outputs when the source does not establish that.

## Non-goals

OARC does not:
- create another vehicle/mecha/starship/base engine;
- create another modular-component authoring grammar;
- create MERA engineering topology, dependency, failure, diagnosis, disassembly, refit or acceptance-testing engines;
- create MBES construction, room/zone, utility-network, facility-operation or settlement engines;
- invent source-absent component anatomy, compatibility, capacities, damage behavior, repair formulas or salvage outputs;
- collapse pilot/crew/occupant identity into machine Asset identity;
- duplicate Inventory/Asset, Project/time, Crafting, Economy, Combat, World or Action/Event authority.

## Completion condition

OARC closes only when real source-backed operational-asset catalogs can be deterministically classified and representative vehicle/mecha/ship/base cases can traverse the existing runtime and owner handoffs without duplicate identity, invented semantics, authority bleed or hidden future-family implementation.


## OARC-01 completed authority/handoff result

OARC-01 completed_verified on 2026-09-20. The machine-readable contract `OARC01.AUTHORITY_HANDOFF.v1` freezes the primary owner matrix and later-OARC field-admission gate.

The closure makes OARC a readiness bridge, validation and certification lane only. MRCS-13 retains reusable definition authoring; MIB-14 retains operational configuration foundations; D17/PPIA-03/shared-assets retain live Asset truth; PPIA-04/F014 retain vehicle/mecha/starship operational semantics; MIB-12, LSS, MIB-13/Economy, APW/D26, World/Environment/Reality and Action/Event/Combat/SCL retain their existing owner domains.

MERA and MBES remain owner-approved planned families with no current implementation authority. OARC may record dependencies and prove handoffs to them but may not implement MERA engineering topology/network/refit runtime or MBES construction/built-environment/settlement runtime early.

Every field or capability proposed by OARC-02 through OARC-07 must identify one existing primary truth owner, representation kind, source-truth state, mutation/handoff path and provenance. Missing owners remain explicit owner gaps; source-unspecified facts remain unresolved rather than defaulted or inferred.

Causal RED: Operations V3 run `35528399109` at `bda33506e54cc2b7b00e3a512840b7aaa9fd53e5`. Exact-head GREEN: run `35528464087` at `51bc5b586efd3088e5346ae3bfdc77373d2a4fe2`. Published contract: PR #1498 as `144769200adfcae9414c3af39c801a81d072abef`.

The fresh roadmap DAG contains no OARC override, so OARC-02 is the strict selected successor.
