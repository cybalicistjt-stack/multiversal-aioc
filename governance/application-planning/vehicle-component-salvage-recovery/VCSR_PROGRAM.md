# VCSR — Vehicle, Component, Salvage & Recovery HTML Tester

**Project:** Multiversal · **Program:** VCSR · **Owner direction:** 2026-11-22 · **Operational system:** OPS5  
**Execution form:** Owner-scoped, on-demand, **standalone browser HTML cycles**. No new application implementation lane or migration.  
**First delivery:** `Multiversal_VCSR_Cycle_01.html` (self-contained, offline-capable).

## Purpose

Deliver an independently executable browser playtest for modular **ships, vehicles, mecha, and other component-bearing objects**, together with their recoverable **loot / scavenging / salvage** workflows. Every cycle supplies a usable cumulative standalone HTML file, a specific test scenario, recorded pass/fail evidence and identified authority boundaries. Later cycles may exchange *versioned JSON files*, but existing GM, Character, Map Maker and Downtime testers **must not be joined or overwritten now**. Source-defined identity and ownership persist through later adapters.

### Existing implementation and canon are inputs, not competing inventions

The original LSS program **LSS-01..10 is completed_verified** in the AIOC backlog, including LSS-04 loot, LSS-05 authored scavenge opportunities, LSS-06 partial extraction, LSS-07 families, LSS-08 repair/reassembly and LSS-10 golden proof. The VCSR series is a **testing/prototyping surface** over their contracts, not a resurrection or duplicate implementation of LSS. The source LSS-01 inventory classifies **57 source concepts, 14 catalogs, 12,718 source records**, of which 2,117 are Mecha and 2,311 Spacecraft rows; those are *coverage evidence*, not guaranteed complete, runnable component profiles.

| Concern | Source owner | VCSR action | Boundary |
|---|---|---|---|
| Loot, ordinary assets/containers | LSS-04 + D17 | Inspect, propose, transfer | Do not create a second live inventory or overwrite Character/GM inventory |
| Scavenging | LSS-05 + World/MIB-11/D18 | Authored opportunity, requirements, result, depletion | No universal random D20 table; no rarity-to-yield conversion |
| Salvage/disassembly | LSS-02/03/06/07 | Slots, condition, explicit outputs, partial preservation | No inferred anatomy/quantity, no orphaned or duplicated outputs |
| Owner mutation, versioning, replay | D17 + MIB-03 | Receipt-like local rehearsal and later exact owner adapters | Only durable D17 owner receipts make canonical outputs real |
| Vehicle/mecha/ship/base components | MIB-14, OARC records | Installed slots, compatible hosts, subsystem state | No second compatibility authority, no universal vessel rules |
| Crafting, repair, refurbishment | MIB-12 + LSS-08 | Repair inputs, donor parts, workbench handoff | VCSR does not invent recipe/refund policy |
| Pricing and trade | MIB-13 | Credit quote/reference and transaction intent | XP must not be spent on physical vehicles/parts; no client-authored universal market price |
| Downtime, long projects | APW/D26 | Request/approval/status with local demo clock when needed | Downtime owns campaign clock; project use not forced to a campaign |
| Maps and space | MMHT + MIB-11/D18 | Stable map/floor/feature/room refs, floor-space / volume later | MMHT owns geometry and topology; VCSR owns component use/recovery state |
| Environment, ecology, farming/foraging | ENV/ICF and existing World | Context/harvest handoff and authored constraints | LSS cannot absorb biology, flora or hazard resolution |
| Mining/geological extraction | DPL mining vertical | Map deposit/haul route and output handoff | Geological extraction is **not** LSS scavenging |
| Rewards, encounter aftermath, GM | GM, Action/Hazard/Encounter | Proposed loot, reveal and approval | GM/Action owners resolve checks, encounters, hazards and visibility |
| Player equipment/hangar | Character Builder, D17 | Later controlled imports/exports and interactive controls | Never treat a workshop demo as character progression or entitlement |

## Foundational invariants (all cycles)

1. A definition is not an instance. Each instance has stable identity, condition, quantity, owner, custodian, source, location and lineage; compatible stacking requires explicit matching keys.
2. Loot **moves** existing items; scavenge **selects an explicitly authored opportunity output**; salvage **extracts selected authored slots**. Their user interface may share a workbench but must retain separate resolution kinds.
3. No outputs or deletions without governed mutation evidence. Proposed, validated, calculated, approved and applied stages remain distinguishable. Do not impersonate D17 receipts with local simulations.
4. Partial salvage preserves *every* unselected slot, component, remnant, cargo container, active capability and relevant historical identity. Total teardown needs a separately authored rule.
5. No global conversion from rarity, level, condition, biome, or item category to find rate, yield, repair result, compatible fitting, DC or market price. Unknown remains visibly unknown and blocks commitment when mandatory.
6. Duplicate operation IDs, stale versions, canceled jobs, restored checkpoints, repeated imports, split stacks and retry after lost response must not create extra assets.
7. GM-only and player-visible data are filtered **before** search results, counts, previews, receipts and exports. HTML role toggle is merely a local preview, not real authentication.
8. Ship, mecha, vehicle, base, weapons, magic, tools and constructed objects reuse asset/component semantics but preserve their own rule profiles. No humanoid/universal equipment fallback.
9. Real map geometry, farming, mining, weather, biology, crafting and downtime remain with their existing authoring/execution owners. This tester consumes typed references and emits proposals, not replacement engines.
10. Every cycle can start from a fresh blank/illustrative fixture without a campaign, scene or live connection; when campaigns are present they are optional attached references.
11. Physical acquisition, components and repairs use **credits / materials / existing assets**, never XP, unless an explicit character advancement rule itself spends XP.
12. Noncanonical demonstration fixtures must be clearly marked and never represented as published Multiversal item statistics.

## Cycle roadmap

| Cycle | Increment to the cumulative standalone HTML | Must be testable before next cycle |
|---|---|---|
| **VCSR-01** | **Foundation and source crosswalk:** separate loot/scavenge/salvage, sample stock/opportunity/wreck, blocked unknown mecha/ship extraction, GM proposal→local commit, receipts, inventories, JSON checkpoint/handoff, built-in assertions | Authored Blackglass result; source leftovers; no duplicate; no hidden site in Player view; exports open |
| **VCSR-02** | Catalog and object search, object vs instance, categories/facets, full descriptions, containers, nested storage, discrete lot/stack handling, complete loot and explicit drop profiles | Carry, split, reserve, take, leave, move and restore without duplication; no random unauthored drops |
| **VCSR-03** | Scavenge site authoring, time/tools/skill references, visibility, specific opportunity outcomes, concentration, access, discoveries, finite depletion and hazards | Search/retry/deplete; unresolved concentration blocks inference; hidden areas never leak through counts |
| **VCSR-04** | Recoverable object and assembly graph authoring, critical vs optional slots, subassemblies, source remnants, partial/full salvage preview | Choose parts from a rover, weapon, base machine; untouched slots and nonrecoverable ones remain correct |
| **VCSR-05** | Exact operation IDs, version/reservation protocol, atomic output/source-replacement rehearsal, status-first replay/recovery and compensation | Lost response/duplicate approval/reimport/cancel/stale-source scenarios conserve quantities |
| **VCSR-06** | Condition, durability, manufacture quality/grade, rarity and component provenance, damage and extraction outcome rules | Clean/damaged/failed extraction differs only through authored source rule; no rarity-to-yield inference |
| **VCSR-07** | Component-family and cross-domain object library (weapons, armor, EVA, technology, magical devices, machinery, traps, construct parts and bases) | Source-backed profiles usable; missing component anatomy marked unresolved |
| **VCSR-08** | **Ground / water / air vehicle builder**: chassis, modules, mounts, capacities, movement profile references and stored owned instances | Create / configure / remove / install / inspect without re-creating asset definitions |
| **VCSR-09** | **Mecha builder**: frames, limb/local subsystem slots, power/heat, pilot link, damage targeting, ejection and transformation-state references | Correct distinction between pilot, frame, components, occupants, cargo and effects |
| **VCSR-10** | **Ship / starship builder**: hull, power/propulsion, crew stations, nav/comms/sensors, environment/life-support, cargo/hangar and dimensional travel extensions | Specialized systems do not inherit inappropriate universal vessel formulas; crew permissions explicit |
| **VCSR-11** | Component system runtime: power/fuel/heat/ammo/charges, dependency propagation, damage, disabled functions, repairability and station controls | Lose a module and see dependent capability disabled; retain module instance and history |
| **VCSR-12** | Repair, refit, upgrade, cannibalize, substitute, reassemble and donor-part integration with MIB-12/14 plans | Compatible donor/source/target; record inputs, leftovers, outputs and explicit failure cases |
| **VCSR-13** | Storage, capacity, cargo handling, workshops, base facilities, crew assignments and hangar service flows | Board/exit/assign/retrieve/store components and payloads; show capacity and permission failures |
| **VCSR-14** | MMHT map/floor/room and ship-deck reference adapters; spatial installation, wreck location, reachable salvage point, storage, mining-route handoff | Round-trip references preserve mapId/revision/featureId; do not run map geometry or mining engine |
| **VCSR-15** | Downtime/APW long-duration salvage and service projects plus environment/ICF/DPL boundary adapters | Pause/resume/approve against imported time; ecological harvest/mining route to their owners, not LSS |
| **VCSR-16** | GM/Character bridges: encounter loot, permissions, character inventory, equipment/hangar and party custody, preview-only role gating | Player proposal, GM acceptance and conservative JSON handoff; no hidden GM data in player exports |
| **VCSR-17** | Economy/legal risk and scenario loop: credit costs/market quotes, rare/substitute component demand, hazards, claims, settlements and Cozy stop markers | No XP gear purchases; hazard/legality and pricing remain explicit owner handoffs |
| **VCSR-18** | End-to-end golden proof and UX/accessibility/conformance: locate wreck → inspect → scavenge → strip → repair → mount/use → transfer/store → restore checkpoint | Multiple independent fixtures plus real export/import rehearsals, responsive/keyboard checks and evidence crosswalk |

Cycle order is the approved planned sequence; a `Continue` in the VCSR conversation requests the next bounded cycle and **a fresh complete HTML snapshot**. No automatic commits to, or rewrites of, the other HTML testers. Other program implementations and OPS5 persistent lanes retain their existing selections.

## Cycle 01 proof and limitations

Cycle 01 is a **demonstration contract simulator** with an illustrative cargo locker, **LSS-10 authored Blackglass 2-piece brass scrap outcome**, illustrative multi-slot utility rover, and inspection-only Hollowstep mecha / unknown ship. All original source rules are either cited or labelled illustrative. The browser in-page check suite covers eight local invariant scenarios. Direct calls into `packages/contracts/src/loot-scavenge-salvage`, D17, GM, Character, MMHT and Downtime are deferred to their bridge cycles.

**Evidence to record per cycle:** filename/hash, functional changes, provenance/authority crosswalk, browser test results, manual owner feedback, unresolved unknowns, new adapters, import/export shape, acceptance status and the next bounded cycle. The HTML is the review artifact; any proposed OPS5 change is canonical only after governed PR publication.

## Source baseline

- AIOC OPS5: `operations/BOOTSTRAP.md`, `OPERATING_CONTRACT.md`, `CURRENT.json`, `LANES.json` on `main` (2026-11-22).
- AIOC LSS program, LSS-01 source authority crosswalk, and terminal LSS-10 checkpoint/backlog.
- Multiversal-app LSS-05 authored opportunity engine inventory, LSS-06 extraction inventory and LSS-10 content-workbench/golden inventory.
- Project Bible reference §§ 12–13, 19–24; Feature Bible V02–V07; Screen Bible V03, V08, V10, V13; UI Bible foundation/components/runtime.
- DB-004 reference: item/vehicle/mecha/ship, crafting/economy, exploration/environment, downtime/project game-framework chapters.
- Attached baseline testers: GM Cycle 33, Character Builder v19, MMHT Illustrated 66 Maps UX 04, Downtime Cycle 07.
- Explicitly not superseding OPS5 CURRENT-selected work in GPR, MTLC, AXI, GM Workspace, MMHT or other lanes.