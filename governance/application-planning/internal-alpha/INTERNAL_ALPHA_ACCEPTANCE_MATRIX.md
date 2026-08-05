# Internal Alpha Acceptance Matrix

**Program:** MV-IA-001  
**Version:** 0.1.0  
**Status:** DESIGN BASELINE

## 1. Feature-design maturity states

| State | Meaning |
|---|---|
| Registered | Feature has identity, class, owner, scope, and dependencies. |
| Packet in progress | Required design sections are being completed. |
| Implementation-ready | Design packet passes all readiness checks and blocking dependencies are identified. |
| Implemented | Repository code and governed data exist. |
| Validated | Required tests and review pass for the implemented scope. |
| Alpha-ready | Feature is integrated into the approved candidate with recovery, documentation, and no blocking defects. |
| Deferred | Explicitly outside the current scope or full form postponed. |

## 2. Universal feature-design acceptance

Every feature packet must answer all of the following before it becomes implementation-ready.

| Area | Required evidence |
|---|---|
| Identity | Stable feature ID, name, classification, owner, status, version |
| User outcome | Testable result for each supported role |
| Scope | Included alpha slice and explicit exclusions |
| Dependencies | Upstream features, services, packs, schemas, decisions |
| Data | Definitions, placements, instances, live state, events, projections |
| Objects | Stable IDs and canonical object families used |
| Permissions | Role, Campaign, field, search, realtime, export, and AI visibility |
| Entitlements | Access source, restrictions, expiry, historical state |
| Primary flow | Step-by-step successful journey |
| Alternate flow | Legal variations and optional branches |
| Failure flow | Loading, empty, error, forbidden, stale, conflict, recovery |
| Persistence | Draft, authoritative save, history, version, idempotency |
| Reconnect | Behavior before submission, pending, committed, and missed events |
| Accessibility | Keyboard, screen reader, touch, scaling, motion, alternatives |
| Responsive behavior | Desktop, tablet, and mobile information hierarchy |
| Notifications | Trigger, recipient, content, action, resolution |
| AI | None, read-only, proposed, or approval-gated mutation |
| Telemetry | Privacy-safe events, diagnostics, performance and error evidence |
| Tests | Unit, contract, integration, E2E, permission, recovery, accessibility |
| Acceptance | Exact pass conditions and required artifacts |
| Owner review | Whether and when John must approve |
| Implementation handoff | Work type, repositories, files, ports, fixtures, gates |

## 3. Entry-critical feature gate

An entry-critical feature may be marked alpha-ready only when:

- its implementation is merged;
- the approved alpha candidate uses real governed data;
- service-level permissions are enforced;
- save/load works;
- interruption and recovery work;
- desktop and mobile primary paths work;
- keyboard and touch paths work;
- the selected accessibility review passes;
- automated tests pass;
- known limitations are documented;
- no blocking security, privacy, data-integrity, or hidden-information defect remains.

## 4. Alpha-required feature gate

An alpha-required feature may enter the tester program before final closure when its bounded slice is safe and documented. It must become alpha-ready before the internal-alpha program closes.

Required closure evidence:

- complete selected user journey;
- persistent consequence;
- no duplicate or lost state;
- permission-safe projection;
- recovery behavior;
- integration with shared systems;
- defect disposition;
- owner-reviewed result where required.

## 5. Experimental feature gate

An experimental feature requires:

- feature flag or equivalent isolation;
- named tester cohort;
- explicit limitations;
- safe disablement;
- nonexperimental fallback;
- no dependency for core alpha success;
- protected data and permissions;
- cost boundary where AI or providers are involved;
- retained evidence and disposition.

An experiment that becomes necessary for the core journey must be reclassified and pass the stronger gate.

## 6. Deferred feature gate

A deferred feature record must state:

- why it is deferred;
- what narrow slice, if any, remains in alpha;
- dependencies or owner decisions needed;
- earliest reconsideration gate;
- risk of accidental scope creep.

Deferred does not mean forgotten or deleted.

## 7. Journey acceptance matrix

| Journey | Required outcome | Blocking failures |
|---|---|---|
| IA-J01 Player onboarding | Correct Player reaches correct Session with correct Character | Unauthorized access, wrong Campaign, hidden data, unrecoverable invitation or identity path |
| IA-J02 GM preparation | GM builds, saves, previews, and launches a Scene with real objects | Invalid dependencies, failed save, visibility leak, inability to launch |
| IA-J03 Action approval | One proposal receives one attributable durable result | Duplicate Effects, lost command, incorrect result, hidden data leak |
| IA-J04 Combat | Complete encounter without development-only tools | Broken timing, state corruption, unrecoverable encounter, duplicate Resource or Condition changes |
| IA-J05 Assets | Ownership, custody, equipment, and transfers remain correct | Duplication, loss, unauthorized transfer, broken reload |
| IA-J06 Relationship/social | Persistent directional consequence with correct visibility | Hidden motive exposure, lost history, incorrect relationship direction |
| IA-J07 Investigation | Facts, clues, hypotheses, and GM truth remain distinct | GM truth leak, hypothesis promoted as fact, lost evidence |
| IA-J08 Encounter Builder | Valid encounter with source-grounded uncertainty | Invalid dependencies, guaranteed-balance claim, lost configuration |
| IA-J09 Adventure flow | Branch and consequence survive reload | Wrong branch, reset progress, Player sees hidden route state |
| IA-J10 Recovery/support | Safe recovery or reproducible issue | Data loss without warning, secret exposure, unusable diagnostics |
| IA-J11 Creator | Draft content validates and remains noncanonical | Unauthorized promotion, duplicate stable ID, source loss |
| IA-J12 AI | Optional source-linked assistance respects all controls | Hidden data leak, silent mutation, canon promotion, no non-AI fallback |

## 8. Internal-alpha entry acceptance

Internal alpha may begin only when all entry-critical features are alpha-ready and the release-level gates pass:

- exact candidate and commit;
- approved content corpus;
- distinct Player and GM identities;
- authoritative Session loop;
- permissions and hidden-information review;
- backup and restore evidence;
- provider-exit artifact;
- two-device acceptance;
- primary accessibility evidence;
- tester onboarding and issue intake;
- cost and environment disclosure;
- rollback and shutdown plan;
- owner approval.

## 9. Internal-alpha closure acceptance

Internal alpha may close when:

- all entry-critical and alpha-required bounded slices are alpha-ready;
- experimental features have a disposition;
- blocking defects are zero or explicitly owner-held;
- Character, Campaign, Scene, Action, combat, Assets, social or investigation, and recovery journeys pass;
- migration and pack lifecycle preserve tester state;
- security, privacy, accessibility, performance, and cost evidence supports the bounded scope;
- final backup and export are verified;
- owner approves the result and next release stage.

## 10. Feature acceptance record template

```text
Feature ID:
Feature version:
Candidate commit:
Environment:
Classification:
Implementation status:
Design packet digest:
Shared systems used:
Required journeys:
Acceptance criteria:
Test runs:
Permission review:
Accessibility review:
Recovery review:
Known defects:
Limitations:
Owner decision:
Final status:
Evidence locations:
```

## 11. No false completion

The following are insufficient by themselves:

- a mockup;
- a route;
- a component library entry;
- a service port;
- a schema;
- a passing unit test;
- a local happy-path demo;
- a plan;
- an AI statement that work is complete.

Completion requires the evidence defined for the feature's current maturity state.