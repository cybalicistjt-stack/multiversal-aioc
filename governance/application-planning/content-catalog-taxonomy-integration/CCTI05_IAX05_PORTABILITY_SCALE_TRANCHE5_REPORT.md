# CCTI Write Phase — Tranche 5: Item IAX-05 Portability-Scale Candidate Projection

**Date:** 2026-08-17  
**Status:** candidate sidecar produced; source masters unchanged; canonical adoption disabled

## Axis authority

Exact Item Taxonomy v0.12.0 defines `IAX-05 portability_scale` as a **single-select** axis with **10 controlled values** describing how portable an item normally is, independent of mechanical range/effect scale. `Computers.csv: Portability_P` remains domain-native authority; this tranche derives only a coarse universal portability candidate and does not replace that rating.

## Result

All **5,389 Item-corpus rows** have an explicit IAX-05 disposition:

- **1,899** rows — high-confidence candidate.
- **3,444** rows — medium-confidence/review-required candidate.
- **10** rows — explicitly unresolved because the current evidence does not safely support one portability value.
- **36** `Weapons_Ammo.csv` legacy/reference-only rows — not applicable.
- silently unaccounted rows — **0**.

The 5,353 current Item Definition rows therefore contain **5,343** rows with one portability candidate plus **10** explicit unresolved rows.

Candidate value distribution:
- `integrated_internal`: **1,439**
- `pocket`: **400**
- `personal_light`: **885**
- `personal_standard`: **1,991**
- `personal_bulky`: **235**
- `team_portable`: **76**
- `cartable`: **21**
- `vehicle_mounted`: **40**
- `fixed_installation`: **165**
- `structural`: **91**

## Evidence policy

The classifier uses explicit host/install/mount/site semantics before weight. Examples: cybernetic/symbiotic implants, EVA modules, computer software/components and Living Spellbook overlays may resolve to `integrated_internal`; vehicle/ship-mounted records resolve to `vehicle_mounted`; explicit facility/site-bound computer forms can resolve to `fixed_installation` or `structural`. For ordinary portable definitions, source Weight is used only as a **coarse universal candidate signal**, normally at medium confidence. Heavy platform-like records for which the Item portability axis does not safely describe the object remain unresolved rather than being forced into the nearest value.

`Computers.csv: Portability_P` is preserved unchanged. Where no stronger form/scope evidence exists, it may seed a medium-confidence coarse candidate only, consistent with the prepared field map and domain-native preservation rule.

## Validation

PASS:
- exact axis `IAX-05 portability_scale`, single-select;
- 10 exact v0.12.0 controlled values, zero foreign values;
- 5,389/5,389 source-row accounting;
- 5,353/5,353 current Definition candidate-or-explicit-unresolved accounting;
- 36/36 legacy/reference-only accounting;
- zero duplicate portability candidates per source row;
- all nine source/master CSV SHA-256 values still match the pre-write manifest;
- source/master mutation flags false for every candidate;
- canonical adoption remains `CANDIDATE_SIDECAR_NOT_ENABLED`.

Private candidate SHA-256: `e34d7a8f9f42523349536b25b598b006c1e388dc21afe9a4fb2f77a6a723a54e`  
Private row-summary SHA-256: `1897674bf799343432b84c86420a8f876a3764474d0c21c41add304ca4d490f5`  
Rule-usage SHA-256: `5906b24abcbc7224bc569eb85dfcb4135a140f187735bf4b7d0d0c4f55323dd5`  
Baseline SHA-256: `b8e37100e75e247e6503b30c4b680833e82e7a327cd21b76952c14ae30c34828`

## Exact next content operation

Proceed to **IAX-06 — consumption_lifecycle**, the next multi-select axis. Preserve IAX-02/IAX-03/IAX-04/IAX-05 unresolved states independently; do not use later-axis evidence to overwrite prior-axis review states. Mechanics reauthoring remains outside taxonomy projection.
