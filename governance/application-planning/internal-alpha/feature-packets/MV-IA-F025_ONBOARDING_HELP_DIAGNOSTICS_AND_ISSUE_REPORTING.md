# MV-IA-F025 — Onboarding, Help, Diagnostics, and Issue Reporting

**Feature ID:** MV-IA-F025  
**Feature version:** 0.1.0  
**Classification:** entry-critical  
**Design status:** implementation-ready  
**Owner:** John Brandon Turner  
**Primary roles:** invited tester, Player, Game Master, Assistant GM, Content Creator, Observer, Owner/Admin, service actor  
**Stage A mapping:** A12 — Internal-Alpha Hardening, onboarding, help, diagnostics, and feedback  
**Historical module mapping:** none; consolidates tester-support requirements distributed across Stage A and internal-alpha planning  
**Prepared by:** Lead Documentation Architect / Internal-Alpha Support and Diagnostics Steward  
**Reviewed by:** product, UX/accessibility, security, privacy, QA, support, identity, permission, persistence, recovery, telemetry, and documentation roles required before implementation  
**Date:** 2026-08-05

## 1. Problem and user outcome

### Problem

An internal alpha cannot produce trustworthy feedback when invited testers do not know:

- which release they are using;
- which role, Campaign, Character, Scene, or Session context is active;
- which workflows are supported;
- which limitations are intentional;
- whether a failure came from permissions, entitlement, stale state, connectivity, or a defect;
- what evidence is safe and useful to attach;
- how to report a reproducible problem without exposing private notes, GM-only truth, secrets, credentials, or unrelated Campaign data.

Generic help text and unstructured messages are insufficient. Multiversal needs a governed, permission-safe path from invitation through first success, contextual help, diagnostics review, structured issue creation, receipt, follow-up, and resolution.

### Required outcome

An approved tester can:

1. identify the exact release, environment, role, and permitted workspace;
2. follow a role-specific onboarding path into a supported internal-alpha journey;
3. open contextual help that describes the current interface and known limitations;
4. distinguish expected alpha limitations from likely defects;
5. create a structured issue draft with reproducible steps, expected and actual results, severity, and safe context;
6. preview and redact diagnostics before submission or export;
7. submit once or export a portable issue package when no issue service is available;
8. receive a stable receipt and later see a permission-safe status;
9. continue using the product without granting support personnel hidden access.

### Why this belongs in internal alpha

This feature is entry-critical because internal alpha is a controlled evidence-gathering program. Testers must be able to enter the supported path, understand boundaries, identify the running build, and report actionable failures safely. Without this system, defects are hard to reproduce, privacy risks increase, and owner decisions are based on incomplete or ambiguous reports.

## 2. Alpha slice

### Included

- invitation-linked welcome and tester acknowledgement;
- role-specific Player, GM, Assistant GM, creator, observer, and Owner/Admin onboarding paths;
- visible release identity with application version, build or commit identity, environment, schema version, pack-set identity, and support policy;
- a supported-journey checklist and first-success markers;
- contextual help anchored to current route, workspace, role, state, and selected context;
- glossary and “what can I do here?” guidance;
- known limitations, experimental-feature labels, and unavailable-feature explanations;
- connection, save, permission, entitlement, conflict, and recovery help;
- structured issue categories, severity, reproducibility, expected result, actual result, and steps;
- optional screenshots and text attachments with preview and removal;
- permission-safe diagnostic manifest;
- explicit consent before diagnostic attachment;
- client-side redaction and server-side revalidation;
- stable issue draft, report, attachment, diagnostic bundle, and receipt IDs;
- idempotent submission;
- portable issue export when no issue intake service is configured;
- bounded issue-status projection and follow-up notification;
- accessibility, responsive, offline-draft, reconnect, and recovery behavior;
- deterministic fixtures and denied-case tests.

### Explicitly excluded

- public registration or public support access;
- public knowledge base;
- production service-level agreements;
- paid crash analytics, ticketing, product analytics, or remote-support services;
- silent background recording;
- automatic upload of logs, screenshots, files, or Campaign content;
- remote screen control;
- blanket Owner/Admin or support access to private or GM-only information;
- AI-required triage;
- automatic canonical promotion of tester suggestions;
- automatic issue creation without user review;
- public release notes or App Store support workflow;
- broad device forensics.

### Full long-term scope deferred

Later releases may add public documentation, localized help, richer support queues, moderated community support, paid-provider adapters, crash-symbolication services, automated duplicate suggestions, AI-assisted triage, and production support metrics. Those additions require separate provider, spending, privacy, security, accessibility, legal, and owner decisions.

## 3. Roles and authority

| Role | Allowed actions | Hidden information | Approval required |
|---|---|---|---|
| Invited tester | acknowledge alpha terms, follow assigned onboarding, open help, create issue drafts, preview diagnostics, submit or export reports | only information already authorized to the tester | consent required before attachments or diagnostics are included |
| Player | receive Player-specific guidance and report Player-visible failures | no GM-only truth, other Player-private notes, security data, or unrelated Campaign data | explicit confirmation before submission |
| Game Master | receive GM-specific guidance and report GM-visible failures | may include GM-visible data from the active Campaign only; cannot include secrets or unrelated Campaigns | explicit confirmation before submission |
| Assistant GM | receive delegated guidance and report within delegated scope | no information beyond active delegation | explicit confirmation before submission |
| Content Creator | receive creator-workflow guidance and report creator-visible failures | no Campaign data unless separately authorized | explicit confirmation before submission |
| Observer | receive observer guidance and report observer-visible failures | no hidden participant data | explicit confirmation before submission |
| Owner/Admin | manage approved alpha release identity, onboarding definitions, known limitations, issue taxonomy, and permission-safe issue status | no automatic access to private content; support access remains separately authorized and audited | owner authority required for policy, release, provider, and retention changes |
| Service actor | generate manifests, redact configured classes, store authorized reports, issue receipts, and deliver bounded status | may process only fields authorized by service policy | service credentials and environment authorization required |
| AI | optional read-only wording or duplicate suggestion after permission filtering | no additional retrieval authority | proposed output only; user review required |

Support personnel never gain data access merely because a report exists.

## 4. Dependencies

### Feature dependencies

- MV-IA-F001 — Application Shell and Workspace Navigation
- MV-IA-F003 — Identity, Dashboard, and Workspace Selection
- MV-IA-F020 — Permissions and Hidden Information
- MV-IA-F021 — Autosave, Reconnect, Recovery, and Bounded Offline Use
- MV-IA-F022 — Accessibility and Adaptive Interface, as a cross-cutting implementation dependency

### Shared systems

- SS-001 application shell and workspace navigation
- SS-002 identity, role, and selected-context presentation
- SS-003 permission-safe projection
- SS-004 notifications and queues
- SS-005 autosave and draft recovery
- SS-006 error, stale, offline, conflict, and recovery states
- SS-007 release identity and environment labeling
- SS-008 telemetry, correlation, and diagnostic redaction
- SS-009 accessibility and responsive primitives
- SS-010 portable export and checksum receipts

### Service ports and adapters

- IdentityPort
- EntitlementPort
- PersistencePort
- RealtimePort for bounded issue-status notifications
- ObjectStoragePort for approved attachments
- TelemetryPort
- IssueIntakePort
- DiagnosticManifestPort
- ReleaseIdentityPort
- NotificationPort
- ExportPort

Every port requires a zero-paid-service local adapter for alpha development and contract testing.

### Canonical objects and packs

- active release identity;
- installed pack-set manifest;
- role-specific onboarding definitions;
- help-topic definitions;
- glossary terms;
- known limitation records;
- feature-status and experimental labels;
- issue taxonomy and severity definitions;
- approved alpha content and fixture identities.

### Schemas and migrations

- OnboardingGuideDefinition
- HelpTopicDefinition
- KnownLimitationDefinition
- ReleaseIdentity
- OnboardingProgress
- IssueDraft
- IssueReport
- IssueAttachment
- DiagnosticBundleManifest
- IssueReceipt
- IssueStatusProjection
- SupportPolicy
- export manifest and checksums

Migrations preserve report identity, original release identity, classifications, consent, attachment history, and status history.

### Decisions and gates

- active P9-06 sequence;
- permission, hidden-information, persistence, recovery, backup, restore, and provider-exit gates;
- approved internal-alpha fixture and tester policy;
- owner approval before paid support, analytics, storage, or ticketing providers;
- owner approval before internal-alpha release;
- privacy and security review before collecting real tester diagnostics.

## 5. Object and state model

### Reusable Definitions

- `OnboardingGuideDefinition`
- `OnboardingStepDefinition`
- `HelpTopicDefinition`
- `GlossaryEntryDefinition`
- `KnownLimitationDefinition`
- `IssueCategoryDefinition`
- `SeverityDefinition`
- `DiagnosticFieldDefinition`
- `SupportPolicyDefinition`

Definitions are versioned, source-linked, and role-scoped.

### Campaign placements or bindings

- Campaign-specific help overrides;
- approved Campaign support contacts;
- alpha fixture references;
- feature flags and experimental labels;
- Campaign-safe issue categories;
- Campaign-specific known limitations.

Bindings cannot broaden access beyond the governing definitions and permission policy.

### Live instances and state

- `OnboardingProgress`
- `HelpContext`
- `IssueDraft`
- `IssueReport`
- `IssueAttachment`
- `DiagnosticBundleManifest`
- `DiagnosticConsent`
- `IssueReceipt`
- `IssueStatusProjection`
- `FollowUpRequest`
- `SupportAccessRequest`

### Events and history

- `OnboardingStarted`
- `OnboardingStepCompleted`
- `OnboardingReset`
- `HelpOpened`
- `KnownLimitationViewed`
- `IssueDraftCreated`
- `IssueDraftAutosaved`
- `DiagnosticPreviewGenerated`
- `DiagnosticFieldRemoved`
- `DiagnosticConsentGranted`
- `DiagnosticConsentWithdrawn`
- `IssueSubmitted`
- `IssueSubmissionRejected`
- `IssueExported`
- `IssueReceiptIssued`
- `IssueStatusChanged`
- `FollowUpRequested`
- `FollowUpAnswered`
- `IssueClosed`
- `SupportAccessRequested`
- `SupportAccessApproved`
- `SupportAccessRevoked`

History is append-only for submitted reports. Corrections create new Events instead of silently rewriting original evidence.

### Projections and indexes

- onboarding progress by subject and role;
- help topics by route, workspace, state, and feature;
- active known limitations by release;
- issue drafts by subject;
- submitted issues by reporter and permitted support scope;
- issue status by receipt;
- diagnostics fields by classification and consent;
- release identity by environment and build;
- duplicate-suggestion index over redacted nonsecret metadata only.

### Stable IDs

Required IDs include:

- `guideId`
- `stepId`
- `helpTopicId`
- `limitationId`
- `releaseId`
- `buildId`
- `onboardingProgressId`
- `issueDraftId`
- `issueReportId`
- `attachmentId`
- `diagnosticBundleId`
- `consentId`
- `submissionOperationId`
- `issueReceiptId`
- `followUpId`
- `supportAccessRequestId`
- `correlationId`

Email, display name, route label, issue title, device name, and provider ticket number are not stable internal identities.

### Provenance

Every help topic and known limitation records:

- source;
- version;
- applicable release range;
- applicable roles and workspaces;
- author;
- reviewer;
- status;
- supersession.

Every report records the release identity, permission-safe selected context, user-provided evidence, generated diagnostics, redactions, consent, and receipt.

## 6. Primary user flow

1. An invited tester enters through MV-IA-F003.
2. The server resolves identity, invitation, role, entitlements, permissions, selected context, and release identity.
3. The application presents the assigned onboarding guide and clear alpha boundary.
4. The tester acknowledges the current release and known limitations.
5. The guide leads to one role-specific first-success journey.
6. Progress autosaves through MV-IA-F021.
7. Contextual help remains available from the shell and current error or recovery state.
8. When a problem occurs, the tester opens Report a Problem from the current context.
9. The reporter chooses category, severity, reproducibility, and whether the issue blocks progress.
10. The reporter records expected result, actual result, and minimal reproduction steps.
11. The system creates a permission-safe diagnostic preview.
12. The reporter inspects every attachment and diagnostic group, removes unwanted items, and grants explicit consent.
13. The server revalidates identity, selected context, permissions, and classifications.
14. The report submits idempotently or exports as a portable package when no issue service is available.
15. The reporter receives a stable receipt containing release identity and report status.
16. A bounded notification reports future status or follow-up without exposing support-only information.

## 7. Alternate and secondary flows

### Alternate flow A — issue during authentication or workspace entry

1. The user cannot enter the intended workspace.
2. A safe pre-workspace reporter records invitation or sign-in state without enumerating hidden Campaigns.
3. Diagnostics include only user-safe identity-session reason codes, release identity, correlation ID, and client environment.
4. The user submits or exports the report.
5. The report never includes protected workspace data.

### Alternate flow B — offline issue draft

1. Connectivity is unavailable.
2. The reporter creates and autosaves an issue draft locally.
3. The interface marks it `local-only-not-submitted`.
4. Screenshots and diagnostics remain local and reviewable.
5. On reconnect, permissions and context are revalidated.
6. The user explicitly submits or exports; no automatic upload occurs.

### Alternate flow C — crash or unrecoverable screen

1. Recovery UI loads from the shell.
2. It displays release identity and a safe recent operation reference.
3. The user creates an issue from the recovery state.
4. The system includes only previously approved local diagnostic fields.
5. The user previews and submits or exports.

### Alternate flow D — known limitation match

1. Contextual help identifies a current known limitation.
2. The user sees the limitation, workaround, affected release range, and issue-report option.
3. The limitation view never suppresses reporting.
4. The report records that the limitation was shown.

### Alternate flow E — follow-up request

1. Authorized support changes status to `needs-information`.
2. The reporter receives a bounded notification.
3. The reporter opens the original receipt and sees a permission-safe question.
4. New evidence uses the same preview, consent, redaction, and idempotency rules.
5. The original report remains immutable.

### Alternate flow F — no configured issue backend

1. The local IssueIntakePort reports `export-only`.
2. The user completes the normal issue workflow.
3. The system creates a portable package with manifest and checksums.
4. The package excludes secrets and unauthorized data.
5. The user receives clear instructions for the approved transfer path.

## 8. Failure, empty, and recovery states

| State | User sees | Allowed action | Preserved data | Evidence |
|---|---|---|---|---|
| Loading | release and guide loading state | wait, retry, return safely | current route and draft | correlation ID |
| Empty | no assigned onboarding or contextual topic | open general quickstart, glossary, or report configuration issue | selected context | release ID |
| Validation error | exact missing or invalid report fields | correct fields | complete issue draft | field reason codes |
| Forbidden | generic unavailable message | return, open safe help, report access problem | no hidden target data | safe permission reason |
| Restricted entitlement | explanation without protected preview | return or request approved Campaign help | issue draft | entitlement reason |
| Offline | offline badge and local-draft label | continue allowed drafting, preview local evidence, export when supported | local draft and attachments | offline state |
| Stale | release, guide, context, or permission changed | refresh and review changes | draft preserved | stale reason and versions |
| Conflict | authoritative report or draft changed elsewhere | compare safe versions, copy, discard, or retry | both safe versions | conflict ID |
| Failed save | draft not durably saved | retry, copy text, export draft | in-memory and last local autosave | operation ID |
| Submission ambiguous | report may have reached server | check status by submission operation ID | report draft | status lookup |
| Attachment rejected | file type, size, malware, classification, or permission failure | remove or replace | report draft | safe rejection code |
| Diagnostic generation failed | partial or no diagnostics | submit without diagnostics or retry | user-entered report | manifest failure reason |
| Consent missing | clear pre-submit warning | review and consent or remove data | report draft | consent state |
| Revoked | access changed | preserve local text, remove protected cached context, sign in or return | user-authored safe text | revocation receipt |
| Recovery required | interrupted issue workflow | restore authorized draft or start a new report | safe autosave only | recovery receipt |

No state may silently submit evidence, broaden support access, or discard user-authored reproduction steps.

## 9. Permissions and hidden information

### Authorization questions

- Who may see each onboarding guide, help topic, limitation, issue draft, issue report, attachment, diagnostic field, receipt, and status?
- Is the reporter authorized for the active role, Campaign, Character, Scene, Session, or creator scope?
- Does the diagnostic manifest reveal hidden IDs, aliases, counts, object relationships, GM truth, Player-private notes, security state, secrets, or unrelated Campaign data?
- Are help search, suggestions, counts, and empty states filtered before pagination?
- Is a support or Owner/Admin viewer explicitly authorized for the report scope?
- Has support access been separately requested, approved, time-bounded, and audited?
- Are permissions rechecked at diagnostic preview, submission, attachment retrieval, status view, follow-up, export, and deletion or retention actions?
- Does revocation invalidate cached help context, report status, attachments, and support access immediately?

### Required denied-case tests

- Player diagnostics exclude GM-only Scene truth.
- GM diagnostics exclude unrelated Campaign data.
- Reporter cannot attach another subject's private notes.
- Observer cannot infer hidden participants through help or issue facets.
- Creator cannot see Campaign issue reports without Campaign authority.
- Support cannot open a report outside assigned scope.
- Owner/Admin cannot use issue existence as blanket content access.
- Revoked subject cannot retrieve attachments or report status.
- Deep link to another report returns safe not-found-or-unavailable.
- Help search does not reveal hidden feature availability.
- Diagnostic manifest excludes access tokens, secrets, cookies, credentials, raw authorization headers, and private keys.
- Logs are redacted before client preview.
- Screenshot attachment requires explicit selection and preview.
- Automatic full-screen capture is prohibited.
- Issue export excludes unauthorized cached data.
- Offline drafts cannot retain protected data after revocation.
- Follow-up cannot request secret or credential material.
- AI duplicate suggestion cannot retrieve hidden issue bodies.
- Counts and duplicate suggestions cannot enumerate protected issues.
- Service actor cannot bypass subject and Campaign scope.
- Attachment object storage denies guessed IDs.
- Status notification contains no protected issue content.
- Release identity shows no secret deployment metadata.
- Rejected submission does not leave an orphaned accessible attachment.

## 10. Entitlements

- **Access sources:** approved invitation, role, Campaign membership, Owner/Admin policy, and explicit support assignment.
- **Free-tier behavior:** safety help, release identity, error explanations, and issue reporting remain available to approved testers regardless of content tier.
- **Campaign grants:** may expose help for granted content but do not expose the content itself through diagnostics.
- **Sponsored access:** follows the current entitlement decision and expiration rules.
- **Expiry behavior:** help falls back to safe general guidance; protected report context and attachments are reauthorized.
- **Historical-state behavior:** a report retains the original entitlement decision metadata without preserving access to content that is no longer authorized.
- **Search and preview restrictions:** contextual help and issue suggestions cannot preview restricted content.
- **Offline snapshot behavior:** only previously authorized help and user-authored issue drafts may persist within the bounded offline policy.

Issue reporting cannot be used as a content-entitlement bypass.

## 11. Persistence and history

- **Draft storage:** local encrypted or platform-appropriate storage under MV-IA-F021 policy, partitioned by stable subject and selected context.
- **Authoritative save:** submitted issue reports, manifests, consent, attachment metadata, receipts, status history, and follow-up Events.
- **Aggregate boundary:** `IssueReport` owns its submitted evidence and status history; attachments and manifests remain separately addressable but report-bound.
- **Expected-version behavior:** update and follow-up commands use expected versions.
- **Idempotency:** `submissionOperationId` returns the prior receipt for identical retries and rejects changed payloads under the same key.
- **Event types:** the Events listed in Section 5 are durable.
- **Snapshot or checkpoint behavior:** support indexes may be rebuilt from issue Events; original evidence and consent are not projection-only.
- **Audit events:** diagnostic generation, field removal, consent, submission, attachment access, status change, follow-up, export, retention, support access, and revocation.
- **Migration behavior:** preserve original release identity, reporter, consent, classifications, checksums, and history.
- **Export behavior:** portable UTF-8 JSON and approved attachment formats with manifest, schema versions, stable IDs, classifications, and SHA-256 checksums.

Deleted or expired attachments retain an auditable tombstone where policy requires without retaining the removed bytes.

## 12. Realtime, interruption, and reconnect

- **Before local submission:** the issue draft remains local and editable.
- **After submission but before acceptance display:** client queries by `submissionOperationId`; it does not create a new report.
- **After acceptance but before display:** the existing receipt is recovered.
- **During diagnostic generation:** partial manifests are invalid; retry creates a new manifest version.
- **During attachment upload:** incomplete uploads remain inaccessible and expire safely.
- **During a pending follow-up:** status and question recover from authoritative state.
- **After missed Events:** status projection resumes from the last acknowledged report Event sequence.
- **With a stale client:** release, schema, permission, and issue versions are revalidated.
- **From a second device:** authoritative drafts and submitted reports are shown only after authorization; local-only drafts remain device-local unless explicitly exported.
- **After service restart:** report Events, receipts, manifests, and finalized attachments recover from durable persistence.
- **After revocation:** protected diagnostics, attachments, issue bodies, and status are removed from projection and cache.

Realtime is advisory. Persistence is authoritative.

## 13. Interface and information hierarchy

### Desktop

The shell provides:

- release identity;
- onboarding progress;
- contextual help panel;
- known limitations;
- report-a-problem action;
- structured issue editor;
- diagnostic preview with grouped fields and removal controls;
- attachment list;
- consent summary;
- submission or export action;
- receipt and status history.

Diagnostics remain secondary to user-authored reproduction steps.

### Tablet

Use a focused editor with drawers for help, diagnostics, and attachments. Preserve the current issue draft when switching panels. Do not require hover.

### Mobile

Use a single-column stepper:

1. describe;
2. reproduce;
3. review context;
4. review attachments;
5. consent;
6. submit or export;
7. receipt.

Critical release identity, draft state, connection state, and submission status remain visible.

### Player hierarchy

Foreground:

- current release;
- supported Player task;
- clear next action;
- help for the current state;
- issue title, steps, expected result, actual result;
- safe diagnostic preview.

Keep raw logs, IDs, and technical detail behind expandable sections.

### GM hierarchy

Foreground:

- current Campaign and Session scope;
- whether the issue affects Players, GM-only state, or Session continuity;
- active release and pack-set identity;
- exact operation, command, Event, or recovery receipt references;
- protected-field warnings before attachment.

GM-only visibility never removes the need for explicit evidence review.

## 14. Accessibility

- semantic heading, landmark, form, fieldset, list, status, and dialog structure;
- complete keyboard operation;
- logical focus order and focus restoration;
- screen-reader names for release identity, guide progress, help context, attachments, diagnostics, consent, and report status;
- polite announcements for autosave and connection changes;
- assertive announcements only for submission failure, revocation, destructive removal, or unrecoverable state;
- scalable text without loss of actions;
- contrast and noncolor state indicators;
- reduced-motion support;
- minimum touch targets;
- nondrag attachment ordering and removal;
- no graph-only or map-only support information;
- error summary with links to invalid fields;
- accessible diagnostic table and plain-language alternative;
- no timed onboarding completion requirement;
- user can pause and resume without losing progress.

## 15. Notifications and queues

| Trigger | Recipient | Message content | Action | Resolution state |
|---|---|---|---|---|
| onboarding assigned | tester | release and role-specific start | begin | started/completed |
| known limitation updated | affected authorized tester | bounded title and affected feature | review | acknowledged |
| issue submitted | reporter | receipt ID and safe summary | open receipt | received |
| issue needs information | reporter | safe question and due policy, if any | answer | pending/responded |
| issue status changed | reporter | status only plus safe note | open receipt | acknowledged |
| attachment rejected | reporter | user-safe reason | replace/remove | resolved |
| support access requested | data owner or authorized approver | scope, purpose, duration | approve/deny | approved/denied/expired |
| alpha release changed | approved testers | new release identity and restart guidance | review | acknowledged |

Notifications never include private report content on lock screens or untrusted channels.

## 16. AI involvement

**AI mode:** none for core operation; optional read-only or proposed assistance only

- **Allowed action:** suggest clearer reproduction wording, summarize user-selected evidence, or suggest possible duplicates over permission-safe redacted metadata.
- **Allowed sources:** current user-authored draft, approved help topics, known limitations, and authorized redacted issue metadata.
- **Permission and entitlement checks:** identical to non-AI access; AI receives no broader retrieval.
- **Provenance:** suggestions identify sources and remain visibly proposed.
- **Uncertainty:** required for duplicate or cause suggestions.
- **Cost boundary:** zero AI is the required internal-alpha baseline.
- **Non-AI fallback:** complete onboarding, help, diagnostics, export, submission, and status workflow.
- **Prohibited behavior:** automatic submission, automatic severity reduction, hidden issue retrieval, secret collection, canonical promotion, support-access approval, or user impersonation.

## 17. Telemetry and diagnostics

Required privacy-safe fields may include:

- release ID;
- application version;
- build or commit ID;
- environment classification;
- schema and migration versions;
- pack-set digest;
- route and feature ID;
- stable operation, command, Event, checkpoint, recovery, and correlation IDs;
- selected-context type and safe stable IDs only when authorized;
- client platform, browser or shell version, viewport class, locale, and accessibility preferences;
- connection state and last acknowledged Event sequence;
- save, submission, reconnect, and recovery result codes;
- performance durations;
- user-selected log excerpts;
- redaction counts and categories;
- diagnostic manifest checksum.

Always excluded:

- passwords;
- access or refresh tokens;
- cookies;
- credentials;
- private keys;
- raw authorization headers;
- payment data;
- unrelated Campaign state;
- unselected private notes;
- unselected GM truth;
- raw database dumps;
- full filesystem inventories;
- precise location unless separately required and approved;
- uncontrolled microphone, camera, or screen recording.

Issue-report attachments and diagnostics are opt-in and previewable.

## 18. Test scenarios

### Unit

- guide selection by role and release;
- help-topic resolution;
- limitation applicability;
- issue validation;
- severity and category rules;
- redaction;
- manifest checksums;
- consent state;
- idempotent submission;
- safe reason mapping.

### Contract

- ReleaseIdentityPort;
- IssueIntakePort;
- DiagnosticManifestPort;
- ObjectStoragePort;
- NotificationPort;
- ExportPort;
- provider-neutral stable errors;
- zero-service local adapters.

### Integration

- identity, permission, entitlement, selected context, help, report, attachment, receipt, status, and export;
- release and pack-set changes;
- support assignment and revocation;
- attachment quarantine and expiration.

### End-to-end

- invited Player completes onboarding and reports an Action failure;
- invited GM reports a Scene or Session failure with GM-safe context;
- pre-workspace sign-in failure report;
- offline draft then reconnect and submit;
- export-only issue package;
- follow-up and closure;
- release update requiring acknowledgement.

### Permission and hidden information

- all denied cases in the companion matrix;
- no hidden counts, aliases, exact IDs, attachments, notifications, or duplicate suggestions;
- support access is separate, bounded, and auditable.

### Entitlement

- safety help remains available;
- restricted content does not appear through help or diagnostics;
- expired access revalidates report views.

### Persistence and migration

- draft recovery;
- idempotent submission;
- report history;
- manifest and attachment migration;
- portable export and reimport validation;
- retention tombstones.

### Reconnect and recovery

- ambiguous submission;
- missed status Event;
- service restart;
- stale release;
- stale permission;
- second device;
- revoked role;
- interrupted attachment upload.

### Accessibility

- keyboard-only onboarding and issue submission;
- screen-reader release identity, help, diagnostics, consent, errors, and receipt;
- touch, text scaling, contrast, reduced motion, and responsive layouts.

### Performance

- contextual help opens within the approved UI budget;
- report editor remains responsive with maximum alpha attachments;
- diagnostic preview remains bounded;
- submission does not block draft preservation;
- export completes within the approved fixture budget.

### Golden or deterministic regression

- [x] 8D-007J does not govern issue-triage semantics directly.
- [x] Deterministic contract fixtures and checksums are required for manifests, exports, redaction, release identity, and idempotency.

## 19. Acceptance criteria

1. **Criterion ID:** OHD-AC-001  
   **Condition:** An invited tester sees the exact release identity, environment classification, assigned role, and safe selected context before beginning the supported journey.  
   **Evidence:** two-role entry test and release-identity fixture.  
   **Blocking:** yes

2. **Criterion ID:** OHD-AC-002  
   **Condition:** Role-specific onboarding leads a Player and a GM through distinct supported first-success paths without exposing hidden workspaces.  
   **Evidence:** Player/GM end-to-end onboarding tests.  
   **Blocking:** yes

3. **Criterion ID:** OHD-AC-003  
   **Condition:** Contextual help resolves by route, feature, role, state, and release and falls back safely when no exact topic exists.  
   **Evidence:** help-resolution contract tests.  
   **Blocking:** yes

4. **Criterion ID:** OHD-AC-004  
   **Condition:** Known limitations identify affected releases, workflows, workarounds, status, and supersession without preventing issue creation.  
   **Evidence:** limitation lifecycle fixtures.  
   **Blocking:** yes

5. **Criterion ID:** OHD-AC-005  
   **Condition:** A tester can create, autosave, reload, and continue a structured issue draft.  
   **Evidence:** local and authoritative draft recovery tests.  
   **Blocking:** yes

6. **Criterion ID:** OHD-AC-006  
   **Condition:** The issue schema captures category, severity, reproducibility, blocker state, expected result, actual result, and ordered reproduction steps.  
   **Evidence:** schema and invalid-fixture tests.  
   **Blocking:** yes

7. **Criterion ID:** OHD-AC-007  
   **Condition:** The diagnostic preview is generated from an allowlist, grouped by classification, and visible before submission.  
   **Evidence:** manifest and UI tests.  
   **Blocking:** yes

8. **Criterion ID:** OHD-AC-008  
   **Condition:** Secrets, credentials, tokens, raw authorization headers, and unrelated Campaign data never appear in the diagnostic manifest, attachment preview, export, or submission.  
   **Evidence:** redaction and denied-case suite.  
   **Blocking:** yes

9. **Criterion ID:** OHD-AC-009  
   **Condition:** Screenshots, logs, and other attachments require explicit user selection, preview, removal capability, and consent.  
   **Evidence:** attachment consent end-to-end test.  
   **Blocking:** yes

10. **Criterion ID:** OHD-AC-010  
    **Condition:** Submission revalidates identity, selected context, permissions, entitlements, release, classifications, and attachment access.  
    **Evidence:** stale and revoked submission tests.  
    **Blocking:** yes

11. **Criterion ID:** OHD-AC-011  
    **Condition:** Retrying the same submission operation returns the original receipt and does not create a duplicate report.  
    **Evidence:** idempotency contract test.  
    **Blocking:** yes

12. **Criterion ID:** OHD-AC-012  
    **Condition:** Ambiguous connection failure resolves by submission-operation lookup without asking the user to resubmit blindly.  
    **Evidence:** interruption test.  
    **Blocking:** yes

13. **Criterion ID:** OHD-AC-013  
    **Condition:** When no issue backend is configured, the system produces a portable redacted issue package with manifest and checksums.  
    **Evidence:** export-only adapter test.  
    **Blocking:** yes

14. **Criterion ID:** OHD-AC-014  
    **Condition:** A receipt identifies the report, release, submission time, safe summary, and current status without exposing support-only information.  
    **Evidence:** receipt projection test.  
    **Blocking:** yes

15. **Criterion ID:** OHD-AC-015  
    **Condition:** Issue status and follow-up notifications are permission-safe and survive disconnect, reconnect, and service restart.  
    **Evidence:** realtime and persistence tests.  
    **Blocking:** yes

16. **Criterion ID:** OHD-AC-016  
    **Condition:** Creating or viewing a report never grants support, Owner/Admin, service, or AI access to the underlying Campaign content.  
    **Evidence:** support-access and denied-case suite.  
    **Blocking:** yes

17. **Criterion ID:** OHD-AC-017  
    **Condition:** Revocation removes protected issue bodies, attachments, diagnostics, help context, and status from cache and future projections while preserving authorized user-authored safe text where policy permits.  
    **Evidence:** revocation and offline-cache test.  
    **Blocking:** yes

18. **Criterion ID:** OHD-AC-018  
    **Condition:** The complete Player and GM onboarding, help, report, diagnostic-review, consent, submission or export, and receipt flows are keyboard-, touch-, and screen-reader-operable.  
    **Evidence:** accessibility test matrix and manual review.  
    **Blocking:** yes

19. **Criterion ID:** OHD-AC-019  
    **Condition:** Core onboarding, help, diagnostics, issue export, and local issue intake work with zero AI and zero paid support, analytics, crash-reporting, or ticketing services.  
    **Evidence:** zero-service environment test.  
    **Blocking:** yes

20. **Criterion ID:** OHD-AC-020  
    **Condition:** Export and provider-exit artifacts preserve stable IDs, release identity, schemas, consent, classifications, report history, attachment metadata, manifests, and checksums.  
    **Evidence:** provider-exit round-trip test.  
    **Blocking:** yes

## 20. Fixtures and approved alpha content

- **Required identities:** invited Player, GM, Assistant GM, creator, observer, Owner/Admin, support service actor, revoked tester.
- **Required Campaign:** bounded alpha Campaign with Player-safe, GM-only, Player-private, and unrelated-Campaign data.
- **Required Characters:** controlled Player Character, uncontrolled Character, archived Character.
- **Required packs:** pinned alpha pack set, outdated pack set, missing optional pack, changed pack-set digest.
- **Required objects:** onboarding guides, help topics, glossary entries, limitations, release identities, issue categories, severities, support policies.
- **Required hidden information:** GM Scene truth, private notes, secret IDs, protected issue, attachment, hidden participant, unrelated Campaign.
- **Required historical state:** prior release, superseded limitation, reopened issue, closed issue, migrated report, expired support access.
- **Required failure fixtures:** offline, stale release, stale permission, expired invitation, rejected attachment, diagnostic failure, ambiguous submission, service restart, export-only adapter, revocation.

## 21. Security, privacy, cost, and risk

### Security

- allowlisted diagnostic fields;
- denylisted secret patterns;
- permission checks before preview, submission, retrieval, export, and follow-up;
- attachment size, type, archive, malware, and path validation;
- unguessable stable IDs;
- quarantined incomplete uploads;
- rate limiting;
- no raw credentials in logs;
- support-access separation;
- audit of attachment and diagnostic access;
- signed or checksummed portable exports.

### Privacy

- data minimization;
- explicit preview and consent;
- no silent recording;
- no automatic screenshot;
- purpose and retention shown before submission;
- field classification and redaction;
- right to remove draft attachments;
- submitted-evidence correction by append-only follow-up;
- no unrelated Campaign data;
- no blanket Owner/Admin access;
- approved retention and deletion policy required before real alpha.

### Cost

- zero paid service required;
- local or repository-backed issue intake supported;
- bounded attachment size and retention;
- diagnostics use existing provider-neutral telemetry;
- no automatic AI calls;
- owner approval before paid ticketing, analytics, crash reporting, storage, or notification adapters.

### Material risks

- hidden-information leakage through logs or screenshots;
- collection of secrets or credentials;
- support access expanding silently;
- reports lacking reproducible evidence;
- issue duplication after ambiguous failure;
- unbounded attachment cost;
- misleading known limitations;
- inaccessible help or reporting;
- issue intake becoming a content-entitlement bypass;
- overclaiming production support readiness.

### Stop conditions

- diagnostic field cannot be classified or redacted;
- attachment storage cannot enforce report scope;
- support access is not separately authorized and audited;
- provider requires paid enrollment or production credentials;
- retention or privacy policy is unresolved for real tester data;
- issue export cannot exclude secrets and unauthorized data;
- implementation would bypass P9-06 dependencies;
- internal-alpha release approval is absent.

## 22. Owner review points

- **Design approval required:** owner may review scope before implementation work orders are opened.
- **Scope decision required:** real alpha retention period, attachment limits, supported issue categories, support roles, and experimental help.
- **Canon decision required:** none; tester reports and suggestions are not canon.
- **Spending or provider decision required:** any paid ticketing, analytics, crash reporting, storage, notification, AI, or support provider.
- **Alpha release decision required:** exact tester cohort, support policy, retention, release identity, known limitations, and issue intake path.

Silence is not approval.

## 23. Implementation handoff

**Target repository:** `cybalicistjt-stack/Multiversal-app` after dependency gates are ready  
**Registered work type:** application vertical slice / internal-alpha hardening / support and diagnostics  
**Decision level:** A2 for bounded implementation; A3 for providers, retention policy, real tester data, production credentials, spending, or release  
**Risk class:** medium-high because diagnostics and attachments can expose protected information  
**Suggested work-order title:** Implement MV-IA-F025 Onboarding, Help, Diagnostics, and Issue Reporting  
**Expected branches or files:** shared contracts, local adapters, issue intake and diagnostic services, UI routes/components, schemas/migrations, fixtures, tests, documentation, and provider-exit export  
**Required reviewers:** architecture, security, privacy, permissions, identity, persistence, recovery, UX/accessibility, QA, support operations, documentation  
**Required gates:** permission/hidden-information, identity/context, persistence, recovery, attachment security, privacy, accessibility, zero-service, export/provider-exit, internal-alpha acceptance  
**Rollback or recovery:** disable report submission while retaining safe local drafts and export; preserve submitted evidence and receipts; revoke support access; quarantine attachments; restore from verified backup  
**Evidence outputs:** contract tests, denied-case suite, redaction fixtures, accessibility evidence, two-role journey, interruption tests, export package, checksums, security/privacy review, PR, CI, merge commit

Implementation decomposition:

1. schemas and shared types;
2. release identity and help-definition ports;
3. local help and issue-intake adapters;
4. permission-safe diagnostic-manifest service;
5. redaction and classification;
6. issue drafts and autosave;
7. attachment quarantine and approved storage;
8. idempotent submission and receipt;
9. status and follow-up;
10. portable export;
11. role-specific onboarding UI;
12. contextual help UI;
13. issue editor and diagnostic preview;
14. accessibility and responsive behavior;
15. fixtures, denied cases, interruption tests, security and privacy evidence.

Application implementation remains dependency-gated by the active P9-06 sequence.

## 24. Readiness decision

- [x] All required sections complete.
- [x] Dependencies identified.
- [x] Shared-system impacts identified.
- [x] Permissions complete.
- [x] Persistence and recovery complete.
- [x] Accessibility complete.
- [x] Tests and acceptance criteria measurable.
- [x] Explicit exclusions complete.
- [x] Owner decisions identified.
- [x] Implementation handoff complete.

**Final design status:** implementation-ready  
**Reviewer:** repository validation and independent specialist review required before implementation  
**Date:** 2026-08-05  
**Packet digest:** generated from the merged canonical artifact; no self-referential digest is embedded
