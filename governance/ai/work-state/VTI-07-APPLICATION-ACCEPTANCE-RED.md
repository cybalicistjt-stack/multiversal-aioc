# VTI-07 Application Acceptance RED

- Exact acceptance head: `5cb646cd4ea49e4ef82cc13d695c6450336c73ff`
- Application PR: `#436`
- Run: `34064038245`
- Repository-health job: `101569552203` — PASS
- Linux job: `101569566705` — expected RED at `vti07-invariants`
- Windows job: `101569566565` — matching expected RED at `vti07-invariants`
- Deterministic comparator: `101569630517` — PASS
- Deterministic receipt: `3c405551b32804277945d4047a99786a2cf5a2dd6d513e0852aae48e8ea94f71`
- Linux artifact: `9998368259`
- Windows artifact: `9998372689`
- Comparison artifact: `9998375374`

Raw lane evidence on both platforms states that `packages/contracts/src/virtual-tabletop-interoperability/permissions-hidden-information-gm-authority-contract.ts` is intentionally absent. The selector resolved exactly one current-family profile (`VTI-07`), and the deterministic payload agrees cross-platform. This is genuine matching TDD RED and authorizes only the bounded production contract.

The RED-unlock authority projection was generated from canonical AIOC main `846459e74360dca83ddbbe8dc225896ab55ee5d0`; this evidence-only commit establishes a normal user-authored exact-head validation candidate after the self-removing projection commit.
