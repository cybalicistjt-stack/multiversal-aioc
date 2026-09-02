# Application Implementation Roadmap — ODL-08 Closeout — 2026-09-02

## Completed tranche

ODL-08 — GM Control, Simulation Depth & Advisory AI — is `completed_verified`.

Application evidence:
- baseline: `b6dbf5539ede1505ffaefc7b1f4e551e11c48a33`
- governed-start AIOC PR: `872`
- governed-start AIOC Repository Health: `33651301557` / `100318702222`
- governed-start AIOC merge: `b214a2f38a2781f5a0d37e7c1cdfd5f181fe652c`
- application PR: `383`
- acceptance-first commit: `bff109d4b65e48fb4b24d8294527cf3e9bffd076`
- acceptance blob, unchanged through GREEN: `8e4e9b4ddc79cdfe7de845442a9e2143e35472fc`
- genuine RED head: `1129d0820e0ae28a29e0da372bd3ca3da7f48848`
- genuine RED run: `33651826652`
- RED selector/repository-health: `100320491904`
- RED self-hosted Linux: `100320533576`
- RED self-hosted Windows: `100320534585`
- RED deterministic comparator: `100320830101`
- RED Linux artifact: `9855087538`
- RED Windows artifact: `9855103966`
- RED comparison artifact: `9855112799`
- RED deterministic receipt: `e7e62f07452de4cf209602133b646218ff41561d33ec8d4c5e4f27026113b6bd`
- final validated head: `1f8ebfbf8deef70b0a0c7e4c447dc1196c2be805`
- final run: `33652175326`
- selector/repository-health job: `100321667415`
- self-hosted Linux: `100321713159`
- self-hosted Windows: `100321713018`
- deterministic comparator: `100321948086`
- Linux artifact: `9855225617`
- Windows artifact: `9855231271`
- comparison artifact: `9855240956`
- deterministic receipt: `29b98302170e459fac496d9d754c4a96c3798b91a538d7c98c9cfb5779447ff6`
- historical predecessor fanout: `0`
- application feature repair cycles: `0`
- application merge: `6a0cc4b3363167978088806146b4998f3b0d69ff`

The acceptance regression was the first application mutation. The governed proof, exactly one ODL-08 Validation Core profile and RED-aware invariant verifier were added while production contract and panel remained absent. Both self-hosted lanes passed invariants and workspace installation and then failed at client typecheck because the production imports were intentionally absent. Their deterministic RED receipts matched.

Only after genuine RED were the production contract and accessible panel added, atomically in one commit. The first complete production head passed exact-head self-hosted Linux and Windows plus deterministic comparison without application feature repair.

ODL-08 delivers read-only already-authorized GM/delegated Assistant-GM control over which ODL-01..07 advisory sources are presented, with `overview`, `standard` and `deep` as presentation/advisory granularity only. Optional AI modes are `off`, `summary` and `options`. AI is explicit advisory input only: no provider invocation, user role, actor control, decision, owner mutation, approval, commit, command, permission, mechanical resolution, hidden truth or completion authority.

Visibility is filtered before every derived surface; hidden cardinality remains undisclosed. Candidate options require resolved visible ODL basis; unresolved basis yields uncertainty. APW-D26 Project/time, MV-IA-F006 GM authority, MV-IA-F020 Permission/visibility, canonical owner domains and future SCL authority remain unchanged.

No second simulation engine, AutoGM creation, campaign-time advancement, command/action/system permission, hidden-data reveal, duplicate ledger, durable ODL-08 persistence or migration `0022` was introduced.

## Execution integrity

ODL-08 completed in one owner `Continue` and one execution cycle. Governed start required one validation-contract repair to keep legacy scorecard fields validator-compatible while enforcing the new strict one-Continue operating requirement separately. Application feature repair cycles were zero. No unrelated historical profile ran, no validation was rerun without changed evidence, and no post-merge stale-pointer incident occurred.

The application repository allows squash merge only; one rejected merge-method attempt was followed by a repository-settings read and the allowed squash merge, without code change or revalidation.

## Strict successor

ODL-09 — Organizational-Life Golden Proof — is `selected_not_started` from exact application main `6a0cc4b3363167978088806146b4998f3b0d69ff`.

Selection grants no implementation authority. A future governed start must resolve the exact golden-proof acceptance contract over completed ODL-01..08 before any application mutation.

Selection does not authorize SCL-01+ implementation, owner mutation, AI provider activation, autonomous commands, action/system permission, hidden-data disclosure, duplicate ledger, durable persistence, migration `0022`, tester distribution, release or deployment.
