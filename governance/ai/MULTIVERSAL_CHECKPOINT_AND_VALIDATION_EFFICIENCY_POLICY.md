# Multiversal Checkpoint and Validation Efficiency Policy

**Document ID:** MV-AI-EFFICIENCY-001  
**Version:** 1.1.0  
**Status:** ACTIVE — OWNER APPROVED  
**Owner and final authority:** John Brandon Turner  
**Effective:** 2026-08-06  
**Updated:** 2026-08-18

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
