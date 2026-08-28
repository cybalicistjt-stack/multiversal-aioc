# Multiversal AIOC Agent Operating Contract

This repository is the governed source for the Multiversal AIOC development platform.

## Mandatory startup

1. Read `governance/current-state/AIOC_CURRENT_STATE.md`.
2. Read `bridge/skills/multiversal-aioc/SKILL.md`.
3. Call the `multiversal_aioc` MCP server before making claims about the live deployment.
4. Use `verify_aioc_live_deployment` after any change intended to affect GitHub Pages.
5. Treat canonical content, shared working state, and browser-local state as different layers.

## Source-of-truth order

1. Certified repository content and governance records.
2. Shared AIOC working state exposed by MCP.
3. Browser-local drafts only when explicitly imported or supplied.
4. Conversation memory is never authoritative project state.

## Tool-use rules

- Use `inspect_aioc_live_deployment` for current live build and route evidence.
- Use `verify_aioc_live_deployment` for explicit PASS/FAIL deployment verification.
- Use canonical content tools for released source records.
- Use shared-state tools for drafts, classifications, pack work, evidence, and review queues.
- Reload the shared-state revision before any write.
- Do not modify canonical content directly through a working-state tool.
- Mutating tools require explicit owner approval and must preserve provenance.

## Deployment rule

A successful GitHub Actions or Railway status is not sufficient evidence that the user-visible site is correct. A deployment-affecting task is complete only after live verification confirms the expected commit, required routes, required assets, and content count.

## Security state

The production MCP bridge is currently read-only. Do not claim that repository or shared-state writes are available unless the bridge reports `writesEnabled: true`.

## Execution termination contract

An implementation command remains active through its governed completion boundary. A commit, open PR, queued/running check, partial green result, merge awaiting canonical closeout, or one completed tool batch is not a stopping condition.

Before emitting a final response from an execution turn:

1. Build an ephemeral state object conforming to `governance/ai/interaction-system/EXECUTION_TERMINATION_STATE.schema.json` from current tool/repository evidence.
2. Run `python scripts/execution_termination_preflight.py --state <temporary-state.json>`.
3. Continue using tools when the decision is `CONTINUE_EXECUTION`.
4. Finalize only when the decision is `ALLOW_FINAL_RESPONSE`, then report evidence matching that reason.

The ephemeral preflight file is execution evidence, not a checkpoint or repository artifact. Do not commit it. A missing or failed preflight is nonterminal while safe authorized work remains.

## Recovery evidence lease

Run the repository-first recovery sequence once per execution cycle. Treat the resolved pointer/checkpoint, relevant exact heads and current gate as fresh until a concrete invalidation occurs: an authority/head/branch change, merge or rebase, conflicting writer, materially new check result, or explicit stale/contradictory tool evidence. Refresh only affected facts. A tool batch ending, elapsed time, context compaction, a status request, or discovering another historical file does not justify restarting recovery.
