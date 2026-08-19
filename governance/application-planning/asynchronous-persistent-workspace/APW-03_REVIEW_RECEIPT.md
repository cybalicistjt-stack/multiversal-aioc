# APW-03 Review Receipt

**Work item:** APW-03 — Between-Session Campaign Activity and Bounded Downtime  
**Attempt:** APW-03-attempt-001  
**Design branch:** `governance/apw-03-bounded-campaign-activity`  
**Review state:** substantive design complete; repository/PR validation pending

## Reviewed source contracts

- APW-01 contextual authority and APW-02 asynchronous proposal/recovery contract.
- Development Bible Downtime and Projects.
- Characters and Progression.
- Crafting and Economy.
- Investigation.
- Social Play.
- APM-01 automated-play authority boundary.

## Findings

1. Campaign Activity can be a bounded orchestration/project layer while all authoritative effects remain with existing owning domains.
2. Initial alpha-useful families are preparation/logistics, training/advancement preparation, research/investigation, journal/notes, relationship/social maintenance, crafting/repair/maintenance and recovery/upkeep.
3. Unlimited economy/business/kingdom simulation, autonomous NPC life, unrestricted background simulation and other broad future systems remain explicitly deferred.
4. Each task is classified informational, immediate-domain-command, proposal-required, timed-project-progress, human-choice-required, GM-adjudication-required or prohibited.
5. Projects are durable aggregates with tasks/phases/progress/complications/evidence, not a single countdown field.
6. Campaign time supports untimed, abstract-block, calendar and task-duration profiles; real elapsed time never advances Campaign state without an explicit profile.
7. Resource/Asset/facility reservations remain owned by Asset/economy and must prevent unauthorized double-spend/concurrency.
8. Training/project completion cannot silently apply Character advancement; final advancement remains a validated progression Event.
9. Research progress cannot reveal hidden clues or promote hypotheses to fact outside A9/Action/GM authority.
10. Relationship progress cannot automate another human’s consent or an NPC canonical response where GM adjudication is required.
11. Crafting/repair requires explicit recipes/rules and A8 ownership/quantity/condition authority; APW creates no parallel economy truth.
12. Pause/resume/cancel/recovery preserve committed Events and use current authorization/version/reservation evidence.
13. APW-03 hands APM-02 safe routine/task/time/budget/stop-condition primitives without granting automation authority.
14. Core functionality remains usable without AI.

## Gate review

- Campaign Activity distinct from Action/Event/reminder/Personal work: **PASS**
- Initial families and deferred breadth explicit: **PASS**
- Owning-domain authority mapped: **PASS**
- Resolution classes/lifecycle defined: **PASS**
- Campaign time avoids universal wall-clock/calendar assumptions: **PASS**
- Resource/facility reservation boundary defined: **PASS**
- Advancement/investigation/social/crafting safety boundaries: **PASS**
- Pause/resume/cancel/recovery attributable and idempotent: **PASS**
- APM-02 safe handoff without automation authority: **PASS**
- Application implementation/migration authorized: **NO**
- Generic mutation engine authorized: **NO**
- CCTI-12-T04 resumed: **NO**

Repository-health/PR merge evidence remains to be attached before `completed_verified` is claimed.
