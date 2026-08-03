# AIOC Current State

**Status:** Operational AIOC certified; Development Brain Release A active  
**Repository:** `cybalicistjt-stack/multiversal-aioc`  
**Default branch:** `main`  
**Owner:** John Brandon Turner

## Operational baseline

AIOC-0-001 through AIOC-0-012 and implementation milestones AIOC-I-001 through AIOC-I-007 are complete.

The seven-step repository and deployment cleanup is complete:

- Public default: `/operational/`
- Authoritative Pages workflow: `.github/workflows/deploy-pages.yml`
- Certified content mode: `CANONICAL_OBJECTS_ONLY`
- Certified content records: 487
- Recent COS capability work: preserved
- Obsolete migration entry behavior: narrowly quarantined
- Corrupted legacy seed execution path: quarantined
- Unified validation workflow: `.github/workflows/full-system-validation.yml`

Canonical deployment records:

- `governance/current-state/AIOC_OPERATIONAL_HANDOFF.md`
- `governance/current-state/AIOC_DEPLOYMENT_BASELINE.md`

## Operational capability workflow

The operational command center exposes preserved COS capabilities, including:

- Content Library
- Content Structure Pipeline
- Content Completion Assistant
- Design Studio
- Balance Lab
- Testing Suite
- Feature Modules
- Diagnostics
- Development OS
- Refresh and Recovery

The intended content lifecycle is:

`canonical source → structure decision → working object → completion → validation/review package → governed promotion → certified content`

Browser durability supports rolling snapshots and export/import. Browser-to-shared-state synchronization remains recorded technical debt.

## Hosted AIOC bridge

Railway hosts the read-only AIOC MCP bridge:

- MCP: `https://aioc-mcp-bridge-production.up.railway.app/mcp`
- Health: `https://aioc-mcp-bridge-production.up.railway.app/health`
- Verification: `https://aioc-mcp-bridge-production.up.railway.app/live-verification`

Repository integration:

- Codex MCP configuration: `.codex/config.toml`
- Agent operating contract: `AGENTS.md`
- Shared AIOC skill: `bridge/skills/multiversal-aioc/SKILL.md`

Hosted writes remain disabled until explicitly authorized and credentialed.

## Active milestone

**Development Brain — Release A: Foundation**

### Step 1 — Canonical Project Memory — IMPLEMENTED

Primary files:

- `governance/project-memory/PROJECT_MEMORY.schema.json`
- `governance/project-memory/PROJECT_MEMORY.json`
- `scripts/validate-project-memory.mjs`
- `.github/workflows/validate-project-memory.yml`
- `governance/development-brain/DEVELOPMENT_BRAIN_ROADMAP.md`

### Step 2 — Unified Object Inventory — IMPLEMENTED

Primary files:

- `governance/development-brain/UNIFIED_INVENTORY.schema.json`
- `scripts/generate-unified-inventory.mjs`
- `scripts/validate-unified-inventory.mjs`
- `.github/workflows/validate-unified-inventory.yml`
- `governance/development-brain/UNIFIED_INVENTORY_CONTRACT.md`

The inventory is derived rather than hand-maintained and preserves canonical-versus-working authority boundaries.

## Next executable action

**Development Brain Release A, Step 3 — Dependency Graph.**

Implement one deterministic derived graph covering explicit and evidence-backed relationships across the unified inventory. Required relationship vocabulary includes:

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

Required controls include stable node IDs, source evidence, confidence, dangling-target detection, duplicate-edge detection, forbidden self-edge detection, cycle validation, generated summary metrics, and CI validation.

Do not begin Development Brain Release B until Step 3 is generated and validated.

## Separate external work item

`WP-011 — Tauri iOS/iPadOS Spike` remains the next Mac-dependent task in `cybalicistjt-stack/Multiversal-app`. It is separate from the active AIOC Development Brain workstream.

## Mandatory failure evidence rule

Before every governed operation, read:

`governance/ci-failures/INDEX.md` on branch `ci/failure-records`.

Any unresolved recorded failure is repaired before new work begins.

## Mandatory continuity sequence

New conversations must read:

1. `governance/ai/MULTIVERSAL_NEW_CONVERSATION_BOOTSTRAP.md`
2. this file
3. `governance/current-state/SESSION_HANDOFF.md`
4. `governance/current-state/AIOC_OPERATIONAL_HANDOFF.md`
5. `governance/current-state/AIOC_DEPLOYMENT_BASELINE.md`
6. `governance/development-brain/DEVELOPMENT_BRAIN_ROADMAP.md`
7. `governance/development-brain/UNIFIED_INVENTORY_CONTRACT.md`
8. `governance/project-memory/PROJECT_MEMORY.json`

When the owner says “Continue,” resume Step 3 immediately after verifying tools, repository state, and the failure index.
