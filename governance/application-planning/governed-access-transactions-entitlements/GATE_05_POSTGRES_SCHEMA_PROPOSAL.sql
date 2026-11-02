-- GATE-05 REFERENCE-ONLY PostgreSQL 17 design sketch.
-- DO NOT EXECUTE ON PRODUCT/RENDER DATABASE. No migrations or deployment authorized.
-- Names, IDs and relationships subject to actual PCV-03F/account schema integration.
-- This intentionally omits real subject foreign keys until schema ownership is reconciled.
CREATE SCHEMA IF NOT EXISTS gate05_proposal;
CREATE TABLE gate05_proposal.provider_customer (
  binding_id text PRIMARY KEY, provider text NOT NULL, environment text NOT NULL,
  provider_customer_ref text NOT NULL, subject_id text NOT NULL,
  binding_version bigint NOT NULL DEFAULT 1 CHECK (binding_version > 0),
  verified_at timestamptz NOT NULL,
  UNIQUE (provider, environment, provider_customer_ref)
);
CREATE TABLE gate05_proposal.checkout_intent (
  intent_id text PRIMARY KEY, subject_id text NOT NULL, operation text NOT NULL,
  idempotency_hash text NOT NULL, offer_id text NOT NULL, offer_version text NOT NULL,
  provider text NOT NULL, environment text NOT NULL,
  storefront text NOT NULL, currency text NOT NULL,
  expires_at timestamptz NOT NULL,
  UNIQUE (subject_id, operation, idempotency_hash)
);
CREATE TABLE gate05_proposal.provider_inbox (
  inbox_id text PRIMARY KEY,
  provider text NOT NULL, environment text NOT NULL, provider_event_ref text NOT NULL,
  digest text NOT NULL, authenticated_at timestamptz NOT NULL,
  processing_state text NOT NULL CHECK (processing_state IN ('pending_lookup','applied','quarantined')),
  current_lookup_ref text,
  UNIQUE (provider,environment,provider_event_ref)
);
CREATE TABLE gate05_proposal.subscription_projection (
  subscription_key text PRIMARY KEY,
  provider text NOT NULL, environment text NOT NULL,
  provider_subscription_ref text NOT NULL,
  binding_id text NOT NULL REFERENCES gate05_proposal.provider_customer(binding_id),
  provider_revision bigint NOT NULL DEFAULT 0 CHECK (provider_revision >= 0),
  billing_status text NOT NULL, auto_renew boolean NOT NULL,
  paid_through timestamptz,
  security_epoch bigint NOT NULL DEFAULT 0 CHECK(security_epoch >= 0),
  UNIQUE(provider,environment,provider_subscription_ref)
);
CREATE TABLE gate05_proposal.paid_period (
  period_id text PRIMARY KEY,
  subscription_key text NOT NULL REFERENCES gate05_proposal.subscription_projection(subscription_key),
  provider text NOT NULL, environment text NOT NULL, provider_invoice_ref text NOT NULL,
  period_start timestamptz NOT NULL, period_end timestamptz NOT NULL,
  invoice_paid boolean NOT NULL DEFAULT false,
  verified_snapshot_ref text NOT NULL,
  CHECK (period_end > period_start),
  UNIQUE (provider, environment, provider_invoice_ref, period_start)
);
CREATE TABLE gate05_proposal.journal_group (
  group_id text PRIMARY KEY,
  provider text NOT NULL, environment text NOT NULL,
  source_fact_ref text NOT NULL,
  currency text NOT NULL,
  created_at timestamptz NOT NULL DEFAULT now(),
  reversed_group_id text REFERENCES gate05_proposal.journal_group(group_id),
  UNIQUE(provider,environment,source_fact_ref)
);
CREATE TABLE gate05_proposal.journal_line (
  group_id text NOT NULL REFERENCES gate05_proposal.journal_group(group_id),
  line_number integer NOT NULL CHECK(line_number > 0),
  account_code text NOT NULL,
  signed_minor bigint NOT NULL,
  PRIMARY KEY (group_id, line_number)
);
-- CRITICAL: The group SUM(signed_minor)=0 must be verified/guarded
-- by a trusted atomic journal-finalization procedure, NOT this DDL alone.
-- Missing finalize trigger/procedure means schema alone cannot guarantee balance.
CREATE TABLE gate05_proposal.entitlement_projection (
  subject_id text NOT NULL, source_kind text NOT NULL, source_ref text NOT NULL,
  scope_key text NOT NULL, version bigint NOT NULL CHECK(version>0),
  policy_epoch bigint NOT NULL DEFAULT 0 CHECK(policy_epoch>=0),
  paid_through timestamptz, revoked_at timestamptz,
  PRIMARY KEY(subject_id,source_kind,source_ref,scope_key)
);
CREATE TABLE gate05_proposal.allowance_slot (
  allowance_id text PRIMARY KEY,
  campaign_id text NOT NULL, beneficiary_subject_id text NOT NULL,
  issuing_gm_subject_id text NOT NULL,
  root_ref text NOT NULL, root_version text NOT NULL, closure_digest text NOT NULL,
  grant_version bigint NOT NULL DEFAULT 1 CHECK(grant_version>0),
  state text NOT NULL CHECK(state IN ('issued','suspended','revoked','expired')),
  UNIQUE(campaign_id,beneficiary_subject_id)
);
-- Tombstone persists in this same unique slot. Deleting/recreating is forbidden by service policy.
CREATE TABLE gate05_proposal.outbox (
  outbox_id text PRIMARY KEY, aggregate_key text NOT NULL,
  aggregate_version bigint NOT NULL CHECK(aggregate_version>0),
  event_kind text NOT NULL, payload_digest text NOT NULL,
  dispatched_at timestamptz,
  UNIQUE (aggregate_key,aggregate_version,event_kind)
);
-- Example atomic uniqueness, not complete business authorization:
-- INSERT INTO gate05_proposal.allowance_slot(...) VALUES (...)
-- ON CONFLICT(campaign_id,beneficiary_subject_id) DO NOTHING RETURNING allowance_id;
-- Implement issuer eligibility + membership + closure checks transactionally FIRST.
-- For queue workers: SELECT outbox_id FROM gate05_proposal.outbox
-- WHERE dispatched_at IS NULL ORDER BY outbox_id LIMIT 20
-- FOR UPDATE SKIP LOCKED;
-- This is only a queue-claim operation, never general authorization proof.
