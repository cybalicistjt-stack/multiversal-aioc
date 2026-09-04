# ALP — Achievements, Learning & Practice

**Program ID:** ALP  
**Status:** OWNER-APPROVED — ALP-01 COMPLETED_VERIFIED; ALP-02 IN_PROGRESS  
**Activation:** after completed_verified ECI-01  
**Successor:** VTI-01  
**Owner and final authority:** John Brandon Turner  
**Approved:** 2026-08-27

## Current state

ALP-01 — Authority Crosswalk & Achievement/Learning/Practice Taxonomy — is `completed_verified` on application merge `c3ff8adb2311d1c59f3288a82593b358e3d47960` through PR #407. Its implementation authority is retired.

ALP-02 — Achievement Definitions, Criteria, Evidence, Scope & Provenance — is `in_progress` from that exact application main on `integration/alp-02-achievement-definitions-criteria-evidence-scope-provenance`. Governed implementation authority is active only for the bounded ALP-02 contract. Production mutation remains locked until genuine matching Linux/Windows acceptance RED is observed.

## Purpose

ALP consolidates recovered achievement, onboarding/mastery and diegetic-practice concepts into one governed learning/recognition family. It preserves optional Synced Achievements while separately developing safe practice/training spaces and mastery guidance.

ALP consumes Character progression, Reputation/Relationship, World/Scene, Projects, GCL, ISE, MAL and campaign authority. Achievements recognize evidence and may link to explicitly governed rewards, but they do not become universal permission or capability gates.

## ALP-01 completed contract

ALP-01 implemented a deterministic read-only crosswalk across six concept families: `platform_learning_milestone`, `campaign_achievement`, `practice_training_marker`, `project_learning_evidence`, `recognition_record`, and `mechanical_reward_reference`. Owner identity, provenance, platform/campaign distinction, optional practice semantics and hidden-evidence uncertainty remain frozen at application merge `c3ff8adb2311d1c59f3288a82593b358e3d47960`.

Diegetic practice remains optional. ALP-01 created no durable persistence, no migration 0022, no universal permission gate, and no hidden completion inference.

## ALP-02 governed contract

ALP-02 may implement deterministic read-only contracts for:

1. stable achievement-definition identity tied to an ALP-01 taxonomy family and explicit authority owner;
2. explicit criterion identity and criterion-to-evidence requirements;
3. authorized evidence references carrying source-owner/object identity and provenance references;
4. explicit scope and authorship so platform and campaign definitions remain distinguishable;
5. criterion-state projection limited to `satisfied`, `unsatisfied`, or unresolved `unknown` when evidence is missing, hidden or unauthorized;
6. deterministic receipts independent of supplied definition/evidence ordering.

ALP-02 does **not** award achievements, infer hidden evidence, commit mechanical rewards, mutate Character Progression, Reputation/Relationship/Faction, World/Scene or Projects, create a universal permission gate, grant unrelated capability, create durable ALP persistence, reserve migration `0022`, or implement ALP-03 platform milestone content.

## Tranches

1. **ALP-01 — Authority Crosswalk & Achievement/Learning/Practice Taxonomy** — **COMPLETED_VERIFIED**.
2. **ALP-02 — Achievement Definitions, Criteria, Evidence, Scope & Provenance** — **IN_PROGRESS**.
3. **ALP-03 — Platform Onboarding & Mastery Milestones**
4. **ALP-04 — GM-Authored Campaign Achievements, Titles, Reputation & Reward Links**
5. **ALP-05 — Diegetic Practice Spaces, Training Scenes & Simulations**
6. **ALP-06 — Rehearsal, Retry, Safe Failure & Training/Project Integration**
7. **ALP-07 — Player/GM UX, Accessibility, Notifications & Recognition History**
8. **ALP-08 — MAL/ISE/WCI/GCL Integration & Golden Learning/Recognition Proof**

## Active invariant

Achievements remain optional recognition/learning structures, not universal permission gates. Achievement completion cannot grant unrelated capabilities by implication. Mechanically meaningful rewards commit only through owning Reward/Progression/Reputation/Faction systems. Platform learning badges and campaign achievements remain distinguishable in scope and authorship. AI may explain progress or propose criteria but may not silently award achievements or infer hidden completion evidence. ALP-03+, VTI-01+, provider activation, tester distribution, release and deployment remain unauthorized.
