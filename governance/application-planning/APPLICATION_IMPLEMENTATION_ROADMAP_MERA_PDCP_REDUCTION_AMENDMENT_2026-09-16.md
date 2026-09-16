# Application Implementation Roadmap — MERA PDCP Reduction Amendment

**Date:** 2026-09-16  
**Program:** MERA — Multiversal Engineering, Refit & Assembly  
**Authority:** owner-approved PDCP family reduction planning  
**Implementation authority:** none

## Decision

The historical MERA baseline of 24 planned tranches is reduced to an effective implementation/proof order of 10 tranches after complete intra-family and cross-family overlap review.

Effective order:

`MERA-01 → MERA-03 → MERA-05 → MERA-06 → MERA-07 → MERA-10 → MERA-12 → MERA-13 → MERA-16 → MERA-24`

Historical tranche IDs remain provenance through `PDCP_MERA_REDUCTION_RECEIPT.json`.

## Consolidations

- `01+02 → MERA-01`
- `03+04+23 → MERA-03`
- `05+09+22 → MERA-05`
- `06 → MERA-06`, plus engineering recovery residuals from `17/18/19`
- `07+08+20 → MERA-07`, plus engineering recovery/work-context residuals from `17/18/19/21`
- `10+11 → MERA-10`
- `12 → MERA-12`
- `13+14+15 → MERA-13`
- `16 → MERA-16`
- `24 → MERA-24`

## Existing-owner absorptions

Historical `MERA-17` and `MERA-18` no longer represent standalone MERA engines. LSS retains salvage/decomposition/donor/cannibalization lineage and MIB-12 retains repair/refurbishment/remanufacture/fabrication transactions. MERA retains only planning, compatibility, disassembly/handoff, emergency/repair orchestration and proof.

Historical `MERA-19` and `MERA-21` no longer represent standalone MERA labor/project/facility schedulers. DPL/Profession retains worker capability, APW/D26 retains Project/time, MIB-14/PPIA-04 retains Vehicle/Base/Fleet context and reduced MBES retains built workshops/garages/hangars/facilities. MERA consumes those owner states as engineering prerequisites.

## Shared infrastructure absorptions

MERA consumes rather than duplicates:

- Packet 07 generic preview/dry-run/commit/explanation/recovery;
- PCA-12 + Packet 08 generic simulation/formal-analysis machinery;
- ARI/PCA generic provenance/version/review/import/export infrastructure;
- GPR + Action/Event execution/replay;
- Packet 04 semantic affordance/effect composition.

## Vehicle-family consolidation

`MERA-13`, `14`, and `15` are one implementation seam because completed PPIA-04 already governs Vehicle, Mecha and Starship as one semantic experience family. MERA implements one shared engineering adapter substrate with target-specific profiles. This does not erase target-specific mechanics or compatibility rules.

`MERA-16` remains separate because machinery, robotics, constructs and industrial/special systems may bind different owners, autonomy/control rules and built-facility contexts.

## DAG and milestone preservation

No dependency-graph edit is required for this reduction:

- `MERA-01` remains the family start/rotation milestone;
- `MERA-24` remains the MERA golden proof;
- MBES continues to consume MERA through its existing governed dependency/golden relationship;
- historical roadmap amendments remain provenance and do not override the current DAG or reduced backlog.

## Count effect

PDCP historical baseline remains **208**.

Approved reductions after this amendment:

- MSLR `18 → 9`;
- MSWI `18 → 7`;
- MBES `24 → 9`;
- MERA `24 → 10`.

Effective future total becomes **159**. Standalone future tranches removed becomes **49**.

## Next PDCP family

**GPR — Gameplay Pattern Runtime & Loop Minis** is next in the overlap-aware reverse-consumer review order.
