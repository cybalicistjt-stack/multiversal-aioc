# IA-D09 — Budgets and Tester-Entry Contract

## Runtime and interaction budgets

These are release-design targets to be verified against the implemented candidate. A target is not evidence until measured on the candidate.

| Budget | Target | Failure handling |
|---|---:|---|
| shell initial usable render | < 2 s on supported baseline hardware/network profile | record regression and optimize before candidate validation |
| ordinary screen transition feedback | < 200 ms | preserve immediate input acknowledgement even if data continues loading |
| local interaction response | < 100 ms where no authoritative round trip is required | surface deterministic progress when longer |
| live-session direct UI response | < 50 ms target for local control feedback | never delay input acknowledgement on optional decoration |
| search/filter on bounded alpha datasets | < 150 ms target | progressive/virtualized fallback allowed |
| accessibility focus change | immediate and deterministic | focus loss is blocking |
| reconnect status indication | visible immediately after connection-state change | no silent stale-authority state |
| authoritative reconnect recovery | measured and reported; no hard promise without implementation evidence | explicit recovering/degraded state until complete |
| optional-provider timeout | bounded and cancellable | manual/core path remains available |

Performance measurements must identify build, device/profile, dataset, and test method. Do not convert design targets into guaranteed product claims.

## Cost and provider budgets

- Core Internal Alpha workflows must function with zero optional AI-provider spend.
- Any AI/provider use must expose the applicable cost/budget state before or at proposal time where the IA-D08 contract requires it.
- Duplicate provider requests caused by retry/reconnect must not be represented as a single charge unless provider evidence proves it.
- Paid plan enrollment, increased quotas, and irreversible vendor commitments require owner authority.

## Test-data budget

The IA-D09 fixture catalog is bounded. Tester data should prefer deterministic fixtures and synthetic campaign data. The alpha must not be described as covering the complete game catalog solely because these fixtures pass.

## Tester-entry prerequisites

Before a tester receives access to a future Internal Alpha candidate, all of the following must be explicit:

1. exact build/candidate identity;
2. supported device/platform scope for that test round;
3. account role and campaign role;
4. data classification and whether the tester should use synthetic/test-only data;
5. known limitations and deferred capabilities;
6. reset, recovery, and support procedure;
7. how to report a defect with build identity and reproduction steps;
8. whether optional AI/provider features are enabled and their limits;
9. privacy/retention expectations for the test environment;
10. owner-approved access boundary for that round.

## Tester onboarding flow

`Invite/authorize -> identify build -> confirm role -> review limitations -> load deterministic tutorial fixture -> verify navigation/accessibility controls -> complete first playable action -> exercise reconnect/recovery -> enter bounded test charter`.

The onboarding path must not require advanced map features, AI assistance, broad offline authority, production credentials, or hidden developer tools.

## Stop conditions

Testing must stop or the affected feature must be disabled if the candidate exposes unauthorized hidden data, corrupts canonical history, loses stable identity/provenance, silently overwrites governed state, cannot recover authoritative action status, or crosses an owner-only release/deployment/data-collection gate.