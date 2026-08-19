# APM-04 Review Receipt

**Work item:** APM-04 — AutoGM Mini-Campaign Director  
**Attempt:** APM-04-attempt-001  
**Design branch:** `governance/apm-04-mini-campaign-director`  
**Review state:** substantive design complete; repository/PR validation pending

## Reviewed dependencies

- APM-03 bounded single-encounter package/run, mechanical replay, hidden-information and recovery contract.
- CSW-05 nonlinear Adventure planning and governed incorporation boundary.
- CSW-06 evidence-backed continuity/open-thread tracker and advisory-only correction boundary.
- APM-01 automation delegation and optional-AI responsibility partition.

## Findings

1. Mini-campaign execution is finite and exact-versioned; packages declare scene/child-run/step/Event bounds and explicit endpoints/fail-safe behavior.
2. CSW planning is not executable; the package consumes governed Adventure/source versions after explicit incorporation/review.
3. Route eligibility is computed only from committed authoritative/package state and exact prerequisite rules.
4. Meaningfully distinct player-facing routes are human choices unless explicitly modeled as automatic non-choice transitions.
5. The director cannot invent edges, reveal hidden routes early or use AI suggestions as executable structure.
6. Encounter nodes compose APM-03 as child runs with durable parent-child correlation and exactly-once parent advancement.
7. Non-encounter automatic operations remain restricted to package-declared `automatic_permitted`/`automatic_with_bounds` owning-domain commands.
8. Authoritative Character/resource/world/investigation/relationship state carries between scenes through owning domains, not parent shadow state.
9. Hidden package state is filtered before player projection and again before optional-AI context; hidden-node cardinality is protected.
10. CSW-06 continuity candidates remain creator-side advisory evidence and cannot rewrite a running package.
11. Deterministic replay covers route eligibility/package-declared automatic transitions/mechanical Events for fixed state, choices, Actions, versions and seed streams; prose is excluded.
12. Hard bounds terminate in explicit success/failure/open/retreat/abandon/fail-safe states rather than endless generation.
13. Parent/child rewards are reconciled exactly once and irreversible advancement choices remain human-required.
14. Initial execution remains foreground-only; reconnect resolves ambiguous child status/parent transition before new work and pauses on incompatible version drift.
15. Optional AI is presentation-only; a complete deterministic/manual no-AI path remains available.
16. Player-facing route/navigation controls have keyboard, screen-reader and mobile parity without revealing secret progress totals.

## Gate review

- Finite package/run/graph bounds: **PASS**
- Governed Adventure source boundary: **PASS**
- Committed-state route eligibility: **PASS**
- Human meaningful-route choice: **PASS**
- APM-03 child-run exactly-once composition: **PASS**
- Cross-scene owning-domain state: **PASS**
- Hidden information/player/AI separation: **PASS**
- CSW-06 advisory-only integration: **PASS**
- Deterministic route/mechanical replay: **PASS**
- Explicit bounded endings: **PASS**
- Recovery/version-drift/idempotency: **PASS**
- Optional AI/no-AI path: **PASS**
- Unlimited autonomous campaign generation: **NO**
- AI GM/mechanical/canonical authority: **NO**
- Application implementation/migration authorized: **NO**
- CCTI-12-T04 resumed: **NO**

Repository-health/PR merge evidence remains required before `completed_verified` is claimed.