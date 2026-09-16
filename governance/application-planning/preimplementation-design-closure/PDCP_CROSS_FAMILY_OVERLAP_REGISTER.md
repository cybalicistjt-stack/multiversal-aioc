# PDCP Cross-Family Overlap & Folding Register

**Project:** PDCP — Preimplementation Design Closure Project  
**Status:** ACTIVE REDUCTION CONTROL SURFACE  
**Implementation authority:** none  
**Purpose:** prevent intra-family and inter-family tranche duplication while preserving capability and owner boundaries.

## Rule

Every PDCP family reduction pass must perform both:

1. an **intra-family overlap audit** — identify baseline tranches that implement the same state, operation, workflow or proof seam and combine them when one bounded implementation tranche can credibly own the remaining work; and
2. a **cross-family overlap audit** — identify generic/canonical infrastructure already owned elsewhere and reduce the local family to domain-specific schemas, adapters, UX and proof.

A family may not keep a standalone tranche merely because the baseline roadmap gave the concern its own number. Two families may not each build a generic engine for the same concern.

Candidate rows do not change roadmap counts until a complete family receipt merges.

## Shared cross-family ownership patterns

| Shared concern | Generic owner / substrate | Specialist consumers |
|---|---|---|
| proposal → preview/dry-run → commit → explanation → compensation | canonical owner operations + PDCP Packet 07 | all PDCP families; local studios implement domain operations/lenses only |
| simulation, parameter sweeps, graph/SAT/SMT/optimization/Monte-Carlo/ABM analysis | PCA-12 + PDCP Packet 08 | MRCS balance adapters, GPR conformance, MERA engineering models, reduced MBES capacity/network models, MSLR-14, reduced MSWI-18 |
| procedural DAG/recipe scheduling, cache, seed/provenance | PCA-02/PCA-03 | MCS generators, MNCS recipes, MSLR-14, reduced MSWI-14 and later generators |
| resource identity, derivative provenance and rights | ARI + PCA-01/PCA-15 | every import/export/generation/publishing workflow |
| generic gameplay execution, replay and delivery modes | GPR + Action/Event | MERA, reduced MBES, MSLR, MSWI specialist adapters |
| reusable semantic affordance/Effect composition | MRCS/GPR + PDCP Packet 04 | MERA, MBES, MSLR, MSWI target/domain adapters |
| map/cartographic projection and editing | MCS | reduced MBES, MSLR, MSWI and other domains provide semantic bindings only |
| audio production/playback/cue presentation | AAI/MSAS/PCA audio tooling | domain systems provide semantic cue bindings, not audio engines |
| multi-resolution aggregate↔individual semantics | Packet 06 + canonical domain owners | MNCS, reduced MBES, MSWI and GPR integration layers |
| systemic consequence propagation | reduced MSWI | upstream families emit typed Events/deltas rather than directly mutating unrelated owner domains |
| engineering topology/interfaces/dependency/failure/repair | MERA + MIB-12/MIB-14 owners | reduced MBES building/infrastructure network and durability adapters |
| production/cultivation truth | ICF + MIB-12 + Inventory/Asset + Economy | reduced MBES facility capability/network/capacity bindings only |
| residents/households/jobs/staffing | Character/MNCS + ODL + DPL + Project/Time | reduced MBES facility-use prerequisites and settlement capacity only |
| property/funding/markets/contracts/trade | MIB-13/Economy + ODL + Project/Time | reduced MBES construction funding/procurement and settlement references only |

## Global repeated-tranche patterns

### A. Authority/workspace opening tranches

Repeated baseline examples include `MCS-01`, `MCCS-01`, `MNCS-01`, `MSAS-01`, `MRCS-01`, `MERA-01`, historical `MBES-01`, `MSLR-01`, `MSWI-01`.

PDCP has closed most authority/product semantics. A standalone `-01` survives only where material schema/workspace/runtime shell work remains. Resolved examples:

- MSLR `01+02 → 01`;
- MSWI `01+02 → 01`;
- MBES `01+02 → 01`, with historical construction-economy runtime `22` absorbed to existing owners.

### B. Import/export/version/review/provenance workflows

Strong remaining candidates:

- `MCS-19 + MCS-20`;
- `MCCS-19` consuming shared provenance/review infrastructure;
- `MNCS-23` slimmed to domain adapters;
- `MSAS-18 + 19 + 20`;
- `MRCS-19 + 20`;
- `MERA-23` slimmed to engineering blueprint/preset adapters.

ARI/PCA/shared review/version infrastructure owns generic workflow. Local families retain domain serializers, validation, UX and migration only.

### C. Creator/debug/simulation workbenches

Remaining candidates:

- `GPR-14` plus creator/GM portions of `GPR-12..16`;
- `MERA-03`, `MERA-22`, `MERA-23`;
- MRCS dependency/balance analysis;
- MCS/MCCS/MNCS creator diagnostics.

Resolved examples:

- MSLR historical `14+17 → 14`, consuming PCA-12/Packet-07/08;
- MSWI historical `17+18 → 18`, consuming PCA-12/Packet-08;
- MBES diagnostics are distributed into surviving domain tranches and consume PCA-12/Packet-08 rather than creating a standalone workbench.

### D. Procedural generation

Remaining candidates:

- `MCS-10+11+12` — one map/world generator adapter family over PCA recipes;
- `MNCS-02` — domain recipe layer over PCA-02;
- later family-specific generators must not rebuild scheduling/cache/seed/provenance.

Resolved examples:

- MSLR-14 is a PCA recipe/analysis adapter;
- reduced MSWI-14 is a systemic variant/promotion adapter.

### E. Golden/conformance gates

Golden proof remains necessary, but proof-only pre-golden tranches should merge into the final gate when no distinct runtime work remains.

- `GPR-15+16` remains a candidate;
- MSWI historical `17+18` resolved into `MSWI-18`;
- MBES keeps `MBES-24` distinct because final cross-scale/Oara/provider-off/accessibility/MSLR-handoff proof is independent closeout work.

## Intra-family candidates for remaining passes

### MCS

- `MCS-10+11+12`: shared map/world-generation substrate over PCA with generator packs.
- `MCS-19+20`: interchange/version/review/publishing workflow.
- Review `MCS-13+14+16` for common built/interior/multi-level projection core while preserving distinct city/dungeon UX where needed.

### MCCS

- `MCCS-13+14+15`: output/derivative renderer substrate.
- Test `MCCS-16` for absorption if style/profile implementation is mostly configuration.
- `MCCS-19` must consume common interchange/review/provenance infrastructure.

### MNCS

- `MNCS-15+16+17`: group/settlement-population/herd-ecosystem generation share aggregate recipe/individualization machinery.
- `MNCS-20+21`: continuity/change-over-time and resolution promotion/demotion share lifecycle state.
- `MNCS-23` should slim to domain batch/preset/import adapters.

### MSAS

- `MSAS-17` generated music/SFX/voice should be absorbed into the corresponding domain workflows because PCA supplies generic generation orchestration.
- `MSAS-18+19+20`: version/review/interchange/rights/publication delivery pipeline.
- `MSAS-15` live-GM trigger UX consumes Packet-07 semantics.

### MRCS

- `MRCS-18` generic simulation engine is absorbed by PCA-12; MRCS retains rule/content model adapters and interpretation.
- `MRCS-19+20`: migration/import/batch edit + pack/version/review/provenance/publication.
- Check `MRCS-17 + slimmed 18` as one dependency/impact/balance diagnostics tranche.

### GPR

- `GPR-12+13`: replay/determinism/Event trace + persistence/snapshot/recovery/version compatibility.
- `GPR-15+16`: conformance/regression + golden cross-system proof if bounded after PDCP closure.
- `GPR-14` consumes Packet-07 instead of implementing a generic studio framework.
- Reduced MSWI confirms GPR as reusable pursuit/race/chase/convoy/interception owner and reusable life/social/performance pattern executor where applicable.

### MERA — next selected review

- `MERA-03` must consume Packet-07 preview/diff/commit infrastructure rather than build a generic proposal framework.
- `MERA-05` and parts of `MERA-22` share inspection/diagnostic/acceptance evidence; inspect for one bounded engineering verification seam after PCA-12 absorption.
- `MERA-10+11`: dependency/failure/redundancy plus power/fuel/heat/fluid/data/control interfaces share a governed system/network kernel; strong consolidation candidate.
- `MERA-17+18`: salvageability/donor-part state plus cannibalization/remanufacture/refurbishment/fabrication share recovery/material-lineage flow and must be checked against LSS/MIB-12 ownership.
- `MERA-19+21`: tools/workstations/crew/projects/time plus garage/hangar/workshop/spares/refit queues share engineering-work execution context and may consolidate.
- `MERA-22` must slim to engineering-specific model/test/acceptance adapters over PCA-12/Packet-08 and Packet-07 tooling.
- `MERA-23` must slim to engineering blueprint/preset/domain interchange adapters over ARI/PCA infrastructure.
- `MERA-12..16` are not presumed mergeable merely because they share engineering core; target-domain integration may remain substantial.
- Reduced MBES now depends on MERA only for the generic engineering/network/failure/repair substrate, which should prevent MERA from retaining MBES-specific facility/infrastructure work.

## Resolved families

### MSLR — 18 → 9

- `01+02 → 01`;
- `03+06 → 03`;
- `04+05+11 → 04`;
- `07+12 → 07`;
- `08+09+10 → 08`;
- `13+15 → 13`;
- `14+17 → 14`;
- `16` retained;
- `18` retained.

Receipt: `PDCP_MSLR_REDUCTION_RECEIPT.json`.

### MSWI — 18 → 7

- `01+02 → 01`;
- `03` retained;
- `04+05 → 04`;
- `06` retained;
- `07+08 → 07`;
- historical `09..13` absorbed to their canonical/runtime owners with residual consequence adapters in surviving MSWI tranches;
- `14+15+16 → 14`;
- `17+18 → 18`.

Receipt: `PDCP_MSWI_REDUCTION_RECEIPT.json`.

### MBES — 24 → 9

- `01+02 → 01`;
- `03+04 → 03`;
- `05+06+07 → 05`;
- `08+09+10 → 08`;
- historical `11` absorbed to ICF/MIB-12/Inventory/Economy with MBES residuals in `05/08/20/24`;
- `12+13 → 12`;
- `14+15+16 → 14`;
- historical `17` absorbed to Character/MNCS/ODL/DPL/Project with MBES residuals in `05/20/24`;
- `18+19 → 18`;
- `20+21+23 → 20`;
- historical `22` absorbed to MIB-13/Economy/ODL/Project with MBES residuals in `01/20/24`;
- `24` retained.

Receipt: `PDCP_MBES_REDUCTION_RECEIPT.json`.

## Reduction order

With MSLR, MSWI and MBES resolved, the remaining preferred reverse-consumer order is:

1. **MERA** next;
2. **GPR**;
3. **MRCS**;
4. **MSAS**;
5. **MNCS**;
6. **MCCS**;
7. **MCS**.

This reverse-consumer walk is deliberate. If a later upstream pass exposes a safer shared-owner consolidation, an already-resolved downstream receipt may be amended only with an explicit capability-preserving reconciliation receipt.

## Guardrails

- MAS is excluded.
- A candidate fold is not an approved reduction until its family receipt resolves every baseline row.
- Shared infrastructure may be implemented once and consumed many times, but domain semantics stay with the domain owner.
- No family reduction changes `operations/CURRENT.json` merely for PDCP work.
- Preserve existing start/golden DAG milestone IDs where possible; stable sparse IDs are preferred over gratuitous renumbering.
- Every removal/merge must preserve accessibility, permissions/privacy, provenance, replay/recovery, migration and automated proof obligations.
