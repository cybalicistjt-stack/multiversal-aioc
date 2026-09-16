# PDCP Cross-Family Overlap & Folding Register

**Project:** PDCP — Preimplementation Design Closure Project  
**Status:** ACTIVE REDUCTION CONTROL SURFACE  
**Implementation authority:** none

## Rule

Every family reduction must perform both:

1. an **intra-family overlap audit** — merge baseline tranches that implement the same state/operation/workflow/proof seam when one bounded implementation tranche can credibly own the residual work; and
2. a **cross-family/shared-owner audit** — remove duplicate generic/canonical infrastructure and retain only domain-specific schemas, adapters, UX and proof.

A tranche does not survive merely because the historical roadmap numbered it separately. Candidate rows do not mutate counts until a complete family receipt merges.

## Shared ownership patterns

| Shared concern | Generic/canonical owner | Specialist rule |
|---|---|---|
| proposal → preview/dry-run → commit → explanation → compensation | canonical owner operations + Packet 07 | families implement domain operations/lenses only |
| simulation, graph/SAT/SMT/optimization/Monte-Carlo/ABM | PCA-12 + Packet 08 | families provide model adapters and interpretation only |
| procedural DAG/recipe/cache/seed | PCA-02/PCA-03 | domain generator packs only |
| resource identity, rights, derivative provenance | ARI + PCA-01/PCA-15 | domain serializers/validation only |
| generic gameplay execution, replay and delivery | reduced GPR + Action/Event | specialist families provide domain adapters only |
| semantic affordances/effect composition | MRCS + reduced GPR + Packet 04 | definitions remain MRCS/domain-owned; GPR executes accepted semantics |
| map/cartographic projection/editing | MCS | domains bind semantic projections only |
| multi-resolution aggregate↔individual | Packet 06 + domain owners | local lifecycle adapters only |
| systemic consequence propagation | reduced MSWI | upstream systems emit typed Events/deltas |
| engineering topology/interfaces/dependency/failure/repair orchestration | reduced MERA + underlying Asset/MIB owners | reduced MBES and later consumers bind building/infrastructure adapters only |
| salvage/decomposition/donor lineage | LSS | MERA plans/hands off; no duplicate salvage truth |
| repair/refurbishment/remanufacture/fabrication transaction | MIB-12 | MERA orchestrates engineering workflows only |
| work capability/project/time | DPL/Profession + APW/D26 | consumers validate prerequisites; no parallel scheduler |
| garage/hangar/workshop/built facility context | MIB-14/PPIA-04 + reduced MBES | MERA/GPR consumers bind facility context only |
| production/cultivation truth | ICF + MIB-12 + Inventory/Asset + Economy | reduced MBES facility bindings only |
| residents/households/jobs/staffing | Character/MNCS + ODL + DPL + Project/Time | reduced MBES capacity/use bindings only |
| property/funding/markets/contracts/trade | MIB-13/Economy + ODL + Project/Time | reduced MBES references only |

## Global repeated patterns

### Authority/workspace openings

Future `-01` tranches survive only if material schema/workspace/runtime-shell work remains after PDCP design closure. Resolved examples include MSLR, MSWI, MBES, MERA and now GPR opening-tranche folds.

### Interchange/version/review/provenance

Remaining strong candidates:

- `MCS-19+20`;
- `MCCS-19` slimmed to domain adapters;
- `MNCS-23` slimmed to domain adapters;
- `MSAS-18+19+20`;
- `MRCS-19+20`.

Generic rights/provenance/version/review/import-export stays ARI/PCA.

### Creator/debug/simulation workbenches

Remaining candidates are primarily MRCS and specialist creator diagnostics. Resolved GPR historical `09+14 → GPR-09`; Packet 07 owns generic Creator/GM execution-inspection semantics, while GPR keeps only gameplay-specific authoring/delivery/control integration.

### Procedural generation

Remaining candidates:

- `MCS-10+11+12` over PCA recipes;
- `MNCS-02` domain recipe layer over PCA-02.

### Golden/conformance gates

Proof-only pre-golden tranches merge into the final gate when no independent runtime remains. Resolved GPR historical `15+16 → GPR-16`; the entire 168-pattern/85-operation/672-variant battery remains mandatory final evidence.

## Remaining family candidates

### MRCS — next selected review

- `MRCS-18`: generic simulation engine must be absorbed by PCA-12/Packet 08; retain only rule/content model adapters and interpretation.
- `MRCS-17 + slimmed MRCS-18`: inspect as one dependency/impact/balance diagnostics seam if bounded.
- `MRCS-19+20`: strong migration/import/batch-edit + pack/version/review/provenance/publication consolidation candidate.
- `MRCS-01+02`: inspect workspace/registry/form overlap after PDCP closure, but preserve a distinct opening implementation seam only if material shell/schema work remains.
- `MRCS-03`: consume shared guided-creation/Packet-07 semantics rather than building a second generic creator framework.
- `MRCS-04+05` must be checked carefully: expression/rule atoms and Action/Effect/Condition/Resource authoring share infrastructure but may remain separate if implementation payload would exceed tranche bounds.
- Reduced GPR confirms MRCS owns reusable definition truth while GPR executes accepted definitions; MRCS must not retain runtime execution duplication.

### MSAS

- `MSAS-17`: generated music/SFX/voice should be absorbed into corresponding domain workflows; PCA owns generic generation orchestration.
- `MSAS-18+19+20`: version/review/interchange/rights/publication delivery pipeline.
- `MSAS-15`: consume Packet-07 live-GM semantics.

### MNCS

- `MNCS-15+16+17`: group/population/herd/ecosystem generation share aggregate recipe/individualization machinery.
- `MNCS-20+21`: continuity/change-over-time + resolution promotion/demotion share lifecycle state.
- `MNCS-23`: slim to domain batch/preset/import adapters.

### MCCS

- `MCCS-13+14+15`: output/derivative renderer substrate.
- Test `MCCS-16` for absorption if style/profile work is mostly configuration.
- `MCCS-19`: consume common interchange/review/provenance infrastructure.

### MCS

- `MCS-10+11+12`: shared map/world-generation substrate with domain generator packs over PCA.
- `MCS-19+20`: interchange/version/review/publishing workflow.
- Review `MCS-13+14+16` for common built/interior/multi-level projection core while preserving genuinely different city/dungeon UX.

## Resolved families

### MSLR — 18 → 9

`01+02→01`; `03+06→03`; `04+05+11→04`; `07+12→07`; `08+09+10→08`; `13+15→13`; `14+17→14`; `16` retained; `18` retained.

Receipt: `PDCP_MSLR_REDUCTION_RECEIPT.json`.

### MSWI — 18 → 7

`01+02→01`; `03` retained; `04+05→04`; `06` retained; `07+08→07`; historical `09..13` absorbed to canonical/runtime owners with residual MSWI adapters; `14+15+16→14`; `17+18→18`.

Receipt: `PDCP_MSWI_REDUCTION_RECEIPT.json`.

### MBES — 24 → 9

`01+02→01`; `03+04→03`; `05+06+07→05`; `08+09+10→08`; historical `11` absorbed to production owners; `12+13→12`; `14+15+16→14`; historical `17` absorbed to people/work owners; `18+19→18`; `20+21+23→20`; historical `22` absorbed to economy/property owners; `24` retained.

Receipt: `PDCP_MBES_REDUCTION_RECEIPT.json`.

### MERA — 24 → 10

`01+02→01`; `03+04+23→03`; `05+09+22→05`; `06` retained; `07+08+20→07`; `10+11→10`; `12` retained; `13+14+15→13`; `16` retained; historical `17+18` absorbed to LSS/MIB-12; historical `19+21` absorbed to DPL/APW/MIB-14/reduced MBES; `24` retained.

Receipt: `PDCP_MERA_REDUCTION_RECEIPT.json`.

### GPR — 16 → 10

- `01+02 → 01`;
- `03` retained;
- `04+05 → 05`, preserving the MERA rotation milestone;
- `06` retained;
- `07` retained;
- `08` retained;
- `09+14 → 09` over Packet-07 shared creator/GM semantics;
- `10+11 → 10` with generic rights/provenance remaining ARI/PCA and creator assets remaining specialist-owned;
- `12+13 → 12` as one multiplayer/replay/persistence/recovery/version-continuity seam;
- `15+16 → 16`, making full conformance part of final golden proof.

Receipt: `PDCP_GPR_REDUCTION_RECEIPT.json`.

## Reduction order

With MSLR, MSWI, MBES, MERA and GPR resolved, the preferred reverse-consumer order is:

1. **MRCS** next;
2. **MSAS**;
3. **MNCS**;
4. **MCCS**;
5. **MCS**.

If a later upstream reduction exposes a safer shared-owner consolidation, an already-resolved downstream receipt may be amended only with an explicit capability-preserving reconciliation receipt.

## Guardrails

- MAS is excluded.
- Candidate folds do not alter counts until complete receipts merge.
- Generic infrastructure is implemented once; domain semantics stay with domain owners.
- PDCP does not mutate `operations/CURRENT.json` merely for design work.
- Preserve start/rotation/golden DAG milestone IDs where possible; sparse stable IDs are preferred.
- Accessibility, permissions/privacy, provenance, replay/recovery, migration and deterministic proof obligations must survive every fold.
