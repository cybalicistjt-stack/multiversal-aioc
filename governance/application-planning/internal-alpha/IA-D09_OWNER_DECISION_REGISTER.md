# IA-D09 — Owner-Decision Register

## Purpose

Separate ordinary reversible engineering work from decisions that require John Brandon Turner as owner and final authority.

## Owner-only gates

| Gate | Earliest point | Required evidence before decision | Default without decision |
|---|---|---|---|
| authorize Internal Alpha tester access | after a candidate is built and validated | candidate identity, validation summary, known limitations, data/privacy boundary, recovery procedure | no tester access |
| authorize real-user data collection | before any non-synthetic collection | data inventory, purpose, retention, privacy/security controls | synthetic/test data only |
| authorize production credentials | before production credential creation/use | provider/service, scope, secret handling, rollback/revocation path | no production credentials |
| authorize paid provider commitment | before spend/plan commitment | expected cost, limits, free/manual fallback, cancellation path | no paid commitment |
| approve Internal Alpha release | after release evidence bundle | exact build, required validations, unresolved-risk register, supported platforms, tester-entry package | candidate remains unreleased |
| approve public release or deployment | separate later gate | production readiness and explicit release package | no public release/deployment |
| promote AI/automation to broader authority | only after separate governance design and owner approval | authority model, permissions, audit, rollback, failure containment | AI remains advisory/proposal-only |
| promote working/noncanonical design standards | after inventory, audit, ID reconciliation, governed repository review | accepted canonical mappings and merge evidence | remain working/noncanonical |

## Decisions not required for IA-D09 completion

The following remain authorized ordinary repository work when bounded by existing governance:

- complete the IA-D09 design package;
- create/update its validator and narrow workflow;
- update backlog, roadmap projection, runtime checkpoint, and status projection;
- open and merge the governed IA-D09 PR after declared checks pass;
- preserve P9-06-008-attempt-002 and Design Standards Completion as paused tracks.

## Current decision state

No owner-only gate must be resolved to complete IA-D09 design work. All release, tester-access, production, spending, and public-access gates remain closed by default.