# Operations V3 Single-Door Reset Implementation Plan

> **For agentic workers:** Use the host's available task-by-task implementation workflow. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Replace overlapping Multiversal governance/behavior entrypoints with one GPT-first operational door while preserving all project work and evidence.

**Architecture:** `operations/BOOTSTRAP.md` is the only entrypoint, `operations/OPERATING_CONTRACT.md` is the only global behavior contract, `operations/CURRENT.json` is the only mutable current-state selector, and `operations/LANES.json` routes user intent to bounded source bundles. Legacy surfaces are redirects, generated compatibility projections, validators, executor adapters, source references, or historical evidence; they may not independently select work.

**Tech Stack:** Markdown, JSON, Python 3, Git/GitHub Actions, existing Multiversal repositories and ChatGPT Project Sources.

## Global Constraints

- Preserve all completed product/code/content/source work and Git history.
- Do not start MIB-17 during the OPS3 cutover.
- Preserve MIB-17 as selected_not_started with no implementation authority.
- Every GPT conversation must enter through the same canonical door.
- Executor availability must be separated from work authority.
- No legacy file may independently redefine Continue semantics, current work, next action, timing, termination, or owner boundaries.
- Historical material is retired from authority, not deleted.
- Project custom instructions and Project Source attachments require a platform/UI cutover because the available Project Files tool cannot mutate those surfaces in place.

---

### Task 1: Install the canonical AIOC operations door

**Files:**
- Create: `operations/BOOTSTRAP.md`
- Create: `operations/OPERATING_CONTRACT.md`
- Create: `operations/CURRENT.json`
- Create: `operations/LANES.json`
- Create: `operations/CONTROL_SURFACE_REGISTRY.json`
- Create: `operations/work-items/OPS3-01.json`
- Create: `scripts/validate_operations_v3.py`
- Create: `tests/control_plane/test_operations_v3_single_door.py`

**Interfaces:**
- Consumes: current MIB-17 selection and live repository evidence.
- Produces: one canonical authority chain and machine-checkable single-door invariants.

- [x] Add focused failing test requiring the new door/state/contract/lane surfaces.
- [x] Observe the real PR workflow fail at the control-plane regression step while legacy health remains green.
- [ ] Implement the minimum OPS3 files and validator.
- [ ] Run the same focused test and canonical workflow green.

### Task 2: Neutralize AIOC duplicate instruction surfaces

**Files:**
- Modify: `AGENTS.md`
- Modify: `governance/ai/MULTIVERSAL_NEW_CONVERSATION_BOOTSTRAP.md`
- Modify: `governance/ai/MULTIVERSAL_STATIC_RESTART_PROMPT.txt`
- Modify: `governance/ai/runtime/CURRENT_WORK_POINTER.json`
- Modify: `governance/ai/runtime/ACTIVE_AUTHORITY_REGISTRY.json`
- Modify: `bridge/CHATGPT_CODEX_ACTIVATION.md`
- Modify: `.github/workflows/validate-repository-health.yml`

**Interfaces:**
- Consumes: OPS3 canonical paths.
- Produces: redirects/projections only; old AIOC control-plane validators become historical rather than active execution authority.

- [ ] Convert repository and restart entrypoints to the single door.
- [ ] Convert legacy selector/authority files to explicit compatibility projections.
- [ ] Replace the canonical health workflow with the OPS3 validator/test only.
- [ ] Verify exact-head PR validation.

### Task 3: Neutralize application-repository operational authority

**Files:**
- Modify: `AGENTS.md`
- Modify: `MULTIVERSAL_MASTER_CONTEXT.md`
- Modify: `project-authority/current-authority.md`
- Modify: `.ai/current-phase.md`, `.ai/current-work-order.md`, `.ai/next-task.md`, `.ai/task-queue.md`, `.ai/agent-handoff.md`, `.ai/owner-control-center.md`, `.ai/owner-decisions-needed.md`, `.ai/project-context.md`
- Modify: `.ai/autonomy-policy.md`, `.ai/autonomous-execution-runbook.md`, `.ai/stop-conditions.md`
- Modify: `tools/validation_core/validate_repository_health_app.py`
- Modify: `.github/workflows/validate-current-family.yml`

**Interfaces:**
- Consumes: canonical AIOC OPS3 door URL/path.
- Produces: an application repository that can provide implementation evidence but cannot select work or behavior.

- [ ] Establish RED by making application health require OPS3 redirects before rewriting old surfaces.
- [ ] Rewrite all live-looking selectors/policies to redirect/history roles.
- [ ] Validate the application repository no longer advertises STAGE-A-A2 or another current task.
- [ ] Preserve product validation profiles as validation-only data.

### Task 4: Cut over GPT Project entry surfaces and close the migration

**Files:**
- Create: `operations/adapters/GPT_PROJECT_INSTRUCTIONS.md`
- Create: `operations/adapters/PROJECT_SOURCE_CUTOVER.md`
- Replace Project Source copies of: `START_HERE.md`, `NEW_CHAT_PROMPT.txt`, `SOURCE_MAP.md`, `PROJECT_SOURCE_MANIFEST.md`

**Interfaces:**
- Consumes: OPS3 canonical repository door.
- Produces: one GPT-first entry path for future conversations.

- [ ] Generate replacement Project Source files and a source-kit bundle.
- [ ] Record the platform limitation: Project attachments/custom instructions cannot be mutated by the available API.
- [ ] Replace those surfaces through the ChatGPT Project UI or a future supported mutation API.
- [ ] Re-run the control-surface contradiction audit.
- [ ] Clear the product-start freeze only after the repository and GPT Project entry surfaces are aligned.

## Unresolved externally observable decisions

None for repository architecture. Full completion depends on one platform capability currently outside repository mutation: replacing the ChatGPT Project custom instructions and Project Source attachments in the Project UI.
