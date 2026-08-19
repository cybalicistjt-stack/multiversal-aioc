# APW-03 — Between-Session Campaign Activity and Bounded Downtime

**Work item:** APW-03  
**Program:** APW — Asynchronous Play & Persistent Workspace  
**Version:** 0.1.0  
**Status:** DESIGN CONTRACT — READY FOR GOVERNED REVIEW  
**Owner and final authority:** John Brandon Turner  
**Date:** 2026-08-18

## 1. Decision

Between-Session Campaign Activity is a **governed orchestration layer over existing owning domains**, not a generic game-state mutation engine and not a second Campaign ledger.

A Campaign Activity may coordinate participants, time, prerequisites, resources, proposals, progress, notifications and provenance across a bounded long-running task, but every authoritative game effect remains owned and committed by the appropriate existing domain: Character/progression, Action/result, Asset/economy/inventory, investigation, social/relationship/faction, World/Adventure, Campaign/Session or another registered owner.

APW-03 intentionally defines only an alpha-useful initial activity set. It does not attempt to solve every possible future downtime subsystem.

## 2. Campaign Activity versus neighboring concepts

### Campaign Activity

A durable Campaign-scoped orchestration record for work that may span hours/days of Campaign time, multiple asynchronous interactions, or multiple domain operations.

### Action proposal

APW-02/A6 owns a proposed Action and delayed GM decision. A Campaign Activity may create/reference one or more Action proposals, but is not itself an Action result.

### Project

The Development Bible already defines Projects as governed long-running activities with objectives, phases/tasks, prerequisites, inputs, time, assets, checks/choices, progress, complications, outputs, cancellation and provenance. APW-03 adopts this as the preferred long-running activity model rather than inventing a countdown field.

### Session Event

An accepted domain Event is authoritative game history. An Activity record may point to Events; it does not replace them.

### Reminder/task

A reminder or “to do” item is coordination/presentation. Completing a reminder cannot spend resources or change Character/Campaign state.

### Personal workspace item

APW-04 will own Personal/no-Campaign workspace behavior. APW-03 is specifically Campaign-context activity.

## 3. Bounded initial activity families

The initial design supports the following **families**, each mapped to owning-domain authority.

### 3.1 Preparation and logistics

Examples: prepare gear, choose loadout, gather permitted supplies, plan travel, assign known assets/facilities, prepare a spell/loadout/kit where rules allow.

- orchestration: APW Campaign Activity;
- inventory/ownership/custody/resource effects: A8/Asset/economy owning domains;
- Character build/loadout effects: Character/progression owning domain;
- travel progression: D28/adventure-travel or Campaign rules, not APW itself;
- approvals: APW-02 proposal/GM inbox where required.

Preparation may remain a checklist until explicit domain commands commit changes.

### 3.2 Training and advancement preparation

Examples: select possible advancement options, plan training, satisfy a time/trainer prerequisite, accumulate governed training progress when the rules profile explicitly supports it.

- progression truth remains event-based in Character/progression;
- an Activity may track preparation/progress evidence;
- the Activity cannot choose irreversible advancement for the player;
- final advancement remains an explicit validated Character/progression operation/Event;
- entitlement, prerequisites, costs, exclusions, source versions and Campaign restrictions are revalidated at final advancement.

“Training complete” never means “advancement silently applied.”

### 3.3 Research and investigation

Examples: research a source, analyze known evidence, decode, compare, interview by asynchronous proposal, surveil, reconstruct, investigate an authorized lead.

- mechanical attempts use shared Action/A6 rules when applicable;
- A9 investigation owns clues, evidence, hypotheses, revelations and conclusions;
- hidden information is filtered before activity/search/notification projection;
- player notes/hypotheses do not become objective truth;
- research completion may yield an A9 clue/result/GM prompt through the owning path; it never invents hidden answers from APW progress alone.

### 3.4 Journal, notes and reflection

Examples: Campaign journal entry, session reflection, personal note attached to a Character/Campaign object, recap drafting.

- user-authored notes are nonauthoritative overlays unless a separate owning-domain publication/reveal operation promotes selected material;
- private/party/GM visibility remains explicit;
- journal completion does not change mechanics by itself;
- if a rules profile rewards journaling, the reward is a separate governed domain effect with explicit source/provenance.

### 3.5 Relationship and social maintenance

Examples: maintain a contact, repay a favor, write to an NPC, cultivate a faction relationship, attempt reconciliation, fulfill an obligation.

- social Actions use the shared Action runtime where mechanical resolution applies;
- A9/social-relations owns relationship, reputation, obligation and faction runtime state;
- NPC canonical response is not generated merely because time elapsed;
- another human participant’s consent/intent cannot be automated;
- promises/favors/debts/attitude changes require owning-domain attributable Effects/Events or explicit GM adjudication;
- private motives/thresholds/secrets remain filtered.

### 3.6 Crafting, repair and maintenance

Examples: craft from an explicit recipe, repair an Item/Vehicle/Asset, maintain equipment, construct a bounded object where a rules profile supports it.

- recipe/rule identifies inputs, tools, facilities, knowledge, time, checks, outputs, quality and failure behavior;
- APW never infers a recipe from item names;
- A8/Asset/economy/inventory remains authority for materials, quantities, custody, condition, ownership, transfers and output objects;
- long crafting/repair uses a Project/activity; short work may remain a normal Action;
- input reservations/consumption and final outputs occur through owning-domain operations with idempotency/provenance;
- no parallel economy/value truth is created.

### 3.7 Recovery and bounded upkeep

Examples: rest/recovery, treatment follow-up, condition recovery, resource refresh, maintenance interval where rules explicitly define it.

- APW coordinates time/progress only;
- Character/resource/condition/Asset domains own actual restoration/condition changes;
- no universal rest rule is invented;
- completion requires the selected rules profile’s prerequisites and explicit owning-domain result.

## 4. Explicitly deferred breadth

APW-03 does **not** commit the alpha to:

- businesses/economic simulation as a universal subsystem;
- estate/kingdom/settlement management;
- mass production/factory scheduling;
- public marketplaces or auction systems;
- autonomous NPC life simulation;
- unrestricted real-time background simulation;
- universal travel/calendar rules;
- universal training/XP formulas;
- generic “do anything while offline” mutation;
- autonomous AI project management;
- public stranger collaboration/matchmaking;
- automatic romance/consent decisions;
- a universal crafting recipe/economy table.

These may be layered later through explicit owning-domain designs without changing APW-03’s orchestration boundary.

## 5. Resolution classes

Every Campaign Activity operation/task is classified as one of:

1. **informational** — notes/checklists/planning; no game mutation.
2. **immediate-domain-command** — an authorized owning-domain operation can resolve immediately and atomically.
3. **proposal-required** — APW-02/A6 or another governed approval path must decide before mutation.
4. **timed-project-progress** — multiple governed progress steps/events over Campaign time.
5. **human-choice-required** — cannot proceed until an authorized human makes a material choice/consent/advancement decision.
6. **gm-adjudication-required** — rules/content explicitly requires GM judgment/revelation/response.
7. **prohibited** — not allowed in this profile/context.

A single Project may contain tasks of multiple classes. Classification is owned by the rules/domain profile, not by UI labels.

## 6. CampaignActivity conceptual identity

A future additive contract may require the following orchestration identity:

- `activityId`;
- `campaignId`;
- optional `sceneId`/`sessionContextRef`;
- `activityKind` and profile/version;
- `ownerSubjectId` and participant subject/Character references;
- `owningDomain` or coordinator profile;
- objective/safe label;
- lifecycle state;
- task/phase references;
- prerequisite refs;
- required time/time-profile refs;
- location/facility refs;
- resource/Asset reservation refs;
- Action/proposal IDs;
- progress/result/Event refs;
- visibility policy;
- permission/entitlement/profile version hints;
- created/updated/provenance/correlation metadata.

The record governs orchestration and history of the activity. **Authoritative Character/Asset/investigation/social/world state remains in owning domains.**

## 7. Lifecycle

Minimum orchestration lifecycle:

1. `draft`;
2. `proposed` where approval is needed;
3. `ready`;
4. `active`;
5. `awaiting-human-choice`;
6. `awaiting-gm-adjudication`;
7. `awaiting-domain-result`;
8. `paused`;
9. `stale`;
10. `blocked`;
11. `cancelling`;
12. `cancelled`;
13. `completed`;
14. `expired` where profile permits;
15. `recovery-required`;
16. `failed-safe`.

Lifecycle state does not itself apply mechanics. A `completed` Activity means all required owning-domain completion evidence is present, not merely that a countdown reached zero.

## 8. Time model

APW-03 does not impose one universal calendar.

A Campaign/rules profile may use:

- **none/untimed** — ordering only;
- **abstract blocks** — downtime turns, watches, shifts, days or other authored units;
- **calendar time** — governed Campaign date/time;
- **task-specific duration** — explicit authored duration without a global calendar.

Wall-clock time and Campaign time are separate. “24 real hours passed” never advances a Project unless a separately governed profile explicitly maps real time to Campaign progress.

### Time reservation

When rules require exclusive Character/facility/Asset availability, the owning scheduling/project contract must prevent double-spending overlapping committed use unless concurrency is explicitly permitted.

## 9. Resource, Asset and facility reservation

Activities may reference reservations but cannot create inventory/economy truth.

Reservation semantics must specify:

- reserving subject/activity;
- exact Asset/resource and version;
- quantity/unit when applicable;
- custody/access/ownership authority;
- start/end or task scope;
- whether reservation prevents other use;
- consume-on-start, consume-on-progress, consume-on-complete, release-on-cancel semantics;
- status/idempotency/provenance.

The owning Asset/economy domain validates and commits the reservation/consumption. Failed/repeated commands cannot duplicate items/resources.

## 10. Progress model

Projects are durable aggregates, not one countdown field.

Progress may consist of:

- completed tasks/phases;
- accumulated authored progress units;
- Action/result references;
- spent Campaign time;
- consumed/reserved inputs;
- complications;
- participant/facility changes;
- GM adjustments with reason/provenance;
- outputs already committed by owning domains.

Each progress mutation uses stable operation identity and expected versions. Ambiguous failures use status lookup before retry.

## 11. Pause, resume, cancellation and transfer

### Pause

Stops acceptance of new automatic/project progress after a deterministic barrier. Committed Events remain.

### Resume

Revalidates current Campaign lifecycle, participants, permissions, entitlement, rules/profile versions, resources/reservations, facilities and stale dependencies.

### Cancel/abandon

Uses the activity/profile cancellation rules. Already committed costs/effects remain unless owning-domain compensation/refund rules explicitly apply. Unconsumed reservations are released through owning-domain operations.

### Participant change/transfer

Does not transfer Character/resource ownership automatically. The activity updates authorized participants and owning domains revalidate access/use rights.

## 12. Advancement safety boundary

APW-03 may support:

- browse/plan advancement;
- save a proposed advancement plan;
- track authored training prerequisites/progress;
- notify when a Character appears eligible under current projection;
- submit final advancement proposal where rules require approval.

APW-03 may **not**:

- choose irreversible advancement for a human automatically;
- infer a legal advancement from points/time alone without full validation;
- bypass free/subscription entitlement restrictions;
- mutate immutable progression history;
- silently replace unavailable source content;
- auto-respec without governing rule/GM authority.

Final advancement remains an immutable Character/progression Event with before state, selected option, cost, grants, prerequisites, rules/source and resulting state.

## 13. Investigation safety boundary

Research/investigation Activities preserve:

- clue provenance;
- acquisition conditions;
- reliability/ambiguity where authored;
- role-safe visibility;
- distinction between clue/evidence, interpretation, rumor, deception, player note, hypothesis and conclusion.

Automatic links remain suggestions unless data defines the relation. AI cannot use GM-only data for a player or declare a hypothesis true. Activity progress cannot reveal a clue solely because a bar filled; the A9/Action/GM path supplies the result.

## 14. Social and consent safety boundary

Relationship work is not a universal “relationship meter grind.”

- different systems may use promises, favors, obligations, reputation, attitudes, faction standing or custom rules;
- relationship/faction change remains attributable owning-domain state;
- one participant cannot consent for another;
- NPC responses requiring GM adjudication pause for GM input;
- private motives and thresholds are not surfaced through progress percentages;
- repeated background actions cannot coerce a guaranteed response unless the authored rules explicitly define deterministic behavior and authority permits it.

## 15. Journal and creator-note boundary

Campaign journal entries, notes and reflections are author-authored records. Their existence is not Campaign canon/mechanical truth.

A GM may explicitly publish/share selected notes where the governing collaboration feature permits it. If a note later becomes World/Adventure/Campaign content, that uses the explicit D29/A10 incorporation/provenance path, not Activity completion.

## 16. Notifications and waiting work

APW-03 reuses APW-02 notification principles. Useful attention states include:

- activity ready to start;
- waiting for player choice;
- waiting for GM approval/adjudication;
- task complete / next task available;
- required resource/facility unavailable;
- activity stale after rules/state change;
- activity paused/cancelled/completed;
- bounded background progress summary where a later authorized profile permits it.

External notifications remain minimal and reauthorize on open.

## 17. Offline and recovery

Offline/local work may include notes and safe draft planning under existing cache policy. Authoritative progress, resource reservation/consumption, social/investigation results and advancement commits require owning-domain connectivity unless a later explicitly proven queued-command path exists.

Recovery uses:

- stable activity/task operation IDs;
- expected versions;
- operation status lookup after ambiguity;
- Event/progress reference reconciliation;
- current permission/entitlement/profile revalidation;
- reservation reconciliation;
- no blind duplicate progress/respend;
- safe stale state instead of guessed migration.

## 18. APM/CozyMode handoff boundary

APW-03 intentionally supplies APM-02 with safe primitives but does not activate Cozy automation.

A later CozyMode profile may mark selected routine tasks `automatic_permitted` or `automatic_with_bounds` under APM-01, but:

- owning domains still commit effects;
- background progress is explicit/bounded;
- mandatory human/GM choices pause progress;
- resource budgets/time bounds are explicit;
- social consent and irreversible advancement remain human-required;
- AI remains presentation/proposal assistance.

## 19. Minimum acceptance scenarios

1. Player creates a Campaign research Project → no clue/truth change until governed research result commits.
2. Long crafting Project reserves exact materials → duplicate/retry cannot double-reserve or double-consume.
3. Crafting is cancelled halfway → committed costs remain according to recipe/profile; unused reservations release explicitly.
4. Player completes authored training prerequisite → Character does not auto-advance; final advancement remains explicit.
5. Player saves an advancement plan then entitlement/rules change → final advancement revalidates and may become stale/blocked.
6. Player journals privately → GM/other players cannot discover content/count unless authorized.
7. Player attempts relationship maintenance with an NPC requiring GM response → activity pauses for GM adjudication; no automatic attitude increase.
8. Activity references another human’s consent → human-required state; no automated acceptance.
9. Investigation progress reaches authored threshold but hidden clue requires GM reveal → activity waits; clue is not leaked by progress UI.
10. Character/facility is committed to overlapping exclusive Projects → second conflicting reservation denied unless rules permit concurrency.
11. Campaign profile uses abstract downtime blocks → no assumption of Gregorian/calendar time.
12. Client offline overnight → wall-clock time does not advance Campaign activity unless explicit profile says so.
13. Progress command response lost → status lookup returns prior outcome; no duplicate progress/cost.
14. Project resumes after rules/profile change → stale dependencies revalidate before further progress.
15. AI unavailable → all core Project/proposal/manual progress behavior remains usable.

## 20. Additive implementation touch points

APW-03 does not authorize implementation. Future handoff may require:

1. bounded Campaign Activity/Project orchestration contract and durable aggregate;
2. task/resolution-class profile contract;
3. Campaign-time/time-profile abstraction without universal calendar assumptions;
4. Asset/economy reservation adapter;
5. Action/APW-02 proposal/result links;
6. progression-abilities preparation/final-advancement adapter;
7. A9 investigation adapter;
8. A9 social/relationship/faction adapter;
9. A8 crafting/repair/Asset adapter;
10. journal/note safe storage/projection seam;
11. notification/waiting-work projections;
12. recovery/status/idempotency/reservation reconciliation fixtures;
13. APM-02 routine-automation classification seam.

## 21. Nonauthorization

APW-03 does not authorize:

- application implementation/migration;
- a universal downtime formula;
- generic cross-domain mutation authority;
- automatic Character advancement;
- automatic social consent/NPC canonical response;
- parallel Asset/economy truth;
- universal real-time background simulation;
- autonomous AI project management;
- release/deployment/tester access;
- CCTI-12-T04 before September 2026.

## 22. Completion gate

APW-03 is substantively complete when:

- Campaign Activity is distinct from Action/Event/reminder/Personal work;
- initial alpha-useful activity families and deferred breadth are explicit;
- every family maps to owning-domain authority;
- resolution classes and lifecycle are defined;
- Campaign time avoids universal calendar/wall-clock assumptions;
- resource/facility reservation prevents parallel ownership/economy truth;
- advancement/investigation/social/crafting safety boundaries are explicit;
- progress/pause/resume/cancel/recovery are idempotent and attributable;
- APM-02 receives safe routine-automation seams without automation authority;
- implementation remains additive and unactivated.

Final `completed_verified` requires exact-head AIOC repository-health and merged PR evidence.
