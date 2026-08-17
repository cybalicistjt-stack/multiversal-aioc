# CCTI Write Phase — Tranche 7: Item IAX-07 Operational-Complexity Candidate Projection

**Date:** 2026-08-17  
**Status:** candidate sidecars produced; source masters unchanged; canonical adoption disabled

## Axis authority

Exact Item Taxonomy v0.12.0 defines `IAX-07 operational_complexity` as a **single-select** axis with **9 controlled values**. It describes general operational/maintenance complexity and explicitly does **not** classify technology era, magic tier, rarity, price, or mechanical power.

## Result

All **5,389 Item-corpus rows** have an explicit IAX-07 disposition:

- **3,805** applicable current Definitions — high-confidence candidate.
- **1,541** applicable current Definitions — medium-confidence/review-required candidate.
- **7** IAX-01 `non_item_support_record` rows — not applicable.
- **36** `Weapons_Ammo.csv` legacy/reference-only rows — not applicable.
- silently unaccounted rows — **0**.

Thus **5,346 operational-complexity-applicable current Definitions** each have exactly one candidate. The exact `unknown` controlled value is used for **225** applicable records where current evidence does not support a safer class; it is review-required rather than being replaced by a guessed value.

Value distribution:

| Complexity value | rows |
|---|---:|
| `specialist` | 1,582 |
| `system_integrated` | 1,441 |
| `autonomous_complex` | 980 |
| `trained` | 599 |
| `simple` | 312 |
| `unknown` | 225 |
| `complex_system` | 207 |
| `unique_artifact` | 0 |
| `variable` | 0 |

Zero-count controlled values remain valid registry values; no row is forced into them merely to exercise the taxonomy.

## Evidence posture

The tranche uses domain-native evidence without replacing it:

- Melee `Proficiency` directly distinguishes simple / trained / specialist complexity.
- EVA modules/interfaces/upgrades are `system_integrated`; suit chassis with fitting/check/subsystem evidence are `complex_system`.
- Computer modules/interfaces/upgrades are system-integrated; complete/control/network/workstation systems may be complex systems; explicit autonomous/AI behavior can support `autonomous_complex`; advanced software remains specialist/trained according to supported function.
- Magitech `Required Knowledge` is specialist evidence; technology/magic tier is not used.
- Cybernetic/symbiote specialist surgery/DC evidence supports specialist complexity unless the definition is already structurally system-integrated by record scope.
- Living Spellbook explicit sentience/independent action can support autonomous-complex classification; otherwise Required Skill/Tools and bond/maintenance evidence support specialist complexity.
- Ranged weapons remain reviewable trained/specialist candidates because no universal proficiency field exists; heavy/mounted/launcher evidence may support specialist.
- General Items use only explicit category/subcategory/activation/requirement evidence. Genre, tech tier, rarity, cost and other deferred facets are excluded.
- `unique_artifact` requires explicit singular/one-of-a-kind/nonreplicable evidence, not rarity or legendary naming. None of the current applicable rows met the conservative test.
- `variable` requires evidence that operational complexity materially varies by implementation/configuration. No current row met the conservative test.

## Validation

PASS:

- exact axis/cardinality: `IAX-07 operational_complexity`, single;
- exact 9-value v0.12.0 registry membership, zero foreign values;
- 5,389/5,389 source-row accounting;
- 5,346/5,346 applicable current Definitions have exactly one candidate;
- 7/7 non-item support records explicitly not applicable;
- 36/36 legacy/reference-only rows explicitly not applicable;
- zero silently unaccounted rows;
- zero duplicate candidate rows per source row;
- all nine Item source/master CSV SHA-256 values match the pre-write manifest;
- candidate taxonomy remains `CANDIDATE_SIDECAR_NOT_ENABLED`;
- mechanics/runtime/game-ready state unchanged.

Private candidate SHA-256: `f296f00a67c74f4541f3883397c8bc144b8ee6d13d7ef371e8bac531e117cde2`  
Private row-summary SHA-256: `ff5167ef8011155cf27de0f1520cbde0cdedef9492c9514a017e7ed2b5200ba0`  
Rule-usage SHA-256: `129283bd1e479f542ff381c54533f0f92ee9cf93f06d68b93c78d894a1ef0c04`  
Baseline SHA-256: `5b195d4af45eb9dbeb86a904c2c244c4acff1b5c1100683b6b143fcb9a6d8633`

Private artifact: `CCTI_Item_Taxonomy_Tranche7_IAX07_20260817.zip`  
SHA-256: `bb4818ca1927076a9702349425f8748fb4c1895a0105f09f3410fba1e96da2b9`

## Exact next content operation

Proceed to **IAX-08 — agency_level**, the next single-select axis. Preserve prior-axis unresolved/unknown/not-applicable states independently. Mechanics reauthoring remains outside taxonomy projection.
