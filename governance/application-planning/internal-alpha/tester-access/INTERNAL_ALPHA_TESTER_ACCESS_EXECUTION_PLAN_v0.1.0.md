# Internal Alpha Tester Access Execution Plan v0.1.0

**Work item:** IA-D09-TA-001 — Internal Alpha Tester Access & Distribution Setup  
**Owner/final authority:** John Brandon Turner  
**Basis:** IA-D09 owner approval + STAGE-A-A12 candidate validation  
**State:** successor validated; blocked on explicit owner distribution approval

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

## Current runtime boundary

The Stage A alpha client still uses synthetic state local to each browser instance. The Windows host and Android browser can each exercise their assigned Multiversal GM/Player identity and role-safe UI, but this tester package does **not** synchronize live Campaign/session actions between the two browser instances.

The previously completed P9 physical runner proves a separate lower-level shared-device/session transport pattern. That acceptance harness is not silently substituted into the Internal Alpha client and does not make this package a synchronized multi-user runtime.

Therefore this first distribution is valid for role isolation, identity/workspace entry, UI/workflow, accessibility, bounded synthetic content/features, recovery surfaces, and device/browser behavior. Synchronized live GM/Player play remains outside this package and is not automatically activated.

## Validated successor identity

Exact successor candidate: `de4ead1a93fa19daae3e3e5149c50139abc50f14`  
Verified application merge: `ebdb1fdaf05eb535a70255a41f76b66987a8f17a`  
Windows ZIP: `Multiversal-Internal-Alpha-Windows-de4ead1a93fa.zip`  
ZIP SHA256: `d3d6e223245b71bc7f6265025168d61d5eb9b39447d662233584395ff0f73983`

Validation evidence:

- 13/13 focused identity/role tests passed;
- 172/172 full client regression tests passed across 61 files;
- typecheck passed;
- accessibility baseline passed;
- Player + GM production build passed;
- focused tester-setup verifier passed;
- packaged local-runner smoke passed;
- 6/6 headed Chromium tester-entry scenarios passed, including 390px Android-style entry, Player-to-GM denial, and John dual-account separation;
- actual packaged PowerShell runner passed on `windows-latest`;
- A1 and DT-008 companions passed;
- A3 and A10 substantive verifier/typecheck/test/build/output stages passed, with only their stale legacy cleanup assertions failing.

Package artifact: `9263895118`, digest `sha256:51e708e8e88f93579e4a9ef99dc12340b15dfabd0ef493137f761c88d25b2796`.  
Browser evidence artifact: `9263886146`, digest `sha256:eabc62aca829f5f69a72818a6ec6e0d173e2ec4490a4ac0939b00b885c97169a`.

## Distribution target

The owner-facing distribution is a private Windows ZIP. It contains:

1. portable static client build with separate Player/default and GM entry pages;
2. one-click Windows launcher;
3. local static runner/server;
4. the 20-account roster projection;
5. build identity/limitations manifest;
6. `START_HERE.txt` with Windows and Android instructions;
7. recovery/troubleshooting boundaries.

Android remains a browser profile for this round. No APK or Play Store package is claimed or required. The Android device connects to the LAN address printed by the Windows runner.

## Construction and validation sequence

1. Freeze the 20-account roster. **Done.**
2. Add deterministic account lookup and role mapping. **Done.**
3. Add account selection and clear GM/Player labeling. **Done.**
4. Enforce role-aware dashboard/workspace entry. **Done.**
5. Add deterministic role/access tests for all 20 accounts. **Done.**
6. Add Windows private-distribution packaging and Android LAN/browser instructions. **Done.**
7. Run focused, full-regression, browser, and actual Windows package validation. **Done.**
8. Record exact successor candidate/package identity. **Done.**
9. Obtain explicit owner approval for this exact successor candidate/package before distribution. **Pending owner decision.**

The previous owner approval is not reused automatically because it was bound to the predecessor candidate `56b127f1fc01eebe5c73ba0472a5b6496fe92b5e`.

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
- tester GitHub/repository access;
- synchronized shared live Campaign/session authority between browser instances.

## Stop condition

Do not distribute the successor ZIP until John Brandon Turner explicitly approves the exact successor candidate/package recorded above. After any future code change, this exact approval requirement applies again to the changed candidate.
