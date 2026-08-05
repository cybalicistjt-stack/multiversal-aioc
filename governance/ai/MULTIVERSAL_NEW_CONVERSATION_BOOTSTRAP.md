# Multiversal New Conversation Bootstrap
## Mandatory Repository-First Session Recovery Protocol

**Document ID:** MV-AI-BOOTSTRAP-001  
**Version:** 5.0.0  
**Status:** ACTIVE  
**Owner and final authority:** John Brandon Turner  
**Governance repository:** `cybalicistjt-stack/multiversal-aioc`  
**Application repository:** `cybalicistjt-stack/Multiversal-app`  
**Last updated:** 2026-08-05

## Permanent owner entry point

The owner may start any new conversation with the unchanged one-line prompt stored at:

`governance/ai/MULTIVERSAL_STATIC_RESTART_PROMPT.txt`

The prompt contains no branch, work-item, date, or status information. All changing state must be recovered from repository evidence.

## Access and permissions

The active assistant is authorized to use connected GitHub tools to read both canonical repositories, inspect files and repository evidence, create bounded branches, create and update files, open pull requests, inspect and repair CI, rerun validation, and merge verified work using a repository-permitted method.

This does not grant authority to spend money, enroll in paid plans, expose credentials, deploy production, publish publicly, approve release, or make irreversible vendor commitments without a separate owner gate.

## Fast mandatory initialization sequence

Perform this sequence before explaining, planning, or claiming work:

1. Verify connected read/write access and the authenticated GitHub identity against `governance/access/AIOC_CONTRIBUTOR_REGISTRY.json`.
2. Read this bootstrap from `main`.
3. Read `governance/ai/runtime/CURRENT_WORK_POINTER.json`.
4. Read the checkpoint named by `primary_attempt_id` and its exact branch or pull-request evidence.
5. Inspect the latest commits, pull requests, reviews, and CI relevant to that checkpoint in both repositories.
6. Read `governance/ci-failures/INDEX.md` from branch `ci/failure-records`; repair any current blocking failure before unrelated work.
7. Read `governance/ai/runtime/ROADMAP_INDEX.json` and only the governing roadmap section for the primary work item.
8. Load additional canonical documents only when required by the active operation. Do not read or rewrite the full roadmap merely to save routine progress.
9. Run `python tools/continuity_state.py validate` when a usable checkout is available. When only connector access is available, verify the same pointer/checkpoint/evidence invariants directly.

Repository evidence is authoritative over stale prose. A newer verified commit, pull request, CI run, or checkpoint controls; stale governance must be corrected through a bounded verified change.

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

## Automatic checkpoint protocol

The owner must not manually copy, promote, or summarize progress between conversations.

For every governed operation:

1. Create or update a `started` checkpoint before substantive mutation.
2. Keep no more than one atomic mutation batch uncommitted.
3. After each atomic batch, run the smallest relevant checks, update the checkpoint with optimistic `revision` matching, commit, and push.
4. Record failures as `validation_failed` or a typed blocked state with exact evidence and next action.
5. Record `ready_for_review` only after implementation and declared local validation are complete.
6. Record `completed_verified` only after required commit, pull request, review, CI, merge, artifact, checksum, file, or owner-decision evidence is present as declared.
7. Regenerate `governance/ai/runtime/CURRENT_IMPLEMENTATION_STATUS.json` with `python tools/continuity_state.py refresh-status` after checkpoint or pointer changes.
8. Never rewrite or delete a failed or interrupted attempt to make it appear complete. Create a new attempt ID for a genuinely new attempt.

If a conversation becomes unable to accept more messages, the latest pushed checkpoint and branch are the handoff. The next conversation must resume that exact recorded state even when no final chat response exists.

## Parallel-track safety

`CURRENT_WORK_POINTER.json` may record multiple attempts and deferred tracks, but it names exactly one primary attempt for conversational execution.

Starting a side mission must not mark another track complete, superseded, or abandoned. Paused and planned tracks remain explicit with their next work item and evidence. Changing the primary attempt is a pointer selection, not a rewrite of the underlying roadmap or checkpoints.

## Roadmap-performance rule

The full roadmap is a milestone and dependency authority, not an autosave file.

Routine progress writes go only to:

- the active checkpoint;
- the current-work pointer when selection changes;
- the compact generated status record;
- the work branch and pull request.

Patch the full roadmap only when a work item becomes `completed_verified`, a milestone or dependency changes, scope changes, an owner decision changes the plan, or a material risk or release gate changes. Prefer a small affected-section patch or generated status block.

## Mandatory behavioral rules

### Execution first

- “Continue” means execute the exact next verified unfinished operation.
- Do not answer “Continue” with only a plan, summary, or restatement.
- Perform work in the current response; do not promise background work.
- Do not ask for confirmation where John has already authorized reversible work.

### Truthfulness

- Never claim a file, commit, branch, pull request, review, merge, test, CI result, artifact, deployment, or completion without tool verification.
- Distinguish authority, permission, connector availability, attempted action, and successful evidence.
- If a tool action fails, record the failure, repair it when possible, and continue.

### Approved recommendations

For ordinary reversible ambiguity, use the best evidence-backed recommendation and record the rationale. Stop only for a genuine owner-only decision, irreversible choice, spending, production credential, deployment, internal-alpha approval, or public-release gate.

### CI and verification

Inspect failed jobs and logs, repair root causes, and rerun or trigger validation. Merge only when declared required checks pass and the pull request is mergeable. Use the repository-permitted merge method; `Multiversal-app` is squash-only.

## Reporting after a bounded step

Report only verified facts needed by the owner:

- work item;
- pull request and merge commit when applicable;
- actual changes;
- validation or CI result;
- restrictions preserved;
- exact next action.

## Recovery fallback

If the pointer or checkpoint is missing, corrupt, contradictory, or references unavailable evidence:

1. stop mutation;
2. preserve the conflicting records;
3. reconstruct state from branches, commits, pull requests, CI, and the roadmap index;
4. create a recovery checkpoint marked unfinished;
5. validate and merge the correction;
6. resume only after the repository again has one deterministic primary state.
