# Continuity Acceptance Test Matrix

| ID | Scenario | Required result |
|---|---|---|
| CONT-001 | New conversation has only the static restart prompt | Bootstrap, pointer, active branch, and latest checkpoint are recovered without an owner-provided summary. |
| CONT-002 | Checkpoint status is `started` | Resume the recorded first substep; do not select the next roadmap item. |
| CONT-003 | Checkpoint status is `in_progress` | Inspect pushed work and continue the active substep. |
| CONT-004 | Work files are pushed but validation is `not_run` | Run validation before review or completion. |
| CONT-005 | Validation failed in the prior conversation | Reproduce and repair the recorded failure. |
| CONT-006 | PR exists with passing local tests but no merge | Report non-complete status and continue review/CI/merge workflow. |
| CONT-007 | Assistant text says complete but no completion evidence exists | Reject the claim and reconcile from repository evidence. |
| CONT-008 | Roadmap says complete; checkpoint and active branch show unfinished work | Treat the work as unfinished and queue a roadmap correction. |
| CONT-009 | Merge exists; roadmap has not yet been patched | Use merge evidence to advance while retaining a pending roadmap projection. |
| CONT-010 | Two agents update the same attempt | Expected-revision protection prevents silent overwrite. |
| CONT-011 | Conversation stops after checkpoint push | Next conversation resumes with no owner handoff. |
| CONT-012 | Conversation stops during an uncommitted atomic batch | Earlier batches remain durable; only the active batch may require reconstruction. |
| CONT-013 | Repository connector is unavailable | Explicitly state that canonical progress could not be persisted; do not claim it was saved. |
| CONT-014 | Ordinary CI or implementation failure occurs | Save failure evidence and continue repair without owner intervention. |
| CONT-015 | Owner-only gate occurs | Save the exact decision packet and stop without losing prior progress. |
| PERF-001 | Routine substep completes | Update small checkpoint/status records; do not rewrite the full roadmap. |
| PERF-002 | Work item reaches `completed_verified` | Patch generated roadmap status and affected work-item entry only. |
| PERF-003 | Bootstrap begins | Load pointer, checkpoint, roadmap index, and relevant roadmap slice before loading the full roadmap. |
