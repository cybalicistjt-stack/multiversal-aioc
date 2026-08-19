# CSW-01 Review Receipt

**Work item:** CSW-01 — Storycraft Vocabulary, Creative Object Model and Authority  
**Attempt:** CSW-01-attempt-001  
**Design branch:** `governance/csw-01-creative-object-authority`  
**Review state:** substantive design complete; repository/PR validation pending

## Reviewed source contracts

- CSW owner-approved program.
- APW-01 Authority, Account, Context and Terminology Canonicalization.
- APM-01 Automated-Play Authority and Mode Contract.
- Stage A10 current-repository revalidation and split D18/D28/D29/D05 authority.
- App D29 authoring draft, proposal/review/publication, authority, operation-status and recovery contracts.
- A10 creator-content and Campaign-local schemas/persistence.
- A9 investigation hypothesis/conclusion contract.

## Findings

1. A distinct pre-authoritative Creative Fragment concept is necessary for incomplete/speculative material that is not yet a valid D18/D28/D29/Character/Campaign/A9 object.
2. The normalized vocabulary remains descriptive and excludes authoritative domain object kinds.
3. `hypothesis` is not duplicated as a generic CSW kind because A9 already owns runtime hypotheses and explicitly marks them `objectiveTruth:false`.
4. Creative Fragment identity is stable/versioned and fixed to `authorityClass=pre-authoritative`.
5. Lifecycle is `inbox → scratch → developing → ready`, with incorporated/superseded/archived/tombstoned branches; `ready` and `incorporated` never mean authoritative.
6. Personal and Campaign-bound creative material are distinct; Campaign binding does not create Campaign truth and GM authority does not grant blanket Personal access.
7. Ownership, authorship, view, edit, link, branch/clone, share, Campaign binding, propose/incorporate, archive, tombstone, restore and export are independent capabilities.
8. Creative links such as supports/foreshadows/pays-off are not runtime evidence/state relationships by themselves.
9. Incorporation is an explicit pinned-version bridge into an owning domain. It never converts the source fragment in-place or authorizes later synchronization.
10. D18 remains World/Location authority, D28 remains Adventure/run authority, D29 remains governed authoring/proposal/publication provenance, A9 remains runtime investigation/social authority, and Character/Campaign/other domains retain their own state authority.
11. Canonical promotion has no direct CSW route and remains owner-only through existing governance.
12. Tombstones preserve reference/provenance integrity without leaking private object existence.
13. Optional AI and APM automation can suggest/use fragments only within existing permission/provenance boundaries and cannot promote them into truth.
14. CSW-01 does not choose or authorize a new persistence root; CSW-10 must decide whether a bounded D29 extension is sufficient before any new seam is considered.

## Gate review

- Normalized vocabulary explicit: **PASS**
- Authoritative object kinds not duplicated: **PASS**
- Stable pre-authoritative identity/version/provenance defined: **PASS**
- Lifecycle and tombstone/reference integrity defined: **PASS**
- Personal versus Campaign-bound context defined: **PASS**
- Authority dimensions separated: **PASS**
- Possibility/rumor/seed/link cannot masquerade as fact: **PASS**
- Incorporation is explicit/pinned/attributable: **PASS**
- A10 D18/D28/D29 split preserved: **PASS**
- A9 hypothesis/runtime boundary preserved: **PASS**
- Optional AI/automation nonauthoritative: **PASS**
- New application persistence authorized: **NO**
- Application implementation/migration authorized: **NO**
- Canonical promotion authorized: **NO**
- CCTI-12-T04 resumed: **NO**

Repository-health/PR merge evidence remains to be attached before `completed_verified` is claimed.
