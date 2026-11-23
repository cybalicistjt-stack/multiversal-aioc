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
