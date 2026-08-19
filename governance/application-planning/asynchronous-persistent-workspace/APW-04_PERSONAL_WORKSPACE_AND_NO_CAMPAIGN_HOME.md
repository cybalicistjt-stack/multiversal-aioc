# APW-04 — Personal Workspace and No-Campaign Home

**Work item:** APW-04  
**Program:** APW — Asynchronous Play & Persistent Workspace  
**Version:** 0.1.0  
**Status:** DESIGN CONTRACT — READY FOR GOVERNED REVIEW  
**Owner and final authority:** John Brandon Turner  
**Date:** 2026-08-18

## 1. Decision

Multiversal must remain useful to a valid user who belongs to **zero Campaigns**.

The account-level landing surface is therefore a **Personal Home / Personal Workspace**, not a forced Player dashboard, forced GM dashboard, empty Campaign picker, or hidden developer mode.

Personal context is a first-class governed scope from APW-01. It may organize and expose resources that are genuinely Personal-owned, entitled general/reference content, safe invitations/notifications, Personal Characters/drafts where owning-domain successor contracts permit them, CSW Creative Library/Creator Projects, Personal notes/references, and explicitly non-Campaign practice/sandbox work.

Personal Home does **not**:

- create global Player or GM authority;
- make Campaign-private material Personal property;
- copy Campaign truth into a Personal truth store;
- make practice/sandbox results Campaign truth or canonical content;
- turn a Personal Character into a Campaign Character without explicit Campaign acceptance/binding;
- bypass Campaign, Character, entitlement, creator, visibility, publication or canonical-promotion authority.

## 2. Personal Home purpose

A useful Personal Home answers:

- What can I do even if I am in no Campaign?
- What Characters and drafts do I own or control outside a Campaign?
- What creative projects/ideas am I working on?
- What reference content am I entitled to use?
- What do I want to continue?
- Are there invitations or safe account-level notifications waiting for me?
- What Personal practice/sandbox work exists?
- What did I recently use, and can I still access it now?
- Which Campaigns are available when I do have memberships, and what role will I have there?

The surface should feel like the user's Multiversal home, not a limbo before “real” Campaign use.

## 3. Personal Home information architecture

Baseline Personal Home areas:

1. **Continue** — permission-revalidated recent Personal work and safe references to currently authorized Campaign work.
2. **Characters** — Personal-owned Character drafts/Characters and safe Campaign-binding summaries.
3. **Creative Library** — CSW Creative Fragments, Creator Projects, Story Bibles and Project Memory.
4. **Practice & Sandbox** — non-Campaign experiments, test encounters, build experiments or lab work where owning domains permit.
5. **Reference Library** — entitled general/reference content independent of Campaign role.
6. **Invitations** — current invitations safe to show at account level.
7. **Notifications / Waiting** — Personal/account-level notifications plus safe summaries of work requiring action in currently authorized contexts.
8. **Campaigns** — currently discoverable Campaign memberships/invitations with contextual roles, not account identity.
9. **Imports / Exports / Backups** — bounded Personal-resource portability and recovery surfaces.
10. **Account & Entitlements** — subscription/access state, provider-neutral account/security/recovery links and nonsecret entitlement summaries.

Each area is a projection over its owning domain. Personal Home is an orchestrating shell, not a monolithic Personal database.

## 4. Resource classification

### 4.1 Personal-owned resources

Where the owning domain supports ownership, examples include:

- CSW Creative Fragments and Creator Projects;
- Personal notes, saved collections, favorites and references;
- Personal templates and reusable creator assets;
- Personal Character drafts/Characters under an additive Character-context successor contract;
- Personal sandbox/lab definitions or snapshots explicitly classified nonauthoritative/non-Campaign;
- user-authored exports/import mappings and Personal recovery metadata.

### 4.2 Personal-accessible but not Personal-owned

Examples:

- entitled canonical/general reference content;
- private creator releases the user is entitled/authorized to access;
- Campaign references shown in recent work or membership cards;
- a Campaign Character the subject controls but does not own independently;
- Campaign invitations.

Viewing/reference access never transfers ownership.

### 4.3 Campaign-private resources

Campaign-local World overlays, hidden clues, GM notes, Campaign-run state, private social state, Session Events and other protected material remain Campaign authority. Personal Home may show only a safe link/card if the user is currently authorized and the projection policy permits it.

It must not persist a Personal copy to make the item “available later.”

## 5. Personal Character model

The desired product model allows a user to create and maintain a Character before joining a Campaign, then later propose/bind/clone/adapt that Character into a Campaign according to Campaign rules.

### 5.1 Current Stage A constraint

The completed A4 contract currently binds `CharacterPolicyBindings` and authoritative Character drafts to a required `campaignId`. This remains valid Stage-A implementation evidence and is **not** retroactively rewritten by APW-04.

APW-04 identifies an additive successor requirement for APW-08 implementation handoff:

- introduce explicit Character context/policy binding capable of Personal and Campaign scopes;
- keep existing Campaign-bound records compatible;
- never reinterpret an old Campaign-bound Character as Personal merely because a new Personal Home exists.

### 5.2 Personal Character semantics

A Personal Character is:

- owned/controlled by the user according to Character-domain ownership/control rules;
- built under an explicit Personal rules/profile/content policy;
- not a participant in any Campaign merely by existing;
- not entitled to Campaign-only grants, secrets, inventory, rewards or house-rule state unless explicitly imported/bound through a governed Campaign operation;
- able to be practiced/tested in Personal sandbox without creating Campaign history.

### 5.3 Campaign entry

Joining/using a Personal Character in a Campaign requires an explicit operation such as `propose-character-binding`, `clone-for-campaign`, or `adopt-personal-character` as later chosen by the Character/Campaign owning contracts.

The operation must validate:

- Campaign membership/role and Character control;
- Campaign creation/advancement policies;
- rules profile and pack locks;
- entitlement and source compatibility;
- Campaign-specific restrictions/grants;
- whether identity/history is shared, cloned or migrated;
- which Personal data remains private;
- provenance from the Personal source;
- owner/GM approval where Campaign policy requires it.

No implicit binding occurs from opening a Campaign route.

### 5.4 Campaign exit

Leaving a Campaign does not automatically convert Campaign-owned/runtime state into Personal property. A governed export/clone policy may allow a permitted Personal descendant/snapshot, with hidden Campaign data stripped and provenance preserved. This is a separate operation, not a side effect of membership loss.

## 6. Creative work integration

CSW-01 and CSW-02 are native Personal Home capabilities.

Personal Home may expose:

- Idea Inbox / Creative Library entry;
- Creator Projects and Story Bibles;
- recently changed/open/unresolved/unused material;
- governed references to entitled content;
- incorporation status/backlinks;
- archived Personal creative material.

Campaign-bound creator work remains context-bound and visibility-filtered. A Personal project may reference a Campaign object only while authorized and according to the reference/provenance policy; it does not copy Campaign truth into Personal authority.

## 7. Practice & Sandbox

Personal practice is deliberately useful but nonauthoritative outside its Personal sandbox scope.

Examples may include:

- test a Character build against sample/dummy encounters;
- preview Actions, Effects or rule interactions;
- experiment with a vehicle/item/loadout configuration;
- run a creator lab fixture;
- try a Cozy Solo activity profile later under APM-02;
- rehearse a rules tutorial.

### Sandbox invariants

- sandbox identity is explicit;
- state/effects are marked Personal sandbox/non-Campaign;
- no Campaign resources, rewards, clues, relationship changes, advancement history or Events are mutated;
- Campaign/private content is unavailable unless a separate current authorized reference projection permits it, and sandbox use never copies hidden truth;
- sandbox results may produce drafts/proposals/notes, not authoritative Campaign effects;
- importing a sandbox result into a Campaign requires a governed owning-domain operation;
- canonical promotion remains separate owner authority.

## 8. Reference Library

Entitled general/reference content remains available based on entitlement/object policy rather than Campaign role.

Personal Home may provide:

- browse/search/reference tools;
- favorites/collections;
- safe creator references;
- version/source/provenance information;
- compatibility hints where the current Personal profile is known.

A Campaign may later add local overlays/restrictions/pack locks, but those do not erase the user's independent entitlement to general reference material outside that Campaign.

## 9. Context switching

Moving between Personal and Campaign contexts is an explicit reauthorization boundary.

### Personal → Campaign

Revalidate:

- membership;
- contextual role/delegation;
- Campaign lifecycle;
- Character control;
- entitlement/pack policy;
- visibility;
- destination route/object existence.

Then issue a fresh nonauthoritative selected-context/entry receipt.

### Campaign → Personal

Revalidate the account/Personal-resource authority independently. Do not carry forward Campaign GM/Player/Assistant-GM authority as a Personal role.

### On every transition

- partition/clear protected caches;
- change realtime subscriptions;
- rebuild search/index projections from authorized sources;
- invalidate stale recent-work deep links;
- partition unsaved drafts according to owning domain;
- rebuild notifications/waiting-work counts after filtering;
- rebuild optional-AI context from the new authorized scope;
- clear hidden Campaign data that is not legal in the destination context.

A route, cached card, previous receipt or URL parameter remains nonauthoritative.

## 10. Recent work and continuation

The existing A3 recent-work contract already requires each historical candidate to be re-evaluated against current membership, role, Character control, entitlement, lifecycle and revocation, and selecting it requires fresh workspace-entry authorization.

APW-04 keeps that rule and extends the conceptual model to Personal resources.

Personal Home “Continue” may contain:

- Personal Character draft;
- Personal Creator Project/Story Bible;
- Personal sandbox experiment;
- Personal note/reference;
- currently authorized Campaign work reference.

If a Campaign/reference is no longer authorized, it is omitted without revealing protected prior existence. Personal recent-work entries remain unaffected by unrelated Campaign revocation.

## 11. Invitations

An invitation is not membership and not authority.

Personal Home may show an invitation only through an account-safe invitation projection containing the minimum permitted context:

- safe Campaign/space label where disclosure is authorized;
- inviter safe identity if policy permits;
- offered role/capability summary;
- expiry/status;
- accept/decline path.

Accepting an invitation invokes the Campaign/membership owning operation and revalidates all requirements. A notification or invitation card cannot grant entry by itself.

## 12. Notifications and waiting work

Personal Home may aggregate safe attention signals across contexts, but filtering occurs before counts and cards.

Examples:

- invitation received;
- Personal draft changed/recovery needed;
- CSW item needing user attention;
- Campaign Action needs response/clarification, represented only by a safe account-level summary;
- Campaign activity waits for the user, if current authorization permits disclosure;
- entitlement/account/security notice.

Click/open performs fresh context/entry authorization. If authorization was revoked, the user receives a safe unavailable message and the cached item is removed.

## 13. Zero-Campaign experience

A user with no Campaigns should see a complete Personal experience rather than an error/empty state.

Baseline useful actions:

- create/manage Personal creative projects/fragments;
- create/manage Personal Character drafts once the additive Character successor is implemented;
- browse entitled reference content;
- use supported Personal sandbox/practice tools;
- import/export Personal creative resources;
- review account/entitlements;
- accept invitations;
- begin later Cozy Solo flows under APM-02 when implemented.

“Create/join a Campaign” is an available action, not the only action.

## 14. Leaving the last Campaign or losing access

When a subject leaves/loses their last Campaign:

- account and Personal Home remain valid;
- Personal-owned resources remain;
- Campaign routes/cards/content are removed after current authorization projection refresh;
- protected Campaign caches/subscriptions are cleared;
- safe historical provenance may retain opaque references only where policy permits;
- Personal notes/resources are not deleted merely because they once referenced a Campaign;
- Campaign-derived copies are handled by their explicit provenance/export rules, not silently retained;
- invitations/new Campaign discovery remain possible according to policy.

Loss of Campaign role must never degrade the account into an unusable state.

## 15. Search and discovery

Personal search may combine authorized result classes while preserving source/context labels:

- Personal resources;
- entitled general/reference content;
- currently authorized Campaign references where the product intentionally provides cross-context discovery.

Rules:

- authorize before result inclusion, counts, facets, snippets, relationships, similarity and AI context;
- result cards show Personal/Campaign/reference source class;
- selecting a Campaign result crosses a fresh workspace-entry authorization boundary;
- a result must not be copied into Personal persistence just to support indexing;
- hidden Campaign existence must not leak through empty graph gaps/count deltas/autocomplete.

## 16. Import/export/backup

### Personal export

May include only Personal-owned or explicitly exportable resources and authorized reference/provenance metadata.

It must not include Campaign-private payload merely because a Personal note/project references it.

### Personal import

Imported material enters an explicit Personal pre-authoritative/draft/reference state unless the owning domain defines another safe Personal state. It cannot create Campaign membership, Campaign truth or canonical content.

### Backup/recovery

Account/Personal recovery restores Personal-owned durable resources and safe references according to retention policy. Campaign state is recovered from Campaign owning domains after current authorization, not from a Personal backup copy.

## 17. AI context boundary

Optional AI in Personal Home receives only the selected Personal/entitled context the user is authorized to provide under existing AI policy.

- no automatic carryover of GM-only/Campaign-private prompt context after switching Personal;
- recent Campaign conversation context must be filtered/partitioned;
- AI suggestions create drafts/proposals/Creative Fragments where accepted;
- AI cannot join Campaigns, bind Characters, publish/canonical-promote or mutate sandbox results into Campaign state;
- core Personal Home remains usable without AI.

## 18. APM-02 Cozy Solo handoff

APW-04 supplies APM-02 with a safe Personal host context.

A Cozy Solo run may later use:

- Personal subject/context identity;
- Personal Character/reference if the owning domain permits it;
- Personal Campaign-Activity-like projects/tasks adapted to Personal context;
- Creative Library/journal/project surfaces;
- explicit resource/time/budget profiles;
- optional AI presentation.

But APW-04 grants **no automation authority**. APM-01/APM-02 must establish explicit controller delegation, automatic-operation classes and bounded background behavior separately.

Cozy Solo does not silently turn Personal sandbox/practice effects into Campaign or canonical truth.

## 19. Current implementation reconciliation

Current Stage A has role-oriented GM/Player dashboards and Campaign-bound Character draft policy. These remain valid completed-alpha surfaces.

APW-04 identifies additive successor work only:

1. introduce explicit Personal context into selected-context/workspace-entry contracts;
2. add Personal Home discovery/projection;
3. extend recent work with Personal resource types;
4. add explicit Personal Character policy/binding successor while retaining Campaign-bound compatibility;
5. integrate CSW Personal Creator Projects/Library;
6. add Personal sandbox source class and strict non-Campaign/noncanonical state boundary;
7. partition caches/search/AI/notifications by explicit context;
8. add zero-Campaign and leave-last-Campaign acceptance fixtures.

No completed Stage A closure is reopened by this design.

## 20. Minimum acceptance scenarios

1. Valid user has zero Campaigns → Personal Home offers meaningful creative/reference/practice/account actions without fake Player/GM role.
2. User owns Personal creative project → GM of unrelated Campaign cannot discover it.
3. User is GM in Campaign A and Player in Campaign B → Personal Home does not display a global GM/Player identity; Campaign cards show contextual roles.
4. User opens Campaign A from Personal Home → fresh entry authorization grants only Campaign A scope.
5. User returns to Personal → Campaign GM authority and hidden caches do not carry over.
6. Recent Campaign item lost authorization → disappears from Continue without leaking prior protected existence; Personal recent items remain.
7. Personal Character is proposed to Campaign → Campaign policy validates; no implicit membership/control or Campaign grants before acceptance.
8. User leaves Campaign → Campaign state is not automatically copied into Personal Character; allowed export/clone requires explicit governed operation.
9. Personal sandbox test changes HP/resources → only sandbox state changes; Personal base Character/Campaign state remains unchanged unless owning sandbox rules explicitly persist a Personal sandbox snapshot.
10. Sandbox reward/item cannot be transferred into Campaign by drag/drop or route switching.
11. Campaign-private object referenced by Personal note becomes unauthorized → note remains, protected reference projection becomes unavailable without cached content leakage.
12. Account-level notification says Campaign work needs attention → payload is safe; click reauthorizes before showing detail.
13. User leaves last Campaign → Personal Home still works and protected Campaign caches clear.
14. Personal export excludes Campaign-private referenced payload.
15. AI context after Campaign→Personal transition contains no stale Campaign-private material.
16. AI unavailable → Personal Home/Library/reference/practice manual flows remain usable.

## 21. Additive implementation touch points

APW-04 does not authorize implementation. Future APW-08 handoff may include:

1. A3 selected-context successor with `contextKind=personal|campaign|session`;
2. A3 workspace discovery/entry and recent-work Personal resource types;
3. Personal Home shell/projection contracts;
4. A4 Character Personal policy/context successor and explicit Campaign bind/clone/adopt operation;
5. CSW Personal Project/Library adapters;
6. Personal notes/collections/reference projection;
7. sandbox/practice source class, state isolation and explicit import/proposal bridge;
8. entitlement/reference library adapter;
9. invitation/account-safe projection;
10. cross-context notification/waiting-work aggregation after filtering;
11. context-partitioned search/recent/caches/realtime/AI;
12. Personal import/export/recovery contracts;
13. zero-Campaign, multi-role, leave-last-Campaign and stale-cache fixtures;
14. APM-02 Cozy Solo host-context adapter.

## 22. Nonauthorization

APW-04 does not authorize:

- application implementation/migration;
- a Personal monolithic persistence database;
- global GM/Player account roles;
- automatic Campaign membership or Character binding;
- copying Campaign-private truth into Personal ownership;
- transferring sandbox rewards/state into Campaign without governed operation;
- canonical promotion/publication;
- public marketplace;
- AI/automation authority;
- release/deployment/tester access;
- CCTI-12-T04 before September 2026.

## 23. Completion gate

APW-04 is substantively complete when:

- Personal Home is useful with zero Campaigns;
- resource classes distinguish Personal-owned, Personal-accessible references and Campaign-private data;
- Personal Character successor/binding semantics reconcile current A4 Campaign-bound implementation without rewriting history;
- CSW work is natively usable in Personal context;
- sandbox/practice is useful but state-isolated/non-Campaign/noncanonical;
- context transitions reauthorize and partition caches/search/notifications/AI;
- recent work/invitations/waiting work are safe account-level projections;
- leaving the last Campaign preserves Personal capability and removes protected Campaign access;
- Personal import/export/recovery cannot retain unauthorized Campaign payload;
- APM-02 receives a safe Personal host but no automation authority;
- implementation remains additive and unactivated.

Final `completed_verified` requires exact-head AIOC repository-health and merged PR evidence.
