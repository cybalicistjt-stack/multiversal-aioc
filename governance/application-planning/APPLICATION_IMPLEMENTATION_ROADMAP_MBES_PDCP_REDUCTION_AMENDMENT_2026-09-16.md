# Application Implementation Roadmap — MBES PDCP Reduction Amendment

**Date:** 2026-09-16  
**Status:** OWNER-APPROVED PLANNING RECONCILIATION  
**Implementation authority:** none

## Decision

PDCP family reduction resolves the historical MBES 24-tranche planning split into **9 surviving implementation/proof tranches** without changing MBES's roadmap position or milestone IDs.

Historical baseline:

`MBES-01 → 02 → 03 → 04 → 05 → 06 → 07 → 08 → 09 → 10 → 11 → 12 → 13 → 14 → 15 → 16 → 17 → 18 → 19 → 20 → 21 → 22 → 23 → 24`

Effective PDCP-reduced strict order:

`MBES-01 → MBES-03 → MBES-05 → MBES-08 → MBES-12 → MBES-14 → MBES-18 → MBES-20 → MBES-24`

## Intra-family folds

- `01+02 → MBES-01` — site/project/authority/construction core;
- `03+04 → MBES-03` — material requirements + structural build assembly;
- `05+06+07 → MBES-05` — functional spaces/furnishing/reusable blueprint assemblies;
- `08+09+10 → MBES-08` — facility networks/automation/logistics integration;
- `12+13 → MBES-12` — civil terrain/hydrology transformation;
- `14+15+16 → MBES-14` — environment conditions/externalities/habitability/reactive-world integration;
- `18+19 → MBES-18` — durability/failure/defense/recovery;
- `20+21+23 → MBES-20` — settlement/transport/regional development;
- `24` retained as golden/MSLR handoff.

## Cross-family absorptions

Three historical standalone MBES runtimes are removed because their canonical/runtime owners already exist elsewhere:

- `MBES-11` production-chain truth → ICF + MIB-12 + Inventory/Asset + MIB-13/Economy. MBES retains facility/network/capacity adapters in `05/08/20/24`.
- `MBES-17` residents/households/crews/staffing/jobs → Character/MNCS + ODL + DPL + Project/Time. MBES retains facility-use/staffing prerequisite and settlement-capacity bindings in `05/20/24`.
- `MBES-22` property/funding/commerce/markets/taxes/contracts/trade → MIB-13/Economy + ODL + Project/Time. MBES retains construction funding/procurement and settlement economic-capacity references in `01/20/24`.

Shared generic infrastructure is also consumed rather than rebuilt:

- MERA — engineering topology/interfaces/dependency/failure/repair;
- GPR + Action/Event — gameplay execution/replay;
- PCA-12 + PDCP Packet 08 — simulation/formal/flow/capacity analysis;
- PDCP Packet 07 — preview/commit/explanation/intervention/recovery;
- PDCP Packet 06 — multi-resolution aggregate/detail semantics;
- MCS — cartographic/spatial authoring;
- reduced MSWI — cross-domain consequence propagation.

## Capability preservation

The authoritative before/after coverage map is:

- `governance/application-planning/preimplementation-design-closure/PDCP_MBES_REDUCTION_RECEIPT.json`.

The implementation-ready family design closure is:

- `governance/application-planning/preimplementation-design-closure/PDCP_MBES_FAMILY_DESIGN_CLOSURE.md`.

The receipt maps all 24 historical rows to a surviving tranche or canonical owner and preserves golden proof, migration/recovery, provenance, permissions/privacy, accessibility and deterministic validation obligations.

## DAG preservation

No `ROADMAP_DEPENDENCY_GRAPH.json` mutation is required by this reduction:

- `MBES-01` remains the MBES start/rotation gate;
- `MBES-24` remains the MBES golden gate;
- `MSLR-01` continues to require `MBES-24`;
- MERA remains the upstream family and will be interpreted through its eventual effective PDCP-reduced golden gate.

Sparse IDs are intentional provenance; removed IDs remain historical baseline references only.

## OPS3 boundary

This amendment is planning work only.

- `operations/CURRENT.json` is untouched;
- no MBES branch or implementation authority is granted;
- no product runtime or Campaign state is changed;
- MAS remains excluded from PDCP.

## PDCP count effect

Historical PDCP baseline remains **208**.

Before MBES reduction, effective future count after MSLR and MSWI was **188**.

MBES reduces **24 → 9**, removing 15 additional standalone future tranches.

New effective PDCP future count: **173**.

Standalone future tranches removed across resolved families: **35**.

Next PDCP family: **MERA**.
