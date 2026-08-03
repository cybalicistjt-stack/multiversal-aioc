# CI Failure Evidence Protocol

GitHub Actions failures are recorded automatically by `.github/workflows/record-action-failures.yml`.

## Authoritative failure record

Branch: `ci/failure-records`

Index:

`governance/ci-failures/INDEX.md`

Individual records:

`governance/ci-failures/records/run-<RUN_ID>.md`

Each record preserves:

- workflow name and run identity;
- branch, commit, event, timestamps, and GitHub run address;
- failed jobs;
- failed or cancelled steps;
- a bounded excerpt of the decoded workflow logs.

## Mandatory pre-operation gate

Before **every** governed operation or implementation step:

1. Read `governance/ci-failures/INDEX.md` from `ci/failure-records`.
2. Inspect the newest unresolved failure record, when present.
3. Treat any relevant unresolved failure as blocking evidence and repair it before advancing unrelated work.
4. Re-check the index after the repair commit before beginning the next operation.

Before asking the owner for screenshots, inspect the failure index and newest run record. Screenshots are fallback evidence only when GitHub does not expose the required logs or metadata.

The recorder runs every five minutes and may also be started manually through GitHub Actions.
