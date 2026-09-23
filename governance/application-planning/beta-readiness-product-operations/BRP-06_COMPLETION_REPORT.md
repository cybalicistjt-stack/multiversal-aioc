# BRP-06 Completion Report

**Status:** `completed_verified`  
**Schema:** `BRP-06.1`  
**Application PR:** #762  
**Causal RED:** run `35864881485`, head `4deb428e524c83cdfbe79a889c56aab3b0b0706b`  
**Validated GREEN:** run `35865075146`, head `6d846795fad324007ea428b881e251207717d5fe`  
**Application merge:** `4464040e8f657be7acb3c63651f934db0cffca79`

BRP-06 completes the bounded beta data-durability, backup, restore, migration and rollback proof over the provider-neutral backup/restore contract, MIB-08 migration engineering and sealed owner-domain Campaign authority.

The beta recovery contract publishes RPO <= 15 minutes and RTO <= 30 minutes for governed rehearsal evidence. Backups must originate from verified snapshots with manifest/object integrity. Restore is validated, staged in isolation, verifies stores/blobs and activates atomically. Corrupt or unverified backup evidence fails closed.

Migration failure recovery preserves immutable history and uses either a known idempotent cursor or verified-snapshot rollback; uncertain commits require manual recovery. Data loss or rewritten migration history fails proof. Application and data rollback both preserve last-known-good versions.

Destructive rehearsal must restore the same Campaign identity, authoritative history and authoritative state checksum, and may not replay irreversible effects already present before the destructive event. Recovery evidence excludes hidden/private cross-context data. No storage/cloud provider or parallel canonical authority is selected.

The causal RED failed exactly because the BRP-06 production module was absent. The first production head passed unchanged focused acceptance, invariants, typecheck, Linux validation, hosted Windows validation and deterministic cross-platform comparison. No repair cycle was required.

BRP-07 — Feature Flags, Cohorts, Remote Configuration & Kill Switches — is selected next but not started.
