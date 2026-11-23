# DTGW — Downtime Games, Sports & Wagering: standalone HTML playtest program

**Plan ID:** DTGW / Cycle 17–30  
**Version:** 0.1.0 · 2026-11-22  
**Requested by:** Multiversal owner in this conversation  
**Selected session lane:** OPS5 `content-design` (owner-directed on-demand design plus standalone HTML playtest artifacts)  
**Canonical operational selector:** `operations/CURRENT.json` on current `main`  
**Application-implementation authorization:** **none**. Do not start PCV-06, mutate app runtime, or modify GPR/MTLC/PCV implementation branches under this program.  
**Status:** Step 1 locally implemented as standalone Cycle 17; user browser acceptance pending. Subsequent steps proposed, not accepted complete.

## 1. Rebootstrap and source-precedence findings

This plan is deliberately a source-backed, **non-authoritative** OPS5 worklog and dependency record, not a new `CURRENT.json` lane selector. It was formed by reading the current OPS5 bootstrap/contract/CURRENT/LANES and the following original project materials.

| Source | Inspection and current meaning | Consequence for HTML |
|---|---|---|
| `governance/application-planning/product-convergence/PCV_GAMES_WAGERING_INTEGRATION_v1.2.0.md`, ID `PCV-GW-01` | **Owner-approved cross-tranche product requirement**; primary full delivery PCV-06, authoring PCV-07, UI PCV-09, installed proof PCV-10. It explicitly prohibits premature PCV-06 activation, real-world-value wagering and a Black-Vegas-only engine. | One generic games/events/markets model; split Campaign Play vs isolated Free Play; no cash-out, no subscription tokens; standalone HTML drafts only. |
| `Multiversal-app/governance/application-planning/sports-rules-system/SPRT-00_PROGRAM_INDEX_v0.1.0.md`, `SPRT-01_UNIVERSAL_SPORTS_CORE_v0.1.0.md`, `SPRT-I01_LEVEL5A_IMPLEMENTATION_REGISTRY_v0.1.0.json` | **95 indexed Sports profiles at Level 5A** (pre-playtest verified) including ball/team, combat, races, judged, target, mounted/animal and vehicle sports. Human Level-5B playtest remains unverified. Deterministic vectors exist as profile-embedded design evidence, not an installed 95-sport runtime. | Bring exact 95 source IDs/names/families into searchable catalog, then implement family-specific sports exchanges and selected complete quick/detailed matches, never treating one Athletics roll as a full sport. |
| `MRC.PDF` (36 pages) | Setting-native MRC event, racing, sanctions, Steward Corps, Chaos Patrols, sponsorship, integrity and betting context. Examples include Chaos Circuit, Black Run, Species Showdowns, Royal Chase and Gambler's Gauntlet. | MRC optional regulatory/venue layer; game/market remains usable when regulator is off. Source event identity must not mean result authority. |
| `Black Vegas.PDF` (18 pages) | Casino Spires, Demon Coliseum, Gambler's Accord and optional high-stakes gambling/memory/trait stakes. Contains an example 1d100 house roll and setting-specific twists. | Black Vegas is a setting skin/content pack, **not** global game mechanics. Old 1d100 example retained as optional source-specific rule, not a universal odds or payout rule. |
| `Multiversal_Downtime_Playtest_Cycle_16.html` and its GM33 review bridge | Working local downtime clock, GM-reviewed activity lifecycle, scene-free workspace, per-character player history, save migration, review-only GM handoffs. | Reuse scheduling, approval, clocks, interruption, results and local files. Do not duplicate APW/project ledger, campaign GM state, or authority. |
| `Multiversal_Downtime_Playtest_Cycle_14.html` | Animal services, market and competition proposals, including source-eligible rodeo and welfare holds. | Sporting animals remain CCP-governed; no forced training/competition, unsupported physical stats or automatic outcomes. |
| `Multiversal_GM_Playtest_Cycle_33(2).html`, Character Builder v19, MMHT UX-04 | Existing independent GM/Character/Map source and exchange boundaries; presently not a single installed live system. | Optional references only until each receiving tester implements explicit import/acknowledgment. |
| DPL-01 Profession Taxonomy / SPRT-108 Rodeo, CCP-06/07 and existing economy contracts | DPL and CCP delegate creature behavior/welfare to CCP, sports rules to SPRT, economy to MIB-13 and equipment to asset owners. SPRT-108 has safety stoppage and animal authority boundaries. | No duplicated animal-health, paid prize, training, credits, inventory, status, skill XP, race or vehicle result ledgers. |

### Explicit source gaps

- The 12 Earth starter game categories are an **approved minimum pack**, not yet 12 verified playable HTML implementations.
- The ten Multiversal/Black Vegas names are **starter design candidates**; some are *external-event market formats* (e.g., Coliseum Book, Hatch Pools, Title Run), not intrinsic games with their own result engine.
- The 95 Sports profiles have Level 5A design certification, **not** installed complete player-versus-player browser proof or human 5B validation.
- Source PDFs can contain older or venue-specific rules that do not supersede `PCV-GW-01`, owning source domains, or currently approved sports contracts.
- Campaign asset stakes, unusual fictional stakes, real sport outcomes and external-result receipts remain owner-domain integration tasks. No fake wallet is campaign wealth.
- Not all other source documents in archival/recovery bundles have been individually re-audited; source mining will continue where a stage actually needs those rules.

## 2. Boundary and model decisions

**Non-casino-first:** player can start with an ordinary card/dice game, sports match, competition or event from a standalone workspace, optional campaign/scene/map/venue.

**Three separate authoritative concerns:** (1) intrinsic game-specific result; (2) independently owned Sports/Vehicle/Creature/Combat/GM event result; (3) stake/market settlement. Wager layer cannot decide an external event result.

**Two participation contexts:** Free Play has isolated resettable fake balance; Campaign Play may ultimately use fictional credits, assets, favors, memories, contracts or other authored stakes **only after** the owning domain adapter validates reservation, legal use and settlement. No real-world money, purchases, gambling devices, transferable/cashable digital balances, or financial payout.

**Regulators optional:** off / light / custom / full at appropriate campaign/venue/event/market scope. Under `off`, the games and bets remain usable when their own rules/owner evidence permit; MRC-only consequences disappear.

**Source states distinct:** reference-listed / source-designed / runtime-bound / test-playable / human-playtest-validated. Unknown facts stay unknown; no universal probability, house edge or sporting match formula is inferred from a title.

**Downtime role:** author/playtest schedule, preparation, GM approval/visibility and handoffs; does not mint a second authoritative Sports, economy, character, creature, world or asset ledger. Every completed HTML cycle produces a **new standalone HTML file** for owner review and preserves earlier files and save migrations.

## 3. Bounded implementation and review cycles

| Cycle | Scope | Reviewable completion evidence / acceptance |
|---|---|---|
| **DTGW-17 — source inventory, taxonomy and scheduling** | Source-backed searchable index; 95 registered Sports profiles, 12 Earth game classes, 10 Multiversal candidates, 10 market structures and 6 MRC event examples. Standalone request → existing GM-reviewed project → time advance/result → external outcome reference, provisional modes and regulator context. | Valid all 133 unique IDs; source/authority labels; GM-only notes filtered; no stake amount, real-money path, invented win or score; request conflict/staleness proof; real Cycle16 save import. **Implemented locally, browser acceptance pending.** |
| **DTGW-18 — reusable game mechanics foundation** | Game schema, participants, turns/rounds, deck/hand/dice/wheel/board/randomizer primitives, source-profile legality and deterministic result receipts/replay. A fully interactive non-stake example demonstrates the kernel. | Same seed/receipt replay produces same result; illegal action rejected, player/GM hidden-information filtering; no universal casino edge. |
| **DTGW-19 — Earth casino pack A** | Blackjack, roulette, baccarat and craps as complete player/house playtest tables with source/profile and optional betting scaffold (fake-only at first). | Each supports opening, legal actions, resolved round, replay and UI at desktop/phone size. |
| **DTGW-20 — Earth casino pack B** | Poker variants, video poker, slots, keno, sic bo, pai gow, three-card poker and casino-war style games. Multiple poker rulesets distinct from generic category. | All 12 required Earth families have a playable validated representative; hidden hands, paytable version and exact odds evidence where relevant. |
| **DTGW-21 — Multiversal / Black Vegas game pack** | Event Horizon, Seven Reflections, Memory Market, Gravestones, Three Futures, The Last Door. Separate market-concept references for Coliseum Book, Ration Grid, Hatch Pools and Title Run; owner-confirmed rules required where missing. | No invented rules presented as canon; at least one playable original game, source/genre variation, source-specific optional stakes only when owner accepts rules. |
| **DTGW-22 — Sports Core and natural exchange runtime** | Generic Sports Exchange, sport-specific skill/attribute, score, tempo, position, possession, fouls, officials, exertion, legality classes; quick 3–7 segment and detailed view. | At least one sport per high-level family can complete legal match, produce deterministic result and explain it; not one Athletics roll. |
| **DTGW-23 — 95-profile sports coverage** | Bind all 95 registry profiles to verified match templates or explicit missing-step states; representative edge vectors and family-specific screens. | Full 95 source crosswalk and no false Level5B label; coverage and gaps visible; representative complete per-family human playtest queue. |
| **DTGW-24 — races, mounts, vehicles and hazardous competitions** | SPRT-39/74/90/101/106/108/109 with CCP care/welfare, vehicle controls, sport safety, map checkpoints and external GM result authority. | Welfare/safety stoppage and legal equipment gates; mount/vehicle results owned externally; MRC is optional. |
| **DTGW-25 — BettableEvent & WagerMarket declarations** | External event version, entrant/outcome observability, lock/close, no-contest, official result receipt; ten market types, probabilities/odds source, conflicts and event outcome mapping. | Market never decides event outcome; stale result, wager-after-lock, ambiguous market and cancelled event blocked; no staking yet. |
| **DTGW-26 — Free Play fake wallet and fictional-stake adapters** | Isolated resettable fake value first; campaign fictional credits/assets/noncash stakes via owner-domain preview → reserve → settle/revert protocol once valid; no cash-out. | Reset leaves campaign unchanged; duplicate settlement idempotent; insufficient/unknown stake refused; no real-money-value path. Without owner adapter, show review-only. |
| **DTGW-27 — venue, MRC and jurisdiction overlays** | Off/light/custom/full GM-configured modules: sanction, licenses, Steward, integrity, sponsorship, fees/tax, prestige and enforcement. Black Vegas venues + other setting profiles. | Same game/race/market usable with MRC off; independent modules toggle without silently altering odds or canonical world state. |
| **DTGW-28 — NPC, player, authored games and venues** | House/dealer/bookmaker/NPC variants, two-human tables, custom rules/markets, venue reservation/schedules and location optionality. | Authoring validation, UI readability, private information and spectator handling; no new campaign/scenes required. |
| **DTGW-29 — cross-system file roundtrips and continuity** | GM, Character, Map, Sport, Creature, Vehicle and Economy proposal/ack contracts; duplicate/replay/reconnect checkpoint tests and multi-participant coordination. | Exact source IDs and versions; read-only reviews until owner receipt; true failure cases and visibility filters; no fake authorization. |
| **DTGW-30 — whole-program acceptance** | Accessibility, responsive screens, save migration from Cycles07–29, representative casino/original sport/market full rehearsals, failure/replay/security tests, missing-data reports and owner review. | Separate findings for code syntax, browser, `file://` user acceptance, human UX, real two-device/installed acceptance and production gates. No Level5B, PCV-06 or release claim without actual separately authorized proof. |

**Priority:** cycle numbers define the default forward review order; owner can retarget a bounded cycle without granting broad app implementation. A source gap or unmet true owner-domain prerequisite is recorded with evidence, never made up. Other independent testers continue on their own cycles; use copied imports/explicit handoffs, not a shared mutable database.

## 4. Cycle 17 concrete source and implementation record

- Artifact: `Multiversal_Downtime_Playtest_Cycle_17.html` (local standalone artifact; not published as an app release).
- Source catalog: **133 unique references** = 95 Sports Level5A profiles + 12 Earth game starters + 10 Multiversal/Black Vegas candidates + 10 market types + 6 MRC event examples.
- Workflow: game/sports activity request using existing flexible-time GM-review ledger, booking conflict protection, pause/resume already owned by Downtime, one-time post-result GM reference, role-filtered exported review packets, source-staleness checks, default regulator `off`, Free/Campaign declared but **not** funded or settled.
- Explicitly not implemented: executable casino game/odds/house, sport exchange engine, stake escrow, free-wallet balance, cash-out, real owner mutation, production network, cross-system authenticated acceptance.
- Local evidence: Node JS syntax checked for code scripts; Chromium `set_content` exercised indexed catalog, role-filtered exports, book/approve/advance/record/share, missing event ID rejected, stale request rejected and Cycle16 save migration. Direct `file://` navigation blocked by test environment and remains user acceptance pending.

## 5. OPS5 registration boundary

This file is a **planning/standalone-test artifact**, not a request to change the persistent `CURRENT.json` selector. Current PCV-06 delivery authority and the existing GPR/MTLC/AXI/GM/MMHT lanes are unchanged. An OPS5 branch/PR containing this plan is *proposed source registration* until protected-main review and merge. In-session source-derived plan content must not be described as current canon or a completed product tranche simply because a draft PR exists.