# Application Implementation Roadmap Supplement — CCTI

**Supplement ID:** MV-APP-ROADMAP-CCTI-001  
**Owner-approved:** 2026-08-17  
**Status:** ACTIVE PARALLEL CONTENT-INTEGRATION / PLATFORM CANDIDATE REVIEW  
**Governing program:** `CONTENT_CATALOG_TAXONOMY_INTEGRATION_PROGRAM.md`

This supplement adds an owner-selected parallel content mission without replacing the ordered Stage A roadmap or any retained Internal Alpha/Design Standards track.

## Current state

- GATX-T07-REMOTE and GATX-T08 remain `completed_verified`.
- App PR #185 remains unfinished at its declared final-confirmation boundary; CCTI does not merge, supersede, or distribution-approve it.
- CCTI read-only CCTI-01 through CCTI-08 is `completed_verified`.
- CCTI-WRITE-01 additive candidate work is active.
- The complete **10-axis universal Item taxonomy candidate pass** is finished across the 5,389-row Item/reference corpus; candidates remain disabled/noncanonical.
- The Item cross-axis review/consolidation is complete and produced 91 structural review rows plus 85 additive correction proposals. Item canonical adoption is **not ready** and remains separately gated.
- Exact row-level private evidence is currently present for IAX-01 through IAX-05, IAX-09 and IAX-10; IAX-06/IAX-07/IAX-08 retain canonical aggregate baselines and sealed hashes but their original row-level private bytes are not in the active evidence workspace. Recovery or an explicitly versioned superseding reprojection is required before Item enablement.
- The next active additive content operation is **Platform v0.11.0 candidate projection/review**.
- OGR-01 Object Game-Readiness schema/baseline remains active as downstream measurement/control work.
- Source/master CSV mutation, mechanics reauthoring, runtime enablement, CCTI-12 app-facing activation and release remain unauthorized.

## Corpus target

CCTI reconciles **11,017 records**:

- 5,389 Item/reference rows;
- 5,628 Vehicles/Mecha/Spacecraft-domain rows.

Of the 5,628 platform-domain rows, exactly **2,984 are platform/model rows** under existing `Record_Type` evidence and **2,644 are component/module/rules/support content** requiring correct cross-domain routing. Spacecraft remains a first-class platform corpus.

## Completed milestones

1. **CCTI-01** existing corpus + sidecar reconstruction — `completed_verified`.
2. **CCTI-02** exact Item/Platform/Reality source recovery — `completed_verified`; canonical SHA-256 identities matched.
3. **CCTI-03** shared integration/boundary model — `completed_verified`.
4. **CCTI-04** deterministic row/identity/evidence crosswalk envelope — `completed_verified`.
5. **CCTI-05 read-only audit** exact Item/current-corpus alignment — complete.
6. **CCTI-06 read-only audit** exact Platform/current-corpus alignment and model/non-model routing — complete.
7. **CCTI-07 read-only audit** relationship evidence/signal inventory — complete.
8. **CCTI-08 read-only audit** shared context/compatibility evidence boundary — complete.
9. **CCTI-05 / CCTI-09 Item universal taxonomy candidate pass** — all IAX-01 through IAX-10 complete at candidate-disposition level across 5,389 rows; disabled/noncanonical.
10. **CCTI-09 Item cross-axis review/consolidation** — complete for available exact row-level evidence; source/master hashes still match; 91 structural review rows, 85 additive correction proposals, and governed adoption proposal prepared. Canonical adoption is not ready.

## Active additive milestone — Platform v0.11.0 review

### CCTI-06 / CCTI-09 — Platform candidate projection/review

Use the exact prepared Platform Catalog v0.11.0 package/crosswalk as the candidate baseline across all **5,628** platform-domain rows.

Mandatory routing:
- preserve **2,984 platform/model** rows as model/archetype/platform candidates;
- preserve **2,644 non-model** rows as components, modules, rules, support equipment/supplies, services or other proper routed content;
- preserve existing stable identities, provenance, normalization and supersession decisions;
- keep proposed/review-required assignments explicit;
- keep shared Genre/Technology context deferred to the exact shared 241-value context registry rather than improvising new context values;
- preserve Platform Model vs individual runtime Asset boundaries.

### Item canonical-adoption dependency retained in parallel

Before Item taxonomy can be enabled:
1. keep all ten sealed historical Item tranches immutable;
2. apply the cross-axis corrections as a new adoption overlay;
3. recover original IAX-06/IAX-07/IAX-08 row-level evidence at the sealed hashes or produce explicitly versioned superseding reprojections;
4. rebuild one complete 5,389-row ten-axis adoption candidate ledger;
5. rerun deterministic validation and present unresolved/review cohorts to the owner;
6. obtain explicit owner approval for canonical enablement.

## Remaining CCTI pathway

### CCTI-07 / CCTI-10 — Cross-domain graph

Resolve candidate Item ↔ Vehicle/Mecha/Spacecraft relationships through stable identities and explicit evidence. Compatibility never implies an Asset Instance is currently installed, equipped or owned.

### CCTI-08 / CCTI-10 — Context/compatibility candidate adoption

Use the exact 241-value shared context registry while preserving intrinsic/affinity/compatibility distinctions and unresolved evidence.

### CCTI-11 — Full candidate validation

After the complete candidate package, prove **11,017/11,017 accounting**, valid controlled values, identity/provenance preservation, correct model/non-model routing, no orphaned relationships and all Definition-vs-Instance boundaries.

### CCTI-12 — App-facing integration

Owner-gated and not started. Candidate data must not become user-facing/canonical merely because sidecars exist.

## Object Game-Readiness program

`OBJECT_GAME_READINESS_PROGRAM.md` defines the pathway from catalog parity to genuinely game-ready content. The current aggregate readiness baseline covers 11,017/11,017 rows and certifies **zero** rows as `GAME_READY`; it distinguishes Item Definitions, platform models, components/modules, rules/support records, services and legacy references.

Before OGR-05 mechanics reauthoring, present failing mechanics cohorts and the proposed current-rule repair policy to the owner. OGR-07 runtime and OGR-08 app-facing enablement retain existing Stage A owner gates.

## Current evidence

Item candidate-pass receipt:
`CCTI_ITEM_TAXONOMY_CANDIDATE_PASS_COMPLETION_RECEIPT_20260817.json`

Item cross-axis review:
- `CCTI09_ITEM_CROSS_AXIS_REVIEW_REPORT_20260817.md`
- `CCTI_ITEM_CROSS_AXIS_REVIEW_BASELINE_20260817.json`
- `CCTI_ITEM_CROSS_AXIS_REVIEW_ARTIFACT_RECEIPT_20260817.json`
- `CCTI_ITEM_TAXONOMY_ADOPTION_PROPOSAL_20260817.md`
- private review artifact `CCTI_Item_Cross_Axis_Review_20260817.zip`, SHA-256 `42a544b5231a721f909a2e4257a2ebcf5971bfda40411d1a052f079ace43f867`.

## Exact next action

Execute the exact **Platform v0.11.0 additive candidate projection/review** across all 5,628 Vehicles/Mecha/Spacecraft-domain rows, preserving the established 2,984 platform/model vs 2,644 non-model split and all evidence/review state. Do not enable Item taxonomy, mutate source/master CSVs or begin mechanics reauthoring.
