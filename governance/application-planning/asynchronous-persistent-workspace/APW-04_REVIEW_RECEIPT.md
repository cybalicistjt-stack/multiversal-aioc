# APW-04 Review Receipt

**Work item:** APW-04 — Personal Workspace and No-Campaign Home  
**Attempt:** APW-04-attempt-001  
**Design branch:** `governance/apw-04-personal-workspace-home`  
**Review state:** substantive design complete; repository/PR validation pending

## Reviewed source contracts

- APW-01 universal-user and Personal/Campaign/Session authority model.
- Current A3 recent-work and workspace-entry authorization contracts.
- Current A4 Campaign-bound Character draft/policy persistence contracts.
- CSW-01/02 Personal creative-fragment/Project/Story Bible/Project Memory contracts.
- APM-01 automated-play authority contract.

## Findings

1. Personal Home is the account-level home and remains useful with zero Campaign memberships; it is not a renamed Player/GM dashboard.
2. Personal Home is an orchestrating projection over owning domains, not a monolithic Personal truth store.
3. Resources are explicitly classified as Personal-owned, Personal-accessible references, or Campaign-private; access never silently transfers ownership.
4. Current Stage A Character drafts require `campaignId`; APW-04 preserves that completed contract and defines an additive future Personal/Campaign Character-context successor rather than rewriting history.
5. Personal Characters do not imply Campaign membership, Campaign grants or Campaign authority. Campaign use requires explicit bind/clone/adopt/proposal semantics with provenance and policy validation.
6. Campaign exit does not silently copy Campaign/runtime Character state into Personal ownership.
7. CSW Creative Library/Projects are native Personal capabilities while Campaign-bound creative material remains context/visibility bound.
8. Personal sandbox/practice is explicitly non-Campaign/noncanonical and cannot transfer rewards/state directly into Campaign authority.
9. Personal↔Campaign context switching is a fresh authorization boundary and partitions caches, realtime subscriptions, search, recent links, drafts, notifications and AI context.
10. Existing A3 recent-work rules already provide the correct revocation-aware foundation: every candidate is reauthorized and selection requires fresh entry authorization.
11. Invitations and notifications are account-safe attention/discovery projections, not membership or authority.
12. Losing/leaving the last Campaign preserves account and Personal capabilities while clearing protected Campaign state.
13. Personal import/export/backup cannot become a cache of Campaign-private truth.
14. APW-04 supplies a Personal host context to APM-02 Cozy Solo but grants no automation authority.
15. Core Personal Home remains useful without AI.

## Gate review

- Zero-Campaign Personal Home useful: **PASS**
- Personal/reference/Campaign-private resource classes separated: **PASS**
- Current A4 Character contract reconciled additively: **PASS**
- Explicit Personal→Campaign Character binding boundary: **PASS**
- CSW Personal integration defined: **PASS**
- Sandbox state isolation/noncanonical boundary: **PASS**
- Context switching reauthorization/cache partitioning: **PASS**
- Recent work/invitations/notifications safe: **PASS**
- Leave-last-Campaign behavior preserves Personal capability: **PASS**
- Import/export/recovery Campaign-private separation: **PASS**
- APM-02 Personal host without automation authority: **PASS**
- Application implementation/migration authorized: **NO**
- Global GM/Player role authorized: **NO**
- Canonical promotion authorized: **NO**
- CCTI-12-T04 resumed: **NO**

Repository-health/PR merge evidence remains to be attached before `completed_verified` is claimed.
