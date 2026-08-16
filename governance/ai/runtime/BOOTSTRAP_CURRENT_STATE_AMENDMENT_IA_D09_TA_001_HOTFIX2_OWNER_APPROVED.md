# Bootstrap Current-State Amendment — IA-D09-TA-001 Hotfix 2 Owner Approved

**State:** canonical on `main`  
**Owner/final authority:** John Brandon Turner

IA-D09-TA-001 remains `completed_verified`, but its distributable package identity is superseded by the physically validated Hotfix 2 replacement.

## Current approved exact package

- Replacement Windows tester ZIP: `Multiversal-Internal-Alpha-Windows-HOTFIX2-a4e262167aa9.zip`
- ZIP SHA256: `5c9f31c96a3373f927f8d3a7ee6ee821aafeda8d0ae26a0c6cecf94ca129e0de`
- Hotfix marker: `IA-HOTFIX-ACCOUNT-DISPATCH-2`
- Default port: `8877`
- Application repair PR: `#156`
- Application repair merge: `7cc9fa4a042a461d03c88d69c2b18ed18c0f9e21`
- AIOC physical-evidence merge: `f717f14730bf617e8176806cfb6134d0da30ff19`
- Owner replacement-package decision: `governance/application-planning/internal-alpha/tester-access/IA_D09_TA_001_HOTFIX2_OWNER_DISTRIBUTION_DECISION_20260816.json`

On August 16, 2026, John Brandon Turner explicitly approved this exact replacement package for the bounded 20-account Internal Alpha distribution.

## Physical Windows evidence

All 20 accounts were physically exercised on Hotfix 2:

- `John GM` plus tester1/3/5/7/9/11/13/15/17: 10/10 opened in GM mode.
- `John Player` plus tester2/4/6/8/10/12/14/16/18: 10/10 opened in Player mode.
- Incorrect role routing: 0/20.
- The previous `Not Found` defect did not recur.

## Withdrawn packages

Do not distribute:

- `Multiversal-Internal-Alpha-Windows-de4ead1a93fa.zip` / SHA256 `d3d6e223245b71bc7f6265025168d61d5eb9b39447d662233584395ff0f73983` — owner approval superseded because physical Windows testing exposed a distribution-entry defect.
- `Multiversal-Internal-Alpha-Windows-fe9e0b3cc45d-HOTFIX-CANDIDATE.zip` — first hotfix candidate, physically failed and withdrawn.

## Known nonblocking alpha issue

Application issue `#157`: GM sidebar buttons Campaign / Session / Combat / Assets are inert. The owner observed this during physical validation. It does not invalidate account-role routing and is accepted as a known Internal Alpha usability issue for this exact distribution package.

## Distribution and authority boundary

Exactly 20 local Multiversal alpha identities remain authorized: 10 GM / 10 Player. Testers do not need GitHub accounts. Data remains synthetic-test-only. Android remains trusted-LAN browser access; no APK is approved.

Browser state remains local per browser instance. This approval does **not** authorize synchronized live GM/Player Campaign/session authority.

Still not authorized: real-user data, production credentials/provider, paid providers, public release/deployment, broader AI/automation authority, Design Standards promotion, native Android APK, or synchronized shared-live Campaign/session authority.

There is no automatic A13. The next bounded operation is use/distribution of the exact approved Hotfix 2 package and normal Internal Alpha defect capture; any altered/rebuilt package requires a new exact-package validation and owner decision.
