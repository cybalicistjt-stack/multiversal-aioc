# Multiversal New Conversation Bootstrap
## Mandatory Repository-First Session Recovery Protocol

**Document ID:** MV-AI-BOOTSTRAP-001  
**Version:** 7.0.1  
**Status:** ACTIVE  
**Owner and final authority:** John Brandon Turner

## Purpose

This file is a compact execution map, not a historical manual and not a current-status record. Runtime authority is repository evidence: `ACTIVE_AUTHORITY_REGISTRY.json` → `CURRENT_WORK_POINTER.json` → selected checkpoint → live repository/CI evidence. Historical prose never overrides those surfaces.

## Fast initialization

1. Verify access to the canonical AIOC and application repositories.
2. Read `governance/ai/runtime/ACTIVE_AUTHORITY_REGISTRY.json` and `governance/ai/runtime/CURRENT_WORK_POINTER.json`.
3. Read `governance/ai/runtime/EXECUTION_PROFILE.json`, the selected checkpoint, family preflight, and only the roadmap/program paths named by current state.
4. Compare the selected attempt to live branch/PR/head/validation evidence. Repair stale or contradictory repository state before unrelated feature work.
5. Resume the exact unfinished operation. Do not recreate completed work, reset counters, or create an alternate branch/PR when the authorized one exists.
6. If an interrupted ledger-backed run exists, preserve the same run/cycle/trace identity and resume its next machine action. Conversation boundaries do not transfer routine scheduling responsibility to the owner.

## Authority and context

Only CURRENT authority governs. Load only the selected tranche and declared dependency closure. Unrelated parallel work is not authorization to load, inspect, or mutate it. Repository-wide expansion requires a concrete failure signature and diagnostic reason.

Before product branch/PR mutation run `scripts/execution_transaction_preflight.py` against a fresh authorized-branch/open-PR snapshot. The transaction gate protects the **exact authorized branch**, carries the **current exact-head validation state**, and retains `owner_continue_turns` only as a legacy compatibility projection; ledger-backed runs derive owner interaction from events. `STOP_DUPLICATE_ATTEMPT` is a control-plane incident. Do not rediscover an already-loaded tool schema, repository capability, branch convention, workflow shape, or merge method unless an invalidating event changes it.

Normal routing stays inside the declared **hermetic tranche context**. `scripts/execution_state_reconciler.py` derives lifecycle/next action and `scripts/execution_context_guard.py` rejects undeclared expansion. When required context is resolved and the focused test exists, `DISPATCH_RED_NOW` is the next legal progression rather than more ordinary discovery.

## Execution System v2 truth model

For ledger-backed execution, `scripts/execution_event_ledger.py` is the source of truth for owner Continues, stall nudges, owner-visible wall latency and related interaction facts. Checkpoints may project those facts but the executor may not author or override them.

A bare `Continue` starts or resumes the current durable run. The execution abstraction is `work item -> durable run -> terminal result`, not a sequence of conversational turns. Completing a substep, commit, RED/GREEN transition, PR, or tool batch is not permission to return control.

## Tranche execution fast path

The one-Continue completion objective remains a user-experience/service objective, not an AI-authored success claim. Routine execution proceeds through bounded implementation, focused repair, exact-head validation, merge, canonical closeout, terminal reconciliation and strict-successor selection unless a genuine blocker prevents further authorized progress.

The historical **closeout-switch point** (`target_active_minutes_per_unit - minimum_closeout_reserve_minutes`, commonly 16 from 24/8) is now a risk/sizing signal only. The 24-minute value is an initial **latency SLO**, not a **minimum runtime**. Actual **terminal invariants** govern completion:

- terminal at minute 8 closes at minute 8;
- terminal at minute 31 closes and records an SLO miss;
- nonterminal at minute 31 continues the same durable run or reports a genuine blocker;
- elapsed time never grants or withholds terminal authority.

When a risk signal is reached, drop optional expansion and protect closeout, but do not manufacture work merely to consume time.

### Critical-path efficiency

- Prefer an **atomic tree/commit** for multi-file governance start/closeout projections.
- While exact-head validation runs, precompute only evidence-independent closeout shapes.
- On successful validation, prefer the compact evidence artifact/receipt over full log retrieval.
- An initial `mergeable: false` is not itself proof of conflict; perform one bounded recomputation check when base/head remain unchanged.
- Do not use fixed sleep/poll loops as normal orchestration; query at meaningful state transitions.
- Avoid repeated unchanged-head reads, schema rediscovery, successful-log dumps, speculative scans, and unrelated parallel work.
- Avoidable overhead that materially contributes to owner-visible latency is a **control-plane efficiency incident**; do not hide it by enlarging the tranche.

## Failure and retry discipline

Capture the exact failure signature first. Classify the fault domain before changing code: product implementation, validation contract, validation infrastructure, runner/environment, repository state, source availability, owner-only, or other explicit class.

A retry requires materially changed evidence. The second related repair enters diagnostic mode with a concrete signature and falsifiable hypotheses. Unchanged reruns, repeated polling, narration, or reading more unrelated context are not progress. Diagnose the first critical failure and causal chain, apply the smallest causal repair, run focused regression, then the required terminal gate.

Environment/harness repairs are isolated from product feature repair counts. A failed runner, cache, line-ending, checkout or workflow precondition is not automatically a feature defect.

## Repository side effects

Discover fresh repository capabilities before merge. Bind merge authorization to exact repository, PR/head SHA and supported method. Unsupported merge methods stop before mutation.

Externally visible effects have durable operation/effect identities and must be verified or compensated. Multi-file control-plane mutation uses one atomic tree/commit/ref update where supported.

Application merge → AIOC closeout is a resumable distributed transition. Observe the application merge durably, then reconcile canonical AIOC state and strict successor; interruption never requires the owner to discover which half completed.

## Final-response gate

Before any final response from execution mode, construct the current termination state and run `scripts/execution_termination_preflight.py`. Open PR, active required validation, pending merge closeout, pending authorized work, nonclosed lifecycle state, unresolved side effects, missing independent evidence, or failed reconciliation blocks the response.

If any blocking condition remains, the preflight returns `CONTINUE_EXECUTION` and execution continues. Only a fresh `ALLOW_FINAL_RESPONSE` result authorizes an execution-mode final response.

Elapsed time is telemetry only. No minimum runtime is required. A correct terminal state closes immediately; a latency SLO miss is recorded rather than used to force more work.

Only these are legitimate execution-mode terminal outcomes:

1. requested bounded work is `completed_verified`, required successor/boundary work is complete, lifecycle is closed and reconciliation passes;
2. a genuine externally evidenced blocker survived reasonable recovery and blocks all remaining authorized progress;
3. the owner explicitly changed to a non-execution command such as get-ready/status-only/analysis-only.

Self-imposed response/tool/token/context pressure is not a genuine blocker while governed tools or fallbacks remain callable.

## Owner operating rule

John sets priority and resolves explicit owner-only decisions. The execution system owns routine scheduling, continuation, verification and recovery. A second owner `Continue` on the same ordinary tranche without a genuine blocker is an execution incident and must be visible in event-derived metrics; it can never be certified as one-Continue success.
