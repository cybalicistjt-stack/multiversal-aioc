# MSWI — Multiversal Systemic Worldplay Integration

**Program ID:** MSWI  
**Status:** ACTIVE — MSWI-03 SELECTED_NOT_STARTED; PDCP-REDUCED  
**Owner:** John Brandon Turner  
**Approved:** 2026-09-15  
**PDCP reduction:** 2026-09-16 — baseline 18 tranches → 7 surviving implementation/proof tranches  
**Activation:** after `MSLR-18` under `ROADMAP_DEPENDENCY_GRAPH.json`  
**Successor:** `SMB-08`  
**Implementation authority:** `false`

## Purpose

MSWI is the cross-domain consequence orchestration and persistent-world-response layer.

Its central product requirement is:

> Major player effort can create attributable, inspectable and persistent consequences across the world, and the application can explain which governed systems responded and why.

MSWI consumes existing owner-domain state and operations rather than duplicating them. DPL owns profession/life foundations, MNCS owns NPC/creature generation and ecology authoring, GPR owns reusable gameplay execution, MERA owns engineering/refit, MBES owns built-environment/settlement, MSLR owns non-standard spatial-law runtime, Project/Time owns long-running work, Religion/Culture/Organization owners own doctrine/social state, and MCS/MAS/MSAS/MCCS retain their specialized presentation/authoring domains.

MSWI exists where consequences cross those boundaries.

## PDCP design-closure authority

The implementation-ready semantic contract is:

`governance/application-planning/preimplementation-design-closure/PDCP_MSWI_FAMILY_DESIGN_CLOSURE.md`

The complete 18-row before/after coverage receipt is:

`governance/application-planning/preimplementation-design-closure/PDCP_MSWI_REDUCTION_RECEIPT.json`

Historical baseline tranche IDs remain provenance. Only the strict order in `MSWI_PROGRAM_BACKLOG.json` is future executable work.

## Roadmap role

MSWI remains between MSLR and system maturation:

`... → MBES → MSLR → MSWI → SMB-08`

`MSWI-01` remains the family start/rotation gate and `MSWI-18` remains the golden proof and SMB-08 handoff gate. Sparse IDs preserve those stable roadmap references.

## Owner-boundary consolidation

PDCP removed several baseline MSWI standalone runtimes because their actual authority already belongs elsewhere:

- doctrine/ideology/social choice → Religion/Culture/Organization owners + Packet 01 + MRCS/GPR;
- profession/enterprise/downtime loops → DPL + Project/Time + GPR;
- pursuit/race/chase/convoy/interception → GPR + Movement/Vehicle/Mount/World/Scene, with MSLR where anomalous space applies;
- performance/rhythm/diegetic timing → DPL + MSAS/AAI + GPR + Accessibility;
- grand/world Project framework → APW/D26 Project/Time + GPR + contributing owner domains;
- procedural DAG/seed/cache infrastructure → PCA-02/PCA-03;
- generic simulation/formal-analysis/diagnostic substrate → PCA-12 + PDCP Packet 08;
- generic preview/commit/explanation/intervention semantics → canonical owner operations + PDCP Packet 07;
- generic resource/rights provenance → ARI/PCA.

MSWI retains only consequence adapters, integration projections and family-specific proof for those concerns.

## Surviving tranches

### MSWI-01 — Systemic Transformation State & Integration Core

Implements the integration registry and reusable transformation profile/projection schemas over existing owner state.

Repository-bound scope:

- `SystemicTransformationProfileDefinition` and related persisted schemas;
- read-only transformation projections referencing exact owner versions;
- thresholds/milestone bindings and attribution;
- integration registry bindings;
- validation, stale-state handling, migration/version compatibility;
- inspectable transformation UI/API.

This tranche absorbs historical `MSWI-01` and `MSWI-02`.

### MSWI-03 — Cross-System Consequence Routing, Recovery & Domain Adapter Runtime

Implements the family’s central fan-out runtime.

Repository-bound scope:

- consequence route definitions/registry;
- dry-run `SystemicConsequenceEnvelope` construction;
- target-owner validation/commit adapters;
- `SystemicPropagationReceipt` persistence;
- cycle, deduplication, route-depth and conflict controls;
- inverse/compensation/restoration/irreversible classification;
- delayed consequence integration with Project/Time/Event owners;
- residual source adapters for accepted doctrine/social, profession/life, pursuit and grand-Project results.

MSWI never grants target-domain authority merely because a route applies.

### MSWI-04 — Ecology Succession, Food-Web, Migration & Population-Band Runtime

Implements campaign-time ecological response from accepted MNCS/World/Environment definitions using Packet-06 multi-resolution semantics.

Repository-bound scope:

- habitat suitability and authored carrying-capacity references;
- exact/range/band/distribution/unknown population semantics;
- succession stages and environment dependencies;
- food-web/dependency links;
- migration/territory pressure;
- introduced/invasive-species hooks;
- harvest/overhunting/resource pressure;
- extinction/extirpation/recovery/restocking/conservation transitions;
- uncertainty-safe projections and receipts.

This tranche absorbs historical `MSWI-04` and `MSWI-05`. It invents no universal ecological equation or unnamed individual history.

### MSWI-06 — Composite Entity Role Binding Runtime

Implements one stable identity participating in multiple governed roles.

Repository-bound scope:

- multi-owner role-binding schema;
- role compatibility and interface checks;
- ownership/control/custody separation;
- role-local versus shared state references;
- role activation/removal/transition;
- multi-role projections and tests.

Creature, mount, vehicle, base, NPC, location/world-host and other owner domains retain their own state authority.

### MSWI-07 — Biological Components, Harvest, Embodied Modification & Lineage Integration

Combines the historical anatomy/harvest and embodied-modification seams because both require the same component/body/provenance integration kernel.

Repository-bound scope:

- source-authored anatomy/component references;
- component condition/damage/availability projection;
- harvest method/quality/conservation-safe output bindings;
- biological material and donor/source lineage;
- downstream crafting/cooking/alchemy/medicine/research/economy adapters;
- graft/implant/symbiote/prosthetic body-location and compatibility bindings;
- grants/removals/retained-state/reversal;
- explicit-rule-only identity/memory/psychological/social consequences.

Absent organs, yields, compatibility rules or donor effects remain unresolved.

This tranche absorbs historical `MSWI-07` and `MSWI-08` while reusing DPL-13 and Character/Species/Form owner foundations.

### MSWI-14 — Systemic Site/Scene Variant, Template & Promotion Integration

Combines procedural systemic candidate assembly, persistent visible campaign variants and transformation Campaign templates.

Repository-bound scope:

- MSWI adapters over PCA-02/PCA-03 recipes;
- stable canonical location/site binding;
- current/historical/alternate variant selection from accepted owner state;
- MCS/MAS/MSAS/MCCS/ARI presentation handoffs;
- ephemeral/proposed/persistent distinction;
- GM/owner promotion receipt;
- transformation Campaign template/profile binding and versioning;
- deterministic/provider-off tests.

Generated content does not become Campaign truth merely because generation succeeded.

This tranche absorbs historical `MSWI-14`, `MSWI-15` and `MSWI-16`.

### MSWI-18 — Systemic Coverage Diagnostics, Golden Proof & SMB-08 Handoff

Combines the MSWI-specific diagnostic adapter with the final family proof.

Repository-bound scope:

- interpretation of PCA-12/Packet-08 graph/run evidence;
- fan-out, loop, dead-route, duplicated-route and missing-integration reporting;
- permission-safe diagnostic projections and accessible text/tabular alternatives;
- automated family golden battery;
- exact-head/provider-off validation;
- SMB-08 capability handoff.

Diagnostics describe declared connectivity. They do not invent mechanics to improve an interaction-density score.

This tranche absorbs historical `MSWI-17` and `MSWI-18` and remains the roadmap golden gate.

## Absorbed historical tranches

The following baseline tranches no longer survive as standalone MSWI implementation units:

- `MSWI-02` → `MSWI-01`;
- `MSWI-05` → `MSWI-04`;
- `MSWI-08` → `MSWI-07`;
- `MSWI-09` → Religion/Culture/Organization + Packet 01 + MRCS/GPR; MSWI residual in `MSWI-03`/`18`;
- `MSWI-10` → DPL + Project/Time + GPR; MSWI residual in `MSWI-03`/`18`;
- `MSWI-11` → GPR + movement/vehicle/world/scene owners; MSWI residual in `MSWI-03`/`18`;
- `MSWI-12` → DPL + MSAS/AAI + GPR + Accessibility; MSWI residual proof in `MSWI-18`;
- `MSWI-13` → APW/D26 Project/Time + GPR + contributing owner domains; MSWI residual in `MSWI-03`/`14`/`18`;
- `MSWI-15` + `MSWI-16` → `MSWI-14`;
- `MSWI-17` → `MSWI-18` over PCA-12/Packet-08 infrastructure.

The machine-readable receipt records every disposition and retained obligation.

## Consequence pipeline

MSWI uses one shared pipeline:

`accepted source Event/change → scope/version compilation → route selection → permission filtering → dry-run envelope → target-owner validation → target-owner commit → propagation receipt → bounded further fan-out/delayed follow-up → presentation refresh`

Preview/evaluation does not prove an Event occurred.

Every target owner remains independently authoritative.

## Systemic safety rules

- no unbounded automatic reaction cascades;
- route depth and deduplication are explicit;
- cycles may block automatic commit;
- conflicting target requests use target-owner conflict rules or remain unresolved;
- rollback never erases Event history;
- inverse operations, compensation and restoration are distinct;
- Campaign time, not wall-clock time, drives delayed/offscreen change;
- aggregate state never implies invented exact individuals;
- exact/range/band/distribution/unknown uncertainty classes are preserved;
- permission filtering precedes counts/search/diagnostics/AI/export;
- optional AI is advisory only;
- paid/cloud providers are never blocking dependencies.

## Golden proof

`MSWI-18` must prove the complete family, including capabilities that were absorbed to other owners.

The durable family DCP defines 36 golden vectors covering:

- transformation attribution, reversibility and fan-out;
- target-owner rejection and cycle blocking;
- delayed consequences;
- ecology bands, pressure, migration and recovery;
- mixed-resolution accounting;
- composite multi-role identity;
- component damage, harvest and biological provenance;
- donor lineage and embodied modification;
- doctrine/social consequence integration without an MSWI social ledger;
- profession/life-loop integration without an MSWI scheduler;
- pursuit integration without an MSWI pursuit runtime;
- accessible performance timing integration;
- grand Project milestone fan-out without an MSWI Project ledger;
- deterministic procedural candidates and explicit promotion;
- stable-location current/history variants;
- transformation template configuration without runtime forks;
- fan-out/missing-route/cycle diagnostics;
- role-safe permission filtering;
- exact-head provider-off closure.

## Execution discipline

Each future surviving tranche retains the family’s 24-minute target with at least 8 minutes reserved for closeout. If implementation scope cannot credibly fit that envelope, it must split before governed start rather than silently restoring removed baseline tranches.

One owner `Continue` carries a governed-started tranche through implementation, required validation, verified closeout and next-tranche selection unless an OPS3 owner-only boundary or genuine external blocker is reached.

## Non-authorization

This reduced program does not:

- modify `operations/CURRENT.json`;
- start MSWI or SMB-08;
- grant an MSWI implementation branch;
- mutate canonical Campaign/world state;
- reopen MAS;
- promote generated/proposed content to canon;
- authorize paid/cloud dependencies or release.

Future implementation still requires ordinary OPS3 governed start.


## MSWI-01 completed — Systemic Transformation State & Integration Core

MSWI-01 completed_verified with application contract `MSWI-01.1`. Causal RED run `35603468568` at `2d7e056111d9ea58f55a76cf0c4d58f9b260d6a2` passed selector/repository health but failed the focused MSWI-01 suite on Linux and hosted Windows because the production entry points were intentionally absent. Exact-head GREEN run `35603724172` at `2c5c2d0ca84b08e6c2470c48aa761a8030a5576d` passed repository health, Linux, hosted Windows, focused tests, invariants, TypeScript typecheck and deterministic cross-platform comparison. PR #705 published that exact validated head as application main `8fa67726006237e2c68dcb1d5fb7e42c7b73b9a0`.

The delivered opening seam provides reusable transformation profiles, exact owner/version integration bindings, read-only permission-filtered projections, threshold/milestone attribution, explicit stale-state detection, uncertainty-preserving owner values, MSLR-18 typed handoff consumption, migration/version safety and semantic/keyboard/provider-off inspection. It copies no mutable canonical World, Environment, Organization, Event or spatial-law state and executes no consequence-route commit runtime.

Fresh roadmap authority schema `1.0.4` supplies no interstitial override. Reduced strict order selects `MSWI-03` — Cross-System Consequence Routing, Recovery & Domain Adapter Runtime — as selected_not_started. `MSWI-04` remains unauthorized.
