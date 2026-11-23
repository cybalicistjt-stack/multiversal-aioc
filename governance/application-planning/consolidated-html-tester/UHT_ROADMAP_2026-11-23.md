# Multiversal consolidated HTML tester: evaluation and improvement plan

Recorded November 23, 2026. Program label: **UHT**, Unified HTML Tester. This is owner-directed standalone tester work under GM-00's on-demand workspace scope, not an installed-app milestone or a new persistent implementation lane.

## Delivered baseline: UHT-01

The single HTML includes the four supplied testers intact, the GM file's complete nested Map Maker, a Player/GM/Tools entry, persistent workspace frames, explicit character handoffs, full private backup/recovery, diagnostics, a complete searchable content library, and an NPC Creator & Library.

NPC creation supports every included creature/NPC profile and all 26 current species. Existing campaign casts and reusable user-created NPCs appear in the same creator. Edits retain NPC identity and increment its revision. Campaign placement makes a distinct actor through the existing GM prep constructor, retains source identity/revision, rejects duplicate placement and leaves existing live actors unchanged when the reusable NPC is edited. Narrative NPCs may retain unresolved mechanics. Numeric placement requires explicit HP, defense and initiative. This is a local prototype; role selection is not authentication.

The originals are compressed inside the HTML and verified against their original SHA-256 hashes. Small adapters add integration at load time. The source files themselves are preserved. The single-file delivery loads tools as needed; it does not yet replace all four domain models with one shared runtime.

## Corpus coverage reconciliation

The GM tester's initial 1,427 records were a subset, not a project-wide census. Reconciliation covers the supplied originals, complete Csv.zip, resolved expanded creature/NPC packs, the Akwi NPC suite, both current canonical weapon CSVs, and the canonical database pinned to AIOC `5715a8f03de237a53264e91b1e43e8612d649c3a`.

| Content | Baseline and additions | What the count means |
| --- | --- | --- |
| Creature/NPC/template profiles | 1,427 original + 3,053 added = **4,480** | Source profiles, not 4,480 independently certified unique entities |
| Added creature profiles | **1,650** | Expanded source records and canonical object records |
| Added NPC profiles | **1,303** | Multigenre, Wardens, Akwi and canonical NPC objects |
| Added templates | **100** | Explicit template references; no automatic eligibility/application |
| Distinct entity names | **3,635** | Same-name profiles can retain different source/version/mechanics |
| Stable-ID source mirrors collapsed | **32** | Older aberration mirrors do not inflate the profile count |
| Current playable species | **26** | Current Core-26 identity list, not the historical 25-profile list |
| Existing equipment and operational assets | **13,325** | Every original catalog ID has an exact source-row match |
| Additional equipment/base/framework references | **943** | 908 facilities/base/material references, 20 mecha frameworks, 13 ship frameworks, 2 vehicle frameworks |
| Additional canonical item/ammunition objects | **44** | Object presence remains distinct from a complete usable stat block |
| Land/sea/air vehicles and components | **1,198** | Includes watercraft previously absent from GM Hangar |
| Mecha and components | **2,097** | Source frameworks counted separately |
| Ships and components | **2,298** | Source frameworks counted separately |
| GM operational-asset catalog | 5,257 → **5,593** | 336 existing Character Builder vehicle records brought into GM Hangar |
| Exact source tables | **100**, from **26** resolved source files | Master, feature, property and provenance CSVs embedded offline |

The equipment source census contains 16,726 source rows because older and newer weapon catalogs and other source views coexist. They are linked to existing catalog IDs where matched, not counted as additional purchases. Feature, property and provenance rows are supporting data, not extra creatures or NPCs. Expanded, inferred and proposed content retain source labels. For example, the Akwi suite identifies pending creator acceptance; inclusion does not promote it to canon. Raw source CSV exports preserve the exact source bytes.

This is a census of the resolved source set, not proof that all possible unindexed or future corpus files have been found. Additions must extend the same source register and coverage checks.

## Evaluation against current planning

| Project requirement / owner | What this baseline can exercise | Remaining gap |
| --- | --- | --- |
| GM-01/02; A3/A4/A5; MTLC | Local campaign, invitation preview, character review, prep and scenes | Shared context, authenticated identity and actual participant continuity |
| GM-03/04; PCV-04; A6/A7 | Local roll proposals, decisions, combat, NPC actions, conditions and logs | One authoritative cross-tool action/effect ledger and real two-human execution |
| GM-05; PCV-05; D24/D25/F009/F016 | Investigation, social prep, clues, relationships, factions and downtime | Same entity references and explicit reviewed handoffs across all tools |
| GM-07/08/09; PCV-06; D17/MIB-14/LSS/OARC | Inventory, crafting, recovery, vehicles, mecha, ships and components | Shared item-instance identity, custody, quantity, resources, time and once-only outcomes |
| GM-10/11; PCV-07; MNCS/MRCS/MAS | Reusable local NPCs, source catalogs, campaign cast and authoring | Source-version reconciliation, NPC progressive detail, comparison and richer runtime handoffs |
| MMHT/VTTG | Native map authoring, calibrated overlay, floors/decks/transitions and GM references | Tested round-trip consumers for shared locations, actors, recovery sites and downtime facilities |
| UI Bible: NPC & Creature Manager; SD-1007 | Search, create, edit, duplicate-by-copy and campaign placement | Compare, structured relationships/equipment, batch workflows and comprehensive source-status filters |
| UI Bible: shared GM behavior; PCV-09 | Global entry/navigation, local backup, diagnostics and per-tool search | One command/search model, consistent undo, accessibility, notifications and responsive polish |
| PCV-10; MTLC-14 | Repeatable synthetic tabletop rehearsal | Installed Windows/Android, real participants, authoritative privacy and recovery proof |

The normal program owners remain intact. MNCS's live backlog is terminal completed history even though its older program prose still says “not started.” Reuse its contracts rather than restarting the program. CURRENT selects PCV-03F and MTLC-14; stale backlog activation wording cannot supersede those selections. The HTML cannot certify completion of those product lanes.

## Ordered improvement steps

UHT-01 is the delivered source-verified baseline. **UHT-02 is the next recommended work package.** The following steps define concrete standalone upgrades. Product integration in UHT-12 retains the product lanes' existing prerequisites and authority.

| Step | Work and result | Acceptance before advancing | Dependencies / existing owner |
| --- | --- | --- | --- |
| **UHT-02 — Browser and recovery qualification** | Exercise the exact final file in desktop Chrome/Edge and an Android browser. Fix actual rendering, startup, focus and file-origin defects. Validate fresh start, switching, reload, backup and restore. | Open every tool and nested map; create/edit/reopen a character and NPC; preserve a map and campaign; download/upload a backup; reject malformed input; prove no lost edits after reload. Record exact browser/file hashes. | UHT-01; current browser executor limitations must be resolved by a capable executor, not hidden by adapter tests. |
| **UHT-03 — Shared context and identity registry** | Introduce explicit current Campaign, Session, Scene, controlled Character, actor and map references across tools. Keep independent use available. | One campaign/actor reference survives all supported tool transitions; a second campaign does not inherit the first campaign's secrets or state. Stale/missing references show a repair path. | A3/A4/A5/PPIA-02/MTLC; no second identity authority. |
| **UHT-04 — NPC and creature authoring depth** | Extend the delivered creator with source-version comparisons, explicit variant/species composition, relationships/factions, equipment references, narrative/full-detail promotion, import/export and draft history. Keep any-creature/any-species coverage. | Humanoid, animal, nonhumanoid, digital/incorporeal, template-dependent and Akwi cases retain identity, source labels and accepted fields. Unresolved mechanics stay unresolved. Public exports omit secrets. Existing cast placements require explicit update review. | MNCS/PPIA-02/MCCS/MIB-09 and current Core-26 authority. |
| **UHT-05 — Character-to-table action loop** | Connect completed player sheets, GM submission/approval, scene entry, action proposals, target selection, rulings and visible results. | One complete character-to-encounter journey with return/resubmit, approval, NPC response, reaction and closeout. Duplicate or stale proposals cannot create duplicate outcomes. | A5/A6/A7; PCV-04 semantics; existing native decisions. |
| **UHT-06 — Assets, economy and operational continuity** | Connect source item IDs to explicit local instances, custody, quantities, component fit, crafting/recovery jobs and vehicle resources. Reuse one reviewed operation per outcome. | Loot → party storage → character → vehicle installation → damage/repair → return; source identity and quantities reconcile after save/reload. Retry/cancel cannot duplicate loot, spend or repair. Exercise land, water, air, mecha and spacecraft. | D17/MIB-14/LSS/MIB-12/OARC; no parallel ledger. |
| **UHT-07 — Map, scene and noncombat round trips** | Bind source-owned map/floor/feature IDs to scenes, NPC placements, clues, recovery sites and downtime facilities. Carry pinned revisions. | Author a multi-floor site; place an NPC and clue; stage recovery/workshop/rest references; edit the map; reject or review stale links; confirm player-safe projections. | MMHT/VTTG/A5/D24/D25/APW. |
| **UHT-08 — Catalog and source-quality completion** | Turn the current audit into maintainable coverage gates: all source IDs accounted for, source/inference/status filters, duplicates/versions linked, compatibility and missing-field warnings. Add any newly discovered corpus sources. | Every primary source row resolves to a catalog profile or an explicit labeled reference. No feature/provenance count inflation. Raw CSV hashes remain reproducible. All 13,325 existing equipment IDs and all 5,593 operational-asset IDs remain reachable. | ARI/entity catalog/MRCS/canonical content registry. |
| **UHT-09 — Consistent interaction and accessibility** | Consolidate navigation, global search/command, inspectors, feedback, validation, undo boundaries and mobile layouts. Reduce repeated role/context controls and dense nested panels. | Core Player and GM journeys work by keyboard; visible focus and meaningful errors; no essential horizontal overflow at 390 px; screen-reader checks on essential forms/tables/maps; consistent back and resume behavior. | UI/Screen Bibles, PCV-09 and current presentation owners. |
| **UHT-10 — Performance and maintainable packaging** | Deduplicate repeated catalogs and derived source views while still producing one offline HTML. Split lazy indexes/details, release inactive renderers when safe and add measured startup/memory checks. | Identical source coverage before/after; measured desktop/phone open/search/switch times and peak memory; no hidden remote dependency; deterministic rebuild from registered inputs. | Current source package; ARI query/pagination and existing packaging boundaries. |
| **UHT-11 — Full-evening standalone playtest** | Execute a reusable GM/player scenario from fresh setup through the next session, then prioritize defects by blocked workflow and recovery cost. | Build/approve a character; create and reuse an NPC; run social/investigation/combat; loot/repair/use a vehicle; downtime; closeout; backup/restore; reopen next session. Test a second campaign and negative visibility/retry cases. Owner review is recorded separately from automated checks. | GM-00 reusable scenario; MTLC lifecycle expectations. |
| **UHT-12 — Product convergence mapping and integration** | Map each accepted tester behavior into the existing app packages and PCV sequence. Reuse proven source contracts; retire duplicate local models only after replacement proof. | Real identity/admission/reconnect/privacy first through PCV-03F, then appropriate PCV-04/05/06/07/08/09 integration, ending with installed PCV-10/MTLC-14 two-human proof. No mock/HTML badge substitutes for an installed boundary. | Existing product lanes; separately selected work. No new release, provider, commerce or spending authority. |

## Validation and limitations

The companion verification receipt records fresh source/adapter checks. They cover byte-preserved originals, exact embedded CSVs, corpus/ID coverage, JavaScript parsing, namespaced save behavior, native character-review functions and NPC identity/revision/placement guards. They do not prove rendered browser behavior, IndexedDB persistence or file-origin reload.

Local Chromium failed to start because the executor denied its process-singleton socket. The connected browser route was unavailable; the alternate browser rejected file URLs. These are executor limitations, not evidence that the HTML passed or failed browser acceptance. No browser restriction was bypassed. UHT-02 explicitly owns the remaining browser proof.

Source corpora containing inferred or proposed content remain references with visible provenance; inclusion is not canon approval. Full backups contain GM-private data. Multiplayer, authenticated access, server-side privacy, cross-device state, installed hosts and public distribution are outside this standalone delivery.

## Sources reviewed

- OPS5 canonical bootstrap, operating contract, CURRENT revision 684 and lane registry on current AIOC main.
- GM-00 work record and GM Build and Playtest Tracker; MMHT program; current PCV, MTLC, MNCS and LSS backlogs.
- Current Core-26 species authority; supplied Character Builder species list has 26 profiles.
- UI Design Bible, NPC & Creature Manager and shared GM behaviors; Screen Design Bible SD-1001–1009 and shared authoring behaviors; relevant Feature Bible domain ownership.
- NCG CPCE installed-client evidence debt, advisory only: research NOT_RUN entries are not treated as field results.
- Exact supplied HTML and resolved corpus hashes in the source/audit manifests. Canonical DB blob: `a440dd88b4715bf20e958d34b79b59ea9e62a747`.

This record adds no operational selector, grants no product-lane authority, changes no unrelated lane and claims no installed-app completion. It is the durable standalone delivery and improvement-plan log requested by the owner.
