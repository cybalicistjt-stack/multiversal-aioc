# Multiversal New Conversation Bootstrap
## Mandatory Repository-First Session Recovery Protocol

**Document ID:** MV-AI-BOOTSTRAP-001  
**Version:** 6.2.0  
**Status:** ACTIVE CANDIDATE — CRS COMPLETION PENDING  
**Owner and final authority:** John Brandon Turner  
**Governance repository:** `cybalicistjt-stack/multiversal-aioc`  
**Application repository:** `cybalicistjt-stack/Multiversal-app`  
**Last updated:** 2026-08-27

## Purpose

This file is a **stable recovery and execution protocol**, not a current-status document.

It must never contain a hard-coded claim about the current milestone, current work item, current PR, current branch, or exact next feature operation. Changing project state belongs in repository runtime state and live GitHub evidence.

The permanent owner entry point remains:

`governance/ai/MULTIVERSAL_STATIC_RESTART_PROMPT.txt`

## Authority lifecycle

Read and obey:

`governance/ai/MULTIVERSAL_AUTHORITY_AND_RETIREMENT_POLICY.md`

The canonical registry is:

`governance/ai/runtime/ACTIVE_AUTHORITY_REGISTRY.json`

Only material explicitly classified `CURRENT` may govern current work. `CURRENT_COMPATIBLE` material may support current work but cannot override canonical state. `HISTORICAL_INERT` and unregistered material remain provenance only and must not select work, impose a gate, or auto-execute merely because they still exist.

Repository evidence always outranks stale prose and prior assistant statements.

## Mandatory operating policies

Read all policies named by `CURRENT_WORK_POINTER.json`. At minimum the current policy set includes:

- `governance/ai/MULTIVERSAL_CHECKPOINT_AND_VALIDATION_EFFICIENCY_POLICY.md`
- `governance/ai/MULTIVERSAL_COMPLETION_CLAIM_INTEGRITY_POLICY.md`
- `governance/ai/MULTIVERSAL_SELF_HOSTED_FINAL_VALIDATION_POLICY.md`
- `governance/ai/MULTIVERSAL_AUTHORITY_AND_RETIREMENT_POLICY.md`

Also obey the owner interaction contract at:

`governance/ai/interaction-system/OWNER_AI_INTERACTION_CONTRACT.md`

Do not infer current status from examples embedded in older policies, conversation archives, or historical work packages.

## Fast mandatory initialization sequence

Perform this sequence before explaining, planning, or claiming current project state:

1. Verify connected read/write access to both canonical repositories and the authenticated identity when required by the contributor registry.
2. Read this bootstrap from AIOC `main`.
3. Read `governance/ai/runtime/ACTIVE_AUTHORITY_REGISTRY.json`.
4. Read `governance/ai/runtime/CURRENT_WORK_POINTER.json`.
5. Read the policies named by the pointer and the owner interaction contract.
6. Read the checkpoint named by `primary_attempt_id` and inspect its exact branch/PR/commit evidence.
7. Compare the pointer/checkpoint with **live GitHub state**. A pointer that names a closed PR, missing branch, superseded attempt, or contradictory head is a repository-health defect; do not continue unrelated feature work until it is reconciled.
8. Read `governance/ai/runtime/ROADMAP_INDEX.json` and only the roadmap/program/supplement paths named by the pointer/checkpoint for the active work. Do not load unrelated historical roadmap sections by default.
9. Inspect current blocking CI/failure evidence only when it is bound to the active attempt or its required gate. Historical failure records are not automatically current blockers.
10. If exact bytes, archives, screenshots, physical devices, generated packages, external credentials, or special hardware are required, inspect the actually available source/execution surface before declaring a blocker.
11. When a checkout is available, run the repository continuity/health validation named by current canonical governance. When only connector access is available, verify the same pointer → checkpoint → branch/PR → evidence invariants directly.
12. Resume the exact unfinished operation. Do not recreate completed work or revive historical authority.

## Owner command modes

Owner command meaning is stateful for the current turn and must not drift because an intermediate milestone is reached.

### `get ready`

`get ready` means **refresh and prepare only**:

1. re-read canonical runtime state and live repository evidence;
2. resolve the exact unfinished operation and any newly changed blockers;
3. prepare the execution path so the next `Continue` can start immediately;
4. do not begin substantive implementation unless the owner separately authorizes it.

After preparation is complete, wait.

### `Continue`

`Continue` means **execute the next verified unfinished implementation tranche as a whole**. It does not mean acknowledge, restate, plan, recap, ask whether to continue, or stop after one meaningful substep.

Unless a permitted stop condition in the termination preflight applies, carry the tranche through governed start if needed, implementation, focused validation and repair, exact-head final validation, required merge, `completed_verified` closeout, and canonical strict-successor selection.

### `status report and continue`

Give only the concise requested status, then immediately resume the same execution authority. The status request does not convert the turn to status-only mode.

### `keep going`, `continue until you need me`, `finish <program/tranche>`

These phrases extend execution across successive bounded units to the named boundary. After one tranche reaches `completed_verified`, select and execute the next authorized unit automatically until:

- the named program/tranche boundary is complete;
- a permitted stop condition occurs; or
- the owner supplies a newer command that changes the boundary.

A later status question such as whether work is still progressing does not silently cancel this keep-going mode; answer briefly and resume unless the owner explicitly changes or stops execution.

## Current-state prohibition

This bootstrap must not be patched merely because a work item completes or the next work item changes.

Specifically prohibited in this file:

- `the current next operation is ...` status prose;
- current PR numbers or branch heads;
- current Stage/Tranche completion summaries;
- dated current-state amendments used as parallel authority;
- hard-coded migration numbers or exact feature baselines that belong to one lifecycle stage;
- instructions to read a historical supplement unless the pointer/registry currently names it.

Those facts belong in the pointer, checkpoint, roadmap index, authority registry, and live GitHub evidence.

## Work-state interpretation

Only `completed_verified` is complete.

Started, in-progress, quarantined, blocked, ready-for-review, and validation-failed states are unfinished unless a governing policy explicitly defines a different terminal state.

Never infer completion from a conversation ending, a generated artifact, a branch, a commit, an open PR, a partial green check, silence, an old completion projection, implementation completion alone, or a required validation job merely being queued or running.

## Execution loop

During an execution command, use this loop until the bounded unit reaches a permitted termination condition:

1. **Recover** the exact checkpoint, branch, PR, and live head.
2. **Act** on the exact unfinished operation.
3. **Validate** with the smallest relevant construction check.
4. **Repair** only evidence-backed failures; do not invent defects to justify stopping.
5. **Poll or work around normal latency** for required asynchronous checks already in flight. Reuse the existing exact-head run when it remains valid.
6. **Run the declared exact-head final gate** at the package boundary.
7. **Merge** when all required evidence is green and merge authority exists.
8. **Close out** with `completed_verified` evidence and canonical state projection.
9. **Select the strict successor** required by the governing roadmap.
10. If a keep-going command is active, continue into the next authorized bounded unit.

Normal GitHub Actions queue time, a running comparator, a running governance audit, an open/mergeable PR, or closeout work still to be written are **intermediate states**, not reasons to return control to the owner.

## Final-response termination preflight

Before sending a final owner-facing response from an execution turn, answer these questions against live evidence:

1. Is the requested bounded unit `completed_verified` and, when required, is its strict successor selected?
2. If not, is there a **genuine blocker** that survived reasonable recovery attempts and prevents any further authorized execution now?
3. If neither is true, did the owner explicitly request a non-execution mode such as status-only, analysis-only, or `get ready` preparation-only?

A final response is allowed only when at least one answer is **yes**.

If all three answers are **no**, continue using tools. Do not finalize merely because:

- implementation code is written;
- a commit or PR exists;
- Linux or Windows validation is green while another required gate remains;
- deterministic comparison is queued/running;
- a governance closeout audit is queued/running;
- merge is still pending;
- closeout projection is still pending;
- a useful status summary can be written;
- one tool-call batch has ended.

Never use a final response to say that work is “continuing” while actually returning control with executable authorized work remaining.

## Reversible ambiguity rule

Standing owner authority covers ordinary reversible implementation choices inside the currently governed scope. When several safe, in-scope choices are possible, choose the option best supported by canonical architecture, current evidence, and least irreversible impact; record the decision where material and continue.

Do not interrupt the owner for reversible ambiguity merely to transfer decision burden. Ask only when the decision crosses an owner-only boundary or materially changes approved scope.

## Branch-versus-main recovery

`main` is the last merged canonical baseline. An unfinished attempt branch may contain newer valid work/evidence.

When the pointer names an unfinished attempt:

1. inspect the `main` checkpoint/pointer;
2. inspect the exact named attempt branch and PR;
3. compare branch evidence with `main`;
4. preserve newer internally consistent attempt work;
5. never let an unregistered historical branch override the pointer;
6. reconcile contradictions through a bounded repository-health change before unrelated work.

## PR lifecycle

A work item may have only one authoritative active integration path.

- Superseded PRs must be closed with preservation/supersession evidence.
- Closed PRs cannot be selected as current work.
- Preserved dormant/special-environment PRs must be explicitly registered as non-authoritative until their activation condition is met.
- Open PR age or existence does not imply current authority.
- PR readiness is not an execution stop condition when merge/closeout work remains authorized.

## Workflow and validator lifecycle

Before relying on an old workflow or validator:

1. verify it is registered for current use;
2. verify its lifecycle assumptions still match current repository state;
3. verify it uses the current validation policy/core or a registered exception;
4. do not weaken a correct historical validator simply to make it pass against a later lifecycle state—retire it from current paths instead;
5. historical workflows must not auto-trigger.

For application/package final validation, use exact-head self-hosted Windows/Linux lanes and deterministic cross-platform evidence when applicable. GitHub-hosted compute is not a generic project-wide final requirement.

## Async validation versus environment blocker

Queued or running work is not by itself a blocker. Before classifying a required self-hosted gate as unavailable:

1. inspect the exact job/run status and required labels;
2. inspect whether a runner has claimed work when that evidence is exposed;
3. check whether related required jobs are progressing;
4. poll existing exact-head work for a reasonable interval;
5. use available repository or execution-surface recovery paths without changing the candidate unnecessarily.

Only preserve an environment blocker when evidence shows the required execution surface is unavailable or cannot make progress and no authorized recovery path remains. Preserve the exact candidate and recovery point rather than manufacturing a new candidate merely to retrigger CI.

## Source-material and execution-surface rule

Distinguish precisely among:

- source bytes unavailable;
- source bytes available but transfer unavailable;
- repository checkout unavailable;
- validation failure;
- normal asynchronous validation latency;
- runner/environment failure;
- owner-only gate.

Never reconstruct checksum-bound exact artifacts from excerpts, memory, OCR, or paraphrase.

## Checkpoint discipline

Checkpoints are recovery boundaries, not activity logs.

- Create one start checkpoint before substantive mutation.
- Update only on material handoff, blocker/recovery-path change, ready-for-review, or `completed_verified`.
- Run focused checks during construction and the declared exact-head gate at the final package boundary.
- Never rewrite a failed/interrupted attempt to make it appear complete.
- A post-merge projection may be bundled with the next work start; avoid gratuitous closure-only churn unless state would otherwise be contradictory.

## Owner operating rule

When John says `Continue`, execute the next verified unfinished **implementation tranche as a whole**. Do not substitute an acknowledgement, plan, promise, recap, or unnecessary clarification.

Unless a genuine owner-only, unavailable-environment, unavailable-source, safety, or irrecoverable external blocker prevents completion, `Continue` means carry that tranche through its governed start if needed, implementation, focused repair, exact-head validation, required merge, `completed_verified` closeout, and canonical selection of its strict successor. Do **not** stop merely because validation is queued/in progress, a PR is open/ready, a closeout is pending, or the successor could be queued as an interstitial step. Poll/work around normal validation latency and finish the bounded tranche before reporting.

Perform work in the current response. If work remains incomplete because a genuine blocker survives reasonable recovery attempts, say so truthfully and preserve the exact recovery point in repository evidence.

## Completion-claim integrity

- Evidence must exist and be inspected before claiming success.
- Artifact existence is not artifact completion.
- A required failed gate leaves the operation unfinished.
- Previous assistant language is not evidence.
- Previous conversation archives are behavioral/provenance evidence, not current implementation authority.
- Truthful partial completion is preferable to unsupported closure.

## Stop-the-line repository-health rule

If stale governance, a retired validator, an unregistered workflow, a superseded PR, or contradictory runtime state can materially alter work selection or validation outcome, treat that as a repository-health defect. Repair or explicitly quarantine the common defect before continuing unrelated feature completion.

Do not repeatedly patch the same class of stale infrastructure inside individual feature tranches.

## Reporting

Report verified bounded results, material findings, genuine blockers, final CI/merge evidence, and the exact next action. Avoid low-level narration and repeated polling in owner-facing prose.

During execution, tool use may continue for many internal steps without intermediate owner narration. A brief progress update does not end the execution command and must not substitute for the termination preflight.

## Recovery fallback

If the pointer/registry/checkpoint is missing, contradictory, or materially stale:

1. stop unrelated mutation;
2. preserve conflicting records;
3. reconstruct state from current `main`, named attempt branches, PRs, commits, CI/artifacts, roadmap index, and owner-approved decisions;
4. classify stale material under the authority lifecycle policy;
5. repair canonical state through a bounded repository-health change;
6. only then resume production work.
