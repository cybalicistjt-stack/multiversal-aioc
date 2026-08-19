# APW-06 — Shell, Navigation, Notifications, Visibility and Spoiler UX

**Work item:** APW-06  
**Attempt:** APW-06-attempt-001  
**Track:** Asynchronous Play & Persistent Workspace  
**Status:** bounded design/governance contract  
**Implementation authority:** none

## 1. Purpose

APW-06 defines the user-facing shell and interaction contract that makes Multiversal's contextual authority model understandable across Personal, Campaign and Session work without turning role, cadence, visibility or connectivity into hidden mode flags.

The shell is an orchestration and projection layer. It does not own Campaign truth, Personal resources, notifications, permissions, search truth, creator content, or spoiler security. Every surface must project already-authorized information from the owning domain.

The design must make five questions answerable at a glance:

1. **Where am I?** — Personal, a named Campaign, or an active Session/encounter.
2. **What authority applies here?** — the user's relevant contextual role/capabilities, never a permanent account caste.
3. **What needs attention?** — waiting, decision-required, result-ready, stale/recovery or creator-advisory work.
4. **What kind of information is this?** — Personal, reusable, Campaign-local, Sandbox, protected/hidden, or merely spoiler-filtered.
5. **Can I safely continue from here?** — including stale deep links, offline state, permission change and recovery.

## 2. Governing invariants

1. Account identity remains universal; Player, GM, Assistant GM, Observer and creator labels are contextual.
2. Authorization happens before shell projection, counts, search, ranking, badges, notifications, related-work discovery or deep-link previews.
3. The shell never creates authority by showing a control. Owning-domain authorization is rechecked at action time.
4. Personal, Campaign and Session context remain explicit and distinct.
5. Sandbox/Lab material is visibly noncanonical and cannot be visually confused with reusable or Campaign truth.
6. Spoiler Shield is an accidental-exposure preference only. It is not an authorization boundary and may never reveal that hidden material exists.
7. Notifications are durable projections of owning-domain events/state, not an alternate workflow engine.
8. Deep links are context-bearing hints, not permission tokens.
9. Counts and badges never include unauthorized items, even as anonymous totals.
10. Quieting and notification preference features must reduce pressure, not create streaks, loss aversion or repeated nagging.
11. Accessibility and nonvisual presentation carry the same context, authority and visibility meaning as visual treatments.
12. Optional AI is not required for shell, navigation, search, notification, visibility or spoiler behavior.

## 3. Global shell model

The shell has four persistent semantic regions. Visual arrangement may adapt by device, but semantics do not.

### 3.1 Context anchor

Shows the active context:

- **Personal** — account-owned independent workspace;
- **Campaign: <name>** — one authorized Campaign;
- **Session: <name> / Campaign: <name>** — active Session/encounter nested inside a Campaign.

The context anchor includes:

- current context name;
- parent context where applicable;
- connectivity state: connected / offline-cached / recovering;
- cadence indicator only when meaningful: live / asynchronous / hybrid;
- contextual role summary where meaningful.

Changing context is an explicit navigation action that clears or re-evaluates protected projections. Context switching may not retain Campaign-private search results, counts, recent items, assistance context or notification previews from the prior context unless the destination independently authorizes them.

### 3.2 Primary navigation

Navigation is capability- and context-aware, but stable enough to teach once.

Personal-capable destinations include:

- Home;
- Creator Command Center;
- Creator Workshop;
- Creative Library / Story Bible projects;
- Personal Characters and drafts where supported;
- Reference/library surfaces allowed by entitlement;
- notifications/attention;
- account/settings/help.

Campaign-capable destinations include:

- Campaign Home;
- current Scene/Session where applicable;
- Character and Campaign Activity surfaces;
- proposal/action state;
- GM review/inbox when authorized;
- Campaign-authorized creator/reference surfaces;
- Campaign-safe search;
- notifications/attention.

A destination's absence is not itself evidence of protected content. The shell does not expose disabled menu entries merely to reveal that a hidden capability or object exists.

### 3.3 Attention center

One shell-level attention entry aggregates authorized projections from owning systems without becoming a second queue.

It groups items by action semantics:

1. **Decision required** — user must choose, approve, clarify or resolve.
2. **Result ready** — a previously submitted or background-bounded action has a durable result.
3. **Waiting** — user has submitted work that is pending another authorized actor or bounded process.
4. **Needs recovery** — stale, conflicted, permission-changed, interrupted or ambiguous state requiring reconciliation.
5. **Informational** — state changed, invitation, completion receipt, context update.
6. **Creator advisory** — open thread, continuity candidate, reusable-material suggestion or creator attention state.

The shell stores only references/projection metadata necessary for display. The owning domain remains authoritative for state and disposition.

### 3.4 Universal search / command entry

The shell may expose a unified search/command entry, but query planning must apply active-context and authorization filters before retrieving or aggregating results.

Commands route to owning domains. Examples:

- `Switch to Personal`
- `Open Campaign: Ember Coast`
- `Continue writing <document>`
- `Show my pending actions`
- `Open Creator Workshop`
- `Find reusable locations tagged coastal`

The command layer cannot execute a mutation that the owning domain would not independently authorize.

## 4. Contextual role presentation

Role labels explain the user's relationship to the current context without exposing raw permission internals.

Examples:

- `GM in Ember Coast`
- `Player in Ember Coast`
- `Assistant GM in Ember Coast`
- `Observer in Ember Coast`
- `Creator / owner` for a Personal reusable asset

Where capability differs from the common role label, concise secondary text may explain the relevant action boundary, such as `Can review player proposals` or `View only`.

The UI must not imply:

- that GM is an account type;
- that a Campaign GM controls Personal resources;
- that a Player loses independent creator/reference capabilities;
- that visibility of a control equals permission to commit its action.

## 5. Waiting and review surfaces

### 5.1 Player waiting state

A submitted asynchronous Action displays:

- what the user submitted, within their visibility;
- submitted time / Campaign timeline marker where applicable;
- current state such as pending review or clarification requested;
- whether the user can withdraw or revise through the owning contract;
- safe next action;
- no hidden reviewer notes or hidden queue position.

### 5.2 GM `Things need you`

GM-facing items aggregate authorized APW-02/APW-03 review work:

- proposal review;
- clarification response;
- bounded Campaign Activity decisions;
- stale/conflict resolution;
- other explicit owning-domain decisions.

It does not include protected items merely because they exist elsewhere, and it does not merge independent decisions into one generic mutable record.

### 5.3 Creator attention

CSW-09 creator attention remains a creator-domain projection. The shell can surface an authorized count or top items, but opening it returns to the Creator Command Center with exact context.

`Needs attention` is advisory, not urgency. There are no streaks, red-loss counters, punitive overdue states or manipulative reminders for creative work.

## 6. Notification taxonomy

Every notification record has at minimum:

- notification ID;
- owning-domain event/reference;
- recipient subject;
- source context;
- type/class;
- created timestamp;
- read/dismissed state;
- deep-link resume token or safe destination;
- current authorization check requirement;
- redaction/projection policy.

### 6.1 Classes

| Class | Meaning | Default treatment |
|---|---|---|
| decision_required | User action blocks governed progress | prominent but noncoercive |
| result_ready | Durable result is available | normal attention |
| waiting_update | Pending work changed state | quiet by default after first acknowledgement |
| recovery_required | Stale/conflicted/interrupted state | prominent with recovery wording |
| informational | FYI state change | normal/quiet |
| invitation | Explicit invitation or membership event | normal |
| creator_advisory | Optional creative attention | quiet, batchable, easily muted |
| system_safety | Account/security/recovery matter | prominent according to owning policy |

Notification class does not override visibility. Content is rendered only after recipient authorization and context-safe projection.

## 7. Notification preference and quieting model

Users may control, where applicable:

- in-app visibility;
- push/email eligibility when those delivery systems later exist;
- per-Campaign quieting;
- creator-advisory batching/muting;
- waiting-update frequency;
- quiet hours or digest preferences when supported later.

Governed decisions may remain visible in the in-app attention center even when external delivery is muted, but the product must not repeatedly pressure the user to act.

No notification preference creates automatic consent, automatic Campaign action, automatic creator task execution or background authority.

## 8. Deep links and return-to-context

A deep link contains a safe target descriptor, not a bearer permission.

Recommended semantic fields:

- destination type;
- stable target ID;
- expected context ID;
- optional expected version/revision;
- return context;
- source notification or surface;
- requested subview/action intent.

On open:

1. establish current subject identity;
2. re-authorize destination/context;
3. re-resolve current target/version;
4. apply visibility filtering;
5. either open the safe target or enter a recovery state.

Recovery outcomes include:

- target moved or renamed → resolve current identity and explain;
- target version changed → open latest safe view, with stale notice when relevant;
- permission revoked → generic unavailable state with no protected detail;
- Campaign left/removed → return to safe Personal/Campaign list;
- offline with cached safe representation → mark cached and read-only where required;
- offline without safe cache → explain that connection is required;
- target deleted/tombstoned → show authorized tombstone/reference-safe state;
- Session ended → return to Campaign continuation context.

## 9. Visibility classes and presentation

These are UX classifications, not replacement authorization models.

### Personal

Owned or independently accessible in Personal context. Presentation should identify `Personal` when context might otherwise be ambiguous.

### Reusable

Independent reusable definition/template/library asset. Show source/provenance and version where useful.

### Campaign-local

Belongs to or is governed by a specific Campaign. Display Campaign identity in cross-context surfaces.

### Sandbox

Disposable/noncanonical experiment. Always carries an explicit `Sandbox` / `Not Campaign state` treatment. Visual styling alone is insufficient; accessible text must say it.

### Protected/hidden

Not a display style. Unauthorized material is absent from projections entirely. The shell cannot reveal its title, count, category, relationship, cardinality or existence.

### Spoiler-filtered

Authorized material intentionally deemphasized/obscured by user preference. It remains authorized and can be revealed by the user. Treatment must state that Spoiler Shield is active and that revealing is a preference action, not a permission escalation.

## 10. Spoiler Shield

Spoiler Shield helps reduce accidental metagame exposure for content the user is already authorized to access.

It may:

- hide titles/previews behind a reveal affordance;
- reduce unsolicited related-content suggestions;
- omit spoiler-sensitive snippets from recents/search previews;
- suppress creator-reference cross-links in Player-oriented views when configured;
- require deliberate reveal for marked content.

It may not:

- grant or revoke access;
- substitute for D05/owning-domain visibility filtering;
- return counts for hidden content;
- expose that an unauthorized clue, secret, NPC state or GM note exists;
- block an authorized GM from governed Campaign work through fake security semantics;
- be represented as parental control or child-safety security.

If Spoiler Shield is bypassed, disabled or unavailable, authorization safety must remain unchanged.

## 11. Authorization-safe counts, badges and search

Pipeline invariant:

`authorize candidate set → visibility project → aggregate/count/rank → render`

Never:

`aggregate all → redact individual rows`

This applies to:

- unread counts;
- pending-review badges;
- search result totals;
- `N related items`;
- Campaign usage counts;
- creator open-thread counts;
- notification summaries;
- autocomplete;
- empty states;
- graph/topology previews.

If the authorized set is empty, the UI uses an ordinary empty state and does not hint at filtered hidden results.

## 12. Context switch safety

Switching Personal ↔ Campaign ↔ Session is a fresh projection boundary.

The shell must invalidate or re-evaluate:

- search results and query suggestions;
- notification previews;
- attention counts;
- recent-item previews;
- related-content panels;
- creator-assistance source scope;
- role/capability labels;
- cached Campaign-private cards;
- command suggestions that depended on the prior context.

Open unsaved Personal creative work may remain available through its owning recovery contract, but Campaign-private context may not bleed into it merely because the user switched tabs or workspaces.

## 13. Connectivity and recovery presentation

### Connected

Normal behavior with fresh authorization.

### Offline/cached

The shell must show an explicit offline state. Only previously authorized cache permitted by owning policy may be shown. Mutation controls become unavailable, queued, or proposal-only strictly according to existing offline contracts; APW-06 does not invent offline write authority.

### Recovering/reconnecting

Show that state is being revalidated. Avoid optimistic counts or stale protected previews until authorization and version checks complete.

Ambiguous mutation outcomes route to owning-domain status lookup/idempotency recovery rather than offering a blind retry.

## 14. Mobile, keyboard and nonvisual contract

Equivalent semantics are mandatory across presentation modes.

### Mobile

- context anchor remains visible or one action away;
- context switcher is not hidden behind role-specific menus;
- attention center preserves classes and safe counts;
- bottom/navigation drawer ordering remains predictable;
- spoiler reveal requires deliberate activation;
- destructive/commit actions retain owning-domain confirmation rules.

### Keyboard

- context switcher, primary navigation, attention center, search/command and spoiler reveal are fully keyboard reachable;
- focus returns predictably after context switch or modal dismissal;
- keyboard shortcuts never bypass authorization or confirmation.

### Screen reader / nonvisual

Every relevant item exposes:

- current context;
- role/capability summary when relevant;
- information class (`Personal`, `Campaign-local`, `Reusable`, `Sandbox`, `Spoiler hidden`);
- notification class/state;
- whether content is cached/offline/stale;
- safe action labels.

Color, iconography, blur and spatial placement may reinforce semantics but cannot be the only carrier.

### Reduced motion

Context switches, attention changes and spoiler reveals function without essential animation. Motion never conveys exclusive state.

## 15. Product voice

Shell and assistance language should be warm, calm, encouraging and concise—more like a capable mentor than an administrator.

Examples of desired framing:

- `You have 2 decisions waiting in Ember Coast.`
- `Your action is still waiting for review.`
- `This link is no longer available in this Campaign.`
- `Spoiler Shield is hiding this preview. You can reveal it.`
- `You're offline. This is the last safe copy we have.`

Avoid blame, panic language, fake urgency and obsequious praise.

## 16. Deterministic acceptance scenarios

APW-06 must be testable without AI or external notification delivery.

Required scenario families:

1. Personal → Campaign → Session → Personal context switch with no protected cache bleed.
2. Same user is GM in Campaign A and Player in Campaign B; shell shows context-specific labels only.
3. Player submits APW-02 action; waiting projection shows safe state without GM-private information.
4. GM has three authorized review items and one inaccessible item; badge/count equals three.
5. Hidden Campaign material does not affect search total, autocomplete, empty states or related counts.
6. Spoiler Shield hides an authorized preview; reveal changes only UX, not authorization.
7. Spoiler Shield disabled; unauthorized material remains inaccessible.
8. Deep link opened after permission revocation returns generic unavailable state without protected metadata.
9. Deep link opened after version change resolves current safe identity and marks stale expectation where relevant.
10. Offline cached Campaign card is labeled cached and cannot invent write authority.
11. Reconnect revalidates counts/previews before rendering protected data.
12. Creator advisory notifications can be muted/batched without deleting underlying CSW state.
13. Sandbox recent item is clearly marked noncanonical and cannot be mistaken for Campaign state.
14. Screen-reader path communicates context, role, visibility class and notification state without visual cues.
15. Mobile path allows context switch, attention review, search and safe deep-link recovery.
16. Ambiguous prior mutation routes to status/recovery rather than duplicate submission.

## 17. Downstream seams

APW-06 supplies:

- **APM-05** with Connected Cozy context/participant/notification/visibility presentation rules;
- **CSW-10** with shell/navigation/creator-assistance integration requirements;
- **APW-07** with exact persistence/recovery/security acceptance cases;
- **APW-08** with shell implementation handoff inputs.

It does not authorize those later tranches or implementation.

## 18. Completion condition

APW-06 is design-complete when the shell can be implemented from this contract such that users can reliably identify context, applicable contextual authority, waiting work and information classification; authorization precedes all aggregates; Spoiler Shield remains purely UX; deep links recover safely; notification pressure is bounded; and desktop/mobile/nonvisual/offline behavior carries equivalent meaning.
