# Multiversal Checkpoint and Validation Efficiency Policy

**Document ID:** MV-AI-EFFICIENCY-001  
**Version:** 1.4.0  
**Status:** ACTIVE — OWNER APPROVED  
**Owner and final authority:** John Brandon Turner  
**Effective:** 2026-08-06  
**Updated:** 2026-09-14

## 1. Purpose

Preserve reliable recovery and final evidence without allowing checkpoint bookkeeping, broad validation, polling, or control-plane narration to dominate substantive Multiversal work. This policy controls where older instructions required per-batch checkpointing or time-filling behavior.

Final validation routing remains governed by `governance/ai/MULTIVERSAL_SELF_HOSTED_FINAL_VALIDATION_POLICY.md`. GitHub remains the orchestration/evidence plane; GitHub-hosted compute is not the default final gate.

## 2. Milestone-only checkpoint rule

Durable checkpoints are written at start, material handoff/blockage, ready-for-review, and completed-verified boundaries. Ordinary edits, checks, commits, validator repairs, polls, and uninterrupted substeps do not require checkpoint churn. The checkpoint is a recovery boundary, not an activity log.

## 3. No standalone completion-loop rule

A separate completion-only pull request is not required merely to copy merge evidence into runtime state. Completed-verified projection may be combined with strict-successor selection when the transition is otherwise atomic and truthful. Standalone correction remains appropriate when execution stops, recovery state would be contradictory, a protected gate depends on it, or the completion record itself is defective.

## 4. Validation cadence

Run the smallest relevant deterministic checks during construction, batch related repairs, then run the declared exact-head terminal gate once on the finished candidate. Superseded-head success does not count. Do not create one full CI cycle per assertion.

## 5. Workflow isolation

Workflows must be scoped to the artifacts and authority they validate. Unrelated historical programs, scorecards, validators, or runner plumbing must not become mandatory fan-out for ordinary current work. Recurring unrelated fan-out is a control-plane efficiency defect.

## 6. Roadmap and pointer writes

Do not repeatedly rewrite roadmap, pointer, status, or historical scorecard surfaces for progress narration. Update them only for real authority, dependency, owner-decision, handoff/blockage, or verified completion transitions.

## 7. Conversation recovery guarantee

A valid recovery surface must identify repository, exact authorized branch/attempt, objective, unfinished operation, next machine action, blockers, and completion gate. An unexpected conversation boundary resumes that durable state; it does not create a new execution unit or transfer routine scheduling responsibility to the owner.

## 8. Owner-facing reporting

Report material findings, genuine blockers/owner-only decisions, finished bounded packages, final evidence, or concise requested status. Routine repository operations and validation polling are not owner-facing milestones.

## 9. Prohibited regressions

This policy never authorizes false completion, hidden validation failure, deletion of failed attempts, weakened permission/privacy/provenance/security/migration/checksum controls, or unapproved paid-service/credential/deployment/release actions.

## 10. Immediate application

Apply this policy to active and future governed work. Historical artifacts remain evidence of their recorded state but do not override current machine-readable authority.

## 11. Tranche execution fast path

The family preflight's active-time target and closeout reserve are sizing, capacity, and **latency SLO** signals—not a **minimum runtime** requirement. **Operational overhead counts against the tranche target.** The historical closeout-risk calculation remains:

`target_active_minutes_per_unit - minimum_closeout_reserve_minutes`

For a 24-minute / 8-minute planning pattern, minute 16 is a risk signal to remove optional work from the critical path. It is not a permission-to-stop threshold and it is not a requirement to keep a terminal run alive. Actual **terminal invariants** govern completion: terminal before the SLO closes immediately; terminal after the SLO closes and records a miss; nonterminal after the SLO continues or surfaces a genuine blocker.

### 11.0 Execution-envelope boundary rule

The durable execution run—not a conversational turn or logical operation—is the ordinary execution boundary. Logical-operation completion is not cycle completion. While state is nonterminal and safe same-lane work exists, dynamic fill selects the next authorized operation. Once terminal invariants are satisfied, closeout proceeds immediately; elapsed time never grants or withholds terminal authority.

Cycle/run identity is monotonic recovery state. Conversation changes, context compaction, tool-batch boundaries, progress reports, and logical-operation completion do not reset it.

### 11.1 Preload once; do not rediscover

At bounded recovery, preload only current authority, checkpoint, exact branch/PR state, predecessor evidence, and declared validation profile. Do not rediscover unchanged tool schemas, repository capabilities, workflow shape, branch conventions, or merge methods unless a concrete invalidating event occurs.

### 11.2 Preserve parallel work without exploring it

Unrelated parallel work is preserved, not re-investigated. When canonical main moves, compare changed paths to the bounded tranche/control-plane surfaces first; inspect only actual overlap.

### 11.3 Batch repository mutations

When independent control-plane files form one governed transition, prefer an **atomic multi-file closeout** using Git-object tree/commit/ref primitives where available. Batch independent evidence reads when the tool surface supports it; serial calls are reserved for true dependencies.

### 11.4 Evidence economy

Prefer exact-head run conclusion, compact job summary/receipt, and only the specific deterministic artifact required by acceptance. **Full successful workflow logs are prohibited by default.** Read full logs only for failure, contradiction, missing evidence, or an otherwise unprovable acceptance fact.

### 11.5 Polling and mergeability discipline

Do not use **fixed sleep/poll loops** as normal orchestration. Query at meaningful state transitions. An initial `mergeable: false` is not proof of conflict when base/head are unchanged; perform **one bounded recomputation check** before race diagnosis. Repeated unchanged reads and status narration are operational noise.

### 11.6 Closeout reserve fast path

When closeout risk rises, stop nonessential discovery and protect exact-head evidence, merge authorization, canonical closeout, successor selection, and post-merge verification. Do not spend the protected path on schema rediscovery, broad scans, successful-log dumps, speculative parallel-work review, cosmetic cleanup, or repeated polling.

If external validation latency causes an SLO miss, record it separately from assistant/control overhead. If avoidable overhead materially contributes, classify it as a **control-plane efficiency incident** and repair the mechanism rather than enlarging the tranche.

### 11.7 One-Continue priority

The **one-Continue completion objective** takes precedence over optional observability work. A status update, tool-call boundary, or intermediate green milestone is not a terminal condition. Finish the bounded terminal gate or surface a genuine blocker with current evidence.
