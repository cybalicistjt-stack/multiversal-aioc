# MERA — Multiversal Engineering, Refit & Assembly

**Program ID:** MERA  
**Status:** OWNER-APPROVED — PLANNED FUTURE INTERSTITIAL  
**Activation:** after MRCS-21  
**Successor:** MBES-01  
**Owner and final authority:** John Brandon Turner  
**Approved:** 2026-09-11  
**Implementation authority:** none

## Purpose

MERA turns Multiversal's existing Asset, Item, crafting, salvage, vehicle, mecha, spacecraft, Project, Profession, economy and rules/content systems into one coherent player/GM engineering experience.

The governing gameplay loop is:

**inspect → diagnose → design/propose → source/salvage/fabricate → isolate/disassemble → repair/replace/modify → install/reassemble → calibrate → test → accept/return to service**

MERA is not a second inventory ledger, crafting engine, salvage engine, vehicle engine, Profession system or rules database. It orchestrates owner-authorized operations across those systems.

## Core product promise

A Character can work on a complex Asset at the resolution the Asset actually supports. A rifle, suit of powered armor, magical device, industrial machine, robot, construct, car, tank, aircraft, mecha, spacecraft or starship may all use the same engineering workflow while exposing different governed systems, interfaces and constraints.

MERA does **not** require 3D rendering or a physics sandbox. Its authoritative engineering representation is schematic and semantic. Presentation may use diagrams, portraits, exploded views or future 3D renderers, but those are optional projections.

## Engineering-resolution ladder

MERA preserves a scalable semantic ladder:

**Asset → system → assembly → subassembly → component → interface/connection → governed network**

A definition may stop at any level. MERA must not invent lower-level detail merely to make an engineering UI look complete.

Examples:

- a simple sword may expose blade, hilt and one enchantment interface;
- a powered suit may expose armor sections, power, locomotion, life support and hardpoints;
- a mecha may expose frame, motive systems, armor, weapons, sensors, power, heat, stations and internal subsystems;
- a starship may expose hull sections, drives, power, fuel, atmosphere, sensors, weapons, cargo, carried craft and other governed systems.

Expanding or collapsing engineering detail never creates a second Asset identity and never discards authoritative condition, provenance or history.

## Existing authorities MERA consumes

- **LSS:** recoverable objects, decomposition, partial stripping, salvage, scavenging, donor components, cannibalization lineage and salvage provenance.
- **PPIA-03 / D17:** Item/Asset identity, ownership, custody, location, containment, condition, durability, installation/modification and history.
- **MIB-12:** crafting, modification, repair, refurbishment and transformation transactions.
- **MIB-13:** prices, services, markets, trade and economic consequences.
- **MIB-14:** vehicle/platform/base definitions, module/facility compatibility, capacity/loadout, resource hooks, maintenance, damage, repair and upgrade foundations.
- **PPIA-04 / F014:** vehicle, mecha and starship configuration, systems, stations, resources, damage, repair, operational state, capture and salvage handoffs.
- **APW/D26:** Projects, tasks, phases, prerequisites, participants, time, cancellation and long-running work.
- **DPL / Profession owners:** engineer, mechanic, technician and other work capabilities, learning and life/profession context.
- **MRCS:** reusable engineering definitions, component/interface profiles, compatibility rules, work recipes, blueprints and system-extension content.
- **ARI:** imported/generated media/resource identity, rights and provenance.

## Benchmark lessons

The clean-room benchmark set includes Hardspace: Shipbreaker, BATTLETECH/MechWarrior-style refit and salvage loops, MegaMekLab/MekHQ/MekBay, Armored Core, Crossout, From the Depths, Space Engineers, TerraTech, Pacific Drive, My Summer Car, Ostranauts, Cosmoteer, EVE fitting/Pyfa, No Man's Sky ship salvage/building, Starfield ship construction, Kerbal Space Program, Stormworks and GearBlocks.

Benchmark products are capability references only. MERA does not copy protected code, data, formulas, authored content, UI expression, save formats or proprietary protocols.

The strongest transferable lessons are:

1. **Simulation before commitment.** A user may design a proposed configuration and inspect requirements, conflicts and derived effects without mutating the real Asset.
2. **Safe disassembly order can matter.** Energy, pressure, heat, hazardous materials, structural dependency and other governed hazards may require isolation or sequencing.
3. **Damage affects recoverability.** The condition of an assembly can change whether it is repairable, reusable, salvageable or only material scrap under owner rules.
4. **Configuration should change behavior.** Parts, systems and tuning should matter through governed capabilities and tradeoffs, not a universal upgrade-level abstraction.
5. **Field repair and overhaul are distinct.** A temporary patch, normal repair, major service, restoration and rebuild may have different requirements and consequences.
6. **Redundancy and dependency are meaningful.** A damaged subsystem may degrade, isolate or cascade according to the owning system definition rather than a universal formula.
7. **Donor parts and substitution matter.** Compatible, adapted, refurbished, remanufactured or improvised parts can be legitimate governed choices.
8. **Engineering can be deep without 3D.** Schematic topology, compatibility matrices, dependency graphs, configuration diffs, system status and test evidence are sufficient blocking workflows.

## Player/GM workflows

### Inspect and diagnose

A Character or GM can inspect only authorized information. The system distinguishes known fault, suspected subsystem, isolated failure, unknown cause and hidden/unrevealed truth. Diagnostics never grant omniscience merely because a repair screen exists.

### Design and dry-run

A proposed configuration is non-authoritative. Users may add/remove/substitute components, compare current versus proposed state, inspect requirements, view unresolved compatibility, estimate owner-defined resource/time requirements and save a blueprint without changing the live Asset.

### Isolate and disassemble

Engineering work can require access, shutdown, depressurization, discharge, lockout, support, environmental protection or other owner-defined prerequisites. LSS governs what actually becomes recoverable; MERA governs the engineering work plan and sequencing around that operation.

### Repair, replace and rebuild

MERA distinguishes owner-defined repair classes, including temporary field patch, service repair, replacement, overhaul, restoration and rebuild where supported. Repair changes current state and preserves prior damage/history.

### Substitute and jury-rig

If a correct component is unavailable, MERA may evaluate an owner-defined substitute, adapter, bypass or improvised replacement. Any degradation, instability, maintenance burden, incompatibility, risk or benefit comes from governed definitions—not a universal MERA penalty.

### Calibrate and tune

Supported systems may expose alignment, calibration, tuning, configuration, power allocation, timing, control profile or other bounded adjustments. Tuning cannot invent capabilities the underlying system does not have.

### Test and acceptance

A completed work order may require bench test, diagnostic test, static test, shakedown, inspection, certification or mission-readiness proof according to the active profile. A successful work transaction is not automatically proof that the Asset is fully operational if the governing profile requires further acceptance.

## Cross-domain data flow

MERA carries stable IDs and authorized projections rather than copying mutable owner truth.

A representative flow is:

1. inspect Asset/system state from the owning domain;
2. create a non-authoritative engineering proposal;
3. resolve compatibility, access, skill, tool, workstation and resource prerequisites;
4. reserve or identify required materials/components through owner systems;
5. submit authorized LSS/MIB-12/APW operations;
6. collect committed receipts and updated owner state;
7. perform any governed calibration/testing;
8. publish a resulting authorized configuration/condition projection.

No MERA preview or simulation proves a mutation occurred.

## Damage, failure and dependency

MERA may visualize dependencies and predicted consequences only where definitions support them. It does not create a universal real-world engineering simulator.

Profiles may support:

- functional dependency;
- structural dependency;
- power/fuel/resource dependency;
- coolant/fluid dependency;
- ammunition/feed dependency;
- data/control dependency;
- atmosphere/life-support dependency;
- heat/stress dependency;
- magical/supernatural dependency;
- redundancy and alternate paths;
- isolation and graceful degradation.

Unknown topology remains unknown.

## Resource and network boundary

MERA may present governed networks such as power, fuel, coolant, hydraulics, pneumatics, atmosphere, ammunition, data, control, heat, magical energy or setting-specific equivalents. It must not infer detailed networks from a coarse source record that merely mentions a resource.

## Profession, tools and time

Engineering work may depend on Character skills/Knowledges/Professions, assistants, tools, facilities, workstations, environmental conditions, access permissions, parts and campaign time. MERA consumes those requirements from owner systems rather than creating a second Profession or Project model.

A GM can override only through the governing rules/authority path; MERA does not silently waive requirements.

## Blueprint and sharing model

Engineering blueprints/presets are reusable plans, not live Assets. They can describe intended component identities, compatible alternatives, configuration roles, interfaces, work sequence and expected owner-defined outputs.

Clone/fork, diff, review, provenance and sharing preserve source identity and rights. Installing a shared blueprint still revalidates every target Asset, component, permission and rules requirement.

## Optional AI

Optional AI may explain a fault report, suggest a diagnostic path, propose compatible alternatives, summarize a configuration difference or draft an engineering work plan using visibility-safe context. It has no authority to install, uninstall, dismantle, consume, fabricate, repair, spend, transfer ownership, change configuration, approve hazards or declare an Asset operational.

All blocking workflows must remain usable locally/offline without a paid/cloud AI provider.

## Twenty-four bounded tranches

1. **MERA-01 — Engineering Workspace, Authority Contract & Engineering-Resolution Ladder**
2. **MERA-02 — System / Assembly / Component / Interface Topology Model**
3. **MERA-03 — Blueprint, Proposed Configuration, Dry-Run, Diff & Commit Workflow**
4. **MERA-04 — Compatibility, Fit, Interface, Adapter & Substitution Resolver**
5. **MERA-05 — Inspection, Diagnostics, Fault Isolation & Unknown-Fault Workflow**
6. **MERA-06 — Safe Isolation, Access, De-Energization & Disassembly Sequencing**
7. **MERA-07 — Repair Classes: Field Patch, Service Repair, Overhaul, Restoration & Rebuild**
8. **MERA-08 — Wear, Reliability, Maintenance State & Service-Interval Profiles**
9. **MERA-09 — Calibration, Tuning, Alignment & Performance-Envelope Adjustment**
10. **MERA-10 — Dependency, Cascading Failure, Redundancy & Graceful-Degradation Model**
11. **MERA-11 — Power, Fuel, Heat, Fluid, Data, Control & Setting-Specific Network Interfaces**
12. **MERA-12 — Item, Weapon, Armor, Tool & Equipment Modular Engineering**
13. **MERA-13 — Ground, Water, Air & General Vehicle Construction / Refit**
14. **MERA-14 — Mecha, Walker, Frame, Motive-System, Hardpoint & Armor Engineering**
15. **MERA-15 — Spacecraft, Starship, Hull, Module, Interior-System & Carried-Craft Engineering**
16. **MERA-16 — Machinery, Robotics, Constructs, Industrial & Special-System Engineering**
17. **MERA-17 — Damage-State → Salvageability / Recoverability / Donor-Part Integration**
18. **MERA-18 — Cannibalization, Remanufacture, Refurbishment, Fabrication & Replacement**
19. **MERA-19 — Engineering Skill, Tools, Workstations, Crew, Projects, Time & Assistance**
20. **MERA-20 — Emergency Engineering, Jury-Rigging, Bypass, Temporary Replacement & Improvisation**
21. **MERA-21 — Garage, Hangar, Workshop, Fleet Maintenance, Spares & Refit Queues**
22. **MERA-22 — Test Bench, Simulation, Shakedown, Inspection, Acceptance & Certification**
23. **MERA-23 — Blueprints, Presets, Loadout Roles, Import/Export, Sharing, Provenance & Optional AI Advice**
24. **MERA-24 — Golden Cross-Domain Salvage → Engineering → Refit → Operational Proof**

Every tranche targets no more than 24 active minutes. If a tranche cannot credibly fit that bound, it must be split before implementation begins rather than overrunning the execution contract.

## Golden proof

MERA-24 must prove at minimum:

- a damaged ordinary Item inspected, diagnosed, repaired and returned to use;
- a weapon or armor configuration modified through a saved non-authoritative blueprint before commit;
- a vehicle repaired with a compatible donor component recovered through LSS;
- a mecha refit that changes governed capability/loadout without replacing Asset identity;
- a starship subsystem failure isolated, replaced/refurbished, calibrated and tested;
- a jury-rigged repair that remains explicitly temporary/degraded only because the governing definition says so;
- a partial teardown that preserves unrecovered components and provenance;
- a destroyed/damaged component whose condition changes recoverability according to an owner-defined profile;
- a proposed incompatible configuration that fails closed before consuming anything;
- a configuration with unknown source data that remains unresolved rather than receiving fabricated capacity/topology;
- Project/Profession/tool/workstation/time requirements routed through their owners;
- exact input/output/lineage receipts across salvage, repair, fabrication and installation;
- local/offline operation with optional AI disabled;
- equivalent nonvisual engineering operation without requiring 3D manipulation;
- handoff into MBES machinery/infrastructure use without MBES creating a second engineering engine.

## Program-wide invariants

- Definition, blueprint/proposal, Asset instance, installed configuration, live operational state and presentation remain distinct.
- LSS remains salvage/decomposition authority.
- MIB-12 remains crafting/repair/refurbishment transformation authority.
- PPIA-03/D17 remain Item/Asset identity, ownership, containment, condition and lineage authority.
- MIB-14/PPIA-04/F014 remain vehicle/mecha/starship definition and operational authority.
- APW/D26 remains Project/time authority.
- DPL/Profession owners remain work-skill and life/profession authority.
- MRCS remains reusable rule/content-definition authority.
- MBES consumes MERA engineering capabilities for machinery/infrastructure but does not replace them.
- Unknown is not zero, absent, unlimited, compatible or safe.
- Simulation/dry-run is not mutation.
- A successful repair operation does not erase damage/provenance history.
- No universal compatibility, reliability, failure, wear, salvage-yield, repair-quality, jury-rig penalty or tuning formula may be invented by MERA.
- No real-world engineering or safety claim is implied by game-rule simulation.
- No 3D renderer is required for blocking engineering workflows.
- Optional AI is advisory only.
- No paid/cloud provider is required for blocking workflows.
- No MERA runtime preflight or implementation authority exists now.

## Roadmap placement

Owner-approved placement:

**… → MSAS-01..21 → MRCS-01..21 → MERA-01..24 → MBES-01..24 → SMB-08 …**

This placement lets MRCS author reusable components/interfaces/engineering rules before MERA productizes playable engineering, then lets MBES consume the finished engineering layer for workshops, machinery, utilities, infrastructure, garages, shipyards and similar built-environment systems.
