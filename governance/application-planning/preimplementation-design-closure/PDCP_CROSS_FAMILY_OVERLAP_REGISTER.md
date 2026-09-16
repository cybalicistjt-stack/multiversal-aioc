# PDCP Cross-Family Overlap & Folding Register

**Project:** PDCP — Preimplementation Design Closure Project  
**Status:** ACTIVE REDUCTION CONTROL SURFACE  
**Implementation authority:** none  
**Purpose:** prevent intra-family and inter-family tranche duplication while preserving capability and owner boundaries.

## Rule

Every PDCP family reduction pass must perform both:

1. an **intra-family overlap audit** — identify baseline tranches that implement the same state, operation, workflow or proof seam and combine them when a single bounded implementation tranche can credibly own the work; and
2. a **cross-family overlap audit** — identify generic infrastructure already owned by another family/shared platform and reduce the local family to domain-specific adapters, definitions, UX or proofs.

A family may not keep a standalone tranche merely because the baseline roadmap gave the concern its own number. A tranche survives only when it still contains material application/schema/UI/runtime/integration/migration/performance/test work after design closure and shared-owner absorption.

Likewise, two families may not each build a generic engine for the same concern. The shared owner implements the generic substrate; downstream families implement only their semantic adapters and domain-specific proof.

This register records overlap candidates. Except where a family reduction receipt is already merged, candidate rows do **not** change roadmap counts by themselves.

## Shared cross-family ownership patterns

| Shared concern | Generic owner / substrate | Families/tranches that must consume rather than duplicate |
|---|---|---|
| proposal → preview/dry-run → commit → explanation → compensation | canonical owner operations + PDCP Packet 07 | all ten PDCP families; local studios implement domain operations/lenses only |
| simulation, parameter sweeps, graph/SAT/SMT/optimization/Monte-Carlo/ABM analysis | PCA-12 + PDCP Packet 08 | MRCS-18, GPR conformance, MERA-22, MBES capacity/network diagnostics, MSLR-14, MSWI-17 |
| procedural DAG/recipe scheduling, cache, seed/provenance | PCA-02/PCA-03 | MCS-10..12, MNCS-02, MSLR-14, MSWI-14 and later generators |
| resource identity, derivative provenance and rights | ARI + PCA-01/PCA-15 | every import/export/generation/publishing workflow |
| generic gameplay execution, replay and delivery modes | GPR + Action/Event | MERA, MBES, MSLR, MSWI specialist runtimes |
| reusable semantic affordance/Effect composition | MRCS/GPR + PDCP Packet 04 | MERA, MBES, MSLR, MSWI target/domain adapters |
| map/cartographic projection and editing | MCS | MBES, MSLR, MSWI and other domains provide semantic projections/bindings only |
| audio production/playback/cue presentation | AAI/MSAS/PCA audio tooling | MSLR/MSWI/domain systems provide semantic cue bindings, not audio engines |
| multi-resolution aggregate↔individual semantics | Packet 06 + canonical domain owners | MNCS, MBES, MSWI and GPR integration layers |
| systemic consequence propagation | MSWI | upstream families emit typed events/deltas rather than directly mutating unrelated owner domains |

## Global repeated-tranche patterns

### A. Authority/workspace opening tranches

Repeated baseline examples: `MCS-01`, `MCCS-01`, `MNCS-01`, `MSAS-01`, `MRCS-01`, `MERA-01`, `MBES-01`, `MSLR-01`, `MSWI-01`.

PDCP has already closed most authority/ownership/product-semantics work. Future family passes must ask whether the remaining workspace/schema shell can be merged into the first substantive implementation tranche. A standalone `-01` survives only if material platform/schema/UI work remains.

### B. Import/export/version/review/provenance workflows

Strong overlap candidates:

- `MCS-19` + `MCS-20`;
- `MCCS-19` (while `MCCS-20` remains a distinct P3D handoff question);
- `MNCS-23`;
- `MSAS-18` + `MSAS-19` + `MSAS-20`;
- `MRCS-19` + `MRCS-20`;
- `MERA-23`.

These families must use ARI/PCA/shared review/version infrastructure rather than implement separate provenance, collaboration or publishing engines. Family-local work should be limited to domain serializers, validation, UI and migration adapters.

### C. Creator/debug/simulation workbenches

Strong overlap candidates:

- `GPR-14` plus the creator/GM portions of `GPR-12..16`;
- `MERA-03`, `MERA-22`, `MERA-23`;
- `MBES-01`, `MBES-07` and domain diagnostics;
- historical `MSLR-14` + `MSLR-17` — resolved by the MSLR family reduction;
- `MSWI-14` + `MSWI-17` shared tooling seams.

Packet 07 owns common execution-inspection semantics and PCA-12 owns reusable analysis. Local tranches must not rebuild generic debuggers, solver UIs or arbitrary GM mutation frameworks.

### D. Procedural generation families

Strong overlap candidates:

- `MCS-10`, `MCS-11`, `MCS-12` — likely one shared map/world-generation substrate plus domain generator packs rather than three independent engines;
- `MNCS-02` — domain recipe layer over PCA-02 rather than another scheduler/cache engine;
- historical `MSLR-14` — now explicitly an adapter over PCA-02/PCA-03/PCA-12;
- `MSWI-14` — seeded scenario/site composition over shared recipe infrastructure.

### E. Golden/conformance gates

Golden proof remains necessary, but a separate pre-golden conformance tranche should be merged into the final proof when it contains no distinct implementation work. Candidate examples:

- `GPR-15` + `GPR-16`;
- `MSWI-17` + `MSWI-18` only if diagnostics are fully implemented earlier and the remaining `MSWI-17` work is proof-only;
- family-specific final integration + golden proof combinations where the implementation can remain within the bounded tranche envelope.

Do not merge a final proof if doing so would remove independent runtime/integration implementation work or make the tranche exceed the execution envelope.

## Intra-family candidate clusters for later passes

### MCS

- `MCS-10` + `MCS-11` + `MCS-12`: one procedural generation substrate with terrain/environment/population/settlement proposal packs; PCA owns generic graph/generator infrastructure.
- `MCS-19` + `MCS-20`: structured interchange, versions, collaboration, review and publishing share one document/provenance workflow.
- Review `MCS-13` + `MCS-14` + `MCS-16` for a common built/interior/multi-level projection implementation core, while preserving distinct city versus dungeon authoring UX where needed.

### MCCS

- `MCCS-13` + `MCCS-14` + `MCCS-15`: output/derivative renderers share one renderer-neutral composition/export substrate and may be foldable.
- `MCCS-16` should be tested for absorption into the derivative-renderer tranche if style/profile implementation is mostly configuration.
- `MCCS-19` should consume common interchange/review/provenance infrastructure rather than remain a broad generic workflow tranche.

### MNCS

- `MNCS-15` + `MNCS-16` + `MNCS-17`: social-group, settlement/population and herd/ecosystem generation share aggregate/group recipe and individualization machinery; strong consolidation candidate.
- `MNCS-20` + `MNCS-21`: continuity/change-over-time and promotion/demotion/resolution management share lifecycle/resolution-transition state; strong consolidation candidate.
- `MNCS-23` should slim to domain batch/preset/import adapters over common review/provenance tooling.

### MSAS

- `MSAS-17`: generated music/SFX/voice should be absorbed into the relevant music/SFX/voice workflows because PCA provides generic generation orchestration; standalone tranche is a strong removal candidate.
- `MSAS-18` + `MSAS-19` + `MSAS-20`: versions/variants/review + interchange/bridges + rights/provenance/publication share one governed asset-delivery pipeline; strong consolidation candidate.
- `MSAS-15` live GM trigger UX must consume Packet-07 shared live-control semantics rather than build a parallel GM execution system.

### MRCS

- `MRCS-18`: generic simulation engine must be absorbed by PCA-12; MRCS retains rule/content model adapters, balance interpretation and playtest evidence UX only.
- `MRCS-19` + `MRCS-20`: migration/import/batch edit plus pack/version/review/provenance/publication share content-pipeline infrastructure; strong consolidation candidate.
- `MRCS-17` + slimmed `MRCS-18` should be checked for a combined dependency/impact/balance diagnostics tranche if bounded after PCA-12 absorption.

### GPR

- `GPR-12` + `GPR-13`: replay/determinism/Event trace and persistence/snapshot/recovery/version compatibility share the same state/history boundary; strong consolidation candidate.
- `GPR-15` + `GPR-16`: conformance/regression and golden cross-system proof may combine if no distinct runtime implementation remains in `GPR-15` after PDCP closure.
- `GPR-14` consumes Packet-07 creator/GM execution infrastructure and should not implement a generic studio framework.

### MERA

- `MERA-22` must slim to engineering-specific model/test/acceptance adapters over PCA-12 and Packet-07 tooling.
- `MERA-23` must slim to engineering blueprint/preset/domain interchange adapters over ARI/PCA common provenance/review infrastructure.
- Review `MERA-10` + `MERA-11` for a common governed network/dependency kernel while preserving failure-propagation versus interface-runtime distinctions.
- `MERA-12..16` are not presumed mergeable: their target-domain integration may remain substantial despite shared engineering core.

### MBES

- `MBES-08` + `MBES-09` + `MBES-10`: utility, automation/control and logistics networks share graph/interface/capacity/runtime infrastructure; strong consolidation candidate after MERA/GPR owner absorption.
- `MBES-12` + `MBES-13`: earthworks and hydrology/civil-water manipulation share terrain/civil transformation infrastructure; consolidation candidate.
- `MBES-14` + `MBES-15` + `MBES-16`: environmental externalities, reactive-world hooks and habitability/resilience share Environment/World condition-response infrastructure; evaluate as one or two bounded tranches.
- `MBES-20` + `MBES-21` + `MBES-23`: settlement growth, transport/regional infrastructure and multi-settlement development share district/regional simulation and may reduce materially after Packet 06/PCA-12 absorption.

### MSLR

Resolved by `PDCP_MSLR_REDUCTION_RECEIPT.json`:

- `01+02 → 01`;
- `03+06 → 03`;
- `04+05+11 → 04`;
- `07+12 → 07`;
- `08+09+10 → 08`;
- `13+15 → 13`;
- `14+17 → 14`;
- `16` retained;
- `18` retained.

Result: **18 → 9**.

### MSWI

- `MSWI-04` + `MSWI-05`: ecology succession/carrying capacity/population bands and food-web/migration/invasion/extinction are one ecology consequence runtime; strong consolidation candidate.
- `MSWI-14` + `MSWI-15`: procedural site/scenario remix and environment-state map/scene variants share generated/proposed/persistent variant machinery; consolidation candidate with MCS presentation remaining external.
- `MSWI-17` should consume PCA-12/Packet-08 and may merge into `MSWI-18` if only final diagnostic proof remains after other tranches implement integration instrumentation.
- `MSWI-02` + `MSWI-03` should be checked carefully: transformation state and propagation/reversibility are closely coupled, but may still merit two tranches if persisted schema/migration and routing implementation each remain substantial.

## Reduction-order rule

Because cross-family folds can change downstream obligations, subsequent family passes should prefer the following order:

1. **MSWI** next, because it directly consumes MSLR and has obvious Packet-06/08 overlap;
2. **MBES**;
3. **MERA**;
4. **GPR**;
5. **MRCS**;
6. **MSAS**;
7. **MNCS**;
8. **MCCS**;
9. **MCS**.

This reverse-consumer walk is deliberate: reduce the downstream integration families first, then use their final owner boundaries to avoid retaining unnecessary upstream handoff work. If a later upstream pass reveals a safer shared-owner consolidation, the already-closed downstream receipt may be amended only with an explicit capability-preserving reconciliation receipt.

## Guardrails

- MAS is excluded.
- A candidate fold is not an approved reduction until its family receipt resolves every baseline row.
- Shared infrastructure may be implemented once and consumed many times, but domain semantics stay with the domain owner.
- No family reduction changes `operations/CURRENT.json` unless OPS3 independently requires it.
- Preserve existing start/golden DAG milestone IDs when possible; stable sparse tranche IDs are preferred over gratuitous renumbering.
- Every removal/merge must preserve accessibility, permissions/privacy, provenance, replay/recovery, migration and automated proof obligations.
