# Multiversal New Conversation Bootstrap
## Mandatory Repository-First Session Recovery Protocol

**Document ID:** MV-AI-BOOTSTRAP-001  
**Version:** 2.0.0  
**Status:** ACTIVE  
**Owner and final authority:** John Brandon Turner  
**Repository:** `cybalicistjt-stack/multiversal-aioc`  
**Last updated:** 2026-08-03

## How to use

Provide this file as the first project instruction in a new ChatGPT or Codex conversation. The assistant must execute the recovery protocol before doing project work. Do not restart, redesign, or summarize the project from memory.

## Project identity

Multiversal consists of two distinct canonical repositories:

- `cybalicistjt-stack/Multiversal-app` — the user-facing Multiversal application.
- `cybalicistjt-stack/multiversal-aioc` — the AIOC development operating system, governance, content tooling, AI coordination, repository intelligence, deployment verification, and Development Brain.

The active work described in this bootstrap belongs to `cybalicistjt-stack/multiversal-aioc`.

## Non-negotiable operating rules

1. Repository state is authoritative; conversation memory is supporting context only.
2. Before every governed operation, read `governance/ci-failures/INDEX.md` from branch `ci/failure-records` and repair any unresolved failure first.
3. Verify tool success before claiming a commit, deployment, test, file, or live-site result.
4. “Continue” means execute the next verified unfinished work item, not produce another plan.
5. Prefer one large, safe, coherent implementation batch over repeated small prompts.
6. Never mix canonical content, shared drafts, proposals, and promoted releases.
7. Significant AIOC updates must be verified against the live deployment, not CI alone.
8. Do not revive the obsolete `/v2/` migration shell or corrupted seed path.
9. Do not treat the old TallBunyon repository as active.
10. John Brandon Turner retains final approval authority.

## Mandatory initialization sequence

Execute these steps in order:

1. Discover the actual available tools and confirm GitHub read/write access.
2. Read the failure index on `ci/failure-records`.
3. Read these files from `main`:
   - `governance/current-state/AIOC_CURRENT_STATE.md`
   - `governance/current-state/SESSION_HANDOFF.md`
   - `governance/current-state/AIOC_OPERATIONAL_HANDOFF.md`
   - `governance/current-state/AIOC_DEPLOYMENT_BASELINE.md`
   - `governance/development-brain/DEVELOPMENT_BRAIN_ROADMAP.md`
   - `governance/development-brain/UNIFIED_INVENTORY_CONTRACT.md`
   - `governance/project-memory/PROJECT_MEMORY.json`
4. Inspect recent commits on `main` and verify the latest Development Brain files exist.
5. Confirm the active repository is `cybalicistjt-stack/multiversal-aioc`.
6. Resume from the exact next action in `SESSION_HANDOFF.md` unless the user explicitly changes direction.

## Current verified state at handoff

### Operational AIOC

- AIOC architecture and implementation milestones AIOC-0-001 through AIOC-I-007 are complete.
- The public operational surface is `/operational/`.
- The certified content database contains 487 canonical records.
- Preserved COS capabilities are published through the operational command center.
- Content Library, Content Structure Pipeline, Content Completion Assistant, and Design Studio are connected as a governed workflow.
- Browser-local durability exists through rolling backups and export/import, but full browser-to-shared-state synchronization remains technical debt.

### Hosted bridge

- Railway project: `Multiversal AIOC Bridge`.
- Service: `aioc-mcp-bridge`.
- Production MCP endpoint: `https://aioc-mcp-bridge-production.up.railway.app/mcp`.
- Health endpoint: `https://aioc-mcp-bridge-production.up.railway.app/health`.
- Verification endpoint: `https://aioc-mcp-bridge-production.up.railway.app/live-verification`.
- Hosted mode is read-only until explicit credentialed write activation.
- Codex configuration exists at `.codex/config.toml`.
- Repository agent rules exist at `AGENTS.md`.
- AIOC operating skill exists at `bridge/skills/multiversal-aioc/SKILL.md`.

### Development Brain roadmap

The Development Brain has 9 major steps delivered in three releases:

- Release A — Foundation: project memory, unified inventory, dependency graph.
- Release B — Content Intelligence: structure, readiness, priority/impact.
- Release C — Active Coordinator: recommendations, governance/verification, browser/MCP/Codex integration.

Completed:

#### Release A, Step 1 — Canonical Project Memory

- Schema commit: `5ccdb34051c8d72c783975ffa84a43251c8e7c52`
- Seeded memory commit: `b3103dfbda0a35cde6140934339f52337ab308ff`
- Validator commit: `97f6cc2b9f53343357d820a71fcfe1e8e2f0f84e`
- CI commit: `4ab60e7d53446350dc149293be4390592e787287`
- Roadmap/contract commit: `586df5f87a7271288eeb28af25be6498b5b04842`

Canonical files:

- `governance/project-memory/PROJECT_MEMORY.schema.json`
- `governance/project-memory/PROJECT_MEMORY.json`
- `scripts/validate-project-memory.mjs`
- `.github/workflows/validate-project-memory.yml`
- `governance/development-brain/DEVELOPMENT_BRAIN_ROADMAP.md`

#### Release A, Step 2 — Unified Object Inventory

- Schema commit: `8cf4d3220309f1058cf145f94c6d2b09e00e181c`
- Generator commit: `b66cee8a31c21c262a16ef5cbd9a53ae7af2ec4d`
- Validator commit: `61122a0144c4461a0430c826c1e302a54a8c193b`
- CI/artifact commit: `710c1c03aa99d943beca870e757b390b83eacaa4`
- Contract commit: `eeec41441369238c147565ef454cb61e5ed8c45b`

Canonical files:

- `governance/development-brain/UNIFIED_INVENTORY.schema.json`
- `scripts/generate-unified-inventory.mjs`
- `scripts/validate-unified-inventory.mjs`
- `.github/workflows/validate-unified-inventory.yml`
- `governance/development-brain/UNIFIED_INVENTORY_CONTRACT.md`

The inventory is derived, not hand-maintained. It normalizes canonical records, shared drafts, structure decisions, packs, evidence, review state, dependencies, and memory references while preserving authority boundaries.

## Exact next executable work item

**Development Brain Release A, Step 3 — Dependency Graph.**

Implement this as one bounded batch:

1. Define the graph schema and relationship vocabulary.
2. Generate graph nodes from the unified inventory.
3. Generate explicit edges for at least:
   - `requires`
   - `grants`
   - `contains`
   - `parent-of`
   - `variant-of`
   - `validates`
   - `affects`
   - `supersedes`
   - `blocks`
   - `member-of-pack`
4. Preserve source evidence and confidence for every derived edge.
5. Detect dangling targets, duplicate edges, self-dependencies, and cycles where cycles are not permitted.
6. Produce a deterministic generated graph artifact and summary metrics.
7. Add validation CI.
8. Update the Development Brain contract and current-state handoff.

Do not begin Release B until Step 3 is generated and validated.

## Separate external task

`WP-011 — Tauri iOS/iPadOS Spike` remains the next Mac-dependent Multiversal App task. It is separate from the active AIOC Development Brain work and must not replace Step 3 unless the owner explicitly switches workstreams.

## Required first response in a new conversation

After executing initialization, respond compactly:

```text
Multiversal session restored.

GitHub read: PASS/FAIL
GitHub write: PASS/FAIL
Active repository: cybalicistjt-stack/multiversal-aioc
Branch: main
Current milestone: Development Brain Release A
Last verified completion: Step 2 — Unified Object Inventory
Next executable work item: Step 3 — Dependency Graph
Blocking issues: <none or exact blocker>
```

If the opening message says “Continue,” begin Step 3 in the same response after the readiness report.

## Honesty and recovery

If any named file or commit cannot be found, stop and reconcile repository state. Do not fabricate continuity. If repository state is newer than this file, follow the newer governed handoff and update this bootstrap after completing the work.
