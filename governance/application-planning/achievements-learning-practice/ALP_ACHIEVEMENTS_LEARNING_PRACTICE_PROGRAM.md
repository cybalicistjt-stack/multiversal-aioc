# ALP — Achievements, Learning & Practice

**Program ID:** ALP  
**Status:** OWNER-APPROVED — ALP-01/02/03 COMPLETED_VERIFIED; ALP-04 SELECTED_NOT_STARTED  
**Activation:** after completed_verified ECI-01  
**Successor:** VTI-01  
**Owner and final authority:** John Brandon Turner  
**Approved:** 2026-08-27

## Current state

ALP-01 — Authority Crosswalk & Achievement/Learning/Practice Taxonomy — is `completed_verified` on application merge `c3ff8adb2311d1c59f3288a82593b358e3d47960` through PR #407. Its implementation authority is retired.

ALP-02 — Achievement Definitions, Criteria, Evidence, Scope & Provenance — is `completed_verified` on application merge `050356f7578856de5931917a60efe8af91def1bd` through PR #408. Its implementation authority is retired.

ALP-03 — Platform Onboarding & Mastery Milestones — is `completed_verified` on application merge `025f653f65be5ea8ccae1d04f9591e146c3d8797` through PR #409. Its implementation authority is retired.

ALP-04 — GM-Authored Campaign Achievements, Titles, Reputation & Reward Links — is `selected_not_started` from exact application main `025f653f65be5ea8ccae1d04f9591e146c3d8797`. It has no implementation branch, acceptance authority or production authority. A future owner Continue must governed-start it before mutation.

## Purpose

ALP consolidates recovered achievement, onboarding/mastery and diegetic-practice concepts into one governed learning/recognition family. It preserves optional Synced Achievements while separately developing safe practice/training spaces and mastery guidance.

ALP consumes Character progression, Reputation/Relationship, World/Scene, Projects, GCL, ISE, MAL and campaign authority. Achievements recognize evidence and may link to explicitly governed rewards, but they do not become universal permission or capability gates.

## ALP-01 completed contract

ALP-01 implemented a deterministic read-only crosswalk across six concept families: `platform_learning_milestone`, `campaign_achievement`, `practice_training_marker`, `project_learning_evidence`, `recognition_record`, and `mechanical_reward_reference`. Owner identity, provenance, platform/campaign distinction, optional practice semantics and hidden-evidence uncertainty remain frozen at application merge `c3ff8adb2311d1c59f3288a82593b358e3d47960`.

Diegetic practice remains optional. ALP-01 created no durable persistence, no migration 0022, no universal permission gate, and no hidden completion inference.

## ALP-02 completed contract

ALP-02 implemented deterministic read-only contracts for stable achievement-definition identity tied to an ALP-01 taxonomy family and explicit authority owner; explicit criterion identity and criterion-to-evidence requirements; authorized evidence references carrying source-owner/object identity and provenance references; explicit scope and authorship so platform and campaign definitions remain distinguishable; criterion-state projection limited to `satisfied`, `unsatisfied`, or unresolved `unknown`; and deterministic receipts independent of supplied definition/evidence ordering.

ALP-02 does **not** award achievements, infer hidden evidence, commit mechanical rewards, mutate Character Progression, Reputation/Relationship/Faction, World/Scene or Projects, create a universal permission gate, grant unrelated capability, create durable ALP persistence, reserve migration `0022`, or implement ALP-03 platform milestone content.

### ALP-02 verification evidence

Acceptance RED on exact head `f86c09aae3af19e7063bc6d0b41f45f6d95c1b45` used run `33880640379`: repository-health/selector `101048164195`, Linux `101048210194`, Windows `101048210090`, comparator `101048360266`, deterministic receipt `f4404793c098b1e382916fc414dcbc47a30f72a2c3922e78b6c9fccd0493015b`.

Final GREEN on exact production head `3e5d47edda7a28f25f6f282a0a4d770570d46280` used run `33880797279`: repository-health/selector `101048684651`, Linux `101048728855`, Windows `101048728763`, comparator `101048936025`, deterministic receipt `84d6bfd06ce885887e06bcae1b057ac2ee6dc0a4865941956a2fdf1c5bfac97c`. Production feature repair cycles were zero and historical predecessor profile fanout was zero.

Application PR #408 merged the validated tree to `050356f7578856de5931917a60efe8af91def1bd`.

## ALP-03 completed contract

ALP-03 implemented deterministic read-only platform-owned `onboarding` and `mastery` milestone definitions over the frozen ALP-02 definition/criteria/evidence projection; stable milestone identity and deterministic ordering; explicit ALP-02 definition and criterion references; prerequisite milestone references that may shape learning guidance without becoming a permission gate; progress states derived only from authorized ALP-02 evidence; optional next-step guidance; and deterministic receipts independent of milestone, definition and evidence ordering.

ALP-03 does **not** award achievements, mutate completion, infer hidden evidence, commit rewards, mutate owner systems, grant capabilities, author campaign achievements, implement diegetic practice, create durable persistence, reserve migration `0022`, or implement ALP-04 campaign achievement behavior.

### ALP-03 verification evidence

Acceptance RED on exact head `a71cc81b6b815b39c90159d13ae43d4b33d5f359` used run `33885427744`: repository-health/selector `101063899325`, Linux `101063942140`, Windows `101063942161`, comparator `101064060265`, deterministic receipt `17f107d0fb2886f6805b57e32282d670046396e96a10f3576c19869162585303`. Both self-hosted lanes failed at `alp03-invariants` while the production milestone module was absent.

Final GREEN on exact production head `a8243e69e5c3831b858e11a87e1dd270865261ab` used run `33886355199`: repository-health/selector `101066974530`, Linux `101067071097`, Windows `101067071127`, comparator `101067567712`, deterministic receipt `a0f75ca0b9ff585dc00dab4ba684abf8b26c412becc53f1026fd8e659c081d1d`. Production feature repair cycles were zero and historical predecessor profile fanout was zero.

Application PR #409 squash-merged the unchanged validated head to verified main `025f653f65be5ea8ccae1d04f9591e146c3d8797`.

## ALP-04 selected boundary

ALP-04 is selection only. A future governed start may bound GM-authored campaign achievements, titles, Reputation/Relationship/Faction references and mechanical reward references while preserving owner-system commit authority. Until that governed start, there is no ALP-04 branch, acceptance package or production mutation.

## Tranches

1. **ALP-01 — Authority Crosswalk & Achievement/Learning/Practice Taxonomy** — **COMPLETED_VERIFIED**.
2. **ALP-02 — Achievement Definitions, Criteria, Evidence, Scope & Provenance** — **COMPLETED_VERIFIED**.
3. **ALP-03 — Platform Onboarding & Mastery Milestones** — **COMPLETED_VERIFIED**.
4. **ALP-04 — GM-Authored Campaign Achievements, Titles, Reputation & Reward Links** — **SELECTED_NOT_STARTED**.
5. **ALP-05 — Diegetic Practice Spaces, Training Scenes & Simulations**
6. **ALP-06 — Rehearsal, Retry, Safe Failure & Training/Project Integration**
7. **ALP-07 — Player/GM UX, Accessibility, Notifications & Recognition History**
8. **ALP-08 — MAL/ISE/WCI/GCL Integration & Golden Learning/Recognition Proof**

## Active invariant

Achievements remain optional recognition/learning structures, not universal permission gates. Achievement completion cannot grant unrelated capabilities by implication. Mechanically meaningful rewards commit only through owning Reward/Progression/Reputation/Faction systems. Platform learning badges and campaign achievements remain distinguishable in scope and authorship. Diegetic practice remains optional. AI may explain progress or propose criteria but may not silently award achievements or infer hidden completion evidence. ALP-04 is selected only; no implementation authority exists until a future governed start. ALP-05+, VTI-01+, provider activation, tester distribution, release and deployment remain unauthorized.