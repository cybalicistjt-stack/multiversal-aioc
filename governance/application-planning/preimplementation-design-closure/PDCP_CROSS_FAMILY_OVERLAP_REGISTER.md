# PDCP Cross-Family Overlap & Folding Register

**Project:** PDCP — Preimplementation Design Closure Project  
**Status:** ACTIVE REDUCTION CONTROL SURFACE  
**Implementation authority:** none

## Rule

Every family reduction performs both an intra-family overlap audit and a cross-family/shared-owner audit. A historical tranche survives only when a distinct bounded implementation/proof seam remains after design closure and shared-owner absorption.

## Shared ownership patterns

| Concern | Generic/canonical owner | Specialist rule |
|---|---|---|
| proposal/preview/dry-run/commit/explain/compensate/debug | canonical owner operations + Packet 07 | family-specific operations/lenses only |
| simulation/graph/SAT/SMT/optimization/Monte Carlo/ABM | PCA-12 + Packet 08 | model adapters and interpretation only |
| procedural DAG/recipe/cache/seed | PCA-02/PCA-03 | domain generator packs only |
| identity/rights/derivative provenance/version/review/import-export | ARI + PCA | domain mapping/serialization/validation only |
| generic gameplay execution/replay/delivery | reduced GPR + Action/Event | domain adapters only |
| reusable rule/content definition authoring | reduced MRCS + owner-domain contracts | specialist studios retain their visual/domain creator UX |
| semantic affordances/effect composition | reduced MRCS definitions + reduced GPR execution + Packet 04 | target/domain adapters only |
| map/cartographic projection/editing | MCS | other families bind map projections only |
| multi-resolution aggregate↔individual | Packet 06 + domain owners | lifecycle adapters only |
| systemic consequence propagation | reduced MSWI | upstream systems emit typed Events/deltas |
| engineering orchestration | reduced MERA + Asset/MIB owners | consumers bind engineering adapters only |
| built environment/facilities | reduced MBES + underlying owners | consumers reference facility context |
| salvage/decomposition/donor lineage | LSS | engineering consumers hand off |
| repair/refurbish/remanufacture/fabrication transactions | MIB-12 | orchestration only |
| work capability/project/time | DPL/Profession + APW/D26 | prerequisite bindings only |

## Repeated folding rules

- opening workspace/authority and registry/schema tranches merge when they form one implementation shell;
- generic creator/debug and simulation workbenches are not rebuilt per family;
- generic interchange/version/review/provenance is not rebuilt per family;
- proof-only pre-golden tranches fold into final golden proof when no independent runtime remains;
- sparse historical IDs are preferred over renumbering when DAG milestones can survive.

## Next selected review — MSAS

Strong candidates to test:

- `MSAS-18+19+20`: one rights-safe interchange/version/review/delivery/publication lifecycle;
- `MSAS-17`: generated music/SFX/voice should use PCA/provider orchestration and stay inside the relevant audio workflows rather than create a separate generic generation engine;
- `MSAS-15`: consume Packet-07 live-GM control semantics rather than implement another generic live-control framework;
- audit whether acquisition/editing/mixing/mastering/export tranches form fewer bounded production kernels without erasing materially different audio workflows;
- preserve whichever start/golden milestone IDs are referenced by the DAG.

## Later family candidates

### MNCS
- `15+16+17`: population/group/herd/ecosystem generation over shared aggregate machinery;
- `20+21`: continuity/change-over-time plus resolution promotion/demotion;
- `23`: slim to domain batch/preset/import adapters.

### MCCS
- `13+14+15`: output/derivative renderer substrate;
- inspect `16` for absorption when style/profile behavior is configuration;
- `19`: consume generic interchange/review/provenance infrastructure.

### MCS
- `10+11+12`: shared world/map-generation substrate over PCA recipes;
- `19+20`: interchange/version/review/publishing;
- inspect `13+14+16` for a shared built/interior/multi-level projection kernel without collapsing distinct city/dungeon UX.

## Resolved families

### MSLR — 18 → 9
`01+02→01`; `03+06→03`; `04+05+11→04`; `07+12→07`; `08+09+10→08`; `13+15→13`; `14+17→14`; `16`; `18`.

### MSWI — 18 → 7
`01+02→01`; `03`; `04+05→04`; `06`; `07+08→07`; historical `09..13` absorbed to owners with MSWI consequence adapters; `14+15+16→14`; `17+18→18`.

### MBES — 24 → 9
`01+02→01`; `03+04→03`; `05+06+07→05`; `08+09+10→08`; `11` absorbed to production owners; `12+13→12`; `14+15+16→14`; `17` absorbed to people/work owners; `18+19→18`; `20+21+23→20`; `22` absorbed to economy/property owners; `24`.

### MERA — 24 → 10
`01+02→01`; `03+04+23→03`; `05+09+22→05`; `06`; `07+08+20→07`; `10+11→10`; `12`; `13+14+15→13`; `16`; `17+18` absorbed to LSS/MIB-12; `19+21` absorbed to DPL/APW/MIB-14/MBES; `24`.

### GPR — 16 → 10
`01+02→01`; `03`; `04+05→05`; `06`; `07`; `08`; `09+14→09`; `10+11→10`; `12+13→12`; `15+16→16`.

### MRCS — 21 → 13
`01+02→01`; `03`; `04`; `05+06+07→05`; `08+09→08`; `11`; `12`; `10+13→13`; `14+15→14`; `16`; `17+18→17`; `19+20→19`; `21`.

MRCS-specific shared-owner result: PCA-12/Packet 08 own generic analysis; Packet 07 owns generic creator/debug semantics; ARI/PCA own generic provenance/version/review/import-export; reduced GPR executes accepted definitions; specialist studios remain specialist authoring owners.

## Reduction order

Resolved: MSLR, MSWI, MBES, MERA, GPR, MRCS. Remaining preferred order:

1. **MSAS** next;
2. **MNCS**;
3. **MCCS**;
4. **MCS**.

Already-resolved receipts may be amended later only through explicit capability-preserving reconciliation if an upstream reduction reveals a safer owner fold.

## Guardrails

MAS is excluded. Candidate folds do not alter counts before complete receipts merge. Accessibility, permissions/privacy, provenance, replay/recovery, migration and deterministic proof survive every fold. PDCP does not mutate `operations/CURRENT.json` merely for planning work.
