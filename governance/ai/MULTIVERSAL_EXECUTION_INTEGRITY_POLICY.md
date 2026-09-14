# Multiversal Execution Integrity Policy

**Policy ID:** MV-EXEC-INTEGRITY-001  
**Status:** CURRENT  
**Effective:** 2026-09-14  
**Updated:** 2026-09-14 — Execution System v2 event-truth binding  
**Purpose:** Prevent a bounded execution from passing repository health while its recorded human-interaction count, latency, diagnostic behavior, environment readiness, or merge authorization contradicts observable evidence.

## Why this policy exists

ARI-22B completed as valid product work, but its execution-quality record was not trustworthy. The run required more owner intervention than the checkpoint admitted, exceeded the owner-visible timing target, crossed the diagnostic-repair threshold without entering diagnostic mode, repaired validation infrastructure inside the product tranche, and attempted a merge method the target repository did not permit. Existing prose rules and helper functions did not prevent those failures because the relevant checks were not mandatory at the state transitions where the failures occurred.

This policy deliberately adds **small executable seams rather than another broad behavioral protocol**. It complements, rather than replaces, the execution profile, convergence policy, transaction preflight, termination gate, and hermetic tranche context.

## Mandatory executable gates

1. **Execution integrity audit — `scripts/execution_integrity_gate.py`.** Repository health must audit both the current selected attempt and every checkpoint listed in `CURRENT_WORK_POINTER.json` under `recently_completed_implementation_work`. A completed predecessor does not fall out of enforcement merely because the strict successor was selected.
2. **Environment admission — `scripts/execution_environment_admission.py`.** Before a product mutation begins, the exact repository/base head must have a passing readiness receipt covering clean worktree, tracked executable line endings, validation harness readiness, incremental-cache policy readiness, and required runner-lane availability. Failed readiness enters a validation-harness repair lane; it is not silently counted as feature implementation.
3. **Merge authorization — `scripts/execution_merge_authorization.py`.** A merge authorization receipt is bound to one repository, one exact PR head SHA, and a method selected from fresh repository capabilities. The merge invocation must exactly match the receipt. Choosing a method first and checking capabilities later is forbidden.
4. **Event-derived owner-visible latency.** For every ledger-backed attempt, `scripts/execution_event_ledger.py` is authoritative for run start/completion and owner-visible wall latency. The initial 24-minute value is a latency SLO, not a minimum runtime or completion gate. A terminal run that misses the SLO closes truthfully and records the miss; elapsed time cannot grant or withhold terminal authority. `started_at → completed_at` checkpoint timing remains only a compatibility measure for pre-ledger historical attempts.
5. **Event-derived owner-interaction truth.** A ledger-backed checkpoint references one repository-relative event ledger by run identity and expected hash-chain head. Continue count, stall-nudge count, and single-Continue outcome are derived from that ledger. Checkpoint/convergence fields may project those values, but any disagreement is an integrity failure. More than one Continue cannot be certified as single-Continue success. An owner stall nudge is a liveness incident and prevents a `conforming` execution-quality result.
6. **Ledger identity and tamper resistance.** The referenced ledger `run_id` must equal the checkpoint attempt identity, the validated chain head must equal the checkpoint's declared `head_digest`, event sequence/linkage/digests must validate, and completed-run metrics require exactly one start and completion event. A rebound, rewritten, truncated, reordered, or otherwise invalid chain fails execution integrity.
7. **Diagnostic threshold integrity.** A record with two or more repair cycles and `diagnostic_mode=false` may be preserved only as historical nonconformance with the missed threshold explicitly recorded; it may not be rewritten into compliance after the fact.

## Completion semantics

Product completion, execution-quality conformance, and latency-SLO performance are distinct dimensions. A product merge with exact-head validation may remain `completed_verified` while its process is marked `historical_nonconforming`; a ledger-backed terminal result may be conforming while separately recording a latency-SLO miss. This prevents three opposite errors: discarding valid product work because the interaction process was poor, falsely declaring the process successful because code eventually merged, or forcing already-terminal work to continue merely to satisfy a clock.

## Provenance and correction rule

Historical checkpoint corrections are additive audit records. They preserve the original bad record so the failure remains inspectable. `governance/ai/execution-audits/ARI-22B_EXECUTION_CORRECTION_2026-09-14.json` remains the compatibility correction for ARI-22B because that attempt predates event-ledger enforcement. Future ledger-backed attempts must not use a correction record to override contradictory event truth; the chain must validate and projections must agree with it.

## Harness complexity budget

New harness controls require a reproduced project failure, an executable acceptance condition, and a regression that demonstrates the failure before the repair. Prefer strengthening an existing state boundary over adding narrative instructions. A control that does not change a machine decision, evidence requirement, or measurable outcome should not be added to the critical path.
