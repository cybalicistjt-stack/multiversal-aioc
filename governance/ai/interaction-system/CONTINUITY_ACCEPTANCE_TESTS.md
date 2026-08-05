# Continuity Acceptance Test Matrix

**Document ID:** MV-CONT-TEST-001  
**Version:** 1.0.0  
**Status:** ACTIVE

| ID | Scenario | Required result |
|---|---|---|
| CONT-001 | New conversation has only the static restart prompt | Recover bootstrap, pointer, primary branch, and exact checkpoint without an owner-provided summary. |
| CONT-002 | Primary checkpoint is `started` | Resume the recorded first substep; do not select a later roadmap item. |
| CONT-003 | Primary checkpoint is `in_progress` | Inspect pushed work and continue the active substep. |
| CONT-004 | Work is pushed but validation is `not_run` | Run validation before review or completion. |
| CONT-005 | Validation failed previously | Reproduce and repair the recorded failure using saved evidence. |
| CONT-006 | PR exists but is not merged | Keep non-complete status and continue review, CI, repair, and merge. |
| CONT-007 | Assistant text says complete without evidence | Reject the claim and reconcile from repository evidence. |
| CONT-008 | Roadmap says complete while checkpoint is unfinished | Treat the work as unfinished and queue a bounded roadmap correction. |
| CONT-009 | Merge exists while roadmap projection is pending | Advance from merge evidence without waiting for a full-roadmap rewrite. |
| CONT-010 | Two agents update the same attempt | Expected-revision protection prevents silent overwrite. |
| CONT-011 | Conversation stops after checkpoint push | Resume without an owner handoff. |
| CONT-012 | Conversation stops during one uncommitted atomic batch | Earlier batches remain durable; only the active batch may need reconstruction. |
| CONT-013 | Repository connector is unavailable | State that canonical progress could not be persisted; do not claim it was saved. |
| CONT-014 | Ordinary failure occurs | Save failure evidence and continue repair without owner intervention. |
| CONT-015 | Owner-only gate occurs | Save the exact decision boundary and stop without losing prior progress. |
| CONT-016 | Multiple parallel attempts exist | Exactly one primary attempt is selected; no active attempt is silently replaced. |
| CONT-017 | Pointer and checkpoint metadata disagree | Validation fails and recovery stops for reconciliation. |
| CONT-018 | Required completion evidence is absent | `completed_verified` is rejected. |
| PERF-001 | Routine substep completes | Update checkpoint, pointer, and compact status only. |
| PERF-002 | Work item becomes `completed_verified` | Patch only generated roadmap status and directly affected work-item entries. |
| PERF-003 | Bootstrap begins | Load pointer, checkpoint, roadmap index, and relevant roadmap slice before the full roadmap. |
| PERF-004 | Roadmap projection is pending | Continue from newer evidence while retaining an explicit projection task. |
