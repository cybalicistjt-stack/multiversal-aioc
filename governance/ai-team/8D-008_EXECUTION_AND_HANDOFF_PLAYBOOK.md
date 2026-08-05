# 8D-008 AI Development Team Execution and Handoff Playbook

## Operating rule

The repository is canonical. Agents execute rather than narrate. A work item continues through implementation, validation, repair, pull request, CI, merge, and handoff unless a mandatory owner gate or an unresolvable external blocker is reached.

## Start-of-session bootstrap

1. Read `governance/ai/MULTIVERSAL_NEW_CONVERSATION_BOOTSTRAP.md` and every file it requires.
2. Verify repository identity, default branch, current `main` SHA, open pull requests, required checks, and the latest merged work.
3. Read canonical current-state, roadmap, and handoff documents.
4. Identify the next verified unfinished work item. Do not recreate completed work.
5. Record the evidence used to select that item.

## Execution loop

1. Create a bounded branch from current `main`.
2. Map each requested outcome to repository evidence and acceptance checks.
3. Implement the smallest complete tranche that can be independently validated.
4. Run local or repository-provided tests and validators.
5. Use a verification role that did not author the implementation to inspect requirements, changed files, failure modes, provenance, and regression risk.
6. Open a pull request with scope, evidence, risks, reversibility, and exact validation commands.
7. Inspect every required CI result. When CI fails, inspect logs, repair the root cause, rerun, and continue automatically.
8. Merge only after required checks pass and no mandatory gate remains.
9. Update canonical handoff and roadmap state in the same tranche or immediately following governance tranche.
10. Continue to the next verified unfinished item.

## Decision boundaries

Agents may decide and execute reversible, non-scope-changing implementation details, including reasonable defaults, deterministic identifiers, mappings, validation repairs, test additions, and documentation corrections.

Owner approval is mandatory before material product-scope changes, irreversible deletion, reduced security or privacy, legal or licensing acceptance, new material recurring costs, or a choice between irreconcilable canonical requirements.

## Truthfulness and evidence

An operation is complete only when repository evidence proves it. A claimed commit must exist. A claimed pull request must exist. A claimed CI result must be fetched. A claimed merge must return a merge result. Generated artifacts must have traceable identifiers or digests. Failed or skipped operations must never be described as completed.

## Independent verification checklist

- Requirement-to-change coverage is complete.
- Changed files are within scope.
- Canonical source truth and provenance are preserved.
- Tests exercise success, failure, rollback, and residue where applicable.
- No unsupported mechanics, identities, relationships, or values became canonical.
- CI evidence is fresh for the exact head SHA.
- Completion and next-step statements match repository state.

## Handoff format

A handoff must state: repository; merged PR and commit; active branch if unmerged; active workstream; completed validations; artifacts and digests; unresolved blockers; owner decisions required; and the next verified work item.

## Incident response

For accidental writes to `main`, stop further writes, identify the exact commit and affected paths, preserve evidence, repair through a governed branch and pull request, rerun all impacted validation, and document the incident without minimizing it. For permission failures, report the exact operation and permission boundary. For data-loss risk, do not proceed without the owner gate.
