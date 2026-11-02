# XTRA-07 — Player, GM, Creator and Tester Onboarding/Human-Evidence Guide

**Status:** Prepared from BRP-02/03, MTLC-13 and MV-IA-F025 source contracts. **These are proposed scripts, not observations of successful installed UI.**  
**Machine-readable companion:** [XTRA-07 Role and Tester Matrix](XTRA-07_ROLE_TESTER_ONBOARDING_MATRIX_v1.0.0.json).

## What is real source evidence — and what is not

BRP-02 completed an owner-bounded account/session/recovery and subject-bound data-rights source implementation; BRP-03 completed guided first-run and help/product-language source work; MTLC-13 completed accessible quickstarts, physical/one-shot/spectator and lifecycle source coverage. F025 supplies a detailed approved internal-alpha support and redaction design. **None of these proves current installed PCV-03F authenticated Windows/Android parity or an independently observed human first-session success.**

The scripts below use the published **Beacon Debt** five-scene fixture as the example. Its launch snapshot is synthetic and GM-only, has no real Player/Character binding and no recorded live actions. It must never be represented as completed two-human play or combat. XTRA-05 rights clearance is still incomplete for all nine PCV asset families.

## Tester setup and reporting protocol

A tester should begin with the exact application version, release/environment classification, build SHA, currently authorized account role and Campaign context. **Do not invent a valid version or account when the UI is unavailable.** Later real testing must use separate authenticated humans and devices, with informed consent and permission-safe evidence.

For each test: identify the source-specific task ID, action/initial state, expected versus actual behavior, allowed role, Windows/Android and Phone/Desktop View where relevant, time and sanitized event/permission receipt. If the app does not expose the needed flow, mark it **UNAVAILABLE/NOT_RUN** and record a safe diagnostic; do not replace it with a fixture screenshot. No test here is marked PASS.

## Role-specific first-use and recovery scripts

### PLAYER — Join only the Campaign to which the verified Player was invited, bind an authorized Character, participate and resume safely.

| Step | Intended user task | Verification boundary |
|---|---|---|
| 1. identify-release | Confirm build, environment and support-policy identity shown on the product; if hidden, collect version safely in report rather than asserting a valid build. | **Not installed-tested**; capture actual service result or explicit unavailability |
| 2. verify-account | Follow verified email/account and device linking when the actual PCV-03F service supports it; distinguish offline cached authority from new sign-in. | **Not installed-tested**; capture actual service result or explicit unavailability |
| 3. accept-invite | Inspect inviter, Campaign, proposed Player membership and permissions; accept once; reject stale/wrong-Campaign/replayed invitation. | **Not installed-tested**; capture actual service result or explicit unavailability |
| 4. open-library | Find the approved first-party object and Character without exposing source-only or restricted content; verify permission gate. | **Not installed-tested**; capture actual service result or explicit unavailability |
| 5. join-scene | Open Beacon Debt Gate Pressure as Player; expect only visible facts and no GM-only CF-01..CF-06 until governed reveal. | **Not installed-tested**; capture actual service result or explicit unavailability |
| 6. propose-action | Submit source-owned Player action; observe pending/approval/denial and eventual authoritative event without locally fabricating result. | **Not installed-tested**; capture actual service result or explicit unavailability |
| 7. resume-safely | Disconnect, restart, reconnect and confirm Campaign context and event sequence; report a loss/mismatch, not 'reset account'. | **Not installed-tested**; capture actual service result or explicit unavailability |


### GM — Create and manage only authorized Campaign and Session, invite verified Player, run governed action decisions without leaking GM truth.

| Step | Intended user task | Verification boundary |
|---|---|---|
| 1. identify-and-consent | Confirm current build, GM account/device authority and tester consent before any diagnostics. | **Not installed-tested**; capture actual service result or explicit unavailability |
| 2. create-campaign | Create/open Campaign only on real supported production surface; bind permitted setting, packs and ownership. | **Not installed-tested**; capture actual service result or explicit unavailability |
| 3. invite-player | Invite a distinct verified Player; check one Campaign allowance per Player under verified subscribing GM if product actually supports it, never assume entitlement from mock UI. | **Not installed-tested**; capture actual service result or explicit unavailability |
| 4. prepare-scene | Select Beacon Debt five-scene sequence; inspect hidden clue and roles while verifying Player-safe projection. | **Not installed-tested**; capture actual service result or explicit unavailability |
| 5. adjudicate | Approve/modify/deny proposed Action once; inspect current rules and event receipt, including denial and idempotency. | **Not installed-tested**; capture actual service result or explicit unavailability |
| 6. handoff-and-recover | Exercise current-party handoff/print/spectator only within permissions; no owner transfer or magical revocation of exported pages. | **Not installed-tested**; capture actual service result or explicit unavailability |
| 7. session-closure | Save/rest/reload and compare durable event history; note installed two-human/cross-device proof separately from source demo. | **Not installed-tested**; capture actual service result or explicit unavailability |


### CREATOR — Use authorized creator workspace and reusable definitions without silently publishing canon or transferring restricted derivatives.

| Step | Intended user task | Verification boundary |
|---|---|---|
| 1. identify-role | Confirm verified Creator role/account, current release, allowed workspace and independent Campaign grants. | **Not installed-tested**; capture actual service result or explicit unavailability |
| 2. search-and-select | Find a permitted governed Definition, inspect source/version/rights and identify which assets are not commercial/export-cleared. | **Not installed-tested**; capture actual service result or explicit unavailability |
| 3. create-local | Create Campaign-local or owned content under current scope; never infer canonical-owner rights from edit access. | **Not installed-tested**; capture actual service result or explicit unavailability |
| 4. validate-dependencies | Check species/item/tree/setting dependencies, exact pack versions and Campaign-tainted derivative boundaries. | **Not installed-tested**; capture actual service result or explicit unavailability |
| 5. preview-and-share | Preview permitted content and any intended share target; deny attempts to export restricted or Campaign-licensed derivative content. | **Not installed-tested**; capture actual service result or explicit unavailability |
| 6. return-to-workspace | Resume draft state after navigation/restart where implemented; log missing persistence without inventing a real success. | **Not installed-tested**; capture actual service result or explicit unavailability |
| 7. issue-or-feedback | Create permission-safe proposal/report; inspect data and attachments and confirm before submission/export. | **Not installed-tested**; capture actual service result or explicit unavailability |

## Recovery, permission and usability copy

| Situation | User-facing draft | Fail-closed expected behavior |
|---|---|---|
| RECONNECT | Reconnect to the authorized Campaign and compare the last saved event. If the state differs, report what the app shows without retrying a paid or destructive action. | reopen existing session using current valid authority; no new identity or duplicate event; if service unavailable stop |
| PERMISSION | This content is not available for your current role or Campaign. Ask your GM about permitted access; do not share credentials or hidden notes. | deny and keep private data hidden; report a safe reason code only |
| ALLOWANCE | This Campaign content is not currently unlocked for this account. The GM can check Campaign permissions; access cannot be copied to another Campaign. | verify real GM subscription and one-slot Campaign grant on backend; fail closed |
| RECOVERY | Use the account recovery path. Your Campaign ownership must remain attached to the verified account; changing local device identity alone does not restore it. | subject-preserving recovery only; if identity or ownership cannot be verified stop |
| DIAGNOSTICS | Review the issue details and every attachment before sharing. Remove private campaign content or secrets. Nothing is sent until you confirm. | preview redacted diagnostic manifest, ask explicit consent and preserve stable receipt |
| OFFLINE | Some saved information may be available offline if your authorization is still valid. Changes that require the server may remain unavailable until reconnection. | no entitlement bypass, no fake server-sync success |

### Accessibility requirements to verify later

MTLC-13 source coverage supports keyboard-visible focus/skip links, screen-reader labels, responsive single-column task navigation, 44-pixel touch targets, contrast/motion/text options, and role-filtered printed/one-shot/GM handoff flows. Test both ordinary mobile Phone View and full Desktop View when actual PCV-09 implements it. Gridless semantic descriptions are already supplied in Beacon Debt, but **real Android/Windows accessibility and assistive-technology proof is outstanding**.

### Permission and account boundaries

- A device ID is **not** a substitute for an independently verified account identity. Account recovery must preserve original subject and ownership authority.
- A Player can only access active Campaign content and permitted clues. GM-only truth `CF-01..CF-06` is not Player-visible until governed reveal.
- Any GM-sponsored allowance requires real backend verification, a subscribing GM and **one Campaign-scoped grant per Player**. It cannot export dependent protected material to another Campaign or become universal free access.
- A Creator's right to edit a local resource is not permission to publish canon or commercial/export rights for third-party or Campaign-derived material.
- A spectator/printed snapshot is a dated, role-filtered disclosure; it cannot be retroactively revoked or confer current GM ownership.
- A denied or offline flow must show a usable, plain-language reason without suggesting that the user bypass permissions.

## Consent-controlled issue reporting

The design's required report fields are: `issueReportId`, `reporterSubjectId`, `releaseId`, `roleContext`, `selectedContextType`, `categoryId`, `severityId`, `reproducibility`, `blocksApprovedJourney`, `title`, `expectedResult`, `actualResult`, `reproductionSteps`, `submissionOperationId`, `createdAt`.

The safe diagnostic manifest must expose: `diagnosticBundleId`, `issueDraftId`, `releaseId`, `generatedAt`, `generatorVersion`, `fieldDefinitions`, `includedFields`, `excludedFieldCountByClass`, `redactionCountByClass`, `attachmentIds`, `consentId`, `manifestSha256`.

**Issue creation sequence:** draft locally → choose category/severity → provide reproducible steps and expected/actual results → preview screenshots/attachments and included diagnostic field classes → remove/redact any hidden or sensitive information → explicitly consent → idempotently submit *if* a configured support service exists, or export a portable sanitized package → save the returned stable receipt if available. If either intake or export is absent, keep the issue locally without inventing an upload or receipt.

Never include auth/session tokens, cookies, private GM clues, unrelated Campaign data, raw database dumps, full request bodies, provider credentials or protected creator manuscripts. The source calls for both client-side redaction and server-side validation, rather than trust in a single UI toggle. Issue/report categories and severity classifications are copied in the machine-readable matrix from F025.

## Negative cases to attempt only on appropriate authorized real test installations

| Case | Role | Attempt | Expected protected outcome |
|---|---|---|---|
| XTRA07-P01 | PLAYER | correct invite vs wrong Campaign | authorized membership only; no implicit role change |
| XTRA07-P02 | PLAYER | GM-only clues before discovery | CF-01..CF-06 remain hidden by server before governed reveal |
| XTRA07-P03 | PLAYER | reconnect with stale action receipt | same accepted event, no duplicate resource delta |
| XTRA07-G01 | GM | repeat invitation and same-Campaign Player allowance | one slot only when subscription authority is actually verified; no duplicate grant |
| XTRA07-G02 | GM | approve/modify/deny while Player watches | single server decision and role-safe view, no direct local truth mutation |
| XTRA07-G03 | GM | handoff and private spectator copy | current participant consent/role controls; no broad ownership escalation |
| XTRA07-C01 | CREATOR | imported third-party asset with unknown license | deny redistribution/commercial selection without ARI rights evidence |
| XTRA07-C02 | CREATOR | Campaign-tainted object shared outside Campaign | deny transfer and export of restricted dependencies |
| XTRA07-C03 | CREATOR | attempt canonical promotion from local edit | reject without owning-domain authorization |
| XTRA07-R01 | PLAYER | offline or expired account lease | use only valid cached authority; restricted-content denial if expired/revoked |
| XTRA07-R02 | GM | app restarts before checkpoint | restore authoritative state or explicit recovery failure, no synthetic success |
| XTRA07-R03 | CREATOR | issue export with unauthorized screenshot | preview, redact/remove, require consent before including attachments |

All 12 cases are **NOT_RUN**, not failed or passed.

## Handoff and true-completion gates

- **XTRA-07 can close** once its source-backed guides, consent-safe issue templates and checks are verified/published. No human test evidence is required to assert document readiness, and no actual product usability certificate flows from it.
- **PCV-03F** still owns real service-backed verification, account/device recovery, Campaign invitation/allowance rights and two distinct installed clients.
- **PCV-04/05/09/10 and MTLC-14** still own action/adjudication, current mobile capability parity, visual/assistive technology verification, reconnect and human user-session evaluation.
- **XTRA-06** supplies 45 future PCV acceptance cases and 24 negatives; those results remain NOT_RUN.
- **XTRA-02** remains externally blocked on Render database preservation and the November 8, 2026 deadline; this guide does not remove that infrastructure risk.
- Public distribution, paid billing, silent data collection or generic support access to private records remain outside scope.

This is a source-derived teaching and tester-preparation artifact, not proof that the app presents every described screen or button today.
