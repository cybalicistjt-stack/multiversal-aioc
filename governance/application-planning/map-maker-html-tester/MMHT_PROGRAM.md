# MMHT — Map Maker HTML Tester

Owner approved November 20, 2026. OPS5 routing is defined in operations/LANES.json and operations/CURRENT.json.

Owner-approved map authoring only. Ship and vehicle operations, base construction, farming, extraction, ecology simulation and other gameplay engines retain their owner-domain scope. Map features may store typed references for later integration.

Each cycle delivers a self-contained HTML and an editable sample. Acceptance covers map authoring, geometry and topology, inspection, visibility, save/reopen, export and the preservation of typed map references where applicable.

Approved scope and per-cycle acceptance: [Map Expansion Review](https://chatgpt.com/library?file_id=libfile_a976a33aebf08191a4e3bcca6d4d1ae1&account_id=personal).

| Cycle | Review focus |
| --- | --- |
| MMHT-01 | Deck Builder |
| MMHT-02 | Ship Layouts & Docking Connections |
| MMHT-03 | Base Layouts & Blueprints |
| MMHT-04 | Base Infrastructure Maps |
| MMHT-05 | Environment Zones & Overlays |
| MMHT-06 | Water, Weather & Hazard Layers |
| MMHT-07 | Habitat & Wildlife Maps |
| MMHT-08 | Farm & Forage Maps |
| MMHT-09 | Animal & Aquatic Facility Maps |
| MMHT-10 | Caves, Sections & Links |
| MMHT-11 | Mine & Deposit Maps |
| MMHT-12 | Storage, Processing & Route Maps |
| MMHT-13 | Habitat & Land-Use Change Maps |
| MMHT-14 | Non-Euclidean Map Authoring |
| MMHT-15 | Advanced Spatial Geometry & Round-Trip |

## First cycle

MMHT-01 provides the editable Kestrel courier decks and Utility Rover. [Download the first HTML](https://chatgpt.com/library?file_id=libfile_c64974e305948191a3ce0656f2ac2819&account_id=personal).

Cycle progress is tracked in operations/work-items/MMHT-01.json. Further cycle selection follows explicit owner direction.

## Ship layouts and downtime handoff

MMHT-02 provides editable Meridian Station, Kestrel courier and Wren shuttle plans. Author crew stations, equipment mounts, ramps, ports and berths. Pair endpoints and inspect authored hull clearance, direction, visibility and unresolved endpoints. [Download the MMHT-02 HTML](https://chatgpt.com/library?file_id=libfile_e2497f209c548191a6041006d9af6e21&account_id=personal).

[The Downtime handoff](https://chatgpt.com/library?file_id=libfile_a2458043636c81919b113c40a0c4788a&account_id=personal) supplies Lantern Post as the shared map reference case. Revision 2 preserves its map, floor and feature IDs, adds typed roles, and distinguishes hoist and ladder access from infrastructure such as ventilation and irrigation. [Lantern Post revision 2 player references](https://chatgpt.com/library?file_id=libfile_70de82c19b548191a853cb245ea5432d&account_id=personal).

Carry stable IDs, pinned revisions, thin map references, explicit link purposes and filtered player projections into the relevant base, environmental, farming, cave, mining, logistics and spatial cycles. The Map Maker supplies geometry and map references, while each gameplay tester owns its activity state and resolution. Use explicit file handoffs while testers run independently.

Cycle progress is tracked in operations/work-items/MMHT-02.json. MMHT-03 remains the planned successor.

## Base layouts and blueprints

MMHT-03 adds editable Workshop Outpost and Field Work Platform maps with separately identifiable sites, parcels, structures and rooms. Draw or resize footprints, save and stamp specific room blueprint versions, and retain optional owner facility references. [Download the MMHT-03 HTML](https://chatgpt.com/library?file_id=libfile_ee67967ffec88191bc9cabb965446af9&account_id=personal).

Blueprint stamps are map instances with their own feature IDs. They retain the chosen source version and authored dimensions when placed at a different map scale. The room scope includes the floor outline, finishes and attached doors or windows. Facility references are assigned independently to each room. Use full draft exports for editing and audience-filtered reference JSON for independent consumers.

Cycle progress is tracked in operations/work-items/MMHT-03.json. MMHT-04 remains the planned successor.

## Base infrastructure maps

MMHT-04 adds the editable Workshop Outpost Utility Plan. Route power, water, ventilation, access and communications between explicit map features. Switch the display between individual services and preview the sample Generator feeder outage. [Download the MMHT-04 HTML](https://chatgpt.com/library?file_id=libfile_44966f8fa900819182540bf51eb3c48c&account_id=personal).

Triggers for map traces are typed source designations, directed links and the closed route IDs in authored scenarios. Room edits move attached route endpoints. Player references filter GM-only scenarios and routes whose endpoints are unavailable. Operational utility state and engineering calculations remain in the owning systems.

Cycle progress is tracked in operations/work-items/MMHT-04.json. MMHT-05 remains the planned successor.

## Environment zones and overlays

MMHT-05 adds editable Harrowfen, Brinegate and Meridian surveys. Bind an environment preset and local overlays to a drawn outline, an existing map feature, a level or the whole map. Display zones and overlays independently. [Download the MMHT-05 HTML](https://chatgpt.com/library?file_id=libfile_28eedbcbca94819188482ba68c894076&account_id=personal).

Reuse 76 governed ENV presets plus the map maker’s five existing local and adventure entries. Include all 47 overlays from ENV-11, ENV-12 and ENV-13 with source links. Diagnostics flag source exclusions within a zone. Map references preserve authored scopes and player/GM visibility. ENV remains the owner of resolved conditions and gameplay effects.

Cycle progress is tracked in operations/work-items/MMHT-05.json. MMHT-06 remains the planned successor.

## Water, weather and hazard layers

MMHT-06 adds watershed, farm and underground shelter surveys. Draw drainage, irrigation and travel routes and authored flood, weather or hazard extents. Independently toggle High water and Heavy rain, then inspect numbered route segments and highlighted coverage. [Download the MMHT-06 HTML](https://chatgpt.com/library?file_id=libfile_0897865c126081918c97130319e42b90&account_id=personal).

Extents may use existing map geometry or their own outline. Conditions independently activate authored extents. Role-filtered map references preserve geometry and catalog links. Crossings describe map geometry only. World, environment, and gameplay systems retain authority over outcomes.

Cycle progress is tracked in operations/work-items/MMHT-06.json. MMHT-07 remains the planned successor.

## Habitat and wildlife maps

MMHT-07 adds the Havalaea Canopy & Basin survey. Author flora zones, habitats and sanctuaries, draw seasonal corridors with width, and place observation or encounter markers. Use the season selector to compare spring and autumn routes. [Download the MMHT-07 HTML](https://chatgpt.com/library?file_id=libfile_80fcba23b0c881918e6558982f4ce518&account_id=personal).

Creature references reuse the governed CEW-01 Identity Ledger and accept explicit external IDs. Role-filtered map references omit restricted observations and their geometry and notes. Sample map annotations are editable scenario authoring. The CEW/ENV and campaign owners retain authority over actual habitat fit, distribution, frequency and encounters.

Cycle progress is tracked in operations/work-items/MMHT-07.json. MMHT-08 remains the planned successor.

## Farm and forage maps

MMHT-08 adds the Lantern Post Farm & Forage Survey and Aster Glasshouse. Draw and measure fields, orchards, hydroponic beds, arcane terrariums and gathering areas. Reuse map footprints or draw new boundaries and mark links to water, irrigation and storage. [Download the MMHT-08 HTML](https://chatgpt.com/library?file_id=libfile_cd733c5fb4488191af8add13a6d94fb1&account_id=personal).

The sample player reference file was imported into Downtime Cycle 07. The 750 sq ft wheat plot, the deep gallery forage pocket and water access are available as mapped locations. Optional growing-medium and ICF-13 resource references remain in the Map Maker handoff. [Download the Lantern Post player references](https://chatgpt.com/library?file_id=libfile_a15d856d33e08191922a05396f99da91&account_id=personal).

Cycle progress is tracked in operations/work-items/MMHT-08.json. MMHT-09 remains the planned successor.

## Animal & aquatic facility maps

MMHT-09 adds editable Reedwater Hatchery & Apiary and Lantern Post animal facilities. Draw and measure pastures, pens, aquaculture tanks, hives and special enclosures, then place entrances and care points and link water, feed and access. [Download the MMHT-09 HTML](https://chatgpt.com/library?file_id=libfile_f505f473bca481918dcf25ece173ee94&account_id=personal).

[Reedwater editable sample](https://chatgpt.com/library?file_id=libfile_44c696f93d048191862bfb59a08daa20&account_id=personal), [player references](https://chatgpt.com/library?file_id=libfile_b3b8438be554819196952fccb12e4990&account_id=personal), and [GM references](https://chatgpt.com/library?file_id=libfile_56e36248f2b88191b791ea5dac04cfb9&account_id=personal) were exported and validated. The GM-only special enclosure is omitted from player references. ICF-13 remains the authority for husbandry eligibility and production; map examples do not compute population, care or yields.

Cycle progress is tracked in operations/work-items/MMHT-09.json. MMHT-10 is the planned successor.

## Caves, sections and links

MMHT-10 adds editable Brinegate Split Caverns and Western Cut maps. It distinguishes floor geometry and cross-map visual overlap from explicit, directional topology. Author cave chambers, passages, tunnels, shafts, ladder anchors, and existing-feature roles; inspect elevation bands, crossings and reachable paths. [Download the MMHT-10 HTML](https://chatgpt.com/library?file_id=libfile_decc4d5e4a08819185566ddca052331b&account_id=personal).

The self-contained tester includes a one-way upper-to-middle hoist, a two-way ladder to the deep vault, a cross-map exit and two intersecting gallery lines without a link. GM-only passages remain absent from filtered player references. Save/reopen and import of the editable sample passed in Chromium; physical Android and installed-app tests remain pending. [Editable Brinegate draft](https://chatgpt.com/library?file_id=libfile_30e7f18c90fc81918ad151559f78ce1b&account_id=personal); [player references](https://chatgpt.com/library?file_id=libfile_dbf3569587008191ae2ca4de3d9b1b4b&account_id=personal); [GM references](https://chatgpt.com/library?file_id=libfile_59a1ff23ff7c81919eb8f50662b3f662&account_id=personal). The owner domains retain movement, mining, ecology and gameplay authority.

Cycle progress is tracked in operations/work-items/MMHT-10.json. MMHT-11 is the planned successor.

## Mine and deposit maps

MMHT-11 adds the editable Brinegate Mine & Deposit Survey and a Lantern Post mine reference copy, building on cave-level topology without introducing a mining gameplay engine. Author deposits, working faces, supports, shafts, hazard zones, drainage, ventilation, access and haul lines. Each deposit has one depth band, geometry, stable feature ID and optional typed owner/profile references. [Download MMHT-11 HTML](https://chatgpt.com/library?file_id=libfile_659ce4b47cbc8191a557dbdccbe5bad2&account_id=personal).

[Brinegate editable draft](https://chatgpt.com/library?file_id=libfile_85ea291abc488191a1f971bb386a9ccd&account_id=personal), [player references](https://chatgpt.com/library?file_id=libfile_886e508c6fd081918148850ed8faa679&account_id=personal) and [GM references](https://chatgpt.com/library?file_id=libfile_b6b6841f08c08191aa3b90f0dc097b98&account_id=personal); [Lantern editable reference copy](https://chatgpt.com/library?file_id=libfile_b0ce97c68d188191ba2494fecf73ca47&account_id=personal). Brinegate has three mapped depths. A hidden high-density vein and gas pocket are present only in the GM reference file; the player export excludes their IDs, geometry, labels, and links. The browser verified editable drawing, route direction/nontraversability, broken-endpoint diagnostics and full save/reopen file round-trip; physical Android and installed app testing remain outstanding. DPL-06 metadata is advisory source vocabulary only; no extraction, depletion, inventory mutation or hazard mechanics have been implemented.

Cycle progress is tracked in operations/work-items/MMHT-11.json. MMHT-12 remains the planned successor.
