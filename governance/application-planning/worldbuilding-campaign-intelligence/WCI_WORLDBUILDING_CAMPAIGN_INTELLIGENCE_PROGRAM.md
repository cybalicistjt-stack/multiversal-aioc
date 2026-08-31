# WCI — Worldbuilding & Campaign Intelligence

**Program ID:** WCI  
**Status:** OWNER-APPROVED — COMPLETED THROUGH WCI-03; WCI-04 IN_PROGRESS  
**Activation:** after completed_verified SSA-10  
**Successor:** KFR-01  
**Owner and final authority:** John Brandon Turner

## Current state

WCI-01 and WCI-02 remain `completed_verified`.

WCI-03 — Relationship, Genealogy, Organization & Diplomacy Explorer — is `completed_verified` through application PR #364 and merge `e4868f1f20bb79ce5bf5bc26011a48bdabe4449f`. Exact validated head `5ba9053074ce02388d8802bfb2ce73db1a4b0ddc` passed current-family run `33394836057`: selector/Repository Health `99496771071`, self-hosted Linux `99496807995`, self-hosted Windows `99496808072`, and deterministic comparison `99496985633`. Linux and Windows produced matching deterministic receipt SHA-256 `3fd0f5d7c67d2bba92040413f581848e7037526b7e1f3df18e2b9735138c43ec`, with zero historical predecessor fanout.

WCI-04 — Living Campaign, GM Workspace & Session Intelligence — is bounded `in_progress` from exact application main `e4868f1f20bb79ce5bf5bc26011a48bdabe4449f` on `integration/wci-04-living-campaign-gm-workspace-session-intelligence`. Product mutation is permitted only after the exact governed-start AIOC candidate passes Repository Health and merges.

## Purpose

WCI solves worldbuilding/campaign workspace problems through Multiversal's existing canonical entities and systems rather than building parallel article, relationship, history or campaign databases.

## Tranches

1. **WCI-01 — World Knowledge Workspace & Canonical Entity Views** — completed_verified.
2. **WCI-02 — History, Calendars, Timelines, Chronicles & Reality Explorer** — completed_verified.
3. **WCI-03 — Relationship, Genealogy, Organization & Diplomacy Explorer** — completed_verified. Family/dynasty, organization hierarchy, allegiance, faction diplomacy and social graph views over MIB-09 and canonical Character/organization relationships; no second relationship ledger; KFR knowledge/familiarity remains separate.
4. **WCI-04 — Living Campaign, GM Workspace & Session Intelligence** — in_progress. Campaign operating workspace for party/NPC/plot/adventure/session preparation, quests/projects, clues, notes, handouts, current state, return summaries and GM controls by composing existing APW/APM/Scene/Investigation systems, including native ISE prepared-Scene and SSA spatial references where useful.
5. **WCI-05 — Creator Writing, Continuity, Consequence Analysis & Integrated Proof** — planned. Connect manuscripts/stories/plots/hooks to world entities; show dependencies, potentially inconsistent material and consequences of proposed changes; support proposal-only assistance, continuity checks and a full worldbuilding→campaign golden proof.

## WCI-04 bounded contract

- APW/APM, Adventure/Project, Character, Scene, Investigation, ISE, SSA, Event/time and Permission/visibility owners remain authoritative. WCI-04 composes stable owner references and cannot mint a second party, NPC, plot, quest/project, clue, Scene, investigation, session or campaign ledger.
- APW campaign-activity orchestration remains non-authoritative for owning-domain gameplay effects; WCI-04 cannot promote orchestration state into canonical gameplay truth.
- APM Mini-Campaign keeps Adventure graph/run authority external and requires fresh owner state before route transitions; WCI-04 session intelligence cannot choose meaningful player routes, reveal hidden state or fabricate owner results.
- The living campaign workspace may project authorized party/NPC/plot/adventure/session preparation, quest/project, clue, note, handout, current-state, return-summary, prepared-Scene and spatial references with stable provenance. Presentation grouping is not canonical state.
- Consequential changes are proposal-only. WCI-04 may form versioned, idempotent owner-operation proposals with canonical owner reference, expected owner version, operation kind and evidence, but the owning domain must authorize and commit any mutation.
- Session and return summaries are projections over authorized committed evidence; they cannot silently advance campaign time or infer uncommitted outcomes.
- Authorization and visibility filtering precede counts, summaries, party/NPC/plot state, clue/handout projection, return summaries, player/reader views and AI context. GM-only/private state and protected cardinality cannot leak through aggregate output.
- Consequential campaign/session information requires accessible nonvisual summaries/equivalents; boards, graphs, maps and prepared-Scene visuals are not exclusive truth.
- Equivalent authorized inputs produce deterministic ordering, projections and receipts independent of view/platform; wall-clock timing, layout and canvas position are not semantic truth.
- No durable WCI-04 persistence is required; canonical owner persistence remains authoritative and migration `0022` remains unreserved.
- Public/community publishing, paid provider activation, tester distribution, release/deployment, WCI-05+ and KFR-01+ remain separately governed and unauthorized here.

## Invariants

- WCI workspaces do not become second canonical World, Character, relationship, Event/history/calendar, campaign, session, Scene, Investigation or Project ledgers.
- APW/APM, Adventure/Project, Character, Scene, Investigation, ISE, SSA, Event/time and Permission/visibility owners remain canonical for WCI-04.
- Hidden/GM/private content and protected cardinality are filtered before counts, summaries, player/reader views and AI context.
- Consequential workspace information has accessible nonvisual representation.
- Equivalent authorized workspace inputs produce deterministic ordering/projection receipts independent of view/platform.
- No durable WCI-04 persistence or migration `0022` is authorized.
- Public/community publishing, paid provider activation, tester distribution, release/deployment and WCI-05+ remain separately governed and unauthorized here.
