# Internal Alpha Tester Access Execution Plan v0.1.0

**Work item:** IA-D09-TA-001 — Internal Alpha Tester Access & Distribution Setup  
**Owner/final authority:** John Brandon Turner  
**Basis:** IA-D09 owner approval + STAGE-A-A12 candidate validation  
**State:** construction in progress

## Owner-selected account model

The first Internal Alpha round uses exactly 20 deterministic local Multiversal alpha identities:

- `John GM` — Campaign role `game-master`; controlled by John Brandon Turner.
- `John Player` — Campaign role `player`; controlled by John Brandon Turner.
- `tester1` through `tester18`.
- odd-numbered tester accounts use Campaign role `game-master`.
- even-numbered tester accounts use Campaign role `player`.

These are Multiversal alpha identities, not GitHub accounts. Ordinary testers receive no repository access.

## Authentication boundary

The first-round identity mechanism is a local/test identity selector supplied by the bounded Internal Alpha runner. It is deliberately not represented as production authentication. No production identity provider, password store, production credential, public registration flow, or real-user account database is authorized by this package.

The environment remains trusted local-runner/browser only and synthetic-test-only. Each browser instance selects one authorized alpha account and establishes a provider-neutral Multiversal subject session for that account.

## Distribution target

The owner-facing distribution should be a private Windows ZIP produced from the validated successor tester-access build. The ZIP should contain:

1. portable static client build;
2. one-click Windows launcher;
3. local runner/server required by the package;
4. tester-account roster projection needed by the local adapter;
5. build identity/known-limitations file;
6. `START_HERE.txt` with Windows and Android instructions;
7. recovery/issue-report instructions.

Android remains a browser profile for this round. No APK or Play Store package is claimed or required. The Android device connects to the LAN address printed by the Windows runner.

## Construction sequence

1. Freeze the 20-account roster.
2. Add deterministic account lookup and role mapping to the local alpha client/test adapter.
3. Add first-entry account selection with clear GM/Player labeling and synthetic-alpha warning.
4. Enforce role-aware dashboard/workspace entry so a GM account cannot silently become Player and a Player account cannot silently become GM.
5. Add deterministic role/access tests for all 20 accounts, including parity rules and John dual-account separation.
6. Add Windows private-distribution packaging and Android LAN/browser instructions.
7. Run focused identity/access tests, typecheck, accessibility, build, headed-browser tester-entry checks, then the proportionate A12 successor validation matrix.
8. Record the new exact candidate/build identity. Because application code changed after the previously approved exact candidate, do not distribute the successor build until its validation is complete and the owner explicitly approves that exact successor candidate for the already-bounded Internal Alpha round.

## Non-authorizations preserved

This setup does not authorize:

- real-user data collection;
- production identity provider selection;
- production credentials;
- paid provider commitments;
- public release or deployment;
- broader AI/automation authority;
- working/noncanonical Design Standards promotion;
- native Android packaging;
- tester GitHub/repository access.

## Stop conditions

Stop tester access if role assignment differs from the roster, a Player can obtain GM-only authorization, a GM login is projected as Player without an explicit separate account, hidden information leaks across roles, account selection crosses browser sessions unexpectedly, the package requires production credentials, or the successor candidate is not freshly validated.
