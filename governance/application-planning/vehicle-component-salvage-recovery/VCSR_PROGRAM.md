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

## Cycle 02 — Asset catalog, containers, lots and authored drops

**Artifact:** `artifacts/Multiversal_VCSR_Cycle_02.html` (complete, cumulative standalone HTML). SHA-256 `fde1ed6427e368f38a81ff55eab8084cf5fecc203c2bde1d02dc3bc64ff16add`.

Cycle 02 adds 14 searchable item/component definitions with descriptions, source status, explicit definition-versus-physical-instance separation, five storage surfaces (including a GM-only workshop and a pouch attached to its anchor item), fractional-stack splitting, reservation/release, item transfer/take/leave/return, explicitly compatible lot merging and authored one-use drop opportunities with mandatory rule/evidence/quantity/provenance. Existing VCSR-01 workbench flows, partial salvage and role-filtered handoffs remain available. Imports accept VCSR-01 checkpoints as upgradeable demonstration fixtures; exports use VCSR-02 checkpoint/handoff schemas.

**Validation:** 8/8 original VCSR-01 embedded checks + 12/12 new cycle invariants in isolated browser fixtures at Chromium desktop 1280×850 and mobile-width 390×844, zero page errors or horizontal overflow. Browser exercised search, split, item transfer, authored drop proposal/approval, GM checkpoint download/reopen parity, player-safe site/storage/catalog filtering and redacted handoff. The actual D17/MIB-03/LSS-04 TypeScript engine and native Android/Unity remain **unconnected and unverified**, as intended for this standalone cycle. Capacity is an explicitly illustrative count of stack slots; pricing, equipment bonuses, vehicle compatibility and generated random drops are deliberately absent.

**Ops5 publication boundary:** This cycle is staged on a separate branch/PR *stacked on* VCSR-01 registration PR #2019. Neither operation becomes canonical on protected `main` until the required publication validation and merge occur. VCSR-03 remains the planned next user-directed HTML cycle; there is no automatic successor or change to GPR/CWKS/MTLC/MMHT/GM/Character/Downtime implementation work.

## Cycle 03 — Scavenge zones, authored search, finite depletion and discovery

**Cumulative standalone artifact:** `artifacts/Multiversal_VCSR_Cycle_03.html`  
**SHA-256:** `21008e8a3f0e5a1f1bf3d9a3822335fff2967b222f5fed800b1a28c6741cfd37`  
**Local file size:** 171,066 bytes

### Authored source alignment

LSS-05 `scavenge-opportunity-engine.ts` owns the *orchestration reference contract* over stable `MIB-11/D18` World locations, separate `LSS-05-OPPORTUNITY` version/depletion state, `D17` output intents, `MIB-03` operation/receipt semantics, and external Character/Profession and Hazard/Action/GM requirements. The tester retains separate scavenge, loot, authored drop, and salvage paths. Its local state is **not** a live LSS-05 owner or D17 mutation.

- Governed Blackglass starter profile `scavenge-opportunity:blackglass-wreck-yard` includes exactly its authored permit, salvage pry kit, industrial scavenging capability, unstable wreckage hazard, known clustered concentration, `outcome:wreck-yard:surface-brass` and 2-piece `material:lighthouse-brass-scrap` output. The new Scavenge Zones screen and the original Workbench Blackglass case **share one depletion source**, preventing double collection across the two UI paths.
- Source-backed `scavenge-opportunity:remote-derelict` has a known World location but unknown concentration and **no authored outcome**; the UI and operation planner must not invent an item or roll.
- Starter `scavenge-opportunity:herb-patch-handoff` and `scavenge-opportunity:ore-vein-handoff` refuse LSS asset mutation and route to ICF/ICF-07 and DPL respectively.
- Explicitly **illustrative** relay outpost and GM-only storage fixtures exercise authored finite use counts, tool/permission evidence, required hazard referral, redacted results and local checkpoint roundtrip. User-authored single-output opportunity creation/editing is supported. Governed source fixtures are read-only; no user edit reinterprets them as published source canon.
- Search text/tags/World reference queries, result counts, selection, disclosure, receipts and player handoffs are visibility-prefiltered. Player previews never receive the GM-only fixture or its outcome cardinality.
- Search times, permits, skills, capability values, discovery, environment/hazards and GM decisions remain owner references and human stops: the HTML does not roll a D20, assign skill/DC/damage, select random drops, infer yields/concentration, advance a campaign clock, mine ore or harvest living plants.

### Local acceptance receipt

**Chromium / Playwright**: 8/8 Cycle-01 checks, 12/12 Cycle-02 checks, and 18/18 new Cycle-03 checks = **38/38**, at both 1280×850 desktop and 390×844 mobile width, without JavaScript page errors or horizontal overflow. Manual browser walkthrough: relay search with explicit tool/access and external hazard referral → GM review → 2 local commits → finite depletion and disabled further proposal; unknown concentration/outcome block; author new opportunity; player-hidden GM cache/catalog exclusion; filtered JSON handoff; actual GM JSON checkpoint download and file reopen with 2 committed receipts and 7 profiles.

**Proof boundary:** This validates only standalone HTML behavior and demo contract conservation, not real D17 durability, LSS-05/MIB-03 runtime parity, World location access, live GM authorization, Android/Unity networking or integration with the other independently running testers.

**OPS5 status:** Staged via a separate stacked draft PR from VCSR-02 PR #2021 (which itself depends on VCSR-01 PR #2019). Publication on protected `main` is still pending prescribed CI/merge/reconciliation. The HTML file is available for owner review now; VCSR-04 is the next owner-directed planned test cycle.

## Cycle 04 — Recoverable component and subassembly graphs, partial extraction

**Cumulative standalone file:** `artifacts/Multiversal_VCSR_Cycle_04.html`.  
**Final local SHA-256:** `265a94aea33c0d265098337b9badf97d9bebe3163cd27d0139d472ee519efdd9`  
**Final local size:** 248,222 UTF-8 bytes. The file is self-contained; prior Cycle 01, 02 and 03 files are not external runtime dependencies.

### Scope and authority

This tranche follows the live Multiversal-app LSS-02 recoverable-object grammar and `LSS-02_ASSEMBLY_LINEAGE_DEPLETION_REFERENCE_ADDENDUM.md`, including source-definition references; D17-shaped physical source identity/version; zero/one/many authored recoverable slots; condition/criticality/recoverability distinctions; explicit parent→child evidence; authored quantities; source remnant behavior and provenance. The LSS-06 extraction inventory and engine govern inspection, partial selection, requirement/condition gates, preservation of unselected slots, total teardown rule gating, and atomic source/output D17 owner-intent semantics. **This HTML simulates local approvals; it does not emit a real durable D17 receipt or execute MIB-03 reservation.**

The assembly page provides seven role-filtered starter objects: the exact governed synthetic LSS-02 zero-slot collapsed masonry, one-slot storm lantern, two-slot utility rover (fixed one auxiliary power module; unresolved sensor-mast quantity), and four explicitly illustrative workshop device, field weapon, nested comms, and GM-only ship profiles. The governed LSS-02 rover has its **own distinct physical demo source instance**, separate from Cycle 01's illustrative utility-rover slots, preventing cross-profile duplicate grants. All display names, tool bonuses, durability and material values outside source are explicitly illustrative or unresolved.

A standalone GM authoring desk supports custom profile creation, parent-child slots with explicit edge evidence, recoverability, criticality, detachment mode, requirement references, known output-definition selection, positive authored fixed quantity or unresolved output, and remnant modes. It supports updating **local illustrative** profiles; immutable governed starter fixtures are not silently overwritten. Profile-version changes invalidate pending operations.

A selected parent slot cannot implicitly destroy/detach child slots. Independent leaf removal preserves the parent; an explicitly authored intact-subtree detachment carries nested children without separately outputting them; selecting both parent and its carried child fails. All unselected nodes stay present. Fully selecting recoverable slots in **partial** mode does not destroy the source; total teardown also requires an explicit exact source rule and removal-compatible authored remnant behavior. Not-recoverable slots and unresolved quantities fail closed. The local D17-shaped inventory records distinct output identity, source slot, lineage and owner/custody reference; duplicate operation ID replay does not duplicate output; stale physical-source or authored-profile versions reject atomically.

Cycle 04 checkpoint format imports Cycle 01–03 and reopens Cycle 04 with source graphs and receipts preserved. GM-only source topology, output cardinality and receipt data are filtered before player source search and handoff; no hidden-source count is returned. The owner-provided GM, Character, MMHT and Downtime HTML testers remain independent and unmodified. Runtime vehicle/mecha/ship builders are later VCSR cycles, not implied complete by assembly authoring.

### Evidence and bounded limitations

- **Chromium Playwright, full actual offline HTML via `page.set_content`** at 1280×850 and 390×844: **8/8 Cycle 01 + 12/12 Cycle 02 + 18/18 Cycle 03 + 26/26 new Cycle 04 = 64/64 green**, no reported JavaScript errors or horizontal document overflow.
- Manual UI verified lantern slot inspect → propose → local GM approve → physically distinct inventory output with lineage; actual checkpoint JSON download and re-import preserving committed source and receipt; player-only list excludes GM-only ship; player JSON handoff excludes hidden source ID/topology; existing Cycle 01 loot flow retains functionality; Cycle 02 inventory movement and Cycle 03 authored scavenge commit still function on `schemaVersion:4`; custom GM authoring form retains entered source facts when adding slots and publishes an eight-assembly workspace.
- **Not proven:** live D17 atomic mutation, MIB-03 reservation/resulting owner version/replay status query, real Character/GM auth, true MIB-14 compatibility, browser sandbox local HTTP serving, Unity/Android/two-device LAN, physical hardware, material yields, condition damage, resource costs or downstream map/downtime integration. Those are future governed scope.

**OPS5:** VCSR-04 is staged as a fourth draft PR **stacked on VCSR-03 #2022**, itself following #2021 and #2019. This is an on-demand standalone tester chain; there is **no protected-main publication** until the required exact-head review, merges and canonical `operations/CURRENT.json` reconciliation. The next owner-directed planned cycle is VCSR-05 (operation ID, reservation, receipt, idempotency and lost-response recovery).
