# MV-CONT-012 Execution Reconciliation Research

**Date:** 2026-09-12  
**Status:** SUPPORTING RESEARCH — non-authoritative except where adopted by CURRENT execution controls  
**Purpose:** Convert repeated owner-AI execution regressions into durable machine-enforced invariants rather than additional prose reminders.

## Research conclusion

The recurring failure was not a lack of instructions. It was reliance on the executor to remember, reinterpret and reapply instructions during a long-running sequence. Proven long-running systems move correctness out of transient reasoning and into durable state, stable identities, reconciliation loops, idempotency, independently checked evidence and transition/fault tests.

The implementation authority for the adopted controls is `governance/ai/runtime/EXECUTION_PROFILE.json`, `governance/ai/interaction-system/EXECUTION_TERMINATION_CONTRACT.json`, the termination-state schema, and `scripts/execution_termination_preflight.py`. This note records why those controls exist; it does not independently govern execution.

## Ten researched operations and adopted controls

1. **Desired-state reconciliation instead of self-declared completion.** Kubernetes-style controllers repeatedly compare observed state with declared desired state. Adopted control: terminal execution declares `desired_state=terminal_verified`; the preflight reconciles observed terminal invariants before permitting a response.

2. **Durable recovery identity instead of conversational reconstruction.** Temporal-style durable execution resumes from persisted execution identity/history rather than recreating intent after interruption. Adopted control: `cycle_id`, `resume_generation` and `resumed_from_cycle_id` preserve the same execution identity across interruption and recovery.

3. **Stable operation identity for retries.** Idempotent retry guidance separates a retry from a new request. Adopted control: one `operation_id` and `idempotency_key` per logical operation; retry attempts increment the existing record. Duplicate identities are invalid and do not count as progress.

4. **Separate side-effect identity from operation identity.** Transactional-outbox and durable-workflow patterns make external effects independently reconcilable. Adopted control: `side_effect_ledger` records effect identity/idempotency separately; terminal state requires each effect to be `verified` or `compensated`, not merely `applied`.

5. **Explicit liveness/no-progress accounting.** SRE and control-loop practice distinguishes useful convergence from repeated activity. Adopted control: terminal reconciliation requires at least one reconciliation pass and zero `consecutive_no_progress_passes`; polling, narration and unchanged reruns do not clear the condition.

6. **Independent verification instead of executor self-attestation.** Production-readiness/evaluation practice requires acceptance evidence separate from the implementation assertion. Adopted control: at least one passing independent evidence record must be bound to the active cycle and trace before terminal response.

7. **Transition-sequence testing instead of only happy-path unit tests.** Stateful/model-based testing finds defects that only appear across sequences. Adopted control: canonical regression tests cover combinations of desired-state drift, duplicate identities, effects, liveness, evidence, recovery and digest failures, and demand that the reconciler return the complete unmet set in one pass.

8. **Interruption/fault-injection recovery tests.** Durable systems must prove resume behavior at multiple interruption points. Adopted control: tests inject interruption after operation start, operation completion, effect application and evidence recording, then require same-cycle recovery without duplicate side effects.

9. **Causal trace continuity across tools and retries.** Distributed tracing preserves causality across process boundaries. Adopted control: one `trace_id` binds operation rows, effect rows and verification evidence; mismatched causal identity keeps execution nonterminal.

10. **Digest-bound terminal evidence.** Immutable/event-history systems make later mutation detectable. Adopted control: `reconciliation_digest` is SHA-256 over canonical reconciliation JSON excluding the digest field; mutation after reconciliation invalidates terminal proof.

## Source families studied

- Anthropic Engineering, long-running agent harness patterns: externalized progress state and recoverable agent context.
- Kubernetes documentation, controller/reconciliation architecture: observed state repeatedly driven toward desired state.
- Temporal documentation and engineering material, durable execution/event history: persisted execution state, replay and idempotent effect handling.
- AWS Builders' Library, safe retries with idempotency: stable request identity and retry semantics.
- Transactional Outbox pattern literature: durable separation and reconciliation of state transition versus external effect.
- Google SRE production-readiness/postmortem practices: evidence-backed readiness, explicit failure classification and operational learning.
- Stateful/model-based testing and fault-injection literature: verify transition sequences and recovery, not only single-function outputs.
- OpenTelemetry context/trace concepts: stable causal identity across process/tool boundaries.

## Anti-regression requirement

These findings are considered adopted only where executable controls or canonical regression tests enforce them. A future prose-only restatement is not a fix. If a new regression is discovered, add or strengthen an executable invariant/test before expanding narrative guidance.
