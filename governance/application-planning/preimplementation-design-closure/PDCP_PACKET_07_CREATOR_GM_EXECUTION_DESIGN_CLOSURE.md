# PDCP Packet 07 — Creator/GM Execution UX & Debuggability — Design Closure

**Project:** PDCP — Preimplementation Design Closure Project  
**Packet:** PDCP-PACKET-07  
**Status:** DESIGN_CLOSED  
**Date:** 2026-09-16  
**Implementation authority:** none  
**Roadmap-count mutation:** none  
**MAS:** excluded and not reopened

## 1. Purpose

Close the benchmark-derived design gap around creator/live-GM execution, preview, explanation and debugging without creating a second Action/Event runtime, GM authority system, studio framework, history ledger, permission system or unrestricted scripting environment.

The useful lesson from Neverwinter Nights/Aurora DM workflows, Inform-style staged action/rulebook concepts and behavior-tree/debugger tooling is that creators and live Game Masters benefit from sharing the same semantic objects while receiving different operations and visibility according to role, context and authority.

Packet 07 therefore defines a reusable **execution-inspection contract** for the future Multiversal creator studios and runtime surfaces. It standardizes the semantic lifecycle from draft/proposal through preview/dry-run and owner commit, provides role-safe explanations and rule traces, defines bounded live-GM interventions, and makes reversibility explicit without rewriting historical truth.

It does not define one visual studio shell. MCS, MCCS, MNCS, MSAS, MRCS, GPR, MERA, MBES, MSLR and MSWI retain their domain-specific creator/runtime experiences.

## 2. Existing foundations retained

### 2.1 MV-IA-F006 — Action and GM approval

MV-IA-F006 already establishes the governed Player/GM action proposal loop, nonauthoritative preview, GM inspection/modification/decision, authoritative owner commit, immutable proposal evidence, Event history, idempotency, reconnect and role-safe projection.

Packet 07 does not create a competing Action proposal or GM approval engine.

### 2.2 IA-D04-002 — reusable proposal/approval component

IA-D04-002 already owns the generic proposal envelope, review queue, evidence slots, semantic modification diff, approve/deny/modify controls, decision receipt, status lookup and role-safe history contract. Domain consumers own their calculation, validation, legal modification classes and commit adapters.

Packet 07 reuses that model wherever a future studio needs proposal review. It does not replace consumer-specific owner operations with a generic super-operation.

### 2.3 IA-D04-004 — authoritative result/history presentation

IA-D04-004 already requires authoritative completion to come from durable decisions, consumer commits, ordered Events and current server projections. It distinguishes pending/stale/conflict/recovery states, preserves source/rule versions and filters result/history projections by role.

Packet 07 extends explanation and diagnostics around those authoritative results; it does not weaken the authority resolver.

### 2.4 MV-IA-F020/F021/F025 and shared permissions/recovery/diagnostics

Existing permission/hidden-information, autosave/reconnect/recovery and safe diagnostics/reporting contracts remain binding. Diagnostic tooling cannot gain hidden-data access simply because it is diagnostic.

### 2.5 Future studio/runtime owners

Each PDCP family already has domain-specific UX obligations:

- MCS owns cartographic editing and semantic map binding;
- MCCS owns appearance/presentation creation;
- MNCS owns NPC/creature generation/construction and resolution management;
- MSAS owns audio creation and live soundboard/cue interaction;
- MRCS owns governed rule/content authoring and bounded expressions;
- GPR owns gameplay-pattern execution plus Creator/GM loop tooling;
- MERA owns engineering previews, diagnostics and test/acceptance workflows;
- MBES owns build/settlement gameplay and previews;
- MSLR owns spatial-law runtime and specialist diagnostics;
- MSWI owns cross-domain systemic composition and coverage diagnostics.

Packet 07 supplies common contracts those surfaces can share.

## 3. Core invariants

1. **Same semantics, different authority.** Creator and live-GM views may inspect the same stable owner IDs/definitions/state, but view identity does not grant identical operations.
2. **Draft/proposal/preview/dry-run/counterfactual/live commit/current result are distinct dispositions.** No UI may visually or semantically collapse them into one state.
3. **Preview is not commitment.** A preview/dry-run cannot spend resources, apply Effects, create canonical Events or mutate owner state.
4. **Diagnostics are projections.** A trace/debug session cannot gain mutation authority merely because it can explain state.
5. **GM tools do not create wildcard mutation authority.** Every live intervention maps to a typed owner operation with ordinary permission, precondition and expected-version checks.
6. **Undo is not history deletion.** Canonical Events remain historical evidence. Reversal uses owner-defined inverse/compensation/recovery operations.
7. **Human/Player agency boundaries remain owner-defined.** GM tooling cannot silently override consent or Player-controlled choices protected by governing rules.
8. **Hidden information is filtered before diagnostics.** Counts, graph edges, rule steps, candidate lists, error detail, exports and optional-AI context are filtered before construction.
9. **Advanced authoring is bounded.** MRCS typed formulas/predicates/selectors/graphs may be exposed; unrestricted scripting is not a required or default control surface.
10. **Optional AI is advisory.** It may explain or propose but never receives extra authority, protected truth or commit power.
11. **Offline drafts are not live truth.** Local creator work may continue offline where allowed; live authoritative commit requires owner-authorized convergence.
12. **Accessibility preserves semantic parity.** Graphical traces and visual controls have keyboard, structured text/tree/list and screen-reader equivalents.

## 4. Shared execution lifecycle

The reusable lifecycle is:

`author/draft → validate → proposal (if review required) → preview/dry-run/counterfactual → authorize/revalidate → owner commit → authoritative Event/result → explanation/history/diagnostics → optional inverse/compensation/recovery`

A family may omit stages that do not apply, but it may not treat an omitted nonauthoritative stage as evidence that a commit happened.

### 4.1 Disposition vocabulary

Packet 07 standardizes these semantic dispositions:

- `draft` — editable noncanonical authoring state;
- `proposal` — submitted candidate awaiting governed decision/acceptance;
- `preview` — nonmutating projection of likely/possible consequences;
- `dry_run` — deeper nonmutating validation/execution simulation over pinned inputs;
- `counterfactual` — explicitly hypothetical alternate input/state evaluation;
- `commit_requested` — owner operation submitted but not yet proven committed;
- `committed` — owner confirms authoritative operation result;
- `projection_pending` — commit confirmed but derived presentation not converged;
- `stale` — source/input versions no longer match;
- `blocked` — currently invalid/unauthorized/unsatisfied;
- `recovery_required` — commit status or cross-owner convergence is ambiguous/partial;
- `superseded` — newer accepted state/version replaces a draft/definition projection without deleting history.

These dispositions are not a new canonical ledger. The appropriate owner stores the actual definition/proposal/operation state; the common contract supplies interoperable semantics.

## 5. Reusable contracts closed by Packet 07

### 5.1 `CreatorRuntimeBindingProfile`

Defines how a creator-facing object binds to live owner-domain state without conflating definition, proposal, placement and live instance.

Required semantics:

- profile id/version;
- authoring object type and stable identity requirements;
- owning domain;
- supported dispositions;
- live binding/reference types;
- allowed preview/dry-run modes;
- allowed live intervention capability references;
- required permission/role predicates;
- expected-version policy;
- explanation/diagnostic lens references;
- reversibility policy references;
- visibility policy;
- import/export/review compatibility metadata.

### 5.2 `ExecutionContextSnapshot`

A pinned, role-filtered input envelope used for preview, explanation and step-through diagnostics.

It records:

- snapshot id;
- viewer/actor role and permitted subject scope;
- Campaign/Scene/Session or authoring scope where applicable;
- owner object/version references;
- rules/profile/definition versions;
- visible resources/capabilities/conditions;
- selected resolution/fidelity profile refs;
- deterministic seed/input stream where relevant;
- canonical-time/Event anchor;
- unresolved/unavailable input markers;
- visibility/provenance receipt.

The snapshot is diagnostic input, not a new owner-state copy. If exact historical values are not retained, the snapshot says so.

### 5.3 `PreviewDryRunRequest`

Requests a nonmutating evaluation over an `ExecutionContextSnapshot`.

Modes:

- `preview` — concise expected/possible outcome;
- `dry_run` — validation plus detailed predicted operation/event route;
- `counterfactual` — hypothetical changed input/state;
- `replay_preview` — evaluate using a historical rules/input envelope when supported.

Required request semantics include stable operation id, viewer/initiator, target owner operation or definition, pinned versions, hypothetical overrides if any, requested depth, allowed diagnostics, visibility scope and optional deterministic seed.

### 5.4 `PreviewDryRunReceipt`

A receipt never claims that predicted effects occurred.

It records:

- request/snapshot/profile ids and versions;
- validation outcome;
- predicted owner operations;
- predicted typed deltas/Events where deterministic rules support prediction;
- ranges/branches/unknowns where outcomes depend on randomness, hidden decisions or human adjudication;
- resource/cost assumptions without reserving or consuming them;
- permission/authority assumptions;
- affected owner domains;
- warning/conflict/unresolved references;
- deterministic seed where used;
- stale detection information;
- provenance.

A preview of a nondeterministic or human-adjudicated outcome must not pretend to be a guaranteed result.

### 5.5 `ExplanationRequest`

A role-safe request for one or more of:

- `what_happened`;
- `why_available`;
- `why_blocked`;
- `why_result`;
- `which_rule_source_version`;
- `which_owner_committed`;
- `what_changed`;
- `what_is_unknown`;
- `what_can_be_done_next`;
- `why_preview_differs_from_commit`.

The request references an accepted Event/result, proposal, preview receipt, diagnostic session or current owner projection.

### 5.6 `ExplanationReceipt`

Contains only role-authorized explanation evidence:

- subject/result ids;
- explanation kind;
- visible rule/profile/source/version refs;
- visible preconditions and reason codes;
- visible owner/operation/Event refs;
- visible before/after values or state classifications;
- unresolved/unknown reasons;
- stale or historical-version warnings;
- causal links that may be disclosed;
- provenance.

Protected rules, secret modifiers, hidden targets, unrevealed topology, private NPC motives and concealed candidate operations are excluded before counts/steps are constructed.

### 5.7 `RuleEvaluationTrace`

An ordered diagnostic projection showing how an already-authorized preview or result was evaluated where the owner/runtime exposes traceable steps.

Each `RuleTraceStep` may include:

- stable step id;
- rule/profile/definition ref;
- operation/predicate/selector kind;
- visible input refs;
- visible output/classification;
- pass/fail/unresolved state;
- branch/precedence reason;
- sequence/dependency refs;
- source/version/provenance;
- role-safe explanation.

The trace is evidence/explanation, not an executable script.

### 5.8 `DiagnosticLensDefinition`

Defines a reusable role-safe diagnostic projection. Examples include:

- authority/permission;
- input/source/version;
- rule evaluation;
- owner handoff;
- dependency/reference;
- effect/consequence fan-out;
- event/provenance;
- stale/concurrency;
- accessibility/presentation;
- performance/fidelity;
- family-specific diagnostic lenses.

A lens declares its source owners, viewer roles, allowed fields, resolution depth and redaction behavior. A diagnostic lens cannot widen authority.

### 5.9 `StepThroughDiagnosticSession`

An ephemeral session over a pinned snapshot/trace.

It supports moving between rule/operation stages, inspecting role-safe inputs/outputs, comparing preview with current state and optionally changing hypothetical inputs for a new counterfactual preview.

A step-through session:

- does not pause canonical Campaign time;
- does not reserve resources;
- does not mutate live state;
- becomes stale if the live owner versions diverge;
- must never claim a hidden step exists to an unauthorized viewer merely through step count/cardinality.

### 5.10 `GMInterventionCapabilityDefinition`

Defines a typed live intervention the GM may request through an existing owner operation.

Required semantics:

- capability id/version;
- owner operation/action ref;
- applicable target/role/scope selectors;
- GM/Assistant-GM authority requirements;
- required evidence/preconditions;
- modifiable fields/parameters;
- expected-version requirements;
- preview/dry-run support;
- approval/confirmation policy;
- reversibility classification;
- Event/provenance requirements;
- Player-agency/consent constraints;
- visibility/notification policy.

There is no generic `force_set_any_field` intervention.

### 5.11 `GMInterventionRequest` and `GMInterventionReceipt`

The request records actor/role, capability, target, requested parameters, reason/context, expected versions and preview reference where applicable.

The canonical owner reauthorizes and commits. The receipt records accepted/modified/denied/blocked/ambiguous status, exact owner operation/Event refs, final parameters, decider/initiator attribution, stale revalidation, resulting state projection refs and provenance.

Assistant-GM interventions remain constrained by active delegation.

### 5.12 `ReversibilityClassification`

Every consequential intervention/commit may expose one of these classes where its owner can determine it:

- `draft_revert` — noncanonical local/draft edit can be reverted without Event mutation;
- `owner_inverse_operation` — owner exposes a semantic inverse operation;
- `owner_compensation_operation` — owner exposes a compensating operation, not literal restoration;
- `snapshot_restore_permitted` — owner explicitly supports restore/recovery under stated version/conflict constraints;
- `gm_adjudication_required` — reversal semantics require an authorized human decision;
- `irreversible` — no supported reversal path.

No universal undo guarantee exists.

### 5.13 `UndoCompensationPlan`

A preview-only plan listing:

- source committed Event/operation;
- current owner versions;
- applicable reversibility class;
- proposed inverse/compensation/restore owner operations;
- affected downstream state and known conflicts;
- later Events that may prevent clean reversal;
- irreversible residual consequences;
- required approvals;
- role-safe notifications;
- recovery plan for partial failure.

The plan itself does nothing.

### 5.14 `UndoCompensationRequest` and `UndoCompensationReceipt`

Execution sends ordinary owner operations. The receipt preserves the original Event and records newly committed inverse/compensating Events. Historical truth is never erased to make the world look as though the original action never occurred.

### 5.15 `LiveControlBindingDefinition`

Binds a studio/runtime control to one of:

- presentation-only operation;
- prepared-content activation request;
- owner-domain gameplay operation;
- proposal/review operation;
- runtime configuration operation;
- diagnostic-only operation.

The binding is explicit so a live control cannot accidentally elevate presentation activity into game truth.

Examples:

- an MSAS soundboard control may start/stop a cue without fabricating the gameplay Event that the cue represents;
- an MCS fog/annotation control may alter an authorized presentation projection without rewriting World truth;
- an MSLR topology mutation control must use MSLR/owner spatial operations before canonical connectivity changes;
- an MSWI generated-site promotion control must follow the governed promotion path rather than treating preview geometry as Campaign truth.

### 5.16 `CollaborationReviewBinding`

Defines comments, review status, requested changes, approval/rejection signals, semantic diffs and reviewer attribution for creator artifacts.

Review is evidence/workflow state, not game authority. A reviewer saying “approved” cannot substitute for an owner commit or publication gate unless the governing profile explicitly binds that reviewer/decision to the canonical operation.

### 5.17 `AuthoringDiagnosticReceipt`

Captures validation/diagnostic findings for a draft/definition without pretending findings are live state. It includes exact artifact/version, diagnostic lens/profile versions, visible findings, severity/classification, dependencies/impact, suggested fixes where permitted and provenance.

### 5.18 `CounterfactualPreviewReceipt`

A counterfactual is always labeled noncanonical. It records the changed assumptions separately from actual state and cannot be committed by “accepting the preview” unless the relevant owner operation is separately constructed, authorized and revalidated.

## 6. Preview, dry-run and commit semantics

### 6.1 Preview cannot reserve or spend

Previewing a construction project, engineering refit, NPC action, map binding, audio cue, spatial-law change, systemic consequence or gameplay loop may calculate expected costs/resources but does not reserve, transfer or consume them.

If reservation is required, the appropriate owner exposes a distinct reservation/commitment operation and Event/receipt.

### 6.2 Dry-run uses pinned versions

A dry-run records every owner version/input it relied on. A later commit revalidates those versions. If target position, ownership, resource inventory, authority, rule version, definition or other relevant state changed, the commit is stale and must re-preview/revalidate as the owner requires.

### 6.3 Unknowns remain unknown

If an outcome depends on hidden GM choice, a random result not yet drawn, missing source data, optional human adjudication, unsupported downstream rules or an unmodeled external owner, the preview reports the uncertainty. It does not generate fake certainty.

### 6.4 Counterfactuals remain isolated

Changing an input in a step-through/debugger creates a counterfactual branch. It never rewrites the snapshot used to explain the actual historical result.

## 7. Explanation and debugging semantics

### 7.1 Explanation is evidence, not new authority

An explanation may reveal why an operation is available/blocked or why a result occurred, but only from evidence the viewer may access. A successful explanation does not create an operation permission.

### 7.2 Trace depth is presentation depth

Packet 07 supports three diagnostic presentation depths:

- `overview` — status, owner, key reason, next safe action;
- `standard` — visible inputs, rules, owner route and result/diff;
- `deep` — ordered rule/operation trace, versions, seeds and provenance where available.

These align with existing presentation-granularity practice and do not create new simulation fidelity or mechanics.

### 7.3 Historical traces pin old versions

When explaining a historical result, the system uses the rule/profile/source version recorded for that result where retained. A newly edited rule cannot silently reinterpret history.

### 7.4 Human adjudication is attributable, not falsely deterministic

A GM judgment may be recorded with inputs, options, modification diff, reason and resulting owner Event. If the decision was discretionary, replay may reproduce the historical decision record but must not claim the same decision would necessarily be generated automatically.

## 8. GM intervention and Player agency

GM authority remains scoped by Campaign, role, delegation and owner contracts.

A GM may have broader visibility/decision authority than Players, but Packet 07 does not assume the GM can mutate arbitrary server fields. Live intervention is always a typed capability routed to its owner.

Where a governing rule protects consent or Player-controlled Character choice, the intervention capability must respect that boundary. A GM tool can expose a separately governed override only if such an override is explicitly part of the owner rules; Packet 07 cannot invent one.

Assistant-GM access is delegation-limited and revocable. Revocation invalidates uncommitted requests.

## 9. Reversal, compensation and recovery

### 9.1 Canonical Events are not deleted by undo

An inverse or compensation creates later Events. History shows both the original and the response.

### 9.2 Snapshot restore is exceptional

Snapshot restore is allowed only when the owning systems explicitly support it and the restore contract addresses later conflicting Events, external owner mutations, version migration and multiplayer/shared authority. A UI “restore” button cannot imply this support universally.

### 9.3 Cross-owner partial reversal

A multi-owner operation may have only partial reversible coverage. The plan/receipt must identify which owner effects were inverted, compensated, blocked or irreversible. The orchestrator cannot falsely display “undone” if a downstream consequence remains.

### 9.4 Ambiguous owner response

If a reverse/compensation request receives an ambiguous response, use operation-status lookup/current-version recovery before retry. Never blindly duplicate the inverse operation.

## 10. Live-control examples across future families

### MCS

Creator edits and generator output stay drafts/proposals. World-sync/binding controls explain which map features are presentation-only versus owner-backed. Live fog/annotation controls cannot silently change canonical World/Discovery truth.

### MCCS

Appearance previews, rigs and derivative renders may change presentation drafts. They cannot silently alter Species/Form anatomy, equipment ownership or Character mechanics. Runtime appearance-state changes require the proper owner binding.

### MNCS

Generated candidates, improv cards, behavior previews and population individualization stay proposals until accepted. Creator diagnostics can show generation provenance, constraints and unresolved fields; live NPC actions still use runtime owner operations.

### MSAS

Waveform/timeline authoring is studio state. Event→cue bindings may be previewed. A live soundboard cue can control audio presentation but cannot manufacture the gameplay Event it symbolizes.

### MRCS

Rule/content definitions, scoped overrides and simulations remain authoring state until published/activated through governed paths. Deep traces may expose bounded rule atoms/predicates/selectors without enabling unrestricted code execution.

### GPR

GM-led loop controls operate through typed gameplay operations/outcomes. Replay/trace/persistence provide core execution evidence. GPR-14 is a primary implementation home for the common Creator/GM execution-inspection UX.

### MERA

Blueprint/configuration dry-runs and fault diagnostics remain nonauthoritative. Installing/removing/repairing/calibrating actual components requires Item/Asset/crafting/Project/etc. owner commits.

### MBES

Build previews, capability inspection, automation graphs and externality previews cannot create construction, ownership, pollution or resident relocation truth. Accepted construction routes through owner operations.

### MSLR

Topology/law previews and solvability diagnostics remain projections until spatial owner operations commit. True/observable/known/suspected topology remain separated in diagnostics.

### MSWI

Systemic fan-out, procedural-site preview and interaction-density diagnostics are explanatory/proposed until owner routes commit consequences or an accepted site is promoted.

## 11. Collaboration and review

Creator collaboration may support comments, semantic diffs, review requests, branch/fork comparisons, conflict resolution and role-attributed review decisions.

Rules:

1. collaborative review cannot widen source visibility;
2. hidden/GM-private data are filtered before collaborator counts/diffs/comments;
3. comments do not mutate governed definitions;
4. review approval is not owner commit unless explicitly bound by the governing publication/acceptance profile;
5. concurrent edits use explicit versions/merge/conflict handling;
6. published/accepted history remains inspectable after later revisions;
7. offline review/draft work is nonauthoritative until synchronized/revalidated.

## 12. Permission and hidden-information behavior

Filtering occurs before:

- preview construction;
- dry-run candidate/operation lists;
- explanation reason lists;
- trace step counts;
- graph nodes/edges;
- GM/Assistant-GM control availability;
- collaboration participants/comments/diffs;
- diagnostic exports;
- rule/source text;
- history timelines;
- optional-AI context.

An unauthorized viewer must not infer a secret NPC, hidden route, unrevealed Effect, concealed resource, private motive, hidden rule, secret successor, undiscovered evidence or protected topology from cardinality or error wording.

## 13. Concurrency, determinism and replay

1. Preview and commit use stable operation IDs and expected owner versions.
2. Commit always reauthorizes/revalidates current state.
3. Deterministic previews record seeds, profiles and exact inputs needed to reproduce the claim.
4. A stochastic preview records the seed if sampled; unsampled distributions/ranges remain ranges.
5. Historical explanation pins historical source/profile versions.
6. Duplicate delivery does not create duplicate interventions or compensation Events.
7. Concurrent GM interventions against the same exclusive state resolve through owner expected-version/idempotency rules, not UI order.
8. Multiplayer/shared state uses the runtime authority model; local debugger frame order has no authority.
9. If exact replay inputs were not retained, diagnostics say replay is incomplete.

## 14. Offline/local-first behavior

Creator drafts, comments, previews from locally available authorized data and diagnostic review may work offline where the owning studio supports it.

Offline limitations must be explicit:

- cached live state is nonauthoritative;
- hidden/revoked content is removed under existing recovery policy;
- live GM commits do not become authoritative while disconnected;
- queued local requests require reconnect reauthorization and may become stale;
- optional AI/provider unavailability never blocks core preview/explanation/typed-control workflows.

## 15. Optional AI boundary

AI may:

- summarize a role-safe explanation receipt;
- suggest a diagnostic lens;
- propose a legal GM intervention before ordinary hard filtering;
- explain a semantic diff;
- suggest authoring fixes;
- summarize a rule trace;
- suggest tests/counterfactuals.

AI may not:

- receive hidden truth unavailable to the invoking role;
- fabricate rule steps or source evidence;
- grant permissions;
- execute unrestricted scripts;
- commit owner state;
- approve a proposal;
- choose for a protected Player-controlled entity without explicit owner-authorized delegation;
- erase history;
- label a preview as an authoritative result.

All blocking functionality works with AI disabled.

## 16. Five-second UX surfaces

### 16.1 Creator glance

A creator should quickly see:

- object/artifact name and stable identity;
- draft/published/proposed/live-binding disposition;
- validation status;
- unresolved/broken references;
- current version and unsaved/local state;
- affected owner domains;
- latest preview status;
- review/conflict state;
- next allowed action.

### 16.2 Live GM glance

A GM should quickly see:

- current authoritative context/version;
- pending proposals/decisions within authority;
- available typed interventions;
- stale/blocked/recovery warnings;
- current live controls and whether each is presentation-only or canonical-owner routed;
- recent attributable Events/results;
- one-step access to role-safe explanation.

The glance surface is not a substitute for deeper inspection.

## 17. Failure and edge cases

- **Preview source stale:** mark stale; do not silently recompute and call it the same receipt.
- **Missing owner definition:** return unresolved/unsupported; no generic fallback operation.
- **Hidden blocked reason:** provide safe generic reason without revealing hidden existence.
- **Rule trace unavailable:** explanation states trace not retained/supported rather than inventing steps.
- **Human adjudication:** preserve attributable decision, not fake deterministic replay.
- **Wildcard GM field mutation:** reject; require typed owner capability.
- **Permission revoked during inspection:** remove protected projection and invalidate uncommitted request.
- **Resource changes after preview:** commit revalidation blocks/recomputes.
- **Later Events prevent inverse:** compensation plan reports conflict/irreversible residual.
- **Partial inverse succeeds:** explicit partial receipt; never show full undo.
- **Two reviewers approve conflicting drafts:** ordinary version/conflict policy decides; review status is not commit.
- **Offline live intervention:** remains unsent/local pending; cannot create authoritative completion.
- **Diagnostic export:** must use same role-safe projection as interactive diagnostics.
- **Graph inaccessible:** semantic ordered list/tree exposes equivalent nodes, edges, status and operations.
- **Optional provider unavailable:** core workflow remains usable.

## 18. Accessibility

Required functional parity includes:

- keyboard operation for preview, trace traversal, review and GM controls;
- ordered textual `RuleEvaluationTrace` alternative to visual graphs;
- semantic tree/list representation for dependencies/fan-out/topology;
- non-color-only disposition and status signals;
- screen-reader announcement of preview versus committed versus stale status;
- before/after/diff descriptions in logical reading order;
- accessible confirmation for irreversible or compensating operations;
- no time-critical pointer-only interaction as the sole GM-control path;
- captions/transcripts/non-audio equivalents for diagnostic cues;
- focus restoration after dialogs/status lookup/recovery.

## 19. Golden validation vectors

Future implementation must automate or equivalently prove these 48 cases.

### Preview / dry-run / counterfactual

1. **PDCP-GMX-001** — editing a draft preview changes no canonical owner state.
2. **PDCP-GMX-002** — preview lists predicted owner-operation routes but creates no Events.
3. **PDCP-GMX-003** — state/version changes after preview cause commit revalidation failure or re-preview.
4. **PDCP-GMX-004** — nondeterministic outcome is shown as range/branch/unknown rather than guaranteed.
5. **PDCP-GMX-005** — unauthorized hidden target is absent from preview and counts.
6. **PDCP-GMX-006** — unsupported downstream effect is explicit unresolved, not invented.
7. **PDCP-GMX-007** — counterfactual output remains visibly noncanonical.
8. **PDCP-GMX-008** — preview receipt preserves exact rule/profile/source versions.
9. **PDCP-GMX-009** — deterministic preview with identical retained inputs/seed reproduces.
10. **PDCP-GMX-010** — discretionary human adjudication is attributable but not mislabeled deterministic.

### Explanation / trace / diagnostics

11. **PDCP-GMX-011** — role-safe explanation identifies why an operation is blocked.
12. **PDCP-GMX-012** — hidden reason does not leak through reason count or trace cardinality.
13. **PDCP-GMX-013** — rule trace preserves ordered visible steps and versions.
14. **PDCP-GMX-014** — missing/disabled rule returns unresolved/blocked rather than fallback behavior.
15. **PDCP-GMX-015** — step-through diagnostic binds a pinned snapshot.
16. **PDCP-GMX-016** — step-through does not pause or mutate canonical Campaign time.
17. **PDCP-GMX-017** — live state change marks an open diagnostic session stale.
18. **PDCP-GMX-018** — Player cannot open a GM-only diagnostic lens by direct URL/API request.
19. **PDCP-GMX-019** — authorized GM receives hidden detail only within actual GM authority.
20. **PDCP-GMX-020** — Assistant-GM explanation/controls are limited by active delegation.

### GM intervention / authority

21. **PDCP-GMX-021** — a valid GM intervention maps to a typed owner operation and Event.
22. **PDCP-GMX-022** — generic arbitrary-field mutation is rejected.
23. **PDCP-GMX-023** — owner-protected Player consent/choice cannot be bypassed by generic GM tooling.
24. **PDCP-GMX-024** — intervention receipt records initiator, reason/context, owner operation and final result.
25. **PDCP-GMX-025** — concurrent incompatible interventions resolve through expected-version owner rules.
26. **PDCP-GMX-026** — ambiguous intervention response triggers status lookup, not blind retry.

### Reversal / recovery

27. **PDCP-GMX-027** — reverting an uncommitted draft creates no canonical Event.
28. **PDCP-GMX-028** — owner inverse operation creates a new Event while original Event remains history.
29. **PDCP-GMX-029** — compensation operation records nonidentical compensating outcome/provenance.
30. **PDCP-GMX-030** — irreversible operation reports no supported undo path.
31. **PDCP-GMX-031** — snapshot restore is blocked when later conflicting Events violate owner restore rules.
32. **PDCP-GMX-032** — partial cross-owner compensation remains explicitly partial.

### Family live-control boundaries

33. **PDCP-GMX-033** — MSAS live cue playback does not fabricate the gameplay Event associated with the cue.
34. **PDCP-GMX-034** — MCS live fog/annotation presentation control does not rewrite canonical World truth.
35. **PDCP-GMX-035** — MSLR topology preview does not change live connectivity until owner commit.
36. **PDCP-GMX-036** — MSWI procedural-site preview remains ephemeral/proposed until governed promotion.
37. **PDCP-GMX-037** — MERA configuration dry-run leaves Asset/component state unchanged.
38. **PDCP-GMX-038** — MBES build preview consumes no construction resources and creates no built state.
39. **PDCP-GMX-039** — MNCS generated candidate becomes live only through explicit acceptance/handoff.
40. **PDCP-GMX-040** — MCCS visual appearance preview cannot change canonical anatomy/mechanics.
41. **PDCP-GMX-041** — MRCS rule simulation cannot silently activate or mutate live Campaign rules.
42. **PDCP-GMX-042** — GPR GM intervention produces typed outcome/Event trace and deterministic replay evidence where declared.

### Collaboration / offline / accessibility

43. **PDCP-GMX-043** — collaborator comment changes no canonical definition or live state.
44. **PDCP-GMX-044** — review approval does not become owner commit unless explicit governing profile binds it.
45. **PDCP-GMX-045** — offline creator draft is allowed where supported while live commit remains nonauthoritative until reconnect/revalidation.
46. **PDCP-GMX-046** — graph/trace diagnostic has keyboard and screen-reader semantic list/tree parity.
47. **PDCP-GMX-047** — diagnostic export applies the same role-safe filtering as interactive inspection.
48. **PDCP-GMX-048** — all core preview/explanation/GM-control workflows operate with optional AI/providers disabled.

## 20. Future-family implementation mapping

Packet 07 creates **no new family and no standalone tranche**. Because creator/GM execution and debugging is cross-cutting, every PDCP family receives a bounded implementation obligation inside already-planned work.

### MCS

- `MCS-01` — workspace disposition/authority labels;
- `MCS-03` — editing-history versus canonical-history separation;
- `MCS-10` / `MCS-11` / `MCS-12` — generator preview/dry-run receipts;
- `MCS-18` — semantic binding/world-sync owner route explanation;
- `MCS-20` — collaboration/review/version integration;
- `MCS-21` — golden creator/live-binding proof.

### MCCS

- `MCCS-01` — creator workspace authority/disposition contract;
- `MCCS-02` — draft-overlay/preview status;
- `MCCS-12` — rig/retarget preview diagnostics;
- `MCCS-17` — variant-generation preview/provenance;
- `MCCS-19` — review/round-trip/provenance;
- `MCCS-21` — golden preview/live-authority separation proof.

### MNCS

- `MNCS-01` — workspace/authority/resolution diagnostics;
- `MNCS-02` — seeded generation preview/explanation;
- `MNCS-05` — five-second GM surface;
- `MNCS-18` — secret/reveal-safe diagnostics;
- `MNCS-21` — resolution-transition inspection;
- `MNCS-22` — runtime handoff/commit status;
- `MNCS-23` — review/provenance/AI boundary;
- `MNCS-24` — golden creator-to-live proof.

### MSAS

- `MSAS-01` — workspace/authority/disposition semantics;
- `MSAS-09` — Event→cue binding preview/explanation;
- `MSAS-14` — listener/spatial preview diagnostics;
- `MSAS-15` — live GM trigger classification and receipts;
- `MSAS-18` — review/collaboration/versioning;
- `MSAS-21` — golden cue/live-state separation proof.

### MRCS

- `MRCS-01` — studio authority/disposition integration;
- `MRCS-02` / `MRCS-03` — inspectable schema/guided authoring validation;
- `MRCS-04` — bounded traceable expressions;
- `MRCS-16` — scoped rule/override preview and conflict explanation;
- `MRCS-17` — dependency/impact diagnostics;
- `MRCS-18` — simulation/playtest evidence;
- `MRCS-20` — diff/review/version/publication;
- `MRCS-21` — golden authoring-to-runtime proof.

### GPR

- `GPR-08` — pattern composer preview/dry-run integration;
- `GPR-09` — GM delivery-mode control semantics;
- `GPR-11` — common accessible UI/feedback projection;
- `GPR-12` — replay/determinism/Event trace;
- `GPR-13` — snapshot/recovery/version semantics;
- `GPR-14` — primary Creator/GM loop studio implementation home;
- `GPR-15` — conformance of shared execution-inspection contract;
- `GPR-16` — golden runtime proof.

### MERA

- `MERA-01` — engineering workspace authority/dispositions;
- `MERA-03` — proposed configuration/dry-run/diff/commit integration;
- `MERA-05` — diagnostic lens/unknown-fault explanation;
- `MERA-22` — test/simulation/acceptance evidence;
- `MERA-23` — review/provenance/optional-AI boundary;
- `MERA-24` — golden engineering preview/commit/compensation proof.

### MBES

- `MBES-01` — workspace/authority/resolution status;
- `MBES-04` — Player/GM build preview/commit semantics;
- `MBES-05` — capability/requirement explanation;
- `MBES-07` — blueprint review/provenance;
- `MBES-09` — condition→action control diagnostics;
- `MBES-14` / `MBES-15` — externality/reactive-world preview and owner-route explanation;
- `MBES-24` — golden build/GM/recovery proof.

### MSLR

- `MSLR-03` — topology Event trace/replay/recovery;
- `MSLR-04` / `MSLR-05` — role-safe topology/observation explanation;
- `MSLR-06` — preview/undo/counterplay owner operations;
- `MSLR-14` — solvability diagnostic receipts;
- `MSLR-17` — specialist GM/Creator diagnostics and simulation UX;
- `MSLR-18` — golden spatial preview/commit proof.

### MSWI

- `MSWI-03` — propagation/reversibility/recovery explanation;
- `MSWI-14` — procedural preview and GM promotion;
- `MSWI-15` — current/history/variant presentation status;
- `MSWI-17` — cross-system diagnostics/fan-out/loop explanation;
- `MSWI-18` — golden systemic creator/GM proof.

There are no `no_direct_obligation_families` for Packet 07: all ten in-scope PDCP families consume the common execution-inspection contract through existing tranches.

## 21. Roadmap-reduction implication

Packet 07 removes the need for each future family to independently research and invent:

- draft/proposal/preview/dry-run/commit semantics;
- creator versus live-GM authority distinction;
- explanation and rule-trace behavior;
- typed GM-intervention boundaries;
- reversibility/compensation meaning;
- collaboration review versus canonical acceptance;
- common diagnostic privacy/accessibility rules.

This design closure does not itself remove or merge any tranche. Family-level PDCP reduction receipts must later identify which baseline UX/authority/diagnostic tranches now contain only implementation work, which can merge, and where the 48 golden vectors are automated.

## 22. Closure decision

Packet 07 is `design_closed`.

- New family required: **no**.
- New standalone implementation tranche required: **no**.
- Owner decision remaining: **no**.
- Roadmap-count mutation in this packet: **none**.
- OPS3 `CURRENT.json` mutation: **none**.
- MAS impact: **none; excluded and not reopened**.
- Residual implementation: **MCS, MCCS, MNCS, MSAS, MRCS, GPR, MERA, MBES, MSLR and MSWI existing planned scopes**.
- Next open benchmark-derived packet: **Packet 08 — Simulation & Formal Validation Laboratory**.
