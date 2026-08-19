# APM-02 — CozyMode Core Loop

**Work item:** APM-02  
**Program:** APM — Automated Play Modes  
**Version:** 0.1.0  
**Status:** DESIGN CONTRACT — READY FOR GOVERNED REVIEW  
**Owner and final authority:** John Brandon Turner  
**Date:** 2026-08-18

## 1. Decision

CozyMode is a **setting-independent, low-pressure automated-play experience** built from ordinary Multiversal resources, APW-03 Activities/Projects, explicit APM-01 delegation, and owning-domain commands.

Initial APM-02 scope is **Cozy Solo in Personal context**. It is useful whether the setting is fantasy, science fiction, superheroes, horror, historical, contemporary, surreal, or something else. “Cozy” describes pacing, interaction pressure, presentation and automation boundaries; it does not require farming, a village, crafting, romance, domestic simulation, or any particular genre.

CozyMode is not a separate rules engine. It does not make failure impossible, erase consequences, grant free resources, alter advancement rules, guarantee NPC affection, or convert wall-clock time into progress unless the selected owning rules/profile explicitly defines those mechanics.

The core loop is:

> **Orient → Choose a focus → Set/confirm bounds → Progress routine work → Stop at meaningful decisions → Reflect/summarize → Continue, change focus, pause or return to ordinary play.**

## 2. What “low-pressure” means

CozyMode lowers *interaction pressure* without falsifying game rules.

It favors:

- self-directed goals rather than urgent externally imposed objectives;
- small understandable next actions;
- explicit preview of likely costs, time and stop conditions;
- routine repetition only when the user has preauthorized it;
- graceful pausing instead of forced completion;
- clear “nothing bad happens if you stop here” boundaries where the owning activity actually permits them;
- gentle summaries rather than noisy streams of micro-events;
- optional reminders rather than punitive engagement loops;
- safe rediscovery of unfinished projects;
- presentation that is warm, calm, encouraging and respectful rather than infantilizing or falsely praising.

It does **not** mean:

- hidden difficulty reduction;
- silent rule changes;
- automatic success;
- removal of costs already required by the rules;
- coercive streaks/daily obligations;
- dark-pattern urgency;
- social consent by proxy;
- automatic irreversible progression.

A future rules profile may explicitly provide low-risk or failure-softening mechanics. CozyMode may use those mechanics when selected, but the authority remains the rules/profile, not the mode label.

## 3. Initial host and subject

Initial Cozy Solo uses:

- one human initiating subject;
- APW-04 Personal context;
- a Personal resource/activity scope the subject owns or is authorized to use;
- a registered Cozy automation controller;
- an explicit `AutomationDelegationGrant`;
- one `CozyPreferenceProfile` and version;
- ordinary owning-domain resources and Events.

Cozy Solo does not require a Campaign or a GM. Operations that inherently require Campaign GM adjudication are unavailable, simulated only in explicitly nonauthoritative sandbox form, or stop with a clear “this needs a governed Campaign/GM context” explanation.

A Personal Character is usable only when the future APW-04/A4 successor permits it. Until then, current Campaign-bound Stage A Character semantics remain unchanged.

## 4. Cozy activity palette

CozyMode does not own activity mechanics. It discovers an **eligible palette** from APW-03/owning-domain profiles and filters it through current authority, current state, user preferences and automation class.

Initial palette categories may include:

- project planning and routine project progress;
- research against authorized sources;
- journaling/reflection and creator notes;
- crafting/repair/maintenance with explicit recipes and resources;
- preparation/loadout/logistics where Personal ownership permits it;
- bounded recovery/upkeep where the rules explicitly define it;
- training/advancement preparation, never irreversible advancement itself;
- Creative Library/Story Bible work that is explicitly nonauthoritative;
- light authored exploration/opportunity discovery when a Personal/sandbox profile defines deterministic content and authority;
- relationship/contact maintenance only where the target is an authored nonhuman/system resource with deterministic permitted behavior or where the action remains a draft/proposal. Human consent is never automated.

The palette excludes operations the user cannot currently authorize or that the selected profile marks prohibited.

## 5. CozyPreferenceProfile

A Cozy run uses an explicit versioned preference profile. Preferences shape what the controller may select **within** legal eligible operations; they are not mechanics or permissions by themselves.

Minimum dimensions:

### 5.1 Focus

- chosen projects/activities;
- enabled activity families;
- excluded activity families;
- pinned goals;
- “ask me before switching focus” preference.

### 5.2 Pace

- `one-step-at-a-time`;
- `until-next-choice`;
- `bounded-batch`;
- optional `bounded-background` for eligible activities.

Pace never grants an operation class that the owning profile does not permit.

### 5.3 Interruption policy

- always stop on human-required choice;
- always stop on GM/adjudication-required state;
- stop on new cost above threshold;
- stop on new resource type or ownership/custody change;
- stop on failure/complication class selected by user/profile;
- stop on stale/conflict/recovery-required;
- stop before irreversible/destructive effect;
- stop before a new activity/project unless preapproved.

Mandatory APM-01 stop classes cannot be disabled by preference.

### 5.4 Budgets

- maximum operation/step count;
- maximum authored progress units;
- maximum Campaign/Personal activity-time units where defined;
- maximum wall-clock background window where background scheduling is separately allowed;
- per-resource quantity limits;
- resource classes that may never be auto-spent;
- in-game currency/material budget where the owning domain supports it;
- real-money/paid-credit budget is always **zero for automation** in APM-02.

### 5.5 Presentation

- summary frequency;
- detail level;
- notification policy;
- optional narrative style/tone preferences;
- accessibility/pacing preferences.

Presentation cannot alter results.

### 5.6 AI

- AI disabled/enabled by feature class;
- allowed tasks such as narration, dialogue styling, summarization or suggestion;
- provider/cost class only if separately authorized by existing AI policy;
- no-AI fallback always available for the core loop.

## 6. Cozy delegation

Starting CozyMode creates or validates an explicit APM-01 delegation restricted to:

- Personal context and exact resource selectors;
- selected Cozy profile/version;
- selected activity/project IDs or eligible scope;
- operation classes the subject may delegate;
- exact automatic-resolution classes;
- budgets and stop conditions;
- background permission if any;
- expiry/revocation;
- optional AI policy;
- visibility/provenance rules.

The controller may not add new resources, raise a budget, change an activity from human-required to automatic, enable background mode, or renew its own grant.

Changing those dimensions is a human reconfiguration that creates a new/updated governed delegation version.

## 7. Cozy operation classification

Every candidate operation is resolved through APM-01 and APW-03 classes.

### 7.1 Automatic permitted

Examples only when the owning profile says they are deterministic and safe:

- advance one already-started routine Project step with no new choice/cost beyond approved budget;
- consume a preapproved exact material quantity under an explicit recipe/reservation;
- apply a deterministic upkeep tick defined by the rules;
- save an automatic progress/checkpoint record;
- organize/update nonauthoritative journal/project bookkeeping.

### 7.2 Automatic with bounds

Examples:

- repeat an eligible routine task up to N steps;
- continue crafting until the next recipe phase or resource threshold;
- continue research until a defined decision/reveal boundary;
- perform bounded upkeep across a whitelisted set of owned resources.

Every repetition revalidates current state and remaining budget.

### 7.3 Proposal required

The controller may prepare or submit a governed proposal if the user explicitly delegated proposal submission for that class. The proposal still awaits the authorized decider.

### 7.4 Human required

Always includes APM-01 mandatory choices and, for Cozy Solo, at minimum:

- irreversible Character advancement/build selection;
- choosing a materially different project direction;
- accepting a new material cost outside the current budget;
- transferring ownership/custody/control;
- destructive deletion;
- joining/leaving/binding to a Campaign;
- accepting another human’s invitation or consent-sensitive action;
- resolving ambiguity that can materially change state;
- overriding a failure/complication by selecting among meaningful options;
- publication/canonical promotion;
- real-money spending;
- widening automation bounds.

### 7.5 GM/adjudication required

In Personal Cozy Solo this normally causes a stop or makes the activity ineligible. It cannot be converted into “AI decides as GM.”

## 8. The Cozy Solo loop

### Step 1 — Orient

Build a current authorized Personal projection:

- active/available projects;
- recently touched work;
- routine opportunities;
- blocked/stale items;
- resources/budgets relevant to selected activities;
- pending human decisions;
- safe “continue where you left off” summary.

No protected Campaign content is carried into Personal context.

### Step 2 — Choose focus

The human may:

- resume a project;
- choose a suggested eligible activity;
- start a new permitted Personal activity;
- work on creative/journal material;
- review rather than progress anything.

Suggestions are advisory. The controller cannot silently choose a new life goal/project category just because nothing is active.

### Step 3 — Confirm bounds

Before automated progress, show/confirm the relevant preference/delegation summary:

- what may happen automatically;
- what will make the system stop;
- what resources/time may be spent;
- foreground/background behavior;
- notification/summary behavior.

Previously saved profile settings may be reused if still valid, but state-changing automation still requires fresh effective delegation/authorization.

### Step 4 — Execute one bounded operation

The controller:

1. queries the owning domain for currently eligible operations;
2. filters by delegation/profile/budget;
3. selects according to deterministic profile preference or explicit user choice;
4. invokes the owning-domain command with expected version and stable operation ID;
5. records result/Event/status evidence;
6. updates remaining budgets;
7. reauthorizes before the next operation.

Optional AI may present the already-determined result; it does not decide legality or mutation.

### Step 5 — Evaluate stop/continue

After every accepted/rejected/ambiguous operation, evaluate stop conditions before another command.

If allowed, continue one step or the declared bounded batch. Otherwise enter the appropriate waiting/paused/recovery state.

### Step 6 — Meaningful decision point

Present:

- what changed;
- why automation stopped;
- currently legal choices/proposals;
- costs/risks/evidence that the owning domain can safely expose;
- option to pause/stop/change focus.

Do not manufacture urgency.

### Step 7 — Reflect/summarize

Create an authorized summary derived from committed evidence plus separately marked nonauthoritative journal/narrative material.

The summary distinguishes:

- authoritative state changes;
- consumed/remaining resources;
- completed/blocked Project tasks;
- pending choices/proposals;
- generated flavor/journal content;
- errors/recovery needs.

### Step 8 — Continue, change focus, pause or exit

A human decides whether to continue beyond the current preauthorized loop/batch when a choice is required. Exiting does not imply background permission.

## 9. Bounded background Cozy

Background execution is opt-in and **activity-specific**.

A Cozy profile may enable background progress only when:

- the owning task is classified automatic/automatic-with-bounds;
- explicit background delegation exists;
- all resource/time/step budgets are fixed;
- no real-money spend is possible;
- no human/GM choice is currently pending;
- retry/status behavior is deterministic;
- notifications/summaries are defined;
- stop conditions are registered.

### Mandatory background stop conditions

Stop before accepting any new automated command when:

- human-required choice appears;
- GM/adjudication/proposal approval is required;
- delegation expires/revokes/changes;
- permission/entitlement/resource ownership changes;
- expected version/stale conflict occurs;
- an approved budget/step/time/resource threshold is reached;
- an unapproved resource class/cost is needed;
- an irreversible/destructive operation would occur;
- consent/social boundary appears;
- activity/rules/profile version becomes incompatible;
- operation result is ambiguous and status lookup cannot prove current state;
- activity completes/cancels/fails-safe;
- profile-specific stop condition fires.

There is no indefinite “keep playing forever” switch in APM-02.

## 10. Time semantics

CozyMode inherits APW-03 time profiles.

- Wall-clock elapsed time is not game progress by default.
- A background job may run later in wall-clock time, but the amount/type of *game/activity* progress still comes from the selected authored time/profile rules.
- A “check again tomorrow” UI affordance does not itself grant 24 hours of in-world progress.
- Personal/sandbox profiles may define abstract activity units without a Campaign calendar.

## 11. Resource and economy safety

Automation may spend only resources that:

- belong to or are controlled by the subject in the relevant context;
- are explicitly in the delegation/profile allowlist;
- remain within quantity/currency/material budget;
- are consumed/reserved through the owning domain;
- are still valid at execution time.

CozyMode cannot:

- invent resources;
- infer a recipe from names;
- spend another participant’s Personal property;
- convert sandbox rewards into Campaign assets;
- bypass custody/ownership;
- double-spend after retry;
- spend real money or paid credits automatically.

## 12. Advancement safety

CozyMode may automate only routine preparation/progress explicitly classified safe by the progression domain.

It may:

- track training progress;
- summarize eligibility;
- prepare possible advancement choices;
- notify the user that a meaningful choice is available.

It may not automatically select/apply irreversible advancement. Final Character progression remains a human-required, validated, attributable progression Event unless a future owning-domain contract explicitly defines a genuinely nonchoice routine operation.

## 13. Research and investigation safety

Routine research steps may progress when authored as automatic, but:

- hidden clues/revelations remain owning-domain authority;
- progress percentage cannot leak hidden truth;
- a player hypothesis is not fact;
- a reveal/adjudication boundary pauses;
- AI cannot infer GM-only truth or declare a conclusion authoritative;
- ambiguous research results remain ambiguous if the source says so.

## 14. Relationships and social activity

CozyMode may support low-pressure social maintenance without turning people/NPCs into progress bars.

### Human participants

- no automatic consent;
- no automatic message/reply pretending to be the human unless a future explicit communication-drafting/send permission separately exists;
- no auto-accepting invitations, ownership changes or relationship commitments.

### NPC/system relationships

Automatic change is allowed only when an authored owning-domain rule deterministically permits the specific effect. If a GM/story authority must decide an NPC response, Cozy Solo pauses or treats the interaction as nonauthoritative sandbox flavor.

AI-generated NPC dialogue cannot by itself mutate relationship truth.

## 15. Crafting, repair and maintenance

CozyMode may be especially useful for routine crafting/repair, but only over APW-03/A8 safe contracts:

- explicit recipe/rule;
- exact input reservations;
- tool/facility requirements;
- time/progress rules;
- checks/quality/failure behavior;
- output authority;
- per-resource budget;
- clear stop before substitutions or new costs.

“Use whatever materials are needed” is not a valid broad delegation unless the owning domain and profile can enumerate and bound every permitted input class/quantity.

## 16. Creative and journal work

CozyMode may help maintain:

- journal/reflection;
- Creative Library organization;
- Story Bible notes;
- project summaries;
- open-question lists;
- creator reminders;
- nonauthoritative narrative flavor.

These remain creator/CSW material, not World/Campaign truth.

Optional AI may draft prose, summaries, dialogue flavor or reflection. Applied/generated content keeps provenance and its correct nonauthoritative evidence class unless a later explicit incorporation/publication operation succeeds.

## 17. Opportunity discovery

A Cozy profile may surface “something small you can do next” using:

- authored activity availability;
- project dependencies;
- currently owned resources;
- open CSW material;
- deterministic seeded tables where the profile authorizes them;
- optional AI suggestions from authorized context.

Opportunity suggestions do not create state. If a suggestion would require a new Project, resource spend or domain mutation, the normal start/approval rules apply.

## 18. Summaries and return experience

After a bounded batch/background window, the user gets an answer-first summary:

- **What changed** — authoritative committed effects with evidence links/reference IDs where useful;
- **What was spent/earned** — from owning-domain receipts;
- **What finished**;
- **What is waiting for you**;
- **Why it stopped**;
- **What could happen next** — advisory choices;
- **Journal/flavor** — clearly separated nonauthoritative narrative if enabled.

The user should not need to inspect raw automation logs to understand what happened.

## 19. Notifications

Notifications are sparse by default.

Possible classes:

- meaningful choice ready;
- background batch completed;
- budget/resource limit reached;
- activity blocked/stale/recovery-required;
- selected project completed;
- explicit user-configured reminder.

No notification is a punishment for not returning. There are no mode-owned streak-loss mechanics.

External notifications contain minimal safe Personal-context information and reauthorize on open.

## 20. Save, exit, resume and recovery

CozyMode uses APM-01 ordinary persistence and APW recovery.

### Exit

- `foreground_only`: pause safely.
- `bounded_background`: continue only under the explicit grant until a stop condition/budget.

### Resume

Revalidate:

- subject/Personal context;
- delegation/profile version;
- resource ownership/custody;
- entitlement/rules/profile versions;
- activity/project state;
- outstanding operation status;
- pending choices;
- remaining budgets.

If stale or ambiguous, stop for review; never guess/migrate silently.

### In-flight ambiguity

Use operation status before retry. No duplicate resource spend, progress, outputs or Events.

## 21. No-AI fallback

The complete core loop must function with AI disabled/unavailable.

Fallback presentation may use:

- authored activity labels/descriptions;
- deterministic templates;
- owning-domain result summaries;
- structured “changed/spent/waiting/next” cards;
- deterministic seeded flavor tables where licensed/authorized;
- manual journal entry;
- explicit user choice menus.

Optional AI enriches wording/ideas, not viability of the mode.

## 22. Transition to ordinary play

Stopping CozyMode leaves ordinary Personal state exactly where committed owning-domain Events left it.

There is no separate Cozy save universe.

The user may:

- continue manually in Personal Home;
- resume Cozy later with a new/effective delegation;
- use an explicitly governed Personal→Campaign Character/resource bridge;
- enter a Campaign through normal authorization;
- later use Connected Cozy when APM-05 and APW-06 authorize it.

No transition carries Personal automation authority into a Campaign automatically.

## 23. Minimum acceptance scenarios

1. Zero-Campaign user starts Cozy Solo on an eligible Personal Project → controller uses only explicit Personal scope.
2. User selects `until-next-choice` → routine progress proceeds, then stops before a meaningful advancement choice.
3. User sets material budget 5 units → controller cannot consume unit 6 even if recipe can continue.
4. User enables background for one crafting Project → unrelated Projects do not start automatically.
5. Background reaches recipe substitution choice → stops; no substitute material selected silently.
6. App closes without background permission → run pauses; no progress occurs from exit alone.
7. Wall-clock day passes → no game-time progress unless the authored profile explicitly maps it.
8. Permission/resource ownership changes while background run is pending → next command denied/stopped after reauthorization.
9. Research reaches hidden reveal boundary → no clue leaked; run waits/stops.
10. Relationship activity involves another human’s consent → human-required; no auto-accept/commitment.
11. NPC response requires GM adjudication → Personal Cozy cannot make itself GM; activity pauses or remains sandbox flavor.
12. Training completes → final advancement still waits for human selection/validation.
13. Duplicate network response during progress → status lookup prevents duplicate spend/progress.
14. AI narrates a deterministic crafting result → wording cannot change output/quality/resource state.
15. AI unavailable → same core Project can progress using structured/manual presentation.
16. Cozy summary distinguishes committed state from generated journal/flavor.
17. User widens resource budget → requires explicit new profile/delegation version; controller cannot self-widen.
18. User stops Cozy and enters Campaign → Personal Cozy delegation grants no Campaign authority.

## 24. Additive implementation touch points

APM-02 does not authorize implementation. Future APM-06/APW-08 handoff may include:

1. Cozy preference/profile contract;
2. APM-01 delegation profile specialization for Cozy;
3. APW-03 Activity eligible-operation enumeration/automatic classification port;
4. Personal Cozy host adapter from APW-04;
5. budget/stop-condition evaluator;
6. bounded background scheduler/run coordinator;
7. summary/provenance projection;
8. sparse notification adapter;
9. no-AI authored/template renderer;
10. optional-AI narration/suggestion adapter with filtered context;
11. domain adapters for crafting/research/upkeep/training preparation/creative-journal tasks;
12. operation-status/reconnect/revocation recovery;
13. fixtures for budget exhaustion, stale state, consent stop, hidden reveal, exit/no-background, background cap and AI failure.

## 25. Nonauthorization

APM-02 does not authorize:

- application implementation/migration;
- a farming/life-sim setting requirement;
- unlimited/open-ended background simulation;
- automatic real-money spending;
- automatic irreversible Character advancement;
- human consent by automation;
- unrestricted NPC/story authority;
- AI mechanical/GM/canonical authority;
- Personal→Campaign authority transfer;
- public matchmaking;
- release/deployment/tester access;
- CCTI-12-T04 before September 2026.

## 26. Completion gate

APM-02 is substantively complete when:

- CozyMode is setting-independent and low-pressure without hidden rule changes;
- initial Cozy Solo Personal host/loop is explicit;
- preference/delegation profile defines focus, pace, interrupts, budgets, presentation and AI policy;
- automatic/bounded/proposal/human/GM/prohibited operation behavior is explicit;
- background execution is opt-in, activity-specific and has mandatory stop conditions;
- wall-clock/game-time/resource boundaries are safe;
- advancement/investigation/social/crafting/creative safety rules are explicit;
- summaries distinguish authoritative state from generated flavor;
- notifications are sparse/noncoercive;
- save/exit/resume/recovery is deterministic/idempotent;
- core loop has no-AI fallback;
- transitions back to ordinary play preserve one state/history model;
- implementation remains additive and unactivated.

Final `completed_verified` requires exact-head AIOC repository-health and merged PR evidence.
