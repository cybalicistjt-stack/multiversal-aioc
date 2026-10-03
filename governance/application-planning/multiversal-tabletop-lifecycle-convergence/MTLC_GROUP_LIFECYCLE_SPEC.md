# MTLC Group and Human-Continuity Architecture

**Program:** MTLC — Multiversal Tabletop Lifecycle Convergence  
**Status:** OWNER_APPROVED_DESIGN_INPUT  
**Recorded:** 2026-10-03  
**Authority:** Product-design input for MTLC-01/02. This specification does not independently select current work or authorize later public-community release.

## 1. Governing principle

> **Multiversal treats the people as more durable than the game they are currently playing.**

A campaign is a game/content continuity. A session is an event. A character is a game identity. A **Group** is the human continuity layer.

Canonical conceptual hierarchy:

`User -> Group -> Campaign / One-shot / Trial Game / Game Event -> Session`

A campaign may end, pause, change GM, change system, or split without forcing the underlying group of people to disappear.

## 2. Responsibility boundary

### Group owns

- human membership and group roles;
- group identity, name and presentation;
- Group Lounge and group announcements;
- recurring availability, default game night and timezone defaults;
- broad attendance expectations and real-world logistics defaults;
- general table expectations that are legitimately group-scoped;
- accessibility and communication defaults that the user chooses to share;
- GM/organizer pool;
- active, past and planned campaigns;
- one-shots, trial tables and game events;
- guest pool, interests and waitlists;
- group invitations and accession/recruitment policy;
- group history and continuity across campaigns;
- appropriate block/mute/privacy relationships.

### Campaign continues to own

- campaign characters and campaign participation;
- campaign-specific rules and house rules;
- campaign-specific Session Zero / consent agreements;
- story, lore, scenes, NPCs, quests, factions and game state;
- campaign schedule overrides and Run Policy;
- campaign seats and campaign roles;
- campaign-specific communication spaces;
- campaign history, timeline and governed gameplay state.

No Group feature may create a competing source of truth for an existing Campaign, Session, Character, rules, inventory, consent, notification, permission, timeline or communication record.

## 3. Group operating-model presets

Do not build six incompatible products. Provide presets over a common policy model:

1. **Dedicated Table** — stable roster, recurring cadence, persistent campaign, optional waitlist.
2. **Open Table / West Marches** — larger member pool, session-by-session seats, caps/waitlist, variable roster.
3. **Gaming Club / Community** — multiple campaigns and GMs under one persistent human group.
4. **Seasonal Campaign** — explicit bounded commitment and renewal point.
5. **Organized-Play Style** — portable participation and changing tables/GMs where the governing rules support it.
6. **Professional/Paid Table** — commercial commitment may be layered later behind separate legal/billing gates; the Group model itself must not depend on payment.

Users see understandable setup questions, not an internal label such as “Policy Engine.”

## 4. Group policy dimensions

### Membership policy
- invite only;
- interest/application with approval;
- open with approval;
- open membership;
- guest only;
- public event with private membership.

### Scheduling policy
- fixed recurring;
- poll by exception/session;
- organizer selected;
- player proposed;
- asynchronous;
- hybrid.

### Attendance policy
- all required;
- quorum;
- GM + minimum players;
- variable roster;
- session-defined.

### Absence / Run Policy
- cancel;
- run without the character;
- GM control where permitted;
- player-selected proxy where permitted;
- side session / alternate game;
- asynchronous resolution.

### Seat policy
- permanent seat;
- first come;
- rotating priority;
- transparent waitlist priority;
- GM selection;
- lottery/random among equal candidates;
- member priority;
- reserved guest seats.

### GM model
- single GM;
- co-GMs;
- rotating GMs;
- session GM;
- campaign steward plus guest GMs.

Policies must be explicit and inspectable. Multiversal must not derive a hidden social-worth score from them.

## 5. Accession lifecycle

Default public/private-table accession is a configurable funnel rather than a one-step accept/reject gate:

`Discover -> Hard Compatibility Gate -> Expectation Preview -> Interested -> Conversation -> Trial Table -> Mutual Fit -> Guest/New Member -> Regular Membership -> Maintenance -> Pause/Exit -> Replacement/Return`

Groups may skip stages. A friends-only group may use `Invited -> Member`; a selective long-form table may use the full funnel.

### Hard compatibility before soft matching

Evaluate explicit constraints first when supplied:
- schedule/timezone;
- language;
- age requirement;
- online/in-person/hybrid format;
- game/system;
- seat availability;
- required device/voice conditions.

Do not collapse compatibility into an opaque percentage or desirability score.

### Expectation preview

Expose high-value expectations before a user invests in accession:
- system/game;
- schedule and expected duration;
- campaign/season length;
- RP/combat/exploration emphasis;
- tone and lethality where declared;
- attendance / Run Policy;
- PvP and character-conflict expectations;
- communication/voice/camera expectations;
- appropriate summarized consent/table expectations without leaking private responses.

### Interest, not job application

The default action is **I’m Interested**. Ask only for information not already available through a permission-appropriate profile/context. Avoid mandatory giant questionnaires.

Possible outcomes should include:
- invite;
- trial invitation;
- keep in guest pool;
- keep on waitlist;
- not this campaign;
- schedule incompatible;
- table full;
- follow group;
- close interest.

Do not frame ordinary compatibility decisions as public rejection marks.

## 6. Trial Table

A Trial Table is a first-class temporary participation flow with:
- temporary Game Event/Session access;
- appropriate pregen/temporary character access;
- consent/expectation acknowledgement;
- limited permissions;
- ordinary session/reconnect behavior;
- no forced permanent Group or Campaign membership.

Afterward both sides can independently choose whether to continue. Positive continuation requires mutual selection.

## 7. Membership is not campaign participation

### Example GroupMembership states
- Trial;
- Guest;
- Member;
- Organizer;
- Group Admin;
- Inactive;
- Hiatus;
- Alumni.

### Example CampaignParticipation states
- Not Participating;
- Interested;
- Waitlisted;
- Seat Offered;
- Active Player;
- Paused;
- Former Player;
- GM;
- Co-GM.

The exact enums are later implementation contracts. The architectural requirement is that these lifecycles remain independent.

## 8. Guest pool and waitlists

Groups may maintain a guest pool for one-shots, trials and vacancy fills.

Waitlists must use an explicit group/session policy, such as:
- FIFO;
- previously waitlisted priority;
- least-recently-played rotation;
- transparent lottery among equal candidates;
- member-before-guest priority.

The application must explain why a seat was offered. It must not publicly rank users by a generalized “reliability” or “quality” score.

Operational attendance facts may distinguish contexts such as attended, communicated absence, emergency, late, no-response and no-show, subject to privacy/retention policy. These facts are logistics evidence, not a human rating.

## 9. Season commitment

Campaigns may expose an explicit season/arc commitment:
- date/session range;
- recurrence;
- expected attendance;
- planned renewal/closure point.

At the boundary a Group may continue the same campaign, begin another arc, change GM, change system, pause or end the campaign while preserving the Group.

## 10. Hiatus, departure and return

Leaving a Campaign must not imply leaving the Group.

A user may, where permitted:
- leave a campaign and remain a Group member;
- enter hiatus through a declared date/window;
- pause campaign notifications;
- retain or release a campaign seat according to policy;
- opt into one-shot/guest invitations;
- leave the Group entirely.

Return should use campaign-memory/catch-up systems instead of requiring manual reconstruction.

## 11. Group health is operational, not psychological scoring

Group surfaces may show actionable facts:
- missing RSVPs;
- quorum met/not met;
- open seats;
- waitlist/guest interest;
- upcoming organizer/GM unavailability;
- season ending soon;
- pending private feedback;
- accession tasks.

Do not create opaque “group health,” personality, trustworthiness or player-worth scores.

## 12. Game Event / Game Night

A Group may own a Game Event above a specific Session. One Group gathering can offer a campaign session, one-shot, trial table or fallback game. This allows the social gathering to survive when a particular campaign lacks quorum.

## 13. Navigation direction

Desktop shell may eventually add **Groups** alongside Campaigns. The persistent context should be able to express:

`Group -> Campaign/Game Event -> Session`

Mobile must not simply add another permanent button beyond its compact navigation budget. Use context-aware projection and preserve primary tasks.

Group Home is an operational home, not a social-media feed. It should prioritize next game/quorum, personal next actions, current games, people/guest pool, important activity and Lounge communication.

## 14. Initial conceptual records

The Group layer may require records such as:

- `Group`
- `GroupMembership`
- `GroupPolicy`
- `CampaignParticipation`
- `GameEvent`
- `Seat`
- `RSVP`
- `Interest`
- `TrialParticipation`
- `WaitlistEntry`
- `Availability`
- `AttendanceEvent`
- `Hiatus`
- `Invitation`

These are conceptual responsibilities, not approved implementation schemas. MTLC-01 must first reconcile them against existing Campaign/Session/identity/invitation/permission records and eliminate duplicates.

## 15. MTLC mapping

- **MTLC-02:** Groups, private table formation and accession; Group entity, membership separation, interest/trial/guest/waitlist lifecycle.
- **MTLC-03:** Group Lounge plus campaign-specific communication.
- **MTLC-04:** Group/Game Event/Campaign scheduling, Run Policy, quorum, seats and waitlists.
- **MTLC-05:** appropriate group defaults plus campaign-specific Session Zero/consent.
- **MTLC-07:** Trial Tables, temporary seats, guests and Game Events use canonical session infrastructure.
- **MTLC-09:** departure, hiatus, return and catch-up contribute to human/campaign continuity.
- **MTLC-10:** Group persists during campaign pauses and between campaigns.
- **MTLC-12:** distinguish Find a Group, Find a Campaign/Game and Find a Session/Event.
- **MTLC-14:** golden lifecycles include `stranger -> interest -> trial -> member -> campaign -> absence -> return` and `campaign ends -> same group starts another game`.

## 16. Non-negotiable acceptance principles

1. No public generalized human reliability score.
2. Hard compatibility is explainable before soft recommendation.
3. Accession is mutual where the relationship requires mutual participation.
4. A Group can outlive every Campaign currently attached to it.
5. Existing Campaign/Session/Character authority is reused, not duplicated.
6. Membership, invitations, privacy and moderation are enforced below the UI.
7. Mobile, offline/reconnect, accessibility and provider neutrality remain first-class.
8. Public discovery waits for MTLC moderation/privacy/rights gates.
