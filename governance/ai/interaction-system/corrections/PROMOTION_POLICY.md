# Correction Candidate Promotion Policy

## Authority

John Brandon Turner is the final authority for approving or rejecting a regression candidate. A tool invocation records evidence; it does not independently authenticate a person.

## Capture boundary

A correction enters this system only when all of the following are true:

- the correction is explicit;
- recurrence risk is material;
- the immediate work was corrected or explicitly blocked;
- the record is a minimized paraphrase;
- no raw transcript or sensitive attachment content is included;
- referenced patterns and controls already exist.

Capture automatically creates a proposed candidate and never changes a promoted evaluation corpus.

## Review boundary

Only a `proposed` candidate may be reviewed. Approval or rejection requires:

- reviewer identifier `john-brandon-turner`;
- a durable evidence reference;
- an explicit decision timestamp.

Review does not yet add an evaluation case.

## Promotion boundary

Only an owner-approved candidate may be promoted. Promotion requires:

- a new `MV-EVAL-NNN` identifier;
- durable promotion evidence;
- exact materialization of the approved proposed case;
- successful repository validation and CI.

Promotion writes to the canonical promoted-evaluation extension rather than rewriting the historical MV-CONT-002 base corpus. It is reversible through the normal governed pull-request rollback process. It does not train or deploy a model automatically.
