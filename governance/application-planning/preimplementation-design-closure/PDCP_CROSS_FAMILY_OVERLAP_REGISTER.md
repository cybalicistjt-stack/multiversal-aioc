# PDCP Cross-Family Overlap & Folding Register

**Project:** PDCP — Preimplementation Design Closure Project  
**Status:** COMPLETED_RECONCILED  
**Implementation authority:** none

## Rule

Every family reduction performed both an intra-family overlap audit and a cross-family/shared-owner audit. A historical tranche survives only when a distinct bounded implementation/proof seam remains after design closure and shared-owner absorption.

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
| audio semantic/runtime/interoperability | AAI | reduced MSAS supplies integrated production/direction UX only |
| adaptive-audio/voice/SFX production primitives | PCA-07/PCA-08 + AAI | MSAS composes creator workflows and domain binding |
| generic generation orchestration | PCA-02/PCA-03/PCA-09 as applicable | specialist families supply domain recipes/briefs/review/acceptance adapters |
| generic localization production | PCA-13 | specialist families bind domain localization context |
| map/cartographic projection/editing | reduced MCS + MAI | other families bind map projections only |
| character/creature appearance presentation | reduced MCCS + CAPP/PPIA/PAPT/PCA | NPC/runtime families request or bind presentation only |
| NPC/creature entity identity/placement/live instance | PPIA-02 + Character/NPC/Creature | reduced MNCS supplies construction/progressive-resolution UX only |
| profession/household/economy/schedule/project/life truth | DPL/Profession + Economy/Organization + Project/Time | MNCS binds projections only |
| relationship/reputation mutation | MIB-09 | MNCS composes/visualizes scoped reputation and party-association behavior |
| multi-resolution aggregate↔individual | Packet 06 + domain owners | specialist creator lifecycle adapters only |
| systemic consequence propagation | reduced MSWI | upstream systems emit typed Events/deltas |
| engineering orchestration | reduced MERA + Asset/MIB owners | consumers bind engineering adapters only |
| built environment/facilities | reduced MBES + underlying owners | consumers reference facility context |
| runtime spatial law/topology | reduced MSLR + World/Scene/SSA owners | MCS/MBES project or author inputs; they do not duplicate runtime law |

## Repeated folding rules

- opening workspace/authority and registry/schema tranches merge when they form one implementation shell;
- generic creator/debug, simulation, generation, localization and lifecycle infrastructure are not rebuilt per family;
- proof-only pre-golden tranches fold into final golden proof when no independent runtime remains;
- sparse historical IDs are preferred over renumbering when DAG milestones can survive;
- family-specific UI may survive even when its canonical data/runtime owner is elsewhere, but only as a bounded adapter/projection seam.

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

### MCCS — 21 → 11
`01+02→01`; `03+04+08→03`; `05`; `06+07→06`; `09+10→09`; `11+12→11`; `13+14+15→13`; `16`; historical `17` absorbed to MNCS/PCA with visual-variant residual in `16`; `18`; `19+20→19`; `21`.

### MCS — 21 → 12
`01+02→01`; `03+04→03`; `05+06→05`; `07+17→07`; `08+09→08`; `10+11+12→10`; `13`; `14+16→14`; `15`; `18`; `19+20→19`; `21`.

MCS-specific result: MAI keeps map schemas/projection foundations; PCA keeps generic generator/style/analysis substrate; ISE/Scene keep live canvas/runtime state; SSA/World/MSLR keep spatial truth; MBES/Settlement keep built-environment truth; ARI/PCA/Packet-07 keep generic lifecycle/provenance/review; MCS keeps map-document/editor UX, cartographic generator packs, geographic/urban/interior/tactical authoring, semantic binding, map interchange/atlas adapters and golden proof.

## Whole-project overlap conclusion

All ten in-scope family receipts are complete and reconciled. No surviving tranche is retained solely because the historical roadmap gave it an independent ID. Generic infrastructure is assigned to one practical owner, while specialist families retain bounded domain adapters/UX/proof. No additional cross-family fold was identified that could be made without creating an oversized survivor, weakening an owner boundary, or moving implementation into a family that does not own the capability.

The final effective family count is **105** from a historical **208**, removing **103** standalone future tranches. MAS remains excluded and unchanged.

Final live-control reconciliation additionally found that retired `MERA-04` still gated MBES even though its capability had been merged into surviving `MERA-03`. The live DAG and parallel execution map now use `MERA-03`. This was an equivalent-gate repair, not a new capability or a roadmap-count change.

## Closeout

PDCP has no remaining family review or design-packet review. Final aggregate totals and live retired-ID validation are owned by `tests/control_plane/test_pdcp_final_closeout.py` and the closeout records dated 2026-09-16.

## Guardrails

Accessibility, permissions/privacy, provenance, replay/recovery, migration and deterministic proof survive every fold. PDCP did not mutate `operations/CURRENT.json` merely for planning work and completion grants no product implementation authority.
