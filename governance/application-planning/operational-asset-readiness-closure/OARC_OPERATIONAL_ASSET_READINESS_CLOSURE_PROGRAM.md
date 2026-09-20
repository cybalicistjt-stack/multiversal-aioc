# OARC — Operational Asset Readiness Closure

**Program ID:** OARC  
**Lane:** `oarc`  
**Status:** ACTIVE — OARC-04 SELECTED_NOT_STARTED  
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


## OARC-02 completed definition-bridge result

OARC-02 completed_verified on 2026-09-20. The application bridge resolves MRCS-13 definition-layer owner references to already-existing MIB-14 operational/module/facility definitions by exact stable ID + version. It does not synthesize MIB-14 definitions, mutate live Assets, infer operational kind from MRCS package kind, or allow MRCS authoring compatibility to override MIB-14 operational validation.

The current MRCS-13 package vocabulary is sufficient for this bridge without adding first-class `base`, `mecha` or `ship` package kinds: an MRCS `vehicle` or `construct` definition may reference an MIB-14 operational definition, while the resolved MIB-14 record remains authoritative for the concrete operational kind. `modular-component` resolves only to MIB-14 module/facility records.

The canonical owner-reference form is `mib14:<operational|module|facility>:<stable-id>@<version>`. Unknown references, version mismatches, unresolved source semantics and GM-adjudication-required records fail closed.

MRCS slot/component references and versioned authoring compatibility are preserved as authoring evidence. MIB-14 currently has no first-class typed slot-identity or component-identity field equivalent; OARC-02 records that as a visible representational gap rather than inventing operational semantics. Operational compatibility remains solely MIB-14 authority.

Causal RED: application validation run `35529025878` at `57f9a76db4c1fa3920b1ecca96b71ba8740e1005` failed because the bridge module was absent. Exact-head Linux/Windows/cross-platform GREEN: run `35529105470` at `44327d61ce5740748fac94d709ed20d740214e87`. Published application: PR #647 as `8cfcdb018483b615a426d2c524f1b8d6f154a084`.

Executor-process note: during this tranche the executor over-polled healthy workflow/platform state, contrary to OPS3-11 milestone-only instrumentation rules, and initially attempted a merge-commit method that the application repository disallows. No unauthorized protected-main mutation occurred. The exact validated head was ultimately published with the repository-supported squash method. The closeout records the OPS3-11 process deviation rather than asserting full execution conformance.

Fresh roadmap DAG schema 1.0.4 has no OARC override, so OARC-03 is the strict selected successor.


## OARC-03 completed catalog-normalization result

OARC-03 completed_verified on 2026-09-20. The application normalizer pins and classifies the governed operational-asset source catalogs without creating a replacement canonical catalog:

- Vehicles.csv — 1,200 rows — sha256 `2edd4f50d18d7d629c1a268122d1d4846e3df364da9b9c45f666359ba0dd791c`
- Mecha.csv — 2,117 rows — sha256 `60ff6a730f5a1d50dd4622da5d199be4f753b1933acfe9d087d5bf21b4a8bf0f`
- Spacecraft.csv — 2,311 rows — sha256 `00ce4a9d5730ac413d22813325ff3ace7e0c7b0445e9bcd0af45aa2911962c6f`
- Bases_Facilities.csv — 1,080 rows — sha256 `bfc80daf90be3f6b1f28e484cccc8333bb25bdc7fa66eb935e54e2b5f7c283cb`

Total governed source surface: 6,708 rows.

Normalization is classification and provenance preservation only. Explicit source record type controls routing. Vehicle/mecha/ship/base/facility candidates route toward MIB-14; support/item records route to MRCS-13; vehicle/mecha/ship rules-framework records route to PPIA-04/F014; unknown record types remain source-insufficient.

No owner definition, live Asset, compatibility relation, parent/component relation, installed relation, salvage output, capacity, system presence or operating envelope is inferred from names, grouping or missing data. MIB-14 ownerReference stays null until an exact existing-owner binding is established.

Rows containing inferred, estimated, best-judgment or completed values retain a mixed-provenance state. The Mecha Workshop representative case proves that populated fields are not automatically clean owner truth.

The initial test-first candidate's workflow was cancelled when the PR head advanced, so OARC-03 does not claim a causal RED receipt. Final exact-head validation run `35529945628` passed the complete governed Linux/Windows/cross-platform gate at `8cf854839d2a03252e96f78ad5525be1e809f3e6`. Application PR #650 then passed fresh-main no-overlap integration and published through READY as `501e4c5c5359d2368f4fb4c835416a35d77aa7e4`.

Fresh roadmap DAG schema 1.0.4 has no OARC override, so OARC-04 is the strict selected successor.
