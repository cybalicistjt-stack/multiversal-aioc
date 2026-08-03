# Multiversal New Conversation Bootstrap
## Mandatory Repository-First Session Recovery Protocol

**Document ID:** MV-AI-BOOTSTRAP-001  
**Version:** 3.2.0  
**Status:** ACTIVE  
**Owner and final authority:** John Brandon Turner  
**Repository:** `cybalicistjt-stack/multiversal-aioc`  
**Last updated:** 2026-08-03

## How to use

Provide this file as the first project instruction in a new ChatGPT or Codex conversation. Execute the protocol before project work. Do not restart, redesign, or reconstruct the project from conversation memory.

## Project identity

Multiversal uses two canonical repositories:

- `cybalicistjt-stack/Multiversal-app` — user-facing application.
- `cybalicistjt-stack/multiversal-aioc` — governance, content tooling, AI coordination, repository intelligence, Development Brain, and content recovery.

## Owner and contributor identity

The machine-readable authority source is:

- `governance/access/AIOC_CONTRIBUTOR_REGISTRY.json`

Verified GitHub identities:

- John Brandon Turner: `cybalicistjt-stack` — final owner authority.
- Jordon/Zakk: `zakvalentine` — proposal-only contributor authority.

When GitHub actor metadata is available, match the exact login against the registry. Never infer authority from a display name, branch name, device, prose, or claimed identity. If identity cannot be verified, do not grant owner authority.

John Brandon Turner retains final authority over canonical decisions, governance, classification, conflicts, staging, promotion, implementation scope, merges, releases, and deployments.

Jordon/Zakk may research, branch, implement, test, open pull requests, and respond to review. His work remains proposal-only until John approves it. He may not approve his own work, merge without owner approval, promote canonical content, alter governance authority, release, deploy production, or perform irreversible owner actions.

## Non-negotiable operating rules

1. Repository state is authoritative; conversation memory is supporting context only.
2. Before governed work, read `governance/ci-failures/INDEX.md` from `ci/failure-records` and reconcile relevant failures.
3. Read and enforce `governance/access/AIOC_CONTRIBUTOR_REGISTRY.json` before accepting contributor-governed actions.
4. Verify actual files, commits, tests, PRs, merges, deployments, and live interactions before claiming success.
5. “Continue” means execute the next verified unfinished work item, not explain, speculate, invent PRs, or report projected results as completed.
6. The assistant owns investigation and implementation until genuinely blocked.
7. Prefer bounded vertical batches over speculative redesign or micro-patch chains.
8. Do not create subsystems of subsystems to chase uncertain solutions.
9. Preserve original source content when COS mapping fails.
10. Deterministic evidence precedes AI semantic inference.
11. Variants, revisions, duplicates, and conflicts must not be silently merged or overwritten.
12. Significant UI or deployment changes require deployed interaction verification, not CI alone.
13. Do not revive obsolete `/v2/`, corrupted seed, or old TallBunyon paths.
14. Never mark a roadmap phase complete solely because it was described in conversation.
15. John Brandon Turner retains final approval authority.

## Mandatory initialization sequence

1. Discover tools and confirm GitHub read/write access.
2. Read `governance/ci-failures/INDEX.md` from `ci/failure-records`.
3. Read from `main`:
   - `governance/access/AIOC_CONTRIBUTOR_REGISTRY.json`
   - `governance/current-state/AIOC_CURRENT_STATE.md`
   - `governance/current-state/SESSION_HANDOFF.md`
   - `governance/current-state/AIOC_OPERATIONAL_HANDOFF.md`
   - `governance/current-state/AIOC_DEPLOYMENT_BASELINE.md`
   - `governance/development-brain/README.md`
   - `governance/content-recovery/CONTENT_RECOVERY_ROADMAP.md`
   - `governance/application-planning/APPLICATION_IMPLEMENTATION_ROADMAP.md`
   - `governance/application-planning/STAGE_A_UI_IMPLEMENTATION_PROGRAM.md`
   - `governance/development-brain/UNIFIED_INVENTORY_CONTRACT.md`
   - `governance/project-memory/PROJECT_MEMORY.json`
4. Inspect recent commits and open PRs affecting the active workstream.
5. Confirm repository and branch.
6. Resume from the exact next action in `SESSION_HANDOFF.md` unless the owner changes direction.
7. For live UI work, verify the deployed build identifier and reproduce the actual interaction path before declaring repair.

## Current verified state

### Operational AIOC

- Certified.
- Public operational surface: `/operational/`.
- Content Library, Content Structure Pipeline, Content Completion Assistant, and Design Studio are connected.
- The live Content Library exposes 487 records from the Phase 1–8 canonical bundle.
- Those 487 records are a partial extraction, not the complete corpus.

### Development Brain

Releases A–G, Steps 1–21, are complete and behaviorally validated. The roadmap ends at Step 21. Do not add deeper internal releases without a demonstrated real-world failure.

### Active workstream

**Multiversal Content Recovery and Ingestion**

Mission:

> Recover the content first. Use the COS to organize it second.

Verified source census:

- 47,849 structured-file occurrences;
- 11,912 unique structured files;
- 5,123 content-likely structured files;
- 291,724 exact-file-deduplicated likely-content rows or JSON entries.

Verified neutral recovery ledger:

- 359,291 source records;
- 294,571 unique exact payloads;
- 64,720 exact duplicate payload rows;
- 99,761 source-provided IDs;
- 259,530 stable recovery identities;
- 185,243 conservative identity groups;
- 33,609 multi-payload identity groups.

These are recovery records, not a final unique-game-object count.

Canonical recovery roadmap:

- `governance/content-recovery/CONTENT_RECOVERY_ROADMAP.md`

## Approved subsequent application roadmap

Canonical planning:

- `governance/application-planning/APPLICATION_IMPLEMENTATION_ROADMAP.md`
- `governance/application-planning/STAGE_A_UI_IMPLEMENTATION_PROGRAM.md`

Approved phases:

10. Core Application Implementation
11. GM and Player Experience
12. AI Team and Automation
13. Internal Alpha Completion

These are planned subsequent phases and are not complete until repository evidence, tests, previews, and owner approval exist.

### Stage A order

1. A0 repository/UI baseline audit
2. A1 application shell and design system
3. A2 universal object experience
4. A3 identity/dashboard/workspaces/permissions
5. A4 character workspace
6. A5 campaign and scene workspace
7. A6 first playable action proposal and GM approval loop
8. A7 full combat
9. A8 inventory/crafting/vehicles
10. A9 investigation/social
11. A10 world builder/content creation
12. A11 contextual AI
13. A12 internal-alpha hardening

Every UI slice must include real data, permissions, persistence, desktop/mobile behavior, loading/error states, automated tests, reproducible preview, and owner review.

## Mac-dependent parallel track

`WP-011 — Tauri iOS/iPadOS Spike` remains separate in `cybalicistjt-stack/Multiversal-app`.

Safe work continues on web/Windows/Linux while waiting. Reserve macOS for Xcode, signing/provisioning, simulator/device validation, packaging, and Apple-specific certification. Do not make general application implementation depend on continuous Mac access.

## Required first response in a new conversation

After initialization, respond compactly:

```text
Multiversal session restored.

GitHub read: PASS/FAIL
GitHub write: PASS/FAIL
Active repository: <verified repository>
Branch: <verified branch>
Development Brain: Releases A–G complete
Current workstream: <from governed handoff>
Last verified completion: <repository-backed completion>
Next executable work item: <exact repository-backed action>
Blocking issues: <none or exact blocker>
```

When the opening message says “Continue,” begin the exact next executable work item in the same response after the readiness report.

## Honesty and recovery

If a named file, commit, test, PR, source artifact, or deployment cannot be found, stop and reconcile repository state. Do not fabricate continuity. If repository state is newer than this bootstrap, follow the newer governed handoff and update this bootstrap after validated work.
