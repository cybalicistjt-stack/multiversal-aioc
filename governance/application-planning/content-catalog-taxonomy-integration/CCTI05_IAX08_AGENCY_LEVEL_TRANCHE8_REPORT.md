# CCTI Write Phase — Tranche 8: Item IAX-08 Agency-Level Candidate Projection

**Date:** 2026-08-17  
**Status:** candidate sidecars produced; source masters unchanged; canonical adoption disabled

## Axis authority

Exact Item Taxonomy v0.12.0 defines `IAX-08 agency_level` as a **single-select** axis with **11 controlled values** describing whether an item is inert, reactive, programmable, autonomous, bonded-intelligent, sentient, sapient, emergent, or unresolved. Agency metadata does not replace domain-native action economy, AI capacity, bonding, sentience, conflict, activation, or control mechanics.

## Result

All **5,389 Item-corpus rows** have an explicit IAX-08 disposition:

- **3,098** applicable current Definitions — high-confidence candidate.
- **2,248** applicable current Definitions — medium-confidence/review-required candidate.
- **7** IAX-01 `non_item_support_record` rows — not applicable.
- **36** `Weapons_Ammo.csv` legacy/reference-only rows — not applicable.
- silently unaccounted rows — **0**.

Thus **5,346 applicable current Definitions** each have exactly one agency candidate.

Value distribution:

| Agency value | rows |
|---|---:|
| `inert` | 3,146 |
| `bonded_intelligence` | 854 |
| `semi_autonomous` | 388 |
| `passive_reactive` | 313 |
| `programmable` | 303 |
| `sentient` | 197 |
| `autonomous` | 66 |
| `variable_emergent` | 55 |
| `triggered_automated` | 24 |
| `sapient` | 0 |
| `unknown` | 0 |

Zero-count controlled values remain valid registry values. In particular, incidental references to sapient beings or non-sapient materials are not treated as evidence that the item itself is sapient.

## Evidence posture and safeguards

- Living Spellbooks use the preparation package's high-confidence `Sentience_Level` and `Independent_Action` mappings. Emergent bonded intelligence maps to `bonded_intelligence`; fully sentient/telepathic books to `sentient`; independent arcane beings to `autonomous`; progression-dependent agency to `variable_emergent`; non-sentient, non-independent objects remain `inert`.
- Computers distinguish explicit sentience/self-awareness, independent operation, autopilot/expert/assistant logic, software programmability, automatic response, and passive monitoring. Static or user-operated computing is not automatically called autonomous.
- Actual symbiotes with Willpower/conflict/parasitism evidence map to `bonded_intelligence`; ordinary cybernetics remain inert/reactive unless source evidence supports more agency.
- EVA systems receive agency above inert only from explicit AI, automatic emergency behavior, or autonomous control evidence; a user-initiated scan/reaction is not misclassified as independent agency.
- Magitech sentience requires the item itself to be explicitly sentient; text about consuming or preserving another sapient/non-sapient identity is ignored as agency evidence. Scripted/runic routines and actual trigger systems may map to programmable/triggered automation.
- Melee and ranged weapons remain `inert` under direct user control; mechanical automatic cycling does not constitute agency.
- General Items remain `inert` unless explicit item-owned automated behavior is evidenced. A detector activated by the user is not treated as autonomous merely because its effect says it detects something.
- The taxonomy's `sapient` value is deliberately unused because no applicable current row provided safe item-self person-level agency evidence under this conservative pass.

## Validation

PASS:

- exact axis/cardinality: `IAX-08 agency_level`, single;
- exact 11-value v0.12.0 registry membership, zero foreign values;
- 5,389/5,389 source-row accounting;
- 5,346/5,346 applicable current Definitions have exactly one candidate;
- 7/7 non-item support records explicitly not applicable;
- 36/36 legacy/reference-only rows explicitly not applicable;
- zero silently unaccounted rows;
- zero duplicate candidates per source row;
- all nine Item source/master CSV SHA-256 values match the pre-write manifest;
- candidate taxonomy remains disabled/noncanonical;
- mechanics/runtime/game-ready state unchanged.

Private candidate SHA-256: `2371b90db1ac3bc28755dca380138682b12c929e11173c5962079a913d28f386`  
Private row-summary SHA-256: `c5ac23d0f1b205ae61f4bc816b765538bf0d2151623f14efd1327b02d6837f07`  
Rule-usage SHA-256: `0856078f19b82d02cc404171bf4818e2544ae88c8063763877e8cb069117c5e1`  
Baseline SHA-256: `32dbd463e328e99128c2d636d64ccbfb9b33b83d5a488023d9087a380a7503e7`

Private artifact: `CCTI_Item_Taxonomy_Tranche8_IAX08_20260817.zip`  
SHA-256: `5fcf56957d3f26a23189f5c541a3365b95b82aa4b9754b034db5cd4eba2f2ce9`

## Exact next content operation

Proceed to **IAX-09 — functional_domain**, the next multi-select axis. Preserve prior-axis review/unknown/not-applicable dispositions independently. Mechanics reauthoring remains outside taxonomy projection.
