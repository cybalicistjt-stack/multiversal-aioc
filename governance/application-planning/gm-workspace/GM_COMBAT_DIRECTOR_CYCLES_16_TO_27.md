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

## Authority

Selected lane `gm-workspace`, work `GM-00`, is read-only product baseline and **standalone HTML planning/playtest** under current OPS5. Do not start PCV-04 implementation, change CURRENT/lane selection, certify real-device transport, or mutate the other independent testers based on this approval.
