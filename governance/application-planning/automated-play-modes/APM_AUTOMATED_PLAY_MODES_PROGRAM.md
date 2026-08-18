# APM — Automated Play Modes Program

**Program ID:** APM  
**Version:** 0.1.0  
**Status:** OWNER-APPROVED PARALLEL PLANNING TRACK — PLANNED / NOT IMPLEMENTATION-ACTIVE  
**Owner and final authority:** John Brandon Turner  
**Approved planning direction:** 2026-08-18

## 1. Purpose

APM defines two additional Multiversal play experiences without creating a second game engine:

- **AutoGM** — governed automated orchestration for bounded solo play, beginning with single encounters and short mini-campaigns. It is expected to be less capable than a strong human GM and is intentionally scoped accordingly.
- **CozyMode** — a low-pressure automated solo play experience built primarily on downtime, persistent Personal/Campaign workspaces, character/world progression, projects, relationships, crafting, research, light exploration, journaling, and similar activity; it may later connect to invited other players through the same persistent multiplayer architecture.

Both modes reuse existing Campaign, Action, proposal/approval, Event, permissions, persistence, provenance, recovery, World, Adventure, Character, downtime, social, crafting, investigation, creator and notification architecture.

## 2. Controlling product principles

1. AutoGM and CozyMode are play experiences, not permanent account roles and not alternate canonical state engines.
2. `AutoGM` must not mean an AI provider receives unrestricted GM authority. A governed automation controller receives only the explicit delegated operations required by the selected automated-play package.
3. Mechanical legality, state transition and canonical mutation remain governed by deterministic/domain-owned rules and authority checks. Optional AI may narrate, converse, summarize, transform presentation or propose bounded content but may not silently bypass those checks.
4. CozyMode is a style/cadence of play rather than a genre. The same framework must be able to support, for example, a quiet starship mechanic, occult shopkeeper, homesteader, alchemist, researcher or other setting-appropriate activity profile.
5. AutoGM Internal Alpha scope begins with **Single Encounter** and **Short Adventure / Mini-Campaign**. Unlimited open-ended autonomous campaigns are not an initial completion requirement.
6. Automated play must preserve one attributable history, provenance and recovery model with ordinary Multiversal play. A Character/world may move between CozyMode, AutoGM, asynchronous Campaign activity and ordinary live play without creating silent forks.
7. Connected Cozy uses invited/known participants first. Public stranger discovery/matchmaking is outside the initial APM scope and remains subject to later community/family-safety governance.
8. Core Cozy organization and progression must retain useful non-AI operation where the owning systems permit it.
9. All automated operations must be inspectable enough to identify the originating mode/controller, governing rule or scenario package, and resulting authoritative Event.
10. No APM tranche grants release, deployment, paid-provider, production credential, public marketplace or autonomous publication authority.

## 3. Core execution model

AutoGM target flow:

`Player Action → AutoGM Controller → Rules / Scenario State → Governed Resolution → Authoritative Event → Role-safe Projection`

Optional AI presentation surrounds but does not replace that authority chain:

`Authorized Scenario/World State → Optional AI narration/dialogue/suggestion → Filtered Presentation`

CozyMode target loop:

`Choose Activity → Progress / Time → Event or Opportunity → Player Choice → Governed Resolution → Reward / Consequence → Persistent State → Next Activity`

## 4. Tranche plan

### APM-01 — Automated-Play Authority and Mode Contract

Define Solo/AutoGM/Cozy/Connected Cozy terminology; distinguish mode from Context, Cadence, Connectivity and role; define automation-controller authority, explicit user delegation, start/stop/revoke behavior, auto-resolvable operations, mandatory player-choice boundaries, deterministic versus optional-AI responsibility, provenance and save/exit/resume rules.

**Gate:** no AutoGM/Cozy flag can imply global GM authority or bypass an owning domain.

### APM-02 — CozyMode Core Loop

Define Character/workspace selection, activity discovery, downtime/project progression, time/progress, event/opportunity generation, player choice points, setback/default failure philosophy, relationships/projects/resources, summaries, pause/resume, no-AI fallback where supported, and transitions between CozyMode and ordinary Campaign/Personal contexts.

**Gate:** a useful solo cozy loop can persist and resume without creating a separate state engine or requiring a human GM continuously online.

### APM-03 — AutoGM Single-Encounter Runner

Define Character selection, encounter package selection/import, setup/difficulty preferences, exposition, player Action, NPC/world response, deterministic mechanical resolution, state transitions, end conditions, summary/rewards, persistence and replay. Reuse governed scenario/fixture/rules infrastructure rather than letting narrative generation own game state.

**Gate:** one bounded solo encounter completes, resumes after interruption, and produces the same governed mechanical outcome for the same deterministic inputs.

### APM-04 — AutoGM Mini-Campaign Director

Extend AutoGM over a short Adventure graph using CSW/Adventure structure: premise, scenes, hooks, revelations, choices, consequences, alternate routes, open threads and end conditions. Initial target is a bounded short adventure rather than unlimited autonomous campaign generation.

**Gate:** a short multi-scene solo Adventure preserves continuity, authority, hidden information, provenance and deterministic mechanical state while allowing optional narrative assistance.

### APM-05 — Connected Cozy and Shared Automated Play

Add invited-participant shared cozy spaces/activities, cooperative projects, governed resource contribution, social/relationship activity, async contribution, live co-op windows, notification, leave/rejoin and participant authority. Preserve a later seam for multi-player AutoGM without requiring it for first APM completion.

**Gate:** solo Cozy can become invited Connected Cozy and return without authority bleed, duplicate state or hidden-information leakage.

### APM-06 — Recovery, Safety, Acceptance and Implementation Handoff

Define interruption/reconnect, stale state, duplicate Action, optional-AI unavailable/illegal suggestion, automation-out-of-scope attempts, hidden-information filtering, Cozy ↔ ordinary Campaign, Solo Cozy ↔ Connected Cozy, AutoGM encounter ↔ mini-campaign, deterministic replay, provenance and implementation slices.

**Gate:** the complete automated-play design has explicit owning domains, persistence and authority boundaries, recovery behavior, acceptance cases and additive implementation destinations.

## 5. Approved planning interleave

APM is inserted into the existing APW/CSW sequence as follows:

1. APW-01 — Authority / Account / Context
2. APM-01 — Automated-Play Authority & Mode Contract
3. CSW-01 — Creative Object Model
4. CSW-02 — Creative Library / Story Bible
5. APW-02 — Async Action / GM Inbox
6. APW-03 — Between-Session / Downtime
7. APW-04 — Personal Workspace
8. APM-02 — CozyMode Core Loop
9. CSW-03 — Idea Inbox
10. CSW-04 — Guided Creation
11. CSW-05 — Plot / Adventure Lab
12. APM-03 — AutoGM Encounter Runner
13. CSW-06 — Continuity / Open Threads
14. APM-04 — AutoGM Mini-Campaign Director
15. CSW-07 — Writing Studio
16. CSW-08 — Reuse / Remix
17. APW-05 — Creator Workshop / Sandbox
18. CSW-09 — Creator Command Center
19. APW-06 — Shell / Navigation / Notifications
20. APM-05 — Connected Cozy / Shared Automated Play
21. CSW-10 — CSW Integration / Handoff
22. APW-07 — Persistence / Recovery / Security
23. APM-06 — Automated-Play Acceptance / Handoff
24. APW-08 — APW Implementation Handoff

This interleave preserves APW authority/downtime/persistence dependencies and lets AutoGM consume structured CSW Adventure/continuity architecture instead of inventing parallel narrative state.

## 6. Provisional implementation ladder

The preferred first implementation progression is:

`Cozy Solo → Single-Encounter AutoGM → Connected Cozy → AutoGM Mini-Campaign → broader/multiplayer AutoGM later`

Each step must reuse and strengthen infrastructure required by the next.

## 7. Program boundaries

APM planning does not itself authorize application implementation, release, deployment, public matchmaking, autonomous AI authority, paid AI services, production credentials, canonical content promotion or public community publication.

CCTI-12-T04 remains separately validation-quarantined. VCH completion does not imply APM implementation, and APM planning must not become a new blocker for already-approved independent production work.
