# Governed Orchestration and Routing

Release F Step 17 defines deterministic, coordinator-mediated routing over validated Specialist Agent Contracts.

## Contract

The routing layer must:

- classify bounded task types;
- identify eligible specialists from governed scope only;
- select the narrowest unambiguous specialist deterministically;
- preserve required inputs, permitted outputs, evidence, freshness, uncertainty, and authority;
- validate coordinator-to-specialist handoffs;
- escalate ambiguous, unsupported, stale, or authority-conflicted routes;
- emit auditable route records and diagnostics.

## Diagnostics

The generated artifact exposes ambiguous routes, missing inputs, unavailable capabilities, authority mismatches, invalid handoffs, and circular routing. These findings remain visible and are never silently reconciled.

## Authority boundary

Routing is advisory and proposal-only. It does not execute work, mutate canonical content, expand specialist authority, grant approval, promote or certify content, assign work, or schedule actions. The Development Coordinator mediates every route, and every handoff must preserve source authority.
