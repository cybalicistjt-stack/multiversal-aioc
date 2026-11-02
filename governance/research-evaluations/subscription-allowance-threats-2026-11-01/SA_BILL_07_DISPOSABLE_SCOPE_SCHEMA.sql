-- SA-BILL-07: DISPOSABLE PostgreSQL 16 ADVERSARIAL FIXTURE ONLY.
-- This is not a live A3/A5, store, rights-owner, search, export or app migration.
-- Synthetic actors are bound by the calling TEST, not authenticated by this DB.
BEGIN;
CREATE SCHEMA IF NOT EXISTS sa_bill07_fixture;

CREATE TABLE IF NOT EXISTS sa_bill07_fixture.membership (
  campaign_id text NOT NULL,
  subject_id text NOT NULL,
  role text NOT NULL CHECK(role IN ('gm','player','observer')),
  active boolean NOT NULL,
  revision bigint NOT NULL CHECK(revision>=1),
  PRIMARY KEY(campaign_id,subject_id)
);

CREATE TABLE IF NOT EXISTS sa_bill07_fixture.issuer_entitlement (
  issuer_subject_id text PRIMARY KEY,
  state text NOT NULL CHECK(state IN ('verified_active','cancel_scheduled','grace_entitled','account_hold','expired','revoked_refunded')),
  source_verified boolean NOT NULL,
  source_revision bigint NOT NULL CHECK(source_revision>=1),
  checked_at timestamptz NOT NULL,
  entitled_from timestamptz NOT NULL,
  entitled_until timestamptz NOT NULL,
  CHECK(entitled_until>entitled_from)
);

CREATE TABLE IF NOT EXISTS sa_bill07_fixture.registered_release (
  id text PRIMARY KEY,
  version text NOT NULL,
  owner_revision bigint NOT NULL CHECK(owner_revision>=1),
  active boolean NOT NULL,
  rights_valid boolean NOT NULL,
  closure_digest text NOT NULL
);
CREATE TABLE IF NOT EXISTS sa_bill07_fixture.registered_closure (
  root_release_id text NOT NULL REFERENCES sa_bill07_fixture.registered_release(id),
  permitted_release_id text NOT NULL REFERENCES sa_bill07_fixture.registered_release(id),
  owner_revision bigint NOT NULL CHECK(owner_revision>=1),
  closure_digest text NOT NULL,
  PRIMARY KEY(root_release_id,permitted_release_id)
);

CREATE TABLE IF NOT EXISTS sa_bill07_fixture.allowance_slot (
  campaign_id text NOT NULL,
  player_subject_id text NOT NULL,
  slot_kind text NOT NULL DEFAULT 'gm-sponsored-premium'
     CHECK(slot_kind='gm-sponsored-premium'),
  issuer_gm_subject_id text NOT NULL,
  root_release_id text NOT NULL REFERENCES sa_bill07_fixture.registered_release(id),
  root_owner_revision bigint NOT NULL CHECK(root_owner_revision>=1),
  closure_digest text NOT NULL,
  grant_epoch bigint NOT NULL CHECK(grant_epoch>=1),
  issuer_membership_revision bigint NOT NULL,
  player_membership_revision bigint NOT NULL,
  issuer_entitlement_revision bigint NOT NULL,
  state text NOT NULL CHECK(state IN ('active','suspended','revoked')),
  PRIMARY KEY(campaign_id,player_subject_id,slot_kind)
);

CREATE TABLE IF NOT EXISTS sa_bill07_fixture.resource (
  id text PRIMARY KEY,
  campaign_id text NOT NULL,
  owner_subject_id text NOT NULL,
  source_release_id text REFERENCES sa_bill07_fixture.registered_release(id),
  safe_label text NOT NULL,
  protected_payload text NOT NULL,
  self_authored_raw_note text NOT NULL DEFAULT ''
);
CREATE TABLE IF NOT EXISTS sa_bill07_fixture.resource_dependency (
  parent_id text NOT NULL REFERENCES sa_bill07_fixture.resource(id),
  child_id text NOT NULL REFERENCES sa_bill07_fixture.resource(id),
  PRIMARY KEY(parent_id,child_id)
);

-- Pure SQL policy oracle. The calling backend MUST authenticate the subject.
-- Caller may not have direct SELECT on fixture tables in a real deployment.
-- This study does not implement GRANT/RLS, which remain a real endpoint gate.
CREATE OR REPLACE FUNCTION sa_bill07_fixture.protected_use_authorized(
  p_campaign text, p_subject text, p_resource text,
  p_action text, p_grant_epoch bigint
) RETURNS boolean
LANGUAGE sql STABLE AS $$
WITH RECURSIVE
scope AS (
  SELECT s.root_release_id, s.root_owner_revision, s.closure_digest
  FROM sa_bill07_fixture.allowance_slot s
  JOIN sa_bill07_fixture.membership gm
    ON gm.campaign_id=s.campaign_id AND gm.subject_id=s.issuer_gm_subject_id
  JOIN sa_bill07_fixture.membership player
    ON player.campaign_id=s.campaign_id AND player.subject_id=s.player_subject_id
  JOIN sa_bill07_fixture.issuer_entitlement ent
    ON ent.issuer_subject_id=s.issuer_gm_subject_id
  JOIN sa_bill07_fixture.registered_release root
    ON root.id=s.root_release_id
  WHERE s.campaign_id=p_campaign
    AND s.player_subject_id=p_subject
    AND s.state='active' AND s.grant_epoch=p_grant_epoch
    AND gm.active AND gm.role='gm' AND gm.revision=s.issuer_membership_revision
    AND player.active AND player.role='player' AND player.revision=s.player_membership_revision
    AND ent.source_verified
    AND ent.source_revision=s.issuer_entitlement_revision
    AND ent.state IN ('verified_active','cancel_scheduled')
    AND now()>=ent.entitled_from AND now()<ent.entitled_until
    AND ent.checked_at >= now()-interval '1 hour'
    AND root.active AND root.rights_valid
    AND root.owner_revision=s.root_owner_revision
    AND root.closure_digest=s.closure_digest
),
lineage AS (
  SELECT r.id, ARRAY[r.id]::text[] AS path, false AS cycle
  FROM sa_bill07_fixture.resource r WHERE r.id=p_resource
  UNION ALL
  SELECT d.child_id, lin.path||d.child_id,
         d.child_id=ANY(lin.path)
  FROM lineage lin
  JOIN sa_bill07_fixture.resource_dependency d ON d.parent_id=lin.id
  WHERE NOT lin.cycle AND cardinality(lin.path)<128
)
SELECT
  p_action IN ('campaign-read','campaign-use','search','ai','wss')
  AND EXISTS(
    SELECT 1 FROM sa_bill07_fixture.resource r
    WHERE r.id=p_resource AND r.campaign_id=p_campaign
      AND r.owner_subject_id=p_subject)
  AND EXISTS(SELECT 1 FROM scope)
  AND EXISTS(SELECT 1 FROM lineage)
  AND NOT EXISTS(SELECT 1 FROM lineage WHERE cycle OR cardinality(path)>=128)
  AND NOT EXISTS(
    SELECT 1
    FROM lineage lin
    JOIN sa_bill07_fixture.resource r ON r.id=lin.id
    CROSS JOIN scope s
    LEFT JOIN sa_bill07_fixture.registered_release rel
      ON rel.id=r.source_release_id
    LEFT JOIN sa_bill07_fixture.registered_closure allowedge
      ON allowedge.root_release_id=s.root_release_id
     AND allowedge.permitted_release_id=r.source_release_id
    WHERE r.campaign_id<>p_campaign OR (
      r.source_release_id IS NOT NULL AND (
        rel.id IS NULL OR NOT rel.active OR NOT rel.rights_valid
        OR allowedge.permitted_release_id IS NULL
        OR allowedge.owner_revision<>rel.owner_revision
        OR allowedge.closure_digest<>s.closure_digest
      )
    )
  )
$$;

CREATE OR REPLACE FUNCTION sa_bill07_fixture.safe_protected_projection(
  p_campaign text,p_subject text,p_resource text,p_action text,p_epoch bigint
) RETURNS TABLE(resource_id text, safe_label text, payload text)
LANGUAGE sql STABLE AS $$
  SELECT r.id,r.safe_label,r.protected_payload
  FROM sa_bill07_fixture.resource r
  WHERE r.id=p_resource AND
    sa_bill07_fixture.protected_use_authorized(
      p_campaign,p_subject,r.id,p_action,p_epoch)
$$;

-- Raw user-authored note recovery deliberately exposes ONLY its separate
-- field; the actual app must confirm independent ownership and data rights.
CREATE OR REPLACE FUNCTION sa_bill07_fixture.recover_raw_note(
  p_subject text,p_resource text
) RETURNS text LANGUAGE sql STABLE AS $$
  SELECT r.self_authored_raw_note
  FROM sa_bill07_fixture.resource r
  WHERE r.id=p_resource AND r.owner_subject_id=p_subject
$$;
COMMIT;
