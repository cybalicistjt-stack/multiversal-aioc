-- SA-BILL-06 TEST SCHEMA ONLY. NEVER APPLY TO PRODUCT DATABASE.
-- Synthetic provider, synthetic HMAC webhook, synthetic A3 bindings.
-- PostgreSQL 16 disposable research CI fixture only.
BEGIN;
CREATE SCHEMA IF NOT EXISTS sa_bill06_fixture;

CREATE TABLE IF NOT EXISTS sa_bill06_fixture.purchase_binding (
  provider TEXT NOT NULL,
  origin_id TEXT NOT NULL,
  subject_id TEXT NOT NULL,
  provider_account_ref TEXT NOT NULL,
  created_at TIMESTAMPTZ NOT NULL DEFAULT now(),
  PRIMARY KEY (provider,origin_id),
  UNIQUE(provider,origin_id,subject_id,provider_account_ref)
);
CREATE TABLE IF NOT EXISTS sa_bill06_fixture.billing_current (
  provider TEXT NOT NULL,
  origin_id TEXT NOT NULL,
  subject_id TEXT NOT NULL,
  provider_account_ref TEXT NOT NULL,
  app_id TEXT NOT NULL,
  product_id TEXT NOT NULL,
  environment TEXT NOT NULL CHECK (environment='sandbox'),
  revision BIGINT NOT NULL CHECK(revision>=1),
  state TEXT NOT NULL CHECK(state IN (
    'verified_active','cancel_scheduled','grace_entitled','account_hold',
    'expired','revoked_refunded','pending_purchase','trial_verified'
  )),
  entitled_from TIMESTAMPTZ NOT NULL,
  entitled_until TIMESTAMPTZ NOT NULL,
  source_epoch BIGINT NOT NULL CHECK(source_epoch>=1),
  updated_at TIMESTAMPTZ NOT NULL,
  PRIMARY KEY (provider,origin_id),
  FOREIGN KEY (provider,origin_id,subject_id,provider_account_ref)
    REFERENCES sa_bill06_fixture.purchase_binding
      (provider,origin_id,subject_id,provider_account_ref),
  CHECK (entitled_until > entitled_from)
);
CREATE TABLE IF NOT EXISTS sa_bill06_fixture.notification_receipt (
  provider TEXT NOT NULL,
  notification_id TEXT NOT NULL,
  origin_id TEXT NOT NULL,
  body_sha256 TEXT NOT NULL,
  projection_revision BIGINT NOT NULL CHECK(projection_revision>=1),
  apply_result TEXT NOT NULL CHECK(apply_result IN('APPLIED','STALE_SOURCE')),
  observed_at TIMESTAMPTZ NOT NULL DEFAULT now(),
  PRIMARY KEY (provider,notification_id),
  FOREIGN KEY (provider,origin_id)
    REFERENCES sa_bill06_fixture.purchase_binding(provider,origin_id)
);
COMMIT;
