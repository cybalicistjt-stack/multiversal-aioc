#!/usr/bin/env python3
"""Validate the owner-approved completion-claim integrity controls."""
from __future__ import annotations

from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
POLICY = ROOT / "governance/ai/MULTIVERSAL_COMPLETION_CLAIM_INTEGRITY_POLICY.md"
BOOTSTRAP = ROOT / "governance/ai/MULTIVERSAL_NEW_CONVERSATION_BOOTSTRAP.md"
AMENDMENT = ROOT / "governance/development-bible/amendments/MV-CONT-005_OWNER_AI_INTERACTION_OPERATING_AMENDMENT.md"


class ValidationError(RuntimeError):
    pass


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ValidationError(message)


def read(path: Path) -> str:
    require(path.is_file(), f"missing required file: {path.relative_to(ROOT)}")
    return path.read_text(encoding="utf-8")


def main() -> int:
    try:
        policy = read(POLICY)
        bootstrap = read(BOOTSTRAP)
        amendment = read(AMENDMENT)

        required_policy_phrases = [
            "Evidence-before-claim requirements",
            "Continue execution rule",
            "Failed-validation rule",
            "Artifact-content gate",
            "Claim/evidence pairing",
            "No fictional continuity",
            "Truth-over-smoothness rule",
            "continue_requires_execution_before_response",
            "failed_validation_forbids_completion_claim",
            "artifact_exists_is_not_artifact_complete",
            "status_claim_requires_matching_tool_evidence",
        ]
        for phrase in required_policy_phrases:
            require(phrase in policy, f"policy missing required control: {phrase}")

        require(
            "MULTIVERSAL_COMPLETION_CLAIM_INTEGRITY_POLICY.md" in bootstrap,
            "bootstrap does not load completion-claim integrity policy",
        )
        require(
            "Do not answer “Continue” with only an acknowledgement, plan, summary, restatement, promise, or explanation." in bootstrap,
            "bootstrap does not enforce execution-before-response for Continue",
        )
        require(
            "Artifact existence is not artifact completion" in bootstrap,
            "bootstrap does not enforce artifact-content gate",
        )
        require(
            "failed required validator" in bootstrap.lower(),
            "bootstrap does not enforce failed-validation integrity",
        )
        require(
            "Previous assistant language is not completion evidence" in bootstrap,
            "bootstrap does not reject fictional continuity",
        )

        require(
            "MULTIVERSAL_COMPLETION_CLAIM_INTEGRITY_POLICY.md" in amendment,
            "MV-CONT-005 amendment does not reference completion-claim integrity policy",
        )
        for regression_class in (
            "continue_requires_execution_before_response",
            "failed_validation_forbids_completion_claim",
            "artifact_exists_is_not_artifact_complete",
            "status_claim_requires_matching_tool_evidence",
        ):
            require(regression_class in amendment, f"amendment missing approved regression class: {regression_class}")

        require(
            "historical baseline" in amendment.lower() and "17 of 17" in amendment,
            "amendment must preserve the prior pilot as historical evidence rather than overclaiming new coverage",
        )

        print("Completion-claim integrity validation: PASS")
        return 0
    except (ValidationError, OSError) as exc:
        print(f"Completion-claim integrity validation: FAIL: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
