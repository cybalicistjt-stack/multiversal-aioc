# PPIA-04 — Vehicle, Mecha & Starship Source and Design Inventory

**Work item:** PPIA-04 — Vehicle, Mecha & Starship Experience  
**Status:** IN PROGRESS — FOUNDATION INVENTORY  
**Owner:** John Brandon Turner  
**Repository branch:** `governance/ppia-04-vehicle-mecha-starship`

## 1. Authority boundary

PPIA-04 deepens the already-approved Internal Alpha vehicle operations model. It does not revive the obsolete 487-object semantic-parse database, invent missing source facts, or replace PPIA-03 Asset/inventory contracts.

Use authority in this order:

1. current repository governance and Internal Alpha contracts, especially MV-IA-F014, F013, F008, F007, F020 and F021;
2. the governed 8E-009 CSV-first Vehicle domain and final 20-dataset/19,199-row reconciliation;
3. retained Vehicle/Mecha/Spacecraft source PDFs for exact source truth;
4. PPIA-01 provenance/inference distinctions;
5. recovered 8E-008G-R1 deferrals only as source-accountability candidates, never automatic canonical vehicle/system Definitions;
6. PPIA-03 Item/Asset contracts for cargo, components, equipment, ownership, containment, lineage and transactions where those semantics actually apply.

## 2. Retained source library

The retained direct Vehicle/Mecha/Spacecraft/Operations library contains **24 PDFs / 608 pages** in `MV_Master_01_Core.zip`.

| Source | Pages | SHA-256 |
|---|---:|---|
| `Stealth class.PDF` | 8 | `051933eaf1114d6656ebdd05957d859899110465f1262444ad74cf028e233ef0` |
| `Assault class.PDF` | 10 | `c35bc928816f35c79e3570ccaa46ae49e0b65dc9c0b7adc65523e1f855d7a515` |
| `Escort class(1).PDF` | 9 | `8a6afdfd05b6fac631e04fefa63e853daba8f3cdcd888fc27c942d6e54863489` |
| `Carrier Class.PDF` | 8 | `ea5e6dcab4e27e3bb8bfeb1069248792dc979259395c9f4cad31399531ead150` |
| `Explorer class.PDF` | 9 | `3c598f968c34f5dcbe53ff4663150dc82d3f23c96c2165a389376d1ccac90980` |
| `Mecha Hangars v2.PDF` | 54 | `f6a3d77ebb5590c91fcb513810b967c3b22364ed57de2552591a9652b34e9cc3` |
| `Seafaring vehicles.PDF` | 2 | `e1b9f31674a28eb9218705b4cd96d9f571abf7cd71a5daf8d20b75b5cea7290f` |
| `Ship classes overview.PDF` | 3 | `1e124c7ef8d871783f125623326e520397c2d64a2eb7edfe8c1f914ddaf955d7` |
| `Seige class.PDF` | 9 | `b316dcbf2087378dd1954fbdadde441a70c38f5643d172ea2cb4188baa67d0dd` |
| `Ship comp stats 11-7-24.PDF` | 20 | `d8d5f20697c9205d0b5373647acc8ecd4d5445048d460d49d7d4cef06aa288b0` |
| `Hybrid class.PDF` | 11 | `f12169c0d7eaa969a4d77ac360b55c1c148b46fea925605f237b9571176d3158` |
| `Space Ships List vAlpha.PDF` | 212 | `c46c6b6b6a550fc8a6e0261c9c73eed676107ec43bded2321465f321d3e88fc5` |
| `Mounts.PDF` | 15 | `90061aefaa7a0a1c8503be207099123948605f967987ac777847d19857eb6593` |
| `Command class.PDF` | 10 | `cbf82924bdb89252b2c6b2db34ef678ef747dc21d4006f2782bffa43804d5cb8` |
| `Logistics class.PDF` | 8 | `769e1618beb135e9afcfe8e0349fc588ffb45cd00245a90815429c9a15359af3` |
| `Mecha List.PDF` | 86 | `e8185c780571e090ef74f4c8fc0732cb22f6d00a05302eb366ebece2522b05fc` |
| `Wheelchairs 12-11-24.PDF` | 8 | `ff494241d2f6cf605f34fc3f6dd9533424f9212135b5cd058f3534267e3eb85e` |
| `Mecha 11-7-24.PDF` | 39 | `e942634e4371088de98f862fb0fcbf72824f7b84c564dfac8b21bc0bc9fb2bc7` |
| `Interceptor class.PDF` | 8 | `1a0672fd09bc7e6ea201bbc0d0af4938176511379329f550bb010707b951b132` |
| `Patrol class.PDF` | 9 | `eb50cd8aed4abd5a8af41c0b8cf9d88c9228a4582666aa14eb52cd2a1207683d` |
| `Vehicles 2-7-25.PDF` | 15 | `ae8079f7b69432c2a8cc0cc5e5008d229cff6d3d8204c314fc96414af586b9dd` |
| `Civilian vehicle gameplay 11-25-24.PDF` | 5 | `02435fc249dc153194627860b157cecf953d587a7884342e1427fa2ed8e38e4f` |
| `Entry class.PDF` | 7 | `6341c6c76e989e987471a18753d0ee6c9f4686a85dc9bbc98e39c573ff26c602` |
| `Vehicles & Operations.PDF` | 43 | `8eac372414eb74efa19ebfdfd954762cdd82f01a71c7563335c0c0f4998ba219` |

These hashes identify the exact retained copies used for PPIA-04 source inventory. They do not by themselves promote or repair content.

## 3. Governed CSV Vehicle surface

`CSV_VEHICLE_DOMAIN_BATCH_CONTRACT.json` defines exactly three Vehicle-domain datasets totaling **5,628 rows**. The original contract explicitly preserves raw source/unmapped columns, forbids cross-domain coercion and silent defaults, and originally staged with no canonical-ID/promotion authority.

### Vehicles — 1,200 rows

Retained CSV: `Vehicles.csv`  
SHA-256: `2edd4f50d18d7d629c1a268122d1d4846e3df364da9b9c45f666359ba0dd791c`

Record types:

- 953 `Vehicle`
- 239 `Vehicle Module`
- 3 `Support Equipment`
- 3 `Consumable Supply`
- 1 `Service Facility`
- 1 `Service Package`

The dataset covers land, water, air, amphibious, underwater and cross-domain vehicle profiles and includes crew, passenger, cargo, movement, durability/armor, module slots, power, fuel/energy, operation, maintenance, failure, cost, upgrades and environment fields.

### Mecha — 2,117 rows

Retained CSV: `Mecha.csv`  
SHA-256: `60ff6a730f5a1d50dd4622da5d199be4f753b1933acfe9d087d5bf21b4a8bf0f`

Record types:

- 1,080 `Original Mecha Component`
- 900 `Original Mecha`
- 87 `Source Mecha Component`
- 30 `Named Mecha`
- 20 `Rules Framework`

Major component families include weapons, mobility, armor/defense, capacitors, power cores, sensors/recon, utility/repair and interface/control. The current `MECHA_TEMPLATE_REGISTRY.json` already distinguishes a mecha frame from a mecha component and requires explicit compatibility evidence rather than name similarity.

### Spacecraft — 2,311 rows

Retained CSV: `Spacecraft.csv`  
SHA-256: `00ce4a9d5730ac413d22813325ff3ace7e0c7b0445e9bcd0af45aa2911962c6f`

Record types:

- 960 `Original Spacecraft`
- 900 `Original Ship Component`
- 186 `Ship Component`
- 111 `Class Module`
- 81 `Named Spacecraft`
- 60 `Class Archetype Spacecraft`
- 13 `Ship Class Framework`

Major component/system families include shields, engines/reactors, weapons, armor, heat dissipators, stealth modules, computers, sensors, hangars, utility modules and FTL systems. The table also carries crew/passenger/cargo, hull/shield/armor, movement, sensors, power, fuel/endurance, FTL, hardpoints, weapons, maintenance, failure and upgrade fields.

## 4. Parent/component identity boundary

`CSV_VEHICLE_PARENT_RECONCILIATION_CONTRACT.json` is controlling evidence for mecha/spacecraft component relationships:

- deterministic parent links require explicit parent references;
- name similarity cannot create a parent link;
- source-document grouping is candidate evidence only;
- cross-dataset parent links require source evidence;
- ambiguous or absent relationships remain unresolved until source verification/governed resolution.

PPIA-04 therefore treats a component Definition, a compatibility rule, an installed component relation and a vehicle configuration as separate concepts.

## 5. Existing Internal Alpha operational authority

### MV-IA-F014 — Vehicle, Mecha, and Starship Operations

F014 is already `complete-design-implementation-ready` for the bounded Internal Alpha operational model. It establishes:

- one server-authoritative operational model for vehicles, mecha, starships, mounts and other crewed mobile Assets;
- ownership distinct from custody/control/station authority;
- explicit pilot/driver, commander, navigator, gunner, engineer, sensor, communications, defense, medical, cargo, passenger and remote-operator stations;
- shared proposal/approval timing for movement, attacks, scans, repairs, power routing, docking, boarding, launching, evasive maneuvers, ramming, towing and emergency procedures;
- semantic zone/range/adjacency/facing/altitude/depth/velocity/docking/interior-exterior positioning;
- installed-system identity, readiness, dependencies, damage and station binding;
- explicit power/fuel/ammunition/charge/heat/stress/maintenance Resources;
- distinct hull/frame, motive, power, sensor, weapon, station, cargo, passenger and environmental-seal damage/failure surfaces;
- idempotency/expected-version recovery and role-safe reconnect;
- accessible list/table/station-roster/system-detail/semantic-movement alternatives.

PPIA-04 must deepen the user experience around these contracts rather than redesign their authority model.

### MV-IA-F013 — Bounded Maps, Zones, and Tactical Positioning

F013 makes semantic position authoritative. Vehicle footprints, crew stations and attached/carried craft are typed adapters; pixels/canvas coordinates remain presentation unless a rules profile explicitly binds them. Positioning does not itself own vehicle damage, fuel, actions or ownership.

### MV-IA-F008 and PPIA-03

F008/PPIA-03 own reusable Asset-instance, ownership/custody/access, containment, quantities, transfer, lineage, permission and recovery primitives. PPIA-04 reuses those primitives for vehicle ownership, cargo and component Assets, but vehicle crew/stations, movement, damage systems, power, docking/boarding and deployment remain PPIA-04 semantics.

### F007 / Combat and Action approval

Vehicle attacks and operational commands enter the same governed Action/proposal/approval/event model. UI controls do not directly mutate authoritative Resources, position or damage.

### F020 / F021

Permissions filter before projection/aggregation. Recovery uses idempotency, expected versions and current role-safe state. Hidden occupants, cargo, systems, routes, capabilities and resources must not leak through counts, totals, previews, notifications, exports, diagnostics or AI context.

## 6. Explicit advanced-feature deferrals

`IA-D08-003_ADVANCED_MAP_VEHICLE_DEFERRAL_PACKAGE.md` keeps these outside the bounded Internal Alpha/PPIA-04 implementation target:

- continuous Newtonian flight;
- full orbital mechanics;
- subsystem circuit simulation;
- real-time crew-station concurrency at scale;
- detailed power-grid routing;
- structural finite-element damage;
- atmospheric-transition simulation;
- carrier fleet command;
- autonomous drones;
- programmable vehicle AI;
- full synchronized interior/exterior geometry;
- unrestricted custom vehicle processors.

PPIA-04 may preserve opaque/versioned extension data and future seams, but cannot make deferred features appear operational when they are ignored.

## 7. Recovered R1 vehicle/system deferrals

PPIA-03 cross-domain triage identified **10 recovered R1 structural candidates** as vehicle/system context. They are preserved in `PPIA-04_R1_DEFERRED_VEHICLE_SYSTEM_CANDIDATES.csv`.

The headings include an armored transport and several weapon/armor/system headings. They are **source-review candidates only**. A heading does not create a new vehicle, component or weapon Definition, and no missing mechanics are synthesized from the heading text.

## 8. PPIA-04 identity/state problem space

The user experience must keep at least these layers distinguishable:

1. reusable Vehicle/Mecha/Starship Definition;
2. source-backed variant/class/configuration Definition;
3. component/module/system Definition;
4. owned Campaign vehicle Asset Instance;
5. installed component/configuration state on that instance;
6. Scene/deployment placement;
7. live Session/encounter operational state;
8. ownership/custody/control/access authority;
9. crew/passenger/station assignments and reservations;
10. cargo/containment and carried/attached craft;
11. hull/frame/subsystem damage/condition/failure;
12. fuel/power/ammunition/charge/heat/stress/maintenance Resources;
13. movement/position/environment/docking/boarding state;
14. provenance/history/recovery.

These layers may share UI panels but must not collapse into one mutable vehicle record.

## 9. Initial experience contexts

PPIA-04 must support a coherent role-safe vehicle through:

- Library/reference browse and compare;
- Vehicle/Mecha/Starship Inspector;
- owned vehicle garage/hangar/fleet list;
- configuration/loadout/component management;
- cargo, passengers and carried craft;
- crew/station assignment;
- deployment into a Campaign Scene;
- Player pilot/station operational view;
- GM vehicle/encounter operational view;
- semantic navigation/movement;
- combat systems/actions/defenses;
- power/fuel/resource management;
- damage/failure/repair/recovery;
- docking/boarding/launch/capture/salvage;
- provenance/history/conflict/variant inspection;
- accessible nonvisual equivalents.

## 10. Cross-domain routing

PPIA-04 owns vehicle-specific semantics but routes rather than invents:

- personal Items, cargo lots, ordinary inventory transfer and generic Asset lineage → PPIA-03;
- species/forms/host biology and biological transformations → PPIA-05;
- Campaign/Scene authoring depth → PPIA-08;
- encounter/balance calibration → PPIA-11;
- world-specific vehicle classes, manufacturers, cultures and extensions → PPIA-12.

## 11. Foundation boundary and next substep

This inventory does not modify raw CSVs, promote R1 candidates, invent component-parent links, implement runtime code, activate A2, or authorize release/deployment.

The next bounded PPIA-04 step is to formalize the 14-layer identity/state model into a machine-verifiable experience taxonomy with presentation profiles, authority/resource invariants, component/cargo/crew/station distinctions, retained-vs-deferred capability rules, and explicit PPIA-03/F013/F014 handoffs.
