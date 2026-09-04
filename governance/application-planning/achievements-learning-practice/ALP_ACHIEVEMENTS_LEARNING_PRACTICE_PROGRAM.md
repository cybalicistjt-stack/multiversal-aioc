# ALP — Achievements, Learning & Practice

**Program ID:** ALP  
**Status:** OWNER-APPROVED — ALP-01 IN_PROGRESS  
**Activation:** after completed_verified ECI-01  
**Successor:** VTI-01  
**Owner and final authority:** John Brandon Turner  
**Approved:** 2026-08-27

## Current state

ECI-01 is `completed_verified` on exact application main `94b8dde9afdce249c873b22f0509406d77fdf099`. Owner `Continue` on 2026-09-04 governed-starts ALP-01 — Authority Crosswalk & Achievement/Learning/Practice Taxonomy — from that exact baseline on implementation branch `integration/alp-01-authority-taxonomy` with bounded implementation authority.

ALP-01 authority is limited to a read-only authority crosswalk and deterministic classification/taxonomy projection. It does not authorize achievement awarding, hidden-completion inference, mechanical reward commit, Character/Relationship/Reputation/Faction/Scene/Project mutation, persistence, migration `0022`, or any ALP-02+ behavior.

## Purpose

ALP consolidates the recovered mine-note achievement, onboarding/mastery and diegetic-practice concepts into one governed learning/recognition family. It preserves the optional Synced Achievements direction while separately developing safe practice/training spaces and mastery guidance.

ALP consumes Character progression, Reputation/Relationship, World/Scene, Projects, GCL, ISE, MAL and campaign authority. Achievements recognize evidence and may link to explicitly governed rewards, but they do not become universal permission or capability gates.

## ALP-01 governed contract

The first tranche separates six concept families before later ALP work defines criteria or runtime behavior:

1. `platform_learning_milestone` — platform-owned onboarding/mastery recognition and teaching evidence;
2. `campaign_achievement` — GM/campaign-authored accomplishment recognition;
3. `practice_training_marker` — optional Scene/training/simulation context markers that do not create success or advancement;
4. `project_learning_evidence` — Project-owned learning/practice references without Project mutation;
5. `recognition_record` — non-mechanical recognition/history classification only;
6. `mechanical_reward_reference` — reference to a possible reward whose commit authority remains entirely with Reward/Progression/Reputation/Faction owners.

ALP-01 must preserve provenance, keep platform and campaign authorship distinct, keep unknown or hidden completion evidence unresolved, and produce deterministic classification independent of input ordering. AI may explain or propose classifications but cannot award, infer hidden completion or mutate owners.

## Tranches

1. **ALP-01 — Authority Crosswalk & Achievement/Learning/Practice Taxonomy** — **IN_PROGRESS**; reconcile campaign Achievements, platform onboarding/mastery milestones, training/practice Scenes, Projects and reward authorities; separate recognition, teaching evidence, campaign accomplishments and mechanical rewards.
2. **ALP-02 — Achievement Definitions, Criteria, Evidence, Scope & Provenance**
3. **ALP-03 — Platform Onboarding & Mastery Milestones**
4. **ALP-04 — GM-Authored Campaign Achievements, Titles, Reputation & Reward Links**
5. **ALP-05 — Diegetic Practice Spaces, Training Scenes & Simulations**
6. **ALP-06 — Rehearsal, Retry, Safe Failure & Training/Project Integration**
7. **ALP-07 — Player/GM UX, Accessibility, Notifications & Recognition History**
8. **ALP-08 — MAL/ISE/WCI/GCL Integration & Golden Learning/Recognition Proof**

## Active invariant

Achievements remain optional recognition/learning structures, not universal permission gates. Achievement completion cannot grant unrelated capabilities by implication. Mechanically meaningful rewards commit only through owning Reward/Progression/Reputation/Faction systems. Platform learning badges and campaign achievements remain distinguishable in scope and authorship. Diegetic practice remains optional. AI may explain progress or propose criteria but may not silently award achievements or infer hidden completion evidence. ALP-01 creates no durable persistence. ALP-02+, VTI-01+, provider activation, tester distribution, release and deployment remain unauthorized until their owning predecessor selects them.
