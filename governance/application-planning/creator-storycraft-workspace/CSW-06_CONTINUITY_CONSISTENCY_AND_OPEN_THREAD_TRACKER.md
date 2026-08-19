# CSW-06 — Continuity, Consistency and Open-Thread Tracker

**Work item:** CSW-06  
**Program:** CSW — Creator Storycraft Workspace  
**Version:** 0.1.0  
**Status:** DESIGN CONTRACT — READY FOR GOVERNED REVIEW  
**Owner and final authority:** John Brandon Turner  
**Date:** 2026-08-19

## 1. Decision

CSW-06 defines a **permission-safe advisory continuity and open-thread layer** over CSW-02 Project Memory/Story Bible and CSW-05 structural planning. It helps creators notice things that may deserve attention without pretending the system knows the one correct story.

The controlling rule is:

> **Surface candidates with evidence; never silently rewrite truth; let the creator decide whether something is wrong, intentional, unresolved, irrelevant or already handled.**

The tracker is useful without AI. Deterministic graph/reference/timeline/name/structure checks are first-class. Optional AI may compare, summarize or critique only authorized evidence and returns candidates, never corrections automatically applied to source material.

## 2. Two related but distinct objects

### 2.1 OpenThread

A durable creator-managed obligation/question/through-line that is worth remembering even if no automated analysis detects it.

Conceptual fields:

- `threadId` and version;
- owner/project/context;
- kind;
- title/summary;
- source fragment/structural/reference links;
- lifecycle state;
- importance/priority note if the creator chooses;
- expected resolution/payoff/revisit condition where known;
- evidence/reference links;
- creator notes;
- visibility policy;
- provenance/history;
- created/updated/resolved timestamps.

Baseline thread kinds:

- hook;
- open-question;
- secret;
- foreshadow;
- setup/payoff obligation;
- unresolved-choice/consequence;
- mystery/revelation;
- character/NPC/faction arc;
- relationship development;
- location/world/lore thread;
- promised follow-up;
- creator-defined.

### 2.2 ContinuityCandidate

An advisory finding produced manually, deterministically or optionally by AI. It is **not** a truth record.

Conceptual fields:

- `candidateId`;
- candidate type/severity presentation class;
- project/context;
- evidence IDs + exact versions/projections;
- detection method/version;
- explanation/reason code;
- confidence/coverage metadata only where meaningful;
- lifecycle/disposition;
- stale/evidence-changed marker;
- creator note;
- created/last-evaluated timestamps;
- optional AI provenance.

A candidate never mutates its evidence sources by itself.

## 3. Lifecycle and dispositions

OpenThread lifecycle:

`open → needs-attention → dormant/snoozed → resolved | intentionally-unresolved | archived`

ContinuityCandidate lifecycle:

`new → reviewed → accepted-as-issue | dismissed | snoozed | intentionally-acceptable | resolved | stale`

Important semantics:

- `open` does not mean broken;
- `needs-attention` means the creator/system wants review, not objective defect;
- `possibly-inconsistent` is a candidate label, never a confirmed universal truth;
- `unused` is descriptive within the authorized analyzed scope, not “bad”;
- `resolved` means the creator recorded a resolution/disposition, not necessarily that source text changed;
- `intentionally-unresolved` suppresses nagging while keeping the creative choice visible;
- a changed source version may make an earlier candidate `stale` and eligible for re-evaluation.

## 4. Deterministic analysis families

### 4.1 Dangling and orphan references

Surface:

- fragment/structure edges whose target is missing/tombstoned/unavailable;
- Story Bible links with unresolved target IDs;
- incorporated/backlink receipts whose referenced source is unavailable;
- structural nodes no longer reachable from any selected entry point where reachability matters.

An unavailable protected reference is not automatically an error; it may be represented as intentionally unavailable if the current viewer cannot know more.

### 4.2 Setup/payoff and open-thread coverage

Using explicit CSW relationships, detect candidates such as:

- `sets-up` without any linked payoff;
- payoff with no recorded setup;
- foreshadow with no linked revelation/payoff;
- hook/open question still open after creator-selected milestone;
- a thread marked resolved while explicitly linked unresolved subthreads remain.

These are reminders, not doctrine. Creators may intentionally omit, subvert or leave unresolved.

### 4.3 Structural reachability and route coverage

Consume CSW-05 semantic edges to flag:

- required node unreachable from selected entry points;
- endpoint/orphan branch with no incoming route;
- revelation required downstream but all evidence paths optional/bypassed;
- branch created but never connected to a continuation/end;
- route whose prerequisite cannot be satisfied within the modeled graph;
- all choice alternatives collapsing immediately where the creator expected meaningful divergence.

CSW-06 records the evidence and disposition; it does not rewrite the graph.

### 4.4 Timeline/date consistency

Only when structured dates/order constraints exist, detect:

- impossible explicit ordering;
- two mutually exclusive fixed dates;
- Character age/date arithmetic mismatch where the relevant dates are structured and authorized;
- event/reference before an explicit prerequisite date;
- overlapping mutually exclusive occupancy/availability claims where semantics are declared;
- pin/version mismatch between a timeline fact and updated governed reference.

Freeform prose with ambiguous chronology yields at most a low-confidence review candidate, not a confirmed contradiction.

### 4.5 Naming/terminology consistency

Within authorized project scope, deterministic checks may surface:

- exact/normalized name variants;
- glossary term variants;
- probable renamed entity where stable reference evidence exists;
- capitalization/spelling variants for creator-marked terminology;
- duplicate labels that may refer to different entities.

The system must not auto-replace names. Homonyms, aliases and intentional style variants are common.

### 4.6 Unused and dormant material

Using Project Memory/backlinks and creator-selected time/scope rules, surface material that is:

- never referenced/used after creation;
- no longer connected to active threads/plans;
- archived/dormant but possibly relevant to current work;
- created for an earlier branch that is no longer selected.

This is rediscovery assistance, not deletion pressure. There is no engagement mechanic punishing unused material.

### 4.7 Contradiction candidates

A contradiction candidate requires traceable evidence from two or more authorized assertions/references that appear mutually incompatible under their declared semantic type.

The tracker distinguishes:

- `confirmed-by-creator` contradiction;
- `possible` contradiction;
- `version-drift` candidate;
- `context-dependent` difference;
- `intentional` inconsistency;
- `insufficient-evidence`.

Pre-authoritative fragments can disagree freely; disagreement is often creative exploration. A contradiction candidate must never collapse alternatives into one truth automatically.

## 5. Evidence contract

Every automated candidate must answer:

- What triggered this?
- Which exact objects/versions/projections were examined?
- Which rule/check/version produced the finding?
- What was the authorized analysis scope?
- What changed since the last evaluation?
- What is inference versus directly recorded fact?

The UI must let the creator open the source evidence from the candidate where still authorized.

Evidence is permission-filtered before graph expansion, counts, similarity, comparison or ranking. The absence/presence of inaccessible material must not leak through candidate counts or “there is another conflicting secret” hints.

## 6. Mystery and clue coverage

CSW-06 may analyze creator **design coverage**, not A9 runtime truth.

Advisory examples:

- planned revelation has only one possible clue/source;
- all clue sources live on one optional route;
- a clue has no recorded purpose/revelation link;
- a mystery-seed has unresolved questions with no creator-marked next step;
- a planned payoff relies on a revelation that can be bypassed.

The analysis does not decide whether a hypothesis is true, whether a player has discovered a clue, or whether a GM should reveal anything. Runtime A9 evidence/hypothesis state remains separate.

## 7. Creator dispositions and anti-nagging

For each candidate/thread the creator may:

- open/review;
- accept as an issue/to-do;
- mark resolved;
- dismiss;
- snooze until a time/milestone/version change;
- mark intentionally acceptable/unresolved;
- merge/link to an existing OpenThread;
- create a new OpenThread;
- add a note;
- ask for alternatives/possible fixes without applying them;
- reopen later.

Dismissal/snooze/intentionally-unresolved dispositions are durable and keyed to the relevant evidence versions/detection rule. The system must not repeatedly resurface the exact same unchanged finding. A materially changed source or detector version may create a re-evaluation prompt, but should explain why it reappeared.

## 8. Staleness and re-evaluation

A candidate becomes stale when:

- one of its evidence versions changes;
- authorization removes required evidence;
- a referenced object is tombstoned/archived/unavailable;
- the detection rule/version materially changes;
- its project/analysis scope changes.

Re-evaluation produces a new evaluation receipt or updates the candidate state while preserving prior history. It must not silently convert a dismissed finding back to active without explaining the changed basis.

## 9. Priority/severity presentation

The tracker may use presentation classes such as:

- info;
- review;
- likely-impactful;
- blocked-reference;

These are workflow aids, not universal quality or correctness scores. Severity should derive from explicit structural effects (for example, unreachable required endpoint) rather than opaque model confidence alone. User priority remains separately editable.

## 10. Optional AI

Optional AI may:

- compare selected authorized passages/fragments;
- explain why two assertions might conflict;
- summarize an open thread;
- propose possible reconciliations;
- suggest missed connections or follow-up questions;
- cluster authorized candidates for review;
- restate continuity findings in simpler language.

AI output remains advisory. It may not:

- edit source material automatically;
- declare objective canon from pre-authoritative fragments;
- resolve A9 hypotheses/runtime truth;
- access hidden material outside the authorized task projection;
- turn confidence into authority;
- mark candidates resolved/dismissed without user action.

A deterministic/manual review path remains available with AI disabled.

## 11. Integration with CSW-05

CSW-05 structural warnings can become ContinuityCandidates with source node/edge IDs, check version and creator disposition. CSW-06 adds persistence, evidence/history, cross-view aggregation and re-evaluation; it does not redefine the Lab’s structure.

OpenThreads can point back to Lab nodes/threads/revelations/payoffs. Resolving an OpenThread does not automatically edit or delete the underlying Lab node.

## 12. Integration with Story Bible/Project Memory

CSW-02 remains the source for authorized backlinks, references, stable fragment history and Story Bible projections. CSW-06 adds candidate/tracker metadata over those references rather than copying governed truths.

The tracker can project:

- unresolved/open threads;
- continuity candidates;
- stale references;
- unused/dormant items;
- recently resolved items;
- snoozed/intentionally-unresolved items;
- candidates grouped by project/section/thread/evidence source.

## 13. Recovery, concurrency and deletion

Candidate/thread dispositions use stable IDs, optimistic versions and idempotent commands. Conflicting edits surface current state rather than silently overwriting another collaborator’s disposition.

Deleting/tombstoning evidence does not erase candidate provenance where retention is required; the candidate may retain a safe tombstone/reference and become stale/unavailable. It must never preserve a protected payload after authorization no longer permits it.

## 14. Accessibility/mobile/nonvisual parity

Required experience:

- queue/list review with semantic headings;
- keyboard actions for all dispositions;
- screen-reader announcement of evidence count/type and stale state without leaking hidden content;
- no color-only severity/continuity state;
- mobile evidence drill-in/back navigation;
- textual timeline/graph evidence descriptions;
- non-drag grouping/reordering;
- batch review with explicit selection and undo where owning operation permits;
- clear difference between system suggestion and creator-confirmed issue.

## 15. Product voice

Continuity assistance should be calm, curious and non-prescriptive. Prefer language such as “This may need a look” or “These two notes appear to differ” rather than “Your story is wrong.” Respect intentional ambiguity, unresolved mystery, unreliable narrators, retcons, alternate drafts and stylistic choice.

Do not manufacture urgency, streaks, completion percentages or shame around unresolved work.

## 16. Acceptance contract

CSW-06 is design-complete when it defines:

- durable OpenThread identity/lifecycle;
- advisory ContinuityCandidate identity/lifecycle;
- deterministic dangling/reference, setup/payoff, structural, timeline, naming and unused-material checks;
- contradiction-confidence distinctions and traceable evidence;
- mystery/clue design coverage without runtime truth claims;
- durable dismiss/snooze/resolve/intentionally-unresolved anti-nagging behavior;
- stale evidence/version re-evaluation;
- authorization-before-analysis privacy;
- optional AI candidate-only role and no-AI path;
- recovery/concurrency/accessibility/mobile parity;
- clean handoff evidence for APM-04 and CSW-07.

No application implementation, migration, automatic truth correction, release/deployment, canonical promotion or CCTI-12-T04 work is authorized.