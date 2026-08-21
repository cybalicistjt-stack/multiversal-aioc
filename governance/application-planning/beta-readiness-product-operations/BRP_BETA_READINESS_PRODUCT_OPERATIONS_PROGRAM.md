# BRP — Beta Readiness & Product Operations

**Program ID:** BRP  
**Program name:** Beta Readiness & Product Operations  
**Version:** 0.1.0  
**Status:** OWNER-APPROVED — PLANNED BETA GATE  
**Owner and final authority:** John Brandon Turner  
**Approved:** 2026-08-21  
**Activation:** after SMB-16  
**Successor:** SMB-17

## 1. Purpose

BRP is the explicit product-operations gate between a feature-complete supported product and a real external beta. It converts the systems completed by MIB and SMB-01 through SMB-16 into a product ordinary external users can safely install, understand, operate, recover, update, report on and resume without developer intervention.

BRP is not another gameplay-system program. SGC remains the retained source/gameplay coverage closure authority, and SMB remains product maturation/buildout authority. BRP owns the missing beta-readiness proof: supportability, durability, observability, recovery, cohort control, tester operations and one integrated `BETA_READY` acceptance package.

BRP pulls beta-grade forms of backup, observability, crash reporting and rollback forward from final commercial release engineering. SMB-18 still owns commercial/release-grade operations, stores/distribution, billing/entitlements when approved and launch operations.

## 2. Activation and authority boundary

BRP activates after SMB-16 Accessibility, Localization & Device Completion and before SMB-17 External Beta & Community Foundations unless the owner later canonicalizes a different dependency order.

BRP planning does not itself authorize tester distribution, public release, paid infrastructure/providers, public community activation, billing, stores or marketing claims. Each tranche must receive normal current-work selection and pass its declared validation gates.

## 3. Tranche plan

### BRP-01 — Beta Definition, Supported Matrix & Acceptance Contract

Define the exact meaning of `BETA_READY`: supported device/OS/browser classes, required Player/GM/Creator journeys, network conditions, campaign/content scale, stability budgets, allowed defect classes, beta entry criteria and beta exit criteria.

**Completion gate:** one versioned acceptance contract can deterministically classify a candidate as not-ready or eligible for the remaining BRP proof; unsupported environments and deferred capabilities are explicit.

### BRP-02 — Account Lifecycle, Consent, Recovery & Data Rights

Prove ordinary-user signup/sign-in, verification where required, invitation acceptance, session/device management, account recovery, ownership recovery, export/deletion requests, privacy choices, beta participation consent and family/guardian seams where applicable.

**Completion gate:** representative account lifecycle journeys complete without administrator/database intervention and preserve existing account/Campaign/family authority boundaries.

### BRP-03 — Guided Onboarding, Teaching, Help & Product Voice

Finish first-run Player, GM and Creator onboarding; guided first Campaign/session experiences; contextual teaching/help; empty states; validation/recovery/error language; searchable help; and the approved warm, knowledgeable, encouraging, restrained Multiversal product voice.

This tranche is the product-completion owner for the retained TODO-UX-VOICE requirement, while UI/Screen Design Bibles remain design authorities.

**Completion gate:** primary first-run and failure/recovery journeys meet comprehension/usability acceptance and product-language review without developer explanation.

### BRP-04 — Beta Distribution, Installation, Updates & Version Compatibility

Turn SMB-13 internal-alpha productization into beta-grade distribution: supported installers/packages, version verification, update flow, safe upgrade path, client/server compatibility, stale-client behavior, migration between beta builds and recovery from interrupted/failed updates.

**Completion gate:** ordinary supported users can install, update, recover from an interrupted update and resume the same authoritative Campaign state without developer hand-holding.

### BRP-05 — Observability, Telemetry, Crash Reporting & Privacy-Safe Evidence

Connect MIB-16 diagnostics to deployed beta operation: crash/error capture, correlation identifiers, product health/performance telemetry, automatic bug bundles, log redaction, evidence consent, privacy classifications and diagnostic export.

**Completion gate:** declared failures can be traced from user-visible incident to actionable privacy-safe evidence without exposing hidden/private cross-context data.

### BRP-06 — Data Durability, Backup, Restore, Migration & Rollback

Implement and prove beta-grade automated backups, Campaign/data restore, corruption detection, migration rehearsal, failed-migration recovery, application/data rollback and published beta recovery objectives.

**Completion gate:** destructive rehearsal scenarios restore to verified authoritative state inside declared beta RPO/RTO targets, with no duplicate irreversible effects.

### BRP-07 — Feature Flags, Cohorts, Remote Configuration & Kill Switches

Provide governed cohort targeting, staged rollout, feature flags, remote safe configuration and kill switches for risky/experimental capabilities, including AI/community surfaces when applicable, without changing canonical game-state authority.

**Completion gate:** a feature can be enabled for a bounded cohort, disabled after a simulated defect and later re-enabled without corrupting Campaign state or silently changing user consent/permissions.

### BRP-08 — Security, Abuse, Moderation & Incident Operations

Operationalize SMB-14 security/privacy/family hardening through authorization regression, secret/config handling, rate/abuse controls, block/report flows, moderation queues where applicable, dependency/security checks and incident runbooks.

Family-safety policy remains owned by MIB-17/SMB-14; BRP proves deployed enforcement and incident operation.

**Completion gate:** declared security/abuse/privacy incident scenarios can be detected, contained, evidenced, recovered and reviewed without unauthorized data exposure.

### BRP-09 — Tester Support, Feedback, Triage & Known-Issue Workflow

Provide in-product feedback/bug reporting, reproducibility evidence, support routing, severity taxonomy, known-issue publication, release notes/changelog, tester communications and report → reproduce → fix → regression → beta-update traceability.

**Completion gate:** an external-style tester report can travel through the complete support/engineering loop and return as a verified fix/update with the original evidence linked.

### BRP-10 — Beta Content, Balance & Real-Play Readiness Sweep

Exercise the real first-party packs/campaign from SMB-08/09 rather than synthetic fixtures across character creation/progression, combat, economy, inventory, crafting, magic, downtime/cozy, travel, vehicles, companions, GM workflows, live/async transitions, failure and recovery.

This tranche may surface tuning/content defects but does not invent missing system authority; defects route to their owning domain/tranche.

**Completion gate:** representative complete play is possible using production-intended content without fixture-only dependencies, and blocking balance/content/integration defects have explicit dispositions.

### BRP-11 — Golden Beta Proof & Marketing Evidence Handoff

Run the end-to-end ordinary-user proof: acquire permitted beta package → install → account/onboarding → create/join Campaign → Character → live play → asynchronous continuation → disconnect/reconnect → update → report a defect → recover/restore → return later and resume from the same authoritative history.

Publish the versioned `BETA_READY` evidence package with supported-matrix results, reliability/recovery measures, unresolved issue register and product capability evidence suitable for downstream claims review.

**Completion gate:** the declared external-beta cohort scenario passes without developer intervention across the supported matrix. The resulting evidence may satisfy product-dependent MCB claims/demo prerequisites but does not itself authorize public launch or paid acquisition.

## 4. Strict default order

`BRP-01 → BRP-02 → BRP-03 → BRP-04 → BRP-05 → BRP-06 → BRP-07 → BRP-08 → BRP-09 → BRP-10 → BRP-11`

## 5. Marketing handoff rule

MCB market/category/customer/brand research and other evidence-independent preparation may proceed earlier when separately selected. Product-dependent public capability claims, final pricing/packaging decisions, major acquisition activation, review/press demonstration and launch marketing must use current product/customer evidence; BRP-11 provides the formal beta product-evidence handoff before SMB-17 external beta broadens the cohort.

## 6. Whole-program invariants

- BRP does not add or replace gameplay mechanics merely to pass beta readiness.
- No telemetry/support path may bypass Campaign/visibility/privacy/family authority.
- Backup/restore/rollback must preserve owner-domain receipts and avoid duplicate irreversible effects.
- Feature flags may control availability/presentation but cannot secretly alter canonical authority or user consent.
- Beta-grade operational systems introduced here are hardened to commercial/release grade in SMB-18 rather than duplicated.
- A queued validation run, staged next step or open PR is not BRP completion; only declared verified evidence counts.
- `BETA_READY` is an evidence state, not a marketing slogan or release authorization.