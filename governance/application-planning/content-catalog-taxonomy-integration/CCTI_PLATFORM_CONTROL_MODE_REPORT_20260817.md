# CCTI Platform Control Mode Facet

**Date:** 2026-08-17  
**Status:** candidate disposition complete; not enabled

This tranche projects the exact Platform v0.11.0 `control_mode` facet across all **5,628** Vehicles/Mecha/Spacecraft-domain rows while preserving the established **2,984 platform/model/named-asset/archetype vs 2,644 non-model** routing. The facet is multi-select.

## Disposition

- **2,984** platform/model/named-asset/archetype rows have one or more control-mode candidates.
- **2,603** component/module rows remain explicitly `HOST_OR_RECORD_DEPENDENT`; host-platform control is not copied onto a component or module.
- **41** rules/support/service/consumable rows are explicitly `NOT_APPLICABLE`.
- **0** rows are silently unaccounted.
- The 2,984 candidate rows contain **3,106** controlled-value assertions.

Controlled assertion counts:

- `MV-PLAT-CONTROL-CREWED`: 1,652
- `MV-PLAT-CONTROL-SINGLE`: 1,325
- `MV-PLAT-CONTROL-ASSISTED`: 43
- `MV-PLAT-CONTROL-BONDED`: 31
- `MV-PLAT-CONTROL-BOUND`: 29
- `MV-PLAT-CONTROL-AUTONOMOUS`: 25
- `MV-PLAT-CONTROL-SWARM`: 1

No candidate was forced for `remote_piloted`, `semi_autonomous`, or `mixed_control`; zero-count controlled values remain valid registry values rather than being manufactured for coverage.

## Evidence policy

Direct-control candidates use explicit structured operating evidence:

- Vehicles: `Crew`;
- Mecha: `Pilot_Count`;
- Spacecraft: `Crew_Optimal` / `Crew_Min`.

Special modes require explicit primary-control/interface evidence. The projection deliberately rejects common false positives:

- `Crew = 0` alone never means autonomous;
- autonomous damage control does not make the host platform autonomous;
- repair drones, carried drones, drone-carrier roles and fleet-command AI do not classify the host platform control mode;
- generic neural-interface language does not imply a bonded/symbiotic control relationship;
- incidental AI/support text does not create autonomy.

Examples of additive special-mode evidence retained by the candidate sidecar include explicit autonomous vehicle control, automatic-pilot assistance, spoken-command/bound-spirit vehicle control, explicit symbiotic mecha interfaces, explicit assisted/manual-override mecha interfaces, and one source spacecraft archetype with explicit autonomous swarm operation.

## Validation

PASS:

- exact **5,628/5,628** row accounting;
- exact **2,984 / 2,644** platform/non-model routing preserved;
- all candidate IDs are members of the exact Platform v0.11.0 `control_mode` registry;
- source/master SHA-256 identities match the canonical CCTI baseline;
- no duplicate source row;
- no source/master CSV mutation;
- no prepared historical crosswalk rewrite;
- no canonical enablement, mechanics reauthoring, runtime asset creation, or `GAME_READY` claim;
- deterministic private artifact rebuild reproduces the same package SHA-256.

## Private artifact

`CCTI_Platform_Control_Mode_20260817.zip`  
SHA-256 `62c3d9bd2f8146298428644bd28bbe6b80044b78db39f03cf4f3aaaa4aa16b91`

The repository stores the governed aggregate/report/receipt. Row-level candidate evidence remains private and checksum-referenced, consistent with earlier CCTI candidate tranches.

## Next

Proceed to the final universal Platform facet, `platform_nature`, using explicit construction/origin evidence and preserving unresolved states rather than inferring living, artifact, magical, improvised, converted, or hybrid nature from genre labels alone.
