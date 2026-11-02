-- SA-BILL-03 SECURITY REFERENCE ONLY. DO NOT APPLY AS A PRODUCTION MIGRATION.
-- Never claims external billing/A3 authority, installed tests or selected owner rules.
-- PostgreSQL 15+ illustrative DDL. NOT EXECUTED IN A REAL POSTGRES INSTANCE.
BEGIN;

CREATE SCHEMA IF NOT EXISTS sa_bill03_reference;

-- Provider VERIFIED account subscription projection. The external provider
-- remains billing truth; a reconciler must enforce receipt+purchase ownership.
CREATE TABLE IF NOT EXISTS sa_bill03_reference.verified_subscription (
  subscription_source_id text PRIMARY KEY,
  canonical_payer_subject_id text NOT NULL,
  provider text NOT NULL,
  provider_product_id text NOT NULL,
  provider_revision bigint NOT NULL CHECK (provider_revision >= 0),
  state text NOT NULL CHECK (state IN (
    'verified_active','cancel_scheduled','trial_verified','grace_entitled',
    'account_hold','paused','expired','revoked_refunded'
  )),
  entitled_from timestamptz NOT NULL,
  entitled_until timestamptz NOT NULL,
  provider_checked_at timestamptz NOT NULL,
  revoked_at timestamptz,
  source_epoch bigint NOT NULL DEFAULT 1 CHECK (source_epoch > 0),
  CHECK (entitled_until > entitled_from)
);

-- A3 membership/GM authority below is an illustrative COPY of a canonical
-- projection, NOT a replacement for an external A3 role/session authority.
-- Actual issuer authorization must fetch/validate owner provenance.
CREATE TABLE IF NOT EXISTS sa_bill03_reference.campaign_membership (
  campaign_id text NOT NULL,
  subject_id text NOT NULL,
  role text NOT NULL CHECK (role IN ('owner','gm','player','observer')),
  active boolean NOT NULL,
  owner_revision bigint NOT NULL CHECK (owner_revision > 0),
  PRIMARY KEY (campaign_id, subject_id)
);

CREATE TABLE IF NOT EXISTS sa_bill03_reference.registered_content_root (
  content_release_id text PRIMARY KEY,
  immutable_source_digest text NOT NULL,
  root_kind text NOT NULL CHECK (root_kind IN (
    'custom-setting','registered-species','registered-item-set',
    'registered-ability-tree'
  )),
  content_owner_revision bigint NOT NULL CHECK (content_owner_revision > 0),
  active boolean NOT NULL,
  owner_authorized_as_grant_root boolean NOT NULL,
  dependency_closure_digest text NOT NULL
);

-- One row per Campaign/Player for the life of the Campaign. Revoked slots
-- remain present, not deletable/reissueable without approved replacement flow.
CREATE TABLE IF NOT EXISTS sa_bill03_reference.campaign_allowance_slot (
  campaign_id text NOT NULL,
  player_subject_id text NOT NULL,
  slot_kind text NOT NULL DEFAULT 'gm-sponsored-premium'
    CHECK (slot_kind = 'gm-sponsored-premium'),
  issuer_gm_subject_id text NOT NULL,
  root_release_id text NOT NULL
    REFERENCES sa_bill03_reference.registered_content_root(content_release_id),
  pinned_closure_digest text NOT NULL,
  status text NOT NULL CHECK (status IN ('active','suspended','revoked')),
  grant_epoch bigint NOT NULL DEFAULT 1 CHECK (grant_epoch >= 1),
  issuer_subscription_source_id text NOT NULL
    REFERENCES sa_bill03_reference.verified_subscription(subscription_source_id),
  created_at timestamptz NOT NULL,
  updated_at timestamptz NOT NULL,
  PRIMARY KEY (campaign_id, player_subject_id, slot_kind),
  FOREIGN KEY (campaign_id, player_subject_id)
    REFERENCES sa_bill03_reference.campaign_membership(campaign_id, subject_id),
  FOREIGN KEY (campaign_id, issuer_gm_subject_id)
    REFERENCES sa_bill03_reference.campaign_membership(campaign_id, subject_id)
);

CREATE TABLE IF NOT EXISTS sa_bill03_reference.allowance_command_receipt (
  command_id text PRIMARY KEY,
  canonical_actor_subject_id text NOT NULL,
  payload_sha256 text NOT NULL,
  campaign_id text NOT NULL,
  player_subject_id text NOT NULL,
  accepted_epoch bigint,
  result_code text NOT NULL,
  occurred_at timestamptz NOT NULL
);

CREATE TABLE IF NOT EXISTS sa_bill03_reference.allowance_immutable_event (
  event_id text PRIMARY KEY,
  command_id text NOT NULL UNIQUE
    REFERENCES sa_bill03_reference.allowance_command_receipt(command_id),
  campaign_id text NOT NULL,
  player_subject_id text NOT NULL,
  event_type text NOT NULL CHECK (event_type IN (
    'issued','suspended','revalidated','revoked','retargeted'
  )),
  old_epoch bigint,
  new_epoch bigint NOT NULL CHECK (new_epoch >= 1),
  trusted_owner_revision_digest text NOT NULL,
  event_at timestamptz NOT NULL
);

-- One provider purchase identity belongs to ONE canonical payer subject.
-- The event table below cannot silently "rebind" a token via a later event.
-- Account recovery/transfers require a separately authorized, audited process.
-- This is not an actual provider ownership verification service.
CREATE TABLE IF NOT EXISTS sa_bill03_reference.purchase_subject_binding (
  provider text NOT NULL,
  purchase_origin_id text NOT NULL,
  canonical_payer_subject_id text NOT NULL,
  bound_at timestamptz NOT NULL,
  PRIMARY KEY (provider, purchase_origin_id),
  UNIQUE (provider, purchase_origin_id, canonical_payer_subject_id)
);

-- Checkout tokens/order provenance MUST NOT be issued by a client-side
-- EntitlementEvaluationInput. This is not an actual payment verifier.
CREATE TABLE IF NOT EXISTS sa_bill03_reference.billing_event_dedupe (
  provider text NOT NULL,
  provider_event_id text NOT NULL,
  purchase_origin_id text NOT NULL,
  canonical_payer_subject_id text NOT NULL,
  raw_event_sha256 text NOT NULL,
  source_revision bigint NOT NULL,
  first_observed_at timestamptz NOT NULL,
  PRIMARY KEY (provider, provider_event_id),
  FOREIGN KEY (provider, purchase_origin_id, canonical_payer_subject_id)
    REFERENCES sa_bill03_reference.purchase_subject_binding
    (provider, purchase_origin_id, canonical_payer_subject_id)
);

-- A UNIQUE(provider,purchase_origin_id,provider_event_id) on the event table
-- would NOT prevent cross-account reuse: different event IDs bypass it.
-- The purchase_subject_binding PRIMARY KEY is the actual cross-account fence.

COMMIT;

-- ISSUANCE TRANSACTION OUTLINE (not executable turnkey SQL):
--
-- BEGIN TRANSACTION ISOLATION LEVEL SERIALIZABLE;
--   1. Validate the authenticated A3 session via the current authority.
--   2. Fetch provider-verified billing state with bounded freshness and
--      canonical payer binding. Lock verified_subscription source row FOR UPDATE.
--   3. Lock issuer and player campaign_membership rows FOR UPDATE in
--      deterministic key order; check issuer GM/owner-policy and player active.
--   4. Lock registered_content_root FOR SHARE. Resolve a *trusted registered*
--      dependency graph: exact immutable release, rights+version, no cycles,
--      no unrelated premium roots and bounded traversal.
--   5. Lookup command_id within this transaction: same digest => return
--      existing result; changed digest => CONFLICT (no mutation).
--   6. INSERT campaign_allowance_slot, never first SELECT count then INSERT.
--      A conflicting (campaign,player,slot_kind) is rejected atomically;
--      a replacement is not approved by this study.
--   7. INSERT receipt and immutable event; any failure ROLLBACKS all writes.
--   8. COMMIT; on SQLSTATE 40001 retry with bounded count AND fresh owner
--      revisions; on ambiguous commit query command_id before retrying.
--
-- CAUTION: Separate external A3 service and billing provider state cannot be
-- atomically locked with this PostgreSQL transaction. Revocations arriving
-- later require update/fencing of the same source epochs and invalidation of
-- all derived capability decisions. If verified fresh authority is unavailable
-- at a protected mutation, fail closed instead of trusting client/cache flags.
--
-- PROTECTED READ/MUTATION: all direct and derived object access must check
-- current subject, campaign, canonical A3 membership and issuer privileges,
-- verified subscription epoch, registered root lineage and action rights.
-- No amount of DB uniqueness alone prevents copying a decrypted asset or
-- cross-Campaign export through an unguarded download/search/AI endpoint.
