# APW-05 Review Receipt

**Work item:** APW-05 — Creator Workshop, Reusable Assets and Sandbox/Lab  
**Attempt:** APW-05-attempt-001  
**Design branch:** `governance/apw-05-creator-workshop-sandbox`  
**Review state:** substantive design complete; repository/PR validation pending

## Reviewed dependencies

- APW-01 universal account/context/authority model.
- APW-04 Personal Workspace/no-Campaign Home and context-switch isolation.
- CSW-08 independent derivative/provenance/source-change model as an integration input.
- Owner-approved APW program boundaries for creator ownership, Campaign variants, owning domains and noncanonical experimentation.

## Findings

1. Creator Workshop is a Personal-context orchestration surface, not a new context or global Creator role.
2. Owning domains keep identity, validation, mechanics, dependency, instance and publication authority.
3. Draft, reusable definition, template, Campaign variant, live instance, published/canonical and Sandbox experiment are explicit separate lifecycle classes.
4. Campaign authority cannot edit another user's Personal reusable library; Personal ownership cannot force Campaign incorporation.
5. Link, copy/clone, instantiate, import, propose and adopt/incorporate have distinct authority semantics.
6. Personal source and Campaign variants/instances evolve independently with provenance and no silent propagation.
7. Sandbox sessions are Personal-owned noncanonical experiments, not Campaign/Session/Adventure runs or alternate save universes.
8. Sandbox cannot mutate live state, award progression/resources or produce live Event-equivalent evidence.
9. Keeping Sandbox work uses explicit discard/archive/save-draft/save-template/clone/proposal/export operations with new identities/provenance.
10. Mechanical comparisons reuse owning-domain deterministic calculations and exact rule/schema/dependency versions.
11. Validation/origin presentation distinguishes draft, scoped-valid, invalid, stale, missing dependency, imported, Sandbox, reusable and separately published states.
12. Missing dependencies never trigger silent rewrite or automatic purchase/install.
13. Source archive/delete preserves independent derivatives/variants and follows reference-integrity/tombstone rules without protected Campaign leakage.
14. CSW-08 derivative/source-change evidence remains visible without introducing synchronization.
15. Promotion/publication is only a separately governed handoff; APW-05 cannot self-publish or self-promote.
16. Optional AI remains candidate-only and nonauthoritative; deterministic/non-AI creation/comparison support remains useful.
17. Offline/recovery/idempotency/conflict behavior is explicit and cannot broaden authority.
18. Search/count/recent/usage projections filter authorization before aggregation.
19. Keyboard, screen-reader, mobile and nonvisual paths cover all primary Workshop/Sandbox actions.

## Gate review

- Personal-context Workshop authority: **PASS**
- Reusable lifecycle separation: **PASS**
- Campaign source/variant isolation: **PASS**
- Transfer verb semantics: **PASS**
- Sandbox noncanonical isolation: **PASS**
- Explicit save-from-Sandbox: **PASS**
- Owning-domain deterministic comparison: **PASS**
- Validation/dependency/origin presentation: **PASS**
- Archive/delete/reference integrity: **PASS**
- CSW-08 integration: **PASS**
- Publication/promotion boundary: **PASS**
- Optional-AI/no-AI behavior: **PASS**
- Recovery/privacy/accessibility/mobile parity: **PASS**
- Live Campaign mutation from Sandbox: **NO**
- Application implementation/migration authorized: **NO**
- CCTI-12-T04 resumed: **NO**

Repository-health/PR merge evidence remains required before `completed_verified` is claimed.