# Continuity Acceptance Test Matrix

**Document ID:** MV-CONT-TEST-001  
**Version:** 1.3.0
**Status:** ACTIVE

| ID | Scenario | Required result |
|---|---|---|
| CONT-001 | New conversation has only the static restart prompt | Recover bootstrap, pointer, primary branch, and exact checkpoint without an owner-provided summary. |
| CONT-002 | Primary checkpoint is `started` | Resume the recorded first substep; do not select a later roadmap item. |
| CONT-003 | Primary checkpoint is `in_progress` | Inspect pushed work and continue the active substep. |
| CONT-004 | Work is pushed but validation is `not_run` | Run validation before review or completion. |
| CONT-005 | Validation failed previously | Reproduce and repair the recorded failure using saved evidence. |
| CONT-006 | PR exists but is not merged | Keep non-complete status and continue review, CI, repair, merge, and canonical closeout. |
| CONT-007 | Assistant text says complete without evidence | Reject the claim and reconcile from repository evidence. |
| CONT-008 | Roadmap says complete while checkpoint is unfinished | Treat the work as unfinished and queue a bounded roadmap correction. |
| CONT-009 | Merge exists while roadmap projection is pending | Advance from merge evidence without waiting for a full-roadmap rewrite. |
| CONT-010 | Two integration paths claim the same attempt | Repository health rejects concurrent authority; preserve and close the superseded path. |
| CONT-011 | Conversation stops after checkpoint push | Resume without an owner handoff. |
| CONT-012 | Conversation stops during one uncommitted atomic batch | Earlier batches remain durable; only the active batch may need reconstruction. |
| CONT-013 | Repository connector is unavailable | State that canonical progress could not be persisted; do not claim it was saved. |
| CONT-014 | Ordinary failure occurs | Save failure evidence and continue repair without owner intervention. |
| CONT-015 | Owner-only gate occurs | Save the exact decision boundary and stop without losing prior progress. |
| CONT-016 | Selected product work coexists with exclusive maintenance | Preserve one product selector; the maintenance lease blocks feature starts without replacing selection. |
| CONT-017 | Pointer and checkpoint metadata disagree | Validation fails and recovery stops for reconciliation. |
| CONT-018 | Required completion evidence is absent | `completed_verified` is rejected. |
| CONT-019 | Required CI is queued or running | The executable termination preflight returns `CONTINUE_EXECUTION`; poll the existing exact-head work. |
| CONT-020 | Status report is requested with `and continue` | Give the concise status and retain execution mode through the original boundary. |
| CONT-021 | Implementation or an open PR exists but merge/closeout remains | The termination preflight rejects finalization and execution continues. |
| CONT-022 | Bounded work is complete but required successor selection is pending | Select the successor before final response. |
| CONT-023 | `keep going` reaches one completed intermediate tranche | Continue until the owner-named boundary is complete or a genuine blocker occurs. |
| CONT-024 | A blocker is asserted without recovery evidence | The termination preflight rejects the blocker as a stopping reason. |
| CONT-025 | A genuine blocker survives recovery and blocks all authorized progress | Preserve exact evidence and permit a truthful blocked handoff. |
| CONT-026 | Owner explicitly requests `get ready`, status-only, or analysis-only | Complete only that non-execution mode and return control without starting reserved implementation. |
| PERF-001 | Routine substep completes | Run focused validation and continue; do not rewrite durable checkpoint/pointer state. |
| PERF-002 | Work item becomes `completed_verified` | Patch only generated roadmap status and directly affected work-item entries. |
| PERF-003 | Bootstrap begins | Load pointer, checkpoint, roadmap index, and relevant roadmap slice before the full roadmap. |
| PERF-004 | Roadmap projection is pending | Continue from newer evidence while retaining an explicit projection task. |
