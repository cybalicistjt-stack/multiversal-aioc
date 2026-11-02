# XTRA — Cross-Tranche Readiness Acceleration

**Program:** XTRA  
**Authority:** owner-directed 2026-11-02, recorded through OPS5 CURRENT/LANES after protected-main approval  
**Status:** XTRA-01 completed_verified; XTRA-02 blocked_external; XTRA-03/04/05 completed_verified; XTRA-06 selected pending publication.  
**Purpose:** finish independent, useful pre-PCV-03F work and prepare downstream acceptance without bypassing PCV/MTLC/AXI/MCB authorities.

## Invariants

- **Single selected on-demand scope.** XTRA is *not* a fourth persistent implementation lane. Exactly three OPS5 persistent slots remain `gpr`, `cwks`, `mtlc`. XTRA's selected substep is determined solely by `operations/CURRENT.json`; backlog prose cannot choose a successor.
- **No scope laundering.** PCV-04..10 application implementation remains predecessor-blocked; MTLC-14 retains native/human proof; AXI retains its own scope; MCB tranches remain planned unless separately authorized.
- **Independent work is real work only when tested/verified.** Source contracts, fixture tests, vendor configuration, simulated receipts, assembled packages, deployed services, installed native proof, commercial clearance, human judgment and public release are separate evidence grades.
- **Cost/right gate.** No paid services, billing activation, public launch, data transfer, redistribution or permission escalation without separate authority. Unknown rights fail closed. Synthetic fixtures only unless current lawful consent and owner approval cover data use.
- **No Railway dependency.** A Railway outage does not bar independent source work. Deployment-specific tests must preserve blocked evidence instead of fictional success.
- **Repository publishing.** Protected main is PR-only, with exact-head validation, fresh-main drift-sensitive integration and the applicable OPS5 publication mechanism. A draft PR or on-branch data is not canonical until merged.

## Dependency order and exit criteria

| Tranche | Priority | Class | Deliverable |
| --- | --- | --- | --- |
| XTRA-01 | P0 | independent | Authority, baseline and independence classification |
| XTRA-02 | P0 | conditional_external | Certification host continuity and recoverability |
| XTRA-03 | P0 | independent | Source and feature discrepancy closeout |
| XTRA-04 | P1 | independent_content_preparation | Golden Campaign and source/content fixture package |
| XTRA-05 | P1 | independent_content_preparation | Golden-path asset and commercial-rights clearance |
| XTRA-06 | P1 | preparation_only | Downstream PCV-04..10 acceptance and diagnostic prework |
| XTRA-07 | P1 | preparation_only | Role-based onboarding, help and tester operations |
| XTRA-08 | P1 | independent_research_and_synthetic | Subscription, allowance, security and rights threat preflight |
| XTRA-09 | P2 | independent_specification | Hosting, backup, privacy, monitoring and incident readiness |
| XTRA-10 | P2 | conditional_mcb_activation | MCB market/customer/brand groundwork |
| XTRA-11 | P2 | conditional_mcb_activation | MCB commercial, website, pricing and recruitment preparation |
| XTRA-12 | P2 | independent_audit_with_external_gates | Pre-PCV-03F handoff and independent terminal readiness review |

### XTRA-01 — Authority, baseline and independence classification

**Scope.** Pin OPS5/app sources and PRs; enumerate prerequisites and evidence gaps; classify each follow-on as independent, preparatory or blocked; publish no duplicate implementation owner.

**Acceptance.** The canonical source/PR matrix includes PCV-03F, MTLC-14, AXI, MCB, 25-feature ledger and all blocked PCV-04..10; evidence is pinned and no ineligible tranche is activated.

**Dependency.** OPS5 owner selection only. **Current state:** completed_verified. Verified OPS5 run 41450960691, merged PR #1928 at ef22a0420b7a31c07a4280189c23cfaefbba7c60.

### XTRA-02 — Certification host continuity and recoverability

**Scope.** Inventory Render/Supabase/Railway without dependency on Railway; address November 8 free Render PostgreSQL expiry via authorized verified export/backup, restore drill, retention and safe secrets procedures; avoid paid changes without approval.

**Acceptance.** Verified restore receipt or a fail-closed externally blocked disposition shows RPO/RTO, encryption, scope and absence of secret content; do not claim a backup on config alone.

**Dependency.** XTRA-01. **Current state:** blocked_external. Render database remains available but no verified export/restore exists; preserve owner action before 2026-11-08; do not treat this as recovered.

### XTRA-03 — Source and feature discrepancy closeout

**Scope.** Review AIOC draft PR1927 25-feature source/PR ledger, reconcile current head and resolve design-vs-implementation/status discrepancies via normal document gates.

**Acceptance.** All 25 feature IDs appear once, fresh source/PR evidence links agree, unresolved F012/F017/F024 and other gaps remain visible; publication only after required exact-head gates.

**Dependency.** XTRA-01. **Current state:** completed_verified. PR1927 exact-head source-ledger reconciliation merged at da998b6913c1e4a7aeefebc9c54e9c4072f20832.

### XTRA-04 — Golden Campaign and source/content fixture package

**Scope.** Define one complete first-party Campaign/encounter/noncombat progression, characters, rules, scenes, inventories, expected ownership and versioned fixture manifest without live multiplayer execution.

**Acceptance.** Each chosen golden-path operation has deterministic setup data, expected result, permission context, source/rights reference and assigned PCV acceptance owner.

**Dependency.** XTRA-01. **Current state:** completed_verified. PR1932 Golden Campaign source-fixture exact-head green and published, without live multiplayer or combat proof.

### XTRA-05 — Golden-path asset and commercial-rights clearance

**Scope.** Map PCV asset demand through ARI/OARC and rights/provenance; prepare original or rights-cleared assets with source digest, license, permitted use, attribution and fallbacks; record AXI visual dependencies without claiming full coverage.

**Acceptance.** No golden-path asset is silently unclassified; missing rights/rig/reviewer evidence remains blocked and commercial redistribution is denied until cleared.

**Dependency.** XTRA-01. **Current state:** completed_verified. PR1934 source-only rights/asset audit published, with all unverified media rights remaining explicitly unresolved.

### XTRA-06 — Downstream PCV-04..10 acceptance and diagnostic prework

**Scope.** Define executable test cases, fixtures, adverse cases, platform matrix, evidence receipt schemas, action/reconnect/hidden-information invariants and support/incident diagnostics for PCV-04..10.

**Acceptance.** Every downstream tranche has a bounded preflight with explicitly named real runtime dependency; no PCV-04..10 implementation or fabricated passes.

**Dependency.** XTRA-01. **Current state:** in_progress (XTRA-06 selector candidate pending publication). Acceptance and diagnostic preparation only.

### XTRA-07 — Role-based onboarding, help and tester operations

**Scope.** Compose Player/GM/Creator first-game flows from BRP-02/03, MTLC-13 and F025; supply copy, permissions/limits, return/recovery context, accessible tester instructions and feedback/diagnostic templates.

**Acceptance.** Scripts and documentation are reviewed against currently available functionality; signed-in cross-device and independent human usability remain clearly unverified.

**Dependency.** XTRA-01. **Current state:** planned. No automatic authority from this roadmap.

### XTRA-08 — Subscription, allowance, security and rights threat preflight

**Scope.** Reuse 2026-11-01 SA-BILL reference research; specify receipt authenticity, Campaign one-slot atomicity, dependency taint, export/cache denial, cancellations, offline leases and negative-case fixtures.

**Acceptance.** Policy and runnable synthetic/reference tests have sourced expected outcomes; no live payment, fake security certification or PCV-03F owner mutation.

**Dependency.** XTRA-01. **Current state:** planned. No automatic authority from this roadmap.

### XTRA-09 — Hosting, backup, privacy, monitoring and incident readiness

**Scope.** Compile provider-neutral operating runbooks, health checks, alert matrix, retention, recovery objectives, data rights/support plans and rollback drills; coordinate with XTRA-02 incident risk.

**Acceptance.** Operator runbooks cover scope/auth/rollback/privacy, identify provider account/service gaps and independent recovery evidence before live data trust.

**Dependency.** XTRA-01. **Current state:** planned. No automatic authority from this roadmap.

### XTRA-10 — MCB market/customer/brand groundwork

**Scope.** Build reusable source-evidenced research, competitive comparison, target-user/persona hypotheses, brand voice and messaging/claim matrices corresponding to MCB-01..08 without silently marking MCB tranches done.

**Acceptance.** Evidence and hypothetical claims are separated; customer observations are labeled as collected vs pending; MCB authority must be separately selected for its own tranche closeouts.

**Dependency.** XTRA-01. **Current state:** planned. No automatic authority from this roadmap.

### XTRA-11 — MCB commercial, website, pricing and recruitment preparation

**Scope.** Prepare demos, site/SEO/content templates, consented recruitment plan, pricing and GM-to-player allowance models, lifecycle/analytics plan, launch/support FAQ corresponding to MCB-09..25.

**Acceptance.** No live subscription, paid acquisition, public discovery, misleading demo or publishable commercial claims; final price and launch remain owner-gated.

**Dependency.** XTRA-01. **Current state:** planned. No automatic authority from this roadmap.

### XTRA-12 — Pre-PCV-03F handoff and independent terminal readiness review

**Scope.** Consolidate all XTRA evidence, owner decisions, retained blockers, artifact hashes and successor handoffs; provide exact pending steps for PCV-03F completion and MTLC-14/PCV-04..10 after their own gates.

**Acceptance.** Completed independent outputs have live source/PR/test evidence; external/PCV-gated tasks remain blocked, not auto-completed; no XTRA record certifies PCV completion or public readiness.

**Dependency.** XTRA-01, XTRA-02, XTRA-03, XTRA-04, XTRA-05, XTRA-06, XTRA-07, XTRA-08, XTRA-09, XTRA-10, XTRA-11. **Current state:** planned. No automatic authority from this roadmap.

## Handoff/compatibility

- PCV source: `governance/application-planning/product-convergence/PCV_PROGRAM_BACKLOG.json`, PCV-03F work-state and app PR #840.
- MTLC source: `operations/work-items/MTLC-14.json` and app PR #860.
- Existing design evidence: internal-alpha 25-feature registry, AIOC PR #1927, application Stage A source/PRs.
- Subscription/allowance research: `governance/research-evaluations/subscription-allowance-threats-2026-11-01/`.
- Market/brand: `governance/application-planning/market-capture-brand-backbone/MCB_PROGRAM_BACKLOG.json`; planned, not silently activated.
- Rights: ARI/OCS catalog and OARC-07 evidence. No catalog listing alone proves use rights.

**Unresolved decisions:** paid hosting/backup purchase; commercial SKU and price; public rights clearance of any disputed third-party content; owner approvals to select MCB tranches and any expansion of XTRA into app code. Do not make these decisions on the owner's behalf.
