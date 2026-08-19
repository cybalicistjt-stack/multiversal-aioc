# APW-01 — Authority, Account, Context and Terminology Canonicalization

**Work item:** APW-01  
**Program:** APW — Asynchronous Play & Persistent Workspace  
**Version:** 0.1.0  
**Status:** DESIGN CONTRACT — READY FOR GOVERNED REVIEW  
**Owner and final authority:** John Brandon Turner  
**Date:** 2026-08-18

## 1. Decision

Multiversal has **users**, not permanent Player accounts or permanent GM accounts.

A Multiversal account resolves to one stable internal subject. Player, Game Master, Assistant GM, Observer, creator/reviewer, Campaign owner, Character controller, resource owner and similar labels describe **contextual authority**, not global account identity.

This contract does not replace or invalidate the completed Stage A identity, authorization, Campaign, Session, entitlement, creator, recovery or hidden-information architecture. It makes their existing separation explicit and establishes the additive vocabulary required by APW, APM and CSW.

## 2. Canonical authority model

Authority is evaluated from the following independent inputs. No input silently implies another:

1. **Subject identity** — the stable internal Multiversal subject.
2. **Authentication session** — evidence that the current client session represents the subject.
3. **Context** — the Personal, Campaign or Session/active-encounter scope in which the operation occurs.
4. **Membership** — whether the subject belongs to a Campaign or other governed collaborative scope.
5. **Contextual role** — a scoped role such as Campaign GM, Player, Assistant GM or Observer.
6. **Ownership** — ownership of a Personal resource, Campaign, reusable draft or other object where the owning domain recognizes ownership.
7. **Control/custody** — Character control, Asset custody or another domain-specific control grant.
8. **Delegation** — an explicit bounded grant from an authority that is permitted to delegate.
9. **Entitlement** — access to content or capability that the user's subscription, purchase, Campaign grant or other approved source permits.
10. **Visibility/classification** — whether the requested fields, relationships, counts, history or projections may be disclosed.
11. **Lifecycle/state** — whether the object, Campaign, Session, invitation, role or grant is active, archived, expired, revoked or otherwise usable.
12. **Policy/version** — the governing policy, ruleset, pack-lock, permission and schema versions.
13. **Support/operational access** — exceptional purpose-bound access, separately attributable and never inferred from Owner/Admin status.

Authorization remains deny-by-default. A UI label, route, cached card, query parameter, prior access, tool availability or selected-context receipt is not authority.

## 3. Universal-user account contract

A **Multiversal user account** is the product-facing representation of one stable Multiversal subject and its provider-neutral authentication/recovery mappings.

The account is not typed as Player, GM or creator. It may simultaneously or sequentially participate in many contexts, for example:

- GM of Campaign A;
- Player in Campaign B;
- Observer in Campaign C;
- owner of Personal Characters and drafts;
- collaborator/reviewer on an assigned creator resource;
- no Campaign membership at all.

Changing or losing one contextual role does not change the account's identity and must not remove unrelated Personal capabilities or unrelated Campaign memberships.

Campaign membership must not reduce access to general/reference content that the user's entitlement otherwise permits. Campaign-local hidden truth and private state remain protected by authorization and visibility rules.

## 4. Context model

### 4.1 Personal context

Personal is the user's independent Multiversal workspace. It exists even when the user has zero Campaign memberships and when no other participant is connected.

Personal context may contain, as owning domains permit:

- personal Characters and drafts;
- reusable creator assets and templates;
- notes, collections, favorites and saved references;
- sandbox/lab experiments;
- recent work and continuation affordances;
- entitled reference content;
- invitations and notifications safe to show outside a Campaign.

A Campaign GM role has no authority over another user's Personal context. Campaign membership does not transfer ownership of Personal resources into the Campaign.

### 4.2 Campaign context

Campaign context is the governed collaborative scope identified by one stable Campaign ID. Membership, contextual role, Character control, delegation, Campaign-local visibility and Campaign policy are evaluated inside this scope.

A subject may hold different roles in different Campaigns. A GM of Campaign A has no implied access to Campaign B. A Player in Campaign A remains an ordinary Multiversal user outside Campaign A.

Campaign owner and Campaign GM are Campaign-scoped authorities. They are not equivalent to application Owner/Admin.

### 4.3 Session / active-encounter context

Session context is subordinate to a Campaign and binds the subject to one authorized Session projection, launch snapshot, participant/Character bindings and current Event-backed state.

Session authority cannot outlive or broaden the governing Campaign authority. A Session route or realtime connection does not create membership or role authority.

### 4.4 Context transitions

Moving Personal → Campaign → Session, Session → Campaign, or Campaign → Personal is an explicit context transition. Each protected destination is reauthorized. Protected caches, subscriptions, AI context, drafts and notifications are partitioned or cleared according to their owning contracts.

## 5. Orthogonal axes: cadence and connectivity

Context is not cadence, and cadence is not connectivity.

**Cadence**:
- Live
- Asynchronous
- Hybrid

**Connectivity**:
- Connected
- Temporarily offline/cached
- Recovering/reconnecting

A Campaign remains the same Campaign when cadence changes. Live and asynchronous play use the same Campaign identity, proposal/approval architecture, Events, projections, permissions and recovery model.

Offline or recovering status never creates broader authority. Bounded offline behavior continues to follow the existing recovery/offline contracts.

## 6. Contextual role vocabulary

The following labels are canonical as **scoped descriptors**, not account types:

- **Campaign Owner** — subject recognized by the Campaign domain as owning/governing that Campaign; Campaign-scoped.
- **Game Master (GM)** — active GM authority for a specific Campaign.
- **Assistant GM** — explicitly delegated Campaign authority, bounded by scope and expiry.
- **Player** — Campaign participant with Player-safe projection and separately governed Character-control rights.
- **Observer** — explicitly granted read-only Campaign/Session projection.
- **Character Controller** — subject granted control of a specific Character in a specific governed scope; independent of membership label where the domain permits.
- **Creator / Reviewer** — subject acting in an owned or assigned creation/review scope; creator status does not imply Campaign access or canonical-promotion authority.
- **Personal Resource Owner** — subject owning a Personal-context resource where the owning domain supports ownership.
- **Owner/Admin** — application/program operational authority only. It does not silently grant Campaign-private or Player-private access.
- **Service actor / AI assistive actor** — narrow nonhuman execution identities with no independent human authority and no silent elevation.

A single operation may depend on several descriptors at once. Future contracts must not collapse them into one global role bit.

## 7. Information and entitlement boundary

Multiversal distinguishes at least these information classes for APW purposes:

1. **Entitlement-available general/reference content** — visible when entitlement and ordinary object policy permit, independent of Campaign role.
2. **Personal-private content** — owned/controlled by the user or explicitly shared from Personal context.
3. **Campaign-shared content** — Campaign-local information visible to the authorized Campaign audience.
4. **Campaign-hidden/GM truth** — Campaign-local protected truth, including unrevealed clues, secret objectives, hidden placements and GM notes.
5. **Player-private content** — private notes or other Player-scoped information.
6. **Creator-private/assigned draft content** — bounded by ownership or assignment.
7. **Operational/security-sensitive content** — governed separately from ordinary play authority.

A Campaign may add local placements, overrides, reveal state or restrictions to Campaign-local material, but membership must not be used as a pretext to hide unrelated reference content the user is otherwise entitled to access.

**Spoiler Shield is never a security boundary.** Optional spoiler filtering may reduce accidental exposure of information the user is already authorized to access. Campaign-private truth must be removed by authorization before publication.

## 8. Reconciliation with completed Stage A contracts

### Stable subject identity

MV-IA-F003 already requires stable subject identity to be independent of provider identity, email, device and current role. APW-01 adopts that unchanged.

### Membership, role, control, ownership and entitlement separation

MV-IA-F003 and MV-IA-F020 already require these decisions to remain separate. APW-01 adopts that unchanged and extends the same rule to Personal context and cross-Campaign multi-role use.

### Current `A3ActiveRole`

The current A3 `A3ActiveRole` union is a valid **Stage-A active-context/navigation projection**. It is not the canonical account type model. Later additive implementation may version or supersede this contract so one subject can carry a context descriptor plus the relevant scoped role/grant set without reopening A3 completion.

### Current `player-dashboard` and `gm-dashboard`

These are valid bounded Stage-A workspace surfaces. APW-01 classifies them as specialized views/projections, not permanent top-level identities. A later Personal Home may become the account-level entry surface while Player/GM dashboards remain context-specific Campaign views where useful.

### Current Campaign authorization policy

The current `CampaignRole` policy is correctly Campaign-scoped and remains valid. APW-01 does not convert application Owner/Admin into Campaign owner and does not globalize Campaign roles.

### Selected-context receipts

Existing receipts remain navigation/recovery evidence only. A future APW successor may add explicit `contextKind`, Personal-context identity and role/grant references, but no receipt becomes client-authoritative permission.

### Test and guided-alpha role selectors

Role query parameters, GM/Player launch shortcuts and single-role fixtures used by guided alpha are test harness conveniences. They must never be promoted into production account-authority semantics.

## 9. Prohibited assumptions

The following assumptions are noncanonical for future implementation:

- `account.isGM` or equivalent global Boolean grants Campaign authority;
- `account.isPlayer` determines general product capability;
- a user must choose one permanent GM or Player persona at registration;
- GM authority in one Campaign applies to another Campaign;
- Campaign membership removes Personal/creator/reference capabilities;
- Campaign role alone grants Character control, ownership or entitlement;
- creator status grants Campaign-private access or canonical promotion;
- Owner/Admin status grants blanket access to private play content;
- Session presence or realtime connection grants membership;
- `?role=gm`, route family, visible button, cached dashboard card or selected context is authorization;
- asynchronous play requires a separate Campaign type, rules engine or authority model;
- Spoiler Shield can substitute for hidden-information authorization.

## 10. Additive implementation touch points

APW-01 does not authorize these changes; it identifies them for APW-08/APW-I01 planning.

1. `packages/contracts/src/a3/selected-context-receipt.ts`
   - preserve current contract compatibility;
   - future version should express Personal/Campaign/Session context explicitly;
   - avoid treating singular `activeRole` as account identity.
2. `packages/contracts/src/a3/a3-authorization-projection.ts`
   - preserve separation of application role and Campaign role;
   - future successor should accept the scoped authority inputs required by Personal and multi-role contexts rather than a global role bit.
3. `packages/contracts/src/authorization/campaign-authorization-policy.ts`
   - retain Campaign scoping;
   - future extension may add richer delegation/multi-role capability evaluation without broadening authority outside the Campaign.
4. A3 dashboard/workspace discovery and projection contracts
   - add Personal workspace/home projection and campaign-context metadata;
   - keep discovery and entry as separate authorization decisions.
5. `apps/client-ui/src/a3/context/WorkspaceSwitcher.tsx`
   - evolve from role-labelled workspace switching toward explicit context switching while retaining safe authorized projections.
6. `apps/client-ui/src/a3/dashboard/DashboardPage.tsx` and shell/navigation
   - future Personal Home should not force the user into a Player or GM caste;
   - Campaign role labels remain contextual metadata.
7. Stage A fixtures and acceptance tests
   - add a zero-Campaign user;
   - one user with different roles in multiple Campaigns;
   - two users who are each GM of one Campaign and Player in another;
   - cross-context revocation and cache-partition cases.
8. Campaign/Session consumers (A5+) and proposal/approval consumers (A6+)
   - continue consuming explicit Campaign/Session authority rather than account-global role state.
9. Creator/world/content surfaces (A10/CCTI and successors)
   - distinguish Personal/reusable ownership, Campaign-local variants and canonical-promotion authority.
10. Notifications, search, recent work, diagnostics, AI context and recovery
   - include context identifiers and perform permission-safe partitioning; counts and previews must not leak hidden context existence.

## 11. Minimum APW-01 acceptance scenarios

### Scenario A — multi-role user

User A is GM of Campaign Alpha and Player in Campaign Beta. Entering Alpha produces Alpha GM authority only. Entering Beta produces Beta Player authority only. Personal context remains available in both cases.

### Scenario B — independent users

User A is GM of Campaign Alpha. User B owns Personal drafts and is not a member of Alpha. User A cannot discover or mutate User B's Personal resources through GM authority.

### Scenario C — no-Campaign user

User C has a valid subscribed/approved account and no Campaign memberships. User C still has a useful Personal context and entitled reference/creator capabilities as permitted by owning domains.

### Scenario D — entitlement and Campaign separation

User D is a Player in a Campaign and is entitled to a general reference object. The Campaign role does not remove the general reference entitlement. Campaign-local hidden overlays or unrevealed placements remain protected.

### Scenario E — role revocation

User E loses GM authority in Campaign Epsilon while retaining the account, Personal resources and a Player membership in Campaign Zeta. Epsilon GM access is revoked without affecting unrelated contexts.

### Scenario F — Owner/Admin separation

An application Owner/Admin without Campaign membership or support-access grant cannot read Campaign-private or Player-private content.

### Scenario G — cadence change

A Campaign transitions Live → Asynchronous → Live. Membership, Campaign identity, authority, Event history and hidden-information rules remain coherent; no second rules engine or role model is created.

## 12. Downstream constraints

APW-02 through APW-08, APM and CSW must use this contract unless explicitly superseded by owner authority.

In particular:

- APW-02 asynchronous proposals are Campaign-context operations;
- APW-04 Personal Home is an account/user surface, not a Player/GM dashboard rename;
- APW-05 Creator Workshop is a general user capability bounded by resource ownership/assignment;
- APM automated play may act only through governed contextual authority and does not create a global AI GM role;
- CSW creator/storycraft work belongs primarily to Personal/reusable creation contexts until explicitly instantiated, linked or promoted elsewhere.

## 13. Nonauthorization

APW-01 authorizes no application implementation, migration, deployment, release, tester distribution, production credentials, paid services, autonomous mutation, public marketplace, canonical content promotion or T04 resumption.

CCTI-12-T04 remains deferred until September 2026 under the current owner routing decision.
