# Multiversal Owner–AI Continuity and Interaction System

**Version:** 0.1.0  
**Status:** Owner-approved design foundation; canonical repository integration pending  
**Owner and final authority:** John Brandon Turner

## 1. Purpose

This system prevents conversation boundaries, context limits, tool interruptions, stale roadmaps, or incomplete steps from causing Multiversal work to be lost, repeated, or falsely treated as complete.

It converts continuity from a conversational habit into a repository-backed operating contract.

## 2. Owner-approved hard requirements

1. Starting a new conversation must require one static prompt that never needs work-item numbers, dates, branch names, copied summaries, or manual handoffs.
2. A conversation reaching its message or context limit must not erase completed or partially completed work.
3. A step that stopped halfway must remain visibly unfinished. A later conversation must not infer completion from silence, a summary, or a planned end state.
4. Progress preservation must occur automatically as part of execution. The owner must not manually promote, copy, or reconstruct ordinary progress.
5. Large roadmap edits must not be used as the high-frequency progress store.
6. Roadmap maintenance must be minimized without allowing current state to become ambiguous or stale.
7. “Complete” is an evidence-gated state, not conversational wording.

## 3. Permanent restart command

The file `MULTIVERSAL_STATIC_RESTART_PROMPT.txt` contains the canonical one-line restart prompt.

The prompt is deliberately static. Dynamic information—current work, permissions, branches, failures, next actions, and owner decisions—belongs in the bootstrap, contributor registry, active-work pointer, checkpoints, repository history, pull requests, and CI.

This means the owner never needs to edit the restart prompt when the project advances.

## 4. Continuity architecture

### 4.1 Dual-channel preservation

Every active operation uses two persistence channels:

1. **Work preservation:** code, documentation, tests, schemas, or artifacts are committed and pushed to the active work branch after each bounded atomic batch.
2. **State preservation:** a compact machine-readable checkpoint records the exact verified state, active substep, next action, validation status, failures, and evidence.

A progress claim without pushed work or other durable evidence is not preserved progress.

### 4.2 One atomic batch maximum

The executor must not hold more than one bounded successful mutation batch without committing and pushing it.

After each atomic batch:

1. run the smallest relevant validation;
2. update the checkpoint;
3. commit the work and checkpoint together where practical;
4. push the branch;
5. continue automatically.

Before a long-running, failure-prone, or context-heavy operation, the executor first pushes the current checkpoint.

This cannot preserve an individual edit interrupted before the tool successfully writes it, but it limits possible loss to the current atomic batch rather than the entire conversation.

### 4.3 Initial STARTED checkpoint

Before substantial work begins, the executor creates and pushes a `started` checkpoint.

The initial checkpoint records:

- work-item ID;
- attempt ID;
- primary repository;
- branch;
- base commit;
- exact objective;
- first active substep;
- exact next action.

If the conversation ends immediately afterward, the next conversation still knows that the item began and was not completed.

### 4.4 Status model

Only these states are used:

- `started`
- `in_progress`
- `validation_failed`
- `blocked_non_owner`
- `blocked_owner`
- `ready_for_review`
- `completed_verified`
- `superseded`

Only `completed_verified` means complete.

Terms such as “implementation written,” “tests pending,” “PR open,” “review requested,” or “merge pending” remain non-complete states.

### 4.5 Completion gate

A checkpoint may enter `completed_verified` only when its registered work-type gate is satisfied.

Examples of evidence include:

- merged commit;
- exact-head pull-request review;
- required CI success;
- generated artifact and checksum;
- required validation report;
- owner approval when the work type requires it.

The checkpoint must set `active_substep` to `none` and identify the next work item or owner-only boundary.

## 5. New-conversation recovery algorithm

When the static prompt is used, the new conversation must:

1. verify access to both canonical repositories;
2. read the canonical bootstrap and contributor authority;
3. read the small current-work pointer;
4. inspect the active repository and branch;
5. load the latest checkpoint from the branch or operational ledger;
6. compare the checkpoint with commits, PRs, CI, and merged repository evidence;
7. treat any state other than `completed_verified` as unfinished;
8. resume the checkpoint’s exact `active_substep` or `next_action`;
9. repair ordinary failures automatically;
10. stop only for a true owner-only, prohibited, credential, spending, production, public-release, or irreversible gate.

A final assistant message, chat summary, or roadmap checkbox is supporting context only. It cannot override newer verified checkpoint and repository evidence.

## 6. Recovery from interrupted work

### Case A — Work started, no implementation yet

The checkpoint remains `started`. The next conversation resumes the first active substep.

### Case B — Files changed and pushed, tests not run

The checkpoint remains `in_progress` and says validation is pending. The next conversation inspects the pushed diff, runs validation, and continues.

### Case C — Tests failed

The failure output and command are recorded. The state becomes `validation_failed`. The next conversation repairs the failure; it does not restart the whole work item or skip it.

### Case D — PR opened but not merged

The state is `ready_for_review` or `in_progress`. The work is not complete. The next conversation checks review and CI, repairs failures, and completes the governed merge path.

### Case E — Conversation claimed completion without evidence

The completion gate rejects the claim. The next conversation treats the item as unfinished and reconciles the record.

### Case F — Roadmap and checkpoint disagree

Newer verified repository and checkpoint evidence controls operational recovery. The discrepancy is recorded, and the roadmap projection is queued for a bounded update.

## 7. Fast operational state versus the roadmap

### 7.1 Roadmap role

`APPLICATION_IMPLEMENTATION_ROADMAP.md` remains the controlling plan, dependency order, acceptance-gate map, and milestone narrative.

It is not the high-frequency execution ledger.

### 7.2 Fast files

The system introduces small operational records:

- `CURRENT_WORK_POINTER.json` — identifies the active work item, repository, branch, attempt, and checkpoint location.
- `AI_WORK_CHECKPOINT...json` — records the exact in-progress state.
- `CURRENT_IMPLEMENTATION_STATUS.json` — a generated summary of completed boundary, active item, next item, blockers, and latest evidence.
- `ROADMAP_INDEX.json` — maps work-item IDs to dependencies and the relevant roadmap section.

### 7.3 Roadmap update frequency

The full roadmap is patched only when one of these occurs:

- a work item reaches `completed_verified`;
- a milestone or tranche boundary changes;
- execution order or dependencies change;
- an owner decision changes scope;
- a material risk, deferral, or release gate changes.

Ordinary substeps and test repairs update only the checkpoint and operational status.

### 7.4 Generated status block

The roadmap should contain a small bounded block:

```text
<!-- BEGIN GENERATED CURRENT STATUS -->
...
<!-- END GENERATED CURRENT STATUS -->
```

Automation replaces only that block and any directly affected work-item status lines. It must not rewrite or reread the entire roadmap merely to save ordinary progress.

### 7.5 Bootstrap context optimization

The bootstrap reads:

1. the small current-work pointer;
2. the exact checkpoint;
3. the relevant roadmap index entry and bounded roadmap section;
4. recent repository evidence.

The full roadmap is loaded only when planning changes, dependency ambiguity, or milestone review requires it.

## 8. Automated progress-saving triggers

A checkpoint and push are required:

- immediately after work-item activation;
- after every successful atomic mutation batch;
- before a long test, migration, bulk conversion, or large generation operation;
- immediately after a validation failure;
- when an ordinary blocker is discovered;
- before requesting an owner decision;
- before opening or updating a PR;
- after CI or review changes the state;
- immediately before the final user-facing completion report.

No owner action is required for these saves.

## 9. Active Work Ledger

A lightweight append-only GitHub operational ledger may supplement checkpoint files.

Each ledger event records:

- work-item and attempt IDs;
- event type;
- repository and branch;
- pushed commit;
- status;
- active substep;
- next action;
- validation evidence;
- owner-decision boundary if any.

The ledger is optimized for fast recovery and history. Final authority remains the verified repository, merged commits, tests, and governed records.

## 10. Idempotency and duplicate-conversation safety

Every work attempt has a stable attempt ID.

When two conversations or agents encounter the same active attempt, they must:

1. inspect the latest remote checkpoint;
2. avoid creating a second attempt unless the first is superseded;
3. use expected-commit or expected-revision checks before updating state;
4. stop and reconcile if another executor advanced the branch.

This prevents duplicate work and stale overwrites.

## 11. Failure and truthfulness rules

The executor must never say that progress was saved, pushed, merged, validated, or completed unless the cited evidence exists.

If repository access fails, it must state that durable project progress could not be saved through the canonical mechanism. It must not substitute conversational memory and call the work preserved.

If a checkpoint write succeeds but a work push fails, the state must report that implementation bytes are not yet durable.

## 12. Proposed repository layout

```text
multiversal-aioc/
  governance/ai/
    MULTIVERSAL_NEW_CONVERSATION_BOOTSTRAP.md
    interaction-system/
      OWNER_AI_INTERACTION_CONTRACT.md
      WORK_CHECKPOINT.schema.json
      CONTINUITY_ACCEPTANCE_TESTS.md
    runtime/
      CURRENT_WORK_POINTER.json
      CURRENT_IMPLEMENTATION_STATUS.json
      ROADMAP_INDEX.json

Multiversal-app or active work repository branch/
  .multiversal/
    work-state/
      <attempt-id>.json
```

A finalized implementation may adjust paths to fit existing repository conventions, but the separation of static bootstrap, fast pointer, branch checkpoint, and roadmap projection is mandatory.

## 13. Acceptance tests

1. A blank new conversation using only the static prompt locates the canonical bootstrap and active checkpoint.
2. A `started` item is resumed, not skipped.
3. An `in_progress` item is not reported as complete.
4. A pushed partial implementation with pending tests resumes at validation.
5. A failed test resumes from the failure with the original command and evidence.
6. An open PR is not treated as merged.
7. A completion claim without evidence is rejected.
8. A stale roadmap does not cause a newer active checkpoint to be ignored.
9. A merged item with a pending roadmap projection still resolves the correct next task.
10. Two simultaneous conversations cannot silently overwrite the same attempt.
11. A conversation ending after any checkpoint loses at most the current uncommitted atomic batch.
12. Roadmap update work is bounded to the generated status block and affected status entries.
13. The owner is never required to copy a handoff or manually promote progress.
14. Repository-access failure produces an explicit unsaved-state warning rather than a false continuity claim.

## 14. Integration sequence within the approved twelve-step program

The new requirements are incorporated as follows:

1. Normalize the archive and establish hashes. **Started in this package.**
2. Build the interaction timeline.
3. Segment interaction episodes.
4. Create the failure and friction taxonomy.
5. Extract successful patterns.
6. Compare behavior with the Project Bible.
7. Finalize the Owner–AI Interaction Contract.
8. Finalize the conversation and execution state model. **Foundation included here.**
9. Implement startup, continuation, checkpoint, and recovery controls.
10. Implement evidence, coverage, deliverable, and roadmap-projection gates.
11. Build the training and evaluation suite.
12. Pilot, measure, integrate, and update the bootstrap, AIOC, and Project Bible.

## 15. Current completion boundary

This package provides:

- a normalized message corpus;
- source hashes and counts;
- the approved continuity requirements;
- the permanent static restart prompt;
- a checkpoint schema and examples;
- the recovery and roadmap-optimization design;
- initial acceptance tests.

It does not claim that these controls are already installed in the canonical repositories or enforced by CI. Repository implementation belongs to later steps of the approved program.
