# CCTI Write Phase — Tranche 2: Item IAX-02 Object-Nature Candidate Projection

**Date:** 2026-08-17  
**Status:** candidate sidecars produced; source masters unchanged; canonical adoption disabled

## Axis authority

Exact Item Taxonomy v0.12.0 defines `IAX-02 object_nature` as a **multi-select** axis with **17 controlled values**. Rules permit multiple values where intrinsically meaningful and require unknown/ambiguous classification to remain unresolved rather than inventing a value.

## Result

All **5,389 Item-corpus rows** have an explicit IAX-02 disposition:

- **3,325** rows: high-confidence candidate set only.
- **1,918** rows: one or more candidate assertions include medium-confidence/review-required evidence.
- **110** rows: explicitly unresolved because current evidence did not support a safe object-nature assignment.
- **36** `Weapons_Ammo.csv` legacy/reference-only rows: not applicable; no current Item Definition taxonomy minted.
- silently unaccounted rows: **0**.

The 5,353 current Item Definition rows therefore consist of **5,243 with at least one object-nature candidate** plus **110 explicit unresolved rows**.

Candidate assertions: **9,101** total:
- high-confidence assertions: **6,949**
- medium-confidence assertions: **2,152**
- low-confidence assertions: **0**

Value distribution:
- `arcane`: 2,385
- `computational`: 1,025
- `hybrid_composite`: 835
- `living_sentient_construct`: 737
- `electronic`: 583
- `powered_device`: 580
- `biological`: 534
- `mechanical`: 397
- `physical_mundane`: 344
- `extradimensional`: 321
- `cybernetic`: 311
- `symbiotic`: 266
- `psionic`: 180
- `digital_informational`: 167
- `chemical_alchemical`: 161
- `divine_sacred`: 148
- `energetic_field`: 127

## Conservative unresolved posture

The unresolved set is retained deliberately rather than forcing coverage. It is concentrated primarily in general `Items.csv` records whose current fields describe context/function but do not safely prove intrinsic material/ontological nature, plus seven EVA customization-package rows whose package contents can span several natures.

IAX-02 is multi-select. A row can therefore carry combinations such as:
- computational + digital/informational;
- biological + symbiotic;
- biological + symbiotic + cybernetic + hybrid/composite;
- arcane + living/sentient construct;
- arcane + hybrid/composite;
- powered device + energetic/field.

These combinations do not alter domain-native mechanics.

## Important catalog treatment

- **Computers:** computational is preserved as the principal nature; software/AI is also digital/informational; physical mechanisms, electronics and extraordinary power sources are secondary candidates only where source fields support them.
- **Living Spellbooks / Magic Charge Holders:** arcane is explicit; Living Spellbooks also receive living/sentient-construct nature; divine, psionic, biological, extradimensional and hybrid secondary candidates require explicit style evidence.
- **Magitech:** the catalog explicitly establishes arcane + hybrid/composite nature; Biomagitech/Divinetech/Psitech and other named types add only supported secondary candidates.
- **Symbiotes/Cybernetics:** domain-native Upgrade Class controls biological/symbiotic/cybernetic/hybrid classification; support supplies use separate evidence rules.
- **EVA:** powered/electronic/computational/biological/arcane/psionic/extradimensional candidates are driven by explicit item/module families and power evidence; generic customization packages are allowed to stay unresolved.
- **Weapons:** ordinary, mechanical, powered, energetic, chemical/alchemical, arcane, divine, psionic and extradimensional candidates are based on explicit category/power/special-rule evidence rather than genre alone.
- **General Items:** magical/alchemical/electronic/powered/etc. candidates require specific catalog evidence; broad contextual labels do not automatically become intrinsic nature.

## Validation

Deterministic tranche checks passed:

- exact axis ID: IAX-02;
- exact controlled-value membership: 17-value registry, no foreign IDs;
- source row accounting: 5,389/5,389;
- current Definition accounting: 5,353/5,353 candidate-or-explicit-unresolved;
- reference-only accounting: 36/36;
- duplicate axis value assertions per row: 0;
- source/master mutation flags: false for every assertion;
- canonical adoption state: candidate sidecar / not enabled.

Private assertion sidecar SHA-256: `a23883cab1ab916151dfa6db2142b1c291c59abe7640277fadc793cb26352173`  
Private 5,389-row summary SHA-256: `f5006c75007dc0ad152e600331c0e68f316e8932848b8befb39c9b0cc23ec897`  
Rules registry SHA-256: `2561a7389d09f3857dd032c063e3d21fb413403f09577468b93cbbccca401ea4`  
Baseline SHA-256: `f3138082449df1ccff44b8308296023995346b7394c8aed6ced9932c5d85f729`

## Next content operation

Proceed to **IAX-03 — form_factor** in another bounded multi-select candidate tranche. Preserve the 110 IAX-02 unresolved states for later review rather than treating them as blockers to independent axes. Mechanics reauthoring remains outside this taxonomy work.
