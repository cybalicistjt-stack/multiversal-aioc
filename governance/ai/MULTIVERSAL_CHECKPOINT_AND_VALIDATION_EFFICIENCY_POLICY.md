# Multiversal Checkpoint and Validation Efficiency Policy

**Document ID:** MV-AI-EFFICIENCY-001  
**Version:** 1.1.0  
**Status:** ACTIVE — OWNER APPROVED  
**Owner and final authority:** John Brandon Turner  
**Effective:** 2026-08-13  

## 1. Purpose

This policy preserves reliable conversation recovery without allowing checkpoint bookkeeping, connector friction, or broad hosted validation to dominate the actual Multiversal work.

The continuity system exists to make restarts faster and safer. It must not require a repository checkpoint, status projection, scorecard regeneration, or full CI cycle after every small mutation.

This policy controls where it conflicts with earlier instructions requiring checkpoint updates after each atomic batch.

## 2. Milestone-only checkpoint rule

A governed work attempt receives a durable checkpoint only at these boundaries:

1. **Start:** once, before substantive work, recording the work item, branch, objective, exact active operation, and exact next action.
2. **Material handoff or blockage:** only when work must stop, the conversation may end before the package is finished, an owner decision is required, or a real failure changes the recovery path.
3. **Ready for review:** once, after the complete deliverable package and its targeted local validation are finished.
4. **Completed verified:** once, after required hosted validation and merge evidence exist.

Do not update checkpoints after ordinary file creation, edits, local checks, commits, validator repairs, or other uninterrupted substeps.

Substantive branch commits, pull-request evidence, and the work package itself provide intermediate history. The checkpoint is a recovery boundary, not an activity log.

## 3. No standalone completion-loop rule

A separate completion-only pull request is not required merely to copy merge evidence into runtime state.

After a package merges, its `completed_verified` projection may be recorded together with the next work item's start checkpoint. Create a standalone completion correction only when:

- work is stopping before the next item starts;
- the repository would otherwise have contradictory recovery state;
- a release, owner, security, or irreversible gate depends on the correction; or
- the completion record itself is materially defective.

When several dependency-ordered work items are intentionally built and validated as one owner-approved bounded tranche, project their final completion together rather than manufacturing one completion PR per item.

A completed package must still have verified final-head CI and merge evidence. This rule removes redundant validation cycles; it does not weaken completion evidence.

## 4. Build-first integrated run pattern

Unless a work item has an explicit incompatible gate, the default Multiversal run pattern is:

1. establish the bounded tranche and one start checkpoint;
2. build the entire bounded tranche before broad hosted review;
3. run targeted deterministic checks during construction;
4. perform integrated QA across the finished tranche;
5. batch related defects into one repair round;
6. rerun the integrated checks after the repair batch;
7. run one final read-only hosted gate on the finished exact head;
8. merge the verified package;
9. project completion once, bundled with the next start when practical.

Do not run a full hosted matrix after every item inside a deliberately integrated tranche. Do not turn validator wording or bookkeeping into a separate implementation loop.

## 5. Validation cadence

During uninterrupted work:

- run the smallest relevant local or deterministic checks;
- finish the complete bounded package before opening or refreshing hosted review;
- batch compatibility and validator repairs together;
- trigger the full declared hosted suite once on the finished package;
- when hosted validation finds multiple related issues, repair them as one batch and rerun once;
- do not create one commit and one full CI cycle per assertion.

The final hosted gate must be read-only. A validation workflow must not repair or rewrite the branch it is validating. If a hosted run identifies a defect, repair the branch first and then run the read-only gate again.

Full hosted validation remains mandatory at the final merge gate where declared by the work item.

## 6. Workflow isolation

Workflows must be scoped to the artifacts they validate.

- Continuity validation may run when checkpoints, pointers, status projections, or continuity tooling change.
- Feature validators may run when their feature artifacts, validator, workflow, or direct dependencies change.
- The interaction operational pilot may run when its pilot scenarios, scorecards, pilot tool, tests, bootstrap integration, or operating amendment change.
- Routine work-pointer or implementation-status changes must not force regeneration of the historical interaction pilot scorecard.
- Historical scorecards are evidence of their recorded run. They are not live mirrors of every later work-item selection.
- Validators that cover an in-progress lifecycle state must also accept the corresponding valid `completed_verified` state when the same artifacts remain valid after completion.

## 7. Connector and safety-wrapper routing

Repository evidence and project governance determine whether a Multiversal operation is valid. Platform-level connector safety wrappers are a separate execution surface and are not project authority.

For an authorized, reversible repository mutation:

1. attempt the smallest normal connector mutation once;
2. if the platform wrapper rejects that mutation without repository evidence of a project-policy defect, do not repeatedly reformulate or retry the same large write;
3. route the mutation through the repository-governed write bridge when the operation fits its allowlisted typed operations;
4. keep the connector-facing request small and semantic; perform coupled state changes inside the governed repository runner;
5. preserve final validation, PR, merge, signature, permission, privacy, provenance, checksum, and release gates exactly as before.

The governed bridge is not permission to bypass platform safeguards. It is the preferred project-side mechanism for expressing already-authorized structured repository changes with a smaller mutation surface.

If a merge API call loses its response, inspect PR/repository state before retrying. Prefer the minimal merge payload after verified green checks if optional metadata causes wrapper friction.

## 8. Roadmap and pointer writes

During a work item, do not repeatedly rewrite:

- the full application roadmap;
- the roadmap index;
- the current-work pointer;
- the compact status projection;
- historical pilot scorecards.

Update roadmap material only when scope, dependencies, owner decisions, milestone status, or final verified completion changes.

Update the current-work pointer when the selected work item changes, when a real handoff/block occurs, or at final completion—not for routine progress narration.

## 9. Conversation recovery guarantee

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

## 10. Owner-facing reporting

Do not narrate every repository operation or validation poll.

Report to the owner only when there is:

- a material finding that changes the approach;
- a genuine blocker or owner-only decision;
- a finished bounded package;
- final CI and merge evidence; or
- a concise end-of-run status.

## 11. Prohibited regressions

This policy does not authorize:

- false completion;
- skipping the final declared acceptance gate;
- hiding failed validation;
- deleting failed attempts;
- weakening permission, privacy, provenance, security, migration, checksum, or release controls;
- using a repository bridge to evade a platform safety restriction outside the authorized project mutation;
- paid services, production credentials, deployment, internal-alpha release, or public release without the existing owner gates.

## 12. Immediate application

Apply this policy to all new bounded Multiversal runs unless a more specific approved work-item contract requires a different cadence.

The CAPP-04 through CAPP-12 integrated production tranche is the reference execution pattern for build-first batching, integrated defect repair, one final read-only hosted gate, and one completion projection.
