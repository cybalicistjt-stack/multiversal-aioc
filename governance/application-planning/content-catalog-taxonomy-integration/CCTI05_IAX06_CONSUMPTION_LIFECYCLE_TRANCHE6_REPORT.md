# CCTI Write Phase — Tranche 6: Item IAX-06 Consumption-Lifecycle Candidate Projection

**Date:** 2026-08-17  
**Status:** candidate sidecars produced; source masters unchanged; canonical adoption disabled

## Axis authority

Exact Item Taxonomy v0.12.0 defines `IAX-06 consumption_lifecycle` as a **multi-select** axis with **13 controlled values**. It describes whether an item persists, expends charges, consumes fuel/supplies, degrades, or is single-use. Domain-native capacity, durability, power, recharge, ammunition, repair, and maintenance mechanics remain authoritative and are not replaced by this universal metadata.

## Result

All **5,389 Item-corpus rows** have an explicit IAX-06 disposition:

- **796** rows — high-confidence candidate set only.
- **4,550** rows — one or more medium-confidence/review-required candidates.
- **7** current Definitions with IAX-01 `non_item_support_record` scope — explicitly not applicable to this lifecycle axis.
- **36** `Weapons_Ammo.csv` legacy/reference-only rows — not applicable.
- explicit unresolved applicable rows — **0**.
- silently unaccounted rows — **0**.

Thus **5,346 lifecycle-applicable current Item Definitions** have at least one candidate assertion. Candidate assertions total **13,899**: **2,748 high-confidence** and **11,151 medium-confidence/reviewable**.

Value distribution:

| Lifecycle value | assertions |
|---|---:|
| `durable_reusable` | 4,816 |
| `indefinite_if_maintained` | 2,365 |
| `limited_charges` | 1,755 |
| `degradable` | 1,706 |
| `rechargeable` | 1,309 |
| `refillable` | 1,272 |
| `single_use` | 324 |
| `consumable_supply` | 178 |
| `persistent_software` | 167 |
| `regenerating_biological` | 5 |
| `expendable_ammunition` | 1 |
| `disposable` | 1 |
| `perishable` | 0 |

A zero count is not converted into an invented assignment. No current row had sufficient lifecycle-specific evidence for `perishable` under the conservative rule set.

## Important semantic safeguards

- `single_use` is not inferred from strings such as `1 use per day`, `1 use per rest`, or a one-use capacity that explicitly regrows/recharges; those are limited-use/recharge semantics rather than destruction of the definition's object.
- Thrown self-contained grenade records are treated as single-use objects; reloadable grenade launchers remain durable/refillable hosts.
- `expendable_ammunition` is assigned only where the prior IAX-03 form-factor evidence explicitly identifies projectile ammunition; a weapon that merely uses ammunition is instead a refillable host candidate.
- IAX-01 `software_data` receives `persistent_software`; routine software calibration is not misread as physical degradation.
- `disposable` and `perishable` require lifecycle/form/category evidence, not incidental words in narrative effect text. This avoids false classifications such as a durable book describing summoned creatures as disposable.
- `regenerating_biological` requires evidence that the item's own functional capacity regrows/restores biologically; an item that merely heals a character is not enough.
- Scheduled service/repair may support `degradable` or `indefinite_if_maintained` only as reviewable metadata. Negative evidence such as “cannot be repaired after use” blocks indefinite-maintenance inference.
- The seven IAX-01 non-item support/rule records remain explicitly not-applicable rather than receiving forced lifecycle values.

## Validation

PASS:
- exact axis/cardinality: `IAX-06 consumption_lifecycle`, multi;
- exact 13-value v0.12.0 registry membership, zero foreign values;
- 5,389/5,389 source-row accounting;
- 5,346/5,346 lifecycle-applicable current Definitions carry candidate assertions;
- 7/7 non-item support records explicitly not applicable;
- 36/36 legacy/reference-only rows explicitly not applicable;
- zero silently unaccounted rows;
- zero duplicate same-value assertions per source row;
- all nine source/master CSV SHA-256 values still match the pre-write manifest;
- source/master mutation false for every assertion;
- canonical adoption remains `CANDIDATE_SIDECAR_NOT_ENABLED`.

Private assertion SHA-256: `6a30a3074fa5f22b9cdea908b4d0c5547165b3a8b0f51430f6ed664b96ae7633`  
Private row-summary SHA-256: `8da19718063f9f57f55df1debc776c66882ef336d70c4e5ce502839fda17b84b`  
Rule-usage SHA-256: `669378410ce2f36b1c9c6b6c44c4046ce6070b99932b6a91bf63d5f63cfb7ae9`  
Baseline SHA-256: `fb24404ff543d1bc1a3f8afb8909d8585aadeb999d3437971b2f0ce046c02081`

## Exact next content operation

Proceed to **IAX-07 — operational_complexity**, the next single-select axis. Preserve prior-axis review/not-applicable dispositions independently. Mechanics reauthoring remains outside taxonomy projection.
