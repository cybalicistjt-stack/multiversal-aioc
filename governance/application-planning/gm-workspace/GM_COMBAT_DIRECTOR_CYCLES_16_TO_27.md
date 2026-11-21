# GM Combat Director — owner-approved standalone playtest plan

**Program:** GM-00 standalone playtest continuation  
**Approval:** Owner approved 2026-11-21, directed "record this in ops5 and start 16"  
**Plan ID:** GM-COMBAT-16-27  
**Source audit:** `Multiversal_GM_Combat_Tracker_Audit_and_Cycle_Plan_v1.0.md` (SHA-256 `a345c451a42d798bec31156a386efd9b6a7d48d1383348f8c7be46108ad05ae5`)  
**Status:** Approved for the standalone HTML playtest, **not** approval to implement PCV-04 or mutate the installed product.

## Approved direction

Continue **one self-contained downloadable GM HTML tester after each cycle**. Retain all Cycles 01–15 functionality. The Combat Director is a runtime workspace within the GM tester, not a separate product or a duplicate action/rules engine. Use the project's actual creatures, character statistics and rules, F006/F007/F012/F013 contracts, GM/runtime design bible, map references and governed provenance. Preserve original roll, GM ruling, costs, effects, permissions and history. Missing/inferred game data stays labeled and does not become canon.

Attached cross-testers remain independent. Their contribution is versioned data/receipt compatibility, not shared in-browser authority: Character Builder (17) owns exported character definitions/equipment/abilities; MMHT-66 owns revisioned maps/floors/features; Downtime Cycle 07 owns its clock, activities and recovery; GM Cycle 15 owns campaign/session/encounter operation. Future convergence is a separate authority boundary. Map visualization never silently substitutes pixel geometry for semantic rules; no full VTT is a prerequisite.

## Approved ordered cycles

| Cycle | Goal | Demonstration / acceptance |
| --- | --- | --- |
| 16 | Combat Cockpit and source alignment | Run a Cycle 15 encounter in a dedicated GM view with always-visible round/turn/pending, searchable/filtered initiative, selected combatant source dossier, zone board, quick rulings and history. A pending action cannot be silently stranded by Next turn. |
| 17 | Participant lifecycle and resources | Distinct independently mutable character/creature instances with sourced HP/Defense/resources/notes; distinguish incapacitation, death/dying, fleeing, surrender, removal. |
| 18 | Initiative, timing, turn economy | Initiative by rules profile, tie/hold/delay/phase support, movement/action/reaction budgets, waves and replay-safe turn hooks. |
| 19 | Character-sheet action bridge | Import versioned character snapshots, browse real equipment/abilities/spells, submit actions and costs with GM approve/modify/deny/return, NPC parity. |
| 20 | Rule-aware resolution | Ordered attack/save checks, criticals where governed, mitigation/resistance, typed effects, compensation and original-result provenance. |
| 21 | Conditions, reactions, interrupts | Quick selectable sourced conditions, stack/duration/lifecycle, bounded reaction windows and no duplicate resolutions. |
| 22 | Semantic movement and MMHT adapter | Optional map/floor/revision import, zones/adjacency/range/cover/elevation, accessible text alternatives and role-safe target previews. |
| 23 | Environment, hazards, waves, objectives | Link authored environment/trap assets, hazard pulse and timed waves; objective-based conclusions beyond defeating every enemy. |
| 24 | Vehicle/mecha/ship combat | Reuse hangar/crew controls, ship/mecha/land stations, hull/power/shields/component damage and authority handoff. |
| 25 | Inventory and aftermath | One-time ammo/consumable costs, death/recovery under governing rules, structured closeout and Downtime interruption/outcome receipts. |
| 26 | Accessibility and role-safe UX | Responsive compact/touch controls, keyboard and screen-reader parity, clear errors, non-color indicators, GM/player/observer leakage audit. |
| 27 | Full local regression and compatibility | Character + map + downtime imports and one end-to-end combat, stale/duplicate/restore tests, role-safe export and provenance review. |

## Cross-cycle invariants and boundaries

1. `EncounterDefinition`, `EncounterPlacement`, `CombatantInstance`, `ActionProposal`, `ResolutionReceipt`, and `MapReference` are distinct; never overwrite source definitions when a participant takes damage.
2. Declare → validate → resolve → GM review/decision → apply once; denied or stale submissions cannot spend costs. All accepted changes retain sources, versions and an attributable correction path.
3. Render GM-only content only into a GM projection. Hidden entities cannot leak via counts, filters, map, target lists, player history, exports or diagnostics.
4. Combat/Free-Downtime/Vehicle use a shared conceptual session. Each independent tester remains executable with no backend and must state where real-device/reconnect or server authority is unverified.
5. Use the project's Rainbow in the Dark visual system, readable grouping, actor/source inspectors, keyboard/touch alternatives and low-interruption active-play controls.
6. Each cycle concludes with a downloadable complete tester, explicit owner playtest route, focused behavioral checks, regression notes and honest rendered/installed proof boundary.

## Cycle 16 delivery evidence (2026-11-21)

- File: `Multiversal_GM_Playtest_Cycle_16.html`; full standalone artifact supplied as a downloadable ChatGPT conversation attachment; 15,042,107 bytes; SHA-256 `680f426cb9a7293cbd1d6eea59939b7c1131ed88463e2e03d7524764e07f4bbd`.
- New GM-only Combat Director navigation, independent from the Live GM scene shell; focused encounter summary, selected combatant inspector, source/approved-character details, initiative filtering, zone board, action queue, history and quick controls.
- The original encounter runtime and 01–15 preparation/continuity/economy/hangar/creator functions remain in the same HTML. Added source snapshot trace on encounter launch. Added pending-action guard on turn advance; action approval stays in the cockpit. Source-backed combat effects are **not** falsely claimed complete in Cycle 16.
- Chromium rendered through `page.set_content` because file and localhost navigation were blocked by the runner. Desktop flow and 390px mobile layout (no horizontal overflow) passed. In-browser player attack → pending GM decision → blocked next turn → approval → successful advance, plus status edit and return to GM routes passed. Node syntax check passed. Persistent origin storage, independent-account sharing, two-device play and installed application remain unverified.
- **Next:** owner evaluates Cycle 16. Advance to Cycle 17 resources/participant lifecycle through another standalone HTML cycle, preserving all previous workflows. Installed GM-13 remains blocked by predecessor evidence.

## Cycle 17 delivery evidence (2026-11-21)

- Full standalone file: `Multiversal_GM_Playtest_Cycle_17.html`, 15,063,769 bytes, SHA-256 `aa6f8098c73745bc7cbf74205e2610807e153ff43577f6a4abc90a812d547957`; downloadable from the owner conversation, not an installed product package.
- Reuses the complete Cycle 16 GM tester and all prior modules; preserves unchanged embedded Character, Transport and GM project catalog JSON checksums.
- Adds live-instance HP/maximum HP and Defense edits, distinguishable encounter-only lifecycle states, custom GM-entered resource pools, per-combatant private notes and a bounded audit trail. Source HP/Defense and origins remain separate from live instance values. Unlisted mana/stamina are not invented.
- Adds textual status facets and explicit labeled rainbow-accented vitals and resource cards (ruby HP, cyan Defense, gold initiative, magenta lifecycle and conditions, violet mana, emerald stamina) following Rainbow in the Dark; color is supplementary to labels, borders and position.
- Chromium desktop and 390px phone views rendered with no page exceptions or horizontal overflow. Positive interaction tests covered pool add/edit, HP 0 then explicit Dying status, private note role filtering, isolation from a second combatant, lifecycle filtering. Negative checks covered over-max resource rejection, reason-required Defense overrides and lifecycle decision confirmation. Two cloned `roster-67` creatures retained independent HP/lifecycle and survived JSON serialization/parse. Node syntax check passed. Catalog embedded JSON remained byte-identical to Cycle 16.
- Browser `file://` navigation was blocked by the executor; Chromium `set_content` could not verify same-origin localStorage reload. The HTML is browser-openable, but this evidence establishes only in-memory test and JSON serialization, **not actual browser reload persistence, installed two-device or server-authoritative play**.
- Next approved GM HTML phase: **Cycle 18**, order/turn economy, rule profile timing, hold/delay and action windows. Keep independent Character, MMHT and Downtime testers intact.

## Cycle 18 delivery evidence (2026-11-21)

- Full self-contained HTML: `Multiversal_GM_Playtest_Cycle_18.html`, 15,086,621 bytes, SHA-256 `f47db48d223f93caf205f695003afac8d0b13ee0ea8b73d13c58dfd97825bad8`; supplied as a downloadable file in the owner conversation. Full earlier GM cycles and the three embedded source catalogs remain present; `sample-character`, `transport-catalog` and `gm-project-assets` JSON payloads were byte-identical to Cycle 17.
- Initiative/turn ledger is a live Encounter-local `turn18` aggregate with a round, ordered queue, acted, delayed and held groups; separate one-round per-actor manual primary/movement/reaction usage; timing-window state; attributable change history; and JSON serialization. Existing encounter action proposals and GM approval continue through the original runtime rather than another combat engine.
- Hold leaves a visible unresolved turn, Release restores it ahead of the current queue, Delay moves a turn behind other remaining turns, unresolvable holds block round rollover until an explicit GM-forfeit decision. Next turn remains blocked by pending GM rulings or an open reaction, interrupt, free-action, simultaneous-group, or environmental timing window. The GM can set initiative for *next-round* ordering and set local action-counting allowances with reason; duplicate use and invalid allowances are rejected.
- **No implicit canon:** Turn usage is GM-entered provisional tracking, not a mechanically enforced or source-backed action cost; opening a timing window does not itself apply damage, consume resources or resolve a reaction. Player actions continue to use existing explicit GM review. Full rule-profile formulas, granular phase/simultaneous resolution and action-cost automation stay in later cycles.
- Applied owner-requested **sidebar differentiation**: uppercase gold/amber section headings, distinct light-blue navigation links, violet/magenta selected-link accent, clear dividers, focus indicators, and the formerly orphaned Session Tools link moved under Prepare. Preserved dark Rainbow in the Dark HP/Defense/initiative/lifecycle/resource tones from Cycle 17. Desktop/390px layouts preserve horizontal bounds.
- Test evidence: Node `--check` succeeded. Chromium rendered both 1440px desktop and 390px phone with no page exceptions, no horizontal overflow and visually differentiated heading/link computed colors. UI tests exercised sample launch, Delay, Hold, Resume, manual action/movement limit rejection, reaction window block/close, initiative edit dialog and source display. A second Chromium test exercised an environmental timing-window dialog, blocked turn advancement, release of a held actor, player-projection secrecy and GM-only turn-completion logging for a hidden actor. Full tester `data` round-tripped through JSON serialization with the encounter and timing receipts intact. Three existing embedded JSON source libraries were verified byte-for-byte unchanged.
- Browser origin navigation was blocked by executor policy (`ERR_BLOCKED_BY_ADMINISTRATOR`); Chromium `set_content` cannot prove localStorage reload across a real origin. Installed Windows/Android, server authority and shared two-device play remain unverified.
- **Next:** Owner reviews Cycle 18 timing and sidebar hierarchy. The next approved standalone GM cycle is **Cycle 19**: approved Character-sheet action bridge, source-linked weapons/abilities/spells and cost/target preview. Product implementation authority and PCV predecessor sequencing remain unchanged.

## Authority

Selected lane `gm-workspace`, work `GM-00`, is read-only product baseline and **standalone HTML planning/playtest** under current OPS5. Do not start PCV-04 implementation, change CURRENT/lane selection, certify real-device transport, or mutate the other independent testers based on this approval.
