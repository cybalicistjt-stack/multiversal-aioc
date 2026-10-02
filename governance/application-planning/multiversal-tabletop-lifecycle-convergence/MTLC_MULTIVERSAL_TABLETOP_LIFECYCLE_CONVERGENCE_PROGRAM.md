# Multiversal Tabletop Lifecycle Convergence (MTLC)

**Program ID:** MTLC  
**Status:** OWNER_APPROVED_PLANNED  
**Authority:** Planning and future-program definition only. This document does not select current work, change `operations/CURRENT.json`, occupy a persistent implementation lane, or grant implementation authority.  
**Owner and final authority:** John Brandon Turner  
**Recorded:** 2026-10-02

## 1. Program purpose

Multiversal should become the default operating environment for tabletop roleplaying: when a group decides to play a TTRPG, the ordinary expectation should be to open Multiversal first.

The program therefore targets the connective tissue around tabletop play: the many small frictions that currently force players and GMs to jump among chat apps, scheduling tools, notes, PDFs, VTT utilities, audio tools, streaming overlays, calendars, file shares, LFG services, spreadsheets, and memory aids.

The governing product principle is:

> Multiversal owns the TTRPG lifecycle. Heavy external services may carry specialized payloads, but Multiversal should own the workflow and make handoffs nearly invisible.

This is not permission to bloat the core client with bundled media or to rebuild every heavyweight external service. Prefer structured data, UI, logic, provider-neutral adapters, optional downloads, local assets, and bounded integrations.

## 2. Existing foundations this program must reuse

MTLC must converge existing Multiversal systems rather than duplicate them. Important foundations include:

- campaigns, sessions, scenes, adventures, quests, objectives, and campaign timelines;
- character creation, character workspaces, inventory, progression, notes, and history;
- GM dashboards, campaign/scene builders, live session controls, approval workflows, improvisation, and post-session workflows;
- social, relationship, reputation, organization, faction, investigation, clue, evidence, timeline, and knowledge systems;
- maps, fog/reveal, cartography, spatial law, exploration, environments, vehicles, bases, economy, crafting, loot, and shared assets;
- local/online sessions, reconnect, persistence, recovery, permissions, notifications, search, provenance, import/export, and provider-neutral boundaries;
- audio/media asset infrastructure and VTT interoperability;
- CWKS structured long-form document editing and future writing/knowledge convergence;
- source-backed consent and Veils content from the legacy/original source corpus, which must be recovered and promoted rather than replaced from memory.

## 3. Program success condition

MTLC is complete only when the end-to-end lifecycle can be demonstrated without ordinary tabletop friction forcing the group into a second application for routine coordination:

`I want to play -> form/join table -> agree on game -> schedule -> prepare -> communicate -> launch -> play -> resolve -> close session -> recap -> advance -> do downtime -> schedule again`

Specialized heavyweight workflows may still use external providers, but the user should initiate and understand those workflows from Multiversal.

## 4. Ordered program path

### MTLC-01 — Canon Recovery and Friction Registry

**Responsibility:** Establish the authoritative connective-tissue baseline before new implementation begins.

Recover legacy/source-backed consent and Veils material; reconcile it into current product references; add CWKS to the feature census; audit the existing Feature/UI/Screen/Project Bibles and live implementation families against the connective-tissue inventory; classify every candidate as `EXISTS`, `RECOVER`, `CONVERGE`, `ADD`, `INTEGRATE`, `DEFER`, or `DO_NOT_BUILD`; create a durable friction registry and traceability matrix so future work never reinvents an existing feature.

**Exit condition:** Every MTLC feature has an owner/source/status and no item is classified as missing solely because it was lost in historical convergence.

### MTLC-02 — Private Table Formation and Campaign Onboarding

**Responsibility:** Make it effortless for an existing group to become a Multiversal table.

Cover player/GM profiles needed for private play; campaign recruitment pages; invite links and QR joins; join requests; seat counts; waitlists; player/role assignment; whole-party invitations; guest/observer/co-GM roles; campaign expectations preview; campaign templates; and conversion of a temporary one-shot group into a persistent campaign.

Public discovery/LFG is intentionally reserved for MTLC-12 because public communities require moderation and abuse controls.

**Exit condition:** A GM can create a campaign and onboard an existing group without relying on an external group-management tool.

### MTLC-03 — Campaign Lounge and Group Communication

**Responsibility:** Give every campaign a persistent social home between sessions.

Provide campaign text chat, channels, threads, announcements, mentions, reactions, polls, pins, bookmarks, spoiler text, attachments, handouts, link previews, GM-only spaces, player-private conversations, in-character/out-of-character spaces, searchable history, campaign notices, and granular notification controls. Messages should be convertible into Multiversal objects where appropriate.

**Exit condition:** Routine campaign communication no longer requires a dedicated Discord server or group chat.

### MTLC-04 — Scheduling, Attendance, and Real-World Logistics

**Responsibility:** Remove the coordination work required to get people to the table.

Provide availability polling, recurring schedules, timezone handling, RSVP states, quorum rules, cancellation/rescheduling, reminders, calendar handoff/export, running-late/absent status, attendance history, venue and arrival notes, accessibility logistics, equipment checklists, optional food/potluck coordination, and other bounded real-world session logistics.

**Exit condition:** A group can schedule, reschedule, remind, and attend a session without an external poll/calendar coordination workflow.

### MTLC-05 — Session Zero, Consent, and Table Agreements

**Responsibility:** Turn Multiversal's source-backed consent/safety material into a first-class campaign workflow.

Recover and expose consent and Veils; support campaign expectations, content boundaries, tone, PvP rules, character-conflict expectations, character-death expectations, romance boundaries, secrecy/metagaming agreements, attendance expectations, recording/streaming consent, accessibility needs, communication preferences, and revisitable agreement state. Audit the original sources for any additional safety tools before adding new equivalents.

Include per-session adjustments, discreet pause/break mechanisms, temporary boundaries, and private GM signaling where source/canon and owner approval support them.

**Exit condition:** A group can establish and revisit table expectations and consent without external forms or documents.

### MTLC-06 — Readiness, Homework, and Prep Cockpits

**Responsibility:** Tell every participant exactly what must happen before the next game.

Provide Player Next Actions, GM Attention Center, player homework, pending approvals, advancement/preparation tasks, downtime deadlines, required handouts, pack/content readiness, character validity, sync/readiness checks, GM prep checklist, unresolved hooks, relevant NPCs/factions/clues, selected scenes, and a session preflight/Ready state.

**Exit condition:** Before a session, the GM and every player can answer `What still needs to be done?` from one place.

### MTLC-07 — Session Launch, Presence, and Table Modes

**Responsibility:** Make joining and remaining present in a session frictionless across in-person, remote, and hybrid tables.

Cover one-click session launch, QR/session join, guest/observer/co-GM entry, late join, AFK state, absent-player handling, delegated control when allowed, return-to-session catch-up, table display/second-screen mode, phone companion behavior, in-person mode, hybrid mode, remote mode, voice-provider integration or bounded voice capability, optional video/screen-share integration, captions, and low-bandwidth fallbacks.

**Exit condition:** A mixed-device group can start, leave, rejoin, and continue a session without reconstructing state or manually coordinating who is present.

### MTLC-08 — Live Play Utilities, Rules, Handouts, and Media Control

**Responsibility:** Eliminate the small tool-switching interruptions that happen during play.

Provide a live utility bar; session/scene/break/countdown timers; dice, saved formulas, secret/blind/manual physical-dice entry and randomizers; map ping/ruler/template/annotation/viewport utilities; handout reveal/share/revoke; session audio playlists, ambience, stingers and soundboard control; bring-your-own audio; user-owned PDF/rulebook library; contextual Rules Concierge; rule bookmarks; and a Rulings Ledger for campaign adjudications.

Heavy rendering, giant bundled art/audio libraries, and OBS-class production remain outside the core-client mandate.

**Exit condition:** Ordinary live-play interruptions can be resolved inside Multiversal or through a one-step Multiversal-controlled integration.

### MTLC-09 — Session Closeout and Campaign Continuity

**Responsibility:** Make the end of a session create durable campaign memory instead of cleanup work.

Handle attendance, rewards, loot, progression availability, relationship/faction/clue/quest changes, rulings, NPCs met, locations discovered, unresolved threads, player feedback where enabled, recap drafting/correction, `Previously on Multiversal`, missed-session catch-up, character-safe knowledge filtering, campaign timelines, and separation of real-world schedule time from in-world calendars/time.

**Exit condition:** Ending a session automatically prepares the campaign for both memory and the next session.

### MTLC-10 — Between-Session Play and Party Administration

**Responsibility:** Keep the campaign alive between live sessions without turning group chat into the game database.

Support asynchronous scenes/play-by-post, downtime submissions, crafting/research/shopping/travel choices, party votes, planning boards, shared objectives, loot assignment, party funds, borrowing/ownership cleanup, character admin inboxes, advancement tasks, GM resolution queues, and due dates.

**Exit condition:** Between-session activity is structured, attributable, and automatically feeds canonical campaign state where the GM approves it.

### MTLC-11 — Universal Connectivity, Capture, Automation, and Integrations

**Responsibility:** Make the entire Multiversal feature surface behave as one application rather than a collection of modules.

Provide global quick capture; Search Everywhere; universal links; `Show/Share/Pin/Attach`; `Turn This Into...`; object backlinks; no-code trigger/condition/action automation; governed macros/quick actions; command palette extensions; deep links; webhooks/adapters where appropriate; calendar/chat/OBS/audio/storage integrations; and safe declarative extension points that cannot bypass authority, permissions, provenance, or pack security.

**Exit condition:** Information created in one Multiversal surface can flow to every relevant surface without manual re-entry.

### MTLC-12 — Public Discovery, Community, and Creator Network

**Responsibility:** Add public network effects only after the private tabletop lifecycle is strong and moderation foundations exist.

Cover public LFG/game discovery, player/GM public profiles, open seats, pickup games, creator profiles, community `.pack` discovery, follows, favorites, collections, ratings/reviews where approved, update/dependency visibility, creator publishing, and a Multiversal Exchange. Commerce, paid GM services, creator revenue share, coupons/bundles and paid marketplace behavior require separate commercial/legal gates.

Moderation, reporting, blocking, abuse prevention, content rights, takedown, appeals, age/minor boundaries, scam/spam handling, and privacy controls are mandatory dependencies for public surfaces.

**Exit condition:** Public game/content discovery can launch without pretending moderation, trust, rights, or abuse handling are someone else's problem.

### MTLC-13 — Accessibility, Onboarding, Physical Output, and Event Modes

**Responsibility:** Ensure Multiversal is usable by different kinds of tables, devices, experience levels, and venues.

Converge the Accessibility Control Center; new-player mode; new-GM mode; quickstarts/tutorials; simplified/focus layouts; mobile companion workflows; printer-friendly character/rule/handout/card outputs; convention/one-shot mode; temporary guest onboarding; pickup-table setup; spectator/actual-play safe views; streaming overlays; and campaign handoff/co-GM continuity.

**Exit condition:** New players, new GMs, physical-table users, convention users, mobile users, and accessibility-dependent users can participate without a second-class workflow.

### MTLC-14 — Golden Lifecycle Certification and Friction Budget

**Responsibility:** Prove the promise end-to-end and prevent future regressions back into app-switching friction.

Build golden lifecycle fixtures across Windows and Android for the complete tabletop loop. Measure click/step counts, unresolved external dependencies, cold-start/session readiness, offline/reconnect behavior, sync recovery, search latency, memory, package size, optional-media separation, and representative large-campaign workloads. Establish permanent size/performance/friction budgets and a release gate that detects when a workflow again requires unnecessary external tooling.

The final acceptance scenario is:

`decide to play -> form/join group -> consent/agreement -> schedule -> prepare -> communicate -> launch -> play -> pause/reconnect -> close -> recap -> advance/downtime -> schedule next session`

**Exit condition:** The lifecycle is certified on supported platforms and the program can demonstrate that ordinary TTRPG administration, coordination, play support, continuity, and between-session work are Multiversal-native.

## 5. Cross-program constraints

1. **Do not preempt active lanes.** MTLC is future planned work until OPS3 explicitly selects/activates it.
2. **CWKS is a dependency, not a target for duplication.** MTLC consumes structured-document capabilities as they become current.
3. **Consent and Veils are recovery/convergence work first.** No replacement design may overwrite source-backed material without source audit and owner decision.
4. **Provider neutrality remains mandatory.** Voice, video, calendar, streaming, storage, AI, and similar services must not become irreversible architecture dependencies.
5. **Core-client size remains protected.** Media-heavy assets should be optional, cached, streamed, imported, or pack-based rather than bundled into the mandatory client.
6. **GM authority remains intact.** Automation, AI, async play, and integrations may propose or assist but must respect governed authority and permissions.
7. **Public community features require moderation readiness.** Public LFG, community content, and marketplaces may not ship ahead of their abuse/privacy/rights controls.
8. **No duplicate source of truth.** MTLC should connect canonical objects and workflows rather than recreate parallel campaign, character, rule, inventory, social, investigation, or media state.

## 6. Program activation rule

MTLC is intentionally recorded as `OWNER_APPROVED_PLANNED`. Activation requires a future explicit owner direction plus OPS3 lane/governance selection. Activation should not silently replace an active persistent implementation lane. When activated, OPS3 should select the first eligible incomplete MTLC work item from the durable backlog and preserve the ordered dependency chain unless the owner explicitly reprioritizes it.

## 7. Durable backlog

Machine-readable ordering, responsibilities, dependencies, and exit criteria are recorded in:

`governance/application-planning/multiversal-tabletop-lifecycle-convergence/MTLC_PROGRAM_BACKLOG.json`
