# MBES — Multiversal Built Environment & Settlement

**Program ID:** MBES  
**Program name:** Multiversal Built Environment & Settlement  
**Version:** 0.1.0  
**Status:** OWNER-APPROVED — PLANNED INTERSTITIAL; NOT STARTED  
**Activation:** after MRCS-21  
**Successor:** SMB-08  
**Owner and final authority:** John Brandon Turner  
**Approved:** 2026-09-11  
**Implementation authority:** none

## Purpose

MBES turns Multiversal's existing base/facility, World/Environment, Project/time, crafting, economy, cultivation, organization, settlement, strategic-consequence and cartography foundations into one coherent **player + GM building and settlement gameplay system**.

The product target is not merely a construction editor. A Character, household, crew, organization, faction, community or GM-authored population can acquire a site, plan work, build and furnish structures, connect utilities, establish production, inhabit and operate facilities, expand a settlement, reshape terrain, manage infrastructure, suffer damage and maintenance, and create consequences that propagate into the owning World/Environment/Economy/Organization systems.

MBES must scale cleanly from personal-space play — decorating a bedroom or upgrading a workshop — through homesteads, forts, shipside bases, mines, factories and research stations to districts, cities and networks of settlements.

## Placement

MBES is a future interstitial program:

`SMB-07 → CNI-01..13 → PCA-01..16 → MCS-01..21 → MCCS-01..21 → MAS-01..21 → MSAS-01..21 → MRCS-01..21 → MBES-01..24 → SMB-08 → SMB-09`

Rationale:

1. MCS supplies maps, interiors, terrain and spatial authoring.
2. MRCS supplies governed rules/content/blueprint definition workflows.
3. MBES then supplies the actual construction, occupancy, logistics, environmental consequence and settlement gameplay layer before large first-party content production begins.
4. SMB-08/09 can therefore create first-party homes, bases, facilities, settlements and world-reactive development using a completed common system rather than bespoke campaign mechanics.
5. MBES does not change the current ARI family, current work pointer or implementation authority.

## Core design doctrine

### One system, variable resolution

MBES uses a construction-resolution ladder:

`settlement/district → site/parcel → structure → level/zone → space/room → component/fixture → connection/network`

A play surface may stop at whatever level is useful.

Examples:

- a village may remain a summarized settlement with population, service, production and infrastructure capabilities;
- a player-owned home may expand to rooms, furniture, utilities and individual fixtures;
- a fortress may use detailed walls, gates, defenses and rooms during a siege and later collapse back to summarized facility state;
- a city may model districts, services and transport without instantiating every chair;
- a factory may model production and logistics networks in detail while neighboring houses remain aggregate capacity.

Expanding or summarizing a level changes presentation/simulation resolution, not canonical identity. MBES must not create duplicate ledgers merely because detail changes.

### Definition is not construction; geometry is not truth

A blueprint, MRCS definition, MCS drawing, preview placement or generated proposal is not a completed structure.

The governed flow is:

`accepted definitions + authorized site + Project/time/resources + construction operations → owner commits → built-environment state`

Likewise, demolition, pollution, extraction, terrain change, ownership transfer, resident relocation or world reaction requires the relevant owner operation rather than visual manipulation alone.

### Capability-derived spaces

MBES must support functional-space recognition based on actual accepted capabilities, not just names.

A space may qualify as a kitchen, laboratory, forge, greenhouse, infirmary, hangar, ritual chamber, reactor room, tavern, bedroom or other governed facility when its installed components, network access, environmental conditions, staffing/access and owner rules satisfy the relevant requirements.

The same capability may be achieved through different technologies, magic, biology or cultural construction traditions. A medieval kitchen, arcane food laboratory and starship galley therefore need not share identical components.

### Small primitives, emergent systems

Construction pieces, networks, sensors, controllers, storage and production components should compose into useful higher-order behavior instead of requiring a bespoke mechanic for every possible machine.

Automation remains bounded. A condition→action network may open doors, reroute power, start an authorized pump, move inventory or stop production at a threshold, but it cannot become unrestricted code or silently exercise GM, consent, ownership or irreversible advancement authority.

## Branch, Reality, World and Environment variation

Built environments must be contextual rather than universal.

Canonical Branch/Reality/World/Environment owners may supply condition profiles including, where applicable:

- gravity and inertial behavior;
- atmosphere, pressure and breathable-medium requirements;
- temperature, climate, weather and seasonality;
- radiation, toxicity, corrosion and contamination;
- geology, soil, hydrology and seismic conditions;
- ecology, carrying capacity, habitat sensitivity and regeneration;
- resource availability and depletion behavior;
- magic, technology or physical-law constraints;
- local sentience, spirits, world minds or other owner-defined reactive-world behavior;
- cultural/legal/property restrictions where those are owned by social/governance systems.

MBES consumes these profiles to determine construction requirements, viability, maintenance burdens, utility choices and consequence exposure. It does not redefine them.

## Oara owner-directed acceptance requirement

Oara has planetary sentience that responds to pollution and over-development.

MBES must therefore prove a generic reactive-world architecture in which construction and operation can emit explicit, inspectable externality observations such as pollution load, habitat disruption, extraction pressure, density, land conversion, waste, hydrological alteration or other owner-defined signals. World/Environment authority then determines whether and how the world responds.

Oara must **not** be implemented as an isolated hard-coded special case. The engine capability must be generic enough for other worlds with spirits, living ecosystems, magical feedback, hostile terraforming responses, divine stewardship, machine-world regulation or other reactive-world semantics.

The final proof must demonstrate that an equivalent development can produce different consequences on two worlds because their owner-supplied condition/response profiles differ.

Recovered Oara source material already contains machinery/pollution concern signals, but MBES does not invent exact Oaran reaction mechanics from incomplete recovered evidence. The owner's 2026-09-11 directive establishes the planning requirement; the canonical World/Environment owner will supply exact mechanics when implemented.

## Existing authorities MBES consumes

- **MIB-14:** base/platform/vehicle definitions, module/facility compatibility, capacity/loadout, crew/station requirements, power/fuel/resource hooks, maintenance/damage/repair/upgrade foundations and storage/workstation integration.
- **MIB-12:** crafting and transformation operations.
- **MIB-13:** currency, price, trade, services, contracts and deterministic market/settlement semantics.
- **APW/D26:** durable Projects, tasks, participants, phases, prerequisites, time and cancellation.
- **CEL/APM:** Cozy/life-loop orchestration and bounded automation/human-stop behavior.
- **ICF:** cultivation, husbandry, ingredients, production and foodcraft definitions.
- **MCS:** maps, terrain, settlement/city/interior geometry, spatial editing and presentation.
- **MRCS:** governed construction materials, components, facility definitions, blueprints, rules and content packs.
- **ARI:** resource identity, bytes/reference state, rights, provenance and derivative lineage.
- **World / Environment / Reality / Branch / Exploration:** canonical place, terrain, climate, environmental conditions, ecology, discovery and world state.
- **Character / NPC / Species/Form:** people/creatures, biology, capabilities and state.
- **Inventory/Asset:** ownership, storage and item/asset state.
- **ODL:** businesses, organizations, factions, settlements, crews, families and leadership/relationship seams.
- **SCL:** strategic-scale conflict, formations and settlement/world/campaign consequence integration.
- **Action/Event:** authoritative mutation/event receipts.
- **Scene / Combat / Visibility:** local placement, tactical state, destruction/hazards and authorized projection.

## Benchmark provenance and clean-room boundary

The benchmark set includes construction, housing, factory, survival, colony and city-building games including The Sims 4, World of Warcraft housing, No Man's Sky, Minecraft, Stardew Valley, Valheim, Subnautica, Enshrouded, Timberborn, Factorio, Satisfactory, SimCity/Cities: Skylines-class city builders, Anno, RimWorld, Dwarf Fortress, Oxygen Not Included, Dragon Quest Builders 2, Fallout/Starfield-style settlement/outpost systems, V Rising, Eco and Against the Storm.

The detailed capability synthesis is recorded in `MBES_BENCHMARK_CAPABILITY_MATRIX.md`.

MBES follows the PCM clean-room rules: public documentation and lawful ordinary-use behavior may establish capability requirements, but protected source, assets, maps, distinctive UI expression, save formats, private protocols or proprietary implementation details are not copied.

## Program tranches

### MBES-01 — Built-Environment Workspace, Authority Contract & Construction-Resolution Ladder

Define MBES workspace projections, stable identities and the resolution ladder from settlement/district through connection/network. Establish proposal/preview/authorized-project/built/damaged/decommissioned dispositions, summary↔detail rules, stale-owner handling and explicit mutation boundaries.

### MBES-02 — Site, Parcel, Claim, Ownership, Permission & Construction-Project Foundation

Bind sites/parcels to canonical World locations and permission/property owners. Support owner/tenant/lease/communal/faction/public/project permissions where owner systems provide them, construction zones, setbacks/reservations where authored, Project creation, funding/labor assignment and cancellation/recovery.

### MBES-03 — Construction Materials, Structural Properties, Cost, Labor & Time Model

Bind MRCS/material definitions and crafting/economy/project owners to construction requirements. Support rule-defined strength/support, mass, durability, insulation, fire/heat resistance, pressure sealing, corrosion, magical conductivity or other setting-specific properties without assuming every setting uses every property.

### MBES-04 — Player/GM Build Mode: Foundations, Walls, Floors, Roofs, Openings & Vertical Access

Provide playable structure assembly over MCS spatial primitives: footprints, foundations, walls, floors, roofs, doors/windows/openings, stairs/ladders/elevators/ramps, multi-level relationships, snapping/free placement, validation and non-pointer alternatives. Build Mode creates proposals/projects until owner operations commit work.

### MBES-05 — Functional Space/Room Recognition, Capability Derivation & Requirement Inspection

Recognize bounded spaces/zones and derive supported capabilities from accepted components, networks, access and environment conditions. Expose why a room does/does not qualify and what change would satisfy requirements. Never classify by decorative label alone.

### MBES-06 — Furniture, Fixtures, Decoration, Comfort, Identity & Achievement Display

Support furnishing, décor, lighting, trophies/collections, cultural styles, comfort/privacy/social-space signals and personal/faction identity. Decorative state may affect governed comfort, hospitality, morale or other mechanics only where an owning rule explicitly defines the effect.

### MBES-07 — Blueprints, Prefabs, Modules, Templates, Clone/Fork, Sharing & Placement

Create reusable assemblies from rooms, buildings, machines, defenses, infrastructure segments or whole sites. Preserve dependencies, rights/provenance, required networks, optional substitutions, scale/style variants and explicit unresolved references. Support private/shared/faction/library scopes without making community publication mandatory.

### MBES-08 — Utility & Life-Support Networks

Model setting-appropriate networks for electricity/energy, water/liquids, sewage/waste, fuel, heating/cooling, breathable atmosphere, magical power, communications/data and comparable resources. Network types are definition-driven; not every world must use the same utilities.

### MBES-09 — Logic, Sensors, Switches, Controllers, Automation & Safe Condition→Action Networks

Compose sensors, switches, timers, thresholds, selectors, controllers and bounded actions over existing owner operations. Support doors, pumps, lighting, resource routing, alarms, shutdowns and production control while preserving authorization, budgets, expected versions and stop conditions.

### MBES-10 — Storage, Conveyance, Routing, Inventory Interfaces & Logistics Networks

Connect canonical storage/inventory assets through transport links such as human/animal handling, carts, conveyors, pipes, tubes, drones, teleportation or setting-specific equivalents. Model throughput/capacity/priority where governed. MBES never creates a duplicate inventory ledger.

### MBES-11 — Extraction, Agriculture, Processing, Manufacturing & Production-Chain Facilities

Compose ICF, crafting, materials, inventory, Project/time and Economy owners into facility production chains: extraction/gathering, cultivation, processing, manufacturing, refinement, preservation and distribution. Support recipes and networks without duplicating MIB-12/ICF truth.

### MBES-12 — Terrain Shaping, Excavation, Fill, Tunneling, Grading & Civil Earthworks

Convert MCS terrain edits into proposed or authorized physical work: digging, filling, grading, foundations, trenches, tunnels, quarries, embankments and comparable operations. Require explicit World/Environment commit paths and preserve original-state/provenance needed for rollback or consequence calculation.

### MBES-13 — Hydrology, Irrigation, Drainage, Dams, Canals, Reservoirs & Land Reclamation

Author and execute governed water-management projects. Hydrology previews may use MCS/PCA simulation, but permanent river/lake/wetland/groundwater or terrain truth changes only through owning World/Environment operations.

### MBES-14 — Pollution, Waste, Heat, Noise, Habitat, Resource Depletion & Ecological Externalities

Produce explicit externality projections/receipts from construction and facility operation. Support source, magnitude, affected area/pathway, accumulation/recovery and owner-defined thresholds without imposing one universal ecological model. Feed Environment/World/Economy/social owners; do not adjudicate their response.

### MBES-15 — Branch, Reality, World & Environment Construction Conditions / Reactive-World Hooks

Resolve construction against owner-supplied branch/reality/world/environment profiles and consume owner-authorized responses. Prove that gravity, atmosphere, magic laws, ecology, legal/cultural constraints and living-world feedback can alter viable designs and consequences. Include Oara's planetary-sentience interface as a required reference case without hard-coding Oara into the generic engine.

### MBES-16 — Habitability, Shelter, Atmosphere, Pressure, Climate, Radiation & Environmental Resilience

Compose structure sealing, insulation, atmosphere, environmental shielding, life support, shelter and emergency refuge requirements. Support hostile planets, underwater habitats, underground complexes, extreme climates and supernatural environments through definition-driven condition profiles.

### MBES-17 — Residents, Households, Crews, Staffing, Jobs, Access & Facility-Use Integration

Connect spaces/facilities to Character/NPC/Species/Form, household/crew/organization and Project owners. Support residence capacity, bed/space assignment, workplace access, staffing prerequisites and use permissions without duplicating Character needs, schedules, employment, relationships or ownership.

### MBES-18 — Durability, Upkeep, Wear, Damage, Fire, Failure, Repair, Retrofit & Disaster Recovery

Support rule-defined maintenance, decay, damage, structural/service failures, fire, contamination, repair, retrofit, salvage and decommissioning. Damage can originate from Combat, hazards, environment or events; MBES projects impacts and commits only through authorized owners.

### MBES-19 — Defense, Security, Fortification, Siege, Emergency & Hazard-Response Infrastructure

Integrate walls/gates, sensors, alarms, shelters, fire suppression, quarantine, evacuation, fortifications and other protective infrastructure with Scene/Combat/SCL/Visibility owners. Construction provides capabilities; Combat/SCL remain adjudication authorities.

### MBES-20 — Settlement/District/City Growth, Land Use, Housing Capacity, Services & Public Works

Scale built-environment state upward into districts and settlements. Support lots/parcels, housing capacity, commercial/industrial/civic/recreational or custom land-use profiles, sanitation, healthcare, education, safety, public space and other services where authored. Avoid assuming modern zoning is universal.

### MBES-21 — Transportation, Roads, Transit, Ports, Access, Traffic & Regional Infrastructure

Compose canonical routes and built infrastructure for paths, roads, bridges, rail, ports, air/space access, transit, freight and setting-specific movement networks. Support accessibility, capacity and congestion projections where rules provide them; Exploration/World retain travel truth.

### MBES-22 — Property, Funding, Commerce, Markets, Taxes, Contracts, Trade & Construction Economy

Connect construction to MIB-13 and ODL: private/communal/faction/public financing, contracts, procurement, labor/service costs, land/property charges where applicable, local supply constraints, operation costs, rents/fees/taxes when authored, businesses, trade and reinvestment. No real-money commerce.

### MBES-23 — Neighborhoods, Community/Faction Projects, Multi-Settlement Networks, Specialization & Regional Development

Support shared neighborhoods, guild/faction/community facilities, cooperative Projects, settlement specialization, inter-settlement dependencies, regional production/trade networks and development choices. Preserve owner-domain population, faction, relationship and political authority.

### MBES-24 — Golden Cross-Scale Building, Settlement, Environment-Reaction & Oara Sentience Proof

Create an original Multiversal golden suite proving at least:

1. a personalized player home with reusable room/blueprint flow;
2. a working homestead/farm/workshop loop;
3. a fortified fantasy or low-tech base;
4. a hostile-environment sci-fi/otherworld outpost with utilities/life support;
5. an extraction→logistics→processing→manufacturing facility;
6. a settlement/city district with services, transport and economy hooks;
7. an underground or submerged installation;
8. a terrain/hydrology engineering project;
9. a multi-settlement regional network;
10. a reactive-world comparison in which equivalent development on Oara and a non-Oara reference world produces different owner-authorized consequences because Oara's planetary sentience responds to pollution/over-development.

The proof must demonstrate manual-build→Project→commit continuity, summary↔detail continuity, functional-space derivation, utility/automation/logistics networks, maintenance/damage, rights/provenance, accessible non-pointer workflows, local/offline blocking operation, deterministic receipts where claimed, unresolved/unsupported states instead of guessing, and explicit proof that geometry/previews/externality signals do not silently mutate owner truth.

## Cross-cutting requirements

Every MBES tranche must preserve:

- player and GM use paths;
- stable identity across summary/detail projections;
- owner references and expected versions;
- explicit proposal/preview/committed distinctions;
- undo/recovery for authoring actions and idempotent recovery for authoritative operations;
- keyboard/touch/non-pointer alternatives for essential build interactions;
- structured/list alternatives to graph/network-only views;
- high-contrast and non-color-only status indicators;
- local-first blocking workflows where practical;
- ARI provenance/rights for reusable assets/blueprints;
- visibility/permission filtering before projection/aggregation;
- deterministic simulation receipts where determinism is claimed;
- conservative unresolved/unsupported states rather than invented semantics;
- scale/performance budgets appropriate to homes, large facilities, cities and regional networks;
- setting/branch/environment specificity without hard-coding one technology level or civilization model.

## Explicit non-goals

MBES does not:

- become a second World, Environment, Character, Inventory, Economy, Project, Action/Event, Settlement, ODL or SCL ledger;
- replace MCS cartography or MRCS rules/content authoring;
- infer completed construction from a map drawing or blueprint;
- make every settlement simulate every object at maximum resolution;
- require voxel terrain or one universal building grid;
- force modern zoning, utilities, labor markets or ecological assumptions onto every setting;
- create unrestricted automation scripting;
- allow AI to make canonical construction, demolition, ownership, resident, pollution or world-response decisions;
- pretend game structural/environment models are real-world engineering guidance;
- copy proprietary game assets, maps, save formats, UI layouts or source code;
- require paid/cloud construction services for blocking workflows;
- authorize public release, tester distribution, provider credentials or paid spend.

## Family execution rule

When MBES is eventually selected, it receives its own sealed family preflight. Every execution unit targets 24 active minutes or less with closeout reserve. Any unit that cannot credibly fit is split before governed start.

No MBES runtime preflight or implementation authority exists now.

## Completion standard

MBES is complete only when all 24 tranches are `completed_verified`, the golden suite proves personal through regional construction scales, equivalent state can move between summary/detail without duplicate truth, construction and environmental consequences flow through canonical owners, Oara's sentient-planet response can be expressed through the generic reactive-world interface, blocking workflows function without paid/cloud providers, and SMB-08 can use the completed system for first-party built-environment/settlement content without inventing a parallel construction engine.
