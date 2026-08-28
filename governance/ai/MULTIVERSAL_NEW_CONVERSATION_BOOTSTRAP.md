# Multiversal New Conversation Bootstrap
## Mandatory Repository-First Session Recovery Protocol

**Document ID:** MV-AI-BOOTSTRAP-001  
**Version:** 6.4.0
**Status:** ACTIVE CANDIDATE — CRS COMPLETION PENDING  
**Owner and final authority:** John Brandon Turner  
**Governance repository:** `cybalicistjt-stack/multiversal-aioc`  
**Application repository:** `cybalicistjt-stack/Multiversal-app`  
**Last updated:** 2026-08-28

## Purpose

This file is a stable recovery protocol, not a current-status document. It must never hard-code the current milestone, current work item, PR, branch, or exact next feature operation. Changing project state belongs in repository runtime state and live GitHub evidence. The permanent owner entry point remains `governance/ai/MULTIVERSAL_STATIC_RESTART_PROMPT.txt`.

## Authority lifecycle

Read and obey `governance/ai/MULTIVERSAL_AUTHORITY_AND_RETIREMENT_POLICY.md` and `governance/ai/runtime/ACTIVE_AUTHORITY_REGISTRY.json`. Only material explicitly classified `CURRENT` may govern current work. `CURRENT_COMPATIBLE` material may support it but cannot override canonical state. Historical, retired, and unregistered material cannot select work, impose a current gate, or auto-execute merely because it still exists. Repository evidence outranks stale prose.

## Mandatory operating policies

Read the policies named by `CURRENT_WORK_POINTER.json` plus all CURRENT operating policies in the authority registry. The stable set includes:

- `governance/ai/MULTIVERSAL_CHECKPOINT_AND_VALIDATION_EFFICIENCY_POLICY.md`
- `governance/ai/MULTIVERSAL_COMPLETION_CLAIM_INTEGRITY_POLICY.md`
- `governance/ai/MULTIVERSAL_SELF_HOSTED_FINAL_VALIDATION_POLICY.md`
- `governance/ai/MULTIVERSAL_AUTHORITY_AND_RETIREMENT_POLICY.md`
- `governance/ai/MULTIVERSAL_EXECUTION_CONVERGENCE_POLICY.md`

Do not infer current status from examples embedded in policies or historical work packages.

## Fast mandatory initialization sequence

Perform this sequence before explaining, planning, or claiming current project state:

1. Verify connected read/write access to both canonical repositories and the authenticated identity when required by the contributor registry.
2. Read this bootstrap from AIOC `main`.
3. Read `governance/ai/runtime/ACTIVE_AUTHORITY_REGISTRY.json`.
4. Read `governance/ai/runtime/CURRENT_WORK_POINTER.json`.
5. Read the current operating policies.
6. Read the checkpoint named by `primary_attempt_id` and inspect its branch/PR/commit evidence.
7. If the active attempt has implementation authority, recover its `convergence_control` counters, failure classification, diagnostic hypotheses, and retry basis. A new conversation does not reset them.
8. Compare pointer/checkpoint with live GitHub state. A closed PR, missing branch, superseded attempt, contradictory head, or post-merge stale pointer is a repository-health defect; repair it before unrelated feature work.
9. Read `governance/ai/runtime/ROADMAP_INDEX.json` and only the roadmap/program/supplement paths named by current state. Do not load unrelated historical roadmap sections by default.
10. Inspect blocking CI/failure evidence only when bound to the active attempt or its required gate. Historical failures are not automatically current blockers.
11. When repeated owner continuations, repair loops, retry behavior, or validation-scope performance matter, inspect the live execution-convergence scorecard. Do not substitute the historical deterministic interaction pilot for live throughput evidence.
12. If exact bytes, archives, screenshots, physical devices, generated packages, external credentials, or special hardware are required, inspect the actual available source/execution surface before declaring a blocker.
13. When a checkout is available, run the current repository continuity/health validation. With connector-only access, verify the equivalent pointer → checkpoint → branch/PR → evidence invariants directly.
14. Resume the exact unfinished operation. Do not recreate completed work, reset convergence counters, or revive historical authority.

## Current-state prohibition

Do not patch this bootstrap merely because a work item completes or selection changes. Current PR numbers, branch heads, milestone summaries, migration numbers, feature baselines, or current-state amendments belong in pointer/checkpoint/roadmap/registry evidence, not here.

## Work-state interpretation

Only `completed_verified` is complete. Started, in-progress, quarantined, blocked, ready-for-review, and validation-failed states remain unfinished unless an explicit governing policy defines another terminal state. Never infer completion from conversation ending, generated artifact, branch, commit, open PR, partial green check, silence, or old projection.

## Branch-versus-main recovery

`main` is the last merged canonical baseline. An unfinished attempt branch may contain newer valid work/evidence. Inspect main, then the exact named attempt branch/PR, preserve newer internally consistent attempt work, never let an unregistered historical branch override the pointer, and reconcile contradictions through bounded repository-health work before unrelated changes.

## PR lifecycle

A work item may have only one authoritative active integration path. Superseded PRs must be closed with preservation/supersession evidence; closed PRs cannot be selected current; dormant/special-environment PRs must be explicitly registered non-authoritative; open PR existence or age does not grant authority.

## Workflow and validator lifecycle

Before relying on an old workflow or validator:

1. verify it is registered current/current-compatible;
2. verify lifecycle assumptions still match repository state;
3. verify it uses current validation policy/core or a registered exception;
4. retire correct historical validators from current paths instead of weakening their historical assertions;
5. historical workflows must not auto-trigger;
6. ordinary substantive application/package PRs must select exactly one governed current-tranche Validation Core profile by default rather than automatically invoking completed historical profiles.

Application/package final validation uses exact-head self-hosted Windows/Linux lanes and deterministic cross-platform evidence when applicable. GitHub-hosted compute is not a generic project-wide final requirement.

## Source-material and execution-surface rule

Distinguish precisely among source bytes unavailable, transfer unavailable, checkout unavailable, feature validation failure, validation-contract failure, validation-infrastructure failure, runner/environment failure, repository-state failure, and owner-only gate. Never reconstruct checksum-bound exact artifacts from excerpts, memory, OCR, or paraphrase.

## Checkpoint and convergence discipline

Checkpoints are recovery boundaries, not activity logs. Create one start checkpoint before substantive mutation; update only on material handoff, blocker/recovery-path change, ready-for-review, or completed_verified; run focused checks during construction and the declared exact-head gate at final package boundary; never rewrite an interrupted attempt to appear complete; and avoid gratuitous closure-only churn where state is already consistent.

The initialization sequence is one bounded recovery pass. Its pointer/checkpoint, relevant exact-head and current-gate facts remain under an evidence-freshness lease until an authority/head/branch change, merge/rebase, conflicting writer, materially new check result, or explicit stale/contradictory tool response invalidates them. Refresh only affected facts. Do not restart full reconnaissance because a tool batch ended, time elapsed, context compacted, status was requested, or another historical file exists.

For implementation attempts:

- convergence counters are monotonic across conversations;
- a retry after failure must record what materially changed; an identical rerun is not progress;
- a second materially related repair requires `diagnostic_mode`, a failure class, a failure signature, and falsifiable root-cause hypotheses before another final rerun;
- related fixes are batched before rerunning the final gate;
- two no-progress cycles require an explicit control-plane, environment, or owner blocker, or a diagnostic change to retry basis;
- a third patch-and-rerun cycle without materially new diagnostic evidence is forbidden.

## Owner operating rule

When John says `Continue`, execute the next verified unfinished implementation tranche as a whole. Do not substitute acknowledgement, plan, promise, recap, or unnecessary clarification.

Unless a genuine owner-only, unavailable-environment, unavailable-source, safety, or irrecoverable external blocker prevents completion, `Continue` means carry the tranche through governed start if needed, implementation, focused repair, exact-head validation, required merge, `completed_verified` closeout, and canonical strict-successor selection. Do not stop merely because validation is queued/in progress, a PR is ready, closeout is pending, or the successor could be selected later. Work through normal validation latency and finish the bounded tranche before reporting.

A repeated `Continue` on the same ordinary tranche is an execution-cost signal. Do not consume another owner turn merely to rediscover the same state or repeat unchanged validation. Classify failure, diagnose by the second related repair, and block explicitly rather than entering an unbounded retry loop.

If a genuine blocker survives reasonable recovery, preserve the exact recovery point and report it truthfully.

## Executable final-response preflight

Owner command mode is stateful for the execution turn:

- `Continue`, `fix this`, and `implement this` select execution mode for the bounded unit;
- `status report and continue` supplies a concise status without cancelling execution mode;
- `keep going`, `continue until you need me`, and a named finish boundary remain active through that boundary;
- `get ready`, status-only, and analysis-only are explicit non-execution modes.

Before a final response from an execution turn, create an ephemeral state object conforming to `governance/ai/interaction-system/EXECUTION_TERMINATION_STATE.schema.json` and run:

`python scripts/execution_termination_preflight.py --state <temporary-state.json>`

The state must reflect current evidence for work status, required successor selection, the owner-requested boundary, active asynchronous operations, pending authorized steps, and any genuine blocker. Continue using tools when the result is `CONTINUE_EXECUTION`. Finalize only when it returns `ALLOW_FINAL_RESPONSE` for `completed_verified`, a sufficiently evidenced all-progress blocker, or an explicit non-execution mode.

The temporary state is not committed. The checkpoint remains milestone-only. Missing, failed, or stale preflight evidence never grants permission to stop.

## Completion-claim integrity

Evidence must exist and be inspected before claiming success. Artifact existence is not completion. A required failed gate leaves work unfinished. Previous assistant prose is not evidence. Truthful partial completion is preferable to unsupported closure.

## Stop-the-line repository-health rule

If stale governance, a retired validator, unregistered workflow, superseded PR, contradictory runtime state, repeated no-progress cycle, or validation-scope fan-out can materially alter work selection or validation outcome, repair or explicitly quarantine the common defect before unrelated feature completion. Do not repeatedly patch the same infrastructure defect inside individual feature tranches.

## Reporting

Report verified bounded results, material findings, genuine blockers, final CI/merge evidence, and the exact next action. Avoid low-level narration and repeated polling.

## Recovery fallback

If pointer/registry/checkpoint is missing, contradictory, or materially stale: stop unrelated mutation; preserve conflicts; reconstruct from current main, named branches, PRs, commits, CI/artifacts, roadmap index, and owner-approved decisions; classify stale material under authority lifecycle; repair canonical state through bounded repository-health work; then resume production work.
