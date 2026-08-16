# IA-D09-TA-001 — Internal Alpha Round Guide

**Status:** owner-authorized bounded Internal Alpha execution guide  
**Approved package:** `Multiversal-Internal-Alpha-Windows-HOTFIX2-a4e262167aa9.zip`  
**SHA256:** `5c9f31c96a3373f927f8d3a7ee6ee821aafeda8d0ae26a0c6cecf94ca129e0de`  
**Marker:** `IA-HOTFIX-ACCOUNT-DISPATCH-2`  
**Default port:** `8877`

This guide does not change the approved package. It organizes testing into multi-check sessions so testers can complete a useful batch before reporting results.

## 1. Boundaries every tester must know

- Use synthetic test data only.
- Testers do not need GitHub accounts.
- Windows uses the approved private ZIP and local runner.
- Android uses a trusted-LAN browser connection to the Windows runner; there is no APK.
- Browser state is local to each browser instance. GM and Player browsers do **not** yet share live synchronized Campaign/session state.
- Do not enter passwords, production credentials, private Campaign notes, real player information, or unrelated personal data into reports.
- The GM sidebar Campaign / Session / Combat / Assets buttons are a known issue (`Multiversal-app#157`): they currently look interactive but do not navigate. Do not report duplicates unless behavior materially differs.

## 2. Account assignment

- `John GM` and odd tester numbers (`tester1`, `tester3`, …, `tester17`) are Game Master accounts.
- `John Player` and even tester numbers (`tester2`, `tester4`, …, `tester18`) are Player accounts.
- Physical Windows validation already confirmed all 20 accounts route to the correct mode.

## 3. One batched tester session

A tester should complete as many of these checks as practical in one session before reporting back.

### Batch A — Entry and identity

1. Start the exact approved package and confirm the HOTFIX 2 marker and port 8877.
2. Select the assigned account.
3. Confirm the displayed account name and assigned role are correct.
4. Refresh the page once and confirm the experience remains usable.
5. Return to `/alpha-access` and re-enter the assigned account.

### Batch B — Primary UI and workflow exploration

1. Review the visible navigation and workspace labels.
2. Exercise the visible controls that appear relevant to the assigned role.
3. Open the available Campaign/session/action/combat/inventory/vehicle/investigation/social/world-content surfaces that the build exposes.
4. Note any control that appears actionable but does nothing, opens the wrong surface, loses context, or exposes the wrong role.
5. Do not treat lack of cross-browser live synchronization as a defect in this round.

### Batch C — State and recovery

1. Refresh during a normal screen.
2. Navigate away and back where possible.
3. Close and reopen the browser while the runner remains active.
4. Stop and restart the runner, then re-enter the assigned account.
5. Record whether the user can understand what happened and recover without hidden manual steps.

### Batch D — Responsive/device behavior

For Windows, resize the browser narrower and wider. For Android, use the LAN URL from the runner.

Check:

- text remains readable;
- primary controls remain reachable;
- no important content is clipped horizontally;
- touch targets are usable on Android;
- role identity and alpha/synthetic-data context remain visible or understandable.

### Batch E — Permission and role sanity

- GM testers should not silently become Player accounts.
- Player testers should not gain GM-only authority.
- If a tester manually attempts a wrong-role entry path, record whether access is refused safely without exposing hidden information.
- Do not use real secrets or private data to test permission failures.

### Batch F — Overall tester judgment

At the end of the session, record:

- the three most confusing things;
- the three most useful/clear things;
- anything that blocked progress;
- anything that looked broken but may simply be an unfinished alpha surface;
- the single improvement that would most improve the next session.

## 4. Defect report format

For each distinct defect, capture:

- tester account ID and role;
- Windows or Android;
- browser and approximate version if known;
- exact screen/area;
- what the tester was trying to do;
- minimal reproduction steps;
- expected result;
- actual result;
- whether it happens every time, sometimes, or once;
- severity: `blocker`, `major`, `minor`, or `cosmetic`;
- whether restarting the page/browser/runner changes it;
- screenshot if useful and safe;
- relevant lines from `internal-alpha-runner.log` for entry/server issues;
- confirmation that the report contains synthetic/non-sensitive information only.

Do not attach unrelated logs, credentials, personal files, hidden GM information to a Player report, or real Campaign/player data.

## 5. Severity guide

- **Blocker:** cannot enter/use the assigned role or cannot continue the intended alpha session.
- **Major:** important workflow is wrong, inaccessible, loses state unexpectedly, or violates role/permission expectations.
- **Minor:** workflow works but is confusing, inconsistent, incomplete, or requires an unnecessary workaround.
- **Cosmetic:** visual/text/layout issue with no meaningful workflow impact.

## 6. Batch reporting rule

Testers should report a group of findings after a reasonable session rather than stopping after every harmless oddity. Stop immediately only for:

- repeated crash or unrecoverable blocker;
- role/permission leak;
- unexpected exposure of sensitive/hidden information;
- behavior that could damage files/system state;
- anything requesting production credentials, payment, or real-user data.

The owner/project operator may turn the session report into one or more repository defects. A tester report is evidence, not automatic canonical product authority.

## 7. Known limitations for this exact round

- No synchronized live GM/Player Campaign/session state between separate browsers.
- No Android APK.
- GM sidebar Campaign / Session / Combat / Assets controls are inert (`Multiversal-app#157`).
- Local/test identity selector is not production authentication.
- Synthetic fixtures are expected; production content/data is not authorized.

Any new limitation discovered during the round should be recorded with the exact package identity above.
