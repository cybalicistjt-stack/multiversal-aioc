# CSV Intake Population Authority Redirect

**Disposition:** HISTORICAL INTAKE AREA FOR POPULATION SELECTION  
**Effective:** 2026-09-17

The files in this directory preserve the August-4 CSV intake, staging, promotion, validation, identity, and reconciliation program.

They remain valid evidence for:
- source provenance;
- prior stable identities and mappings;
- conflict/variant history;
- validators and runtime-test evidence;
- reconstruction of prior decisions.

They are **not** the current authority for selecting the working Item/Object source population.

For any new Item/Object corpus count, readiness audit, enrichment pass, or content migration, begin with:

`governance/object-system/CURRENT_GAME_OBJECT_SOURCE_AUTHORITY.json`

In particular, do not use historical totals such as `5,389`, `5,353`, `5,346`, `5,443`, melee `327`, ranged `230`, or program total `19,199` as the current object population unless the current source authority explicitly says so.

Older files are historical/reference-only for population selection unless a later owner-authorized manifest explicitly reactivates or supersedes them.

This redirect does not erase or invalidate historical provenance. It removes authority to steer the current working corpus.
