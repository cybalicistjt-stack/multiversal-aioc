# Application Implementation Roadmap — MAI-03 Closeout — 2026-08-25

## Completed tranche

**MAI-03 — Grid, Coordinates, Scale & Projection Engine** is `completed_verified`.

### Application evidence

- Application PR: **#314**
- Exact validated head: `223cd0d64ae3c38f3edb2e16dddfbbbf6294ce1a`
- Exact-head Repository Health: run `32919674724`, job `98030594099` — PASS
- Validation Core: run `32919675012`
- MAI-03 Linux job: `98030595667` — PASS
- MAI-03 Windows job: `98030595750` — PASS
- MAI-03 deterministic comparison job: `98031978726` — PASS
- Linux evidence artifact: `9589464335`, digest `sha256:85b393a8491d4b79dd20c7f68190dd93132d150ae686ace30f1262861ef61055`
- Windows evidence artifact: `9589544628`, digest `sha256:251d8ce4d3c9201c338f14a6618b53914813d73e8578f4a61f6f748cab293aba`
- Comparison artifact: `9589611554`, digest `sha256:87ffd288da8b69d54bb08f5bb0e018d5ec50f0dcbe29b355a925234802b629bd`
- Deterministic receipt: `1f8c80bd7f3a252fdd43097abb1e1355e34cae0ae81a39d386676d38a232d19c`
- Application squash merge: `16a4e2c8422be4a8a1677ea98247a6eb62c05f72`
- Repair cycles: **1**

The one repair cycle corrected generic TypeScript failure-result inference (`Mai03ProjectionResult<null>`). It did not change projection formulas, owner boundaries or acceptance requirements.

## Completed projection proof

MAI-03 completed a provider-neutral read-only projection layer over the MAI-02 schema with:

- four coordinate spaces: asset-local pixel, map pixel, grid coordinate and normalized map;
- square, gridless, flat/point hex, isometric and staggered projection descriptors;
- deterministic forward/inverse grid projection;
- reversible MAI-02 asset transforms using dimensions, anchors, translation, rotation, scale and flips;
- normalized-map conversion;
- explicit finite positive pixels-per-unit presentation scale conversion;
- deterministic round-trip proof with matching Linux/Windows receipts.

Gridless maps do not invent grid coordinates, invalid/unknown projection metadata remains explicit, and no vendor/editor projection model becomes canonical.

## Completed boundaries

MAI-03 completion preserves the following verified truth:

- MAI-01 license, incomplete-pack and vendor-neutral boundaries remain binding;
- MAI-02 source/checksum/license/evidence/import lineage and unsupported-source metadata preservation remain binding;
- MIB-11/D18 retains canonical World/location identity, hierarchy, topology and navigation truth;
- D29 authoring-provenance retains governed publication/provenance workflow ownership;
- coordinates, transforms, projections and scale remain presentation constructs and do not create World/combat identity;
- no owner-domain mutation occurred;
- terrain/autotile/connectivity grammar (MAI-04), runtime geometry (MAI-05), import adapters (MAI-06), resolver automation (MAI-07), workbench UI (MAI-08), runtime owner integration (MAI-09) and later mechanics were not implemented;
- migration `0022` remains unreserved;
- no real-money commerce, tester distribution, release/deployment or provider/payment activation was introduced.

## Strict successor

Strict MAI order selects **MAI-04 — Terrain, Autotile & Connectivity Grammar** as `selected_not_started` only.

MAI-04 has:

- checkpoint `governance/ai/work-state/MAI-04-attempt-001.json`;
- no implementation branch;
- no implementation authority;
- application baseline `16a4e2c8422be4a8a1677ea98247a6eb62c05f72` at selection time.

A future owner **Continue** must freshly verify then-current canonical AIOC/application heads, re-read completed MAI-01..03 evidence plus World/provenance owner boundaries, resolve the exact terrain/autotile/connectivity grammar and authority contract, and only then governed-start MAI-04. **MAI-05+ remain unauthorized until their strict predecessors complete and are separately selected.**
