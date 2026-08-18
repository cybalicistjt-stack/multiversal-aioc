# CCTI Platform Nature Facet

**Date:** 2026-08-17  
**Status:** candidate disposition complete; not enabled

This tranche projects the final universal Platform v0.11.0 facet, `platform_nature`, across all **5,628** Vehicles/Mecha/Spacecraft-domain rows while preserving the established **2,984 platform/model/named-asset/archetype vs 2,644 non-model** routing. The facet is multi-select.

## Disposition

- **2,659** platform/model/named-asset/archetype rows have one or more explicit nature candidates.
- **325** platform/model/named-asset/archetype rows remain `UNRESOLVED_REVIEW` because the current source does not provide safe construction/origin evidence for a controlled nature value.
- **2,603** component/module rows remain explicitly `HOST_OR_RECORD_DEPENDENT`.
- **41** rules/support/service/consumable rows are explicitly `NOT_APPLICABLE`.
- **0** rows are silently unaccounted.
- The 2,659 candidate rows contain **3,267** controlled-value assertions.

Controlled assertion counts:

- `MV-PLAT-NATURE-MANUFACTURED`: 2,569
- `MV-PLAT-NATURE-BOUND-ANIMATED`: 183
- `MV-PLAT-NATURE-BIOENGINEERED`: 154
- `MV-PLAT-NATURE-MAGICAL-CONSTRUCT`: 121
- `MV-PLAT-NATURE-IMPROVISED`: 91
- `MV-PLAT-NATURE-LIVING`: 69
- `MV-PLAT-NATURE-ARTIFACT`: 62
- `MV-PLAT-NATURE-CONVERTED`: 18

No row is forced into `MV-PLAT-NATURE-HYBRID`. Generic `Hybrid` ship classes/roles are not treated as evidence that the platform has a foundational hybrid nature.

## Evidence policy

Nature is derived only from explicit construction/origin evidence in the current record. The projection deliberately rejects common false positives:

- genre or technology style alone never assigns nature;
- power source alone never assigns nature;
- creator identity, rarity, or market context do not assign nature;
- salvageability or support-service text does not make a platform improvised/salvaged;
- a generic `Hybrid` class/mission label does not create `Hybrid Nature`;
- special nature values require foundational evidence such as salvaged/rebuilt construction, cultured/grown biology, fully living platform language, runic/bound construction, or explicit precursor/ancient construction.

The 325 unresolved platform rows are retained rather than guessed. This includes source-defined records/archetypes where the available text defines role/class behavior but not safe construction nature.

## Validation

PASS:

- exact **5,628/5,628** row accounting;
- exact **2,984 / 2,644** platform/non-model routing preserved;
- all candidate IDs are members of the exact Platform v0.11.0 `platform_nature` registry;
- source/master SHA-256 identities match the canonical CCTI baseline;
- no duplicate source row;
- unresolved and host-dependent states remain explicit;
- no source/master CSV mutation;
- no prepared historical crosswalk rewrite;
- no canonical enablement, mechanics reauthoring, runtime asset creation, or `GAME_READY` claim;
- deterministic private artifact rebuild reproduces the same package SHA-256.

## Private artifact

`CCTI_Platform_Nature_20260817.zip`  
SHA-256 `f756f63c4b641fc541141141b02af57e3d6a56efc394e3bda19e177b864f3bdc`

The repository stores the governed aggregate/report/receipt. Row-level candidate evidence remains private and checksum-referenced.

## Next

All seven universal Platform facets now have explicit candidate/disposition state. Proceed to the Platform cross-facet review/consolidation before any canonical enablement, then continue the governed CCTI cross-domain graph/context pathway.
