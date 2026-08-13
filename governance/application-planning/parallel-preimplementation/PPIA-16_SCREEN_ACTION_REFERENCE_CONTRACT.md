# PPIA-16 — Screen States / Action Contracts / Reference Cases

Status: **candidate substep package; not PPIA-16 completion**

This package converts the verified PPIA-16 Foundation information architecture into deterministic interaction contracts. It does not implement a Developer Console and does not create application, repository, release, deployment, tester, credential, paid-service, owner-gate, or canonical-content authority.

## Locked source boundary

The package inherits the verified Foundation merge `015f200595fd6e8ba5da85a2956ee1c9dc8fb15b` and preserves:

- five-layer authority precedence: canonical repository authority → active-attempt repository state → derived repository projection → tool observation/evidence → generated development aid;
- raw tool/lifecycle semantics, including PASS/WARN/FAIL/BLOCK, PREPARED/READY_TO_EXECUTE, UNDECLARED/DECLARED/PROVEN, and `completed_verified` as the only complete work state;
- exact-candidate evidence binding and explicit stale/historical relationships;
- non-authoritative DT-001 through DT-010 boundaries;
- interruption recovery from repository evidence rather than conversation inference;
- all eight Foundation action classes, ten semantic screens, twelve workflows and eight cross-screen components;
- no activation of STAGE-A-A2 or any other application-runtime work.

## Screen-state model

`PPIA-16_SCREEN_STATE_CONTRACTS_v0.1.0.json` defines eight shared states: `loading`, `ready`, `empty`, `stale`, `conflict`, `blocked`, `error`, and `recovering`. Each of P16-SCR-001 through P16-SCR-010 has deterministic state oracles plus screen-specific variants such as `scope-gap`, `scenario-pass`, `privacy-block`, `tool-test-only`, `undeclared/declared/proven`, `partial-green`, `budget-missing`, and `continuity-conflict`.

State transitions are evidence-driven. Time passing, animation, navigation, a generated package, an open PR, or a partial green CI set cannot upgrade state. Stale evidence becomes current only after the controlling source/candidate is re-read and rebound. Conflict cannot disappear by silently dropping one source. Ambiguous mutation status enters recovery and forbids blind retry.

## Governed action model

`PPIA-16_ACTION_CONTRACTS_v0.1.0.json` defines enablement, disablement, confirmation, result, receipt and retry behavior for all eight Foundation action classes:

1. ACT-OBSERVE — idempotent source/tool observation.
2. ACT-NAVIGATE — exact-source/evidence navigation.
3. ACT-GENERATE — generated aid/evidence output with explicit destination/overwrite semantics.
4. ACT-RUN-EVIDENCE — deterministic validation/evidence execution bound to declared inputs.
5. ACT-EXTERNAL-ADAPTER — explicit separately governed adapter invocation; mutation authority is never inferred.
6. ACT-PROPOSE-GOVERNED-MUTATION — bounded proposal/task preparation only.
7. ACT-EXECUTE-GOVERNED-MUTATION — enabled only by external governing authority for the exact mutation/scope/candidate.
8. ACT-OWNER-GATED — never auto-executed; requires an explicit owner decision in the owning gate.

Confirmation never creates authority. It only confirms deliberate use of authority that already exists elsewhere.

## Component interaction model

`PPIA-16_COMPONENT_INTERACTION_CONTRACTS_v0.1.0.json` locks behavior for P16-CMP-001 through P16-CMP-008:

- Authority Badge preserves the exact authority class.
- Candidate Identity Chip preserves repository/ref/full SHA and current/stale/historical relationship.
- Raw Status Pill never semantically flattens tool or lifecycle states.
- Source Stack orders sources by authority precedence and exposes conflicts.
- Finding Row preserves source, raw state, scope, candidate/input identity, blocker effect and next action while preventing protected-data leakage.
- Evidence Receipt Card preserves producer-defined candidate, run/digest, mutation flag and limitations.
- Stop Condition Panel keeps active stop conditions adjacent to governed actions.
- Nonactivation Strip makes absent PPIA-16 authority explicit and requires an external governing source for any future true authorization.

## Accessibility, responsive and interaction parity

Core authority, candidate, status, blocker and next-action semantics are available without color, hover, drag, spatial layout or screenshots. Keyboard order follows source → state → action. Screen-reader announcements are concise state/blocker/action changes rather than auto-streamed logs. At 200%+ zoom, safety and action-critical content reflows before secondary metadata. Mobile/touch layouts may convert tables to labeled cards but may not hide authority, stop conditions, raw status, candidate identity or blocker effect.

## Reference-case corpus

`PPIA-16_SCREEN_ACTION_REFERENCE_CASES_v0.1.0.json` contains **48 synthetic noncanonical QA reference cases**: exactly four cases for each P16-WF-001 through P16-WF-012. Each workflow has:

- a normal/ready path;
- a stale, conflict, blocker or recovery path;
- a keyboard/nonvisual path;
- a mobile/touch/high-zoom path.

The corpus covers all ten screens, all eight action classes and all eight cross-screen components. It includes explicit cases for stale candidate evidence, scope gaps, PREPARED vs READY_TO_EXECUTE, fixture provenance conflict, missing owning-domain adapters, privacy/design blockers, tool-test-only UI evidence, UNDECLARED/DECLARED/PROVEN traceability, missing performance budget authority, partial exact-head CI, historical-vs-current findings, owner-only gates, and continuity conflict.

All cases are `synthetic_noncanonical_qa_reference_fixture`, `canonical:false`. They test the console contract only. They are not application fixtures, product-capacity promises, production evidence, canonical game content, or authorization to mutate any owning domain.

## Substep acceptance boundary

This package may advance only when one exact PR head passes the deterministic substep validator and every applicable hosted workflow, then merges with verified GitHub signature and receives the standard three-file recovery checkpoint. Passing this package advances PPIA-16 to **Integrated Screen / Workflow Traceability** (exact repository wording must be taken from the recovered checkpoint/program state); it does not mark PPIA-16 `completed_verified`.
