# Application Implementation Roadmap — Automated Play Modes Supplement

**Document ID:** MV-APP-ROADMAP-APM-001  
**Version:** 0.1.0  
**Status:** ACTIVE OWNER-APPROVED ROADMAP SUPPLEMENT  
**Owner and final authority:** John Brandon Turner  
**Approved:** 2026-08-18

This supplement amends the planning projection in `APPLICATION_IMPLEMENTATION_ROADMAP.md` by adding **APM — Automated Play Modes** alongside the already approved APW and CSW planning tracks. It does not move the current runtime pointer, does not declare APM implementation active, and does not supersede current VCH/CCTI work-state evidence.

## Added product modes

- **AutoGM:** bounded governed automated GM orchestration for simpler solo play, initially single encounters and short mini-campaigns. Optional AI presentation does not receive unrestricted GM authority; legal state mutation remains governed by owning-domain rules and explicit automation scope.
- **CozyMode:** low-pressure automated solo play based primarily on downtime/persistent activity systems, with a later invited-participant Connected Cozy form. CozyMode is setting-independent and is not synonymous with one genre or activity type.

Canonical planning detail is in:

- `governance/application-planning/automated-play-modes/APM_AUTOMATED_PLAY_MODES_PROGRAM.md`
- `governance/application-planning/automated-play-modes/APM_PROGRAM_BACKLOG.json`

## Revised APW / CSW / APM planning order

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

## Implementation recommendation

Preferred implementation ladder after planning/handoff dependencies are satisfied:

`Cozy Solo → Single-Encounter AutoGM → Connected Cozy → AutoGM Mini-Campaign → broader/multiplayer AutoGM later`

This order maximizes reuse: Cozy Solo exercises persistence, downtime, Character, projects, relationships, crafting, Personal Workspace, Events and optional-AI seams before the harder continuous scene/NPC/world orchestration required by AutoGM.

## Boundaries

APM does not create a second game engine, global AutoGM role, public matchmaking authority, autonomous AI canonical mutation, release/deployment authority, paid-provider authority or canonical-promotion authority. Existing Family Safety/community boundaries remain applicable to any later public social discovery or minor-facing connected-play features.
