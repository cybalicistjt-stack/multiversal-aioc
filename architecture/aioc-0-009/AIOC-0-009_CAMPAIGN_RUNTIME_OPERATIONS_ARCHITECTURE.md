# AIOC-0-009 — Campaign and Runtime Operations Architecture

## 1. Purpose

Define the AIOC command-center architecture for monitoring and coordinating live Multiversal campaigns, sessions, deployments, runtime approvals, incidents, operational health, and recovery while preserving owner, GM, player, moderator, and repository authority boundaries.

## 2. Scope

The architecture covers campaign registration, runtime environments, session lifecycle, participant and device presence, operational commands, approval routing, runtime telemetry, health checks, incidents, maintenance windows, deployments, rollback, backups, diagnostics, support bundles, notifications, audit receipts, and cross-repository traceability.

## 3. Governing Principles

1. AIOC coordinates; the game runtime remains authoritative for gameplay state.
2. Every operational action is identity-bound, permission-checked, idempotent, and auditable.
3. Owner and GM authority are never inferred from hosting or infrastructure roles.
4. Runtime operations never expose hidden campaign information outside authorized scope.
5. Destructive or high-impact actions require explicit approval and rollback readiness.
6. AIOC must distinguish planned maintenance, degraded operation, incident response, and emergency containment.
7. Observability data is privacy-minimized and content-free by default.
8. Every campaign and runtime environment remains traceable to builds, schemas, packs, deployments, and repositories.
9. Recovery never fabricates events or silently rewrites authoritative history.
10. Human authority remains final for irreversible actions.

## 4. Core Domain Objects

- Campaign Operations Record
- Runtime Environment
- Runtime Session
- Participant Presence Record
- Operational Command
- Approval Request
- Deployment Record
- Maintenance Window
- Health Snapshot
- Runtime Alert
- Incident Record
- Recovery Plan
- Backup Record
- Diagnostic Bundle
- Operational Receipt
- Escalation Policy

## 5. Campaign Registration

Each campaign registered with AIOC records:

- campaign ID and display name;
- owner and delegated administrators;
- authorized GMs;
- linked Multiversal App environment;
- repository and build references;
- pack and schema bindings;
- privacy classification;
- deployment profile;
- backup and retention policy;
- operational contacts;
- current health and lifecycle state.

AIOC registration does not create campaign authority. It mirrors verified authority from canonical systems.

## 6. Runtime Environment Model

Supported environment classes:

- local development;
- test;
- internal alpha;
- closed alpha;
- staging;
- production;
- offline local host;
- LAN host;
- peer-assisted host;
- hosted service;
- disaster-recovery environment.

Each environment declares build ID, protocol version, schema versions, pack bindings, platform profile, secrets scope, health endpoint, backup policy, deployment policy, and operational limits.

## 7. Session Lifecycle

```text
Planned -> Preparing -> Ready -> Active -> Paused -> Recovering -> Completed -> Archived
                         |        |          |
                         +------ Cancelled --+
```

A session record includes campaign, environment, participants, devices, host, authoritative sequence, checkpoint, current scene, operational locks, incident state, and privacy scope.

## 8. Operational Commands

Representative commands:

- RegisterCampaignOperations
- CreateRuntimeEnvironment
- ScheduleSession
- StartSession
- PauseSession
- ResumeSession
- EndSession
- RequestRuntimeApproval
- ApproveRuntimeOperation
- RejectRuntimeOperation
- ScheduleMaintenance
- StartDeployment
- PromoteDeployment
- RollBackDeployment
- CreateRuntimeIncident
- ContainRuntimeIncident
- StartRuntimeRecovery
- RestoreBackup
- GenerateDiagnosticBundle
- CloseRuntimeIncident

Commands never mutate gameplay state directly. They invoke governed application or infrastructure interfaces.

## 9. Approval Classes

- informational;
- routine operator approval;
- GM approval;
- campaign-owner approval;
- repository-maintainer approval;
- security approval;
- emergency dual approval.

Approval policy is derived from action type, environment, campaign classification, affected users, reversibility, and blast radius.

## 10. Health and Observability

AIOC tracks:

- availability;
- command admission latency;
- event-sequence continuity;
- snapshot freshness;
- queue depth;
- reconnect rate;
- participant and device presence;
- host health;
- storage health;
- pack and schema compatibility;
- backup age;
- deployment state;
- moderation and communication service state;
- privacy-safe error counts.

Raw campaign text, private messages, hidden notes, credentials, and full event payloads are excluded by default.

## 11. Alert Severity

- Info — no action required.
- Advisory — review when convenient.
- Warning — operational degradation exists.
- Major — user-visible failure or elevated risk.
- Critical — authority, history, privacy, security, or availability at immediate risk.

Alerts deduplicate by campaign, environment, detector, and causal incident.

## 12. Incident Management

Incident states:

```text
Detected -> Triaged -> Contained -> Recovering -> Monitoring -> Resolved -> Archived
                         |                               |
                         +-------- Unrecoverable --------+
```

Every incident records detection source, severity, campaign and environment scope, last known good state, affected participants, evidence, containment, recovery, communications, approvals, root cause, corrective actions, and closure authority.

## 13. Deployment Operations

Deployment records contain source commit, build ID, artifact hashes, target environments, schema and pack compatibility, migration plan, backup checkpoint, approval evidence, rollout plan, health gates, rollback trigger, and final disposition.

AIOC supports dry-run, canary, staged, full, rollback, and emergency-disable operations.

## 14. Backup and Recovery

AIOC tracks backup creation, verification, retention, restore tests, encryption, location, campaign scope, event-sequence position, snapshot references, and recovery point objectives.

Restore requires environment isolation, authority confirmation, integrity verification, replay-gap analysis, projection rebuild, hidden-information checks, and post-restore monitoring.

## 15. Cross-Repository Traceability

Operational records link to:

- `cybalicistjt-stack/Multiversal-app` commits, builds, releases, issues, and pull requests;
- `cybalicistjt-stack/multiversal-aioc` work orders, policies, tests, incidents, and decisions;
- content pack IDs and versions;
- schema IDs and versions;
- campaign and runtime identifiers.

## 16. AI Assistance Boundaries

AI may summarize health, classify incidents, propose runbook steps, draft notices, compare deployments, identify likely regressions, and recommend escalation.

AI may not independently approve high-impact operations, expose hidden content, rotate secrets, delete authoritative history, promote production deployments, or close critical incidents without authorized human approval.

## 17. Offline and Degraded Operation

When AIOC or GitHub is unavailable, local runtime operation continues according to campaign policy. AIOC queues non-destructive records, preserves timestamps and identities, and reconciles after reconnection. It never treats delayed synchronization as proof an operation occurred.

## 18. Accessibility and UX

The operations UI must support keyboard navigation, screen readers, text scaling, high contrast, color-independent severity, reduced motion, accessible timelines, clear approval summaries, and plain-language recovery guidance.

## 19. Security Requirements

- least-privilege access;
- explicit environment scoping;
- short-lived credentials;
- secret redaction;
- replay protection;
- signed operational receipts;
- rate and payload limits;
- device and session revocation;
- protected production actions;
- immutable audit history;
- emergency containment controls.

## 20. Performance Targets

- dashboard health refresh: under 2 seconds;
- command acknowledgement: under 500 ms excluding external execution;
- critical alert creation: under 1 second;
- approval notification: under 2 seconds;
- incident record creation: under 1 second;
- common operational search: under 1 second;
- local continuity restoration: under 5 seconds for normal project state.

## 21. Acceptance Criteria

AIOC-0-009 is complete when the architecture defines campaign registration, runtime environments, session lifecycle, operational commands, approvals, observability, alerts, incidents, deployments, backups, recovery, diagnostics, AI boundaries, security, accessibility, cross-repository traceability, schemas, validation rules, and tests.

## 22. Final Invariants

- Infrastructure roles never silently grant campaign authority.
- AIOC never becomes the authoritative gameplay event store.
- Every high-impact operation has approval, evidence, and rollback readiness.
- Hidden information remains filtered through all operational surfaces.
- Recovery preserves history and never fabricates events.
- Repository, build, schema, pack, campaign, and runtime provenance remain traceable.
