# GM-IS — Investigation & Social GM HTML Integration Plan

**Authority:** OPS5 `gm-workspace`, currently selected `GM-00` (on-demand standalone HTML/playtest and audit only).
**Selected by owner:** 2026-11-22: review investigation and social development, register the steps, and begin Step 1.
**Product implementation authorization:** NONE under GM-IS; application integration stays in separately selected PCV/domain lanes.
**Deliverable rhythm:** one complete standalone GM tester HTML per numbered cycle with source provenance, safe views, focused tests, verification limits and owner review.

## Existing source and implementation basis

- **D24 Investigation** is the source of truth for Investigation, Clue Definition, Campaign Clue, Observation, Claim, Evidence Item, Hypothesis, Connection, Question and Conclusion. F011 contains 15 semantic predicates; PPIA-09 adds source-grounded mystery preparation, layered information, witness/forensics, redundancy and diagnostics. MIB-10 demonstrates authorization-before-topology and graph/nonvisual equivalence. A clue is not automatically true; a hypothesis never silently becomes a conclusion.
- **D25 Social Relations** is separate from Investigation. F009 describes directional relationships with fourteen dimensions and typed Bonds/leverage/favors/promises/debts/oaths/obligations; F010 specifies freeform/assisted/structured-challenge Social Mode and seven alpha Actions; F016 separates factions, organizations, membership, office, rank, standing, influence and reputation. PPIA-10 documents source-derived social skills and what remains design-derived, including absence of a universal social DC/standing scale.
- **Shared owners:** D05 handles visibility projections, A6 owns Actions, rolls, proposals and GM decisions, A7 owns combat, A8 owns assets/currency, and A5 owns campaign/scene/session. Reuse existing owners instead of storing parallel 'truth' in the HTML.
- **Adventure Studio MAS-06/07** authors prepared clue/revelation/mystery and NPC agenda/relationship/callback references. Prepared is not discovered, revealed, executed or authoritative live state.
- **Live application A9 sample** supplies separate local Investigation, Social, Faction, Relationship and semantic graph workspaces with a limited NoncombatRuntime presentation; it is not installed two-device certification.
- **Standalone GM tester through Cycle 27** has functioning campaign/session/GM ruling entry, simple Noncombat clue card sharing, objectives/clocks, flat 'relationship' and 'faction' outcome notes, MMHT, encounters/assets/fleet and local regression checks. It does **not** yet expose the full D24/D25 records as an integrated GM workbench.

## Approved ordered steps

| Step | HTML Cycle | Scope and deliverable | Required proof |
| --- | --- | --- | --- |
| IS-01 | 28 | Director route, source/authority census, integrated launcher, exportable coverage register | Synthetic GM/Player role-safe use; source / version / authority boundary, current state and regression retained |
| IS-02 | 29 | Campaign-independent Investigation case library and campaign placements, lifecycle, draft recovery | Synthetic GM/Player role-safe use; source / version / authority boundary, current state and regression retained |
| IS-03 | 30 | GM mystery dossier, core question, layered truth and source-grounded leads | Synthetic GM/Player role-safe use; source / version / authority boundary, current state and regression retained |
| IS-04 | 31 | Reusable Clue Definitions, Campaign Clues, evidence reference and discovery/reveal state | Synthetic GM/Player role-safe use; source / version / authority boundary, current state and regression retained |
| IS-05 | 32 | Observation, Claim, witness belief, reliability, authenticity and recorded testimony | Synthetic GM/Player role-safe use; source / version / authority boundary, current state and regression retained |
| IS-06 | 33 | Semantic clue graph, 15 typed edges, player Hypotheses/Questions, graph-list parity | Synthetic GM/Player role-safe use; source / version / authority boundary, current state and regression retained |
| IS-07 | 34 | Timeline/alibi and temporal windows, contradiction review, red herrings, provenance | Synthetic GM/Player role-safe use; source / version / authority boundary, current state and regression retained |
| IS-08 | 35 | Revelation routes, redundancy/stall warnings, optional clues, authored solvability diagnostics | Synthetic GM/Player role-safe use; source / version / authority boundary, current state and regression retained |
| IS-09 | 36 | GM case conclusion, safe player dossiers, history, continuity and recovery | Synthetic GM/Player role-safe use; source / version / authority boundary, current state and regression retained |
| IS-10 | 37 | Social Director, freeform/assisted/structured challenges, NPC context and participants | Synthetic GM/Player role-safe use; source / version / authority boundary, current state and regression retained |
| IS-11 | 38 | Seven social Actions via A6 proposal/roll/GM approval, conditions and negotiation | Synthetic GM/Player role-safe use; source / version / authority boundary, current state and regression retained |
| IS-12 | 39 | Directional relationship graph, 14 dimensions, scale profiles, Bonds and obligations | Synthetic GM/Player role-safe use; source / version / authority boundary, current state and regression retained |
| IS-13 | 40 | Faction/organization/reputation, membership, rank, office, standing, influence and services | Synthetic GM/Player role-safe use; source / version / authority boundary, current state and regression retained |
| IS-14 | 41 | Interpersonal/community social status, negotiation consequences, rumors, cross-domain events | Synthetic GM/Player role-safe use; source / version / authority boundary, current state and regression retained |
| IS-15 | 42 | Integrated live social/investigation GM workspace, scenes, player, combat, maps and downtime | Synthetic GM/Player role-safe use; source / version / authority boundary, current state and regression retained |
| IS-16 | 43 | Content source lookup, import/export, accessible/role-safe projection, comprehensive regression | Synthetic GM/Player role-safe use; source / version / authority boundary, current state and regression retained |

### IS-01 / Cycle 28 implementation

- Permanent GM **Investigation & Social** navigation and global launch shortcut.
- GM Director opens even when no active campaign or session exists. Campaign-specific sample and linked live routes remain optional.
- Searchable/paged source-to-screen register with all 16 steps, existing standalone functions, remaining gaps and domain owners. Direct reference links and explicit statuses.
- Coverage-only JSON export: does not serialize campaign state, hidden clues or Player-private knowledge.
- Preserve original Cycle 27 source scripts and five embedded JSON datasets exactly; local UI wiring only.
- Completed focused evidence: Node syntax checks; Chromium desktop 1440, tablet 768 and mobile 390 with zero JS exceptions and no document overflow; sample investigation 2 clues/2 tracks, player-mode isolation, filter/paging and export JSON tested.
- File SHA-256: `b524d1c1a6cc0fb08da95b1eaedda70d087ab1e3d37a7cc9ccd86718ceee71c2`.
- Full Cycle 27 regression rerun **not verified for this change**; earlier source unchanged, but a heavyweight test attempt timed out.
- Status: **delivered_for_owner_playtest**, **not installed-product certified**.

## Cross-step invariants

1. Reusable case, social, template and reference workspaces remain available outside a particular scene/campaign when appropriate. Explicit placement, not implicit scene ownership.
2. Distinguish prepared content, authored canon, revealed clue, observation, witness belief, Player hypothesis, GM conclusion and applied effect. Do not promote by proximity in UI.
3. Filter authorization before graph/node/edge/cardinality, search, history, notifications, export, AI or diagnostics. Preserve separate GM, Player, Observer and revoked-audience behavior.
4. Domain mutations require existing owner authority, `expected_version` and stable operation IDs; duplicate deliveries converge or fail safely. No new private action/relationship/investigation engine.
5. Do not infer a universal social DC, universal relationship/standing scale, automatic reciprocal relationship, forced NPC compliance, universal solvability algorithm or missing canon.
6. Source-backed facts, governed design, synthetic fixture and unresolved gap must remain labeled. Player-facing absence of a clue is not proof the clue exists.
7. Preserve prior GM playtest routes (including Combat, Vehicle, MMHT, Assets, Continuity and Cycle 27 Regression Lab) through each standalone HTML increment.
8. Installed Windows/Android, real two-device authorization, native file-origin persistence, external Map Maker/Downtime imports and screen-reader certification need independent evidence.

## Source pointers

- AIOC: `governance/application-planning/internal-alpha/feature-packets/MV-IA-F009_RELATIONSHIP_TRACKER.md`
- AIOC: `governance/application-planning/internal-alpha/feature-packets/MV-IA-F010_SOCIAL_INTERACTION_MODE.md`
- AIOC: `governance/application-planning/internal-alpha/feature-packets/MV-IA-F011_INVESTIGATION_AND_CLUE_BOARD.md`
- AIOC: `governance/application-planning/internal-alpha/feature-packets/MV-IA-F016_FACTIONS_REPUTATION_AND_ORGANIZATIONS.md`
- AIOC: `governance/application-planning/parallel-preimplementation/PPIA-09_INVESTIGATION_MYSTERY_AUTHORING_EXPERIENCE_SPEC_v1.0.0.md` and `PPIA-10_SOURCE_AND_DESIGN_INVENTORY.md`
- App: `contracts/a9-domain-authority-map.json`; `apps/client-ui/src/a9/shared/A9Workspace.tsx`; `apps/client-ui/src/a9/runtime/NoncombatRuntime.tsx`
- App: `governance/application-planning/multiversal-implementation-backbone/MIB-10_LIVE_INVESTIGATION_CLUE_GRAPH_INVENTORY.md`
- App: `governance/application-planning/multiversal-adventure-studio/MAS-06_CLUE_REVELATION_MYSTERY_INVESTIGATION_DESIGN.md`, `MAS-07_CAST_NPC_AGENDA_RELATIONSHIP_CALLBACK_PLANNING.md`
- ChatGPT Project: UI Design Bible and Screen Design Bible V05 (Investigation), V06 (Social), V11 (Authoring).

**Current selected on-demand work remains `GM-00`. This plan does not change `operations/CURRENT.json`, select product implementation or override persistent lanes.**

## IS-02 / Cycle 29 status — 2026-11-22

**Delivered for owner playtest**, not installed-app or canonical D24 implementation.

- Standalone artifact: `Multiversal_GM_Playtest_Cycle_29.html`, SHA-256 `70b94dc386b3f4531415804bb918c8afde33a816071c8c882135c4404dbfe32a`; 15,398,348 bytes.
- Adds a campaign-independent GM Case Library under Prepare, search/sort/status filters, local authored definitions with stable IDs, revisions and draft/ready/archive state. Campaign placements link by definition ID and pin a source revision, optionally reference real local world/scene records and manual unverified NPC IDs, and have separate draft/active/paused/resolved/archive local states.
- Expected-version checks, stable operation ID idempotency, duplicate-placement prevention, explicit revision refresh, local audit receipts, optional synthetic fixture and GM-only private JSON backup. No clue discovery, evidence source ownership transfer, reveal, GM conclusion or canonical action is created.
- Verification: new focused Chromium checks 31/31 PASS (1440/768/390), inherited Cycle 27 regression lab 27/27 PASS, source script/JSON byte preservation and Node syntax PASS. Original Harrowfen case and IS-02 library unchanged during retained suite.
- Browser policy blocks navigation to localhost; controlled storage shim used, so genuine file-origin/localStorage reload remains **not verified**. Installed Windows/Android, independent D24/A6 server operations and external map/downtime interfaces also not verified.
- **Next planned IS-03 / Cycle 30:** GM mystery dossier, source-grounded core question/event, surface/hidden/revealed layers and role-safe differentiated handout. Unknown canon stays unknown.

## IS-03 / Cycle 30 status — 2026-11-22

**Delivered for owner playtest**, not installed-app or canonical D24 implementation.

- Standalone artifact: `Multiversal_GM_Playtest_Cycle_30.html`, SHA-256 `94ed24ad925b8c961b783368252a31e7a0e1f7395d269e562cf6b4521a76ae97`; 15,436,616 bytes.
- Adds GM-only mystery dossier with empty/unestablished facts (core event, responsible party, motive, twist, solution, setting, provenance) and explicit pinned case-definition version. Prepared lead cards have Surface / Hidden / Reveal candidate layers, separate private and public descriptions, manual source references, revisions and retirement history.
- Dedicated public copy and opted-in Surface leads can be snapshotted for a selected active campaign placement and party or specific active Player. GM-only/private and reveal-candidate details never enter the projected handout; publication does not record a canonical discovery, clue sharing, outcome or conclusion. Local Player preview is only a demonstration, not a server-side permission barrier.
- Guards cover stale edits, idempotent operation receipts, source revision drift, placement state, individual/party audience selection, observer/revoked/invited access, campaign mismatch and explicit local revocation. Source edits and later GM notes do not silently modify already published local snapshots.
- Verification: all five executable JS script bodies pass Node syntax; five embedded JSON and four prior executable JS script bodies byte-identical to Cycle29. Chromium 41/41 focused checks PASS at desktop 1440, tablet 768 and phone 390; zero page JS errors/horizontal overflow. Inherited Cycle27 Regression Lab 27/27 PASS.
- Native browser-origin persistence and installed/shared D24/A6/D05 remote authority remain **not verified**. In-memory controlled localStorage shim only. Independent screen-reader, cross-device, Map Maker/Downtime import not tested.
- **Next planned IS-04 / Cycle31:** Clue Definitions and Campaign Clue/evidence records, distinct prepared vs discovered vs revealed state, strict provenance and audience boundaries.


## IS-04 / Cycle 31 status — 2026-11-22

**Delivered for owner playtest**, no installed-app or authoritative D24 implementation.

- Artifact: `Multiversal_GM_Playtest_Cycle_31.html`, 15,475,619 bytes, SHA-256 `317acef25a66de89b8a633aab77791f169d4302d3cba7a02d325e6c6eb59c56f`.
- New GM **Clue & Evidence Workshop** under Prepare. Reusable source-referenced Clue Definitions independent of any campaign. Explicit Campaign Clue instances bound to existing IS-02 case placements, with stable identity, pinned source revision and duplicate guards.
- Manual Evidence References store source owning domain, object ID, source version, role and private provenance note, never copy ownership or assert truth/authenticity.
- Standalone local GM-controlled lifecycle: registered-hidden, discoverable, discovered-private, discovered-shared, withheld, revoked, superseded, archived. Private/party simulation requires an active case placement, current pinned source, active Player or party audience, player-safe authored text, and explicit method. No D24 Event is emitted.
- Player preview is derived from authorized local instances and immutable disclosure snapshots, not from a complete GM record. Archived/withheld/revoked clues and evidence notes/hidden counts are absent from Player projection. This is not real server-side access control.
- Optimistic expected-revision and stable operation ID/collision controls, explicit refresh, evidence link retirement history, safe fallback for temporary unavailable campaign fixtures and GM-only JSON archive.
- **Verification:** Node --check 6/6 executable blocks; five embedded JSON blocks valid; all 10 prior script blocks byte-identical. Chromium Playwright 45/45 checks passed including the original Cycle27 27/27 regression suite; 1440/768/390 px render clean with zero errors/overflow. The original Regression Lab's temporary campaign replacement revealed a missing-reference crash, repaired by fail-closed historical projection then rerun green.
- **Not verified:** native file:// storage reload, installed dual-device D24/A6/D05 authority, independent imports, offline/reconnect and screen-reader behavior. Tests use page.set_content() and a controlled localStorage shim.
- **Next:** IS-05 / Cycle32 — observation, claim and witness testimony with witness belief, evidence origin, source reliability and authenticity kept distinct from objective truth.

## IS-05 / Cycle 32 status — 2026-11-22

**Delivered for owner playtest**, not installed-app or authoritative D24 implementation.

- Artifact: `Multiversal_GM_Playtest_Cycle_32.html`, SHA-256 `32bc3f32247662411c6085a4904b7176fde62f6b12f70cbf014c4b7327f37edd`, 15,512,338 bytes.
- GM **Witnesses & Testimony** workshop under Prepare and linked from Investigation & Social and Clue & Evidence. Records are bound to a case placement by reference; no new NPC/Character identity, canonical Observation/Claim store, or case truth store.
- Witness profiles include explicit NPC/source ID, source version and provenance, safe display alias, GM-private context, stable local revision, duplicate and archive controls.
- **Observation** holds observer subject, perceived wording, source ref and reliability. **Claim** references an active witness, original assertion, speaker belief, source reliability, separate authenticity indicator and truth reference. They cannot be reclassified into each other or promoted into objective fact. Only supported A9 truth-reference states (unknown or externally-referenced without verification) are modeled.
- Optional link to an existing same-case Campaign Clue leaves its ownership, discovery and reveal unchanged. An existing external truth reference remains unverified in this HTML.
- Local GM release chooses active Player or party and requires deliberately authored public wording and rationale. Player projection uses only frozen safe fields, excludes private notes, evidence IDs, source reliability/authenticity and hidden counts. Paused case, observer, revoked participant and cross-campaign filtering fail closed. Explicit revocation preserves historical receipts.
- **Verification:** all 7 executable JS scripts Node-parse; 5 embedded JSON parse; original 11 scripts byte-identical to Cycle31. Chromium 45/45 focused checks PASS, including inherited Cycle27 Regression Lab 27/27; separate real-form DOM interaction creates a witness, records Claim and shares to party. 1440/768/390 viewport no JS exceptions/overflow.
- **Unverified:** actual browser-origin/file:// persistence (test used storage shim), real installed D24/A6/D05 rights and Event authority, two-device Windows/Android, native screen reader and independent Map Maker/Downtime importer. Local Player preview cannot enforce server-side security.
- **Next planned:** IS-06 / Cycle 33 — player/GM Hypothesis and Question records, typed semantic links, graph/list parity, permission-before-topology and nonvisual navigation.


## IS-06 / Cycle 33 status — 2026-11-22

**Delivered for owner playtest**, not installed-app or canonical D24 implementation.

- Artifact: `Multiversal_GM_Playtest_Cycle_33.html` (15,547,348 bytes), SHA-256 `8cf4c16fd5898dad623c8093f9c0c735ca8f5e5914af914f0b2c1f44dfb01155`.
- New **Connected Clue Board** in GM Prepare and linked from Investigation & Social. A case placement can show existing Cycle31 Campaign Clue IDs, Cycle32 Claim/Observation IDs, and IS-06 player/GM-created Hypothesis and Question records. Explicit semantic links use exactly the 15 D24 predicates from current `connection-port.ts` with directional endpoints, rationales, version, actor operation ID, and GM/party/individual preview audience.
- Player UI can author a private hypothesis or question when a case is already available to them; a deliberate Player Share button makes it visible to the party. The GM graph/inspector/private archive exclude other people's unshared private theories, per F011. All hypotheses carry `objectiveTruth:false`; this cycle cannot issue a canonical GM Conclusion.
- Authorization-first Player projection: only already disclosed Cycle31 clue and Cycle32 testimony snapshots plus own or intentionally shared theories; hidden endpoints and their counts/topology do not appear even if an edge is marked party-visible. Semantic diagram/list/outline share identities and typed links; diagram geometry never owns meaning.
- Reject unsupported predicate, invalid/cross-case endpoint, duplicate typed link, conflicting operation ID, stale expected revision, unauthorized actor, historical/paused case mutation. Retired links and archived items remain historical.
- **Verification:** source 12 prior HTML script blocks preserved byte-for-byte, 5 source JSON blocks parse, Node 8/8 JS syntax. Chromium focused 55/55 PASS, including inherited Cycle27 Regression Lab 27/27, GM form submission and actual Player Share click; desktop 1440, tablet 768 and mobile 390 zero page errors and no document overflow.
- **Unverified:** native `file://` persistence/reload (tests use page.set_content and localStorage shim), server D24/A6/D05 authorization, installed Windows/Android two-device, independent Map Maker/Downtime import and native assistive-technology testing.
- **Next planned IS-07 / Cycle34:** case timelines and alibis, contradiction review and false leads with source provenance. Contradiction never automatically decides which statement is true.

## IS-07 / Cycle 34 status — 2026-11-22

**Delivered for owner playtest**, NOT installed-product/D24/PPIA-12 implementation.

- File: `Multiversal_GM_Playtest_Cycle_34.html` · 15,587,408 bytes · SHA-256 `9a5face49316313cc487146a6f16146ee8f546b09231fcbefe3659d8099d446e`. Supporting `Multiversal_GM_IS07_Cycle34_Verification_Notes.md` and `Multiversal_GM_IS07_Cycle34_Automated_Report.json`.
- Permanent GM **Prepare → Timeline & Alibi Review** plus Investigation & Social Director launch, available outside a live session. Existing case placements own local context; references never create canonical D24 Campaign Clues/Observations, A6 actions, or PPIA-12 Setting chronology.
- Case Event and Alibi authored records use explicit owning source IDs/versions; five PPIA-09 time forms: exact, bounded-window, relative-before, relative-after, unknown. Numerical local timestamps require a shared clock/calendar basis; circular relative anchors, invalid calendar days and reversed intervals are rejected. Relative/unknown setting-specific time is not silently converted to Gregorian values.
- Read-only interval diagnostic compares only compatible numeric windows and reports overlapping/separate/not-comparable **without determining source truth**.
- Manual GM contradiction reviews retain two attributed same-case source snapshots from existing Timeline, Clue and Observation/Claim records, eight PPIA-09 classes, six PPIA-09 review states, source-history rationale and expected-version/idempotency protection. A claimed externally authorized conclusion reference is **not verified in this HTML** and cannot become canonical fact.
- Player-safe separate text is explicitly authored and locally published to active Player or party. Frozen disclosure, GM notes/source version/contradiction history exclusion, revocation, player/observer/revoked/campaign/pause scope and GM-only export are tested. Private Player hypothesis drafts from IS-06 remain untouched; single-file Player preview is not real server-enforced privacy.
- **Verification:** all 13 preceding embedded scripts are byte-identical to Cycle33; all 5 source JSON parse; Node --check 9/9 executable JS scripts PASS. Chromium Playwright 58/58 new Cycle34 checks PASS and 55/55 inherited Cycle33 checks PASS (including Cycle27 27/27), with desktop 1440, tablet 768 and mobile 390 zero uncaught page exceptions or document horizontal overflow.
- **Unverified:** native `file://` browser reload storage (automation used `page.set_content` with localStorage shim), installed D24/D05/A6 server authority, two-device Windows/Android, world-specific calendar sources, independent Downtime/Map Maker import, native screen-reader and offline/reconnect boundaries.
- **Next planned:** IS-08 / Cycle35 — revelation/route dependencies, warnings for important information with one authored route, stall recovery and read-only solvability diagnostics, without revealing or solving an investigation.

## IS-08 / Cycle 35 status — 2026-11-22

**Delivered for owner standalone GM playtest**, not installed-app, D24 or MAS runtime implementation.

- Artifact: `Multiversal_GM_Playtest_Cycle_35.html` · **15,625,461 bytes** · SHA-256 `2b5c3e8a7260882cf629a480cd782e21d714db3145be37d97a7dfb93ea1c51b8`. Local verification notes and full machine-readable test report accompany the HTML.
- GM **Prepare → Revelation Routes & Solvability Review** and top **Investigation + Social** entry. Opens with zero campaigns/scenes; authored revelations remain bound to reusable Cycle29 case definitions, not to active scene or an independent truth database.
- Revelations have required/optional/bonus authoring priority, GM-only description, optional important-for-progression marker, source/provenance and pinned case revision. Routes point to same-case dossier leads, reusable Clue Definitions, Campaign Clues, testimony, timeline/alibi, or explicitly labeled unverified manual source. All-of prerequisites on a route; multiple routes to a revelation are authored alternatives (OR). Routes can be primary, alternative or stall-recovery; duplicate-of and disabled states are explicit.
- **Read-only authoring diagnostic:** fixed-point dependency evaluation marks locally sourced, provisional manual or currently unreachable *planned* revelations; flags circular prerequisites, important information with fewer than two distinct discovery routes (direct source guidance, not universal requirement), required single-point route, missing designated recovery route, missing/retired or stale source, stale case-revision pin. A text outline and structured table are semantically equivalent, with no graph geometry/drag dependency.
- Strict separation: authored routes are **not discovered**, revealed, authorized Player knowledge, successful Investigation, verified conclusion, objective truth, NPC/world change, or actual GM decision. Manual references are not source canon. No new Player preview, output payload, source discovery or private note access is added.
- Source/evidence identity and version protection: same-case guards, active source checks, expected version, operation ID replay/collision denial, duplicate route and duplicate-of-cycle rejection, historical retirement, GM-private JSON export.
- **Fresh verification:** all 14 earlier embedded script blocks byte-identical, 5 original JSON datasets parse, Node --check 10/10 executable blocks; Playwright Chromium Cycle35 58/58 focused checks PASS, inherited Cycle34 58/58 and Cycle33 55/55 PASS, Cycle27 Regression Lab 27/27 within those. 1440/768/390 responsive render no page exception/overflow. A separate 390px empty-campaign route + actual GM-private JSON download/parse smoke passed.
- **Not verified:** native `file://` reload/localStorage persistence (Playwright `set_content` + controlled shim), installed Windows/Android multiplayer, D24/D05/A6 server-side operations and actual audience security, independent Downtime/Map Maker imports, source Calendar/Knowledge adapters, screen-reader acceptance.
- **Next planned IS-09 / Cycle36:** authorized GM conclusion, safe player case resolution projection, history and continuity/recovery while preserving private Player hypotheses and prior source events.

## IS-09 / Cycle 36 status — 2026-11-22

**Delivered for standalone owner playtest**; no installed-app or authoritative D24 implementation.

- Artifact: `Multiversal_GM_Playtest_Cycle_36.html`, SHA-256 `a0db226f9344dab72561d5e5acd94b4ebe7843581f1c12ed0e3fb018226de3a8` · 15,665,200 bytes. Notes and an inspectable JSON automated report accompany the user artifact.
- Added **Prepare → Conclusions & Case History**, also launched from Investigation & Social Director. GM chooses an existing campaign-specific case placement (not tied to a live scene) and drafts an interpretation linked by stable ID to same-case local Campaign Clues, Observations/Claims, timeline entries or prepared revelations. Player-private hypotheses are never treated as evidence visible to the GM.
- Deliberate **recorded-local** milestone requires a Ready current pinned case, private reasoning, source references and GM acknowledgment. It snapshots source identities/labels/versions, disallows silent edits to recorded conclusions, enforces expected revision and stable operation id, and preserves replacement decisions in history. **It does not emit D24 `ConclusionRecorded`, change campaign lifecycle or promote hypotheses into objective truth**.
- Player-safe resolution handouts are separately authored title/summary/outcome fields, published locally to party or an active Player with explicit GM rationale. Only frozen safe snapshots are projected; GM truth, rationale, source IDs/versions and private Player theories are excluded. Access projection respects campaign, active Player, paused/archived case, direct revocation and supersession. Supersession revokes extant handouts while retaining historical disclosure copies.
- Linear private history displays draft revisions, source snapshots, local status transitions, handout revocation and bounded action receipts. GM-only private checkpoint JSON is downloadable. A real browser file-input/import test verified **merge-only, draft-only restoration requiring GM review**; prior published/revoked handouts cannot be automatically restored.
- **Verification:** all 15 preceding HTML script bodies byte-identical to Cycle35, 5 JSON source blocks parse and Node --check 11/11 executables PASS. Chromium Cycle36 focused 58/58 PASS, inherited Cycle35 58/58 PASS, inherited Cycle34 58/58 PASS, inherited Cycle33 55/55 PASS (including original Cycle27 GM Regression Lab 27/27). Five additional real button/file-input/download/recovery checks PASS. Desktop 1440, tablet 768, mobile 390 had zero uncaught page errors or document overflow.
- **NOT VERIFIED:** real `file://` browser-origin persistence/reload (tests use `page.set_content()` plus localStorage shim), installed Windows/Android/two-device multiplayer, canonical D24/A6 recorded Events, server D05 authorization, screen readers or cross-tester Map Maker/Downtime imports.
- **Next planned IS-10 / Cycle37:** Social Director with source-informed freeform, assisted and structured social encounters/challenges, NPC context and participant selection. D25 social owns runtime interaction; A6/A5/D05 boundaries remain separate.
