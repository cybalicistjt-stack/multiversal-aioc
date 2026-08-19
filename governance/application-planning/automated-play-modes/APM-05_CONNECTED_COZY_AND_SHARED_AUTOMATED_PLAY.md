# APM-05 — Connected Cozy and Shared Automated Play

**Work item:** APM-05  
**Attempt:** APM-05-attempt-001  
**Track:** Automated Play Modes  
**Status:** bounded design/governance contract  
**Implementation authority:** none

## 1. Purpose

APM-05 extends the governed CozyMode loop from one person into **invited, known-participant shared play** without creating a second rules engine, pooled participant authority, public matchmaking, or an AI-operated social simulation.

Connected Cozy is a participation/orchestration experience over existing owning domains. It coordinates people, activities, contributions, automation and presentation; it does not become authoritative truth for Characters, Campaigns, resources, relationships, crafting, investigations, creator content or account permissions.

The core shared loop is:

`Invite → Join with explicit bounds → Choose shared activity → Declare individual contribution/choice → Validate authority/resources/version → Reserve if needed → Execute governed operation → Commit one attributable result → Project per participant visibility → Continue / pause / leave / finish`

Optional automation may shorten routine work, but the shared loop remains inspectable and deterministic at every authoritative boundary.

## 2. Controlling invariants

1. Connected Cozy is an **experience**, not a permanent account role.
2. Initial participation is invitation-only. No public stranger discovery or matchmaking is authorized.
3. Every participant has independent identity, authorization, visibility and delegation.
4. One participant's authority can never be silently pooled with another's.
5. The host/owner may administer the shared Cozy space but cannot spend, consent, choose or speak canonically for another human participant.
6. Shared automation is bounded by APM-01 operation classes and current owning-domain authorization.
7. Human choice remains human-required wherever APM-01, APM-02, Campaign policy or an owning domain requires it.
8. Shared resource contribution uses explicit reservation/commit/refund semantics and cannot double-spend Personal or Campaign resources.
9. Shared social/relationship activity never treats AI narration or another participant's action as human consent.
10. APW-06 authorization-before-aggregation governs invitations, counts, badges, notifications, search, waiting state and deep links.
11. Hidden information is filtered per participant before presentation or optional-AI context.
12. Solo Cozy and Connected Cozy share the same governed history model; transition does not create silent Character/world forks.
13. Leaving or revocation removes future authority but does not erase already-committed attributable history.
14. No AI provider is required for core Connected Cozy operation.
15. APM-05 preserves a future seam for multiplayer AutoGM but does not require or authorize it.

## 3. Connected Cozy space model

APM-05 defines a semantic `ConnectedCozySpace` orchestration aggregate. Implementation persistence belongs to the later handoff.

A space has at minimum:

- stable `spaceId`;
- display name;
- owner/host subject ID;
- owning or host context reference;
- source/origin reference when created from Solo Cozy;
- participant membership records;
- shared activity/project references;
- explicit automation policy/delegation reference;
- visibility policy reference;
- lifecycle state;
- current version;
- created/updated timestamps;
- provenance/history references.

The space does **not** own copies of Character, resource, inventory, relationship or Campaign truth. It stores governed references and orchestration state only.

### 3.1 Space lifecycle

- `draft`
- `inviting`
- `ready`
- `active`
- `waiting_for_choice`
- `waiting_for_contribution`
- `paused`
- `recovering`
- `completed`
- `archived`
- `revoked`

Lifecycle transitions are explicit and versioned.

### 3.2 Host context

A Connected Cozy space may be attached to a governed shared destination allowed by the owning architecture, such as:

- a Campaign-backed shared context; or
- a later bounded collaboration workspace defined by the implementation handoff.

APM-05 does not invent a fourth global account role/context axis. If a Solo Cozy Personal activity is shared, the operation creates or binds to an explicitly governed shared space; it does not silently convert another user's Personal workspace into shared authority.

## 4. Solo Cozy → Connected Cozy transition

Sharing is explicit.

A Solo Cozy owner chooses `Invite others / make shared` and receives a preview of:

- which activity/project is proposed for sharing;
- which state remains Personal/private;
- which references are copied, linked or proposed into the shared space;
- which resources are **not** contributed until separately authorized;
- what automation policy would apply;
- who may be invited;
- what happens if the share is canceled.

The transition produces a new shared orchestration identity with provenance back to the Solo source. It does not mutate the Solo source into a multi-owner object.

Personal private notes, journals, hidden ideas and unrelated resources remain Personal unless the owner explicitly shares a permitted derivative/reference.

A user may later continue Solo Cozy independently. Shared committed results only affect a Personal or Campaign owning domain when that domain's explicit operation committed them.

## 5. Participant membership and authority

### 5.1 Membership record

Each participant membership records:

- subject ID;
- invitation ID;
- inviter/issuer;
- state;
- joined timestamp;
- current capability set;
- contribution/delegation bounds;
- visibility projection policy;
- notification preferences where applicable;
- leave/revoke history.

Membership states:

- `invited`
- `accepted`
- `declined`
- `active`
- `temporarily_disconnected`
- `left`
- `revoked`

### 5.2 Minimal contextual capabilities

Capabilities may include:

- view shared activity;
- contribute to allowed projects;
- make own Character/activity choices;
- propose shared activity changes;
- participate in live co-op window;
- submit asynchronous contribution;
- manage own contributed resources;
- manage invitations (host/delegated only);
- configure bounded automation (host/delegated policy only);
- pause/close shared space (host/delegated where policy permits).

Capabilities are contextual. There is no global `ConnectedCozyPlayer` or `ConnectedCozyGM` account role.

### 5.3 Host authority limits

The host may administer the space but may not:

- spend another participant's resources;
- accept an irreversible choice for another participant;
- consent to relationship/social actions for another human;
- change another participant's Personal Character truth without owning-domain authority;
- reveal hidden Campaign information;
- extend another participant's automation delegation;
- bind a participant to a Campaign without the required membership/invitation path.

## 6. Invitation contract

An invitation contains only the safe information needed to decide whether to join:

- inviter identity;
- space/activity display summary;
- owning context identity when authorized to disclose;
- expected participation style/cadence;
- requested capability/contribution scope;
- whether optional AI narration is enabled/available;
- expiration or revocation state where applicable.

The invitation does not reveal protected Campaign details, hidden participants, secret activity branches or unauthorized resource state.

Accepting an invitation:

1. authenticates the subject;
2. revalidates the invitation and current space version;
3. checks entitlement/context membership requirements;
4. presents current participant-specific visibility;
5. records explicit acceptance;
6. creates bounded membership;
7. does **not** grant resource contribution or automation delegation beyond what is separately confirmed.

## 7. Shared activity families

Connected Cozy may coordinate activity families that already have owning-domain semantics and can safely support multiple participants.

Initial bounded families:

- cooperative preparation/logistics;
- shared crafting/repair/maintenance projects;
- collaborative research/investigation where visibility permits;
- settlement/home/base improvement projects;
- light exploration/planning activities;
- shared creative/journal/worldbuilding artifacts where explicitly collaborative;
- social/relationship activities with explicit human consent boundaries;
- cooperative resource gathering/management where governed;
- shared downtime goals and project milestones.

Not automatically supported:

- irreversible advancement choices for another human;
- GM-required adjudication without a GM/proposal path;
- unrestricted market/business/kingdom simulation;
- public stranger social spaces;
- autonomous romance/intimacy consent;
- hidden Campaign truth discovery beyond current participant authorization;
- unbounded automated combat/adventure direction;
- multiplayer AutoGM campaign direction.

## 8. Shared project model

A shared Cozy project is a durable orchestration aggregate referencing owning-domain state.

Recommended fields:

- `projectId`;
- space ID;
- activity family;
- owning-domain/project definition reference;
- current milestone/state;
- participant contribution rules;
- resource requirement/reservation references;
- choice barriers;
- stop conditions;
- expected version;
- committed contribution ledger references;
- controller delegation reference;
- completion/result references.

The project may coordinate contributions but cannot become a parallel inventory, crafting, relationship or advancement truth store.

## 9. Contribution packet

Every contribution is attributable to one participant or one explicitly delegated controller operation.

A contribution packet contains:

- contribution ID / idempotency key;
- space/project ID;
- participant subject ID;
- actor/controller identity if different;
- intended operation;
- referenced asset/resource IDs;
- quantity/amount where applicable;
- expected source versions;
- expected project version;
- visibility/provenance metadata;
- optional participant note;
- submit timestamp;
- current state.

Contribution states:

- `draft`
- `submitted`
- `validating`
- `reserved`
- `awaiting_choice`
- `awaiting_other_contribution`
- `committing`
- `committed`
- `rejected`
- `canceled`
- `stale`
- `recovering`
- `refunded_or_released`

## 10. Resource reservation, commit and refund

Shared contributions use a two-phase resource rule whenever an operation could consume scarce state.

### Phase A — reserve

The owning domain validates:

- subject ownership/authority;
- quantity/availability;
- entitlement/pack requirements;
- expected version;
- conflicting reservations;
- project compatibility;
- any human/GM approval requirement.

A reservation is attributable and time/state bounded.

### Phase B — commit

Commit occurs only when:

- required participant choices exist;
- all required reservations remain valid;
- project/current versions still match;
- current authorization remains valid;
- owning-domain validation passes.

Commit emits the authoritative owning-domain result/event and records project contribution provenance exactly once.

### Release/refund

If a contribution is canceled, becomes stale, loses authorization or the project is abandoned before commit, reservations are released according to the owning domain. The Connected Cozy layer may not invent compensating resources.

## 11. No pooled authority

A shared controller must never reason as if the participant group has the union of all permissions.

For every operation, effective authority is bounded by the intersection of:

1. operation class under APM-01;
2. space/project policy;
3. initiating participant's current authorization;
4. any explicit delegation to the controller;
5. owning-domain rules;
6. current resource/state version;
7. required consent/choice barriers;
8. destination visibility/context policy.

Another participant's permission cannot satisfy a missing permission unless the owning domain explicitly defines a multi-party approval operation.

## 12. Human choice and consent barriers

Human-required choices include, at minimum:

- spending another person's Personal resource;
- irreversible Character advancement/identity choice;
- agreeing to join/leave/bind to a shared context;
- consenting to social/relationship actions that require human consent;
- publishing or sharing Personal material;
- accepting a proposal that changes a participant's owned canonical state;
- extending automation delegation;
- revealing a participant's private material.

AI narration, host preference, majority vote or inactivity cannot substitute for required individual consent.

A group preference may decide only matters explicitly owned by the shared project/space policy.

## 13. Social and relationship activity

Connected Cozy may support shared scenes and relationship-maintenance activities, but the system distinguishes:

- descriptive/narrative flavor;
- a proposal for a social action;
- a participant's own authored response;
- a governed relationship/reputation mutation.

An AI narrator may portray nonhuman setting flavor only within its allowed presentation scope. It cannot impersonate a human participant's consent, private intent or canonical statement.

Relationship/reputation mutations remain owned by their existing domains and policies.

## 14. Asynchronous contributions

Async contribution is the default shared persistence path.

Each participant may submit a bounded contribution and disconnect. The system:

1. stores the attributable packet;
2. validates/reserves as permitted;
3. waits for other required human/GM inputs;
4. commits only when all governing conditions hold;
5. emits durable participant-safe result notifications;
6. supports idempotent status lookup on return.

Waiting does not grant the automation controller permission to fill missing human decisions.

## 15. Live co-op windows

Connected Cozy may temporarily become synchronously active without creating a different state engine.

Live contributions use the same authoritative endpoints, expected-version checks, reservation rules and event history as asynchronous contributions.

If two valid contributions race:

- owning-domain version/order rules decide which can commit;
- the losing/stale contribution receives a recoverable stale state;
- UI offers re-evaluate/resubmit, not silent last-write-wins.

A live window ending simply returns the space to asynchronous cadence.

## 16. Automation controller contract

The shared Cozy controller is a nonhuman service actor under APM-01.

It may perform only explicitly delegated operation classes such as:

- routine project progress where all inputs are already authorized;
- deterministic event/opportunity selection from allowed tables/packages;
- summary/projection generation from authorized state;
- bounded maintenance/upkeep operations under explicit budgets;
- reservation/status housekeeping where owning domains permit;
- stop-condition evaluation.

It must stop for:

- human-required choice;
- missing or revoked delegation;
- stale state/version conflict;
- resource conflict;
- consent boundary;
- GM/adjudication-required action;
- visibility ambiguity;
- entitlement loss;
- unsupported operation family;
- automation budget/limit exhaustion;
- ambiguous prior mutation outcome.

The controller never inherits host authority merely because the host created the space.

## 17. Optional AI boundary

Optional AI may:

- narrate participant-safe summaries;
- suggest activity options;
- propose flavor/scene variations;
- rephrase participant-authored text;
- summarize shared project progress;
- generate candidate nonauthoritative creative material.

Optional AI may not:

- choose for a human participant;
- spend resources;
- approve contributions;
- resolve mechanics;
- manufacture hidden facts;
- reveal cross-participant private context;
- consent on behalf of a human;
- change relationship state;
- extend delegation;
- publish/canonicalize content;
- bypass an owning domain.

AI context is constructed **after** participant-specific authorization and visibility filtering. Group AI context cannot contain the union of private participant material unless every included source is explicitly shared and authorized for the operation.

No-AI mode retains the complete shared loop using deterministic prompts, tables, project rules, summaries and human-authored text.

## 18. APW-06 shell, attention and notification integration

Connected Cozy uses APW-06 semantics directly.

Notification classes include:

- invitation;
- decision required;
- contribution accepted/committed;
- contribution stale/recovery required;
- waiting for another participant;
- project result ready;
- participant joined/left when authorized;
- informational project update.

Badges/counts are authorization-filtered before aggregation.

Deep links include safe space/project/contribution identity and current context hints, then reauthorize on open.

The shell must show when the user is in a shared Cozy experience and which contextual capabilities apply, without implying a global role.

## 19. Visibility model

Each projection is participant-specific.

A participant may see:

- space identity and safe participant list where policy permits;
- own contribution details;
- shared committed project state;
- shared notes/artifacts explicitly visible to them;
- safe waiting/result status;
- Campaign information already authorized to them.

They may not infer from counts, AI context, badges, project prerequisites or notification wording that unauthorized hidden material exists.

If a Campaign-backed project includes GM/private state, that state is filtered before participant projection exactly as in ordinary Campaign use.

## 20. Shared artifact ownership

Connected Cozy must distinguish:

- **Personal source** — remains owned by its creator;
- **shared derivative/artifact** — owned according to the shared project's collaboration policy;
- **Campaign-local result** — governed by Campaign/domain policy;
- **reusable derivative** — requires explicit CSW/APW reuse/clone/promote path;
- **private participant note** — remains private until explicitly shared.

Host status alone does not transfer another participant's copyright-like authorship/provenance or Personal ownership inside the product model.

## 21. Leave, revoke and rejoin

### Leave

A participant may leave when permitted. On leave:

- future authority is removed;
- uncommitted reservations are released according to owning policy;
- already committed contributions remain in history;
- their private Personal state remains theirs;
- shared artifacts retain provenance;
- notifications/deep links become safe historical/unavailable projections as appropriate.

### Revoke

Authorized administrators may revoke participation subject to shared-context policy. Revocation is not retroactive deletion of committed history.

### Rejoin

Rejoin requires a fresh current invitation/authorization check. Old delegation, reservations and stale UI state do not revive automatically.

## 22. Host disconnect or departure

Host connectivity is not shared-play authority.

If the host disconnects:

- already-authorized bounded async work may continue only within existing policy;
- missing host-required decisions wait;
- no participant receives host privileges automatically.

If the host leaves/revokes the space:

- the space follows explicit ownership/administration policy;
- it may pause, transfer administration through a separately authorized process, or close;
- authority is never transferred by inactivity alone.

## 23. Pause, cancel, completion and archive

### Pause

Stops new automated progress and preserves state/reservations according to owning policy.

### Cancel project

Requires authority, releases uncommitted reservations, preserves committed history and records reason/provenance.

### Complete

Completion records final shared project result(s), participant contribution provenance and any owning-domain committed outcomes.

### Archive

Removes the space from active attention without deleting governed history or breaking referenced artifacts.

## 24. Recovery and idempotency

All mutating Connected Cozy operations require stable idempotency/status identity.

Recovery cases include:

- duplicate contribution submit;
- disconnect during reservation;
- disconnect during commit;
- participant revoked while waiting;
- resource changed after reservation;
- project version advanced by another contribution;
- host disconnect;
- AI/provider unavailable;
- notification delivery delayed;
- deep link stale;
- space completed while participant offline.

On uncertain outcome, the client asks authoritative status first. Blind retry is prohibited.

Exactly-once semantics apply to the authoritative owning-domain mutation, not merely the UI request.

## 25. Solo return and shared-to-Personal continuation

A participant may leave Connected Cozy and continue independent Personal work, but there is no implicit copy of protected shared truth.

Allowed patterns include:

- continue their pre-existing Solo Cozy source;
- create an explicitly permitted reusable derivative through CSW-08/APW-05;
- save their own private notes;
- clone a shared artifact only when collaboration/context policy permits;
- reference a Campaign result only under current authorization.

The app must not offer `take everything with me` semantics that copy other participants' private material or Campaign-private state.

## 26. Multi-player AutoGM future seam

APM-05 deliberately leaves reusable infrastructure for later multiplayer AutoGM:

- participant membership;
- per-subject authority/visibility;
- contribution/action packets;
- shared deterministic ordering;
- human choice barriers;
- invitation/leave/rejoin;
- participant-safe narration projection;
- notification/recovery.

It does **not** define automated shared combat/adventure direction or grant a controller broader GM authority.

## 27. Mobile and accessibility contract

### Mobile

- invitation acceptance shows scope before join;
- current shared space/context and participant-safe waiting state remain visible;
- contribution/reservation confirmation is usable on small screens;
- live and async views share the same semantic actions;
- leave/pause/recovery actions are findable without hidden gestures.

### Keyboard

All invitations, contribution choices, project navigation, participant controls and recovery actions are keyboard reachable.

### Screen reader/nonvisual

Expose:

- current shared space and host context;
- membership/capability state;
- project state;
- contribution state;
- whether a choice is human-required;
- resource reservation/commit status;
- visibility class;
- waiting/recovery reason;
- participant-safe result summary.

Color, avatar position and animation cannot be the sole carriers of participant/contribution state.

### Reduced motion

Live co-op presence and project progress remain understandable without animated presence indicators or transitions.

## 28. Product voice

Connected Cozy should feel welcoming, cooperative and low-pressure.

Preferred examples:

- `Maya invited you to help with the observatory project.`
- `Your materials are reserved. Nothing will be spent until the project can commit.`
- `We're waiting on one participant choice.`
- `That contribution changed while you were away. Review it before resubmitting.`
- `You left the shared space. Your Personal work is unchanged.`

Avoid competitive pressure, blame for absence, streak language, social guilt and fake urgency.

## 29. Deterministic acceptance scenarios

Required scenario families:

1. Solo Cozy owner creates invited Connected Cozy space without mutating source Personal state.
2. Invitee accepts current invitation and receives only bounded capabilities.
3. Declined/revoked/expired invitation cannot create membership.
4. Host cannot spend participant-owned resource without participant contribution authorization.
5. Two participants contribute scarce resources; reservations prevent double spend.
6. One reservation becomes stale before commit; project stops/re-evaluates without partial duplicate mutation.
7. Async participant submits contribution and disconnects; exactly one result commits later.
8. Live contributions race; one becomes stale and recovers without last-write-wins overwrite.
9. Human-required advancement/social choice blocks controller automation.
10. Host disconnects; no host authority transfers automatically.
11. Participant leaves; uncommitted reservations release and committed provenance remains.
12. Participant rejoins only through fresh current authorization; old delegation does not revive.
13. Hidden Campaign fact does not affect unauthorized participant counts/badges/AI context.
14. Optional AI unavailable; deterministic/no-AI shared loop completes.
15. AI suggestion cannot spend, consent or commit mechanics.
16. Shared social activity requires each human's relevant consent/choice.
17. Stale deep link after membership revocation returns generic safe unavailable state.
18. Notification counts exclude inaccessible shared spaces/items.
19. Participant creates permitted Personal derivative without copying protected shared state.
20. Space completes while participant offline; return uses durable status/result lookup.
21. Screen-reader path exposes membership, project, contribution and choice state.
22. Mobile path supports invitation, contribution, waiting, leave and recovery.
23. Duplicate submit with same idempotency key produces one authoritative result.
24. Public stranger discovery is absent from initial surface/contract.

## 30. Downstream seams

APM-05 supplies:

- **CSW-10** with shared creator/assistance integration constraints;
- **APW-07** with multi-user persistence, idempotency, revocation, hidden-information and cross-device recovery scenarios;
- **APM-06** with Connected Cozy safety/recovery/acceptance inputs;
- **APW-08** with future implementation handoff dependencies.

## 31. Completion condition

APM-05 is design-complete when invited shared Cozy can be implemented with explicit participant authority, independent per-person consent/delegation, deterministic resource/contribution handling, async/live parity, APW-06-safe notification/visibility behavior, leave/rejoin and recovery, no public matchmaking, no pooled authority and no required AI provider.
