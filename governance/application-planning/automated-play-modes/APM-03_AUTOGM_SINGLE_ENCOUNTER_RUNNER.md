# APM-03 — AutoGM Single-Encounter Runner

**Work item:** APM-03  
**Program:** APM — Automated Play Modes  
**Version:** 0.1.0  
**Status:** DESIGN CONTRACT — READY FOR GOVERNED REVIEW  
**Owner and final authority:** John Brandon Turner  
**Date:** 2026-08-19

## 1. Decision

APM-03 defines AutoGM’s first playable scope as **one bounded solo encounter run** over ordinary Multiversal rules/state. The controller orchestrates only explicitly delegated scenario operations; owning domains continue to authorize and resolve mechanics, persistence and authoritative Events.

The controlling flow is:

`Select Character + Encounter Package → Validate Setup/Delegation → Start Run → Player Action → Deterministic Resolution → Eligible NPC/World Response → Deterministic Resolution → Repeat → End Condition → Governed Rewards/Summary → Stop`

Optional AI may narrate already-resolved state, render dialogue from filtered presentation context or suggest nonauthoritative phrasing. It does not select legal mechanics, reveal hidden truth, grant itself GM authority or mutate canonical state.

## 2. Encounter package

An AutoGM encounter package is a bounded scenario authority package with exact versioning. It declares:

- package ID/version and compatibility constraints;
- intended context and eligible Character/party assumptions;
- setup requirements and initial encounter state;
- controlled NPC/world actors and the exact operation families the controller may request;
- hidden scenario state needed by deterministic orchestration;
- player-visible projection rules;
- encounter objective(s), optional objectives and end conditions;
- allowed response policies/decision tables;
- deterministic/random seed requirements;
- reward/result proposal rules;
- undefined-situation/fail-safe policy;
- maximum round/step/event budget where applicable;
- provenance and source Adventure/CSW references.

A package is not an AI prompt. Machine-private scenario truth is available only to the deterministic controller components that require it. Optional AI receives a separately filtered presentation projection.

## 3. Run state

Conceptual `AutoGMEncounterRun` fields:

- `automationRunId`;
- `automationControllerId` and version;
- initiating subject;
- selected Character/party IDs and exact versions/projections;
- encounter package ID/version;
- context/session ID;
- delegation grant ID/version;
- authoritative Event sequence/version at start/current point;
- encounter phase/round/turn window;
- current actor/priority window;
- deterministic seed/entropy stream reference;
- pending player choice/Action;
- pending reaction/interrupt window;
- hidden deterministic scenario state reference;
- player-visible projection version;
- run status;
- stop/end reason;
- summary/reward receipt references;
- correlation/provenance IDs.

Initial status model:

`draft → validating → ready → running → awaiting-player-action → resolving → awaiting-reaction → paused/recovery-required → ending → completed | aborted | failed-safe`

No status grants authority by itself.

## 4. Setup validation

Before `running`, the system revalidates:

1. subject/context authorization;
2. selected Character eligibility and current availability;
3. package/rules/pack/schema compatibility;
4. encounter prerequisites and required definitions;
5. delegation grant scope and expiry;
6. hidden-information projection policy;
7. configured difficulty/presentation preferences;
8. resource/condition starting state;
9. deterministic seed/entropy configuration;
10. end/reward rules;
11. foreground-only execution for initial AutoGM.

“Difficulty preference” may select among package-supported legal variants, encounter composition or presentation hints. It may not silently change core mechanics or grant unlisted bonuses/penalties.

## 5. Player Action contract

The player retains intentional control of their Character unless an explicit narrow preauthorization exists under APM-01. The runner presents currently legal/actionable options where the owning domain supports enumeration, but freeform/select-from-character-sheet Action entry remains possible.

Player Action sequence:

1. capture action intent with operation ID;
2. authorize against current subject/Character/control state;
3. validate targets/costs/prerequisites/current turn window;
4. resolve through owning-domain rules using exact expected versions and governed randomness;
5. persist authoritative Event/effects;
6. produce player-safe resolved projection;
7. advance the encounter state only from committed evidence.

The controller cannot repair an illegal Action by inventing a legal state change. It may explain the failure and return control.

## 6. NPC/world response contract

After a committed player/world event, the controller computes an **eligible deterministic response set** from:

- exact package policy/version;
- current encounter/scenario state;
- controlled actor capabilities and status;
- current authority/delegation;
- visibility-safe machine-private scenario state;
- deterministic/randomized response tables or policy rules.

Each response candidate is classified using APM-01 operation classes. The controller may choose/execute only `automatic_permitted` or `automatic_with_bounds` operations inside the grant. `proposal_required`, `human_required` and `prohibited` remain barriers.

If no permitted safe response exists, the runner pauses or enters `failed-safe`; it does not improvise new mechanical authority.

## 7. Initiative, reactions and interrupts

The runner consumes the owning encounter/rules model for initiative/priority. It must support explicit windows for:

- player turn/action;
- NPC/world response;
- reactions/interrupts;
- triggered effects;
- mandatory choices;
- simultaneous/ordered resolution when the owning system defines it.

A reaction opportunity that belongs to the human Character pauses automated progression until chosen, declined or an explicit bounded default exists. Timing windows are persisted so reconnect does not silently skip them.

## 8. Deterministic mechanics and replay

The required determinism claim is **mechanical**, not prose identity.

For a fixed set of:

- starting authoritative state/version;
- encounter package/version;
- rules/pack/schema versions;
- delegation/mode profile versions;
- ordered player Actions;
- deterministic seed/entropy stream;
- controller decision-policy version;
- environment-independent deterministic domain inputs;

the owning-domain mechanical outcomes and authoritative Event sequence must be reproducible according to existing deterministic rules.

Narration, wording, optional AI dialogue, animation timing or UI layout need not be byte-identical and are excluded from mechanical replay identity.

Every random draw relevant to state records the source stream/sequence evidence required by the owning domain. Optional AI randomness never substitutes for mechanical randomness.

## 9. Hidden information

Encounter packages may contain hidden NPC stats, tactics, secrets, triggers or unrevealed state. Protection order is:

`authorize machine-private deterministic use → resolve event → compute player-safe projection → optionally construct AI presentation context`

Hidden material must not leak through action enumeration, failure messages, target labels, counts, logs, summaries, accessibility text, AI prompts, autocomplete or retry hints.

AI never receives raw package-private state by default. Dialogue/narration prompts contain only the resolved/player-permitted facts required for the presentation task.

## 10. Stop and end conditions

The encounter ends or pauses on explicit conditions including:

- primary objective complete;
- all configured endpoints reached;
- player defeat/incapacitation where rules/package define it;
- retreat/escape;
- surrender/negotiated end when supported;
- package-defined timeout/round/step bound;
- player abort;
- delegation revoked/expired;
- authorization/entitlement/version invalidation;
- unresolved human-required choice;
- undefined/out-of-scope mechanical situation;
- persistence/conflict failure that cannot be safely reconciled;
- safety/privacy boundary.

A `completed` run requires a package-valid ending. `aborted` and `failed-safe` preserve committed Events and recoverable evidence without pretending success.

## 11. Defeat, retreat and failure

AutoGM does not guarantee victory. Encounter packages define legal consequences of defeat/retreat/surrender. Any permanent Character death, irreversible loss or other high-impact result remains subject to the owning game/domain policy; APM-03 adds no hidden protection or punishment.

Where the system requires a human decision after defeat, the runner stops at that decision rather than choosing for the player.

## 12. Rewards and advancement

Encounter completion may produce:

- authoritative rewards that the owning domain explicitly permits automatically;
- loot/resource result candidates requiring normal ownership/inventory validation;
- XP/progress evidence;
- advancement eligibility/proposal;
- narrative summary/history receipt.

Irreversible build/advancement choices remain human-required. A reward package cannot bypass entitlement, capacity, uniqueness, quantity, ownership or Character advancement rules.

## 13. Persistence, disconnect and recovery

Initial APM-03 is `foreground_only`. Disconnect/exit creates a safe pause/recovery state; it never authorizes background rounds.

Persisted recovery evidence includes:

- run/package/controller/delegation versions;
- last committed authoritative Event sequence;
- current phase/round/turn/reaction window;
- deterministic seed stream position;
- pending human Action/choice identity;
- accepted operation IDs and statuses;
- hidden scenario state/version;
- visible projection version.

Resume reauthenticates/re-authorizes, checks package/rules compatibility, resolves ambiguous in-flight operations by status lookup, rejects duplicate Action operation IDs idempotently and resumes only from a proven committed boundary.

If versions are no longer compatible, the run pauses for explicit recovery/migration/abort; it does not silently reinterpret old encounter state under new rules.

## 14. Optional AI presentation

Optional AI may:

- narrate committed mechanical outcomes;
- render NPC dialogue from filtered state;
- summarize the encounter so far;
- restate legal choices already produced by deterministic systems;
- explain rules/results from authorized evidence;
- provide tone/accessibility transformations.

It may not:

- select or validate mechanical outcomes;
- receive unrestricted hidden scenario state;
- choose the human Character Action;
- invent an authoritative NPC ability/state;
- change reward legality;
- decide whether a run counts as completed;
- mutate the encounter/package/Character/Campaign.

If AI is unavailable, deterministic text/templates/manual presentation remain sufficient to complete the encounter.

## 15. Replay and restart

“Replay encounter” creates a **new run** with new run identity. A replay may intentionally reuse the same starting fixture and seed for testing, or use a new seed for play, but it never rewinds/overwrites the history of a completed authoritative run.

Testing fixtures may use isolated/noncanonical sandbox state. Campaign/live replay requires the normal owning-domain rules for starting a new encounter from current state.

## 16. Acceptance contract

APM-03 is design-complete when the package defines:

- encounter package/run identities and compatibility;
- explicit bounded delegation and eligible response selection;
- governed player Action/NPC response loop;
- initiative/reaction/human-choice barriers;
- deterministic mechanical replay inputs;
- hidden-information and AI projection separation;
- defeat/retreat/end/abort/fail-safe semantics;
- reward/advancement boundary;
- foreground-only persistence/recovery/idempotency;
- no-AI completion path;
- explicit provenance/audit evidence.

No application implementation, migration, unbounded AutoGM, release/deployment, canonical promotion or CCTI-12-T04 work is authorized.