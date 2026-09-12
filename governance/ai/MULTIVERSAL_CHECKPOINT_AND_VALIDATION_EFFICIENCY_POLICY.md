# Multiversal Checkpoint and Validation Efficiency Policy

**Document ID:** MV-AI-EFFICIENCY-001  
**Version:** 1.3.0  
**Status:** ACTIVE — OWNER APPROVED  
**Owner and final authority:** John Brandon Turner  
**Effective:** 2026-08-06  
**Updated:** 2026-09-12

## 1. Purpose

This policy preserves reliable conversation recovery without allowing checkpoint bookkeeping or broad final validation to dominate the actual Multiversal work.

The continuity system exists to make restarts faster and safer. It must not require a repository checkpoint, status projection, scorecard regeneration, or full CI cycle after every small mutation.

This policy controls where it conflicts with earlier instructions requiring checkpoint updates after each atomic batch.

Final validation compute/routing is governed by:

`governance/ai/MULTIVERSAL_SELF_HOSTED_FINAL_VALIDATION_POLICY.md`

GitHub remains the orchestration/evidence control plane; GitHub-hosted compute is not the default final gate.

## 2. Milestone-only checkpoint rule

A governed work attempt receives a durable checkpoint only at these boundaries:

1. **Start:** once, before substantive work, recording the work item, branch, objective, exact active operation, and exact next action.
2. **Material handoff or blockage:** only when work must stop, the conversation may end before the package is finished, an owner decision is required, or a real failure changes the recovery path.
3. **Ready for review:** once, after the complete deliverable package and its targeted local validation are finished.
4. **Completed verified:** once, after required exact-head final validation and merge evidence exist.

Do not update checkpoints after ordinary file creation, edits, local checks, commits, validator repairs, or other uninterrupted substeps.

Substantive branch commits, pull-request evidence, and the work package itself provide intermediate history. The checkpoint is a recovery boundary, not an activity log.

## 3. No standalone completion-loop rule

A separate completion-only pull request is not required merely to copy merge evidence into runtime state.

After a package merges, its `completed_verified` projection may be recorded together with the next work item's start checkpoint. Create a standalone completion correction only when:

- work is stopping before the next item starts;
- the repository would otherwise have contradictory recovery state;
- a release, owner, security, or irreversible gate depends on the correction; or
- the completion record itself is materially defective.

A completed package must still have verified final-head CI and merge evidence. This rule removes redundant validation cycles; it does not weaken completion evidence.

## 4. Validation cadence

During uninterrupted work:

- run the smallest relevant local or deterministic checks;
- finish the complete bounded package before opening or refreshing final review;
- batch compatibility and validator repairs together;
- trigger the full declared final suite once on the finished package;
- route application/package final validation through the self-hosted Windows/Linux architecture defined by `MV-AI-VALIDATION-003` unless the work item explicitly requires another environment for a specific reason;
- when final validation finds multiple related issues, repair them as one batch and rerun once;
- do not create one commit and one full CI cycle per assertion.

The final declared acceptance gate remains mandatory. GitHub-hosted compute is optional unless explicitly justified as a blocking independent audit under the controlling self-hosted final-validation policy.

## 5. Workflow isolation

Workflows must be scoped to the artifacts they validate.

- Continuity validation may run when checkpoints, pointers, status projections, or continuity tooling change.
- Feature validators may run when their feature artifacts, validator, workflow, or direct dependencies change.
- The interaction operational pilot may run when its pilot scenarios, scorecards, pilot tool, tests, bootstrap integration, or operating amendment change.
- Routine work-pointer or implementation-status changes must not force regeneration of the historical interaction pilot scorecard.
- Historical scorecards are evidence of their recorded run. They are not live mirrors of every later work-item selection.
- Runner wake/recovery plumbing is infrastructure and should not be allowed to broaden a feature workflow's acceptance scope.

## 6. Roadmap and pointer writes

During a work item, do not repeatedly rewrite:

- the full application roadmap;
- the roadmap index;
- the current-work pointer;
- the compact status projection;
- historical pilot scorecards.

Update roadmap material only when scope, dependencies, owner decisions, milestone status, or final verified completion changes.

Update the current-work pointer when the selected work item changes, when a real handoff/block occurs, or at final completion—not for routine progress narration.

## 7. Conversation recovery guarantee

A valid start checkpoint must contain enough information for a new conversation to recover:

- canonical repository;
- exact branch;
- work-item and attempt IDs;
- objective;
- active operation;
- next action;
- known blockers;
- completion gate.

If a conversation stops unexpectedly, the latest substantive branch commit and open pull request supplement that start checkpoint. A special handoff checkpoint is needed only when the branch evidence does not make the next operation clear.

## 8. Owner-facing reporting

Do not narrate every repository operation or validation poll.

Report to the owner only when there is:

- a material finding that changes the approach;
- a genuine blocker or owner-only decision;
- a finished bounded package;
- final CI and merge evidence; or
- a concise end-of-run status.

## 9. Prohibited regressions

This policy does not authorize:

- false completion;
- skipping the final declared acceptance gate;
- hiding failed validation;
- deleting failed attempts;
- weakening permission, privacy, provenance, security, migration, checksum, deterministic cross-platform comparison, or release controls;
- paid services, production credentials, deployment, internal-alpha release, or public release without the existing owner gates.

## 10. Immediate application

Apply this policy immediately to active and future governed work.

For application/package final gates after 2026-08-18, use the self-hosted validation policy as the normal routing authority. Historical work whose only blocker was the former generic requirement for GitHub-hosted compute must be re-evaluated rather than automatically completed.

## 11. Tranche execution fast path

The family preflight's active-time target and closeout reserve are operating constraints, not descriptive estimates. **Operational overhead counts against the tranche target.** For a preflight that declares `target_active_minutes_per_unit` and `minimum_closeout_reserve_minutes`, the closeout-switch point is:

`target_active_minutes_per_unit - minimum_closeout_reserve_minutes`

For the current 24-minute / 8-minute pattern, that means the closeout-critical path is protected beginning at minute 16. Crossing the closeout-switch point is not permission to stop execution; it means optional investigation ends and only completion-critical work remains.

### 11.0 Execution-envelope boundary rule

The execution envelope, not a logical operation, is the ordinary cycle boundary. **Logical-operation completion is not cycle completion.** One owner `Continue` owns one stable cycle identity across every dynamically packed operation in that envelope.

During the fill phase, when a logical operation finishes before the closeout switch and safe same-lane work exists, immediately use dynamic fill to select the next safe operation. Do not perform a shared closeout, increment the cycle, or return control merely because a sub-operation, research facet, commit, artifact, test batch, or milestone completed.

For the canonical 24-minute envelope, minute 16 switches the same cycle from fill to shared closeout; it does not create a new cycle. Normal completion requires the shared closeout to finish and the 24-minute target to be accounted. Earlier closure is permitted only after an actual dynamic-fill attempt proves that no safe same-lane work remains, or through the separately evidenced genuine-blocker path.

Cycle identity and elapsed envelope state are monotonic recovery state. Conversation changes, context compaction, tool-batch boundaries, progress reports, and logical-operation completion do not reset them. If execution is interrupted, resume the same cycle rather than turning the next logical step into a fresh cycle.

### 11.1 Preload once; do not rediscover

At bounded recovery, preload only the current tranche's named authority, checkpoint, exact branch/PR state, required predecessor evidence, and declared validation profile. After that:

- do not rediscover an already-loaded tool schema, connector capability, repository identity, workflow shape, branch naming pattern, or merge method unless a concrete tool error or authority change invalidates it;
- do not reread unchanged authority or repository facts merely because time passed, a tool batch ended, context compacted, or commentary was emitted;
- do not browse unrelated Drive, Airtable, Sheets, Docs, historical branches, dormant programs, parallel work packages, or broad repository history unless current failure evidence makes one of them directly relevant.

### 11.2 Preserve parallel work without exploring it

Unrelated parallel work is preserved, not re-investigated. If canonical `main` moved during the tranche, first compare the changed paths against the bounded tranche/control-plane surfaces.

- If there is no overlap, rebase/transplant the already-prepared bounded blobs or commit onto current `main` without rereading unrelated content.
- If there is overlap, inspect only the overlapping files and reconcile them.
- The mere existence of DWC, LXG, GCL, CNI, PCA, SAA, or any other parallel/future work is not a reason to load its internal state during an ARI tranche.

### 11.3 Batch repository mutations

When several independent control-plane files form one governed transition, prefer an **atomic multi-file closeout** using a single tree/commit operation where the available GitHub surface supports it. Do not spend the closeout reserve creating one serial commit per projection unless atomic mutation is unavailable or a concrete conflict requires isolated writes.

Likewise, batch independent reads or evidence checks when the tool surface supports it. Sequential calls are reserved for true data dependencies.

### 11.4 Evidence economy

For a successful validation run, prefer the smallest authoritative evidence surface:

1. workflow/run conclusion and exact head;
2. compact job-step summary or compact generated evidence artifact;
3. deterministic receipt/comparison artifact when required.

**Full successful workflow logs are prohibited by default.** Read full logs only when the run failed, the compact evidence is missing/contradictory, or a specific acceptance fact cannot otherwise be proved.

Do not download or inspect every artifact when one compact receipt already proves the required facts.

### 11.5 Polling and mergeability discipline

Do not use fixed sleep/poll loops as ordinary orchestration. Query only at meaningful state transitions: queued/running → terminal validation, validated → merge, merge → canonical-main verification.

An initial GitHub `mergeable: false` response, by itself, is not evidence of a conflict when base/head are unchanged and no conflicting paths are reported. Allow **one bounded recomputation check** before launching repository-race diagnosis. Investigate a race only when `main` actually changed, GitHub reports a conflict, or path comparison shows overlap.

Repeated mergeability reads, repeated unchanged head reads, and repeated status narration are operational noise and count as a convergence defect when they consume the protected reserve.

### 11.6 Closeout reserve fast path

At the closeout-switch point, stop all nonessential discovery. The remaining allowed work is limited to:

- bind final exact-head application evidence;
- merge the validated application PR if atomic AIOC closeout remains credible;
- project `completed_verified` and retire implementation authority;
- select the strict successor without starting it unless separately authorized;
- validate the exact AIOC closeout head;
- merge the AIOC closeout;
- verify canonical main/post-merge health once.

Do not spend the reserve on broad scans, schema/tool rediscovery, successful-log dumps, speculative parallel-work review, cosmetic cleanup, repeated polling, or explanatory narration.

If required external validation latency alone causes the tranche to exceed target, record that separately from assistant/control overhead. If avoidable assistant operational noise causes or materially contributes to an overrun, classify it as a control-plane efficiency incident and repair the governing fast path rather than normalizing the overrun.

### 11.7 One-Continue priority

The one-Continue completion objective takes precedence over optional observability work. A status update, tool-call batch boundary, or already-green intermediate milestone never justifies consuming another owner turn. The executor must finish the bounded terminal gate or surface a genuine blocker with current evidence.
