# ALP — Achievements, Learning & Practice

**Program ID:** ALP  
**Status:** OWNER-APPROVED — ALP-01/02/03/04/05/06/07 COMPLETED_VERIFIED; ALP-08 SELECTED_NOT_STARTED  
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

ALP-06 — Rehearsal, Retry, Safe Failure & Training/Project Integration — is `completed_verified` on application merge `b59e47dfe5754ad22cfdbe2082585d265335da51` through PR #412. Its implementation authority is retired.

ALP-07 — Player/GM UX, Accessibility, Notifications & Recognition History — is `completed_verified` on application merge `773b9bcfbdc549e53e51dcedaae83b450a74c8fc` through PR #413. Its implementation authority is retired.

ALP-08 — MAL/ISE/WCI/GCL Integration & Golden Learning/Recognition Proof — is `selected_not_started` from exact application main `773b9bcfbdc549e53e51dcedaae83b450a74c8fc`. It has no implementation branch, acceptance-package authority, production authority, provider activation, tester distribution, release or deployment authority.

## Purpose and frozen invariants

ALP consolidates achievement, onboarding/mastery and diegetic-practice concepts into one governed learning/recognition family. Achievements and practice remain optional structures, not universal permission or capability gates. AI may explain progress or propose criteria but may not silently award achievements or infer hidden completion evidence.

Diegetic practice remains optional. Practice participation remains optional. Mechanically meaningful rewards commit only through owning Reward/Progression/Reputation/Faction systems. Character Progression, Projects, World/Scene, GCL, ISE and MAL retain their own canonical mutation authority.

ALP-01 froze the taxonomy families `platform_learning_milestone`, `campaign_achievement`, `practice_training_marker`, `project_learning_evidence`, `recognition_record`, and `mechanical_reward_reference`.

Diegetic practice remains optional. ALP-01 created no durable persistence, no migration 0022, no universal permission gate, and no hidden completion inference.

ALP-02 froze deterministic read-only definition, criterion, evidence, scope, provenance and `satisfied` / `unsatisfied` / `unknown` projection semantics. It does **not** award achievements, infer hidden evidence, mutate owner systems, create durable persistence, reserve migration `0022`, or create universal permission gates.

ALP-03 froze deterministic platform-owned onboarding/mastery milestone projection and prerequisite guidance without owner mutation, campaign achievement authoring, durable persistence, migration `0022`, or capability grants.

ALP-04 froze deterministic GM-authored campaign achievement/title/recognition/reputation/reward-reference projection. The projection preserves deterministic criterion state, campaign identity, definition provenance, title and recognition references, Reputation/Relationship/Faction owner-system references, and mechanical reward owner-system references. It does not commit rewards or mutate Character Progression or Reputation/Relationship/Faction state.

ALP-05 froze deterministic read-only optional practice-space contracts for diegetic practice spaces, training scenes and simulations. Practice participation remains optional, hidden or unauthorized practice evidence remains unknown, and practice does not grant XP, advancement, capability, achievement completion, reward, permission, or canonical owner-state mutation.

## ALP-06 completed contract

ALP-06 implements deterministic read-only contracts for optional rehearsal attempts, explicit retry lineage, safe failure, and training/project integration over the frozen ALP-01 through ALP-05 contracts.

A rehearsal carries stable identity, a practice-space reference, participant, scope, provenance, optional participation, `practice_training_marker` references, `project_learning_evidence` references, and read-only owner references to Character Progression, Projects, World/Scene, GCL, ISE, and MAL. Rehearsal remains optional and is not a universal permission or capability gate.

Each visible attempt carries stable identity, explicit sequence, optional retry lineage, provenance, and a `satisfied` or `unsatisfied` rehearsal outcome. Retry lineage is preserved rather than replacing prior attempts. Hidden or unauthorized rehearsal evidence remains `unknown`; hidden inventory or cardinality is never inferred.

Safe failure is non-mutating rehearsal semantics. An unsatisfied rehearsal attempt may be projected as evidence, but ALP-06 imposes no canonical failure penalty, injury, resource loss, project mutation, world/scene mutation, achievement completion, or reward consequence solely from that rehearsal outcome.

ALP-06 does not grant XP, does not grant advancement, does not grant capability, does not award achievements, does not commit rewards, and performs no owner-system mutation. Character Progression, Projects, World/Scene, GCL, ISE, and MAL retain canonical mutation authority.

There is no durable ALP-06 persistence change. Migration `0022` remains unreserved.

### ALP-06 verification evidence

Acceptance RED on exact head `7e9078a8f1d6a2a906b3f30842259ebbc7ff7ea2` used run `33906923458`: selector `101133915974` PASS, Linux `101133957472` FAIL at `alp06-invariants`, Windows `101133957503` FAIL at `alp06-invariants`, comparator `101134118612` PASS, deterministic receipt `d8d9d18a26fd83567b4e17cc02df777accdd9247222864cbbfa696d28e1d2338`. The ALP-06 production module was intentionally absent and historical predecessor profile fanout was zero.

Final GREEN on exact production head `0b895ee21ea7585527b3acdb309bd11b05b5bea3` used run `33907481266`: selector `101135753784`, Linux `101135792580`, Windows `101135792717`, comparator `101135958021`, deterministic receipt `5d28a9e9ca42ee65bb9c37f7c1425242b3f2ce56f24cdec0d89c5161c401cde3`. Linux artifact `9950045482` SHA-256 `ec6d2b347b831cb0cd00ae82a21c8b4eeec8c7f8c883c45975f1ab848ba3ba9d`; Windows artifact `9950048430` SHA-256 `646264848e4c8c9f369a7aa35ee9f2314c68ab642f5da1c0b87a068a7e89fdf3`; comparator artifact `9950056600` SHA-256 `52b6b1d9139c0a94a179a650a17c4ffef1fef430cb266d41be4877c9a57aaf98`. Production feature repair cycles were zero and historical predecessor profile fanout was zero.

Application PR #412 squash-merged the exact validated tree to verified main `b59e47dfe5754ad22cfdbe2082585d265335da51`.

## ALP-07 completed contract

ALP-07 implements deterministic read-only Player/GM UX projection over frozen ALP-01 through ALP-06 state. Each projection carries explicit viewer role and viewer identity; player and GM views differ only through explicit authorization and GM role creates no hidden-state inference authority.

Accessibility behavior is presentation-only. Caller-supplied display preferences may influence density, emphasis, labels, ordering or equivalent display metadata, but ALP-07 does not persist those preferences or mutate canonical ALP or owner-system state.

Notifications are deterministic notification candidates only. ALP-07 does not send messages, perform external delivery, mutate acknowledgement state, subscribe or unsubscribe users, or create delivery history by implication.

Recognition history is projected only from explicit authorized records and preserves stable identity, source family, subject identity, provenance and supplied timestamp/order metadata. Missing, hidden or unauthorized evidence, events, records and cardinality remain unknown or omitted rather than inferred.

ALP-07 does not award achievements, grant XP, advancement, capability, titles, reputation or rewards, commit mechanical rewards, or mutate Character Progression, Reputation/Relationship/Faction, World/Scene, Projects, GCL, ISE or MAL. It creates no universal permission gate, no durable ALP persistence, and no migration `0022`.

### ALP-07 verification evidence

Acceptance RED on exact head `94dd477084f397735dcf9744e07f1e9b7276a3ce` used run `33943679416`: selector `101245758343` PASS, Linux `101245778946` FAIL at `alp07-invariants`, Windows `101245778947` FAIL at `alp07-invariants`, comparator `101245846282` PASS, deterministic receipt `dfd9b42aedeecf1faa896d9d6050dedc57c5265dd75118ba2827c596787f6d3b`. The ALP-07 production module was intentionally absent and historical predecessor profile fanout was zero.

Final GREEN on exact production head `1c9de1fba3152078a1607fc43fcbbe333d8b6ade` used run `33943944092`: selector `101246503087`, Linux `101246519558`, Windows `101246519562`, comparator `101246591645`, deterministic receipt `33815b1c0da7ec674cc7175d510feda6035468a0c8f430a04b387ede9f79a19e`. Linux artifact `9962718243` SHA-256 `6bd40b177d156ad0584379c3effa4b10c50e994ed1ba51379a38c3f0519eb248`; Windows artifact `9962719646` SHA-256 `da982399311277d427309184f6bbcc22bfeb72fb0f8eef689cb5af7e04812f9c`; comparator artifact `9962722391` SHA-256 `3b3aa37ece7f7b5de35d168c3278b9af24dea7ca17d24d909dc1a888dc7491b5`. Production feature repair cycles were zero and historical predecessor profile fanout was zero.

Application PR #413 squash-merged the exact validated tree to verified main `773b9bcfbdc549e53e51dcedaae83b450a74c8fc`.

ALP-08 MAL/ISE/WCI/GCL integration and golden learning/recognition proof behavior remains reserved until a future governed start.

## Tranches

1. **ALP-01 — Authority Crosswalk & Achievement/Learning/Practice Taxonomy** — **COMPLETED_VERIFIED**.
2. **ALP-02 — Achievement Definitions, Criteria, Evidence, Scope & Provenance** — **COMPLETED_VERIFIED**.
3. **ALP-03 — Platform Onboarding & Mastery Milestones** — **COMPLETED_VERIFIED**.
4. **ALP-04 — GM-Authored Campaign Achievements, Titles, Reputation & Reward Links** — **COMPLETED_VERIFIED**.
5. **ALP-05 — Diegetic Practice Spaces, Training Scenes & Simulations** — **COMPLETED_VERIFIED**.
6. **ALP-06 — Rehearsal, Retry, Safe Failure & Training/Project Integration** — **COMPLETED_VERIFIED**.
7. **ALP-07 — Player/GM UX, Accessibility, Notifications & Recognition History** — **COMPLETED_VERIFIED**.
8. **ALP-08 — MAL/ISE/WCI/GCL Integration & Golden Learning/Recognition Proof** — **SELECTED_NOT_STARTED**.

## Active invariant

ALP-01 through ALP-07 are frozen completed_verified contracts with implementation authority retired. ALP-08 is selected_not_started from exact application main `773b9bcfbdc549e53e51dcedaae83b450a74c8fc`, with no branch, acceptance package or production mutation authorized. No owner-system mutation, notification delivery, durable preference/history persistence, provider activation, tester distribution, release or deployment is authorized. VTI-01+ remains unauthorized.