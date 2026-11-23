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

## Cycle 05 — Stable operations, source reservations, atomic commits and status-first recovery

**Complete cumulative standalone artifact:** `artifacts/Multiversal_VCSR_Cycle_05.html`.  
**Local SHA-256:** `9b5536dd78b7861b4ba9e5d6b612a72ec8b1b1cbd82013f54a1896369b9acb69`; **308,334 UTF-8 bytes**.

### Functional extent

Cycle 05 retains every independent Cycle 01–04 browser workflow and adds a dedicated **Operation Safety** lab. It models immutable operation IDs, idempotency/correlation keys, a local noncryptographic fingerprint, versioned source/profile inspection, one active reservation per physical source, and a D17-shaped owner receipt with returned **nonsequential** owner versions. GM-visible actions independently dispatch the reservation and atomic extraction commit, with selectable **normal reply**, **owner executed but response lost**, or **request never delivered** cases.

- **Planning** is read-only and writes no physical inventory. Identical operation ID + identical immutable payload replays the plan; the same ID with different destinations/output data is rejected.
- **Reservation** requires exact inspected source and profile version and a locally role-gated GM action. Its demo receipt supplies `resultingVersion`, rather than assuming old version +1. Competing reservations and legacy extraction attempts on that source are blocked while it is held.
- **Atomic extraction** consumes the checked *post-reservation* owner version and uses the prior LSS-02/06 local assembly extraction pathway to produce one source-slot transition plus authored physical outputs. The demo mock owner reports a second nonsequential commit version and durable result/evidence reference.
- **Lost response** produces an ambiguous stage: commit/retry/cancel cannot continue until the operator queries the mock-owner status. A present matching receipt is replayed without a second output. Known no-result permits a retry **using the identical immutable intent**.
- **Cancellation** before reservation has no owner mutation; cancellation of a confirmed reservation emits an explicit release receipt with a returned version, without producing loot. Synthetic competing owner-version changes fail closed. Receipt tampering, duplicate receipt identities, unknown yield, missing tool references and stale authored profiles are regression-checked.
- **Persistence and sharing**: full GM checkpoint reopens Cycle 01–05 state including ambiguous steps, mock reservation/commit/release receipts, physical outputs and untouched slots. A player handoff first filters GM-only assembly and operation references/receipt counts. Existing other testers remain independent; no file is imported automatically into GM, Character, MMHT, Downtime or Unity.

### Governing contract and evidence

Implementation is a **local contract illustration**, not a new canonical engine: `packages/contracts/src/runtime/deterministic-runtime-primitives.ts` (MIB-03 stable operation, version gate and safe-retry decision) and `packages/contracts/src/loot-scavenge-salvage/salvage-extraction-engine.ts` (LSS-06 exact post-reservation version, atomic source/output commit and durable receipt confirmation) control future adapters. D17 retains canonical Asset mutations and identity. The HTML cannot claim real D17 owner receipts, authentic cryptographic evidence, production idempotency guarantees or network-backed status lookups. The demo FNV-32 fingerprint/checksum is an instructional integrity signal, **not** security-grade signing. No real expenditure, equipment compatibility, campaign clock or hazard action is resolved.

**Browser validation:** Chromium Playwright on the full offline file via `set_content`, 1280×850 and 390×844: **8/8 Cycle 01 + 12/12 Cycle 02 + 18/18 Cycle 03 + 26/26 Cycle 04 + 30/30 Cycle 05 = 94/94**. Zero JavaScript page errors and no horizontal document overflow at these viewports. Manual browser walkthrough: plan lamp lens → mock-owner reservation with lost response → owner status query → atomic commit with lost response → owner status query → replay without duplication, followed by actual GM checkpoint download and fresh-page import, role-filtered player handoff and legacy Cycle 01 loot operation.

**Publication status:** This is a separate OPS5 stacked draft PR following VCSR-04 #2024 → VCSR-03 #2022 → VCSR-02 #2021 → VCSR-01 #2019. `main` is not modified, and prior drafts must be published/reconciled under exact-head guards before advancing the stack. Next owner-directed standalone artifact is **VCSR-06** (condition, durability, quality/rarity provenance and only source-authored damaged/failed extraction outcomes).

## Cycle 06 — Condition, Durability, Quality, Grade, Rarity and Recovery Outcomes

**Artifact:** `artifacts/Multiversal_VCSR_Cycle_06.html`, complete cumulative portable offline HTML. **SHA-256** `646c1d0899c5f597a9e8aff601906e66e378304506716d556d79876519364d97`; **376,219 bytes**.

The new **Condition & Outcomes** view preserves Cycles 01–05 and exposes independent, evidence-backed reference facets. The Multiversal-app LSS-03 governed **synthetic starter fixture** is reproduced precisely as a contract illustration: precision tool masterwork/industrial-grade/rare; legendary-only with quality/grade unknown; auxiliary-power service-grade with *one exact* MIB-14 rover compatibility reference; D17 precision-tool condition:damaged at version 7. No such synthetic fixture is portrayed as a published Multiversal item rule. Condition/history is an instance snapshot reference owned by D17; quality, grade and rarity are definition facts; MIB-14 compatibility requires its explicit own evidence. Durability is shown only if a current, maximum, unit and evidence reference are explicitly provided. The `3/12 demo-points` generator figure is an **illustrative authored sample**, not a universal durability rule or automatic damage converter.

The browser includes an owner-scoped local authoring desk for illustrative condition snapshots, definition facets and exact recovery rules. The four generator and one field-sidearm authored outcome samples are explicitly **synthetic VCSR-06 fixtures**, not production LSS-06 rules. They exercise `extracted`, `damaged-extracted` (explicit output condition + condition rule), and `failed-no-output` (explicit failure rule, slot-remains or rule/evidence-backed slot-damaged). Failed outcomes produce *zero physical loot*, preserving source slots unless a specific authored damage transition exists. Unknown output quantity or missing evidence is not inferred. Full condition/durability/quality/grade/rarity/economy conversions do not exist.

The outcome lab reuses Cycle-05 stable job identity and mock-D17 reservation/atomic-commit receipts; its source-condition projection follows the **owner-returned** post-reservation version. Lost replies query mock owner status first; replay yields no duplicated component. The simulation is neither a real D17 condition ledger nor a real MIB-03 receipt, GM authorization, MIB-12 repair, MIB-13 price, MIB-14 compatibility engine, Unity app or LAN deployment. GM, Character, MMHT and Downtime testers remain independent.

### Local proof

Chromium Playwright `set_content` of the **entire actual file**, desktop 1280×850 and mobile-width 390×844: **130/130** built-in checks (8+12+18+26+30+36), no JS page errors and no horizontal overflow. Manual GM path: plan authored damaged generator regulation core → reserve response lost → mock owner status query → atomic commit response lost → status query/replay: **one** condition:damaged component with explicit rule, remaining coil preserved. Actual GM JSON checkpoint downloaded and reopened in a fresh browser page with two mock receipts, four condition snapshots and job stage preserved. A second field-sidearm optic extraction succeeded after reimport. Player role disabled owner dispatch, and player JSON filtered GM-only ship, private facet and condition references. Original Cycle01 loot still committed on schemaVersion6.

**Sources:** Multiversal-app `LSS-03_LIVE_CONDITION_QUALITY_RARITY_GRAMMAR_INVENTORY.md`, `condition-quality-rarity-grammar.ts`, `lss-03-starter-library.ts`, LSS-06 extraction inventory; D17/MIB-03 owner contracts; VCSR Program and previous tester artifacts.

**OPS5:** VCSR-06 is a draft PR stacked behind #2026 → #2024 → #2022 → #2021 → #2019. Protected-main publication and canonical CURRENT reconciliation remain pending; all other lane state is preserved. Next owner-directed cycle: **VCSR-07 reusable component families** across weapon, armor, EVA, technology, magic, machinery, traps, constructs and bases with explicit unknowns.

## Cycle 07 — Cross-domain component families and exact decomposition registrations

**Cumulative standalone HTML:** `artifacts/Multiversal_VCSR_Cycle_07.html`. **SHA-256:** `d7aa25abd80fb35fb293d9b12a992371b464a57a1a2b583a253187f4e975d10d`; **430,534 UTF-8 bytes**; exact Git blob `7f1ee8f0fba775d9b2bb8332de9f21e1741bbbdf`.

### Source-governed LSS-07 coverage

The library is based on the *actual* Multiversal-app `LSS-07_LIVE_COMPONENT_FAMILY_LIBRARY_INVENTORY.md`, `component-family-library.ts`, and `lss-07-starter-library.ts`. Eight governing taxonomy families are included: Explorer-class mecha, authored traps/hazards, carrier-class spacecraft, vehicles, computers/electronics, bases/facilities, weapons, and magitech devices. Four specific reference profiles use stable exact source and provenance binding:

| Registered source | Authored recoverable names | Status |
|---|---|---|
| Mecha MCH-0031 **Primax RX-07 Hollowstep** | Cloaking Shroud, Adaptive Limbs, No-Flash Drive Core | 3 names, quantity **unknown** |
| Mecha MCH-0032 **Falconex Skyray Veil Dancer** | Solar camo weave, Wind-Mapping AI core, Glider wing assemblies | 3 different names in the **same Explorer family**, quantity **unknown** |
| HTR-0079 **Frost Wire** | Trigger, housing, payload, focus, sensors, wiring, mechanisms, reusable materials | 8 authored categories; quantity **unknown**, hazard resolution external |
| Spacecraft SCF-0027 **Orrukhal Bastion-Class Carrier** | **Zero** authorized salvage slots | `Installed_Modules` is configuration, not salvage-output evidence |

Three source-hash anchors are retained in source references (Mecha `60ff6a73…`, Hazards/Traps `39185483…`, Spacecraft `00ce4a9d…`). All unprovided output quantities remain explicitly unresolved. The category/family labels never synthesize anatomy, yield, compatibility or physical Assets.

### New interactive surfaces

A new **Component Families** screen supports name, alias, tag, domain and exact source-reference search; classification cards and exact registered-profile cards have distinct presentations and detail inspectors. User-visible family and registration counts are computed only **after** visibility filtering. Inspectors show source evidence, provenance, registered slots, output definition references, quantity status, category, exact compatibility authority and identity. A registration reference may be exported as JSON without performing an extraction.

To prepare later cross-system work, six additional category families (armor, EVA/environmental suits, machinery, constructs, tools and other authored devices) are marked **VCSR-07 illustrative classification only**, with zero decomposition profiles and no automatic outputs. The terms are cross-domain coverage scaffolding, not claimed as canonical governed LSS-07 starter categories.

GM-only local authoring can add a classified family with required evidence, tags, aliases and audience; then explicitly register an **already authored VCSR-04 assembly** by its exact physical definition and source evidence. Linking a graph preserves its authored slot quantities, including unresolved ones; it neither creates an Asset nor silently mutates that assembly or any D17 state. Duplicate registration, nonexistent family, private-to-player escalation, source evidence drift and edits to canonical source-backed fixture profiles fail closed. Player role previews and JSON handoffs redact GM-private classifications, linked assembly topology and hidden source IDs.

Cycle 07 adds `schemaVersion:7` checkpoint and filtered JSON family/profile references while retaining Cycle01–06 state, import compatibility, scavenge, inventory, assemblies, condition and operation safety. No link into GM, Character, Map Maker, Downtime, Unity or production D17/MIB-03 systems has been activated.

### Verification

**Chromium/Playwright full actual offline HTML** at 1280×850 and 390×844: **169/169** embedded regression checks—Cycles 01–06 `8 + 12 + 18 + 26 + 30 + 36 = 130`, plus **39/39** new Cycle-07 checks. No JavaScript page errors or horizontal document overflow at either viewport. The first new-layer run found four regressions (older storage/scavenge checkpoint dispatch and source-fixture mutation guard); these were repaired before the final complete run.

Manual two-browser walkthrough: exact Hollowstep alias search; carrier profile shows zero authorized slots; GM creates a private classification, links existing two-slot relay comms graph, and downloads a real JSON checkpoint. In Player preview neither private family nor registration appears, and the actual downloaded role-filtered handoff excludes their IDs and hidden ship. A fresh mobile-width browser imports the downloaded GM file and retains **15** families and **5** exact registrations. Original source-governed 8/4 starter fixtures remain intact. Source-backed and illustrative records are clearly differentiated.

**Authority boundaries:** LSS-07 owns classification/registration references only. LSS-02 owns authored decomposition shapes; LSS-06 orchestrates salvage; D17 owns physical assets/condition/history; MIB-14 compatibility; MIB-12 repair/reassembly; ICF-07 biological harvest; MIB-13 economy. No universal loot, rarity/yield, source condition, install rule, extraction success or source durability is inferred.

**OPS5:** VCSR-07 is staged as an additional **draft stacked PR** based on VCSR-06 #2028 (preceded by #2026, #2024, #2022, #2021 and #2019). Protected-main publication still requires the governed exact-head PR chain and canonical selector reconciliation. No other OPS5 lane is changed.

**Next owner-directed cycle:** VCSR-08, ground / water / air vehicle builder (chassis, mounts, components, authored capacity/movement and asset identity).

## Cycle 08 — Ground / water / air owned vehicle builder

**Complete cumulative standalone file:** `artifacts/Multiversal_VCSR_Cycle_08.html` — SHA-256 `e8ed3ecf7dd6498ef92318714ae216315dc77e5510e991434ff9b315f71265f6`, **524,232 UTF-8 bytes**; exact Git blob `9608a17e0d0d189e3d37a42770161d82dd41fa76`. The file retains every prior Cycle 01–07 UI, local owner simulation, import/export and evidence suite.

### Source provenance and scope

Read Multiversal-app `MIB-14_LIVE_VEHICLE_PLATFORM_BASE_INVENTORY.md`, `vehicle-platform-base-engine.ts`, `mib-i14-starter-library.ts`, `smb-06-full-vehicle-system.ts`, plus project `FEATURE_BIBLE.md` Volume 6 (Vehicle framework, ownership/crew/cargo and governed update pipeline) and `PROJECT_BIBLE_OPS3_REFERENCE.md` §24.9–10. Physical identity and custody remain D17, configuration/slot/power/cargo/crew checks MIB-14, stations A8 / Character, World/location MIB-11/D18, movement SMB-04/D28, campaign time APW/D26, repair MIB-12, trade MIB-13. The UI models reference projections and local mock receipts, never canonical owner actions.

**Governed MIB-14 starter data reproduced as reference:** `vehicle:utility-rover-standard` (ground, slots 6, cargo-mass cap 500, power cap 10, fuel cap 100, minimum 1/maximum 4 crew, `pilot` required, `movement:ground-wheeled`) and the four distinct module definitions `module:cargo-rack-standard` (slot 1, installed mass 20, cargo delta +250), `module:sensor-mast-standard` (slot 1, mass 15, power 2, station sensor), `module:auxiliary-power-standard` (slot 1, mass 30, power delta +8), and `module:heavy-turret-standard` (slot 3, mass 180, power 8, requires `mount:heavy` definition tag). They are **MIB-14 governed synthetic starter fixtures**, not newly inferred Multiversal-wide vehicle statistics. The Utility Rover's physical mounting layout is **VCSR-08 illustrative**, because the MIB-14 source does not define hardpoint positions.

Two additional **explicitly illustrative** chassis `fixture:chassis:marsh-skiff` (water) and `fixture:chassis:sky-surveyor` (air), plus two domain-specific demo modules, allow different settings/classes without claiming source-authorized speeds, movement rates, fuel consumption or real operational fit. The aircraft demo has deliberately `null` fuel capacity. Three player-visible demo owned vehicles, a GM-only airframe and nine distinct preowned component Assets are local test identities. **The chassis definition is never the physical Asset**.

### Functional tests

- **Fleet builder:** filter owned vehicle by name/owner/chassis/domain, inspect source-backed class and per-instance owner/custodian/location/version, provenance/evidence and explicit movement/location refs.
- **Mounts and owned components:** choose a physical stored component Asset; require an explicit demo mount/module allow-list *plus* MIB-14 kind/class/tags, occupied mount, slot budget and power budget; install/uninstall and return the **same instance ID** without creating extra assets; reject missing inventory, wrong owner, stale version and duplicate operation mismatch. Installation on a source-backed rover does **not** overwrite the separate LSS-02 rover salvage definition.
- **Crew and cargo references:** pilot station minimum/maximum and added module station checks, multi-station constraint, source-evidenced external Character/crew refs, and D17-shaped cargo source/mass/quantity; no actual Character skill grant, item movement, inventory mutation or priced consumption. Over capacity, self cargo loop, duplicate cargo, absent evidence and invalid station fail closed.
- **Authoring desk:** GM can author exact local ground/water/air chassis definitions with sourced numeric capacities/movement/terrain refs, custom mounting points with explicit allow-list, a new physical owned demo vehicle referencing an existing chassis, and preowned demo component identities with external acquisition evidence. Governed MIB-14 fixtures are immutable; a custom chassis definition cannot be edited after a physical instance references its old version. None of these actions imply an earned reward or deduct XP/credits.
- **Saving/visibility:** imports Cycle 01–08 checkpoints; exports full GM JSON or player-visible JSON after GM-only instances/stock/provenance/count filtering. No other HTML tester is imported, mutated or linked automatically.

### Validation

**Chromium Playwright** on the complete actual self-contained HTML using `page.set_content`: original **169/169** tests (8+12+18+26+30+36+39) plus **60/60** Cycle-08 checks = **229/229** at desktop 1280×850 and mobile-width 390×844, zero page JS errors and no document horizontal overflow. New tests include exact MIB-14 number/compatibility preservation, source/template immutability, ground/water/air isolation, unique component identities, mount install/remove/reinstall, duplicate-id replay, stale versions, authoring, cargo/crew rights, checkpoint tampering and previous Cycle-01/02/03/05/06 operation behavior on `schemaVersion:8`. Two compatibility defects discovered in focused tests were corrected: an inherited loot test used the wrong expected-version field and legacy condition/extraction needed cumulative checkpoint validation rather than v6-only.

**Actual UI browser interaction:** installed and removed the exact rover cargo rack, mounted rover sensor, added 60 mass units in D17-shaped cargo references; mounted water sounder and flight stabilizer; authored a new Crosswind air chassis with source and mount evidence, added a second mount, created a *GM-only* physical vehicle from that definition and assigned a pilot. Downloaded a real GM checkpoint (schema 8, 4 chassis, 5 owned vehicles, 10 local mock receipts), then reimported it in a fresh 390px browser; physical module bindings and crew persisted. Switched to Player; visible vehicle count 3, no GM authoring/installation controls; downloaded player handoff that excluded both private airframes and their private module identities.

**Non-authority:** No real D17/MIB-03 owner receipts, production authentication, installed Unity/Android apps, two-device LAN, movement/fuel/repair simulation, purchases, XP or economy, live MIB-14 service, ship/mecha builder or cross-tester integration has been verified.

**OPS5:** This is a separate draft stacked PR based on VCSR-07 #2029, following #2028, #2026, #2024, #2022, #2021 and #2019. Protected `main` remains unchanged until exact-head CI/merge and selector reconciliation. No other persistent lane was rewritten.

**Next owner-directed cycle:** VCSR-09 — Mecha builder (frames, limb/subsystem mounts, pilot link, localized damage, energy/heat references and controlled module installation).

## Cycle 09 — Mecha Frame Builder, Physical Modules, Pilot & Occupants, Localized Conditions

**Cumulative single-file offline HTML:** `artifacts/Multiversal_VCSR_Cycle_09.html`; **SHA-256** `1dd7ea67ef2e4e4333cb311e35a966677a07b78e3d001576a2d5877b09c698bc`; **632,296 UTF-8 bytes**; exact Git blob `4bf539503f6bfb39b5f25122c339c1b638fafa2a`. It includes Cycles 01–08 in full, without fetching or modifying other independent testers.

### Governing sources directly reviewed

- Multiversal-app `packages/contracts/src/vehicle-platform-base/mib-i14-starter-library.ts`, especially `MIB14_HOLLOWSTEP` and `MIB14_AUXILIARY_POWER`;
- `governance/application-planning/multiversal-engineering-refit-assembly/MERA-13_VEHICLE_MECHA_STARSHIP_ENGINEERING_ADAPTERS.md`, and `mera-13-vehicle-mecha-starship-engineering-adapters.ts`;
- `governance/application-planning/operational-asset-readiness-closure/OARC-04_SPECIALIZATION_PROFILE_MANIFEST_v1.0.0.json` for sourced/unresolved EP, heat and engineering topology semantics;
- LSS-07 Hollowstep salvage library already validated in Cycle07; MIB-14 vehicle owner and source-specific configuration engine reviewed for Cycle08.

MIB-14's **owner-backed Hollowstep operational definition** is exactly `mecha:mch-0031-hollowstep`, 5 configuration slots, 250 cargo-mass capacity, 1 pilot / 1 crew maximum, power capacity 60 configuration units, `interface:neural` tag and movement refs `movement:ground-walker:40ft`, `movement:air:20ft`, `movement:water:20ft`, `movement:jump-burst:20ft`. Source material supplies neither a universal EP pool nor a heat value; those remain **unknown** for this fixture. The source-defined power capacity is **never** mapped to EP or heat. MIB-14's reusable auxiliary-power unit is kept exactly one slot, 30 installed mass, power draw 0, config power delta +8, with `mecha` an explicitly allowed kind. Installed modules must also pass exact local mount allow-lists and MIB-14 kind/class/tag, power and slot checks.

The LSS-07 salvage names `Cloaking Shroud`, `Adaptive Limbs`, `No-Flash Drive Core` are **only decomposition-profile names with unresolved quantities**, not an installed component catalog or automatic salvage output. The Hollowstep's six display areas and five mount positions are explicitly **illustrative VCSR-09 presentation mappings**, not a claim of governed anatomy. A second Bastion Strider and GM-private frame are also clearly labelled synthetic fixtures; the Strider's example `12/30 EP` and `3/8 fixture heat` are *authored demo owner snapshots*, not universal values.

### Executable local lab

A new **Mecha Builder** sidebar page separates:
- immutable mecha frame definitions vs individual D17-shaped owned physical mecha Asset IDs, owner/custodian/location/version;
- localized areas and explicit frame mounts vs existing separately owned physical module identities (mount, unmount, reinstall with same Asset ID);
- authored crew-station assignment, Character qualification/pilot link vs independently evidenced onboard occupants;
- cargo Asset IDs and quantity×mass references vs passengers, pilots, and installed modules;
- configuration power budget vs EP energy and heat projections; unknown numbers cannot masquerade as known;
- recorded per-area condition snapshot refs vs unprovided hit-point subtraction, dismemberment, repair, or game effects;
- owner-confirmed ejection event references vs actual actor relocation (only reference stored), and authored mode/transform state references vs automatic shape changes, speed or fuel calculations.

Every GM operation runs only against the tester's local mock-owner projection, with stable operation IDs, expected instance version, idempotent replay, duplicate-payload rejection, local rollback for invalid compatibility/over-capacity, evidence refs and nonauthoritative receipts. A conditional actor cannot automatically board or eject from the mecha; external Character/Action/World evidence is required. GM can author a locally evidenced new mecha frame, add an area/mount to an *unbound* custom frame, create a new owned demo Asset referencing an existing frame, and register an already-owned demo component with acquisition proof. Source-backed immutable frames/modules cannot be edited, and no physical item/vehicle/credits/XP is generated from a name, list, or chassis selection.

**Proof:** Full Chromium/Playwright actual offline document via `page.set_content`, desktop 1280×850 and mobile 390×844: **312/312** passing checks. Prior 229 tests (8+12+18+26+30+36+39+60), plus **83/83 Cycle09**. Zero page JavaScript errors and no horizontal overflow. Local UI walkthrough: mounted and unmounted same Hollowstep auxiliary power Asset; Strider heat 4/8 external snapshot, left-arm condition, separately boarded actor, ejection reference with **no occupant relocation**, cargo `asset:owner:toolkit` with 14 mass×2, owner-confirmed `mode:secured`; authored a custom frame and second area/mount and GM-hidden owned Moonwalker; saved real 146,552-byte Cycle09 GM checkpoint with four frames, four mecha and eleven local receipts, imported into a fresh 390px browser preserving all edits, and reopened the preexisting vehicle builder. Downloaded player handoff contained exactly two visible mecha and excluded hidden frame IDs, private mecha, private module identity and GM location.

**Non-authority:** No live D17 identity, reservation, condition ledger or durable receipt; no real MIB-14/MERA/PPIA-04/F014 transaction, player authentication, Character permission or ejection movement, World geometry, Action effects, combat, actual resource consumption, repair, Unity/Android/LAN devices or cross-tester synchronization. All demo source references are labelled; no product implementation authority is granted.

**OPS5:** VCSR-09 is stacked as a new **draft PR** based on VCSR-08 #2031 (after #2029, #2028, #2026, #2024, #2022, #2021, #2019). No protected-main publication until predecessor exact-head review/merge and selector reconciliation. All other OPS5 lane selection remains unchanged. Next owner-directed standalone cycle: **VCSR-10 Ship / Starship Builder**, including hull, power, crew stations, nav/comms, environment/life support, cargo/hangar and dimensional travel *reference-only* controls.

## Cycle 10 — Hulls, ship systems, crew, hangars and dimensional travel references

**Complete cumulative offline HTML:** `artifacts/Multiversal_VCSR_Cycle_10.html`; SHA-256 `77914f4b74bd19103dc816744abfb5a5dcf5177235a7420e5c3317c001d004f6`; **748,346 UTF-8 bytes**; verified exact Git blob `e2cf38fc932b7567f144a5ccc3a47f5b39239975`. The file contains the entire independently functional VCSR-01..09 runner in addition to Cycle10. It does not import other GM, Character, MMHT or Downtime testers.

### Governing sources and fixture separation

The actual Multiversal-app `packages/contracts/src/vehicle-platform-base/mib-i14-starter-library.ts` supplied the **source-backed synthetic owner definition** `ship:scf-0027-orrukhal-bastion-carrier`: `kind=ship`, `class=space`, `mount:heavy` tag, 12 slots, 400,000 cargo mass, 200–500 crew, stations commander/navigator/engineer/gunner, power capacity 110, fuel capacity 400, and source movement references `movement:space-sublight:1500km-per-turn` and `movement:ftl:carrier-gate-drive:15ly-per-jump`. Those movement strings remain **references**, not a new cost, range or route formula. No invented two-hundred-person crew list was inserted: the starter physical carrier has four source-reference station occupants and correctly remains under its minimum crew. Source modules/facilities reproduced with exact MIB-14 capacities: cargo rack (slot 1 / mass 20 / cargo delta +250), sensor mast (slot1/mass15/power2/station sensor), auxiliary power (slot1/mass30/config power delta+8), heavy turret (slot3/mass180/power8/requires `mount:heavy`), storage locker (facility slot1/cargo mass +500), repair workshop (facility slot3/power6), foodcraft station (facility slot2/power3).

The live `MIB-14_LIVE_VEHICLE_PLATFORM_BASE_INVENTORY.md`, `vehicle-platform-base-engine.ts`, `smb-06-full-vehicle-system.ts`, `MERA-13_VEHICLE_MECHA_STARSHIP_ENGINEERING_ADAPTERS.md`, `OARC-04_SPECIALIZATION_PROFILE_MANIFEST_v1.0.0.json`, `DevelopmentBible/02-game-framework/items-vehicles-mecha-and-starships.md`, and `MSS-10_LIVE_PORTAL_TRANSIT_INVENTORY.md` were inspected. MIB-14 governs configuration; PPIA-04/F014, D17 and MERA preserve existing owner state; A8/Character retains station grants, World/MIB-11/D18/MMHT route/spatial identities, SMB-04/D28 actual travel, MSS-10/GM access/gate decisions, MIB-12 repair and MIB-13 settlement. OARC-04 explicitly leaves detailed power-grid and life-support capacity **unresolved** absent direct evidence; a carrier's installed modules and cargo/fuel capacities do not provide atmosphere, hangar count or salvage yields. The LSS-07 SCF-0027 zero-slot salvage profile remains separate from installed operational modules.

Four additional hull **types** are clearly labeled VCSR-10 fixture demonstrations: Coastal Survey Cutter (water), Aether Sky Barge (air), Rift Survey Skiff (space/dimensional) and GM-private unlisted starship. Their mounting coordinates, room labels, modules, berths and demonstration capacities are not canonized. The Rift's `fixture:ship:dimensional-interface` is an illustrative component only; no cross-reality drive rules are inferred. Different hulls retain their allowed travel modes; `MSS-10` does not create a universal gate stability, cost, travel duration or route discovery formula. The Bastion hangar remains `unknown` despite a starter reference berth label.

### Interactive Cycle 10 functionality

- Owned ship roster, search, visible-only counts and per-instance D17-shaped identity, owner/custodian/location/version/evidence. Hull definitions never become free physical ships.
- Accessible hull area/condition layout, per-mount known-module allow-lists, source-correct kind/class/tag/slot/power/cargo checks; install/uninstall/reinstall retains the exact separately owned physical part. No component is auto-generated from a hull, crafting library, LSS salvage name, ship module label or equipment entry.
- Crew-station permissions (existing Character actor references), onboard occupants, D17 mass/quantity cargo projections, and MMHT-shaped hangar berth/space references remain separate. Unknown berth capacity or unassigned crew cannot be silently filled in. Cargo/berth identity and self-cycles fail closed.
- Distinct MIB-14 **configuration power/fuel capacities** vs current D17-shaped hull/shield/fuel/life-support readings. Known resource snapshots require explicit values, unit, external owner result and evidence; unknown has null numerical values. No automatic resource consumption or life-support determination. Navigation/comms/sensors/propulsion/power-grid are owner references, not equipment-name-based effect grants.
- Source-evidenced localized ship damage with no guessed HP, repair, armor/shield formulas or explosions. Transit proposals require exact hull travel mode, distinct World endpoint IDs, route/gate reference and authorized GM/gate access source; they preserve ship location and status. Hidden destinations remain filtered until owner authorizes visibility.
- GM-only local authoring for independent water/air/space/dimensional hull definition and numeric capacity evidence, extra areas/mounts and optional specific berths **before the hull is bound to an owned ship**; exact physical ship registration with acquisition evidence; pre-owned module reference registration without creating items, spending credits or XP. Governing MIB-14 fixtures stay immutable.
- Imports prior Cycle01–09 checkpoint formats and exports Cycle10 GM checkpoint or role-filtered player integration handoff. The first nine cycles' screens remain available. No cross-tester automatic connection is performed.

### Browser validation and limitations

**Actual self-contained HTML via Chromium/Playwright `page.set_content`**, desktop 1280×850 and mobile 390×844: **397/397 embedded checks** = original 312 from VCSR-01..09 plus **85/85 Cycle10**. No reported page JavaScript errors or horizontal overflow. Initial check failed on a duplicate JavaScript lexical binding; this was fixed. A later **83/85** exposed incorrect legacy registration/vehicle fixture references in test assertions; those references were corrected and replaced with a real old-vehicle module-install operation, then both widths passed 397/397.

Manual end-to-end GM browser actions: select cutter, physically mount/unmount preowned locker, add D17 cargo 8×5, assign a map-space-referenced hangar tender, externally evidence life support `4/6 GM:demo-units`; install Rift dimensional interface, submit source-bound distinct-endpoint/access-approved **nontravelling** request; author GM wave-skimmer hull, add second area/mount and a prebound hangar berth, then register a private owned ship. Downloaded actual **192,082-byte GM checkpoint**: `schemaVersion:10`, 6 hulls, 6 physical ships and 11 local owner-like receipts, then imported it in a fresh 390px Chromium page with all retained state and no errors. Player preview contained four visible ships, not six; downloaded player handoff excluded private ship, hidden starter hull, GM-only physical component and private location/ship references. Existing mecha and vehicle screens remained accessible after reimport. No mounted component or D17 owner resource was duplicated.

**Unverified boundaries:** No real D17/MIB-03 owner receipt, no authenticated GM/Character permission, no actual MIB-14 transaction, no World routing or dimensional gate action, no travel time/fuel/stability formulas, no MMHT 3D geometry, no Unity/mobile device/two-device LAN, no MIB-12 repair/crafting or priced credit transaction. The operation receipts are explicitly `D17-local-ship-simulation` and `authoritative:false`.

**OPS5:** VCSR-10 is staged as an additional **draft stacked PR** on VCSR-09 #2034 (preceded by #2031, #2029, #2028, #2026, #2024, #2022, #2021 and #2019). Protected `main` is not updated; governed exact-head checks, precursor publication and canonical selector reconciliation are still required. No other lane selector changed.

**Next owner-directed cycle:** **VCSR-11 — component system runtime**: dependency-aware power/fuel/heat/ammunition/charges, disabled functions, damage and station control **through explicit sourced rules**, not universal inferred formulas.

## Cycle 11 — Component runtime: declared dependencies, owner observations, coarse resources and station plans

**Cumulative offline HTML:** `artifacts/Multiversal_VCSR_Cycle_11.html`. **SHA256** `4d0bde82216e4c5a11d35223abeb4c8398b44ac2e40b3e4383bce91e1dc48623`; **818,493 UTF-8 bytes**, exact Git blob `ef8a4d707ff2bfd3bcd1aba3203075c91b312cd4`. Cycles 01–10 remain embedded and independently usable; schemaVersion11 upgrades Cycle01–10 GM checkpoint imports.

### Source authority

Read source `governance/application-planning/multiversal-engineering-refit-assembly/MERA-10_DEPENDENCY_NETWORK_FAILURE_RUNTIME.md` and `packages/contracts/src/multiversal-engineering-refit-assembly/mera-10-dependency-network-failure-runtime.ts` on Multiversal-app main, plus MERA-07/05 owner diagnostics/maintenance contracts and the MIB-14 configuration engine. MERA-10 prescribes declared dependency edges only; alternate-path protection only when explicit relation AND accepted owner evidence show activation. Hidden nodes/edges are filtered **before** graph lists, counts, diagnostics and export. A resource label does not give hidden circuits, tanks, heat curves, fuel rates or other detailed topology. Unknown/conflict is unresolved, not guessed.

A dedicated **System Runtime** browser workspace provides five expressly *VCSR-11 synthetic demo networks* bound to already-owned physical instances: Coastal Cutter, Rift Skiff, Hollowstep mecha, Utility Rover and GM-private ship. The examples deliberately **do not assert a canonical source anatomy or wiring diagram**. Cutter examples: a source-backed demo main bus and an explicitly independent backup (no active failover by default), an actual pre-owned Sensor Mast that must be installed on its source-authorized mount, a helm station and unrelated cargo access. The sample relationships are `sensor → core`, `helm → core`, and `sensor → backup` as an inactive alternate. They are authored fixture relationships, not universal equipment facts.

- **Network inspector:** visible-only node cards, physical Asset identity and installed status, effect on specifically declared downstream capabilities, explicit inactive/activated backup owner evidence, related owner-state snapshots and a semantic text relation list. Owner-observed available/degraded/failed/unknown/conflict states have distinct meaning; a derived disabled capability does **not** mutate its physical module or repair history. Cycles and missing/secret endpoints reject invalid authoring/checkpoints.
- **Resources:** independent coarse power/fuel/heat/fluid/ammunition/charges/data/control/magical readings. Unknown state contains `null` quantities. A known snapshot demands a current, maximum, unit, owner-result reference and evidence. Example Cutter power is **6/8 fixture-units** with one explicitly *synthetic* `fixture:rule:cutter-scan` cost of 1; no other cost, regenerative rate, timer, inferred ammunition or overheat formula exists. Applying this example cost is a local mock owner result and history event, **not live D17 consumption**.
- **Station requests:** only accepted capability, exact actor/assigned station/permission and owner evidence can produce a typed nonexecuting request. Disabled, unresolved, uninstalled or unauthorized systems fail closed. A station plan never applies attack, travel, sensors, repair, heat, cooldown, fuel or any Action/Effect itself.
- **GM authoring:** source-evidenced additional subsystem and exact dependency/alternate/interface definitions over an existing real target Asset, without creating the component or changing MIB-14 installation. Alternate activation separately requires owner-result evidence. D17-shaped history and mock receipts use stable idempotent operation identity, version guards, replay and full rollback. Copies of the same physical Asset preserve IDs; failed operations mint nothing.
- **Privacy / persistence:** GM-private runtime ship and any hidden network endpoint are filtered before Player lists, edge sets, counts, receipt lists and downloaded handoff. Actual GM checkpoint uses all Cycle01–11 structures. Existing Ship, Mecha, Vehicle, LSS loot/scavenge/salvage screens remain independent and functional.

### Source and validation proof

**Chromium/Playwright full offline file** at 1280×850 and 390×844: 397 inherited Cycle01–10 checks + **58/58 Cycle11 checks = 455/455**. No page JS errors or horizontal overflow. An early 56/58 new suite came from privacy checks toggling an irrelevant JavaScript variable rather than the actual role select; corrected to use the real UI selector, then reran both widths fully green. JS `node --check` passed.

**Manual interactive browser test:** opened Runtime, installed the exact pre-owned physical Cutter Sensor Mast through the previously validated ship installer; recorded main core failed and observed both helm and sensor disabled while unrelated cargo remained available. Confirmed alternate owner result, sensor recovered without magically restoring helm. Restored core with history preserved; applied one source-explicit mock power cost (6/8→5/8), prepared an exact helm-station request with no execution. GM-authored another subsystem and source-evidenced dependency. Player role exposed only four of five runtime profiles and no GM authoring; downloaded Player handoff excluded GM-hidden topology. Downloaded an **actual 206,180-byte schema11 GM checkpoint**: five runtime profiles, seven local receipts, cutter profile v8 and owned sensor still mounted. Imported it into a fresh 390×844 browser, checked the retained node/edge counts, resource 5/8, station request, installed Asset ID and original Ship/Mecha navigability. Zero JS errors/overflow.

**Boundary:** D17/owner state remains canonical, MIB-14 configuration/Asset installation, MERA-10 advisory dependency, MIB-12 repair, Character/A8 station permission and Action/Effect runtime external. No live D17 provider, actual MIB-03 receipt, production auth, Unity/Android/LAN, cross-tester connection, auto resource loop or real combat/engineering effects are claimed. No payments or XP spent.

**OPS5 publication:** VCSR-11 is another **draft stacked PR** on VCSR-10 #2035, following VCSR-09 #2034 → #2031 → #2029 → #2028 → #2026 → #2024 → #2022 → #2021 → #2019. Protected main still selects older on-demand state until prerequisite exact-head publication/reconciliation; other persistent lane selections untouched.

**Next owner-directed cycle:** **VCSR-12 — Repair, refit, upgrade, cannibalization, substitution, reassembly and donor-part intake**, with MIB-12 and LSS-08 authority boundaries, exact source/target IDs, input/output conservation and explicit failures.

## Cycle 12 — Source-exact repair, refit, cannibalization, substitution and reassembly

**Self-contained cumulative offline HTML:** `artifacts/Multiversal_VCSR_Cycle_12.html`, **900,006 UTF-8 bytes**, SHA-256 `fb216f7afb85714e28cf96ed6a96944ab9cda9c403897f718871e506aff1877d`, verified exact Git blob `e183ee46220f87a2e3ddbb9eedbcda3a151751cf`. Includes all working VCSR-01..11 HTML screens and schemaVersion1–11 checkpoint import migration, with the new **Repair / Refit** page and schemaVersion12 portable checkpoint. No other tester is linked or modified.

### Governing sources inspected directly

Multiversal-app main `governance/application-planning/loot-scavenge-salvage/LSS-08_LIVE_REPAIR_REASSEMBLY_INVENTORY.md`, `packages/contracts/src/loot-scavenge-salvage/repair-reassembly-engine.ts`, `lss-08-starter-library.ts`, `governance/application-planning/multiversal-implementation-backbone/MIB-12_LIVE_CRAFTING_ENGINE_INVENTORY.md`, and MERA-07 repair/maintenance source. MIB-12 owns transformation *rules*, MIB-14 owns exact compatibility evidence, D17 owns physical identity/quantity/condition/lineage and **atomic** owner mutation, MIB-03 owns stable operation identity/status-first retry and version binding, APW-03 owns long-running Project time, and MIB-13 owns prices/settlement. The HTML creates **local mock D17 receipts**, not a second authoritative ledger.

The original source-backed LSS-08 **synthetic starter** rows, including exact definition names/versions/conditions/units, are included as immutable demonstration fixtures; they are **not** published game-world item statistics or proof that an actual D17 service was called.

| Exact LSS-08 rule | Physical source / explicit result |
|---|---|
| `lss08-rule:rover-sensor-replacement` | damaged `asset:rover:repair-target` v7 and owned serviceable `asset:sensor-mast:donor` v3, one module; exact accepted MIB-14 rover/sensor evaluation, target serviceable through `mib12:condition-rule:rover-sensor-repaired` |
| `lss08-rule:rover-survey-sensor-substitution` | alternative serviceable survey-sensor donor v4; *both* exact substitution rule and exact donor/target MIB-14 compatibility evidence mandatory |
| `lss08-rule:lantern-brass-cannibalization` | damaged lantern bracket v5; `asset:brass-scrap:lot` v8 with **3 pieces**, consumes exactly **1**, leaves **2** in the same original physical Asset, repairs lantern only under explicit condition rule |
| `lss08-rule:damaged-field-coil-reassembly` | two damaged physical fragments A v2/B v6; exact conditioned-combination rule required, atomic result one `assembly:field-coil-rebuilt` with explicit output quantity/unit/condition and stable new lineage |
| `lss08-rule:field-repair-bench-refurbish` | weathered Field Repair Bench v9 becomes `condition:serviceable`, **not automatically pristine**, preserving prior history |

The LSS-08 `asset:rover:repair-target` has a **typed reference** to VCSR-08's `demo:vehicle:rover-01`, explicitly **not the same physical D17 Asset**. The repair screen does not modify the independent prior vehicle inventory when this source-backed fixture repairs. No already installed parts or source salvage names can be minted from a display label. GM may author **local illustrative** donor references and refit/upgrade rules only with explicit MIB-12-shaped source, condition, quantity/unit and acquisition evidence; generic GM substitution is deliberately blocked until an exact approved MIB-14 donor/target compatibility registration and substitution authority exist. Conditioned reassembly also demands the separate combination reference.

### Active operations and fail-closed behavior

- Rule browser / target & owned-donor selection, exact D17-shaped stable Asset IDs, provenance and per-Asset history.
- Read-only `plan` checks source condition/definition/tag/quantity/unit, explicit condition & compatibility, exact physical selection and per-Asset expected versions. Source rule content is fingerprint-pinned; a same-version rule mutation invalidates the pending plan.
- `reserve` returns **mock owner-provided nonsequential** post-reservation versions; no output or donor consumption yet. Lost reservation response enters uncertainty, requires owner-status query, and cannot immediately commit. Cancel/release uses exact owner-returned versions, preserving donor quantities.
- An accepted `commit` atomically records target condition change, exact donor consumption, preserved remainder, output/lineage and a single D17-shaped mock receipt **only after source-version checks**. Failure and stale or incompatible evidence cause no partial donor consumption. A lost-commit-response is recovered by owner-status query and receipt replay without duplicate output.
- Source-backed starter rules are immutable. Same-idempotency-key different payload rejected; active donor source locks prevent parallel double allocation. Player view is read-only and filtered before sources, plans, receipts, counts and downloaded integration handoff.
- No XP, credits, market values, inferred recipe time, universal repair ladder, magically pristine condition, implicit salvage drop, actual world or Character effect, or live workshop automation.

### Verified local acceptance evidence

Actual complete HTML loaded with Chromium/Playwright `page.set_content` at **1280×850 desktop and 390×844 mobile widths**, zero JS page errors and no horizontal document overflow: **528/528 embedded checks** (prior VCSR01–11 **455/455** plus VCSR12 **73/73**). JavaScript syntax passed Node check. A preliminary new-layer 66/69 failure isolated stale test object references after intentional atomic clone/commit plus one older Cycle11 handoff adapter; fixed and rerun full green. Four additional targeted tests pinned rule fingerprint and blocked unapproved custom substitution and conditioned assembly.

**Manual real-button browser path:** GM planned a Rover sensor repair, lost the reservation reply, queried owner, lost the atomic commit reply, queried and replayed receipt; exact physical donor quantity reached zero and target became serviceable, no duplicate owner event. Ran authored lantern-brass cannibalization (three→**two** original pieces) and damaged-coil reassembly (exact **one** new output). Authored a distinct GM refit rule through its on-screen form. Downloaded a real **225,389-byte GM JSON checkpoint** (`schemaVersion:12`, three committed jobs, six local owner receipts), then opened it in a completely fresh **390px browser**, retaining the same physical IDs, reassembly output, brass quantity two, and authored rule. Downloaded Player JSON handoff, confirmed GM-private donor/rule absent, and reopened **Vehicle, Mecha, Ship and System Runtime** pages from the imported file without errors.

**Authority exclusions:** This is not a live D17 or MIB-03 receipt, actual MIB-12 transformation, authoritative MIB-14 compat query, real inventory/crafting/market settlement, Unity/Android install, LAN proof, or integration of GM, Character, Downtime or MMHT tester. Only locally labeled synthetic fixtures and browser checkpoint save files are changed.

**OPS5 staging:** VCSR-12 is a **new stacked draft PR** based on VCSR-11 #2037 and all preceding VCSR drafts; protected main is not merged and cannot claim a canonical VCSR selector until governed exact-head publication/reconciliation. Other persistent lanes unchanged.

**Next owner-directed cycle:** **VCSR-13 — Storage, cargo handling, workshops, base facilities, crew assignments and hangar service**, with explicit physical owner identities, source-evidenced capacities and permissions, and independent map/scene references only.

## Cycle 13 — D17-linked storage, cargo, facility work orders, workforce and hangar services

**Full cumulative offline artifact:** `artifacts/Multiversal_VCSR_Cycle_13.html`, **992,173 UTF-8 bytes**, SHA-256 `2dd6ce72e64d48fbc7f58a7127cb8714f3e1b042b656dae86a7d818a3d131d1d`, verified exact Git blob `1a29711e53b7db3b81f8ff99542ac008cb91d1eb`. Contains Cycles 01–12 unmodified and new **Storage / Hangar** page, `schemaVersion:13`, backward imports for Cycle01–12. It neither requires a campaign nor links to GM, Character, MMHT, Downtime or Unity applications.

### Exact reviewed governing source basis

Multiversal-app `governance/application-planning/multiversal-implementation-backbone/MIB-14_LIVE_VEHICLE_PLATFORM_BASE_INVENTORY.md`, `packages/contracts/src/vehicle-platform-base/mib-i14-starter-library.ts`, `vehicle-platform-base-engine.ts`, `governance/application-planning/system-maturation-buildout/SMB-05_FULL_BASE_HOUSING.md`, `smb-05-full-base-housing.ts`, `governance/application-planning/multiversal-built-environment-settlement/MBES-08_FACILITY_NETWORKS_AUTOMATION_LOGISTICS.md`, `packages/contracts/src/inventory-equipment/inventory-projection-port.ts`, and MIB-12 crafting-engine inventory.

MIB-14's **source-backed synthetic starter** `base:workshop-outpost-standard` has 20 module/facility slots, 3000 cargo mass, power capacity 40 and no universal habitation size. Illustrative *physical* Outpost instance `fixture:base:haunted-lighthouse-outpost` demonstrates installation of exactly MIB-14-governed **Storage Locker** (facility slot1, storageMassCapacity500), **Repair Workshop** (slot3, powerDraw6, `workstation-capability:repair`, `workstation-capability:upgrade`) and **Foodcraft Station** (slot2, powerDraw3, `workstation-capability:foodcraft`). A base's total cargo allowance is not its storage locker, room volume or housing count. The player's Utility Rover's 500 MIB-14 cargo mass is a total chassis configuration reference, while Cutter's illustrative local compartment has separately authored 120 fixture mass. Unsurveyed annex capacity stays `unknown` and blocks transfers.

**Eight demo logical spaces** begin: workshop locker, repair station, foodcraft station, Cutter cargo, Rover cargo, Cutter tender berth, GM-private engineering store, unsurveyed annex. World/Map Maker IDs are typed `MMHT:` references only—no floor geometry, path, room volume, mine, crop field, or autonomous logistics is created. A cutter tender berth's illustrative capacity **1 craft** is not source-authorized universal hangar capacity.

### Playable local actions and boundaries

- Binds exact existing physical source IDs from prior Cycle08 vehicle parts, Cycle10 ship parts and Cycle12 LSS-08 source Assets (including original 3-piece Lighthouse Brass Scrap lot) into **independent, explicitly local placement projections**. A real source Asset's definition, ownership, quantity, version, attachment and lineage are *not overwritten*. Sources installed on a vehicle/ship or changed by a later owner version cannot be moved as uninstalled stock.
- Mass is source-evidenced when available (MIB-14 Cargo Rack 20, Sensor Mast 15, Auxiliary Power 30). The illustrated 2 mass per Lighthouse scrap piece is explicitly **VCSR-13 GM authored demonstration**, not an assertion from MIB-12 or LSS. Known receiving-space mass and occupancy are calculated from visible physical projections; unknown or over-capacity moves fail closed.
- Exact source owner/Actor/operation control-grant evidence is required independently of GM preview. **Transfer** creates immutable plan → local nonsequential owner-version reservation → atomic local placement update with mock D17 receipt. Ambiguous/lost reserve or commit replies query owner status; replay cannot duplicate component or item. Cancel/release preserves source quantity and physical identity. Real D17 inventory is never mutated.
- **Hangar** binds an already-owned VCSR08 Skiff with an authored one-berth MMHT-like reference, without spawning, boarding, relocating, or destroying a vehicle. Duplicate berth/ownership/version conflicts reject.
- **Workforce** preserves Character qualification and station grants as typed references. The fixture's `actor:ari` assignment does **not** grant actual skill or a new Character asset.
- **Service** requires a source-present MIB-14 workstation capability, explicitly assigned qualified operator, owner grant and *exact* GM-authored or already-registered target-compatible MIB-12-shaped rule. The default Cargo Rack diagnostic work-order is explicitly `fixture:mib12:request:cargo-rack-assessment` with `VCSR-13-LOCAL-NOT-MIB-12` provenance. No arbitrary `mib12:` prefixed text passes as recipe authority, no Rover replacement recipe applies to a Cargo Rack, and the work order remains **request-only** with no donor consumption or repair result.
- GM can author additional evidence-backed storage/room references and bind an *existing* preowned physical component; cannot mint one from a label, change protected MIB-14 fixtures or upgrade a public source using private stock. Role-filtering occurs before space/asset counts, receipt projections, handoff and physical IDs.
- No second live Asset inventory, map geometry, facility graph, production ledger, automatic housing/workshop process, paid provider, price quote, XP purchase, Game Clock, remote server, Unity install or real Windows/Android LAN proof.

### Browser validation and physical-file proof

**Chromium Playwright full offline document** at 1280×850 and 390×844: **606/606 checks**—VCSR01–12 **528/528** inherited, plus **78/78** new. No uncaught JS page errors or horizontal document overflow at either viewport. Node.js `--check` passed.

Manual **actual HTML button interactions**: selected existing Rover Cargo Rack, planned transfer locker→Rover cargo; lost reserve reply→owner query→lost commit reply→owner query confirmed exactly one placement; original Cycle08 Asset `demo:owned:rover-rack` kept its source location/version. Then physically referenced existing `demo:vehicle:skiff-01` into Cutter's single berth; created an explicitly local service request on Cargo Rack under a demo-only assessed work-order; added new GM authored storage space with **90 mass cap**, linked existing `demo:owned:skiff-rack` instead of minting it, and verified older screens. Downloaded real **237,930-byte schema13 GM checkpoint**, containing **9 spaces, 8 physical projections, 3 committed local jobs, 6 mock owner receipts**; imported it in a fresh 390px browser preserving exact identities, storage move, berth, service request and authored stock. Downloaded actual **142,623-character Player JSON**; private GM store, private stock/source/map IDs excluded, prior repair bridge retained. All previous Vehicle, Mecha, Ship, Runtime and Repair navigation remained functional.

**OPS5 governance:** a draft stacked PR based on VCSR-12 #2039, itself stacked behind prior VCSR drafts. Protected `main` remains unchanged; source-branch staged selector advances only VCSR to **VCSR-13** at revision **697**, with other lanes unchanged. Exact-head authority CI, predecessor publication and canonical selector reconciliation remain pending.

**Next owner-directed cycle:** **VCSR-14 — MMHT spatial references for owned ships, vehicles, mecha, bases, workshop floors, cargo routes and placed storage**, preserving geometry ownership and optional map link; future ENV/ICF/farming/mining stay typed external adapters.
