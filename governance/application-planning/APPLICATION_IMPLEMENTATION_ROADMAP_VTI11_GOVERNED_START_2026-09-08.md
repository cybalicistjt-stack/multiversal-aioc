# VTI-11 — Governed Start

VTI-11 — Adventure / Campaign Package Export — is `in_progress` from exact application baseline `145eee04181b9ed66cae887ea6830da111918c25` on `integration/vti-11-adventure-campaign-package-export`.

## Governed-start RED evidence

- exact test-only AIOC head: `e07bb429d5279f4819223152d0d61a4bce1154ec`
- canonical repository-health run: `34204525189`
- audit job: `101990801135`
- canonical authority/lifecycle/sealed-proof validation: PASS
- current control-plane regressions: 298 total, exactly one expected failure because VTI-11 was still `selected_not_started`
- repository-health artifact: `10047180291`
- artifact ZIP SHA-256: `0891fe6a900d933f1045514d09c4b839e0bd966cd36c8edf1018703a615da628`
- historical validator executions: 0

## Projection verification

The bounded state projection completed in workflow run `34205212933`, job `101992996240`. The focused VTI-11 lifecycle regression and the full 298-test current control-plane suite passed before the helper self-removed and committed the projected state. The two predecessor/planning assertions exposed by the first changed projection were made lifecycle-aware; no historical validator fanout or production authority was introduced.

## Open authority

Only application branch creation, bounded implementation scaffolding and acceptance-package work are authorized. Acceptance may cover deterministic export-package manifests for maps/scenes, encounters, creatures/NPCs, tokens, journals/handouts, treasure/items, roll tables, environments and other explicitly permitted content. Completed VTI identity, permission, hidden-information, capability and compatibility semantics remain authoritative.

## Closed authority

Production package-export behavior remains locked until a genuine matching VTI-11 self-hosted Linux/Windows RED is sealed. Provider credentials/accounts, provider network access, live external or canonical mutation, durable VTI persistence/new migration, provider activation, tester distribution, package publication/upload/distribution, release/deployment, VTI-12+ and SGC-01+ remain unauthorized. ARI/SAA remain planning only and P3D remains deferred.
## Matching application RED and bounded production unlock

- application PR: `#440`
- exact acceptance head: `8c2f75144404d4fef558a4383b081621282a9a55`
- current-family run: `34206133589`
- selector/repository-health job: `101995926174` — PASS
- Linux job: `101995973396` — matching RED at `vti11-invariants`
- Windows job: `101995973371` — matching RED at `vti11-invariants`
- deterministic comparator: `101996191118` — PASS
- deterministic receipt: `ac550c382fa35df15d600a938f65228078c706a33592200320b19cd1952709b3`
- Linux artifact: `10047821469` / `6ad82bc5928e6e5709bf736ebffb258d32a2669febdb91f014206678376e4e94`
- Windows artifact: `10047839414` / `d0939ef8c5360cc4ab0efba0122f3862545fda48598da89f16c7114eb417c7f2`
- comparison artifact: `10047848771` / `8ac9e2de5382a3c5e302198e151ba579e3e0900a31858de12b9670e007923a98`
- historical profile fanout: `0`
- failure reason: production contract intentionally absent

This seals the acceptance RED and opens production mutation only for `packages/contracts/src/virtual-tabletop-interoperability/adventure-campaign-package-export-contract.ts`. All provider credentials/accounts/network, live mutation, persistence/migration, activation, tester distribution, package publication/upload/distribution, release/deployment, VTI-12+ and SGC-01+ authority remains closed.
