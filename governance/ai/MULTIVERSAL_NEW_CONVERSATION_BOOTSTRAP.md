# Multiversal New Conversation Bootstrap
## Mandatory Repository-First Session Recovery Protocol

**Document ID:** MV-AI-BOOTSTRAP-001  
**Version:** 6.8.0
**Status:** ACTIVE CANDIDATE — CRS COMPLETION PENDING  
**Owner and final authority:** John Brandon Turner  
**Governance repository:** `cybalicistjt-stack/multiversal-aioc`  
**Application repository:** `cybalicistjt-stack/Multiversal-app`  
**Last updated:** 2026-09-13

## Purpose

This file is a stable recovery protocol, not a current-status document. It must never hard-code the current milestone, current work item, PR, branch, or exact next feature operation. Changing project state belongs in repository runtime state and live GitHub evidence. The permanent owner entry point remains `governance/ai/MULTIVERSAL_STATIC_RESTART_PROMPT.txt`.

## Authority lifecycle

Read and obey `governance/ai/MULTIVERSAL_AUTHORITY_AND_RETIREMENT_POLICY.md` and `governance/ai/runtime/ACTIVE_AUTHORITY_REGISTRY.json`. Only material explicitly classified `CURRENT` may govern current work. `CURRENT_COMPATIBLE` material may support it but cannot override canonical state. Historical, retired, and unregistered material cannot select work, impose a current gate, or auto-execute merely because it still exists. Repository evidence outranks stale prose.

## Mandatory operating policies

Read the policies named by `CURRENT_WORK_POINTER.json` plus all CURRENT operating policies in the authority registry. The stable set includes:

- `governance/ai/runtime/EXECUTION_PROFILE.json`
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
5. Read the current execution profile and operating policies.
6. Read the checkpoint named by `primary_attempt_id` and inspect its authorized branch/PR/commit evidence.
7. If the active attempt has implementation authority, recover its `convergence_control` counters, failure classification, diagnostic hypotheses, retry basis, and exact authorized implementation branch. A new conversation does not reset them.
8. Compare pointer/checkpoint with live GitHub state. A closed PR, missing branch, alternate branch for the same active work item, duplicate open PR, superseded attempt, contradictory head, or post-merge stale pointer is a repository-health defect; repair it before unrelated feature work.
9. Read `governance/ai/runtime/ROADMAP_INDEX.json` and only the roadmap/program/supplement paths named by current state. Do not load unrelated historical roadmap sections by default.
10. Inspect blocking CI/failure evidence only when bound to the active attempt or its required gate. Historical failures are not automatically current blockers.
11. When repeated owner continuations, repair loops, retry behavior, or validation-scope performance matter, inspect the live execution-convergence scorecard. Do not substitute the historical deterministic interaction pilot for live throughput evidence.
12. If exact bytes, archives, screenshots, physical devices, generated packages, external credentials, or special hardware are required, inspect the actual available source/execution surface before declaring a blocker.
13. When a checkout is available, run the current repository continuity/health validation. With connector-only access, verify the equivalent pointer → checkpoint → branch/PR → evidence invariants directly.
14. Resume the exact unfinished operation. Do not recreate completed work, reset convergence counters, revive historical authority, or create an alternate branch/PR when the authorized branch/PR already exists.
15. If the prior execution turn was interrupted before its execution envelope became terminal, recover and resume the same `cycle_id`, phase, elapsed envelope state, dynamic-fill status, and exact next same-lane operation. Conversation change does not create a new execution cycle.

## Current-state prohibition

Do not patch this bootstrap merely because a work item completes or selection changes. Current PR numbers, branch heads, milestone summaries, migration numbers, feature baselines, or current-state amendments belong in pointer/checkpoint/roadmap/registry evidence, not here.

## Work-state interpretation

Only `completed_verified` is complete. Started, in-progress, quarantined, blocked, ready-for-review, and validation-failed states remain unfinished unless an explicit governing policy defines another terminal state. Never infer completion from conversation ending, generated artifact, branch, commit, open PR, partial green check, silence, or old projection.

## Branch-versus-main recovery

`main` is the last merged canonical baseline. An unfinished attempt branch may contain newer valid work/evidence. Inspect main, then the exact named attempt branch/PR, preserve newer internally consistent attempt work, never let an unregistered historical branch override the pointer, and reconcile contradictions through bounded repository-health work before unrelated changes.

## PR lifecycle

A work item may have only one authoritative active integration path. Superseded PRs must be closed with preservation/supersession evidence; closed PRs cannot be selected current; dormant/special-environment PRs must be explicitly registered non-authoritative; open PR existence or age does not grant authority.

After a governed product start and before creating or mutating an application implementation branch, run the deterministic execution transaction preflight against a fresh snapshot of the exact authorized branch, observed same-work-item branches, and open pull requests. Resume the exact authorized branch or PR when it already exists. `STOP_DUPLICATE_ATTEMPT` is a stop-the-line control-plane incident; do not create an alternate branch or duplicate PR to work around it.

Before product-branch creation or mutation, the started checkpoint, current pointer, active authority registry, runtime lifecycle projection, and compiled roadmap selection must agree on work item, attempt, state and implementation authority; every branch-bearing projection must agree on the exact authorized branch. The executable check is `scripts/execution_transaction_preflight.py`.

## Workflow and validator lifecycle

Before relying on an old workflow or validator:

1. verify it is registered current/current-compatible;
2. verify lifecycle assumptions still match repository state;
3. verify it uses current validation policy/core or a registered exception;
4. retire correct historical validators from current paths instead of weakening their historical assertions;
5. historical workflows must not auto-trigger;
6. ordinary substantive application/package PRs must select exactly one governed current-tranche Validation Core profile by default rather than automatically invoking completed historical profiles.

Application/package final validation uses exact-head self-hosted Windows/Linux lanes and deterministic cross-platform evidence when applicable. GitHub-hosted compute is not a generic project-wide final requirement.

Validation evidence is bound to its exact candidate head. Once the candidate head changes, evidence from an earlier head is superseded and cannot satisfy merge or closeout. Do not spend another discovery pass proving that stale evidence is stale; compare the evidence head to the current head and continue with only the current-head gate.

## Source-material and execution-surface rule

Distinguish precisely among source bytes unavailable, transfer unavailable, checkout unavailable, feature validation failure, validation-contract failure, validation-infrastructure failure, runner/environment failure, repository-state failure, and owner-only gate. Never reconstruct checksum-bound exact artifacts from excerpts, memory, OCR, or paraphrase.

Also distinguish the execution layers explicitly: host/filesystem access, shell/network access, repository authentication, per-task plugin or MCP availability, sandbox/approval policy, and external model/session quota. Never summarize a missing optional plugin or MCP method as “this environment is unavailable” when the Windows host, repositories and authenticated GitHub fallback remain usable. Name the exact unavailable interface, whether it is required, the fallback used, and any material cost or scope impact.

## Checkpoint and convergence discipline

Checkpoints are recovery boundaries, not activity logs. Create one start checkpoint before substantive mutation; update only on material handoff, blocker/recovery-path change, ready-for-review, or completed_verified; run focused checks during construction and the declared exact-head gate at final package boundary; never rewrite an interrupted attempt to appear complete; and avoid gratuitous closure-only churn where state is already consistent.

The initialization sequence is one bounded recovery pass. Its pointer/checkpoint, relevant exact-head and current-gate facts remain under an evidence-freshness lease until an authority/head/branch change, merge/rebase, conflicting writer, materially new check result, or explicit stale/contradictory tool response invalidates them. Refresh only affected facts. Do not restart full reconnaissance because a tool batch ended, time elapsed, context compacted, status was requested, or another historical file exists.

For implementation attempts:

- convergence counters are monotonic across conversations;
- a retry after failure must record what materially changed; an identical rerun is not progress;
- a second materially related repair requires `diagnostic_mode`, a failure class, a failure signature, and falsifiable root-cause hypotheses before another final rerun;
- related fixes are batched before rerunning the final gate;
- two no-progress cycles require an explicit control-plane, environment, or owner blocker, or a diagnostic change to retry basis;
- a third patch-and-rerun cycle without materially new diagnostic evidence is forbidden;
- every newly completed governed execution unit records `owner_continue_turns`, `single_continue_achieved`, and `execution_incident`; a second owner `Continue` without a genuine blocker must be recorded as an execution incident and may not be reported as one-Continue success.

## Tranche execution fast path

Immediately after bounded recovery, read the current execution profile plus the family preflight's `target_active_minutes_per_unit` and `minimum_closeout_reserve_minutes`. Protect the closeout reserve from the beginning of execution. The closeout-switch point is `target_active_minutes_per_unit - minimum_closeout_reserve_minutes`; with the current 24/8 pattern, optional implementation/reconnaissance work must be off the critical path by minute 16. Crossing that point never grants permission to stop; it switches execution to terminal closeout only.

The **execution envelope** is the cycle boundary. A logical operation is not a cycle boundary. One owner `Continue` creates or resumes one stable cycle and dynamically packs safe same-lane operations into it. While the envelope remains in fill and safe same-lane work exists, completing one operation must immediately trigger dynamic fill with the next safe operation; do not close, report, or increment the cycle merely because a research facet, implementation substep, artifact, commit, or validation milestone completed.

For the current 24-minute pattern, minute 16 changes the same execution envelope from fill to shared closeout. The remaining reserve is part of the same cycle. Normal terminal response requires the envelope to close after the 24-minute target is accounted. Earlier closure requires an actual dynamic-fill attempt that proves safe same-lane work is exhausted, or a separately evidenced genuine blocker. If a turn or conversation is interrupted, resume the same `cycle_id`; do not reset cycle identity, elapsed state, or turn a remaining logical operation into a new cycle.

### Deterministic execution routing

After bounded recovery, derive lifecycle phase and next action with `scripts/execution_state_reconciler.py` from the canonical execution record plus observed repository facts. Stored narrative next-action text is a display projection, not independent authority.

Build and obey a **hermetic tranche context** through `scripts/execution_context_guard.py`. Normal execution may read only declared tranche inputs and their authorized dependency closure. Repository-wide search or undeclared reads require diagnostic mode plus a concrete failure signature; exploration without such evidence is non-progress.

Run `scripts/execution_transaction_preflight.py route` before expanding implementation context. When it returns `DISPATCH_RED_NOW`, dispatch the focused RED validation immediately. Do not perform additional ordinary research, repository search, or source expansion between a resolved focused test and RED. Focused Validation Core profiles should be generated from bounded work-item data through `scripts/generate_focused_validation_profile.py` rather than manually reconstructed.

The following rules are mandatory in every new conversation and every resumed `Continue`:

- **Before any product branch or PR mutation, run the execution transaction preflight.** Use the checkpoint's exact authorized branch and a fresh branch/open-PR snapshot. Resume the exact branch/PR when present; do not create an alternate attempt.
- **Do not rediscover an already-loaded tool schema**, connector capability, repository identity, workflow shape, branch convention, or merge method unless a concrete error or authority change invalidates it.
- Load only the selected tranche and explicitly named dependencies. The existence of unrelated parallel work does not authorize loading or reviewing it. Preserve parallel work by path comparison when a live head actually changes.
- If `main` moved, compare changed paths first. When there is no overlap, transplant/rebase the bounded prepared change without rereading unrelated DWC/LXG/GCL/CNI/PCA/SAA content.
- Prefer an **atomic tree/commit** for a multi-file governance start/closeout when the available repository surface supports it. Do not burn the reserve on serial one-file bookkeeping commits.
- On successful validation, prefer exact-head run status, job-step summary, and the compact evidence artifact or deterministic receipt. Do not fetch full successful logs unless compact evidence is missing or contradictory.
- Do not use fixed sleep/poll loops as routine orchestration. Query at meaningful state transitions only.
- An initial `mergeable: false` from GitHub is not, by itself, a repository conflict when base/head are unchanged. Perform one bounded recomputation check before race diagnosis unless another signal already proves conflict.
- Re-read canonical `main` only at a named invalidation event or the declared merge/closeout boundary. Repeated unchanged-head checks are not progress.
- While current-head final validation is running, precompute the closeout and successor projections that do not depend on final evidence. Never fabricate validated-head, validation-run, receipt, or merge evidence; leave those fields unbound until observed.
- At the closeout-switch point, stop broad scans, successful-log dumps, speculative parallel-work review, schema/tool rediscovery, cosmetic cleanup, repeated polling, and explanatory narration. Spend the reserve only on final evidence binding, application merge, AIOC closeout, exact-head AIOC health, AIOC merge, successor selection, and one post-merge verification.

Required external validation latency is measured separately from assistant/control overhead. Avoidable tool rediscovery, redundant reads, repeated polling, unnecessary full-log retrieval, duplicate branch/PR creation, serial closeout writes where atomic mutation is available, or speculative investigation that causes/materially contributes to a target overrun is a **control-plane efficiency incident**, not normal tranche complexity. Repair the governing process rather than increasing the tranche size to hide the regression.

These fast-path rules are part of the mandatory bootstrap precisely so they survive conversation boundaries; a new conversation must not fall back to broader reconnaissance merely because prior conversational context is absent.

## Owner operating rule

When John says `Continue`, execute the next verified unfinished implementation tranche as a whole. Do not substitute acknowledgement, plan, promise, recap, or unnecessary clarification.

Unless a genuine owner-only, unavailable-environment, unavailable-source, safety, or irrecoverable external blocker prevents completion, `Continue` means carry the tranche through governed start if needed, implementation, focused repair, exact-head validation, required merge, `completed_verified` closeout, and canonical strict-successor selection. Do not stop merely because validation is queued/in progress, a PR is ready, closeout is pending, or the successor could be selected later. Work through normal validation latency and finish the bounded tranche before reporting.

A repeated `Continue` on the same ordinary tranche is an execution-cost signal and, absent a genuine blocker, an execution incident. Do not consume another owner turn merely to rediscover the same state or repeat unchanged validation. Classify failure, diagnose by the second related repair, and block explicitly rather than entering an unbounded retry loop.

If a genuine blocker survives reasonable recovery, preserve the exact recovery point and report it truthfully.

Before an application merge, stage the corresponding AIOC closeout mutation and retain an execution-budget reserve for merge verification, canonical closeout and successor selection. If an observable platform usage ceiling makes that reserve unavailable, keep the validated application pull request open. If the ceiling interrupts execution anyway, record a privacy-minimized `environment_unavailable` handoff with all pending authorized steps and resume them before unrelated work.

## Executable final-response preflight

Owner command mode is stateful for the execution turn:

- `Continue`, `fix this`, and `implement this` select execution mode for the bounded unit;
- `status report and continue` supplies a concise status without cancelling execution mode;
- `keep going`, `continue until you need me`, and a named finish boundary remain active through that boundary;
- `get ready`, status-only, and analysis-only are explicit non-execution modes.

Before a final response from an execution turn, create an ephemeral state object conforming to `governance/ai/interaction-system/EXECUTION_TERMINATION_STATE.schema.json` and run:

`python scripts/execution_termination_preflight.py --state <temporary-state.json>`

The state must reflect current evidence for work status, required successor selection, the owner-requested boundary, active asynchronous operations, pending authorized steps, any genuine blocker, and—when known—the governed pull-request state, current exact-head validation state, and whether merge closeout remains pending. For execution-mode `completed_verified`, the state must also contain the current execution envelope: stable `cycle_id`, phase, elapsed active minutes, canonical 16/24 switch/target, safe same-lane work availability, dynamic-fill attempt state, shared-closeout completion, and fill-exit reason. Open PR, queued/running exact-head validation, merged-with-closeout-pending, fill/closeout envelope state, unproved early exhaustion, or a normal closed envelope below the 24-minute target independently forces `CONTINUE_EXECUTION`, even if a pending-step list was accidentally incomplete. Continue using tools when the result is `CONTINUE_EXECUTION`. Finalize only when it returns `ALLOW_FINAL_RESPONSE` for `completed_verified`, a sufficiently evidenced all-progress blocker, or an explicit non-execution mode.

The temporary state is not committed. The checkpoint remains milestone-only. Missing, failed, stale, or envelope-incomplete preflight evidence never grants permission to stop.

## Completion-claim integrity

Evidence must exist and be inspected before claiming success. Artifact existence is not completion. A required failed gate leaves work unfinished. Previous assistant prose is not evidence. Truthful partial completion is preferable to unsupported closure.

## Stop-the-line repository-health rule

If stale governance, a retired validator, unregistered workflow, superseded PR, duplicate/alternate active integration path, contradictory runtime state, repeated no-progress cycle, or validation-scope fan-out can materially alter work selection or validation outcome, repair or explicitly quarantine the common defect before unrelated feature completion. Do not repeatedly patch the same infrastructure defect inside individual feature tranches.

## Reporting

Report verified bounded results, material findings, genuine blockers, final CI/merge evidence, and the exact next action. Avoid low-level narration and repeated polling.

## Recovery fallback

If pointer/registry/checkpoint is missing, contradictory, or materially stale: stop unrelated mutation; preserve conflicts; reconstruct from current main, named branches, PRs, commits, CI/artifacts, roadmap index, and owner-approved decisions; classify stale material under authority lifecycle; repair canonical state through bounded repository-health work; then resume production work.
