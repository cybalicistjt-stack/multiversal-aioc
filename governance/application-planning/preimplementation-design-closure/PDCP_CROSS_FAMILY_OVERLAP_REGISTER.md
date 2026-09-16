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
| reusable rule/content definition authoring | reduced MRCS + owner-domain contracts | specialist studios retain domain creator UX |
| semantic affordances/effect composition | reduced MRCS + reduced GPR + Packet 04 | target/domain adapters only |
| audio semantic/runtime/interoperability | AAI | MSAS supplies integrated production/direction UX only |
| adaptive-audio authoring primitives | PCA-07 + AAI | MSAS composes creator workflows and domain binding |
| voice/speech/SFX production primitives | PCA-08 | MSAS owns audio-domain workflow/binding only |
| generic generation orchestration | PCA-09 | audio families supply briefs/review/acceptance adapters |
| generic localization production | PCA-13 | MSAS/MNCS/etc. bind domain localization context |
| map/cartographic projection/editing | MCS | other families bind map projections only |
| multi-resolution aggregate↔individual | Packet 06 + domain owners | lifecycle adapters only |
| systemic consequence propagation | reduced MSWI | upstream systems emit typed Events/deltas |
| engineering orchestration | reduced MERA + Asset/MIB owners | consumers bind engineering adapters only |
| built environment/facilities | reduced MBES + underlying owners | consumers reference facility context |
| work capability/project/time | DPL/Profession + APW/D26 | prerequisite bindings only |

## Repeated folding rules

- opening workspace/authority and registry/schema tranches merge when they form one implementation shell;
- generic creator/debug, simulation, generation, localization and lifecycle infrastructure are not rebuilt per family;
- proof-only pre-golden tranches fold into final golden proof when no independent runtime remains;
- sparse historical IDs are preferred over renumbering when DAG milestones can survive.

## Next selected review — MNCS

Strong candidates to test:

- `MNCS-15+16+17`: population/group/herd/ecosystem generation over shared aggregate/recipe machinery;
- `MNCS-20+21`: continuity/change-over-time plus resolution promotion/demotion over one lifecycle state machine;
- `MNCS-23`: slim to NPC/creature-specific batch/preset/import adapters, with generic lifecycle/provenance/version/review/import-export remaining ARI/PCA;
- `MNCS-02`: consume PCA-02/PCA-03 procedural recipe/generation substrate rather than create a parallel generic generator;
- Packet 03 owns generic autonomous-process orchestration; MNCS should keep NPC/creature policy bindings rather than another generic AI planner;
- Packet 06 owns generic aggregate↔individual resolution semantics; MNCS retains domain identity/state adapters;
- reduced MRCS owns reusable rule/content definition authoring; MNCS retains NPC/creature authoring and runtime-facing identity/behavior UX.

## Later family candidates

### MCCS
- `13+14+15`: output/derivative renderer substrate;
- inspect `16` for absorption when style/profile behavior is configuration;
- `19`: consume generic interchange/review/provenance infrastructure.

### MCS
- `10+11+12`: shared world/map-generation substrate over PCA recipes;
- `19+20`: interchange/version/review/publishing;
- inspect `13+14+16` for shared built/interior/multi-level projection infrastructure without erasing materially different city/dungeon UX.

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

### MSAS — 21 → 11
`01+02→01`; `03`; `04+16→04`; `05+06→05`; `07+08→07`; `09+10+11→09`; `12+13→12`; `14`; `15`; historical `17` absorbed to PCA-09/PCA-08 plus domain adapters; `18+19+20→18`; `21`.

MSAS-specific result: AAI keeps semantic/runtime authority; PCA-07/08/09/13 keep generic audio authoring/generation/localization primitives; Packet 07 keeps generic live-control semantics; ARI/PCA keep generic rights/provenance/version/review; MSAS keeps the integrated audio-domain production UX.

## Reduction order

Resolved: MSLR, MSWI, MBES, MERA, GPR, MRCS, MSAS. Remaining preferred order:

1. **MNCS** next;
2. **MCCS**;
3. **MCS**.

Already-resolved receipts may be amended only through explicit capability-preserving reconciliation if a later upstream reduction exposes a safer owner fold.

## Guardrails

MAS is excluded. Candidate folds do not alter counts before complete receipts merge. Accessibility, permissions/privacy, provenance, replay/recovery, migration and deterministic proof survive every fold. PDCP does not mutate `operations/CURRENT.json` merely for planning work.
