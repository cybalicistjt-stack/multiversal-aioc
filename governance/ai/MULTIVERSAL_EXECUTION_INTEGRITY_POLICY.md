# Multiversal Execution Integrity Policy

**Policy ID:** MV-EXEC-INTEGRITY-001  
**Status:** CURRENT  
**Effective:** 2026-09-14  
**Purpose:** Prevent a bounded execution from passing repository health while its recorded human-interaction count, timing, diagnostic behavior, environment readiness, or merge authorization contradicts observable evidence.

## Why this policy exists

ARI-22B completed as valid product work, but its execution-quality record was not trustworthy. The run required more owner intervention than the checkpoint admitted, exceeded the owner-visible timing target, crossed the diagnostic-repair threshold without entering diagnostic mode, repaired validation infrastructure inside the product tranche, and attempted a merge method the target repository did not permit. Existing prose rules and helper functions did not prevent those failures because the relevant checks were not mandatory at the state transitions where the failures occurred.

This policy deliberately adds **small executable seams rather than another broad behavioral protocol**. It complements, rather than replaces, the execution profile, convergence policy, transaction preflight, termination gate, and hermetic tranche context.

## Mandatory executable gates

1. **Execution integrity audit — `scripts/execution_integrity_gate.py`.** Repository health must audit both the current selected attempt and every checkpoint listed in `CURRENT_WORK_POINTER.json` under `recently_completed_implementation_work`. A completed predecessor does not fall out of enforcement merely because the strict successor was selected.
2. **Environment admission — `scripts/execution_environment_admission.py`.** Before a product mutation begins, the exact repository/base head must have a passing readiness receipt covering clean worktree, tracked executable line endings, validation harness readiness, incremental-cache policy readiness, and required runner-lane availability. Failed readiness enters a validation-harness repair lane; it is not silently counted as feature implementation.
3. **Merge authorization — `scripts/execution_merge_authorization.py`.** A merge authorization receipt is bound to one repository, one exact PR head SHA, and a method selected from fresh repository capabilities. The merge invocation must exactly match the receipt. Choosing a method first and checking capabilities later is forbidden.
4. **Owner-visible timing — execution integrity audit.** `started_at → completed_at` wall time is the owner-visible timing measure for the checkpoint. Synthetic `elapsed_active_minutes` may remain useful for the internal execution envelope but may not substitute for owner-visible elapsed time or certify the timing service objective.
5. **Owner-interaction truth.** A completed attempt records the actual owner Continue count and owner stall nudges. More than one Continue cannot be certified as single-Continue success. An owner stall nudge is a liveness incident and prevents a `conforming` execution-quality result.
6. **Diagnostic threshold integrity.** A record with two or more repair cycles and `diagnostic_mode=false` may be preserved only as historical nonconformance with the missed threshold explicitly recorded; it may not be rewritten into compliance after the fact.

## Completion semantics

Product completion and execution-quality conformance are independent dimensions. A product merge with exact-head validation may remain `completed_verified` while the execution is marked `historical_nonconforming`. That distinction prevents two opposite errors: discarding valid product work because the interaction process was poor, or falsely declaring the process successful because the code eventually merged.

## Provenance and correction rule

Historical checkpoint corrections are additive audit records. They must preserve the original bad record so the failure remains inspectable. `governance/ai/execution-audits/ARI-22B_EXECUTION_CORRECTION_2026-09-14.json` is the first such correction and is applied by the integrity gate when auditing ARI-22B.

## Harness complexity budget

New harness controls require a reproduced project failure, an executable acceptance condition, and a regression that demonstrates the failure before the repair. Prefer strengthening an existing state boundary over adding narrative instructions. A control that does not change a machine decision, evidence requirement, or measurable outcome should not be added to the critical path.
