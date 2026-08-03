# Multiversal New Conversation Bootstrap
## Mandatory Repository-First Session Recovery Protocol

**Document ID:** MV-AI-BOOTSTRAP-001  
**Version:** 3.0.0  
**Status:** ACTIVE  
**Owner and final authority:** John Brandon Turner  
**Repository:** `cybalicistjt-stack/multiversal-aioc`  
**Last updated:** 2026-08-03

## How to use

Provide this file as the first project instruction in a new ChatGPT or Codex conversation. The assistant must execute this recovery protocol before project work. Do not restart, redesign, or reconstruct the project from memory.

## Project identity

Multiversal uses two distinct canonical repositories:

- `cybalicistjt-stack/Multiversal-app` — the user-facing Multiversal application.
- `cybalicistjt-stack/multiversal-aioc` — governance, content tooling, AI coordination, repository intelligence, operational surfaces, Development Brain, and the active content-recovery workstream.

The active work described here belongs to `cybalicistjt-stack/multiversal-aioc`.

## Owner authority and contributor boundary

John Brandon Turner retains full and final authority over:

- canonical decisions;
- repository governance;
- classification policy;
- conflict and variant resolution;
- staging acceptance;
- promotion and production migration;
- merges and releases.

Other contributors, including Jordon/Zakk, may research, branch, implement, test, and open pull requests, but their work remains proposal-only until John approves it. They may not approve their own work, alter governance authority, or treat AI output as an owner decision.

## Non-negotiable operating rules

1. Repository state is authoritative; conversation memory is supporting context only.
2. Before every governed operation, read `governance/ci-failures/INDEX.md` from branch `ci/failure-records` and repair any unresolved failure first.
3. Verify actual tool, test, artifact, merge, deployment, and live-site results before claiming success.
4. “Continue” means execute the next verified unfinished work item, not explain what someone else should do.
5. The assistant owns investigation and implementation until genuinely blocked by missing access or evidence.
6. Prefer bounded, coherent vertical batches over repeated micro-patches or speculative redesign.
7. Do not create subsystems of subsystems to chase uncertain solutions.
8. Never mix canonical content, recovered source payloads, shared drafts, proposals, staging imports, and promoted production records.
9. Significant UI or deployment changes must be verified against the deployed build, not CI alone.
10. Do not revive the obsolete `/v2/` migration shell, corrupted seed path, or old TallBunyon repository.
11. Preserve original source content even when current COS mapping fails.
12. Deterministic evidence must precede AI semantic inference.
13. Variants and conflicts must not be silently merged or overwritten.
14. John Brandon Turner retains final approval authority.

## Mandatory initialization sequence

Execute these steps in order:

1. Discover available tools and confirm GitHub read/write access.
2. Read `governance/ci-failures/INDEX.md` from `ci/failure-records`.
3. Read these files from `main`:
   - `governance/current-state/AIOC_CURRENT_STATE.md`
   - `governance/current-state/SESSION_HANDOFF.md`
   - `governance/current-state/AIOC_OPERATIONAL_HANDOFF.md`
   - `governance/current-state/AIOC_DEPLOYMENT_BASELINE.md`
   - `governance/development-brain/README.md`
   - `governance/content-recovery/CONTENT_RECOVERY_ROADMAP.md`
   - `governance/development-brain/UNIFIED_INVENTORY_CONTRACT.md`
   - `governance/project-memory/PROJECT_MEMORY.json`
4. Inspect recent commits and open pull requests affecting the active workstream.
5. Confirm the active repository and branch.
6. Resume from the exact next action in `SESSION_HANDOFF.md` unless the owner explicitly changes direction.
7. If a live UI issue is involved, verify the deployed build identifier and reproduce the actual interaction path before declaring it repaired.

## Current verified state

### Operational AIOC

- Operational AIOC is certified.
- The public operational surface is `/operational/`.
- The Content Library, Content Structure Pipeline, Content Completion Assistant, and Design Studio are connected.
- Browser-local durability exists through backup and export/import mechanisms.
- The live Content Library currently exposes 487 records from the Phase 1–8 canonical bundle.
- Those 487 records are a partial extraction and must not be represented as the complete Multiversal content corpus.
- Content Library mobile selection has dedicated click and pointer/touch regression coverage.

### Development Brain

Releases A–G, Steps 1–21, are complete and behaviorally validated.

The Development Brain roadmap ends at Step 21. Do not add deeper internal releases unless a specific real-world failure demonstrates a missing capability.

The Development Brain remains advisory and non-executing. It cannot grant owner approval, merge changes, silently mutate canonical content, promote records, or resolve content conflicts.

### Active governed workstream

**Multiversal Content Recovery and Ingestion**

Mission:

> Recover the content first. Use the COS to organize it second.

The owner does not authorize manually recreating years of existing game content.

Verified source census:

- 47,849 structured-file occurrences;
- 11,912 unique structured files;
- 5,123 unique content-likely structured files;
- 291,724 exact-file-deduplicated likely-content rows or JSON entries.

Verified neutral recovery ledger:

- 359,291 source records;
- 294,571 unique exact payloads;
- 64,720 exact duplicate payload rows;
- 99,761 source-provided IDs;
- 259,530 stable recovery identities;
- 185,243 conservative identity groups;
- 33,609 identities with multiple distinct payloads.

These figures are not a final count of unique game objects. They include primary assets, relationship rows, indexes, mappings, embedded mechanics, reports, and support records.

## Recovery doctrine

The recovery workstream must:

- preserve complete original payloads and provenance;
- use explicit IDs, types, pack metadata, source files, workbook sheets, field names, directories, and cross-references before semantic inference;
- separate primary assets from relationships, support records, indexes, reports, governance, and technical artifacts;
- preserve exact duplicates with occurrence traceability;
- preserve revisions, variants, alternate forms, and conflicts;
- allow records to exist as `native-cos`, `cos-mapped`, `partially-mapped`, `structured-raw`, `unresolved`, or `support-record`;
- use staging before production migration;
- retain the existing 487-record database as a restorable named collection;
- require representative sample review before domain promotion;
- measure success against reconciled source coverage, not the current live count.

## Active roadmap

Canonical roadmap:

- `governance/content-recovery/CONTENT_RECOVERY_ROADMAP.md`

Phases:

0. Preserve and freeze
1. Deterministic Classification Contract
2. Primary assets versus support records
3. Identity, version, and variant groups
4. Domain recovery passes
5. Lossless library import format
6. Staging Content Library integration
7. Coverage and quality validation
8. Production migration
9. Gradual COS normalization

Estimated work through production certification: 26–36 bounded batches.

## Exact next executable work item

**Phase 0 — Preserve and Freeze, followed immediately by Phase 1 — Deterministic Classification Contract.**

Execute one bounded foundation batch:

1. Preserve and checksum the source-census and neutral-recovery-ledger evidence.
2. Snapshot the current 487-record database and deployed Content Library fingerprint.
3. Define a machine-readable classification contract with:
   - record classes;
   - evidence precedence;
   - mapping states;
   - confidence levels;
   - conflict and fallback behavior.
4. Build a mixed-domain representative fixture containing examples from abilities, species, items, creatures, NPCs, vehicles, environments, settings/adventures, rules, relationships, reports, and technical artifacts.
5. Record expected outcomes from objective source evidence.
6. Run deterministic validation and report observed failures honestly.
7. Update current state and handoff only after the fixture passes review.

**Hard gate:** Do not classify the entire 359,291-row ledger until the representative fixture passes review.

## Separate external work item

`WP-011 — Tauri iOS/iPadOS Spike` remains the separate Mac-dependent Multiversal App task. It must not displace the active recovery workstream unless the owner explicitly switches priorities.

## Required first response in a new conversation

After initialization, respond compactly:

```text
Multiversal session restored.

GitHub read: PASS/FAIL
GitHub write: PASS/FAIL
Active repository: cybalicistjt-stack/multiversal-aioc
Branch: main
Development Brain: Releases A–G complete
Current workstream: Multiversal Content Recovery and Ingestion
Last verified completion: Source census and neutral recovery ledger
Next executable work item: Phase 0/1 recovery foundation and deterministic classification fixture
Blocking issues: <none or exact blocker>
```

If the opening message says “Continue,” begin the exact next executable work item in the same response after the readiness report.

## Honesty and recovery

If a named file, source artifact, commit, test, or deployment cannot be found, stop and reconcile repository state. Do not fabricate continuity. If repository state is newer than this bootstrap, follow the newer governed handoff and update this bootstrap after the work is validated.
