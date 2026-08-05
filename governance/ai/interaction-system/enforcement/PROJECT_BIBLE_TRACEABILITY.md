# Project Bible and Governance Traceability

**Work item:** MV-CONT-003  
**Version:** 0.1.0  
**Purpose:** Connect every interaction pattern and evaluation case to controlling authority and enforceable controls.

## Controlling Project Bible clauses

- **6.2 Operating principles:** execute approved work, recover repository context, repair failures, never claim unverified work, preserve source truth.
- **6.4 Mandatory boundaries:** preserve owner-only spending, credentials, deployment, publication, release, and irreversible decisions.
- **6.5 Work continuity:** record authority, verified work, branch or PR, checks, failures, owner decisions, and exact next action.
- **36.23–36.28 Schemas and Validation:** validators must be deterministic, CI-enforced, fixture-tested, independently checked where warranted, and truthful about local, CI, PR, and merge states.
- **63.32–63.37 Testing and CI:** repair failures, preserve multiple coverage forms, provide PR evidence, and verify target-branch merge truth.
- **67.46–67.52 Context Loading:** block on missing required authority, refresh dynamic evidence, treat conversation summaries as non-authoritative, and minimize private context.
- **71.1–71.20 Checkpoints, Handoffs, and Recovery:** reconstruct exact state from durable records, preserve work-state snapshots and open work, and close with evidence and follow-up.

## Governance authorities

- `governance/ai/MULTIVERSAL_NEW_CONVERSATION_BOOTSTRAP.md`
- `governance/ai/interaction-system/OWNER_AI_INTERACTION_CONTRACT.md`
- `governance/access/AIOC_CONTRIBUTOR_REGISTRY.json`
- `governance/ai/interaction-system/analysis/FAILURE_FRICTION_TAXONOMY.json`
- `governance/ai/interaction-system/analysis/SUCCESS_PATTERN_CATALOG.json`
- `governance/ai/interaction-system/evaluation/EVALUATION_CASES.json`

## Coverage result

The matrix covers all 22 registered interaction patterns and all 15 evaluation cases.

Before MV-CONT-003:
- 13 patterns were enforced or enforced by existing domain systems;
- 2 were partially enforced;
- 7 required new interaction-level controls.

MV-CONT-003 adds typed receipts for:
- deliverable handoff;
- authority and capability state;
- source coverage;
- current UI verification;
- notification deduplication;
- request alignment;
- concise owner reporting.

One lower-priority gap remains intentionally deferred: automatic conversion of every owner correction into a new regression record. The current audit and evaluation workflow supports the conversion, but intake is not yet automatic.

## Enforcement rule

Policy text alone is not counted as enforced. A control is `enforced` only when it has a deterministic representation, validation command, negative fixture or test, and CI path capable of failing.
