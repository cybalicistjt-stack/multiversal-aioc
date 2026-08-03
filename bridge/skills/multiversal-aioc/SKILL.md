---
name: multiversal-aioc
description: Operate the Multiversal AIOC through its governed MCP bridge. Use for AIOC status, canonical content research, shared drafts, structure decisions, proposals, reviews, live deployment verification, and development coordination.
---

# Multiversal AIOC Operating Skill

Use the `multiversal-aioc` MCP server as the authoritative programmatic interface to the AIOC.

## State boundaries

Treat these as separate layers:

1. **Canonical content** — certified repository records returned by `search_aioc_content` and `get_aioc_object`. Read-only through normal working tools.
2. **Shared working state** — editable drafts, structure decisions, packs, evidence, and review queue returned by `get_aioc_shared_state` and working-object tools.
3. **Live deployment** — the user-visible GitHub Pages artifact inspected through `inspect_aioc_live_deployment` and `verify_aioc_live_deployment`.
4. **Governed proposals** — reviewable repository proposals created by `create_aioc_change_proposal`.
5. **Canonical promotion** — not automatic. It requires owner approval, repository validation, certification, and promotion workflows.

Never describe a shared draft or exported review package as canonical or game ready merely because it is complete locally.

## Start every AIOC task

1. Call `aioc_status`.
2. Read the shared-state revision if the task involves drafts or decisions.
3. Search canonical content before creating a new object or recommending a merge.
4. Use stable IDs in all tool calls and explanations.
5. When the task concerns the website or a deployment, call `inspect_aioc_live_deployment` before making claims about what is live.

## Live verification workflow

For any change intended to affect the deployed AIOC:

1. Identify the repository commit containing the change.
2. Call `verify_aioc_live_deployment`, supplying the expected commit when available.
3. Require evidence for the root page, operational surface, health record, deployment manifest, content database, Content Library, Content Assistant, Content Structure Pipeline, and Design Studio.
4. Treat a CI success as supporting evidence only; it is not a substitute for live verification.
5. Report `PASS`, `FAIL`, or `DEGRADED` and name every failed route or commit mismatch.
6. Do not close the task as complete until the live deployment contains the expected change and required routes pass.

## Read workflow

- Use `search_aioc_content` to locate canonical source records.
- Use `get_aioc_object` for the full canonical record.
- Use `list_aioc_working_objects` to find active shared drafts.
- Use `get_aioc_working_object` before editing one draft.
- Use `get_aioc_current_state` for roadmap, constraints, and active work.
- Use `get_aioc_shared_state` for structure decisions, packs, evidence, review queue, or revision-sensitive operations.
- Use `inspect_aioc_live_deployment` for current deployed-build evidence.
- Use `verify_aioc_live_deployment` for a bounded live smoke test and repository comparison.

## Write workflow

Mutations require clear user approval.

Before calling `upsert_aioc_working_object` or `record_aioc_structure_decision`:

1. Read the current shared-state revision.
2. Explain the intended change in practical language.
3. Preserve stable ID and provenance.
4. Pass the exact current revision as `expectedRevision`.
5. If a revision conflict occurs, reload state and reconcile rather than overwriting.

Use `create_aioc_change_proposal` for changes intended to affect canonical content, including add, update, merge, retire, or link operations. Proposal creation is not canonical promotion.

## Content structure decisions

Classify source records before full development when their correct granularity is uncertain:

- `standalone`
- `reusable-generic`
- `parent-component`
- `granted-variant`
- `duplicate`
- `obsolete`

Prefer parent components or granted variants for labels that describe use of a specific parent object, such as “Attack with Rapier,” unless they contain genuinely unique reusable mechanics.

## Safety and governance

- Do not mutate certified `content-db` records directly.
- Do not silently retire, merge, or replace content.
- Do not expose repository credentials or bridge secrets.
- Keep write operations bounded and reviewable.
- Preserve source provenance and owner authority.
- John Brandon Turner is the final approval authority for Multiversal content and project direction.
- The production bridge is read-only unless `aioc_status` explicitly reports `writesEnabled: true`.

## Recovery

If the bridge is unavailable:

- Do not pretend a read, verification, or write succeeded.
- Record the intended operation in the conversation.
- Use repository access only when explicitly authorized and when the same governance boundary can be preserved.
- For deployment questions, state that live verification could not be completed rather than inferring success from source code or CI alone.
