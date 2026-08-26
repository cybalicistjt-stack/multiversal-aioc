# Application Implementation Roadmap — MAI-07 Closeout — 2026-08-26

## Completed tranche

**MAI-07 — Semantic Asset Taxonomy, Availability Resolver & Cross-Pack Substitution** is `completed_verified`.

### Application evidence

- Application PR: **#318**
- Exact validated head: `06e291c68ee79f58b7115d62b878f35e300d700a`
- Exact-head Repository Health: run `32935412459`, job `98075587069` — PASS
- Validation Core: run `32935412701` — PASS
- MAI-07 Linux job: `98075588684` — PASS
- Linux artifact: `9594801142`, digest `sha256:b9a6b14dda47ddc9540e95260e280a17b1558d6e692ba36d1efb3156fc634ba0`
- MAI-07 Windows job: `98075588678` — PASS
- Windows artifact: `9594818885`, digest `sha256:75fe6b4e10a3edaf6583d69312e258d66917c1f1a0ae019383a7d5fa54a19df9`
- MAI-07 deterministic comparison job: `98077001992` — PASS
- Comparison artifact: `9594892255`, digest `sha256:3474e105218d8dd3774505043e348416ae744c824ed0edefadad5fe966448e9c`
- Deterministic receipt: `f94ab58d2e7000910afaf8eceec3e59b13ce58b468bb0e5325d85c25e7723266`
- Application squash merge: `c7aeff6470199366ba033cce892e6816f9253d8a`
- Repair cycles: **1**

## Completed resolver proof

MAI-07 completed the governed semantic availability/resolution layer over MAI-01..06:

- provider-neutral semantic requirements remain independent from provider/package identity;
- explicit availability distinguishes permitted-compatible, denied, unknown-permission, incompatible, missing and unverified evidence;
- eligibility requires catalogued compatibility plus explicit granted `useInExperience` permission;
- cross-pack substitution additionally requires explicit semantic compatibility, granted `substitute` permission and enabling policy;
- deterministic ranking is independent of catalog ordering and does not invent semantic equivalence;
- manual assignment/override remains first-class and an ineligible pin stays explicitly unresolved rather than silently falling back;
- approved placeholders require explicit policy and remain separate from missing/unresolved outcomes;
- stable diagnostics and receipts preserve requirement, asset, package, source and permission evidence;
- Linux and Windows produced the identical deterministic receipt `f94ab58d2e7000910afaf8eceec3e59b13ce58b468bb0e5325d85c25e7723266`.

## Completed boundaries

MAI-07 completion preserves the following verified truth:

- no vendor/editor/provider schema becomes canonical Multiversal truth;
- no asset pack is assumed complete;
- semantic requirements remain separate from selected/available art;
- denied, unknown and unverified permission cannot become allowed use;
- semantic compatibility is not inferred from filenames, provider identity, visual similarity or missing metadata;
- MAI-06 raw-source/import diagnostics and unsupported metadata remain preserved evidence;
- no provider acquisition, download, authentication, scraping, purchase or payment behavior was introduced;
- MIB-11/D18 World, D29 provenance, Scene/Tabletop, Visibility/Permissions and Combat/Exploration retain canonical owner truth;
- no MAI-08 workbench, MAI-09 runtime integration or MAI-10 corpus/performance mechanics were implemented;
- migration `0022` remains unreserved;
- no real-money commerce, tester distribution, release/deployment or provider/payment activation was introduced.

## Repair history

The first exact-head MAI-07 validation exposed a governed-report/verifier literal mismatch. The bounded repair added the already-approved phrase `catalog-only deterministic resolver` to the MAI-07 report without weakening the validator or changing the resolver contract. The repaired exact head then passed the complete declared gate.

## Strict successor

Strict MAI order selects **MAI-08 — Asset Intake Wizard, Map Composer, Palette & Workbench** as `selected_not_started` only.

MAI-08 has:

- checkpoint `governance/ai/work-state/MAI-08-attempt-001.json`;
- no implementation branch;
- no implementation authority;
- application baseline `c7aeff6470199366ba033cce892e6816f9253d8a` at selection time.

A future owner **Continue** must freshly verify then-current canonical AIOC/application heads, re-read completed MAI-01..07 evidence, and resolve the bounded asset-intake wizard, map-composer, palette and workbench contract plus owner/permission/provenance boundaries before implementation. **MAI-09+ remain unauthorized until their strict predecessors complete and are separately selected.**
