# AIOC-0-012 Cross-Package Traceability

| Package | Primary responsibility | Operational Core dependency |
|---|---|---|
| AIOC-0-001 | Command-center foundation | Shell, navigation, state ownership |
| AIOC-0-002 | Feature preservation | Regression and capability inventory |
| AIOC-0-003 | COS runtime extensions | Shared operational primitives |
| AIOC-0-004 | Commands, events, projections, automations | Work-ledger command/event contracts |
| AIOC-0-005 | Local data, indexing, evidence, search | Persistent records, indexes, provenance |
| AIOC-0-006 | Agent orchestration and credit optimization | Assignment, routing, budgets, agent status |
| AIOC-0-007 | Developer Workbench | Implementation, review, testing, diagnostics |
| AIOC-0-008 | Content Studio | Governed authoring and content validation |
| AIOC-0-009 | Campaign and runtime operations | Runtime workspaces, approvals, replay, recovery |
| AIOC-0-010 | AI Assistant and GM intelligence | Context assembly, bounded proposals, explanations |
| AIOC-0-011 | Security, permissions, secrets, releases | Identity, authorization, protected operations |
| AIOC-0-012 | Readiness gate | Implementation authorization and controls |

## First vertical implementation chain

1. Project state record and schema.
2. Work-package ledger and dependency graph.
3. Decision, blocker, evidence, and handoff records.
4. Deterministic next-work resolver.
5. `Continue` command producing a proposed execution record.
6. Permission and approval evaluation.
7. Audit event and state transition.
8. Dashboard projection.
9. Backup, restore, migration, and smoke tests.
10. GitHub read adapter, initially read-only.

## Traceability rule

Every implementation task must cite:

- the architecture package that authorizes it;
- the schema or contract it implements;
- its acceptance tests;
- the repository files changed;
- its migration and rollback behavior;
- the evidence proving completion.
