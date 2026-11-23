# GM-VTTG — Five-Foot Grid, Square Assignments and VTT Program

**Status:** Owner-directed GM/Map Maker standalone HTML program, Stage VTTG-01 delivered for owner playtest, 2026-11-23  
**Owner:** John Brandon Turner  
**OPS5 lane:** `gm-workspace` / `GM-00` (on-demand source/planning/prototype; `implementation_authority: false`).  
**Baseline:** `Multiversal_GM_Integrated_Map_Maker_v1.html` (GM IS-16/Cycle43 and MMHT UX-04). The attached owner Map Maker has 22 map types and 66 curated examples. Product implementation remains with separately selected PCV/MTLC and owning domains; MMHT source map-authoring lane stays unchanged.

## Owner direction

Create a working 5-ft square grid on the Map Maker canvas, each square with a unique persistent ID across map/level/grid/row/column. In both GM Scene Builder and Map Maker, a GM may select individual or multiple squares to place creatures, NPCs, loot, items, traps, hazards, encounters, events, triggers and interaction references. Build full virtual-tabletop operation in governed stages. Do not lose existing GM or Map Maker features or duplicate overlapping authoring/ledger functions.

The owner request revises the *planned product scope* to include a VTT, but this GM-00 work does **not** grant installed-product implementation authority or waive existing PCV/MTLC source, D05 permission or domain Event gates.

## Stable spatial contract

A square ID is `sq5:v1:{encoded-mapId}:{encoded-levelId}:{encoded-gridId}:r{zero-based-row}:c{zero-based-column}`. Example map `mapdoc:tester:atlas-keep` tactical grid `grid:square`, level `level:0`, row 2/column 3 represents display label D3. A1 on another floor or map is distinct. Each square is five feet per side on calibrated native square grids. IDs do not contain map revision, but placements carry source map revision for drift and migration validation; map scale/origin/rotation or topology change must not silently remap a placement.

The grid is **sparse**: only references actually selected/placed are stored as GM Scene anchors. Map Maker is the sole geometry owner. The A5 Scene/Session system owns placements; actor/Combat/Condition/Inventory/Investigation/Social/Downtime source owners own gameplay effects. A reference does not grant Player access, reveal a hazard or trigger anything.

**Stage 01 calibrated modes:** native interior `interiorFeetPerUnit`, tactical `grid:square` with exact feet/5 units per cell/zero origin/unrotated native projection, and urban map source `50 ft per map unit`. Regional maps without a local battle-area scale, hex/gridless/rotated tactical grids and unsupported calibration are explicitly refused; do not invent physical units. Squares drawn over cave or non-Euclidean floorplans are spatial anchors, **not** promises of lawful movement/path/visibility.

## Twelve bounded phases and acceptance

| Phase | Core delivery | Acceptance evidence |
| --- | --- | --- |
| **VTTG-01** | 5-ft canvas overlay, unique floor/map/grid square IDs, mouse/keyboard/coordinate multi-selection, native zoom/pan alignment, GM Scene anchor pin and private JSON backup | Working Ruined Keep source example; no duplicate map/Scene; unsupported grid fails closed; original GM regression and Map Maker preserved. **Delivered for owner playtest.** |
| **VTTG-02** | Typed square content: items, loot/containers, creatures/NPCs, encounters, hazards/traps, interactables, events and triggers, with source definitions and versions | Multiple placements per square, multi-square footprints, hidden vs safe fields, typed owner records, no applied gameplay Event |
| **VTTG-03** | Scene Builder placement editors, source search, drag/resize, layers, bulk operations, templates, versioned Scene snapshots and import/export | One Scene placement owner, editable/archivable/restorable, source drift warnings, no geometry duplication |
| **VTTG-04** | Characters/NPCs/creatures and vehicle/mecha tokens; controlled actor binding, multi-cell sizes, facing/elevation and ownership | No token-to-actor duplication or Player-control escalation |
| **VTTG-05** | Distance rulers, diagonals, terrain/elevation, collision, move paths and GM-approved A6 movement | No universal movement assumptions; source walls and elevation honored; approved Event vs preview distinct |
| **VTTG-06** | Per-Player fog, vision, wall/door occlusion, lighting, explored history, hidden entries and reveal controls | Authoritative field-safe Player projection including counts/coordinates/exports; revocation checks |
| **VTTG-07** | A7 live encounter and Combat/initiative, A6 attacks/saves/conditions/reactions, templates and ranges | F012 prepared encounter separate from A7 running state, Event receipts own changes |
| **VTTG-08** | Source-owned trigger/interactive event contracts; enter/exit, turn, discovery, disarm, reinforcements | Deterministic declarative actions, order/idempotency, explicit GM approval, no untrusted code execution |
| **VTTG-09** | Loot, containers, pickups, items/equipment, credits, objects and transfer operations | A8 custody/inventory and economy validate, no client-created ownership or duplicate resources |
| **VTTG-10** | Floors, stairs, ship/mecha/vehicle decks, gates/portals, mobile bases, non-Euclidean transitions | Per-floor square identity and source-approved map-to-map transitions; physical/dimensional rules owner-specific |
| **VTTG-11** | Multiplayer VTT with GM/Player/observer, controlled tokens, chat/pings/handouts/dice and realtime reconnect | D05 server rights enforced before every read/coordinate/submit; A5/A6 owner receipt; physical two-device |
| **VTTG-12** | Full QA, saved migrations, device/mobile and accessibility, high-square-count performance, offline/reconnect, integration and rollout | Installed app/source owner/Map Maker/Downtime import verified with physical Windows/Android LAN, security, screen readers and owner acceptance |

## Stage acceptance that applies throughout

- Every new bounded standalone increment delivers one reviewable HTML, checksums, tested regressions and clear limitations.
- Preserve the original GM and MMHT toolchains, map library, floor/geometry identity and 66 editable examples. Reuse existing Scene & Handoff Desk rather than adding another Scene/map library.
- Each placement carries Campaign, Scene, map ID/revision, grid ID/origin, level, row/col, source owner ID/revision, role visibility and lifecycle. Calibrate physical scale or reject unsupported maps.
- Distinguish local draft, reviewed placement, GM-approved action and canonical owner-committed Event. D05 player disclosure must be filtered before counts/search/exports, not hidden only with client CSS.
- Use no automatic NPC/faction/status/inventory/trap effects until the correct domain owner accepts an Event.
- No production deployment, installed Unity/client implementation or automatic Stage-02 execution follows from this planning record. Product priority/authorization must be separately selected in OPS5.

## Delivered Stage VTTG-01 verification record

**HTML:** `Multiversal_GM_Map_Maker_VTT_Grid_Step01.html` · 23,682,643 bytes · SHA-256 `4cfbe30082e85b6a9583ac7589d2bd2f00917c29a2e62bd3dcaf7f1ca9271a5d`.

- New focused Chromium **26/26 PASS**; inherited integrated GM+MMHT **37/37 PASS** including original GM27 Regression Lab **27/27** nested; static/source/syntax **33/33 PASS**. Playable Ruined Keep sample has independently selected cells and a screenshot with D3 highlighted.
- All prior 23 GM Cycle43 script blocks and the original integrated GM↔Map Maker bridge remain byte-identical. Map Maker keeps all prior source scripts but its native editor block receives a **minimal read-only viewport hook**; one new canvas overlay script is added. Do not claim the Map Maker executable source is byte-identical.
- Current Scene reference records are updated idempotently, and selecting squares creates a separate **GM-private local anchor record only**, not an item/NPC/encounter, gameplay object, event, token or line-of-sight state. JSON backup contains all authority flags false.
- Browser checks use Playwright `set_content` and controlled localStorage; native `file://` reload, Android `content://`, actual D05 security, source owner imports and installed Windows+Android multiplayer remain **unverified**.
- Owner-review artifacts: `Multiversal_GM_VTT_5ft_Grid_12_Stage_Program.md`, `Multiversal_GM_VTT_Grid_Step01_Verification_Notes.md`, `Multiversal_GM_VTT_Grid_Step01_Automated_Report.json`, `Multiversal_5ft_Grid_Ruined_Keep_Preview.png`.

**Next owner-directed VTTG-02:** typed square placement authoring, source identity and visibility, multi-square footprints, initial GM inspector. No automatic source Event or full VTT runtime.
