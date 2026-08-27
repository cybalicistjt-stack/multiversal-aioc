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

This file is a **stable recovery protocol**, not a current-status document.

It must never contain a hard-coded claim about the current milestone, current work item, current PR, current branch, or exact next feature operation. Changing project state belongs in repository runtime state and live GitHub evidence.

The permanent owner entry point remains:

`governance/ai/MULTIVERSAL_STATIC_RESTART_PROMPT.txt`

## Authority lifecycle

Read and obey:

`governance/ai/MULTIVERSAL_AUTHORITY_AND_RETIREMENT_POLICY.md`

The canonical registry is:

`governance/ai/runtime/ACTIVE_AUTHORITY_REGISTRY.json`

Only material explicitly classified `CURRENT` may govern current work. `CURRENT_COMPATIBLE` material may support current work but cannot override canonical state. `HISTORICAL_INERT` and unregistered material remain provenance only and must not select work, impose a gate, or auto-execute merely because they still exist.

Repository evidence always outranks stale prose.

## Mandatory operating policies

Read all policies named by `CURRENT_WORK_POINTER.json` and all `CURRENT` operating policies in the authority registry. At minimum the stable operating-policy set includes:

- `governance/ai/MULTIVERSAL_CHECKPOINT_AND_VALIDATION_EFFICIENCY_POLICY.md`
- `governance/ai/MULTIVERSAL_COMPLETION_CLAIM_INTEGRITY_POLICY.md`
- `governance/ai/MULTIVERSAL_SELF_HOSTED_FINAL_VALIDATION_POLICY.md`
- `governance/ai/MULTIVERSAL_AUTHORITY_AND_RETIREMENT_POLICY.md`
- `governance/ai/MULTIVERSAL_EXECUTION_CONVERGENCE_POLICY.md`

Do not infer current status from examples embedded in older policies or historical work packages.

## Fast mandatory initialization sequence

Perform this sequence before explaining, planning, or claiming current project state:

1. Verify connected read/write access to both canonical repositories and the authenticated identity when required by the contributor registry.
2. Read this bootstrap from AIOC `main`.
3. Read `governance/ai/runtime/ACTIVE_AUTHORITY_REGISTRY.json`.
4. Read `governance/ai/runtime/CURRENT_WORK_POINTER.json`.
5. Read the policies named by the pointer and the `CURRENT` operating policies in the authority registry.
6. Read the checkpoint named by `primary_attempt_id` and inspect its exact branch/PR/commit evidence.
7. If the active attempt has implementation authority, recover its `convergence_control` counters, failure classification, diagnostic hypotheses and retry basis. These values are repository state and do not reset because the conversation changed.
8. Compare the pointer/checkpoint with **live GitHub state**. A pointer that names a closed PR, missing branch, superseded attempt, or contradictory head is a repository-health defect; do not continue unrelated feature work until it is reconciled.
9. Read `governance/ai/runtime/ROADMAP_INDEX.json` and only the roadmap/program/supplement paths named by the pointer/checkpoint for the active work. Do not load unrelated historical roadmap sections by default.
10. Inspect current blocking CI/failure evidence only when it is bound to the active attempt or its required gate. Historical failure records are not automatically current blockers.
11. Inspect the live execution-convergence scorecard when evaluating repeated owner continuations, repair loops, retry behavior, or validation-scope performance. Do not substitute the historical deterministic interaction pilot for live throughput evidence.
12. If exact bytes, archives, screenshots, physical devices, generated packages, external credentials, or special hardware are required, inspect the actually available source/execution surface before declaring a blocker.
13. When a checkout is available, run the repository continuity/health validation named by current canonical governance. When only connector access is available, verify the same pointer → checkpoint → branch/PR → evidence invariants directly.
14. Resume the exact unfinished operation. Do not recreate completed work, reset convergence counters, or revive historical authority.

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

Never infer completion from a conversation ending, a generated artifact, a branch, a commit, an open PR, a partial green check, silence, or an old completion projection.

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

## Workflow and validator lifecycle

Before relying on an old workflow or validator:

1. verify it is registered for current use;
2. verify its lifecycle assumptions still match current repository state;
3. verify it uses the current validation policy/core or a registered exception;
4. do not weaken a correct historical validator simply to make it pass against a later lifecycle state—retire it from current paths instead;
5. historical workflows must not auto-trigger;
6. ordinary substantive application/package work must select the one governed current-tranche Validation Core profile rather than automatically invoking completed historical profiles.

For application/package final validation, use exact-head self-hosted Windows/Linux lanes and deterministic cross-platform evidence when applicable. GitHub-hosted compute is not a generic project-wide final requirement.

## Source-material and execution-surface rule

Distinguish precisely among:

- source bytes unavailable;
- source bytes available but transfer unavailable;
- repository checkout unavailable;
- validation failure;
- validation-contract failure;
- validation-infrastructure failure;
- runner/environment failure;
- repository-state failure;
- owner-only gate.

Never reconstruct checksum-bound exact artifacts from excerpts, memory, OCR, or paraphrase.

## Checkpoint discipline

Checkpoints are recovery boundaries, not activity logs.

- Create one start checkpoint before substantive mutation.
- Update only on material handoff, blocker/recovery-path change, ready-for-review, or completed_verified.
- Run focused checks during construction and the declared exact-head gate at the final package boundary.
- Never rewrite a failed/interrupted attempt to make it appear complete.
- A post-merge projection may be bundled with the next work start; avoid gratuitous closure-only churn unless state would otherwise be contradictory.
- Implementation attempts must preserve monotonic convergence counters across conversations.
- A retry after failure must record what materially changed; an identical rerun is not progress.
- A second related repair requires diagnostic mode, failure classification and falsifiable root-cause hypotheses before another final rerun.
- Two no-progress cycles require an explicit control-plane, environment or owner blocker, or a diagnostic change to the retry basis.

## Owner operating rule

When John says `Continue`, execute the next verified unfinished **implementation tranche as a whole**. Do not substitute an acknowledgement, plan, promise, recap, or unnecessary clarification.

Unless a genuine owner-only, unavailable-environment, unavailable-source, safety, or irrecoverable external blocker prevents completion, `Continue` means carry that tranche through its governed start (if needed), implementation, focused repair, exact-head validation, required merge, `completed_verified` closeout, and canonical selection of its strict successor. Do **not** stop merely because validation is queued/in progress, a PR is open/ready, a closeout is pending, or the successor could be queued as an interstitial step. Poll/work around normal validation latency and finish the bounded tranche before reporting.

A repeated `Continue` on the same ordinary tranche is an execution-cost signal. Do not consume another owner turn merely to rediscover the same state or repeat an unchanged validation attempt. Follow the execution-convergence policy: classify the failure, diagnose by the second related repair, and block explicitly rather than entering an unbounded retry loop.

Perform work in the current response. If work remains incomplete because a genuine blocker survives reasonable recovery attempts, say so truthfully and preserve the exact recovery point in repository evidence.

## Completion-claim integrity

- Evidence must exist and be inspected before claiming success.
- Artifact existence is not artifact completion.
- A required failed gate leaves the operation unfinished.
- Previous assistant language is not evidence.
- Truthful partial completion is preferable to unsupported closure.

## Stop-the-line repository-health rule

If stale governance, a retired validator, an unregistered workflow, a superseded PR, contradictory runtime state, repeated no-progress cycle, or validation-scope fan-out can materially alter work selection or validation outcome, treat that as a repository-health defect. Repair or explicitly quarantine the common defect before continuing unrelated feature completion.

Do not repeatedly patch the same class of stale infrastructure inside individual feature tranches.

## Reporting

Report verified bounded results, material findings, genuine blockers, final CI/merge evidence, and the exact next action. Avoid low-level narration and repeated polling.

## Recovery fallback

If the pointer/registry/checkpoint is missing, contradictory, or materially stale:

1. stop unrelated mutation;
2. preserve conflicting records;
3. reconstruct state from current `main`, named attempt branches, PRs, commits, CI/artifacts, roadmap index, and owner-approved decisions;
4. classify stale material under the authority lifecycle policy;
5. repair canonical state through a bounded repository-health change;
6. only then resume production work.
