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
| generic gameplay execution/replay | GPR + Action/Event | specialist adapters only |
| semantic affordances/effect composition | MRCS/GPR + Packet 04 | target/domain adapters only |
| map/cartographic projection/editing | MCS | domains bind semantic projections only |
| multi-resolution aggregate↔individual | Packet 06 + domain owners | local lifecycle adapters only |
| systemic consequence propagation | reduced MSWI | upstream systems emit typed Events/deltas |
| engineering topology/interfaces/dependency/failure/repair orchestration | reduced MERA + underlying Asset/MIB owners | reduced MBES and later consumers bind building/infrastructure adapters only |
| salvage/decomposition/donor lineage | LSS | MERA plans/hands off; does not duplicate salvage truth |
| repair/refurbishment/remanufacture/fabrication transaction | MIB-12 | MERA orchestrates engineering workflows only |
| work capability/project/time | DPL/Profession + APW/D26 | MERA/MBES/etc. validate prerequisites; no parallel scheduler |
| garage/hangar/workshop/built facility context | MIB-14/PPIA-04 + reduced MBES | MERA consumes facility context rather than owning it |
| production/cultivation truth | ICF + MIB-12 + Inventory/Asset + Economy | reduced MBES facility bindings only |
| residents/households/jobs/staffing | Character/MNCS + ODL + DPL + Project/Time | reduced MBES capacity/use bindings only |
| property/funding/markets/contracts/trade | MIB-13/Economy + ODL + Project/Time | reduced MBES references only |

## Global repeated patterns

### Authority/workspace openings

Future `-01` tranches survive only if material schema/workspace/runtime-shell work remains after PDCP design closure. Resolved examples:

- MSLR `01+02 → 01`;
- MSWI `01+02 → 01`;
- MBES `01+02 → 01`;
- MERA `01+02 → 01`.

### Interchange/version/review/provenance

Remaining strong candidates:

- `MCS-19+20`;
- `MCCS-19` slimmed to domain adapters;
- `MNCS-23` slimmed to domain adapters;
- `MSAS-18+19+20`;
- `MRCS-19+20`.

Resolved MERA: historical `MERA-23` merged into `MERA-03`; generic infrastructure stays ARI/PCA.

### Creator/debug/simulation workbenches

Remaining candidates:

- `GPR-14` plus creator/GM portions of `GPR-12..16`;
- MRCS dependency/balance analysis;
- MCS/MCCS/MNCS creator diagnostics.

Resolved families consume Packet 07 and PCA-12/Packet 08 rather than rebuilding workbenches. MERA historical `05+09+22 → MERA-05` is the engineering-specific diagnostic/calibration/acceptance interpretation surface.

### Procedural generation

Remaining candidates:

- `MCS-10+11+12` over PCA recipes;
- `MNCS-02` domain recipe layer over PCA-02.

### Golden/conformance gates

Proof-only pre-golden tranches should merge into the final gate when no distinct implementation work remains. `GPR-15+16` remains a strong candidate. Final family golden proof itself remains required.

## Remaining family candidates

### GPR — next selected review

- `GPR-12+13`: replay/determinism/Event trace plus persistence/snapshot/recovery/version compatibility share one state/history seam.
- `GPR-15+16`: conformance/regression plus final golden proof may combine if no independent runtime remains after PDCP closure.
- `GPR-14`: consume Packet 07 rather than build a generic creator/debug framework.
- Reduced MSWI confirms GPR as the one reusable pursuit/race/chase/convoy/interception executor and reusable life/social/performance pattern executor where those patterns apply.
- Reduced MERA confirms GPR should own generic gameplay execution/composition while MERA remains an engineering-domain consumer.
- Check early GPR pattern-definition/execution tranches for overlap with MRCS rule-definition authority and Action/Event execution.

### MRCS

- `MRCS-18`: generic simulation engine absorbed by PCA-12; retain rule/content model adapters and interpretation only.
- `MRCS-19+20`: migration/import/batch edit + pack/version/review/provenance/publication.
- Check `MRCS-17 + slimmed MRCS-18` as one dependency/impact/balance diagnostics tranche.

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

- `01+02 → 01`;
- `03+04+23 → 03`;
- `05+09+22 → 05`;
- `06` retained with recovery/work-context handoff residuals;
- `07+08+20 → 07`;
- `10+11 → 10`;
- `12` retained;
- `13+14+15 → 13` over the completed PPIA-04 Vehicle/Mecha/Starship shared domain;
- `16` retained;
- historical `17+18` absorbed to LSS/MIB-12 with MERA residuals in `06/07/24`;
- historical `19+21` absorbed to DPL/APW/MIB-14/reduced MBES with MERA prerequisite/work-order residuals in `06/07/13/16/24`;
- `24` retained.

Receipt: `PDCP_MERA_REDUCTION_RECEIPT.json`.

## Reduction order

With MSLR, MSWI, MBES and MERA resolved, the preferred reverse-consumer order is:

1. **GPR** next;
2. **MRCS**;
3. **MSAS**;
4. **MNCS**;
5. **MCCS**;
6. **MCS**.

If a later upstream reduction exposes a safer shared-owner consolidation, an already-resolved downstream receipt may be amended only with an explicit capability-preserving reconciliation receipt.

## Guardrails

- MAS is excluded.
- Candidate folds do not alter counts until complete receipts merge.
- Generic infrastructure is implemented once; domain semantics stay with domain owners.
- PDCP does not mutate `operations/CURRENT.json` merely for design work.
- Preserve start/golden DAG milestone IDs where possible; sparse stable IDs are preferred.
- Accessibility, permissions/privacy, provenance, replay/recovery, migration and deterministic proof obligations must survive every fold.
