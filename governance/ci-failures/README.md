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

## Operating rule

Before asking the owner for screenshots, inspect the failure index and newest run record on `ci/failure-records`. Screenshots are fallback evidence only when GitHub does not expose the required logs or metadata.

The recorder runs every five minutes and may also be started manually through GitHub Actions.
