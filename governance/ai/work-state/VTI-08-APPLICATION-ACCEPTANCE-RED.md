# VTI-08 Application Acceptance RED

- Application PR: #437
- Exact acceptance head: `420dced5ba3daf982d80a5b6cf141d2bdb4376bd`
- Validation run: `34066821411`
- Repository health job: `101576932682` — PASS
- Linux job: `101576947365` — matching RED at `vti08-invariants`
- Windows job: `101576947375` — matching RED at `vti08-invariants`
- Deterministic comparator: `101576996334` — PASS
- Deterministic receipt: `45e107c94e4cf57ae3e360cf1e89b043c8dc79d60f95362afed9a52458fb0bc2`
- Linux artifact: `9999198302`
- Windows artifact: `9999200675`
- Comparison artifact: `9999203683`
- Historical profile fanout: `0`

Both self-hosted lanes failed for the same governed reason: the production VTI-08 contract was intentionally absent. This seals matching RED and authorizes only `packages/contracts/src/virtual-tabletop-interoperability/adapter-sdk-capability-manifest-reference-vtt-contract.ts`. Provider selection/schemas/credentials/accounts/network/live mutation/persistence/new migration/activation/tester distribution/release/deployment/VTI-09+/SGC-01+ remain unauthorized.
