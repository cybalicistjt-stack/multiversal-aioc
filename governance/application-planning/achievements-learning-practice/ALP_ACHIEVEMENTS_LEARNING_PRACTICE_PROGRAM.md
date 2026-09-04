# ALP — Achievements, Learning & Practice

**Program ID:** ALP  
**Status:** OWNER-APPROVED — ALP-01 COMPLETED_VERIFIED; ALP-02 SELECTED_NOT_STARTED  
**Activation:** after completed_verified ECI-01  
**Successor:** VTI-01  
**Owner and final authority:** John Brandon Turner  
**Approved:** 2026-08-27

## Current state

ALP-01 — Authority Crosswalk & Achievement/Learning/Practice Taxonomy — is `completed_verified` on application merge `c3ff8adb2311d1c59f3288a82593b358e3d47960` through PR #407. Its implementation authority is retired.

ALP-02 — Achievement Definitions, Criteria, Evidence, Scope & Provenance — is `selected_not_started` from that exact application main. No ALP-02 branch or implementation authority exists. A future owner `Continue` performs the governed start-preflight.

## Purpose

ALP consolidates the recovered mine-note achievement, onboarding/mastery and diegetic-practice concepts into one governed learning/recognition family. It preserves optional Synced Achievements while separately developing safe practice/training spaces and mastery guidance.

ALP consumes Character progression, Reputation/Relationship, World/Scene, Projects, GCL, ISE, MAL and campaign authority. Achievements recognize evidence and may link to explicitly governed rewards, but they do not become universal permission or capability gates.

## ALP-01 completed contract

ALP-01 implemented a deterministic read-only crosswalk across six concept families:

1. `platform_learning_milestone` — platform-owned onboarding/mastery recognition and teaching evidence;
2. `campaign_achievement` — GM/campaign-authored accomplishment recognition;
3. `practice_training_marker` — optional Scene/training/simulation context markers that do not create success or advancement;
4. `project_learning_evidence` — Project-owned learning/practice references without Project mutation;
5. `recognition_record` — non-mechanical recognition/history classification only;
6. `mechanical_reward_reference` — reference to a possible reward whose commit authority remains entirely with Reward/Progression/Reputation/Faction owners.

The implementation preserves provenance, distinct platform/campaign authorship, unresolved hidden or unknown completion evidence, deterministic ordering, and explicit false mutation/reward/persistence boundaries. It creates no owner ledger and no migration `0022`.

## ALP-01 validation evidence

- acceptance RED head: `bf331f7c02e097306bf8a7e6704bcea2b4dd184d`
- acceptance run: `33876941953`
- RED Linux job: `101036106592`
- RED Windows job: `101036106232`
- RED comparator: `101036217246`
- matching RED receipt: `edfc93fe2e4ff5e5598099683975d1c2378ea2614995b919f4b0fcc5c6e5490b`
- validated GREEN head: `ea637d3e84d0722c4a190f4d12b856c8891a6e07`
- final run: `33877131806`
- GREEN Linux job: `101036717193`
- GREEN Windows job: `101036717366`
- GREEN comparator: `101036904859`
- final deterministic receipt: `81509fda2166f4c34058a14184dadc661fc531e6a92f4dbc3f717ae4af3cf9de`
- application PR: `407`
- application merge: `c3ff8adb2311d1c59f3288a82593b358e3d47960`
- production feature repairs: `0`
- historical predecessor profile fanout: `0`

## Tranches

1. **ALP-01 — Authority Crosswalk & Achievement/Learning/Practice Taxonomy** — **COMPLETED_VERIFIED**.
2. **ALP-02 — Achievement Definitions, Criteria, Evidence, Scope & Provenance** — **SELECTED_NOT_STARTED**.
3. **ALP-03 — Platform Onboarding & Mastery Milestones**
4. **ALP-04 — GM-Authored Campaign Achievements, Titles, Reputation & Reward Links**
5. **ALP-05 — Diegetic Practice Spaces, Training Scenes & Simulations**
6. **ALP-06 — Rehearsal, Retry, Safe Failure & Training/Project Integration**
7. **ALP-07 — Player/GM UX, Accessibility, Notifications & Recognition History**
8. **ALP-08 — MAL/ISE/WCI/GCL Integration & Golden Learning/Recognition Proof**

## Active invariant

Achievements remain optional recognition/learning structures, not universal permission gates. Achievement completion cannot grant unrelated capabilities by implication. Mechanically meaningful rewards commit only through owning Reward/Progression/Reputation/Faction systems. Platform learning badges and campaign achievements remain distinguishable in scope and authorship. Diegetic practice remains optional. AI may explain progress or propose criteria but may not silently award achievements or infer hidden completion evidence. ALP-01 creates no durable persistence. ALP-02 remains selected only; ALP-03+, VTI-01+, provider activation, tester distribution, release and deployment remain unauthorized.
