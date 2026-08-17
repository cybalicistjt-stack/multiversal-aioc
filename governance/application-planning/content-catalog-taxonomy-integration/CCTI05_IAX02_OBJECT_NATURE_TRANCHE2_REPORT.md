# CCTI-05 — IAX-02 Object-Nature Candidate Projection, Tranche 2

**Date:** 2026-08-17  
**Status:** CANDIDATE SIDECAR / NOT ENABLED  
**Source/master CSV mutation:** none  
**Mechanics mutation:** none

## Axis authority

Exact Item Taxonomy v0.12.0 defines `IAX-02 object_nature` as a **multi-select** axis with **17 controlled values**. A record may legitimately carry multiple natures, while unknown or ambiguous classifications must remain unresolved rather than being invented for coverage.

## Result

All **5,389 Item-corpus rows** have an explicit IAX-02 disposition:

- **3,325** rows — high-confidence candidate set only.
- **1,918** rows — one or more candidate assertions are medium-confidence / review-required.
- **110** rows — explicitly unresolved because current evidence did not support a safe intrinsic-nature assignment.
- **36** `Weapons_Ammo.csv` legacy/reference-only rows — not applicable; no current Item Definition is minted.
- silently unaccounted rows — **0**.

The 5,353 current Item Definition rows therefore contain **5,243 rows with at least one object-nature candidate** plus **110 explicit unresolved rows**.

Candidate assertions: **9,101** total:
- high-confidence: **6,919**;
- medium-confidence: **2,182**;
- low-confidence: **0**.

Value distribution:

| Object-nature value | assertions |
|---|---:|
| `arcane` | 2,385 |
| `computational` | 1,025 |
| `hybrid_composite` | 835 |
| `living_sentient_construct` | 737 |
| `electronic` | 583 |
| `powered_device` | 580 |
| `biological` | 534 |
| `mechanical` | 397 |
| `physical_mundane` | 344 |
| `extradimensional` | 321 |
| `cybernetic` | 311 |
| `symbiotic` | 266 |
| `psionic` | 180 |
| `digital_informational` | 167 |
| `chemical_alchemical` | 161 |
| `divine_sacred` | 148 |
| `energetic_field` | 127 |

## Conservative unresolved posture

The **110 unresolved rows are intentional**, not a failure-accounting gap. They are concentrated in general `Items.csv` records whose current fields describe use/context but do not safely prove intrinsic ontological/material nature, plus seven EVA customization-package definitions whose package contents can span several natures.

Independent axes continue even when IAX-02 is unresolved; an unresolved object-nature value must not be replaced by an invented classification merely to reach 100% populated values.

## Multi-select examples preserved

The derived model permits supported combinations such as:

- computational + digital/informational;
- biological + symbiotic;
- biological + symbiotic + cybernetic + hybrid/composite;
- arcane + living/sentient construct;
- arcane + hybrid/composite;
- powered device + energetic/field.

These are additive classification assertions and do not replace domain-native mechanics.

## Catalog treatment

- **Computers:** computational remains the principal nature. Software/AI is also digital/informational; physical mechanism, electronics and extraordinary power-source natures are secondary only where current fields support them.
- **Living Spellbooks / Magic Charge Holders:** arcane is explicit. Living Spellbooks also receive living/sentient-construct nature. Divine, psionic, biological, extradimensional and hybrid secondary candidates require explicit style evidence.
- **Magitech:** the catalog establishes arcane + hybrid/composite nature. Biomagitech, Divinetech, Psitech and other named types add only explicitly supported secondary candidates.
- **Symbiotes/Cybernetics:** domain-native `Upgrade Class` controls biological/symbiotic/cybernetic/hybrid candidates; support supplies are handled separately.
- **EVA:** powered/electronic/computational/biological/arcane/psionic/extradimensional candidates are driven by explicit item/module families and operating evidence. Generic customization packages may remain unresolved.
- **Weapons:** ordinary, mechanical, powered, energetic, chemical/alchemical, arcane, divine, psionic and extradimensional candidates require explicit category/power/special-rule evidence; genre alone is not used as intrinsic nature.
- **General Items:** magical, alchemical, electronic, powered, etc. candidates require specific source fields; broad setting/context labels are not converted into intrinsic nature.

## Validation

Deterministic tranche checks passed:

- exact axis: `IAX-02 object_nature`;
- registry cardinality: multi;
- controlled-value membership: 17 exact v0.12.0 values, zero foreign IDs;
- source accounting: 5,389/5,389;
- current Definition accounting: 5,353/5,353 candidate-or-explicit-unresolved;
- legacy/reference accounting: 36/36;
- duplicate same-value assertions per source row: 0;
- source/master mutation flags: false for all 9,101 assertions;
- canonical adoption state: `CANDIDATE_SIDECAR_NOT_ENABLED`.

Private assertion sidecar SHA-256: `a23883cab1ab916151dfa6db2142b1c291c59abe7640277fadc793cb26352173`  
Private 5,389-row summary SHA-256: `f5006c75007dc0ad152e600331c0e68f316e8932848b8befb39c9b0cc23ec897`  
Rules registry SHA-256: `2561a7389d09f3857dd032c063e3d21fb413403f09577468b93cbbccca401ea4`  
Baseline SHA-256: `f3138082449df1ccff44b8308296023995346b7394c8aed6ced9932c5d85f729`

## Private tranche artifact

`CCTI_Item_Taxonomy_Tranche2_IAX02_20260817.zip`  
SHA-256: `5ff36546966e0a438e0c946cf3730ac330522fd9ee5ab383bbdb8afe73ecd5c1`

## Exact next content operation

Proceed to **IAX-03 — form_factor** as another bounded multi-select candidate tranche. Preserve the 110 IAX-02 unresolved states for later review rather than treating them as blockers to independent axes. Mechanics reauthoring remains outside taxonomy projection.
