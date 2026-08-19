# CSW-04 — Guided Creation Workflows

**Work item:** CSW-04  
**Program:** CSW — Creator Storycraft Workspace  
**Version:** 0.1.0  
**Status:** DESIGN CONTRACT — READY FOR GOVERNED REVIEW  
**Owner and final authority:** John Brandon Turner  
**Date:** 2026-08-19

## 1. Decision

CSW-04 defines an **optional guided-creation framework** for common creator tasks. It helps a creator move from an empty page or loose idea toward a coherent, usable **pre-authoritative draft** without forcing one creative method, one genre, one sequence, one answer, or one UI wizard.

The controlling product rule is:

> **Guidance is scaffolding, not authority. The creator may skip it, reshape it, leave it, branch it, or work freeform at any time.**

Guided workflows reuse:

- CSW-01 Creative Fragments for durable creative content and provenance;
- CSW-02 Creative Library, Creator Project, Story Bible and Project Memory for organization and authorized context;
- CSW-03 Idea Inbox and Inspiration Engine for deterministic and optional-AI candidate generation.

CSW-04 does **not** create a parallel authoring database, a universal truth form, a mandatory wizard, or a route around the owning World, Adventure, Character, Campaign, investigation, relationship, encounter, publication or other domain.

A workflow can help prepare material for later incorporation, but the workflow itself cannot make that material authoritative.

## 2. Product outcome

A novice creator should be able to choose a task such as “Create an NPC,” “Build a mystery,” or “Plan a campaign premise” and receive enough structure to produce a useful draft without already knowing every Multiversal concept.

An experienced creator should be able to:

- open the same task and jump directly to any relevant section;
- skip questions that do not matter;
- reorder independent steps;
- replace guided answers with freeform writing;
- use an existing fragment or Story Bible reference instead of answering again;
- branch into alternatives;
- invoke CSW-03 inspiration only where useful;
- save a personal template/preset;
- pause and resume later;
- abandon the workflow without losing explicitly saved creative work;
- use the same underlying capabilities without opening guided mode at all.

The framework therefore optimizes for **helpful structure with a permanently visible escape hatch**.

## 3. Authority boundary

### 3.1 Workflow state is orchestration state

A guided workflow may persist bounded orchestration metadata such as:

- workflow/run identity;
- definition/version used;
- current/visited/skipped steps;
- explicit branch choices;
- creator progress markers;
- references to saved Creative Fragments and governed objects;
- template/preset references;
- timestamps, provenance and recovery metadata.

This state answers “where was I in the guidance?” It does not become a new source of World, Adventure, Campaign, Character or other truth.

### 3.2 Creative answers remain CSW material

When a creator chooses to durably save creative content from a guided step, that content is stored as or linked to CSW-01 Creative Fragments, creator annotations, project notes or other already-governed CSW content forms.

The workflow may hold an ephemeral/local answer draft before save, but it must not create a second long-lived content store that silently diverges from the Creative Library.

### 3.3 Governed references remain references

When a workflow uses existing Story Bible or governed-domain material, it stores a stable authorized reference/version where needed. It does not copy authoritative payload merely to simplify the wizard.

### 3.4 Completion is not approval

`workflow-complete` means only that the creator considers the guided exercise complete enough for their purpose.

It does not mean:

- published;
- canonical;
- mechanically valid;
- Campaign-approved;
- GM-approved;
- balanced;
- runtime-ready;
- incorporated into an owning domain.

Any owning-domain conversion remains an explicit later command/proposal/review/publication path.

## 4. Reusable workflow model

CSW-04 defines reusable conceptual objects rather than hard-coded page sequences.

### 4.1 GuidedWorkflowDefinition

Conceptual fields:

- `workflowDefinitionId`;
- `workflowDefinitionVersion`;
- owner/source (`multiversal-core`, creator-owned, later approved shared source);
- task family;
- name and plain-language purpose;
- supported contexts;
- ordered baseline sections;
- step definitions;
- dependency graph;
- optional branch rules;
- suggested fragment kinds/output roles;
- completion summary rules;
- optional incorporation-handoff hints;
- accessibility/nonvisual metadata;
- provenance and created/updated timestamps.

A definition describes guidance. It does not contain privileged code, arbitrary executable logic, hidden authority or unrestricted queries.

### 4.2 GuidedWorkflowRun

Conceptual fields:

- `workflowRunId`;
- definition ID/version;
- creator subject;
- Personal or authorized Campaign creative context;
- optional Creator Project;
- optional seed fragment(s);
- lifecycle;
- current/visited/skipped step references;
- creator-selected ordering overrides where allowed;
- branch/alternate run relationships;
- references to saved answer fragments/annotations;
- selected Story Bible/governed references;
- explicit InspirationRequest/candidate dispositions where retained;
- local/offline recovery metadata;
- optimistic concurrency/version;
- created/updated/completed/abandoned timestamps.

### 4.3 Definition versus run

Changing a reusable workflow definition later never silently rewrites an existing run. A run records the definition version it began with.

A creator may explicitly:

- continue on the pinned version;
- migrate to a newer definition after reviewing differences;
- clone/restart from the newer definition;
- remain entirely freeform.

## 5. Step primitive library

A small primitive set should support many workflows without forcing each creator task into bespoke UI.

### 5.1 `prompt`

Plain-language guidance, examples or framing. No answer required.

### 5.2 `short-answer`

One concise freeform response. May be saved into an existing/new fragment only on explicit save.

### 5.3 `long-answer`

Longform freeform response for premise, description, history, motivation, etc.

### 5.4 `single-choice`

Creator chooses one option from a bounded list or enters their own. Options are prompts, never classifications of truth unless separately governed.

### 5.5 `multi-choice`

Creator selects zero or more suggestions and/or adds their own.

### 5.6 `reference-picker`

Select authorized Creative Fragments, Story Bible entries or governed references. Authorization filtering occurs before search/count/ranking.

### 5.7 `inspiration-action`

Invoke a declared CSW-03 deterministic generator or optional-AI candidate action. Results remain ephemeral until explicitly saved/applied/branched.

### 5.8 `relationship-builder`

Suggest or explicitly create CSW creative relationships among selected fragments. It cannot create owning-domain relationships/runtime state.

### 5.9 `checklist`

Creator-facing considerations. Items may be checked, skipped, marked not applicable or intentionally unresolved. Checklist completion is not an authority gate.

### 5.10 `review-summary`

Show what the creator has saved/linked/left unresolved and provide explicit next actions.

### 5.11 `branch-choice`

Choose among optional workflow paths, including “none / stay freeform.” A branch changes guidance, not truth.

### 5.12 `freeform-section`

An open writing area with no required questions. This is a first-class step, not a fallback error mode.

### 5.13 `handoff-preview`

Explain what explicit later incorporation or specialized tool could consume the current material. It never performs authority escalation automatically.

## 6. Step contract

Each step definition should declare only what is needed for safe, comprehensible guidance:

- stable step ID within definition/version;
- label and purpose;
- primitive type;
- optional/required-for-workflow-summary status;
- prerequisites where genuinely necessary;
- reordering group/constraints;
- suggested output fragment kind(s);
- allowed answer bindings;
- context/reference scopes it may request;
- deterministic Inspiration action(s) it may offer;
- optional AI action(s) it may offer;
- branch rules if any;
- accessibility label/help;
- explicit validation type if present;
- creator-facing “why am I being asked this?” explanation where useful.

A step may never declare itself “required” merely to lock the creator inside a wizard. `required-for-workflow-summary` only means the summary will identify it as unresolved unless the creator marks it intentionally skipped/not-applicable.

## 7. Workflow lifecycle

Canonical run lifecycle:

1. **not-started** — definition selected but no durable progress yet.
2. **in-progress** — creator has begun.
3. **paused** — intentionally paused with recoverable state.
4. **branched** — parent run has one or more explicit alternate runs; parent may remain active or paused.
5. **completed-by-creator** — creator ended guidance and requested a completion summary.
6. **abandoned** — creator ended the run without treating it as completed; saved fragments remain independently durable.
7. **archived** — run removed from active resume surfaces but retained for history where authorized.
8. **tombstoned** — run content/progress removed under governed deletion while minimal reference integrity remains.

No lifecycle state grants target-domain authority.

## 8. Creator control: skip, revisit, reorder, pause, branch, leave

The framework must assume creative work is nonlinear.

### Skip

Any nonessential step can be skipped. A creator may also explicitly mark a normally useful step `not-applicable` or `intentionally-unresolved`.

### Revisit

Answered steps remain revisitable. Revisiting can edit the existing saved fragment, create a revision, or branch an alternative according to the creator's explicit choice.

### Reorder

Steps with no declared dependency can be reordered. The interface must distinguish:

- baseline suggested order;
- dependency-constrained order;
- creator-custom order.

A reorder does not rewrite saved content.

### Pause/resume

The run saves a recoverable progress projection. Resume must return to the actual selected context and reauthorize protected references before displaying them.

### Branch

A creator may branch the whole run or a selected section to explore an alternate direction. Branches retain source run/definition/provenance but have independent future edits.

### Abandon

Abandoning guidance never deletes Creative Fragments already saved explicitly. Unsaved ephemeral answers are discarded only after clear confirmation/recovery rules.

### Freeform escape

Every guided workflow provides a visible route to:

- open the underlying project/fragment in freeform editing;
- save current material and leave guidance;
- continue the same creative task without the workflow UI.

The system must not make guided mode a prerequisite for creating equivalent CSW content.

## 9. Progress model

Progress is informative, not coercive.

The UI may show:

- steps visited;
- saved answers;
- unresolved suggested areas;
- intentionally skipped/not-applicable steps;
- branch count;
- summary readiness.

It must not:

- imply a story is “80% good” because 80% of prompts are answered;
- hide the finish action until every prompt is answered;
- penalize skips;
- create streak pressure or failure messaging;
- present one workflow path as the only correct creative process.

A creator may finish with unresolved questions and the summary should preserve that intentionally.

## 10. Universal workflow phases

Task families may differ, but a reusable baseline phase vocabulary reduces duplication:

1. **Intent & seed** — what are we making and what existing material should anchor it?
2. **Core anchors** — identity, purpose, desire/function/problem, tone or constraints.
3. **Development** — deepen motivations, relationships, details, complications and contrasts.
4. **Connections** — link to existing Story Bible/Creative Library material.
5. **Pressure / questions** — surface conflict, costs, uncertainty, missing pieces or alternatives.
6. **Review** — show the current draft, unresolved choices and contradictions/candidates.
7. **Next use** — save, branch, continue freeform, pass into another creator tool, or later explicitly incorporate.

These phases are suggestions, not mandatory form sections.

## 11. Initial bounded workflow families

CSW-04 defines nine initial families. They are **creator-task blueprints**, not authoritative schemas for the target domains.

### 11.1 Backstory creator

Goal: develop a coherent Character/NPC history candidate.

Suggested areas:

- present identity/context;
- formative events;
- important relationships;
- wants/fears/obligations;
- unresolved history;
- secrets/rumors/contradictions;
- why the past matters now;
- hooks for future play/use.

Outputs default to `backstory-element`, `character-motivation`, `relationship`-related creative references, hooks/questions and freeform notes. Actual Character facts require Character-domain incorporation.

### 11.2 NPC / antagonist creator

Goal: create a playable/useful NPC concept without requiring a full stat block.

Suggested areas:

- role/function;
- memorable surface trait;
- desire/need;
- method/resources;
- fear/vulnerability;
- relationships/faction ties;
- secret/complication;
- how they react under pressure;
- possible introduction/use.

An antagonist path may emphasize opposition, leverage, escalation and sympathetic/contradictory dimensions. It is not required to define villainy or combat mechanics.

### 11.3 Faction creator

Suggested areas:

- purpose/identity;
- members/constituency;
- goals;
- methods;
- assets/influence as descriptive concepts only;
- internal tensions;
- allies/rivals;
- public face/private concerns;
- current pressure;
- hooks and consequences.

Runtime reputation/faction state remains owned elsewhere.

### 11.4 Settlement / location creator

Suggested areas:

- function and first impression;
- physical/social character;
- important places/actors;
- resources/opportunities;
- danger/tension;
- history/lore candidates;
- connections/routes;
- secrets/rumors;
- reasons to arrive/stay/leave/return.

World/Location truth remains D18/owning-domain authority.

### 11.5 World / culture creator

Suggested areas:

- premise/distinguishing idea;
- environment/material conditions;
- values/norms;
- institutions/power;
- economy/livelihood at creator-description level;
- belief/myth;
- conflict/change;
- language/terminology/style notes;
- internal diversity and exceptions;
- relationships with other places/cultures;
- playable hooks.

The workflow must avoid presenting a culture as monolithic by default and should encourage internal variation without enforcing one sociological doctrine.

### 11.6 Mystery creator

Suggested areas:

- motivating question;
- possible underlying truth candidates;
- affected actors;
- clues/evidence candidates;
- misleading interpretations/red herrings as explicitly authored possibilities;
- revelation sequence options;
- consequences of discovery/failure/delay;
- alternative explanations;
- unresolved coverage questions.

CSW material remains pre-authoritative. Actual investigation clues/hypotheses/runtime conclusions are governed by A9 and later owning tools. A workflow must never label a creator hypothesis as objective truth merely because it is the designer's preferred answer.

### 11.7 Adventure / quest creator

Suggested areas:

- premise/hook;
- stakes and reasons to engage;
- actors/factions;
- locations;
- obstacles/conflicts;
- discoveries/revelations;
- meaningful choices;
- consequences;
- optional content;
- alternate approaches/failure states;
- possible climax/resolution;
- loose ends/future hooks.

CSW-05 later owns serious nonlinear plot/adventure structure. CSW-04 provides guided seed-to-draft scaffolding and must not preempt CSW-05's graph/beat/agency analysis.

### 11.8 Encounter creator

Suggested areas:

- purpose in play;
- context/location;
- participants;
- desired pressure/tone;
- objectives other than “win combat”;
- environmental/social/tactical features as creative candidates;
- escalation/de-escalation;
- consequences and exits;
- accessibility/safety/complexity notes where appropriate;
- possible noncombat alternatives.

This workflow does not calculate authoritative balance, statistics, rewards or mechanics unless a future owning encounter tool provides an explicit governed handoff.

### 11.9 Campaign premise / arc creator

Suggested areas:

- campaign promise/premise;
- player-facing appeal;
- themes/tone;
- setting anchors;
- major pressures/actors;
- campaign questions;
- possible arcs rather than fixed outcomes;
- recurring locations/NPCs/factions;
- escalation possibilities;
- open space for player-driven change;
- boundaries/constraints;
- first-session/first-hook candidates.

A campaign workflow creates planning fragments and project context, not Campaign runtime truth or participant consent.

## 12. Family blueprint contract

Each family definition should declare:

- purpose;
- suggested phases;
- step list;
- optional branch modules;
- suggested Creative Fragment kinds;
- allowed reference types;
- deterministic Inspiration actions;
- optional AI actions;
- review questions;
- next-tool/handoff suggestions;
- explicit authority boundary.

A family must not require every creator to answer every field. Family definitions should prefer “useful prompts” over “schema completeness.”

## 13. Context-aware guidance from Project Memory and Story Bible

Guidance may become more useful when it can see authorized project context.

Examples:

- NPC workflow suggests existing factions the creator may want to connect;
- location workflow offers existing terminology/themes;
- mystery workflow offers currently unused creator fragments as possible clue seeds;
- adventure workflow offers existing locations/hooks/actors;
- Campaign premise workflow offers creator-selected World references.

Rules:

1. authorization filtering happens before search, counts, autocomplete, similarity or AI context;
2. the creator controls which references are actually inserted/linked;
3. a suggestion that “this may relate to X” remains advisory;
4. Story Bible creator notes and governed facts remain visibly distinct;
5. inaccessible material cannot affect suggestion counts/ranking or reveal that it exists;
6. revoked references become unavailable rather than copied into workflow answers;
7. an existing governed fact is never silently transformed into editable CSW truth.

## 14. CSW-03 Inspiration integration

Any step may offer bounded Inspiration actions appropriate to its task, for example:

- “give me three motives”;
- “invert this assumption”;
- “show contrasting versions”;
- “connect this NPC to two selected factions”;
- “what is missing?”;
- “combine these two ideas”;
- seeded table draws;
- question ladders.

The CSW-03 contract remains controlling:

- candidates are ephemeral by default;
- source fragments are not overwritten;
- creator explicitly saves/applies/branches;
- deterministic generator/version/input/seed provenance is retained where applicable;
- optional AI is candidate-only and separately authorized;
- development loops are bounded.

A workflow may remember that an Inspiration candidate was accepted/rejected/branched, but cannot elevate it to truth.

## 15. Freeform and guided editing are peers

Guided workflows are an alternate interaction projection over the same creator material, not a separate content mode.

A creator may:

- begin freeform, then open a guided workflow using selected fragments as seed;
- begin guided, then continue freeform;
- answer one guided section entirely through linked existing fragments;
- use freeform content to satisfy a suggested step;
- run multiple workflows against the same project without duplicating content automatically.

The UI must avoid language like “Convert to advanced mode” that implies freeform is expert-only or guidance is beginner-only. Both are legitimate creative styles.

## 16. Reusable creator-owned templates and presets

Creators may save reusable workflow variants.

### 16.1 Preset

A **preset** stores creator preferences over an existing definition, such as:

- hidden optional sections;
- preferred order for reorderable steps;
- default generator choices;
- default output fragment kinds;
- preferred Story Bible sections/references to offer;
- presentation density/help level.

### 16.2 Template/fork

A **creator-owned workflow template** may clone an allowed core definition and edit/add/remove bounded step primitives.

Template fields include:

- stable template ID/version;
- creator owner;
- source definition/version if derived;
- Personal/Campaign context/visibility;
- step definitions using the approved primitive library;
- provenance;
- created/updated timestamps.

### 16.3 Template safety

Templates may not contain:

- arbitrary executable code;
- unrestricted data queries;
- hidden privilege changes;
- automatic publishing/incorporation;
- external network calls outside separately governed integrations;
- bypasses for authorization, AI consent, cost or retention policy.

A creator template is private/creator-owned by default. Later sharing/marketplace/publication is separate future authority.

### 16.4 Template version behavior

Existing runs pin the template version used. Updating a template does not rewrite prior runs. A run may explicitly adopt a newer version after showing material step/branch changes.

## 17. Optional AI at individual steps

Optional AI may assist with bounded creator requests such as:

- propose alternate answers;
- ask useful follow-up questions;
- summarize selected saved material;
- rephrase a creator-authored answer;
- generate a few candidate names/hooks/complications;
- compare selected alternatives;
- identify possible missing considerations;
- help transform a freeform paragraph into suggested CSW fragments.

AI may not:

- decide the creator's answer silently;
- mark steps complete automatically based on generated text;
- auto-save generated content;
- reorder the workflow without explicit user action;
- access hidden project/Campaign context;
- create owning-domain truth;
- publish or incorporate;
- trap the creator in an AI-dependent workflow.

Every workflow remains fully usable without AI through manual answers, deterministic tools and creator-selected references.

## 18. “Coherent usable draft” validation

CSW-04 may provide creator-facing readiness checks, but these are advisory and task-relative.

Examples:

- “You have a goal and an opposing pressure, but no reason this matters now.”
- “This mystery has a proposed answer but no clue candidates yet.”
- “This NPC has a motive but no connection to the current project.”
- “You intentionally skipped history.”

Readiness checks must distinguish:

- missing suggested area;
- intentionally skipped;
- not applicable;
- creator-marked unresolved;
- potential inconsistency candidate;
- owning-domain validation not yet run.

They must not output a universal quality score or claim objective correctness.

## 19. Saving, revisions and conflicts

A workflow action that edits a saved fragment follows CSW-01 optimistic concurrency/version rules.

If the referenced fragment changed elsewhere:

- do not silently overwrite;
- show the newer version and the creator's pending answer where practical;
- allow explicit merge/edit, discard, or branch;
- preserve provenance.

Multiple workflow runs may reference the same fragment. Completing or abandoning one run does not mutate the others.

## 20. Pause, offline and recovery

### 20.1 Online durable state

A workflow run may durably save its progress projection and references when authorized.

### 20.2 Offline Personal draft guidance

Under existing cache/recovery policy, offline mode may retain:

- local workflow run draft ID;
- pinned workflow definition/version already available locally;
- local navigation/progress state;
- local unsynced answer drafts;
- references only to already-authorized locally cached safe material;
- local provenance/timestamps.

### 20.3 Offline Campaign restrictions

Offline mode cannot newly establish Campaign authority, fetch hidden references, perform owning-domain incorporation, or assume previous membership remains valid.

### 20.4 Reconnect

Reconnect must:

1. authenticate;
2. reauthorize Personal/Campaign context;
3. resolve current workflow/template version policy;
4. reauthorize referenced Story Bible/governed items;
5. reconcile saved answer operations idempotently;
6. surface fragment version conflicts;
7. preserve unresolved local drafts until explicit resolution;
8. avoid duplicate fragment creation.

## 21. Accessibility, mobile and nonvisual parity

Guided creation must not depend on cards connected by lines, drag-only reordering or visual progress bars.

Requirements:

- every workflow has a linear semantic outline representation;
- branch choices expose text labels, consequences and return paths;
- progress is announced as meaningful text such as “5 answered, 2 skipped, 3 remaining suggestions,” not only percentage/color;
- keyboard users can navigate sections, skip, revisit, reorder where allowed and open reference/inspiration controls;
- reordering has button/command alternatives to drag;
- screen readers receive step purpose, optionality, saved/unsaved state and validation messages;
- touch targets and compact mobile layouts preserve the same operations;
- mobile can answer one prompt at a time without losing a project/workflow overview;
- reduced-motion settings apply to transitions/branch visualization;
- errors focus the relevant step and explain recovery;
- branch trees have outline/list alternatives;
- destructive abandon/tombstone actions are separated from ordinary navigation;
- autosave/recovery state is conveyed without color alone;
- examples/help can be collapsed without hiding required labels.

## 22. Product voice

Guided creative assistance should embody the approved Multiversal personality:

- warm, welcoming and encouraging;
- curious rather than prescriptive;
- confident about how the tool works, modest about what makes a “good” story;
- respectful of “I don't know yet,” “skip,” and “none of these”;
- never obsequious or excessively congratulatory;
- never frames a creator's unusual answer as a mistake merely because it differs from a template;
- offers examples as possibilities, not instructions from an authority.

Representative guidance tone:

- “What does this person want badly enough to cause trouble?”
- “You can answer now, leave it open, or pull in an idea you've already saved.”
- “That part may not matter for this version. Skip it if it doesn't help.”

## 23. Privacy and visibility invariants

Before any workflow can show, search, rank, summarize, autocomplete, suggest, generate from or count context:

1. resolve current subject/context;
2. apply current authorization/visibility;
3. limit scope to task-relevant material;
4. expose only safe labels/snippets/projections;
5. apply AI consent/provider policy separately where AI is used.

Hidden Campaign material must not leak through:

- step suggestions;
- “you already have…” hints;
- counts;
- completion/readiness checks;
- relation recommendations;
- generated examples;
- AI output;
- template defaults;
- recent-history surfaces.

## 24. Incorporation handoff

A workflow completion summary may offer governed next actions such as:

- continue developing in CSW;
- open CSW-05 narrative design when available;
- propose/create a World/Location candidate through the owning authoring path;
- propose/create an Adventure candidate;
- propose Character/NPC facts through the Character/owning path;
- prepare investigation content for the owning mystery/investigation authoring path;
- prepare encounter content for the owning encounter system;
- bind selected creative work to a Campaign preparation context if authorized.

Every such action must show the authority change and use the target domain's validation/permission path. “Finish workflow” itself never performs incorporation.

## 25. CSW-05 handoff

CSW-04 intentionally stops short of serious nonlinear narrative structure analysis.

It gives CSW-05:

- guided Adventure/quest drafts;
- plot/thread/hook/conflict/secret/twist/foreshadow/payoff fragments;
- actors/locations/factions references;
- unresolved questions;
- creator-selected alternate branches;
- provenance and Story Bible links.

CSW-05 may then project these into richer plot/beat/scene/choice/consequence structures without treating workflow order as story chronology or canon.

## 26. Acceptance requirements

CSW-04 is design-complete only when the contract demonstrates all of the following:

1. reusable workflow/step primitives are defined independently of one task family;
2. all nine initial creator-task families have bounded blueprint coverage;
3. guidance is optional and equivalent freeform creation remains available;
4. skip/revisit/reorder/pause/branch/abandon behavior preserves saved work;
5. durable creative answers reuse CSW-01/02 rather than a second content truth store;
6. Story Bible context is authorization-filtered and reference-based;
7. CSW-03 Inspiration remains candidate-only and explicit-save;
8. creator templates/presets are versioned, provenance-preserving and non-executable;
9. optional AI is bounded to step assistance and no-AI fallback is complete;
10. workflow completion remains pre-authoritative;
11. offline/reconnect behavior prevents duplicate saves and stale Campaign authority;
12. accessibility/mobile/nonvisual parity covers progress, branching and reordering;
13. product voice is encouraging without prescribing one correct story;
14. CSW-05 receives clean downstream seed/branch/provenance inputs;
15. no application implementation, migration, release or CCTI-12-T04 work is activated.

## 27. Explicit non-authorizations

CSW-04 does not authorize:

- application implementation;
- persistence migration execution;
- mandatory wizard-only authoring;
- automatic authoritative content;
- automated Campaign/World/Adventure/Character mutation;
- AI-controlled workflow completion;
- autonomous AI authorship/publication;
- arbitrary executable creator templates;
- marketplace/community template sharing;
- training on private creator material;
- canonical promotion;
- release/deployment/tester distribution;
- CCTI-12-T04 before September 2026.

## 28. Final design conclusion

Multiversal's guided creation should feel like a thoughtful creative partner laying useful tools on the table, not a form demanding to be completed.

The durable architecture is deliberately simple:

**workflow definitions guide → workflow runs remember progress → Creative Fragments hold creative material → Project Memory/Story Bible supply safe context → Inspiration proposes possibilities → creators decide what to save/use → owning domains decide what becomes truth.**

That separation gives beginners a coherent path, gives experts freedom, keeps creative work recoverable, and preserves the authority/provenance boundaries established by the rest of Multiversal.
