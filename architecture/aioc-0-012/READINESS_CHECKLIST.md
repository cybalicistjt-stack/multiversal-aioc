# AIOC-0-012 Readiness Checklist

| Gate | Result | Required implementation control |
|---|---|---|
| Canonical repository identified | PASS | Verify repository before every write |
| Canonical current state exists | PASS | Update after every completed tranche |
| Architecture packages 001–011 accounted for | PASS | Preserve dependency order |
| App and AIOC repositories separated | PASS | Route writes by workstream |
| Stable record identity defined | PASS | Enforce for all new persistent records |
| Schemas and versioning represented | PASS | Validate at boundaries and migration points |
| Permission model defined | PASS | Default deny for protected operations |
| Approval model defined | PASS | Require evidence-bearing approval records |
| Secret handling defined | PASS | No secrets in repository or local storage |
| Audit and provenance defined | PASS | Append-only evidence for governed actions |
| Offline and recovery defined | PASS | Test interrupted-write and restore paths |
| AI assistant bounded | PASS | Separate answer, proposal, approval, execution |
| GM runtime authority bounded | PASS | Preserve owner/GM control and alteration evidence |
| Release governance defined | PASS | Disable release actions until gates pass |
| Acceptance tests specified | PASS | Convert architecture tests into executable suites |
| Smoke tests currently passing | PASS, owner reported | Keep smoke workflow blocking on implementation PRs |
| Implementation slices identified | PASS | Begin with AIOC-I-001A |
| Continuity protocol implemented | PASS | Bootstrap and current-state files remain mandatory |

## Blocking conditions for implementation

Implementation must stop if any of the following occurs:

- active repository or branch cannot be verified;
- a persistent record lacks a stable ID or schema version;
- a protected action can bypass permission or approval checks;
- secrets are written to browser storage, logs, artifacts, or Git;
- a migration can overwrite data without a backup and rollback path;
- smoke tests or contract tests fail;
- current-state documentation materially disagrees with repository evidence.
