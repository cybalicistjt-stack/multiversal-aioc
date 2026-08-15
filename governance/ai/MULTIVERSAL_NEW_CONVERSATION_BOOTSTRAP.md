# Multiversal New Conversation Bootstrap
## Mandatory Repository-First Session Recovery Protocol

**Document ID:** MV-AI-BOOTSTRAP-001  
**Version:** 5.6.2  
**Status:** ACTIVE  
**Owner and final authority:** John Brandon Turner  
**Governance repository:** `cybalicistjt-stack/multiversal-aioc`  
**Application repository:** `cybalicistjt-stack/Multiversal-app`  
**Last updated:** 2026-08-15

## Permanent owner entry point

The owner may start any new conversation with the unchanged one-line prompt stored at:

`governance/ai/MULTIVERSAL_STATIC_RESTART_PROMPT.txt`

The prompt contains no branch, work-item, date, or status information. All changing state must be recovered from repository evidence.

## Mandatory operating policy

Read and follow:

`governance/ai/MULTIVERSAL_CHECKPOINT_AND_VALIDATION_EFFICIENCY_POLICY.md`

and:

`governance/ai/MULTIVERSAL_COMPLETION_CLAIM_INTEGRITY_POLICY.md`

The checkpoint/validation policy controls checkpoint cadence, validation cadence, workflow isolation, and owner-facing reporting wherever it conflicts with older per-batch checkpoint language. Checkpoints are recovery boundaries, not activity logs.

The completion-claim integrity policy controls execution/completion reporting. Evidence must exist and be inspected before any material success claim. Artifact existence is not artifact completion. A failed required validation leaves the operation unfinished. When the owner says `Continue`, execute first; do not substitute an acknowledgement, plan, promise, or explanation.

## Access and permissions

The active assistant is authorized to use connected GitHub tools to read both canonical repositories, inspect files and repository evidence, create bounded branches, create and update files, open pull requests, inspect and repair CI, rerun validation, and merge verified work using a repository-permitted method.

This does not grant authority to spend money, enroll in paid plans, expose credentials, deploy production, publish publicly, approve release, or make irreversible vendor commitments without a separate owner gate.

## Fast mandatory initialization sequence

Perform this sequence before explaining, planning, or claiming work:

1. Verify connected read/write access and the authenticated GitHub identity against `governance/access/AIOC_CONTRIBUTOR_REGISTRY.json`.
2. Read this bootstrap from `main`.
3. Read both mandatory operating policies named above.
4. Read `governance/ai/runtime/CURRENT_WORK_POINTER.json` from `main` and its `mandatory_operating_policy` when present.
5. Read the checkpoint named by `primary_attempt_id` from `main`, then inspect that attempt's exact recorded branch and pull-request evidence. If the checkpoint exists on the recorded attempt branch, compare it with the `main` copy. A newer internally consistent branch checkpoint or substantive branch commit controls recovery until it is merged or explicitly superseded; do not discard newer branch state merely because `main` has an older projection.
6. Read `governance/ai/runtime/INTERACTION_OPERATIONAL_SCORECARD.json`. Treat it as the compact control-health projection; follow its source scorecard only when a pilot result, limitation, or regression needs inspection.
7. Inspect the latest commits, pull requests, reviews, and CI relevant to the checkpoint in both repositories, including repository evidence newer than the pointer's timestamp.
8. Read `governance/ci-failures/INDEX.md` from branch `ci/failure-records`; repair any current blocking failure before unrelated work. Historical recorded failures are not automatically current blockers; bind any blocker claim to the active attempt or current required gate.
9. Read `governance/ai/runtime/ROADMAP_INDEX.json` and only the governing roadmap section for the primary work item. If the primary work item is in CAPP, also read `governance/application-planning/character-appearance-production/CAPP_CHARACTER_APPEARANCE_PRODUCTION_PREPARATION_PROGRAM.md` and `CAPP_PROGRAM_BACKLOG.json` before execution. When a current or next Stage A item has a governed supplemental-authority reconciliation, read it before revalidating recovered historical preparation. For STAGE-A-A8 this remains mandatory historical provenance: `governance/application-planning/stage-a-a8/supplemental-authority/STAGE_A_A8_SUPPLEMENTAL_AUTHORITY_RECONCILIATION.md`; its source manifest and authority matrix remain part of A8 evidence. If `STAGE-A-A8-R0-attempt-001` is `completed_verified`, do not repeat the reconciliation. STAGE-A-A8 is now `COMPLETED_VERIFIED` through application PR #144 / verified squash `e9aaa858b345e6a29e27369c01468551752a2483` with closure receipt `Multiversal-app/receipts/STAGE-A-A8-CLOSURE.json`. The current next application operation is STAGE-A-A9 current-repository revalidation; A9 is not activated. For A9, inspect recovered `governance/stage-a-a9-preimplementation`, current post-A8 application truth, and PPIA-09/PPIA-10/PPIA-14/PPIA-15 authority before any activation.
10. If the active operation depends on owner-supplied archives, generated packages, binaries, exact publication bytes, screenshots, physical-device artifacts, or other external source material, inspect the actually available project/session sources before declaring an execution-surface blocker. Distinguish `source bytes unavailable`, `source bytes available but tool cannot transfer them`, `repository checkout unavailable`, and `validation/CI failure`; these are different recovery states.
11. Load additional canonical documents only when required by the active operation. Do not read or rewrite the full roadmap merely to save routine progress.
12. Run `python tools/continuity_state.py validate` when a usable checkout is available. When only connector access is available, verify the same pointer/checkpoint/branch/evidence invariants directly.

Repository evidence is authoritative over stale prose. A newer verified commit, pull request, CI run, checkpoint, or attempt-branch handoff controls; stale governance must be corrected through a bounded verified change.

## Branch-versus-main recovery rule

`main` is the canonical merged baseline, but an unfinished governed attempt may legitimately contain newer recovery evidence on its recorded branch.

When `CURRENT_WORK_POINTER.json` names an unfinished attempt:

1. read the `main` checkpoint;
2. inspect the exact branch named by that checkpoint/pointer;
3. compare the branch to `main` and identify newer checkpoint or substantive work commits;
4. prefer the newest internally consistent attempt evidence for resumption while preserving `main` as the last merged canonical baseline;
5. never reset, recreate, or overwrite the attempt merely because its branch is ahead of or diverged from `main`;
6. if branch and `main` contradict each other materially, stop unrelated mutation and reconcile continuity through a bounded governance change.

A branch checkpoint is not itself a completion claim. `completed_verified` still requires the declared completion evidence and merge boundary.

## Source-material and execution-surface rule

Do not collapse all file-access problems into a generic statement that a tool or interface "cannot do the work."

For any exact-byte, checksum-bound, binary, archive, or evidence-ingestion task, determine which condition actually applies:

- **source bytes unavailable:** the required owner/source artifact is not present in the current accessible sources;
- **source bytes available, transfer unavailable:** the exact source exists, but the active repository tool cannot ingest/copy it byte-for-byte;
- **repository checkout unavailable:** file-system operations or validators require a checkout not exposed on the current surface;
- **validation failed:** the bytes/work exist but a required deterministic or hosted gate failed;
- **owner gate required:** a genuine owner-only approval, spending, release, credential, production, or irreversible decision is required.

Never reconstruct exact-byte artifacts from truncated excerpts, paraphrase, regenerated prose, OCR, screenshots, or memory when checksum identity is part of the acceptance gate. Never invent missing checksums. If the required source becomes available on a later surface, re-evaluate the blocker instead of repeating an obsolete tool-limitation claim.

## Work-state interpretation

Only `completed_verified` is complete.

The following states are unfinished and must resume from `active_substep` and `next_action`:

- `started`
- `in_progress`
- `validation_failed`
- `blocked_non_owner`
- `blocked_owner`
- `ready_for_review`

`superseded` is not completion. It requires an explicit replacement attempt or disposition.

Never infer completion from a previous conversation ending, a long response, a generated file, a branch, a commit, a pull request, a green partial check, or silence. Completion requires every evidence kind and validation command declared in the checkpoint's `completion_gate`.

## Milestone-only checkpoint protocol

The owner must not manually copy, promote, or summarize progress between conversations.

For every governed operation:

1. Create a `started` checkpoint once before substantive mutation.
2. Keep branch commits bounded and meaningful, but do not rewrite the checkpoint after ordinary uninterrupted substeps.
3. During work, run the smallest relevant local or deterministic checks and batch related repairs.
4. Update the checkpoint only for a material handoff, a real blocker or changed recovery path, `ready_for_review`, or `completed_verified`.
5. Record failures as `validation_failed` or a typed blocked state only when the failure changes the recovery path or work must stop.
6. Record `ready_for_review` once after the complete package and declared local validation are finished.
7. Run the full declared hosted validation suite at the final package gate, not after every small mutation.
8. Record `completed_verified` only after required commit, pull request, review, CI, merge, artifact, checksum, file, or owner-decision evidence is present as declared.
9. A post-merge completion projection may be bundled with the next work item's start checkpoint; do not create a standalone completion-only pull request unless work is stopping or repository state would otherwise be contradictory.
10. Regenerate `governance/ai/runtime/CURRENT_IMPLEMENTATION_STATUS.json` only when the checkpoint or pointer changes at one of these milestone boundaries.
11. Never rewrite or delete a failed or interrupted attempt to make it appear complete. Create a new attempt ID for a genuinely new attempt.

If a conversation becomes unable to accept more messages, the latest pushed start or handoff checkpoint, substantive branch commits, and pull request are the handoff. The next conversation must resume that exact recorded state even when no final chat response exists.

## Material owner-correction protocol

When John explicitly corrects a behavior, claim, omission, or operating assumption:

1. repair or explicitly block the immediate work;
2. determine whether recurrence risk is material;
3. when material, capture a minimized correction record and proposed regression candidate through `tools/correction_regression.py`;
4. never publish raw message text, conversation titles, or attachment content;
5. never promote a candidate into the canonical evaluation extension without recorded owner approval and promotion evidence.

False or premature execution/completion claims are always material recurrence risks and must enter this lifecycle.

Correction capture is part of the work, not a separate reminder the owner must issue.

## Interaction-control health

`governance/ai/runtime/INTERACTION_OPERATIONAL_SCORECARD.json` is the compact AIOC view of the latest deterministic pilot. A passing scorecard means the installed repository controls passed their declared simulated scenarios. It does not prove long-term behavior in every interface. A null longitudinal intervention metric remains unmeasured and must not be described as improved without later evidence.

A historical passing scorecard is evidence of its recorded pilot run; it is not a live mirror of every later work-pointer selection. Routine pointer or status changes must not require pilot-scorecard regeneration. Re-run the pilot when its scenarios, controls, tool, scorecards, bootstrap integration, or operating amendment materially change.

If the scorecard is missing, failing, or contradicts its source scorecard for the recorded run, treat interaction control health as a blocking governance defect and repair it before relying on the affected control.

## Parallel-track safety

`CURRENT_WORK_POINTER.json` may record multiple attempts and deferred tracks, but it names exactly one primary attempt for conversational execution.

Starting a side mission must not mark another track complete, superseded, or abandoned. Paused and planned tracks remain explicit with their next work item and evidence. Changing the primary attempt is a pointer selection, not a rewrite of the underlying roadmap or checkpoints.

Application implementation authority may also be recorded canonically inside `cybalicistjt-stack/Multiversal-app` even while the AIOC conversational primary points to a governance/design side mission. A selected AIOC primary attempt does not by itself supersede the application repository's authorized current work order, and an application work order does not silently complete or discard the AIOC primary attempt.

CAPP — Character Appearance Production Preparation is an owner-approved parallel track that inherits completed PPIA-06 without reopening it. When CAPP is selected, recover its active work from `governance/application-planning/character-appearance-production/CAPP_PROGRAM_BACKLOG.json`, the CAPP checkpoint, exact branch/PR/CI evidence and the CAPP program document. Selecting CAPP does not activate or supersede STAGE-A-A2, DS-008, WP-011 / Apple work or any other retained track.

CAPP work is repository/governance production preparation unless a specific item explicitly requires a checkout or external exact bytes. Do not invent an A2-style checkout blocker for CAPP merely because A2 itself is checkout-blocked; evaluate the actual CAPP work item and available connector/source surface.

## Roadmap-performance rule

The full roadmap is a milestone and dependency authority, not an autosave file.

Routine substantive progress belongs in the work branch and pull request. Runtime state writes occur only at the milestone boundaries defined above.

Patch the full roadmap only when a work item becomes `completed_verified`, a milestone or dependency changes, scope changes, an owner decision changes the plan, or a material risk or release gate changes. Prefer a small affected-section patch or generated status block.

## Mandatory behavioral rules

### Execution first

- “Continue” means execute the exact next verified unfinished operation.
- Do not answer “Continue” with only an acknowledgement, plan, summary, restatement, promise, or explanation.
- Perform work in the current response; do not promise background work.
- Do not ask for confirmation where John has already authorized reversible work.
- Respond after an actual bounded result exists, or when a genuine blocker prevents further safe execution.

### Completion-claim integrity

- Evidence must exist and be inspected before a material success claim is made.
- Artifact existence is not artifact completion; inspect substantive contents against the promised scope.
- A failed required validator, assertion, tool action, integrity check, or CI gate leaves the operation unfinished.
- Never conceal an unresolved failure behind a later successful packaging or file-creation step.
- Previous assistant language is not completion evidence. Repository/tool evidence controls continuity.
- A truthful partial result is preferable to a polished unsupported completion claim.

### Truthfulness

- Never claim a file, commit, branch, pull request, review, merge, test, CI result, artifact, deployment, extraction, index, audit, validation, or completion without matching tool verification.
- Distinguish authority, permission, connector availability, source-material availability, repository-checkout availability, attempted action, and successful evidence.
- If a tool action fails, record the failure, repair it when possible, and continue.

### Approved recommendations

For ordinary reversible ambiguity, use the best evidence-backed recommendation and record the rationale. Stop only for a genuine owner-only decision, irreversible choice, spending, production credential, deployment, internal-alpha approval, or public-release gate.

### CI and verification

Use targeted checks during construction. Inspect failed final-gate jobs and logs, batch related repairs, and rerun the smallest applicable hosted set. Merge only when declared required checks pass and the pull request is mergeable. Use the repository-permitted merge method; `Multiversal-app` is squash-only.

## Reporting after a bounded step

Do not narrate every repository operation or validation poll. Report only verified facts needed by the owner when there is a material finding, genuine blocker, completed bounded package, final CI/merge result, or concise end-of-run status.

Include as applicable:

- work item;
- pull request and merge commit;
- actual changes;
- validation result;
- restrictions preserved;
- exact next action.

Every material status claim must have matching current execution or canonical-repository evidence behind it, even when that evidence is not dumped into the chat.

## Recovery fallback

If the pointer or checkpoint is missing, corrupt, contradictory, references unavailable evidence, or is materially older than the attempt branch it names:

1. stop unrelated mutation;
2. preserve the conflicting records;
3. reconstruct state from the named attempt branch, commits, pull requests, CI, the application current-work order, and the roadmap index;
4. inspect required external/project source availability when the operation is checksum- or artifact-bound;
5. create or update a recovery checkpoint marked unfinished without erasing the prior attempt;
6. validate and merge the correction when repository state itself is contradictory;
7. resume only after the recovery path has one deterministic primary state and an evidence-backed exact next action.
