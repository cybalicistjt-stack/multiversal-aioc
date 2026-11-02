# GATE-02 — Membership, capabilities, content and ownership

**Status:** GATE-02 candidate design, not approved product implementation.  
**Owner-approved source precedence:** UADS Oct 27 account/offline baseline and Campaign Allowances; app tier/content contracts where they do not conflict with later owner allowance scope.  
**Proof:** 50 synthetic reference scenarios, not production authorization/security certification.

## Decision principles

- A permanent verified Multiversal `subjectId` is an account, not a device, username, email or Stripe customer. Two accounts may share an email but never share licenses. No checkout/session redirect, device download, GM relationship, author identity or payment screenshot can confer a second account's rights.
- A membership subscription belongs to **one account**, not a role. GMs and Players have the same proposed personal subscription product; GM/Player/Owner roles are independently authorized within the Campaign.
- Four existing entitlement sources are `free`, `subscription`, `sponsored-month` and `campaign-premium-grant`. They do **not** have interchangeable scope. A Sponsored Month is an account-scoped sponsored subscription per approved baseline; the current app evaluator's `campaignId` field may be issuance provenance, not automatically a runtime Campaign restriction. Precise sponsorship purchase/grant policy is not specified yet.
- The approved free-access policy permits ability trees' first **two** tiers; it does not grant every licensed setting, private GM resource or premium pack. `official-content` is a necessary type of capability, not universal content permission.
- A subscribing account can access **authorized content and capabilities** within the applicable license, campaign role, privacy and rules constraints. Payment does not allow global catalog export, copying someone else's work, GM administration, private information or removal of Campaign-restricted provenance.
- The subscribed GM's one allowance per Campaign/player account covers **one selected root and its exact required dependency closure**, used only for the eligible Campaign and game context. It does not create a subscriber-tier badge, global unlocked ability tiers, a library license, GM privileges or independent transfer rights.
- The allowance beneficiary may inspect their owned Campaign character and possessed items outside an active session via a **narrow retained projection**. This does not permit standalone execution, recreating library definitions or inspecting GM-hidden data. Restriction survives subscription upgrade and allowance/GM expiry.
- Subject/account suspension and hidden-information rules apply *before* membership or retention. Preservation of authored records is different from unrestricted access to protected runtime/content.

## Access evaluation

An authoritative access decision is a tuple of `(subject, installation/session, actor role, campaign membership, action, resource/version, content provenance, visibility, entitlement cause+scope, time, policy version)`. Fail closed on missing essential identity, source proof, resource or permission. The same decision is enforced by API, WSS, search, autocomplete, counts, AI, export, native client and offline-signed authorization; a disabled UI button alone is insufficient.

A proposed order of evaluation:

1. Verify subject and online session or a valid already-verified, narrowly scoped offline lease (depending on action). Verify security version, account suspension, installation binding and audience.
2. Resolve Campaign, role/membership, visibility, ownership and resource source/rights. Privileged GM and private source material cannot become visible through money or allowance.
3. For copy/export/import/transfer, test the **source and destination** and every nested dependency; Campaign-restricted provenance may not be stripped by renaming, variants, snapshot, new ID or personal subscription.
4. Apply action-specific free, personal subscription, Sponsored Month or exact-root Campaign allowance. Keep the cause and exact scope in the result, **never collapse allowance into personal subscriber**.
5. Return a typed decision and reason, with provenance and policy version. Signed offline grants are the *result* of an authorized server decision; clients cannot mint one.
6. On lapse, preserve authored material and previously valid restricted-character read projection subject to account security. No stale cache may undo an already-known revocation.

## Action / source matrix

Notation: **Y** yes when authenticated, appropriately licensed and role/visibility-eligible; **C** conditional exact Campaign/root or independently licensed ownership; **N** not granted by that source. Each row is subject to normal permission constraints.

| Protected action | Free | Subscriber | Account Sponsored Month | Campaign allowance | Retained ownership only |
| --- | :---: | :---: | :---: | :---: | :---: |
| Browse genuinely free public rules/catalog | Y | Y | Y | Y | Y |
| Choose/use eligible ability tiers 1–2 | Y | Y | Y | Y | Y for historical inspection, not new protected use |
| Choose/use protected tier 3–5 in an eligible Campaign | N | C | C | **C: selected tree closure** | N |
| Use selected premium content in an eligible Campaign | N | C | C | **C: selected root closure** | N |
| Browse unrelated premium source definitions/catalog | N | C | C | N | N |
| Execute account-owned platform-dependent content | N | C | C | **C: only allowed exact Campaign root** | N |
| Issue a Campaign allowance | N | **C: subscribed, authorized GM** | **Pending sponsorship eligibility policy** | N | N |
| Read own character and possessed-item projection outside active session | Y | Y | Y | **Y, including restricted-character projection** | **Y, narrowed** |
| Export independently useful owned text/media, if rights permit | C | C | C | C | C |
| Export/clone/transfer Campaign-restricted character or object into independent/other Campaign space | N | N | N | N | N |
| View GM-secret/private content without authorized GM/Owner role | N | N | N | N | N |
| Run GM-authorized administration | Role-dependent, not paywall bypass | Role-dependent | Role-dependent | N | N |

**Clarification:** Free historical inspection of an otherwise legitimately owned character does not imply a free right to continue using protected tier 3–5 content. Campaign allowance inspection persists through the separate retained projection. Payment never removes source/visibility limits.

## Proposed typed contracts (specification only)

```ts
type EntitlementCause = 'free' | 'subscription' | 'sponsored-month' | 'campaign-premium-grant';
type AccessAction = 'read' | 'list' | 'search' | 'use' | 'execute' | 'create' | 'edit' | 'transfer' | 'import' | 'export' | 'offline-grant' | 'issue-allowance' | 'inspect-character';
type DecisionReason = 'authorized-free' | 'authorized-subscriber' | 'authorized-sponsored' |
  'authorized-allowance-closure' | 'authorized-owned-projection' |
  'authentication-required' | 'membership-required' | 'hidden-information' |
  'unlicensed-source' | 'untrusted-grant' | 'entitlement-required' |
  'source-restricted' | 'destination-restricted' | 'policy-version-stale';
interface AccessRequest {
  subjectId: string; sessionOrLeaseProof: unknown; installationId: string;
  action: AccessAction; campaignId?: string; role?: string;
  resourceId: string; resourceVersion: string; provenanceDigest: string;
  evaluatedAtTrusted: number; policyVersion: string;
}
interface AccessDecision {
  allow: boolean; reason: DecisionReason; cause?: EntitlementCause;
  scope?: { campaignId?: string; rootId?: string; manifestDigest?: string };
  projection?: 'full-permitted' | 'retained-character-minimal';
  effectiveUntil?: number; policyVersion: string;
}
```

The above is **proposed extension**, not a claim the current app contract or service already implements it.

## Nonnegotiable provenance model

A restricted character retains `(campaignId, beneficiarySubjectId, allowanceId+version, originatingRootId+version, dependencyManifestDigest, sourcePackIDs, derivedObjectLineage, transferScope='campaign-only')` through Creation → Variant → Placement → Instance → Snapshot → Import/Export. Exact data names are proposals; the scope rule is owner-approved. Rights require source license, actual Campaign membership, resource visibility, current grant and eligible issuer. Changing username, character ID, installed device or personal subscription cannot break the lineage.

No self-service root swap, unbounded grant stack, unlimited GM gifts or group membership purchase is created. Ongoing GM-subscription validation for **existing** allowances remains recommended, not yet separately ratified; preserve the original eligibility rule and mark pending lifecycle choice.

## Acceptance and example boundaries

- The [reference fixtures](GATE_02_POLICY_FIXTURES.json) and [runnable reference oracle](../../../scripts/gate02_reference_oracle.mjs) cover 50 synthetic cases across Free, Subscription, Sponsored Month, Campaign allowance, retained projection, exports and role/visibility.
- The reference oracle omits real cryptography, identity and entitlement-store verification intentionally. It cannot make real endpoint or device accept decisions and is **not** a drop-in product evaluator.
- Further GATE-05/06/07/09 tests must prove actual unique DB slot, signed lease scope and end-to-end source and destination denial, with real Windows/Android independent tests only in GATE-11/12.
- Consumer checkout, final pricing, payment grace, refunds, sponsorship purchasing, AI metering and Play/Apple storefront compatibility remain later tranches and owner/provider decisions.

## Source evidence

| Source | Pinned artifact | Grade |
| --- | --- | --- |
| Approved account/offline | `cybalicistjt-stack/NCG/docs/uads/ACCOUNT_DEVICE_ENTITLEMENT_DESIGN.md` @ `9c91b6f44dc92a8bfa3aa3f92c37a73fdc37d856` | owner-approved design, native implementation unverified |
| Approved allowance exception | `cybalicistjt-stack/NCG/docs/uads/CAMPAIGN_ALLOWANCES.md` @ `d41293dd087f5ad829c6bf67aa3013b75e9302de` | owner-approved scope, policy lifecycle recommendations pending |
| UADS evidence debts | `cybalicistjt-stack/NCG/docs/uads/DECISIONS_AND_EVIDENCE_DEBT.md` @ `35e1b0ca786fae44e0e25e22ea2896e80136cf5c` | implementation/security NOT_RUN |
| Existing app port | `cybalicistjt-stack/Multiversal-app/packages/entitlements/src/entitlement-service-port.ts` @ `d461a158938c9e56dde8334bb106152c18827d27` | typed contract, not end-to-end billing |
| App current evaluator | `cybalicistjt-stack/Multiversal-app/packages/contracts/src/identity-device/entitlement-evaluator.ts` @ `11e9a377a2231dc4c8305df36a299aca37b36de9` | source has generic grants and timestamp string comparisons |
