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
| generic generation orchestration | PCA-02/PCA-03/PCA-09 as applicable | specialist families supply domain recipes/briefs/review/acceptance adapters |
| generic localization production | PCA-13 | specialist families bind domain localization context |
| map/cartographic projection/editing | MCS | other families bind map projections only |
| character/creature appearance presentation | MCCS + CAPP/PPIA/PAPT/PCA | NPC/runtime families request or bind presentation only |
| NPC/creature entity identity/placement/live instance | PPIA-02 + Character/NPC/Creature | MNCS supplies construction/progressive-resolution UX only |
| profession/household/economy/schedule/project/life truth | DPL/Profession + Economy/Organization + Project/Time | MNCS binds projections only |
| relationship/reputation mutation | MIB-09 | MNCS composes/visualizes scoped reputation and party-association behavior |
| multi-resolution aggregate↔individual | Packet 06 + domain owners | specialist creator lifecycle adapters only |
| systemic consequence propagation | reduced MSWI | upstream systems emit typed Events/deltas |
| engineering orchestration | reduced MERA + Asset/MIB owners | consumers bind engineering adapters only |
| built environment/facilities | reduced MBES + underlying owners | consumers reference facility context |

## Repeated folding rules

- opening workspace/authority and registry/schema tranches merge when they form one implementation shell;
- generic creator/debug, simulation, generation, localization and lifecycle infrastructure are not rebuilt per family;
- proof-only pre-golden tranches fold into final golden proof when no independent runtime remains;
- sparse historical IDs are preferred over renumbering when DAG milestones can survive;
- family-specific UI may survive even when its canonical data/runtime owner is elsewhere, but only as a bounded adapter/projection seam.

## Next selected review — MCCS

Strong candidates to test:

- `MCCS-13+14+15`: portrait/bust/card, token/paper-doll/isometric and sprite/stance/animation-sheet outputs may share one derivative-rendering/export kernel while preserving format-specific adapters;
- `MCCS-16`: inspect whether style packs/templates/renderer profiles are configuration inside the shared output/renderer substrate rather than a standalone runtime;
- `MCCS-17`: NPC/crowd/herd/creature visual-variant generation must not duplicate MNCS identity/population generation or PCA generation orchestration;
- `MCCS-18`: inspect whether multi-form/transformation/lifecycle appearance management is one appearance-state adapter over Character/Species/Form owners rather than a separate state engine;
- `MCCS-19`: generic interchange/version/review/provenance stays ARI/PCA; retain only character/creature presentation mapping and round-trip validation;
- preserve `MCCS-02` because it is an MNCS rotation milestone unless an equivalent DAG update is demonstrably safer;
- preserve `MCCS-21` golden gate unless an equivalent gate update is required.

## Later family candidates

### MCS
- `10+11+12`: shared world/map-generation substrate over PCA recipes;
- `19+20`: interchange/version/review/publishing;
- inspect `13+14+16` for shared built/interior/multi-level projection infrastructure without erasing materially different city/dungeon UX;
- strip generic generation, analysis, provenance and creator-debug infrastructure to PCA/Packet-07/08/ARI owners.

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

### MNCS — 24 → 13
`01+02+03→01`; `04`; `05`; `06+07→06`; `08`; historical `09` absorbed to DPL/Profession + Economy/Organization + Project/Time with MNCS bindings; `10+11→10`; `12+13→12`; `14`; `15+16+17→15`; `18+19→18`; `20+21→20`; `22`; historical `23` absorbed to ARI/PCA/Packet-07 generic infrastructure plus MNCS adapters; `24`.

MNCS-specific result: PPIA-02/Character/NPC/Creature keep entity truth; MIB-09 keeps reputation mutation; DPL/Economy/Project keep life truth; Packet 06 keeps multi-resolution semantics; Packet 03 keeps generic autonomous orchestration; reduced MRCS/GPR keep reusable definitions/runtime execution; MNCS keeps progressive construction, group/population creator UX, privacy-safe roleplay prep and governed handoff.

## Reduction order

Resolved: MSLR, MSWI, MBES, MERA, GPR, MRCS, MSAS, MNCS. Remaining preferred order:

1. **MCCS** next;
2. **MCS** final family review.

Already-resolved receipts may be amended only through explicit capability-preserving reconciliation if a later upstream reduction exposes a safer owner fold.

## Guardrails

MAS is excluded. Candidate folds do not alter counts before complete receipts merge. Accessibility, permissions/privacy, provenance, replay/recovery, migration and deterministic proof survive every fold. PDCP does not mutate `operations/CURRENT.json` merely for planning work.
