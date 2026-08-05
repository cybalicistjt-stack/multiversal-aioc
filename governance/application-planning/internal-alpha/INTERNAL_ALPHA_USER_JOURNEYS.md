# Internal Alpha User Journeys

**Program:** MV-IA-001  
**Version:** 0.1.0  
**Status:** DESIGN BASELINE

## 1. Journey design rules

Every journey must define:

- user role;
- starting state;
- required data;
- permissions;
- actions;
- persistence;
- hidden information;
- loading and error states;
- interruption and recovery;
- desktop and mobile behavior;
- accessibility;
- observable completion evidence.

## 2. Journey IA-J01 — Player onboarding and Session entry

### Goal

A Player enters the correct Campaign and reaches a live Session with an approved Character.

### Flow

1. Open Multiversal.
2. Enter or select identity.
3. Accept or review a Campaign invitation.
4. See only permitted Campaigns, Characters, Sessions, and notifications.
5. Open the Campaign workspace.
6. Create, select, or resume a Character.
7. Resolve validation or entitlement problems.
8. Enter the available Session.
9. Receive the Player-safe Scene projection.
10. Review current Character summary and available Actions.

### Required failure states

- expired invitation;
- wrong account;
- revoked membership;
- missing Character approval;
- restricted content;
- Session not started;
- stale client;
- network interruption.

### Completion evidence

A distinct Player identity reaches the correct live Session without seeing GM-only information.

## 3. Journey IA-J02 — GM Campaign and Scene preparation

### Goal

A GM prepares and launches a playable Scene using real governed content.

### Flow

1. Enter the GM workspace.
2. Create or open a Campaign.
3. Select rules profile and approved packs.
4. Invite a Player and assign Campaign role.
5. Review or approve the Player Character.
6. Create a Session and Scene.
7. Use the universal object picker to add:
   - location;
   - environment;
   - creatures or NPCs;
   - hazards or interactables;
   - objectives or clues;
   - rewards or consequences.
8. Configure Player-visible and GM-only information.
9. Add a map or choose theater-of-the-mind/zone mode.
10. Validate dependencies and permissions.
11. Save and reopen the Scene.
12. Preview the Player view.
13. Launch the Session.

### Required failure states

- unavailable pack;
- invalid object dependency;
- incompatible rules profile;
- missing permission;
- duplicate object placement;
- hidden information without a visibility policy;
- failed save;
- stale Scene version.

### Completion evidence

The GM launches a Scene that the Player can enter and that preserves hidden information.

## 4. Journey IA-J03 — First playable Action and approval loop

### Goal

Complete the core Player-to-GM tabletop loop.

### Player flow

1. Review Scene and Character summary.
2. Select an available Action.
3. Open a quick rules explanation.
4. Select target or targets.
5. Review costs, requirements, roll, modifiers, and proposed Effects.
6. Confirm and submit proposal.
7. See pending status without exposing GM-only information.

### GM flow

1. Receive approval notification.
2. See:
   - Player;
   - actor;
   - Action;
   - source and rules summary;
   - targets;
   - costs;
   - roll and modifiers;
   - computed result;
   - proposed Effects;
   - warnings.
3. Approve, deny, or modify.
4. Confirm the final attributable decision.

### Result flow

1. Authoritative service commits the accepted result.
2. Events and state update atomically.
3. Player and GM receive role-filtered projections.
4. Resources, Conditions, and history update.
5. The result survives reload and reconnect.

### Required interruption cases

- Player disconnects before submission;
- Player disconnects after submission but before decision;
- GM disconnects with pending proposal;
- duplicate submit;
- stale expected version;
- disconnect after commit before display;
- missed realtime event.

### Completion evidence

The proposal has one durable outcome, no duplicated Effects, and a complete decision receipt.

## 5. Journey IA-J04 — Complete combat encounter

### Goal

Run one bounded encounter without development-only interfaces.

### Flow

1. GM starts encounter.
2. Participants and timing/order appear.
3. Player completes movement and Actions.
4. GM runs NPC or enemy Actions through the same governed approval and result model.
5. Resources and Conditions change.
6. Environment or objective affects play.
7. A reaction or interrupt is resolved where available.
8. An actor is defeated, withdraws, or satisfies the objective.
9. Encounter ends.
10. Rewards and consequences persist.

### Completion evidence

Encounter history can be inspected and replayed sufficiently to reproduce accepted results.

## 6. Journey IA-J05 — Inventory and shared Asset lifecycle

### Goal

Prove ownership, custody, permissions, and persistence.

### Flow

1. Character acquires an item.
2. Item enters personal inventory.
3. Character equips it.
4. Character transfers it to another Character or shared container.
5. Permission and acceptance are checked.
6. Ownership and custody update.
7. Item is used, damaged, repaired, upgraded, consumed, or salvaged.
8. A shared vehicle or Asset is assigned to multiple permitted users.
9. Save and reload.

### Completion evidence

No Asset is duplicated or lost; audit history explains every transition.

## 7. Journey IA-J06 — Relationship and social consequence

### Goal

Use the Relationship Tracker during structured social play.

### Flow

1. Player opens an NPC or faction relationship summary.
2. Player sees only known relationship information.
3. Player selects a social approach or Action.
4. GM sees private motives, thresholds, and modifiers.
5. The proposal resolves through approve, deny, or modify.
6. Relationship history records the event.
7. Attitude, trust, fear, obligation, reputation, promise, debt, or social Condition changes.
8. Later Scene behavior reflects the persistent consequence.

### Completion evidence

The directional relationship changes without exposing hidden GM state.

## 8. Journey IA-J07 — Investigation and clue discovery

### Goal

Prove persistent nonlinear investigation without collapsing hypotheses into truth.

### Flow

1. Player investigates a Scene, witness, object, or record.
2. A clue is proposed or discovered.
3. GM controls reveal and detail level.
4. The clue enters the Player evidence workspace.
5. Player links it to other evidence.
6. Player creates a hypothesis.
7. The system labels the hypothesis separately from established facts.
8. A false lead or unresolved question remains possible.
9. A later Scene reveals, contradicts, or expands the evidence.

### Completion evidence

Player-safe evidence persists while unrevealed truth remains hidden.

## 9. Journey IA-J08 — Encounter preparation and balance review

### Goal

Help the GM assemble a reasonable encounter without claiming guaranteed balance.

### Flow

1. Open Encounter Builder.
2. Select party or expected participant profile.
3. Add creatures, NPCs, hazards, environment, and objectives through object pickers.
4. Validate dependencies and rules versions.
5. Display source-grounded pressure indicators and uncertainties.
6. Run bounded deterministic or seeded simulations where available.
7. Show warnings and retained outliers.
8. Save the encounter to a Scene.

### Completion evidence

The encounter is valid, traceable, and reviewable; the system does not represent simulation as certain table outcome.

## 10. Journey IA-J09 — Adventure branch and persistent consequence

### Goal

Run a bounded adventure path containing a meaningful branch.

### Flow

1. GM launches an Adventure Definition in a Campaign.
2. Initial objectives, Scene, and known information appear.
3. Players make a choice or complete an Action.
4. The choice changes route, objective, clock, faction, relationship, reward, or Scene state.
5. GM sees private branch state.
6. Players see only revealed consequences.
7. Save, close, and reopen the Campaign.
8. Resume from the correct branch state.

### Completion evidence

Campaign history and current adventure state agree after reload.

## 11. Journey IA-J10 — Recovery and support

### Goal

A tester recovers safely or reports a reproducible problem.

### Flow

1. Encounter a failed save, stale client, missing data, or reconnect problem.
2. Receive a clear state-specific explanation.
3. Retry, refresh, restore draft, or reconnect through a safe action.
4. Preserve unsent local work where appropriate.
5. When recovery fails, open issue reporting.
6. Automatically include permitted version, environment, correlation, and diagnostic metadata.
7. Tester adds expected and actual result without exposing protected content.
8. Team receives a reproducible issue.

### Completion evidence

The tester either returns to a safe state or submits a useful privacy-safe issue.

## 12. Journey IA-J11 — Basic creator workflow

### Goal

Create Campaign-usable content without granting canonical authority.

### Flow

1. Enter Content Creator or GM authoring workspace.
2. Search for possible duplicates.
3. Create or clone a bounded object such as a Location, NPC, faction, item, or Scene component.
4. Add source and ownership metadata.
5. Validate fields and relationships.
6. Preview runtime and Player-safe presentation.
7. Save as Campaign-local or draft pack content.
8. Submit for review where reusable promotion is requested.

### Completion evidence

The object can be used within the permitted Campaign but remains noncanonical until approved.

## 13. Journey IA-J12 — Optional governed AI assistance

### Goal

Test one bounded AI-assisted action without making AI a product dependency.

### Flow

1. User invokes a specific assistant action.
2. System binds identity, role, Campaign, permissions, entitlement, and allowed sources.
3. AI returns a source-linked explanation, search result, summary, validation finding, or draft.
4. Output is labeled as proposed.
5. User accepts, revises, rejects, or ignores it.
6. Any mutation uses the normal governed action and approval path.
7. Core workflow remains available when AI is disabled.

### Completion evidence

AI does not expose hidden content, bypass permissions, create canon, or silently mutate state.

## 14. Journey-to-feature traceability

| Journey | Primary features |
|---|---|
| IA-J01 | F001, F003, F004, F019, F020, F021, F022, F025 |
| IA-J02 | F002, F003, F005, F012, F013, F015, F020, F024 |
| IA-J03 | F003, F004, F005, F006, F020, F021 |
| IA-J04 | F006, F007, F012, F013 |
| IA-J05 | F004, F008, F014, F020 |
| IA-J06 | F006, F009, F010, F016, F020 |
| IA-J07 | F002, F005, F009, F011, F020 |
| IA-J08 | F002, F005, F012, F024 |
| IA-J09 | F005, F010, F011, F016, F017 |
| IA-J10 | F001, F003, F021, F025 |
| IA-J11 | F002, F015, F024 |
| IA-J12 | F002, F019, F020, F023 |