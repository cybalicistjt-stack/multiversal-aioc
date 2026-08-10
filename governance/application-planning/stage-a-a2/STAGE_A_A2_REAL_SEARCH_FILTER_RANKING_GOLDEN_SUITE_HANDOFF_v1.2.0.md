# STAGE-A-A2 Real Search / Filter / Ranking Golden Suite Handoff v1.2.0

**Work item:** STAGE-A-A2 — Universal Object Experience  
**Status:** pre-implementation search/filter/ranking acceptance suite complete; A2 implementation not started by this handoff  
**AIOC branch:** `governance/stage-a-a2-detailed-design`  
**Application repository:** `cybalicistjt-stack/Multiversal-app`  
**Owner/final authority:** John Brandon Turner

## Owner-visible package

`STAGE_A_A2_REAL_SEARCH_FILTER_RANKING_GOLDEN_SUITE_v1.2.0.zip`

SHA-256:

`635e512213fea04d49ccb0a318f6ed8e9d7d04bb9a9a653b54b72dae8d677813`

This package is an implementation addendum to the A2 pre-implementation bundle and the v1.1 projection/profile mapping. It turns the approved v0.2 deterministic ranking contract into machine-readable real-data acceptance cases over the complete current Batch 8E governed release index.

## Verified coverage

- governed release search documents: **11,861**;
- query/filter/ranking cases: **28**;
- suggestion leakage cases: **3**;
- deep-link/URL-state cases: **4**;
- v0.6 object-query request schema conformance: **PASS** for all 28 requests;
- v0.5 URL-state schema conformance: **PASS** for all 4 deep-link states;
- deterministic suite validator: **PASS**;
- outer ZIP CRC/integrity: **PASS**.

## Locked ranking behavior

The suite instantiates the approved ranking order:

1. exact stable ID;
2. exact canonical name;
3. exact permitted alias;
4. canonical-name prefix;
5. canonical-name token;
6. alias prefix/token;
7. profile-declared structured field;
8. tag/pack/source-title/type;
9. short description;
10. lower-priority detail field.

The current golden browse corpus uses neutral profile relevance within a tier because no authoritative profile-weight table is available. Same-tier ties therefore resolve by canonical display name then stable ID. The suite does not invent a profile-weighting policy.

## Real-data stress cases

- exact stable-ID lookup for governed Dagger;
- duplicate exact names preserved as distinct identities: `Absolute Authority`, `Titan's Grip`, and cross-domain `Plasma Cutter`;
- explicit ingestion aliases `Elf → Elves` and `Dwarf → Dwarves`;
- `Any Race` remains explicitly **not** a Species alias;
- Plasma prefix/token ranking across multiple domains;
- object-kind and presentation-profile filtering;
- real Environment package filtering using `MV-CONTENT-V2-BATCH8B-ENVIRONMENT-PROFILE-PROMOTION-001`, yielding 40 governed Environment definitions;
- real source-title search for `ENVIRONMENT_DEFINITIONS_v1.0.0.csv`;
- source-backed corrected `Titan's Grip` tier 1 structured filtering while the separate tier 5 `Titan's Grip` identity remains distinct;
- zero-result behavior;
- Mythragara profile filtering;
- WarDog Recruit remains searchable while unresolved raw `Any Race` does not become a searchable Species object.

## Authorization and leakage cases

Authorization overlays are deterministic test policies applied to real governed IDs. They are not claims about canonical content visibility.

The suite requires:

- denied objects removed before matching/ranking;
- hidden duplicates excluded from `authorizedResultCount` and all facets;
- hidden names absent from suggestions;
- exact forbidden stable IDs returning the same safe `not_found_or_forbidden` family as nonexistent IDs;
- URL/deep-link state never granting access.

## Source-only collision finding

The first validator run correctly rejected an invalid expected result for the real source-only Vehicle `Civilian Car` (`VEH-0001`). The governed release also contains `Civilian Carbine` (`DEF-WPN-F3BB08FEEEC9`), which legitimately matches the text `Civilian Car` by the approved canonical-name prefix tier.

The corrected golden case therefore requires ordinary governed search to return only `Civilian Carbine` while exact `VEH-0001` remains `not_found_or_forbidden` / noncanonical. This preserves both ranking correctness and the source-only authority boundary instead of forcing a false zero-result expectation.

## Codex integration

Transfer this suite during A2-01 and run it starting in A2-02/A2-03 through the same deterministic local query path used by the UI. Production search logic must not contain fixture-specific name or stable-ID exceptions. The expected-results oracle changes only when governed authority changes—not merely to make implementation tests pass.

## Preservation boundary

This handoff does **not** change `CURRENT_WORK_POINTER.json`, does not activate A2 application implementation, does not alter the Design Standards primary attempt, does not promote source-only IDs, and does not authorize internal-alpha release, production release or deployment.

## Exact next pre-Sunday A2 operation

Build the real Picker acceptance corpus using governed Scene Add Object caller constraints: single/bounded multi-select, family/profile constraints, source-only rejection, stale/version failure, provisional tray persistence, final authorization/entitlement/pack-lock/compatibility revalidation, atomic receipt behavior, duplicate prevention policy, and expected stable-ID/version receipts suitable for A2-07/A2-08 day-one tests.
