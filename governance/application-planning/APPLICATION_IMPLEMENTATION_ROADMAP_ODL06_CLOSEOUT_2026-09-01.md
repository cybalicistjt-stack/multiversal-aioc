# Application Implementation Roadmap — ODL-06 Closeout — 2026-09-01

## Completed tranche

ODL-06 — Crisis, Coup, Fragmentation, Recombination & Recovery — is `completed_verified`.

Application evidence:
- baseline: `9c29ba560b2a36a1923d03bab0292adaae74ebbb`
- PR: `380`
- genuine RED head: `cf8f41ec6bb9f4f6cfb645f864eb773c299a1450`
- genuine RED run: `33553261083`
- RED selector/repository-health: `100007763263`
- RED self-hosted Linux: `100007803184`
- RED self-hosted Windows: `100007803223`
- RED deterministic comparator: `100008091641`
- RED deterministic receipt: `802b78508436ef7fb2b0e95c08ec5825e9fd79f2a7c241862c0bd59d192bef86`
- RED Linux artifact: `9818285737`
- RED Windows artifact: `9818303795`
- RED comparison artifact: `9818312169`
- final validated head: `1ae60f53a85e1612316600e7f8b2194e59c7dab8`
- final run: `33553744922`
- repository-health/selector job: `100009387701`
- self-hosted Linux: `100009434230`
- self-hosted Windows: `100009434187`
- deterministic comparator: `100009630954`
- deterministic receipt: `48172bd38e793a777cae7766a5c86586c517871272441f12c6b8cbdd857e30f3`
- Linux artifact: `9818474922`
- Windows artifact: `9818479590`
- comparison artifact: `9818487891`
- historical predecessor fanout: `0`
- application feature repair cycles: `0`
- application merge: `e64b5c9568428b2fe9d138ffc2dc33acfa5ea7dc`
- canonical application main after bounded repository-state repair: `ec4ac5efdaca2f495b51c0e5ea652b74ce601c47`

The acceptance regression, governed proof, RED-aware invariant verifier and exactly one ODL-06 Validation Core profile were introduced before production. Genuine RED established that invariants and workspace installation passed, then self-hosted Linux and Windows failed at client typecheck on the intentionally absent contract and panel. Deterministic comparison matched the failing receipts.

After verified RED, only the production contract and accessible panel were added atomically. The first complete production head passed exact-head self-hosted Linux and Windows plus deterministic comparison. ODL-06 therefore required zero application feature repairs.

ODL-06 delivers a visibility-first read-only projection over explicit canonical-owner event evidence for `crisis`, `coup`, `split`, `fragmentation`, `recombination`, and `recovery`. Observations reconcile only by canonical event reference and resolve only when compatible visible observed evidence agrees on event kind, opaque owner event-state reference and profile/context tuple. Missing/unknown/incompatible/conflicting evidence remains conservative. ODL-02 through ODL-05 remain advisory-only. MIB-09, Character-Actors, APW-D26, DPL, WCI and Permission/visibility remain canonical owners. No event or succession adjudication, owner mutation, Project/time advancement, command/permission grant, duplicate ledger, durable persistence or migration `0022` was introduced.

## Execution integrity note

The execution runtime stalled while the genuine RED workflow was still running. That already-started run was resumed and inspected rather than rerun, so there was no unchanged-evidence retry.

After the verified ODL-06 application merge, an erroneous empty root file `NONEXISTENT_PLACEHOLDER` was written in commit `e6f7da9db469f96fc0a19fdfc3cbbdb3436bda2d`. This was a `repository_state` defect unrelated to ODL-06 product semantics. The file was immediately removed in `ec4ac5efdaca2f495b51c0e5ea652b74ce601c47`. GitHub compare from `e64b5c9568428b2fe9d138ffc2dc33acfa5ea7dc` to `ec4ac5efdaca2f495b51c0e5ea652b74ce601c47` reports two commits and zero net changed files. ODL-06 product bytes therefore remain identical to the verified merge while the exact repaired main becomes the successor baseline.

This is recorded as one repository-state repair, zero application feature repairs, zero historical predecessor fanout, zero unchanged-evidence reruns, and zero post-merge stale-pointer incidents.

## Strict successor

ODL-07 — Business, Base, Settlement, Faction, Crew, Family & SCL Integration — is `selected_not_started` from exact repaired application main `ec4ac5efdaca2f495b51c0e5ea652b74ce601c47`.

Selection grants no implementation authority and does not authorize integration mechanics; business/base/settlement/faction/crew/family owner mutation; relationship/reputation/leadership/resource/Project/time mutation; command, action or system permission; SCL implementation; a duplicate ledger; durable persistence; or migration `0022`.

A future governed start must resolve exact integration reference vocabulary, canonical owner seams, profile/context behavior, unknown/conflict semantics, SCL-facing projection behavior and persistence before product mutation. Completed ODL-01 through ODL-06 outputs remain read-only/descriptive/advisory and cannot create ODL-07 integration state or SCL outcomes by themselves.
