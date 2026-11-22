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
