# Bootstrap Current-State Amendment — IA-D09-TA-001 Successor Pending Owner

**State:** canonical when merged to `main`  
**Owner/final authority:** John Brandon Turner

STAGE-A-A12 remains `completed_verified`. The earlier Internal Alpha tester-access and release approvals remain valid only for their exact predecessor candidate/build; they must not be silently transferred to later application code.

## IA-D09-TA-001 current state

The owner-selected 20-account tester-access setup is constructed and freshly validated:

- `John GM` — Game Master;
- `John Player` — Player;
- `tester1` through `tester18`;
- odd-numbered tester accounts — Game Master;
- even-numbered tester accounts — Player;
- 20 total local Multiversal alpha identities: 10 GM / 10 Player.

Exact successor candidate: `de4ead1a93fa19daae3e3e5149c50139abc50f14`  
Verified app merge: `ebdb1fdaf05eb535a70255a41f76b66987a8f17a`  
Windows tester ZIP: `Multiversal-Internal-Alpha-Windows-de4ead1a93fa.zip`  
ZIP SHA256: `d3d6e223245b71bc7f6265025168d61d5eb9b39447d662233584395ff0f73983`

Validation passed:

- focused account/role suite: 13/13;
- full client regression: 172/172 tests across 61 files;
- client typecheck;
- accessibility baseline;
- Player + GM production build;
- focused setup verifier;
- packaged local-runner smoke;
- six headed-Chromium tester-entry scenarios including 390px Android-style entry and direct Player-to-GM denial;
- actual packaged PowerShell runner on `windows-latest`;
- A1 and DT-008 companion validation.

Package workflow artifact: `9263895118`, digest `sha256:51e708e8e88f93579e4a9ef99dc12340b15dfabd0ef493137f761c88d25b2796`.  
Browser evidence artifact: `9263886146`, digest `sha256:eabc62aca829f5f69a72818a6ec6e0d173e2ec4490a4ac0939b00b885c97169a`.

## Owner hold

The successor package is **validated but not yet approved for distribution**. The previous owner approval cannot be inferred because application code changed after the previously approved exact candidate.

John Brandon Turner must explicitly decide whether to approve this exact successor candidate/package for the already-bounded 20-account Internal Alpha distribution.

## Preserved boundaries

- Testers do not need GitHub accounts.
- Identity is a local/test Multiversal selector, not production authentication.
- Data remains synthetic-test-only.
- Windows distribution is a private ZIP with a one-click local runner.
- Android remains a LAN/browser profile; no APK is included or approved.
- Browser state is local per browser instance.
- This package does **not** synchronize live Campaign/session actions between Windows and Android browsers.
- The P9 physical runner remains separate lower-level acceptance evidence and is not silently substituted as product authority.
- Real-user data, production credentials, paid providers, public release/deployment, broader AI/automation authority, and working/noncanonical Design Standards promotion remain closed.

There is no automatic A13 and no automatic activation of a synchronized shared-live runtime. The current operation stops at the explicit successor distribution owner decision.
