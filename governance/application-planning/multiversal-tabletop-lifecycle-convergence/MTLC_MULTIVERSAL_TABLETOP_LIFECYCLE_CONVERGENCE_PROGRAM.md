# Multiversal Tabletop Lifecycle Convergence (MTLC)

**Program ID:** MTLC  
**Status:** OWNER_APPROVED_ACTIVE  
**Authority:** Program definition is owner-approved. Live implementation authority is selected only by `operations/CURRENT.json`; as of 2026-10-06 MTLC-01 is CURRENT-selected in the former terminal FGA/FDE persistent slot. This document cannot independently expand that scope.  
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

Recover legacy/source-backed consent and Veils material; reconcile it into current product references; add CWKS to the feature census; audit the existing Feature/UI/Screen/Project Bibles and live implementation families against the connective-tissue inventory; classify every candidate as `EXISTS`, `RECOVER`, `CONVERGE`, `ADD`, `INTEGRATE`, `DEFER`, or `DO_NOT_BUILD`; create and maintain the durable friction registry and traceability matrix so future work never reinvents an existing feature or loses evidence of a recurring community need.

**Exit condition:** Every MTLC feature has an owner/source/status, every community-derived friction has an MTLC mapping or explicit rejection/defer rationale, and no item is classified as missing solely because it was lost in historical convergence.

### MTLC-02 — Private Table Formation and Campaign Onboarding

**Responsibility:** Make it effortless for an existing group to become a Multiversal table.

Cover player/GM profiles needed for private play; campaign recruitment pages; invite links and QR joins; join requests; seat counts; waitlists; player/role assignment; whole-party invitations; guest/observer/co-GM roles; campaign expectations preview; campaign templates; and conversion of a temporary one-shot group into a persistent campaign. Common onboarding must remain useful with sparse information and must not require exhaustive profile/database completion.

Public discovery/LFG is intentionally reserved for MTLC-12 because public communities require moderation and abuse controls.

**Exit condition:** A GM can create a campaign and onboard an existing group without relying on an external group-management tool or completing unnecessary configuration.

### MTLC-03 — Campaign Lounge and Group Communication

**Responsibility:** Give every campaign a persistent social home between sessions.

Provide campaign text chat, channels, threads, announcements, mentions, reactions, polls, pins, bookmarks, spoiler text, attachments, handouts, link previews, GM-only spaces, player-private conversations, in-character/out-of-character spaces, searchable history, campaign notices, and granular notification controls. Messages should be convertible into Multiversal objects where appropriate. Communication/history must preserve offline, export, backup, privacy, and provider-exit expectations rather than becoming a new non-portable silo.

**Exit condition:** Routine campaign communication no longer requires a dedicated Discord server or group chat, and the resulting campaign history remains portable under governed export/privacy rules.

### MTLC-04 — Scheduling, Attendance, and Real-World Logistics

**Responsibility:** Remove the coordination work required to get people to the table and reduce scheduling failure as a cause of campaign collapse.

Provide availability polling, recurring schedules, timezone handling, RSVP states, quorum rules, cancellation/rescheduling, reminders, calendar handoff/export, running-late/absent status, attendance history, venue and arrival notes, accessibility logistics, equipment checklists, optional food/potluck coordination, and other bounded real-world session logistics. Support explicit `run anyway` policies such as minimum quorum, approved absent-character proxy behavior, alternate one-shot/async fallback, and next-session polling after closeout where the campaign chooses them.

**Exit condition:** A group can schedule, reschedule, remind, decide whether to run with absences, and attend a session without an external poll/calendar coordination workflow.

### MTLC-05 — Session Zero, Consent, and Table Agreements

**Responsibility:** Turn Multiversal's source-backed consent/safety material into a first-class campaign workflow.

Recover and expose consent and Veils; support campaign expectations, content boundaries, tone, PvP rules, character-conflict expectations, character-death expectations, romance boundaries, secrecy/metagaming agreements, attendance expectations, recording/streaming consent, accessibility needs, communication preferences, and revisitable agreement state. Audit the original sources for any additional safety tools before adding new equivalents.

Include per-session adjustments, discreet pause/break mechanisms, temporary boundaries, and private GM signaling where source/canon and owner approval support them. Structured table-expectation data may later support transparent compatibility matching, but must not become an opaque desirability or reputation score.

**Exit condition:** A group can establish and revisit table expectations and consent without external forms or documents, with privacy appropriate to each field.

### MTLC-06 — Readiness, Homework, and Prep Cockpits

**Responsibility:** Tell every participant exactly what must happen before the next game while minimizing the amount of preparation Multiversal itself creates.

Provide Player Next Actions, GM Attention Center, player homework, pending approvals, advancement/preparation tasks, downtime deadlines, required handouts, pack/content readiness, character validity, sync/readiness checks, GM prep checklist, unresolved hooks, relevant NPCs/factions/clues, selected scenes, and a session preflight/Ready state. Apply **Minimum Viable Prep**: prioritize likely-relevant material and blockers, allow sparse useful records, and do not reward encyclopedic data entry merely because fields exist.

**Exit condition:** Before a session, the GM and every player can answer `What still needs to be done?` from one place, and Multiversal does not require more clerical prep than the workflow saves.

### MTLC-07 — Session Launch, Presence, and Table Modes

**Responsibility:** Make joining and remaining present in a session frictionless across in-person, remote, and hybrid tables, with mobile and hybrid participants treated as first-class seats.

Cover one-click session launch, QR/session join, guest/observer/co-GM entry, late join, AFK state, absent-player handling, delegated control when allowed, return-to-session catch-up, table display/second-screen mode, role-appropriate phone/tablet projections, in-person mode, hybrid mode, remote mode, voice-provider integration or bounded voice capability, optional video/screen-share integration, captions, and low-bandwidth fallbacks.

Hybrid support must address **presence parity**, not only transport: remote participants need visible presence, turns/reactions, shared dice events, synchronized handouts/map state, reconnect continuity, and GM-facing cues that reduce accidental exclusion without policing table behavior.

**Exit condition:** A mixed-device group can start, leave, rejoin, and continue a session without reconstructing state or manually coordinating who is present, and remote participants are not structurally second-class seats.

### MTLC-08 — Live Play Utilities, Rules, Handouts, and Media Control

**Responsibility:** Eliminate the small tool-switching interruptions that happen during play without making users operate a complicated VTT stack.

Provide a live utility bar; session/scene/break/countdown timers; dice, saved formulas, secret/blind/manual physical-dice entry and randomizers; map ping/ruler/template/annotation/viewport utilities; handout reveal/share/revoke; session audio playlists, ambience, stingers and soundboard control; bring-your-own audio; user-owned PDF/rulebook library; contextual Rules Concierge; rule bookmarks; and a Rulings Ledger for campaign adjudications.

Dense rule/ability surfaces should support progressive **Full / Standard / Essential** projections where appropriate, preserving canonical mechanics while reducing cognitive and mobile-screen burden. Common tabletop intentions should remain obvious even when expert controls exist behind progressive disclosure.

Heavy rendering, giant bundled art/audio libraries, and OBS-class production remain outside the core-client mandate.

**Exit condition:** Ordinary live-play interruptions can be resolved inside Multiversal or through a one-step Multiversal-controlled integration without forcing ordinary users through specialist configuration.

### MTLC-09 — Session Closeout and Campaign Continuity

**Responsibility:** Make the end of a session create durable campaign memory instead of cleanup work.

Handle attendance, rewards, loot, progression availability, relationship/faction/clue/quest changes, rulings, NPCs met, locations discovered, unresolved threads, player feedback where enabled, recap drafting/correction, `Previously on Multiversal`, missed-session catch-up, character-safe knowledge filtering, campaign timelines, and separation of real-world schedule time from in-world calendars/time.

Apply **Zero-Secretary Campaign Memory**: ordinary approved play/state changes should maintain continuity automatically wherever possible. Human correction and interpretation remain available, but accurate campaign memory must not depend on someone manually maintaining a second wiki or journal database. AI assistance may summarize, organize, retrieve, or draft but remains clerical/advisory and cannot silently invent canon.

**Exit condition:** Ending a session automatically prepares the campaign for both memory and the next session, and accurate continuity does not require a dedicated human campaign secretary.

### MTLC-10 — Between-Session Play and Party Administration

**Responsibility:** Keep the campaign alive between live sessions without turning group chat into the game database.

Support asynchronous scenes/play-by-post, downtime submissions, crafting/research/shopping/travel choices, party votes, planning boards, shared objectives, loot assignment, party funds, borrowing/ownership cleanup, character admin inboxes, advancement tasks, GM resolution queues, and due dates.

Asynchronous play must be **async-native**: scenes may remain open across days; actions can wait for governed GM resolution; private/parallel scenes can coexist; maps/state persist without a live host; notification cadence is controllable; mobile participation is first-class; and accepted outcomes reconcile through the same canonical authority boundaries as live play.

**Exit condition:** Between-session activity is structured, attributable, and automatically feeds canonical campaign state where the GM approves it, without requiring a live host or treating chat history as the database.

### MTLC-11 — Universal Connectivity, Capture, Automation, and Integrations

**Responsibility:** Make the entire Multiversal feature surface behave as one application rather than a collection of modules without creating a fragile plugin dependency ecosystem.

Provide global quick capture; Search Everywhere; universal links; `Show/Share/Pin/Attach`; `Turn This Into...`; object backlinks; no-code trigger/condition/action automation; governed macros/quick actions; command palette extensions; deep links; webhooks/adapters where appropriate; calendar/chat/OBS/audio/storage integrations; and safe declarative extension points that cannot bypass authority, permissions, provenance, or pack security.

Extensions must prefer stable declarative capability contracts with explicit permissions, dependencies, compatibility ranges, migration/rollback behavior, and campaign-visible compatibility before upgrade. AI-assisted connectivity follows the rule **AI is the clerk, not the GM**: assistance may organize, summarize, locate, convert, and propose, but not silently author canon or decide governed outcomes.

**Exit condition:** Information created in one Multiversal surface can flow to every relevant surface without manual re-entry, while upgrades/extensions remain inspectable and do not create dependency roulette.

### MTLC-12 — Public Discovery, Community, and Creator Network

**Responsibility:** Add public network effects only after the private tabletop lifecycle is strong and moderation foundations exist, and help users find compatible tables rather than merely available seats.

Cover public LFG/game discovery, player/GM public profiles, open seats, pickup games, creator profiles, community `.pack` discovery, follows, favorites, collections, ratings/reviews where approved, update/dependency visibility, creator publishing, and a Multiversal Exchange. Public game discovery may expose transparent, user-controlled compatibility dimensions such as schedule overlap, play preferences, tone/expectations, accessibility, experience, and commitment. It must not reduce people to an opaque quality/desirability score. Trial one-shots/temporary tables should be able to graduate cleanly into persistent campaigns.

Commerce, paid GM services, creator revenue share, coupons/bundles and paid marketplace behavior require separate commercial/legal gates.

Moderation, reporting, blocking, abuse prevention, content rights, takedown, appeals, age/minor boundaries, scam/spam handling, and privacy controls are mandatory dependencies for public surfaces.

**Exit condition:** Public game/content discovery can launch without pretending moderation, trust, rights, abuse handling, or table-fit information are someone else's problem.

### MTLC-13 — Accessibility, Onboarding, Physical Output, and Event Modes

**Responsibility:** Ensure Multiversal is usable by different kinds of tables, devices, experience levels, and venues.

Converge the Accessibility Control Center; new-player mode; new-GM mode; quickstarts/tutorials; simplified/focus layouts; progressive information-density modes; role-appropriate mobile companion workflows; printer-friendly character/rule/handout/card outputs; convention/one-shot mode; temporary guest onboarding; pickup-table setup; spectator/actual-play safe views; streaming overlays; and campaign handoff/co-GM continuity.

Accessibility is a cross-lifecycle requirement, not a final polish pass. Mobile/tablet behavior proven in MTLC-07/08 remains part of this tranche's convergence rather than being deferred until here.

**Exit condition:** New players, new GMs, physical-table users, convention users, mobile users, and accessibility-dependent users can participate without a second-class workflow.

### MTLC-14 — Golden Lifecycle Certification and Friction Budget

**Responsibility:** Prove the promise end-to-end and prevent future regressions back into app-switching friction or human-administration burden.

Build golden lifecycle fixtures across Windows and Android for the complete tabletop loop. Measure click/step counts, mandatory configuration steps, representative prep/administration minutes, manual campaign-memory maintenance required for accurate continuity, unresolved external dependencies, cold-start/session readiness, offline/reconnect behavior, sync recovery, search latency, memory, package size, optional-media separation, mobile/tablet role parity, hybrid-presence parity, async-without-live-host behavior, extension/pack upgrade safety, and representative large-campaign workloads. Establish permanent size/performance/friction/administration budgets and a release gate that detects when a workflow again requires unnecessary external tooling or clerical labor.

The final acceptance scenario is:

`decide to play -> form/join group -> consent/agreement -> schedule -> prepare -> communicate -> launch -> play -> pause/reconnect -> close -> recap -> advance/downtime -> schedule next session`

**Exit condition:** The lifecycle is certified on supported platforms and the program can demonstrate that ordinary TTRPG administration, coordination, play support, continuity, and between-session work are Multiversal-native without shifting the burden into hidden maintenance work.

## 5. Cross-program constraints

1. **Do not preempt active lanes.** MTLC is future planned work until OPS3 explicitly selects/activates it.
2. **CWKS is a dependency, not a target for duplication.** MTLC consumes structured-document capabilities as they become current.
3. **Consent and Veils are recovery/convergence work first.** No replacement design may overwrite source-backed material without source audit and owner decision.
4. **Provider neutrality remains mandatory.** Voice, video, calendar, streaming, storage, AI, and similar services must not become irreversible architecture dependencies.
5. **Core-client size remains protected.** Media-heavy assets should be optional, cached, streamed, imported, or pack-based rather than bundled into the mandatory client.
6. **GM authority remains intact.** Automation, AI, async play, and integrations may propose or assist but must respect governed authority and permissions.
7. **Public community features require moderation readiness.** Public LFG, community content, and marketplaces may not ship ahead of their abuse/privacy/rights controls.
8. **No duplicate source of truth.** MTLC should connect canonical objects and workflows rather than recreate parallel campaign, character, rule, inventory, social, investigation, or media state.
9. **AI is the clerk, not the GM.** Generative assistance remains optional, attributable, reviewable, permission-aware, and non-authoritative until accepted where required; it may not silently invent canon or decide governed outcomes.
10. **Capability without operational complexity.** Product depth may be large, but ordinary intentions must map to obvious contextual actions with sparse useful defaults and progressive disclosure.
11. **Portable campaign ownership.** Connective-tissue data inherits Multiversal offline/reconnect, backup, restore, export, migration, privacy, and provider-exit obligations.
12. **Human-labor budgets matter.** A technically successful feature fails MTLC intent if its required bookkeeping or configuration costs more human effort than the friction it removes.
13. **Mobile and hybrid are cross-program acceptance dimensions.** They may not be postponed into a final responsive-design pass.
14. **Extension stability is a product promise.** Safe extensibility must expose compatibility and avoid silent campaign breakage from routine upgrades.

## 6. Program activation rule

MTLC is intentionally recorded as `OWNER_APPROVED_PLANNED`. Activation requires a future explicit owner direction plus OPS3 lane/governance selection. Activation should not silently replace an active persistent implementation lane. When activated, OPS3 should select the first eligible incomplete MTLC work item from the durable backlog and preserve the ordered dependency chain unless the owner explicitly reprioritizes it.

## 7. Durable planning records

Machine-readable ordering, responsibilities, dependencies, and exit criteria are recorded in:

`governance/application-planning/multiversal-tabletop-lifecycle-convergence/MTLC_PROGRAM_BACKLOG.json`

Community-derived unmet-need/friction evidence, its strength classification, mapped work items, source examples, and acceptance implications are recorded in:

`governance/application-planning/multiversal-tabletop-lifecycle-convergence/MTLC_COMMUNITY_FRICTION_REGISTRY.json`

The community registry is qualitative planning evidence rather than prevalence statistics. MTLC-01 owns its recovery/reconciliation and must classify each finding against current Multiversal reality before implementation.
