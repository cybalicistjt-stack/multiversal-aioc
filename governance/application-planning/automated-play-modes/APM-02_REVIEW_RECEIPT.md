# APM-02 Review Receipt

**Work item:** APM-02 — CozyMode Core Loop  
**Attempt:** APM-02-attempt-001  
**Design branch:** `governance/apm-02-cozy-core-loop`  
**Review state:** substantive design complete; repository/PR validation pending

## Reviewed dependencies

- APM-01 automated-play authority/delegation/run lifecycle.
- APW-03 bounded Activity/Project, time, resource and owning-domain safety boundaries.
- APW-04 Personal Workspace/no-Campaign host and sandbox separation.

## Findings

1. CozyMode is setting-independent and describes low interaction pressure, not a farming/life-sim genre or hidden mechanical difficulty setting.
2. Initial scope is Cozy Solo in Personal context with one human initiator, explicit controller identity, delegation and versioned preference profile.
3. Core loop is Orient → Choose focus → Confirm bounds → Execute bounded operation → Evaluate stop → Meaningful decision → Reflect/summarize → Continue/change/pause/exit.
4. Low-pressure behavior favors self-directed goals, small clear steps, cost/stop preview, graceful pause, sparse notifications and respectful warm presentation without automatic success or rule changes.
5. Cozy preferences govern focus, pace, interrupts, budgets, presentation and optional AI, but cannot widen owning-domain legality/authority.
6. Every operation remains automatic, bounded automatic, proposal-required, human-required, GM/adjudication-required or prohibited.
7. Background progress is opt-in and activity-specific with hard step/time/resource limits and mandatory stop conditions.
8. Wall-clock time is distinct from game/activity time and cannot silently create progress.
9. Resource/crafting automation requires explicit ownership/reservation/recipe/budget and cannot auto-spend real money.
10. Irreversible Character advancement remains human-required; research cannot leak hidden truth; social automation cannot consent for humans; GM-required NPC responses cannot be replaced by AI authority.
11. Creative/journal output remains nonauthoritative and summaries distinguish committed state from generated flavor.
12. Notifications are sparse and noncoercive; CozyMode has no streak-loss engagement mechanic.
13. Save/exit/resume/recovery uses ordinary state, status lookup, current authorization and remaining budget evidence; there is no separate Cozy save universe.
14. Core loop remains fully usable without AI.
15. Stopping Cozy and entering a Campaign does not carry Personal automation authority into the Campaign.

## Gate review

- Setting-independent low-pressure definition: **PASS**
- Cozy Solo Personal host and loop explicit: **PASS**
- Preference/delegation dimensions defined: **PASS**
- Operation/stop classes defined: **PASS**
- Background opt-in/bounded/stop-safe: **PASS**
- Wall-clock/game-time/resource boundaries safe: **PASS**
- Advancement/investigation/social/crafting/creative safety: **PASS**
- Authoritative state versus generated flavor separated: **PASS**
- Sparse/noncoercive notifications: **PASS**
- Save/exit/resume/recovery deterministic: **PASS**
- No-AI fallback complete: **PASS**
- Personal→Campaign authority transfer: **NO**
- Application implementation/migration authorized: **NO**
- CCTI-12-T04 resumed: **NO**

Repository-health/PR merge evidence remains to be attached before `completed_verified` is claimed.
