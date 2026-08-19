# CSW-09 — Creator Command Center and Assistance Integration

**Work item:** CSW-09  
**Program:** CSW — Creator Storycraft Workspace  
**Status:** DESIGN CONTRACT — READY FOR GOVERNED REVIEW  
**Owner and final authority:** John Brandon Turner  
**Date:** 2026-08-19

## 1. Decision

Multiversal provides a **Creator Command Center** that helps a returning creator immediately understand what they were doing, what may deserve attention, and where to continue. It is a projection and navigation layer over existing CSW/APW/owning-domain state. It is not a new source of truth, not a social-engagement feed, not a task authority engine, and not a hidden AI workspace.

The governing flow is:

`authorized owning-domain projections → context-safe ranking/grouping → creator-facing resume/attention surfaces → exact deep link or bounded command → owning-domain action`.

Authorization and visibility filtering happen **before** counts, ranking, search, similarity, related-work analysis or optional-assistance context.

## 2. Product purpose

The Command Center should answer five questions quickly:

1. **What was I working on?**
2. **What can I continue right now?**
3. **What ideas or threads might deserve attention?**
4. **Where is my reusable work being used, where I am allowed to know?**
5. **What can Multiversal help me do next without taking control away from me?**

It should feel warm, calm and useful rather than urgent, competitive or productivity-scoring.

## 3. Context model

Every Command Center item declares its context explicitly:

- Personal;
- Project;
- Campaign-linked creative work;
- Campaign-bound creator work where the subject is currently authorized;
- APW-05 Workshop/reusable library;
- APW-05 Sandbox/Lab, always visibly marked noncanonical.

The Command Center does not invent another context. A creator may have many contextual roles, but those roles remain metadata used by the owning context, not account identity.

## 4. Required primary surfaces

### 4.1 Continue Writing
Projects/documents/revisions from CSW-07 where a safe resume point exists.

Each card may include:
- document/project title;
- context indicator;
- last meaningful revision timestamp;
- branch/revision label when needed;
- short safe excerpt/summary where permitted;
- exact resume target;
- stale-reference or conflict indicator where relevant.

### 4.2 Ideas to Develop
CSW-03 Idea Inbox/fragments in captured, triaged, incubating or selected development states. The Command Center never promotes or reclassifies them automatically.

### 4.3 Open Threads
CSW-06 creator-managed OpenThreads and evidence-backed continuity candidates filtered by creator disposition and current evidence.

### 4.4 Needs Attention
A union of creator-actionable states from owning systems, such as:
- unresolved references;
- stale source/revision dependencies;
- validation failures affecting a declared use;
- CSW-06 continuity candidates not dismissed/snoozed;
- APW-05 reusable asset dependency/validation issues;
- Workshop/Sandbox save/proposal review states;
- failed/recoverable exports or imports;
- collaboration conflicts requiring creator choice.

“Needs Attention” means a workflow state, not objective creative quality.

### 4.5 Recently Created / Recently Worked On
Role-safe recent creator work across CSW and APW-05. Recency never creates authority and does not preserve a protected preview after access is lost.

### 4.6 Unused Material
Authorized creator-owned work that has no known current usage link under the available authorized projection. “Unused” is descriptive, not a negative score, and absence of an authorized Campaign link must not imply no hidden/protected usage exists.

### 4.7 Drafts
Creator-owned drafts from CSW and supported APW-05 owning-domain authoring flows. Draft validity, lifecycle and origin are shown without implying publication/canonical status.

### 4.8 Story Bible
Fast access to the creator’s current Project/Story Bible and recently referenced authorized entries. Story Bible remains CSW-02 authority.

### 4.9 Campaigns Using My Work
A privacy-filtered projection of authorized Campaign usage relationships. It shows only Campaigns/usages the current subject is allowed to know. Counts are computed after visibility filtering.

### 4.10 Workshop / Sandbox
APW-05 reusable assets, validation states, recent Workshop work and Sandbox sessions may appear, but Sandbox content is visibly labelled **Experiment / noncanonical** and never grouped as Campaign progress or reusable truth unless explicitly saved out.

## 5. Ranking without coercive engagement

The Command Center may rank within surfaces using transparent workflow relevance such as:

- explicit user pin/favorite;
- active resume token;
- unresolved creator action;
- recent meaningful edit;
- user-selected Project priority;
- due/reminder metadata only when creator-configured;
- stale conflict/recovery need;
- saved view/filter relevance.

It must not use:

- streak loss;
- “you are falling behind” messaging;
- hidden engagement scores;
- fear-of-missing-out pressure;
- arbitrary urgency merely because time passed;
- competitive creator productivity scoring;
- repeated resurfacing of dismissed/snoozed items without changed evidence.

Default ordering should favor recoverability and creator intent over engagement.

## 6. Projection-not-duplication rule

Every Command Center card stores or carries only the minimum projection metadata required to render/navigate safely. The authoritative state remains in its owning system.

A card must identify:

- source object/resource ID and current accessible version or projection token;
- owning domain/feature;
- context kind/ID where applicable;
- projection generated-at/version metadata;
- exact destination/deep-link descriptor;
- safe display fields;
- current workflow status;
- authorization/visibility basis or revalidation requirement.

The Command Center does not copy Story Bible truth, prose, Campaign state, Workshop validation truth or OpenThread state into an independent mutable record.

## 7. Return-to-context tokens

A `CreatorReturnTarget` or equivalent descriptor provides resumable navigation without becoming authority.

It includes, as applicable:

- owning feature/domain;
- Personal/Project/Campaign context;
- object/resource ID;
- exact branch/revision/span/node where meaningful;
- view/mode;
- safe selection/focus target;
- source version observed when the token was created;
- fallback destination hierarchy;
- optional transient UI state that contains no protected truth.

Opening a return target reauthorizes the subject and resolves the current object state before rendering protected content.

## 8. Deep-link recovery

When a deep link is stale, the system chooses a safe outcome:

- exact target still valid → open it;
- target version changed → open current object with “changed since last visit” context;
- target moved/renamed → resolve stable identity and open current location;
- branch/revision/span no longer current but retained → open retained historical context if authorized;
- target archived → open archive-safe detail if permitted;
- permission lost → show access-unavailable without leaking protected details;
- target deleted/tombstoned → show a safe unavailable/tombstone state;
- offline and cached projection available → show explicitly cached/read-only state as allowed;
- offline and protected/current data unavailable → fail safely with resume-later option;
- ambiguous conflict → open owning feature’s recovery flow rather than guessing.

A deep link never carries sufficient authority to bypass reauthorization.

## 9. Search and creator command palette

The Command Center defines one creator-oriented search/command entry that spans authorized CSW/APW-05 capabilities while routing every action to the owning domain.

### Search classes

- title/name/tag search;
- Project/folder/collection filters;
- creative type/lifecycle filters;
- recent/pinned/unused/open-thread/needs-review filters;
- provenance/source relationship filters;
- authorized Campaign usage filters;
- Workshop validation/origin/dependency filters.

### Command classes

Examples:

- create idea;
- continue writing;
- open Project/Story Bible;
- create from template;
- open Workshop;
- start Sandbox experiment;
- review OpenThreads/continuity candidates;
- compare source/derivative;
- prepare Campaign proposal;
- export exact revision;
- show related unused material;
- open guided workflow;
- invoke optional assistance on the current authorized selection.

The palette is a router, not a generic command authority. Before execution, the owning feature performs current authorization, validation and required confirmation.

## 10. Authorization-before-aggregation

For search, counts, recents, related-work, usage and ranking:

1. determine current subject/context;
2. build permitted resource scope;
3. apply visibility/ownership/membership/entitlement filtering;
4. only then aggregate/count/rank/search/similarity-match;
5. return role-safe projections.

This prevents leakage such as:

- “3 hidden Campaigns use this asset”;
- search-result count changes revealing a secret object;
- related-work suggestions exposing GM-only material;
- a recent card retaining a no-longer-authorized title/excerpt;
- AI context receiving protected material through a Command Center aggregate.

When exact global cardinality cannot be safely known, UI wording should describe the visible subset rather than imply completeness.

## 11. Multi-project and Campaign usage

Cross-project relationships come from CSW-02/08 provenance/reference graphs after authorization filtering.

Campaign usage may be shown only when the user can know the Campaign and usage relationship. The projection may say:

- used in Campaign X;
- proposed to Campaign X;
- Campaign variant exists;
- source changed since Campaign derivative, if the creator is authorized to know both sides.

It must not expose protected Campaign object names, hidden GM notes, participant-private material or undiscoverable usage merely to make the relationship graph complete.

## 12. “What needs you” semantics

A creator-action item must have:

- owning system;
- reason it needs explicit creator choice;
- current status;
- evidence/source links where safe;
- available actions;
- snooze/dismiss/resolve behavior where applicable;
- changed-evidence behavior;
- no automatic application of the suggested fix.

Examples include merge conflicts, stale references, continuity candidates, missing dependencies, incomplete imports, source-change review and explicit proposal decisions owned by the creator.

The Command Center is not allowed to turn advisory CSW-06 findings into mandatory correctness tasks.

## 13. Reminder/task hooks

CSW-09 defines metadata seams for future creator-chosen reminders or task integrations but does **not** implement a scheduler.

A future hook may reference:

- exact owning object/context;
- user-written reminder purpose;
- optional due date/window/cadence;
- completion/dismiss status;
- safe deep-link target;
- notification/privacy policy.

Default product behavior must not create recurring reminders, streaks or nagging without explicit user request. Reminder state never changes creative or Campaign truth.

## 14. Assistance entry points

Optional assistance can be invoked from a card, search result, document, idea, OpenThread, derivative, Workshop asset or explicit selection.

Before invocation, the UI displays or makes directly inspectable:

- **Scope:** which Project/Personal/Campaign context applies;
- **Sources:** which exact authorized objects/revisions/entries are included;
- **Task:** what the assistant is being asked to do;
- **Capabilities:** suggest, summarize, compare, transform, critique, explain, etc.;
- **Output status:** candidate/draft/advisory, never automatic truth;
- **Provider/cost policy:** where governing product configuration makes it relevant;
- **Privacy boundary:** no unrelated private content added implicitly.

The user can narrow/remove sources before sending where the product flow permits.

## 15. Assistance authority

Optional AI may:

- suggest next creative steps;
- summarize authorized Project state;
- propose ways to develop an Idea;
- explain continuity candidates;
- generate variants/transformations under CSW-03/08;
- assist with writing under CSW-07;
- compare authorized materials;
- explain Workshop validation/dependency evidence;
- surface candidate related work from already authorized projections.

It may not:

- promote an idea/draft to Story Bible/Campaign/canonical truth;
- accept a writing revision automatically;
- resolve OpenThreads/continuity dispositions by itself;
- publish/promote/incorporate material;
- use protected Campaign/GM/private sources that were not authorized into the task;
- widen permissions or change context;
- execute arbitrary palette commands outside owning-domain authority;
- schedule actions/reminders without a separate authorized scheduling feature;
- hide that its output is generated/advisory.

## 16. No-AI parity

Core organization/resume/development remains useful with AI disabled or unavailable.

Non-AI capabilities include:

- exact resume/deep links;
- Idea triage;
- deterministic inspiration tables/generators;
- guided workflows/templates;
- plot/outline/graph tools;
- deterministic continuity/open-thread checks;
- writing/version/compare tools;
- clone/remix/template/provenance tools;
- Workshop/Sandbox comparisons and validation;
- search/filter/saved views;
- deterministic related/reference graph queries;
- creator-authored reminders metadata where supported later.

AI unavailability must not make the Command Center unusable.

## 17. APW-05 Workshop integration

Workshop assets can appear in:

- Continue / recent work;
- Needs Review for validation/dependency/source-change issues;
- Your Reusable Library shortcut;
- related/derived work;
- Campaigns Using My Work when authorized.

Sandbox sessions can appear in Continue/Recent/Needs Review only with a strong **Sandbox / noncanonical experiment** label. They do not appear as Campaign progress, reusable truth or published assets until an explicit save/proposal operation creates a separate governed object.

## 18. Empty states

Useful zero-state experiences include:

- no Projects → create Project, capture Idea, open Workshop or browse entitled references;
- no recent work → show pinned/library/create actions rather than an empty “productivity” score;
- no attention items → calm “Nothing needs your decision right now” state;
- no Campaign usage → do not imply the material has never been used in hidden/unknown Campaigns;
- AI unavailable/disabled → show ordinary tools with no degraded-warning pressure.

## 19. Offline behavior

The Command Center can show cached projections only where APW/offline policy permits. Every cached card is visibly stale/read-only when current authority/state cannot be confirmed.

Offline behavior:

- does not broaden search scope;
- does not infer current Campaign usage;
- does not execute authoritative palette commands requiring connectivity;
- preserves safe draft/local actions only where their owning domain permits;
- records resume intent without claiming a target remains authorized/current;
- revalidates on reconnect.

## 20. Recovery and stale projections

Projection cards include enough version metadata to detect stale state. Opening/actioning a stale projection never silently overwrites current work.

Recovery behavior covers:

- target changed since card generated;
- object archived/deleted;
- Project moved/renamed;
- permission/entitlement changed;
- collaboration conflict;
- failed search index refresh;
- incomplete optional-assistance request;
- interrupted export/import;
- stale Workshop validation;
- Sandbox session expired/discarded.

The owning domain performs resolution; the Command Center explains and routes.

## 21. Accessibility and mobile parity

All primary surfaces and commands work without large-screen dashboards, hover, drag-and-drop, graph-only navigation or color-only state.

Required behavior:

- logical heading/landmark structure;
- keyboard/screen-reader traversal by surface and item;
- text labels for Personal/Project/Campaign/Sandbox context;
- ordered lists as alternatives to visual grids;
- accessible filter/search/command palette;
- screen-reader-readable reason/status for Needs Attention;
- textual related/usage/provenance summaries;
- mobile stacked cards and staged detail/actions;
- preserved focus/return position after completing a task;
- reduced-motion-compatible transitions;
- no information encoded only by badge color.

## 22. Product voice

The Command Center reflects Multiversal's warm, encouraging, mentor-like personality without becoming obsequious or coercive.

Prefer:

- “Pick up where you left off.”
- “A few threads may be worth another look.”
- “This source changed since you made the copy. Review the differences?”
- “Nothing needs your decision right now.”
- “This Sandbox experiment is separate from your campaign.”

Avoid:

- “You’re behind.”
- “Don’t lose your streak.”
- “Critical story flaw” for advisory continuity findings;
- pressure to enable AI;
- fake urgency based solely on inactivity.

## 23. Acceptance invariants

CSW-09 is design-complete only if:

1. every Command Center surface is a role-safe projection from an owning system;
2. authorization filtering precedes counts/search/ranking/related/usage aggregation;
3. Personal/Project/Campaign/Sandbox context is visible;
4. resume targets reauthorize before protected content/action;
5. stale/moved/deleted/lost-access deep links recover safely;
6. the creator command palette routes to owning-domain commands and cannot bypass authority;
7. Needs Attention represents creator-actionable/advisory workflow state, not objective creative scoring;
8. dismissed/snoozed advisory work does not nag without changed evidence;
9. Campaign usage never leaks protected Campaign existence/details/cardinality;
10. APW-05 Sandbox projections remain visibly noncanonical;
11. optional assistance shows source/context/task scope and outputs candidate/advisory material only;
12. core organization/resume/development has useful no-AI parity;
13. reminder/task behavior remains an explicit future integration hook, not hidden scheduler authority;
14. cached/offline projections do not broaden authority;
15. recovery routes state conflicts back to owning systems without silent overwrite;
16. mobile/accessibility/nonvisual parity is complete;
17. ranking avoids streak/FOMO/productivity-score engagement mechanics.

## 24. Downstream handoff

CSW-09 supplies creator-context/navigation/attention/search requirements to APW-06 Shell/Navigation/Notifications, creator workflow integration to CSW-10, and recovery/privacy cases to APW-07.

No application implementation, notification scheduling, publication, canonical promotion or release authority is granted by this design tranche.