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
