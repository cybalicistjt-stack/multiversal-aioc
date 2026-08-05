# Multiversal New Conversation Bootstrap
## Mandatory Repository-First Session Recovery Protocol

**Document ID:** MV-AI-BOOTSTRAP-001  
**Version:** 4.0.0  
**Status:** ACTIVE  
**Owner and final authority:** John Brandon Turner  
**Governance repository:** `cybalicistjt-stack/multiversal-aioc`  
**Application repository:** `cybalicistjt-stack/Multiversal-app`  
**Last updated:** 2026-08-05

## Purpose

This file is the canonical starting point for a new Multiversal conversation. The assistant must recover project state from the repositories before explaining, planning, or claiming work.

## Access and permissions

The active assistant is authorized to use the connected GitHub tools to:

- read both canonical repositories;
- inspect files, branches, commits, pull requests, reviews, and CI;
- create bounded branches;
- create and update repository files;
- open pull requests;
- inspect CI failures and logs;
- repair failures and rerun validation;
- merge verified pull requests using a repository-permitted method;
- continue the owner-authorized P9-06 implementation backlog.

This does not grant authority to create paid services, spend money, expose credentials, deploy production, publish publicly, enroll in paid plans, or make irreversible vendor commitments without a separate owner approval gate.

## Project identity

Multiversal uses two canonical repositories:

- `cybalicistjt-stack/Multiversal-app` — user-facing application and active P9-06 implementation.
- `cybalicistjt-stack/multiversal-aioc` — governance, Development Brain, source intake, canonical content, validation, roadmap, AI coordination, and bootstrap authority.

John Brandon Turner is owner and final authority. `zakvalentine` remains proposal-only unless a newer registry entry explicitly changes that status.

## Mandatory initialization sequence

1. Confirm connected GitHub read/write access to both repositories.
2. Read this file from:
   - repository: `cybalicistjt-stack/multiversal-aioc`
   - path: `governance/ai/MULTIVERSAL_NEW_CONVERSATION_BOOTSTRAP.md`
3. Read and enforce:
   - `governance/access/AIOC_CONTRIBUTOR_REGISTRY.json`
   - `governance/current-state/AIOC_CURRENT_STATE.md`
   - `governance/current-state/SESSION_HANDOFF.md`
   - `governance/current-state/AIOC_OPERATIONAL_HANDOFF.md`
   - `governance/current-state/AIOC_DEPLOYMENT_BASELINE.md`
   - `governance/application-planning/APPLICATION_IMPLEMENTATION_ROADMAP.md`
   - `governance/object-system/CANONICAL_OBJECT_TEMPLATE_PROGRAM.md`
   - `governance/development-brain/README.md`
   - `governance/content-recovery/CONTENT_RECOVERY_ROADMAP.md`
   - `governance/project-memory/PROJECT_MEMORY.json`
4. Inspect recent commits, open PRs, active branches, and CI in both repositories, prioritizing `cybalicistjt-stack/Multiversal-app` for the active implementation workstream.
5. Verify the latest merged P9-06 item and resume the exact next unfinished item unless John changes direction.
6. When repository evidence is newer than a handoff document, trust the repository evidence and update the stale governance document through a verified PR.

## Mandatory behavioral rules

### Execution first

- “Continue” means execute the next verified unfinished operation.
- Do not answer “Continue” with only a plan, explanation, or restatement.
- Perform repository work in the current response; do not promise background work.
- Do not ask for confirmation when John has already authorized the work.

### Truthfulness

- Never claim a file, commit, branch, PR, merge, test, CI result, artifact, deployment, or completion without tool verification.
- If a tool action fails, say what failed, fix it when possible, and continue.
- Do not conceal mistakes or describe intended work as completed work.

### Approved recommendation process

John has approved using the assistant’s best recommendation for ordinary ambiguities. The assistant should:

- identify the most reasonable reversible choice;
- use it without repeatedly asking John;
- record the decision and rationale where governance requires it;
- stop only for a genuine owner-only decision, irreversible choice, spending, production credentials, deployment, or release approval.

### Efficient tranches

- Combine compatible field verification, runtime validation, identity checks, compatibility checks, migration checks, and repairs when they can safely be completed together.
- Avoid artificially splitting work into many tiny conversational steps.
- Continue automatically through ordinary failures and corrections.

### CI and verification

- Inspect failed CI jobs and logs.
- Correct the root cause.
- Rerun or trigger new CI through a follow-up commit.
- Merge only after required checks pass and the PR is mergeable.
- Use the repository-permitted merge method. `Multiversal-app` may require squash rather than merge commits.

### Reporting

After completing a step, report:

- the exact backlog item or work package;
- PR number and merge/squash commit;
- what was actually added or changed;
- CI or test result;
- any preserved restrictions;
- the exact next step.

Keep explanations practical for a non-professional programmer.

## Current verified project state

### Completed foundations

- Phase 0 legacy PDF content creation: complete.
- Phase 0.5 Multiversal Definition Document: complete.
- Phases 1–7 planning, architecture, UI/workflow design, and repository governance: complete.
- Phase 8 canonicalization, validation, content conversion, balance harness, and AI Development Team Operating Package: complete.
- 8E-009 final state: 20 governed datasets, 19,199 source rows, 19,199 promoted records, zero unprocessed rows, passing provenance/runtime/install/uninstall validation.
- 8D-007 Golden Test Corpus and Balance Harness: complete.
- 8D-008 AI Development Team Operating Package: complete.

### Canonical Phase 9

The uploaded Phase 9 package is authoritative. Completed:

- P9-01 entitlements and freemium architecture;
- sponsored-month amendment;
- P9-02 authoritative session architecture;
- P9-03 technology decision package;
- P9-04 Postgres-centered provider-neutral architecture contract;
- P9-05 bounded technical spike and cost envelope;
- P9-06 implementation backlog and acceptance gates.

John authorized bounded implementation of **P9-06-001 through P9-06-023**.

### Completed P9-06 application work

In `cybalicistjt-stack/Multiversal-app`:

1. P9-06-001 — complete, PR #71.
2. P9-06-002 — complete, PR #72.
3. P9-06-003 — complete, PR #73; AG-01 complete.
4. P9-06-004 — complete, PR #74.
5. P9-06-005 — complete, PR #75.
6. P9-06-006 — complete, PR #76.
7. P9-06-007 — complete, PR #77; squash commit `149b866f530f3a8896170bfe3ba6af0c01fb2f72`.

## Active workstream

**P9-06 bounded application implementation** in `cybalicistjt-stack/Multiversal-app`.

## Current next executable action

**P9-06-008 — Implement backup, restore, and provider-exit export ports.**

Required characteristics:

- provider-neutral interfaces;
- deterministic backup manifest and integrity checksum behavior;
- restore planning, validation, execution, and receipts;
- complete provider-exit export with identities, entitlements, session state, audit/provenance, and schema/version metadata as applicable;
- recovery and corruption failure results;
- schemas, fixtures, validator, dedicated CI;
- no hosted backup provider, credentials, paid service, production data, or deployment.

After P9-06-008, continue through the dependency-ordered authorized backlog to P9-06-023 unless an owner-only gate is reached.

## Later roadmap

- Phase 10 — Core Application Implementation.
- Phase 11 — GM and Player Experience.
- Phase 12 — AI Team and Automation.
- Phase 13 — Internal Alpha Completion.
- Then formal closed-alpha, beta, commercial-readiness, production-release, and public-launch governance.

## Mac-dependent parallel track

`WP-011 — Tauri iOS/iPadOS Spike` remains separate. The borrowed Mac is a one-time Apple-only environment for Xcode, signing, provisioning, simulator/device validation, and packaging. Minimize Mac time, prepare everything possible beforehand, and remove project material afterward.

## Recovery rule

If this bootstrap conflicts with newer verified repository state, follow the newer evidence, update this file through a validated PR, and never silently continue from stale assumptions.
