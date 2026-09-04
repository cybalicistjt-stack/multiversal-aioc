# ALP — Achievements, Learning & Practice

**Program ID:** ALP  
**Status:** OWNER-APPROVED — ALP-01/02/03/04/05 COMPLETED_VERIFIED; ALP-06 SELECTED_NOT_STARTED  
**Activation:** after completed_verified ECI-01  
**Successor:** VTI-01  
**Owner and final authority:** John Brandon Turner  
**Approved:** 2026-08-27

## Current state

ALP-01 — Authority Crosswalk & Achievement/Learning/Practice Taxonomy — is `completed_verified` on application merge `c3ff8adb2311d1c59f3288a82593b358e3d47960` through PR #407. Its implementation authority is retired.

ALP-02 — Achievement Definitions, Criteria, Evidence, Scope & Provenance — is `completed_verified` on application merge `050356f7578856de5931917a60efe8af91def1bd` through PR #408. Its implementation authority is retired.

ALP-03 — Platform Onboarding & Mastery Milestones — is `completed_verified` on application merge `025f653f65be5ea8ccae1d04f9591e146c3d8797` through PR #409. Its implementation authority is retired.

ALP-04 — GM-Authored Campaign Achievements, Titles, Reputation & Reward Links — is `completed_verified` on application merge `788a8025caf8046edfeddcbf238cce972a4c5378` through PR #410. Its implementation authority is retired.

ALP-05 — Diegetic Practice Spaces, Training Scenes & Simulations — is `completed_verified` on application merge `402aa6d91795d6e75be64c106aa122b0b79cb872` through PR #411. Its implementation authority is retired.

ALP-06 — Rehearsal, Retry, Safe Failure & Training/Project Integration — is `selected_not_started` from exact application main `402aa6d91795d6e75be64c106aa122b0b79cb872`. It has no implementation branch or authority. A future owner Continue must governed-start it.

## Purpose and frozen invariants

ALP consolidates achievement, onboarding/mastery and diegetic-practice concepts into one governed learning/recognition family. Achievements and practice remain optional structures, not universal permission or capability gates. AI may explain progress or propose criteria but may not silently award achievements or infer hidden completion evidence.

Diegetic practice remains optional. Practice participation remains optional. Mechanically meaningful rewards commit only through owning Reward/Progression/Reputation/Faction systems. Character Progression, Projects, World/Scene, GCL, ISE and MAL retain their own canonical mutation authority.

ALP-01 froze the taxonomy families `platform_learning_milestone`, `campaign_achievement`, `practice_training_marker`, `project_learning_evidence`, `recognition_record`, and `mechanical_reward_reference`.

Diegetic practice remains optional. ALP-01 created no durable persistence, no migration 0022, no universal permission gate, and no hidden completion inference.

ALP-02 froze deterministic read-only definition, criterion, evidence, scope, provenance and `satisfied` / `unsatisfied` / `unknown` projection semantics. It does **not** award achievements, infer hidden evidence, mutate owner systems, create durable persistence, reserve migration `0022`, or create universal permission gates.

ALP-03 froze deterministic platform-owned onboarding/mastery milestone projection and prerequisite guidance without owner mutation, campaign achievement authoring, durable persistence, migration `0022`, or capability grants.

ALP-04 froze deterministic GM-authored campaign achievement/title/recognition/reputation/reward-reference projection. The projection preserves deterministic criterion state, campaign identity, definition provenance, title and recognition references, Reputation/Relationship/Faction owner-system references, and mechanical reward owner-system references. It does not commit rewards or mutate Character Progression or Reputation/Relationship/Faction state.

## ALP-05 completed contract

ALP-05 implements deterministic read-only **optional practice-space contracts** for diegetic practice spaces, training scenes and simulations. A practice space carries stable identity, explicit kind, scope, author and provenance; explicit practice goals; `practice_training_marker` references; and read-only references to Character Progression, Projects, World/Scene, GCL, ISE and MAL owner objects.

Authorized practice observations may project goal state as `satisfied` or `unsatisfied`. Missing, hidden or unauthorized observations remain `unknown`; hidden inventory and cardinality are never inferred. Deterministic projection and receipts are independent of supplied practice-space, goal, owner-reference and observation ordering.

Practice participation remains optional and does not grant XP, advancement, capability, achievement completion, reward, permission, or canonical owner-state mutation. There is no durable ALP-05 persistence change. Migration `0022` remains unreserved. ALP-06 rehearsal, retry, safe-failure and training/project integration behavior remains reserved.

### ALP-05 verification evidence

Acceptance RED on exact head `11cc4da854fe11f90cd95f8b6cc0b2f5eb91077c` used run `33899883790`: selector `101111207134` PASS, Linux `101111246662` FAIL at `alp05-invariants`, Windows `101111246544` FAIL at `alp05-invariants`, comparator `101111350291` PASS, deterministic receipt `e6c47a4c749d8caa4b3a22dafec5e52acb2c6c66876ac8b94e7a1ad8fb291ba2`. The ALP-05 production module was intentionally absent and historical predecessor profile fanout was zero.

Final GREEN on exact production head `359ee958759d4be86cc347e463c28a3ff565d150` used run `33900659543`: selector `101113693568`, Linux `101113735301`, Windows `101113735273`, comparator `101113906755`, deterministic receipt `fedc7e7a6a824acf582b64a095b64a42b7bae19d1a4590f3a4ee4e4b02c81288`. Linux artifact `9947503603` SHA-256 `fb07174ae1392c069d044bf465a67d848c1ebd7adeaa964e7cd0819ec6fb96b8`; Windows artifact `9947508007` SHA-256 `b9ba4cec9103afb8cde997123d11b09bd035d0cac6150b2a9c3896a92ef60ace`; comparator artifact `9947515569` SHA-256 `2e5045a712c7818179b009e1ed0b8be1a2d7684385c55190936103c7cced051f`. Production feature repair cycles were zero and historical predecessor profile fanout was zero.

Application PR #411 squash-merged the exact validated tree to verified main `402aa6d91795d6e75be64c106aa122b0b79cb872`.

## Tranches

1. **ALP-01 — Authority Crosswalk & Achievement/Learning/Practice Taxonomy** — **COMPLETED_VERIFIED**.
2. **ALP-02 — Achievement Definitions, Criteria, Evidence, Scope & Provenance** — **COMPLETED_VERIFIED**.
3. **ALP-03 — Platform Onboarding & Mastery Milestones** — **COMPLETED_VERIFIED**.
4. **ALP-04 — GM-Authored Campaign Achievements, Titles, Reputation & Reward Links** — **COMPLETED_VERIFIED**.
5. **ALP-05 — Diegetic Practice Spaces, Training Scenes & Simulations** — **COMPLETED_VERIFIED**.
6. **ALP-06 — Rehearsal, Retry, Safe Failure & Training/Project Integration** — **SELECTED_NOT_STARTED**.
7. **ALP-07 — Player/GM UX, Accessibility, Notifications & Recognition History**.
8. **ALP-08 — MAL/ISE/WCI/GCL Integration & Golden Learning/Recognition Proof**.

## Active invariant

ALP-01 through ALP-05 are frozen completed_verified contracts. ALP-06 is selected_not_started only: no branch, acceptance package, production mutation, owner-system mutation, provider activation, tester distribution, release or deployment is authorized until a future owner Continue governed-starts it. ALP-07+, VTI-01+ remain unauthorized.
