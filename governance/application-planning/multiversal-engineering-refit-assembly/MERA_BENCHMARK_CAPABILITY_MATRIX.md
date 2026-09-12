# MERA Benchmark Capability Matrix

**Program:** MERA — Multiversal Engineering, Refit & Assembly  
**Status:** owner-approved planning provenance  
**Clean-room rule:** benchmark products identify capabilities and interaction lessons only. They are not permission to copy protected code, data, formulas, authored content, prompts, UI expression, save formats, assets or proprietary protocols.

## Existing Multiversal baseline

MERA starts from completed or implementation-ready owner systems rather than a blank engineering game:

- LSS already owns recoverable objects, partial stripping, salvage, decomposition, donor components, cannibalization and lineage.
- PPIA-03/D17 already own Item/Asset identity, condition, durability, installations/modifications, ownership, containment and history.
- MIB-12 owns crafting/repair/refurbishment transformations.
- MIB-13 owns economy/trade/service value.
- MIB-14 owns vehicle/platform/base compatibility, loadout, resource hooks, maintenance, damage, repair and upgrade foundations.
- PPIA-04/F014 already model vehicles, mecha and starships with installed systems, stations, hardpoints, resources, damage, repair, capture and salvage.
- APW/D26 owns long-running Projects and campaign time.
- DPL/Profession owners own engineering/mechanic work capability.
- MRCS will own reusable component/interface/engineering-rule definitions.

The major uncovered product layer is advanced construction/refit/engineering orchestration across those owners.

## Benchmark capability lessons

| Benchmark family | Capability lesson for MERA |
|---|---|
| Hardspace: Shipbreaker | Inspection, hazardous dependency awareness, selective subsystem extraction and meaningful dismantling order. |
| BATTLETECH / MechWarrior-style campaign refit | Persistent machines, battlefield salvage feeding repairs, component replacement and economic pressure around keeping equipment operational. |
| MegaMekLab / MekHQ / MekBay | Deep rules-valid construction, refit and campaign maintenance can work through forms, matrices and records without requiring 3D editing. |
| Armored Core | Parts/configuration should alter role, mobility and behavior rather than only increasing an abstract upgrade level. |
| Crossout | Component destruction, protection, dependency and redundancy can make configuration tactically meaningful. |
| From the Depths | Engines, weapons and control systems can themselves be assemblies of interacting subcomponents. |
| Space Engineers | Construction and dismantling can share a conservation loop: components become machinery and machinery can return recoverable components. |
| TerraTech | Salvaged enemy components can immediately feed player construction/refit loops. |
| Pacific Drive | Field repair, expedition survival, workshop restoration and longer-term upgrade are distinct maintenance depths. |
| My Summer Car | Assembly order, diagnostics, individual components, maintenance and tuning can make knowing the machine part of play. |
| Ostranauts | Salvage, installation, ship systems, wear, repair, replacement and resource/network dependencies form one persistent engineering loop. |
| Cosmoteer | Module placement, crew/resource delivery, targeted system damage and breakup create operational consequences from configuration. |
| EVE fitting / Pyfa | Simulation before commitment: saved hypothetical fits, requirement checks, derived performance and comparison without owning/installing the hardware yet. |
| No Man's Sky ship salvage/building | Targeted component salvage can become inputs to later custom construction. |
| Starfield ship construction | Acquisition, legal/registration state, operation, repair, subsystem targeting, capture and later modification are separable concerns. |
| Kerbal Space Program / Stormworks / GearBlocks | Functional construction can be validated through staging, propulsion, logic, power/control and mechanical dependencies without treating the vehicle as a monolith. |

## Capability gaps MERA closes

### 1. Engineering-resolution ladder

Support `Asset → system → assembly → subassembly → component → interface/connection → governed network`, stopping wherever the source definition stops.

### 2. Dry-run configuration

Users can design a proposed configuration, compare against current state, inspect requirements/conflicts and save the plan without mutating the Asset.

### 3. Diagnosis and uncertainty

Represent observed symptom, suspected subsystem, isolated fault, identified component and unknown/unrevealed cause as distinct states. An engineering screen is not omniscience.

### 4. Safe work sequencing

Where a profile defines hazards or prerequisites, work can require access, shutdown, discharge, depressurization, support, isolation, environmental protection or other ordered steps.

### 5. Repair depth

Support profile-defined field patch, service repair, component replacement, overhaul, restoration and rebuild without imposing universal quality math.

### 6. Compatibility and substitution

Evaluate exact interfaces, fit, compatibility evidence, adapters, substitutes, donor parts, refurbished parts and jury-rigs. Unknown compatibility fails unresolved rather than becoming compatible by name similarity.

### 7. Dependency and redundancy

Visualize and evaluate governed functional, structural, resource, control, heat, atmosphere, magical or other dependencies, alternate paths and graceful degradation only where defined.

### 8. Calibration and tuning

Support bounded owner-defined calibration/tuning/alignment/performance adjustments after installation or repair.

### 9. Damage ↔ salvage ↔ repair continuity

Condition should be able to affect recoverability, donor usefulness, repairability and final re-use through owner rules while preserving LSS lineage and conservation.

### 10. Engineering labor

Bind work to Profession/Skill/Knowledge requirements, tools, facilities, assistants, Project phases, time and economy without creating duplicate owners.

### 11. Test and acceptance

Support bench test, diagnostic test, shakedown, inspection, certification or other profile-defined return-to-service evidence.

### 12. Fleet/workshop operations

Support garages, hangars, workshops, spares, work queues, planned maintenance and multi-Asset refits while preserving Asset identity and Project/time authority.

## Anti-goals

MERA does not:

- require a 3D renderer or precision spatial editor;
- simulate every bolt, wire or real-world engineering equation;
- reopen or replace LSS;
- create another Item/Asset, crafting, Profession, Project, economy or vehicle ledger;
- infer detailed topology from coarse source text;
- create universal failure, wear, compatibility, repair-quality, tuning or salvage formulas;
- treat a simulation/blueprint preview as a committed mutation;
- erase provenance or historical damage during repair/restoration;
- permit AI to perform authoritative engineering mutations.

## Golden benchmark proof

MERA-24 must demonstrate ordinary Item repair, equipment modification, donor-part vehicle repair, mecha refit, starship subsystem diagnosis/replacement/calibration, temporary jury-rig, partial teardown, condition-dependent recoverability, failed incompatible dry-run, unresolved unknown source data, Project/Profession/tool/time routing, exact provenance/lineage, local/offline operation and nonvisual engineering parity.
