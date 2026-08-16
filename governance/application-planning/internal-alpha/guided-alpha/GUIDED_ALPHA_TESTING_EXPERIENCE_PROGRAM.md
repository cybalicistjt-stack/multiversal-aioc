# Guided Alpha Testing Experience Program

**Program ID:** GATX  
**Status:** ACTIVE — OWNER APPROVED  
**Owner/final authority:** John Brandon Turner  
**Activated:** 2026-08-16  
**Parent context:** Internal Alpha / IA-D09 tester execution  
**Highest completed tranche:** GATX-T01  
**Active prerequisite:** GATX-DIAG-F01 — Automatic diagnostics foundation  
**Next tranche after prerequisite:** GATX-T02

## Purpose

The Guided Alpha Testing Experience turns the existing Internal Alpha from a development-oriented collection of surfaces into a cohesive, self-explanatory testing environment that can be reused as Multiversal progresses from one-computer testing to trusted-LAN testing and eventually geographically separated online testing.

The program exists to remove tester friction and ambiguity, increase the amount of useful evidence produced per session, make defects reproducible, and select the highest-value next tests so Internal Alpha testing advances development instead of creating repeated one-off troubleshooting loops.

This is a bounded subproject that must reach its current-stage completion boundary before ordinary roadmap progression resumes.

## Owner construction-first execution rule

For every GATX tranche or owner-inserted bounded prerequisite:

1. finish the complete bounded construction;
2. do not interrupt construction with repeated per-slice validation cycles;
3. once construction is sealed, run the focused and proportionate validation as one validation phase;
4. batch related repairs discovered by that validation;
5. rerun the smallest applicable final gate;
6. record `completed_verified` only after the declared evidence exists.

This rule inherits the repository checkpoint/validation efficiency policy and is stricter where necessary to prevent tiny fix/check/fix loops from dominating the work.

## Design principles

- **One cohesive test environment:** testers should not need developer knowledge to understand what they are looking at.
- **In-product guidance:** objectives, expected results, progress, limitations and reporting should remain visible while the tester uses Multiversal.
- **One durable reference Campaign:** Glass Harbor Incident in Meridian Testbed is the canonical synthetic testing context; its full application integration belongs to GATX-T02.
- **Role-safe guidance:** GM and Player use the same guidance contract without weakening application authorization.
- **Transport-neutral testing contract:** the testing experience must be reusable across one-machine, LAN and future remote-online transport.
- **Evidence over memory:** build identity, account, role, scenario and relevant bounded diagnostics should be captured by the system wherever possible.
- **Testing the test:** confusion caused by bad instructions is a test-system defect, not automatically an application defect.
- **No hidden authority expansion:** GATX does not silently activate production identity, shared-live runtime, real-user data, public deployment, paid providers or native Android packaging.

## Tranches and prerequisite foundations

### GATX-T01 — Guided Alpha framework — COMPLETED_VERIFIED

Turn the current Alpha into a recognizable guided testing environment.

Completed outcome:

- persistent Guided Alpha shell around the real GM/Player application;
- tester identity and role;
- exact build/candidate context;
- connection mode;
- test round;
- reference Campaign context;
- current objective and next action;
- expected result;
- start/resume;
- progress;
- report-problem entry;
- reset/recovery entry;
- connection status;
- known limitations;
- preservation of the physically confirmed GM Campaign/Session/Combat/Assets navigation repair.

Exit condition satisfied: a tester can enter the Alpha and understand what they are supposed to do.

### GATX-DIAG-F01 — Automatic diagnostics foundation — ACTIVE PREREQUISITE

Owner-inserted prerequisite before T02. Pull forward only the reusable diagnostic collection/transport/export substrate that T04 would otherwise have needed to retrofit later.

Required outcome:

- automatically capture pertinent **system-known** build/package/tranche/round/account/role/Campaign/browser/device/connection/progress/error context;
- maintain an in-progress JSON diagnostic snapshot on the host laptop;
- automatically write a final JSON diagnostic file to the laptop when a guided round completes;
- finalize active diagnostic sessions during normal runner shutdown;
- provide an explicit `Save Diagnostics Now` snapshot control;
- route trusted-LAN/Android browser diagnostic events back to the Windows host laptop;
- use one tranche-dynamic package/runner contract reusable by T02 and later GATX work;
- prohibit credential/password, arbitrary form-content, keystroke, free-text problem-description, real Campaign/player-data, unrelated-file and browser-history collection.

This prerequisite **does not complete GATX-T04**. T04 still owns scenario/step/application-area/synthetic-state attachment, tester-perceived/expected input, defect classification and reproducible evidence-bundle workflow.

Exit condition: pertinent technical context is captured automatically and a host-side diagnostic file exists without manual log archaeology.

### GATX-T02 — Reference Campaign integration

Integrate the already validated Stage A reference Campaign kit into the application rather than inventing a new fixture.

Reference Campaign: **Glass Harbor Incident**  
Reference World: **Meridian Testbed**

Required outcome: Character, NPC, clue, relationship, faction, combat, vehicle, scene, world and related synthetic surfaces belong to one recognizable campaign with deterministic reset, and pertinent system-known T02 evidence flows through GATX-DIAG-F01.

Exit condition: the Alpha behaves like a small coherent Multiversal campaign instead of a component showroom.

### GATX-T03 — Guided scenario and test-journey engine

Convert scripted journeys into machine-readable test scenarios containing role, prerequisite state, context, objectives, actions, expected results, systems covered, permission/hidden-information expectations, recovery expectations, reset points and outcome capture.

Support progressively larger charters such as smoke, feature, workflow, session, recovery, device, multiplayer and regression.

Exit condition: testers execute meaningful repeatable journeys instead of free-form poking.

### GATX-T04 — Frictionless evidence and defect capture

Build on GATX-DIAG-F01. Automatically attach safe information the system already knows to a tester report, including scenario, step, application area and synthetic state identity in addition to the foundation's build/account/role/platform/connection/diagnostic context.

The tester supplies only information the system cannot know, such as what they perceived and expected. T04 also owns defect classification and reproducible evidence packaging.

Exit condition: a useful defect report requires minimal tester effort and is reproducible without manual archaeology.

### GATX-T05 — Device and trusted-LAN connection center

Absorb current Android/LAN issue handling into a guided device workflow rather than continuing isolated networking fixes.

Required capabilities include server/port/network-profile/firewall/listener/request visibility, explicit bounded LAN preparation and cleanup, easy device URL/QR entry, diagnostics and layer-specific failure classification.

Application issue #159 is retained as current evidence for this tranche.

Exit condition: supported same-LAN second-device testing is guided and a failure identifies which layer failed.

### GATX-T06 — Testing operations and control layer

Provide round configuration, tester/role assignment, required/optional scenarios, known defects, coverage states, retest status and highest-value-next-test selection.

Exit condition: test selection is driven by missing evidence and changed code rather than memory or instinct.

### GATX-T07 — Remote-online-ready Guided Alpha

Make the guidance/scenario/evidence layer transport-neutral and prepare the UI/contracts for a future Remote Test Session mode.

The architecture may be completed before remote runtime activation. Actual remote transport remains dependency-gated by authoritative session, realtime, hidden-information and reconnect foundations.

Exit-now boundary: the Guided Alpha experience does not have to be rebuilt when true remote sessions become available.

### GATX-T08 — Cross-location Guided Alpha and permanent regression loop

After the existing online/runtime dependencies permit it, execute geographically separated guided testing (for example Alabama GM and Kentucky Player) across a scripted shared-session sequence and adverse reconnect/permission/latency cases.

Successful scenarios become durable future regression charters.

Exit condition: geographically separated testers can join, understand, execute, recover and report a meaningful Multiversal test session without developer supervision.

## Current-stage completion boundary

Before ordinary roadmap progression resumes, complete and verify:

- GATX-T01;
- GATX-DIAG-F01;
- GATX-T02 through GATX-T06;
- the transport-neutral architecture/UI portion of GATX-T07.

The remote-runtime activation portion of GATX-T07 and physical cross-location execution in GATX-T08 remain gated by the existing authoritative online/session roadmap and must not be simulated into completion.

## Relationship to existing authorities

### IA-D09

GATX operationalizes the existing IA-D09 tester-entry requirements rather than replacing them. IA-D09 already requires explicit build identity, supported platform, role, data classification, limitations, reset/recovery, defect reporting, privacy boundaries and a deterministic tutorial/test charter.

### Stage A reference Campaign kit

The validated Stage A Tester / Reference Campaign Kit is the content basis for GATX-T02. GATX must not invent a parallel replacement fixture unless later owner authority explicitly changes that decision.

### P9-06 two-device/online acceptance

GATX-T07/T08 are a testing-experience bridge to the existing two-device online acceptance authority. They do not replace server authority, ordered realtime delivery, hidden-information filtering or reconnect-restoration dependencies.

### Current Hotfix 2 package

The owner-approved Hotfix 2 package remains the approved exact distribution until a changed GATX successor package is separately built, validated, physically checked when required, and explicitly approved. GATX development does not retroactively modify the approved ZIP.

## Permanent feature-entry rule

After the Guided Alpha framework becomes canonical, any feature intended to enter Internal Alpha should carry the testing material required by the active GATX contract. At minimum, that should eventually include:

- deterministic fixture/context;
- guided scenario coverage;
- expected result;
- reset behavior;
- automatic diagnostic/evidence hooks;
- known limitations;
- regression/retest mapping.

A feature should not be considered truly Alpha-ready merely because its controls render.

## Non-authorizations

This program does not by itself authorize:

- real-user data collection;
- credential/password/arbitrary-form-content collection by diagnostics;
- production identity or credentials;
- paid-provider commitment;
- public deployment or release;
- synchronized shared-live Campaign/session authority before its governing runtime gates;
- public Internet exposure of the current local runner;
- native Android APK distribution;
- automatic A13 or other unapproved roadmap expansion.
