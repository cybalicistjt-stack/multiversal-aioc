# Application Implementation Roadmap — SSA-01 Closeout

**Date:** 2026-08-29  
**Program:** SSA — Semantic Spatial Authoring  
**Completed tranche:** SSA-01 — Authority Crosswalk & Spatial Semantic Taxonomy  
**Selected successor:** SSA-02 — Structural Primitives, Attachments & Construction Relationships

## Completion evidence

SSA-01 is `completed_verified`.

- Application PR: **#348**
- Application baseline: `1381a97573b6b36d31a72ddd37ed0c3177674ef3`
- Exact validated head: `f5e7d1cca6c1cdb6a06268bba4c4bb900e73c7ff`
- Validation run: `33274022700`
- Current-family selector / Repository Health: `99157467357`
- Self-hosted Linux: `99157481187`
- Self-hosted Windows: `99157481147`
- Deterministic comparator: `99157550121`
- Matching deterministic receipt SHA-256: `2297ee65a51d418839fb9e80f49c29a7e37db28c3d34832153750131ecb0eed2`
- Historical predecessor fanout: `0`
- Application merge: `a04749b381f08aaf8fc23290e7b3f1d3dd48050a`

## Delivered boundary

SSA-01 established the governed semantic-spatial crosswalk without creating a new source of game truth:

- canonical owner references for World/Reality, Scene, Exploration, Research, Creature ecology, Asset, Permission, MAI and completed ISE;
- stable semantic references with optional owner-version and provenance evidence;
- explicit separation of geometry, semantic structure and live state;
- high-level entity families and owner-specific relation families;
- confirmation state that keeps uncertain inference assistance-only;
- authorization-before-projection and hidden-cardinality exclusion;
- nonvisual semantic representation for consequential spatial meaning;
- deterministic crosswalk/taxonomy receipts.

Pixels, visual adjacency and geometry remain evidence/presentation rather than canonical semantic or structural truth. SSA-01 performs no canonical mutation and creates no parallel owner ledger.

## Family-boundary validation transition

SSA-01 is the first member of a new Validation Core family. The first application selector run `33273927303` correctly rejected `SSA-01` while the application family contract still named ISE. The existing `family_transition_rule` was then applied: active family changed to SSA, ISE-08 application baseline `1381a97573b6b36d31a72ddd37ed0c3177674ef3` became the sealed predecessor baseline, one-profile/no-history rules were retained, and workflow code was unchanged.

Changed-evidence run `33273963834` resolved only SSA-01 and exposed a verifier-only literal-whitespace mismatch in artifact `9720927142`; prose whitespace normalization in `tools/verify_ssa_01.py` corrected the validation contract without changing product behavior. Final run `33274022700` passed both platforms and deterministic comparison.

## Convergence

- Owner Continue count: `1`
- Execution cycles: `1`
- Repair cycles: `4`
- Diagnostic mode: `true`
- Unrelated historical validation jobs: `0`
- Reruns without changed evidence: `0`
- Post-merge stale-pointer incidents: `0`
- Same-cycle completion: `true`

The four repairs were evidence-driven: two AIOC program-transition control-plane projection repairs before application mutation, one application family-boundary contract transition, and one source-verifier whitespace normalization after raw artifact inspection.

## Persistence

No durable SSA-01 persistence was required. Migration `0022` remains unreserved.

## Selected successor

SSA-02 — Structural Primitives, Attachments & Construction Relationships — is `selected_not_started` only.

SSA-02 will eventually define governed walls, openings, doors, windows, floors, ceilings/roofs, stairs, ramps, rooms, entrances, shafts and other structural primitives plus attachment/connectivity relationships. Existing Scene/World/Reality/Transition/Portal/permission/MAI/ISE authorities remain canonical. Visual adjacency alone is never structural truth; imported governed semantic metadata or explicit confirmation is required where appropriate.

Selection grants no implementation branch, product-mutation authority, persistence reservation, tester distribution, release or deployment authority. A future owner `Continue` is required before SSA-02 governed start.
