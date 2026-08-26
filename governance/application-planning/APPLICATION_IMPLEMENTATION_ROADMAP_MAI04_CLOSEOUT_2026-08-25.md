# Application Implementation Roadmap — MAI-04 Closeout — 2026-08-25

## Completed tranche

**MAI-04 — Terrain, Autotile & Connectivity Grammar** is `completed_verified`.

### Application evidence

- Application PR: **#315**
- Exact validated head: `b5b7e3213a83ce38a890a3b577a2beaad087a3f7`
- Exact-head Repository Health: run `32921844538`, job `98036808168` — PASS
- Validation Core: run `32921844837`
- MAI-04 Linux job: `98036809657` — PASS
- MAI-04 Windows job: `98036809752` — PASS
- MAI-04 deterministic comparison job: `98038279918` — PASS
- Linux evidence artifact: `9590174344`, digest `sha256:2a2eacaf778ab9314ae776022485ea97a7e79028908568d5cf5f3319c625f03f`
- Windows evidence artifact: `9590246475`, digest `sha256:d601a760cd95743e6139dd7286281ed9d4c3a3e897f1bd65582e960a63ff7e55`
- Comparison artifact: `9590264218`, digest `sha256:39a3d1cdbcb3ef1d7064d280f7028ae4b1b525d466ba62acc11782ad0f666cdb`
- Deterministic receipt: `0eb0718acabb41b1c11d4262c013857b75915670a47ee984c316d63051d6633c`
- Application squash merge: `bf72b52d07c62ca81604f9fbc15b6c80b2f1a0eb`
- Repair cycles: **0**

## Completed grammar proof

MAI-04 completed a provider-neutral visual terrain/autotile/connectivity grammar over MAI-01..03 truth:

- **3** deterministic terrain descriptors;
- **4** bounded visual variants;
- **4** primary square-like local ports;
- **6** normalized hex local ports;
- explicit gridless non-autotile behavior;
- explicit `connected`, `incompatible`, `absent`, and `unknown` neighbor states;
- explicit connection channels and terrain compatibility declarations;
- deterministic priority + stable-ID visual variant selection;
- explicit manual/unresolved outcomes when permitted compatible art is unavailable;
- unknown permissions remain unresolved rather than inferred;
- unsupported source metadata remains preserved rather than silently normalized away.

## Completed boundaries

MAI-04 completion preserves the following verified truth:

- no vendor/editor, Wang-set implementation, terrain-set format or other provider-specific encoding becomes canonical Multiversal autotile truth;
- MAI-01 license/incomplete-pack rules remain binding;
- MAI-02 asset/source/checksum/license/evidence/import lineage and unsupported metadata remain binding;
- MAI-03 coordinates/projections/scale remain presentation constructs;
- visual terrain connectivity does not create canonical World adjacency, routes, topology, navigation, movement permission or gameplay traversability;
- MIB-11/D18 remains canonical World owner;
- D29 remains governed authoring-provenance owner;
- Scene/tabletop, Visibility/Permissions, and Combat/Exploration runtime owner truth is not mutated or inferred;
- no MAI-05 runtime/occlusion/interactive geometry was implemented;
- no MAI-06 importer, MAI-07 resolver, MAI-08 workbench, MAI-09 runtime integration or MAI-10 corpus/performance mechanics were implemented;
- migration `0022` remains unreserved;
- no real-money commerce, tester distribution, release/deployment or provider/payment activation was introduced.

## Strict successor

Strict MAI order selects **MAI-05 — Layers, Objects, Overhead, Occlusion & Interactive Geometry** as `selected_not_started` only.

MAI-05 has:

- checkpoint `governance/ai/work-state/MAI-05-attempt-001.json`;
- no implementation branch;
- no implementation authority;
- application baseline `bf72b52d07c62ca81604f9fbc15b6c80b2f1a0eb` at selection time.

A future owner **Continue** must freshly verify then-current canonical AIOC/application heads, re-read completed MAI-01..04 evidence, and resolve the exact Scene/tabletop, Visibility/Permissions, Combat/Exploration, World and provenance owner seams before implementing layer/object/overhead/occlusion/interactive geometry mechanics. **MAI-06+ remain unauthorized until their strict predecessors complete and are separately selected.**
