# Internal Alpha Content and Fixture Baseline

**Program:** MV-IA-001  
**Version:** 0.1.0  
**Status:** DESIGN BASELINE

## 1. Purpose

Define the bounded content and deterministic fixtures required to design and later validate internal-alpha features without attempting to expose the entire Multiversal corpus in the first release.

## 2. Fixture principles

Internal-alpha fixtures must be:

- deterministic;
- version-pinned;
- source-linked;
- permission-aware;
- small enough to understand;
- rich enough to exercise realistic workflows;
- separate from production data;
- reusable across services, UI, migration, recovery, and E2E tests.

## 3. Required identity fixtures

- Owner/Admin identity.
- Primary GM identity.
- Assistant GM identity.
- Primary Player identity.
- Second Player identity.
- Content Creator identity.
- Revoked former participant.
- Service actor.
- AI service actor with no mutation authority.

## 4. Required Campaign fixtures

### IA-CAMPAIGN-01 — Core internal-alpha Campaign

Must contain:

- one GM;
- two Players;
- approved rules profile;
- installed alpha content packs;
- at least two Characters;
- one prepared Session;
- multiple Scenes;
- Player-safe and GM-only content;
- one relationship and faction path;
- one investigation path;
- one combat encounter;
- one shared Asset or vehicle;
- one adventure branch;
- retained history.

### IA-CAMPAIGN-02 — Isolation Campaign

Used to prove:

- cross-Campaign access denial;
- search and count isolation;
- notification isolation;
- export isolation;
- AI context isolation.

## 5. Required Character fixtures

- valid Player Character using only free or Campaign-granted content;
- valid higher-tier Character with approved access;
- invalid Character with missing prerequisite;
- Character with active Conditions and depleted Resources;
- Character with personal and shared Assets;
- Character with relationship history;
- retired or archived Character;
- Character with migration history.

## 6. Required content families

The bounded corpus must include representative records for:

- species and forms;
- attributes and derived values;
- skills and proficiencies;
- Abilities across at least two tiers;
- Actions;
- Effects;
- Conditions;
- Resources;
- items and equipment;
- containers;
- creatures and NPCs;
- environments;
- hazards;
- vehicles or operational Assets;
- factions;
- relationships;
- Locations;
- Scenes;
- clues and evidence;
- objectives and rewards;
- adventure routes and branch state;
- source and provenance records.

## 7. Required Scene fixtures

1. **Social Scene** — NPC motive and relationship state partly hidden.
2. **Investigation Scene** — clues, false lead, hypothesis, and unrevealed GM truth.
3. **Combat Scene** — environment, objectives, creatures, Actions, Resources, Conditions, and encounter end.
4. **Travel or vehicle Scene** — shared Asset, access roles, cargo or occupants.
5. **Recovery Scene** — prebuilt event history and checkpoint for reconnect tests.

## 8. Required Action fixtures

- valid no-roll Action;
- valid rolled Action;
- Action with target choice;
- Action with multiple targets;
- Action with Resource cost;
- Action with prerequisite failure;
- Action producing a Condition;
- Action producing relationship or reputation change;
- Action requiring GM modification;
- duplicate command fixture;
- stale expected-version fixture.

## 9. Required permission fixtures

- Player-safe object with GM-only extension fields;
- unrevealed clue;
- private Player note;
- GM note;
- hidden NPC motive;
- restricted content object;
- Campaign-granted content object;
- revoked participant;
- wrong-Campaign subject;
- AI query attempting to retrieve hidden content.

## 10. Required Asset fixtures

- personal item;
- equipped item;
- stackable Resource;
- shared party container;
- borrowed item;
- damaged and repairable item;
- consumable;
- crafting components and result;
- shared vehicle;
- blocked transfer;
- split and merge history;
- anti-duplication test state.

## 11. Required relationship fixtures

- Character to NPC relationship with asymmetric views;
- Character to faction standing;
- promise;
- debt;
- trust threshold;
- fear or hostility threshold;
- hidden motive;
- revealed relationship event;
- conflicting Player hypothesis about a relationship;
- relationship history spanning multiple Scenes.

## 12. Required investigation fixtures

- clue known to all Players;
- clue known to one Player;
- unrevealed clue;
- evidence document;
- witness record;
- false lead;
- unresolved question;
- Player hypothesis;
- contradicted hypothesis;
- GM truth;
- reveal event.

## 13. Required failure fixtures

- unavailable pack dependency;
- invalid stable ID reference;
- stale object version;
- failed save;
- reconnect gap;
- corrupted local draft;
- corrupted snapshot;
- missing media derivative;
- invalid entitlement snapshot;
- revoked permission during an open screen;
- duplicate Action command;
- migration interruption;
- backup checksum mismatch;
- provider-exit import mismatch.

## 14. Pack lifecycle fixture set

The alpha corpus must support:

1. clean install;
2. repeated install;
3. update with migration;
4. dependency conflict;
5. blocked removal because Campaign state depends on the pack;
6. safe removal of an unused pack;
7. reinstall;
8. export and import;
9. zero unintended residue.

## 15. Accessibility fixtures

Include data that stresses:

- long names;
- long descriptions;
- many Conditions;
- dense relationship graphs;
- large inventory;
- nested objects;
- localized or unusual characters;
- high zoom;
- narrow mobile width;
- map alternative text;
- validation errors across multiple fields.

## 16. Fixture ownership

Every fixture must identify:

- fixture ID;
- purpose;
- source or synthetic status;
- schema version;
- pack versions;
- expected permissions;
- expected results;
- migration path;
- cleanup behavior.

Fixtures are not canonical content unless separately released as canonical records.

## 17. Next fixture-design work

The detailed fixture IDs, object selections, expected Events, and exact pack versions should be completed during Tranche IA-D03 after the Universal Object, permissions, identity, Character, and Campaign feature packets define their final data needs.