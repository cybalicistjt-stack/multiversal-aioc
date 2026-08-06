#!/usr/bin/env python3
"""Validate IA-D03-004 internal-alpha content and deterministic fixtures."""

from __future__ import annotations

import hashlib
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
REPO = ROOT.parents[2]
SPEC = ROOT / "IA-D03-004_INTERNAL_ALPHA_CONTENT_AND_FIXTURE_SPEC.md"
BASELINE = ROOT / "INTERNAL_ALPHA_CONTENT_AND_FIXTURES.md"
CATALOG = ROOT / "INTERNAL_ALPHA_FIXTURE_CATALOG.json"
COVERAGE = ROOT / "INTERNAL_ALPHA_FIXTURE_COVERAGE_MATRIX.json"
TRACE = ROOT / "IA-D03-004_IMPLEMENTATION_TRACEABILITY.json"
REVIEW = ROOT / "IA-D03-004_REVIEW_RECEIPT.md"
READINESS = ROOT / "IA-D03-004_READINESS_RECORD.md"
COMPLETION = ROOT / "IA-D03-004_COMPLETION_RECORD.json"
BACKLOG = ROOT / "INTERNAL_ALPHA_DESIGN_BACKLOG.md"
PROGRAM = ROOT / "README.md"
ROADMAP = REPO / "governance/ai/runtime/ROADMAP_INDEX.json"
GOLDEN = REPO / "governance/balance/8D-007_GOLDEN_CORPUS_MANIFEST.json"


def canonical_hash(value: object) -> str:
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode("utf-8")).hexdigest()


def load(path: Path, errors: list[str]) -> dict:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception as exc:  # noqa: BLE001
        errors.append(f"Cannot parse {path.relative_to(REPO)}: {exc}")
        return {}


def req(condition: bool, message: str, errors: list[str]) -> None:
    if not condition:
        errors.append(message)


def main() -> int:
    errors: list[str] = []
    required = [SPEC, BASELINE, CATALOG, COVERAGE, TRACE, REVIEW, READINESS, COMPLETION, BACKLOG, PROGRAM, ROADMAP, GOLDEN]
    for path in required:
        req(path.exists(), f"Missing required file: {path.relative_to(REPO)}", errors)
    if errors:
        print("\n".join(f"- {e}" for e in errors))
        return 1

    spec = SPEC.read_text(encoding="utf-8")
    baseline = BASELINE.read_text(encoding="utf-8")
    backlog = BACKLOG.read_text(encoding="utf-8")
    program = PROGRAM.read_text(encoding="utf-8")
    review = REVIEW.read_text(encoding="utf-8")
    readiness = READINESS.read_text(encoding="utf-8")
    catalog = load(CATALOG, errors)
    coverage = load(COVERAGE, errors)
    trace = load(TRACE, errors)
    completion = load(COMPLETION, errors)
    roadmap = load(ROADMAP, errors)
    golden = load(GOLDEN, errors)

    req(spec.startswith("# IA-D03-004 — Internal Alpha Content and Deterministic Fixture Specification"), "Specification title mismatch", errors)
    for section in range(1, 25):
        req(f"## {section}." in spec, f"Specification missing section {section}", errors)
    criteria = [f"ACF-AC-{i:03d}" for i in range(1, 21)]
    for criterion in criteria:
        req(criterion in spec, f"Specification missing {criterion}", errors)
    for phrase in ["not the complete game", "not a canonical content release", "synthetic-contract-fixture", "IA-D03-005"]:
        req(phrase.lower() in spec.lower(), f"Specification missing boundary or next action: {phrase}", errors)

    req(catalog.get("catalogId") == "MV-IA-FIXTURE-CATALOG-001", "Catalog ID mismatch", errors)
    req(catalog.get("version") == "0.1.0", "Catalog version mismatch", errors)
    req(catalog.get("owner") == "John Brandon Turner", "Catalog owner mismatch", errors)
    req(catalog.get("coverageBoundary") == "bounded-internal-alpha-test-corpus-not-complete-game-not-canonical-release", "Catalog coverage boundary mismatch", errors)
    supplied_catalog_hash = catalog.get("catalogChecksum")
    core = dict(catalog)
    core.pop("catalogChecksum", None)
    req(supplied_catalog_hash == canonical_hash(core), "Catalog checksum mismatch", errors)

    golden_ids = {item["fixtureId"] for item in golden.get("fixtures", [])}
    source_defaults = catalog.get("sourceFixtureDefaults", {})
    req(source_defaults.get("inheritExactDefinition") is True, "Source fixture defaults must inherit exact definitions", errors)
    req(source_defaults.get("sourceStatus") == "source-backed-governed-selector", "Source fixture defaults status mismatch", errors)
    source_groups = catalog.get("sourceBackedFixtureGroups", [])
    inherited_ids: set[str] = set()
    for group in source_groups:
        supplied = group.get("groupChecksum")
        group_core = {"domain": group.get("domain"), "fixtureIds": group.get("fixtureIds", [])}
        req(supplied == canonical_hash(group_core), f"Source group checksum mismatch: {group.get('domain')}", errors)
        inherited_ids.update(group.get("fixtureIds", []))
    req(len(golden_ids) == 36, "Golden source manifest must contain 36 fixtures", errors)
    req(len(inherited_ids) == 36 and inherited_ids == golden_ids, "Catalog must inherit exactly all 36 golden fixture IDs", errors)

    synthetic_defaults = catalog.get("syntheticFixtureDefaults", {})
    req(synthetic_defaults.get("sourceStatus") == "synthetic-contract-fixture", "Synthetic defaults not labeled synthetic", errors)
    req(synthetic_defaults.get("canonicalContent") is False, "Synthetic defaults imply canonical content", errors)
    req(synthetic_defaults.get("fixtureChecksumDerivation") == "sha256(canonical-json(category,pack,fixtureId,contractId,schemaVersion))", "Synthetic checksum derivation mismatch", errors)
    contracts = catalog.get("syntheticContractRegistry", {})
    synthetic_groups = catalog.get("syntheticFixtureGroups", [])
    synthetic_ids: list[str] = []
    for group in synthetic_groups:
        category = group.get("category", "<missing>")
        req({"category", "pack", "fixtureIds", "contractId", "groupChecksum"} <= set(group), f"Synthetic group {category} missing required fields", errors)
        supplied = group.get("groupChecksum")
        group_core = {"category": category, "pack": group.get("pack"), "fixtureIds": group.get("fixtureIds", []), "contractId": group.get("contractId")}
        req(supplied == canonical_hash(group_core), f"Synthetic group checksum mismatch: {category}", errors)
        contract_id = group.get("contractId")
        req(contract_id in contracts and bool(contracts.get(contract_id)), f"Synthetic group lacks contract: {category}", errors)
        ids = group.get("fixtureIds", [])
        synthetic_ids.extend(ids)
        for fixture_id in ids:
            derived = canonical_hash({"category": category, "pack": group.get("pack"), "fixtureId": fixture_id, "contractId": contract_id, "schemaVersion": synthetic_defaults.get("schemaVersion")})
            req(len(derived) == 64, f"Cannot derive fixture checksum: {fixture_id}", errors)
    req(len(synthetic_ids) == 119, "Catalog must contain 119 synthetic fixture identities", errors)
    req(len(synthetic_ids) == len(set(synthetic_ids)), "Duplicate synthetic fixture ID", errors)
    req(not (set(synthetic_ids) & golden_ids), "Synthetic and source fixture IDs overlap", errors)
    summary = catalog.get("fixtureIdentitySummary", {})
    req(summary.get("sourceBacked") == 36 and summary.get("synthetic") == 119 and summary.get("total") == 155, "Fixture identity summary mismatch", errors)

    packs = catalog.get("packManifests", [])
    pack_keys = {f"{p.get('packId')}@{p.get('version')}" for p in packs}
    req(len(packs) == 5 and len(pack_keys) == 5, "Catalog must define five unique fixture packs", errors)
    for pack in packs:
        pack_core = dict(pack)
        supplied = pack_core.pop("manifestChecksum", None)
        req(supplied == canonical_hash(pack_core), f"Pack checksum mismatch: {pack.get('packId')}", errors)
        for dep in pack.get("dependencies", []):
            req(dep in pack_keys, f"Pack {pack.get('packId')} references missing dependency {dep}", errors)

    req(len(catalog.get("packLifecycleTable", {}).get("rows", [])) == 9, "Pack lifecycle must contain nine scenarios", errors)
    req(len(catalog.get("accessibilityStressors", [])) == 11, "Accessibility stressor count mismatch", errors)
    req(len(catalog.get("globalExpectedInvariants", [])) >= 10, "Global invariants incomplete", errors)

    req(coverage.get("owner") == "John Brandon Turner", "Coverage owner mismatch", errors)
    supplied_matrix_hash = coverage.get("matrixChecksum")
    matrix_core = dict(coverage)
    matrix_core.pop("matrixChecksum", None)
    req(supplied_matrix_hash == canonical_hash(matrix_core), "Coverage matrix checksum mismatch", errors)
    req(coverage.get("sourceFixtureCount") == 36, "Coverage source count mismatch", errors)
    req(coverage.get("syntheticFixtureCount") == 119, "Coverage synthetic count mismatch", errors)
    rows = coverage.get("coverageRows", [])
    req(len(rows) == 15, "Coverage must contain 15 requirement families", errors)
    req(all(row.get("status") == "covered" and row.get("actualCount", 0) >= row.get("minimumCount", 1) for row in rows), "Coverage family gap", errors)
    claims = coverage.get("coverageClaims", {})
    req(claims.get("boundedInternalAlphaRequirementsCovered") is True, "Bounded coverage not declared", errors)
    req(claims.get("completeGameCovered") is False, "Coverage falsely claims complete game", errors)
    req(claims.get("canonicalContentRelease") is False, "Coverage falsely claims canonical release", errors)
    req(claims.get("unselectedSourceMaterialDiscarded") is False, "Coverage implies source discard", errors)
    req(claims.get("syntheticFixturesImplicitlyPromoted") is False, "Coverage implies synthetic promotion", errors)
    matrix_criteria = coverage.get("acceptanceCriteria", [])
    req(len(matrix_criteria) == 20, "Coverage must contain 20 acceptance criteria", errors)
    req({item.get("criterionId") for item in matrix_criteria} == set(criteria), "Coverage criterion IDs mismatch", errors)
    req(all(item.get("blocking") is True for item in matrix_criteria), "All acceptance criteria must be blocking", errors)
    req(coverage.get("blockingFindings") == [], "Coverage contains blocking findings", errors)

    req(trace.get("workItemId") == "IA-D03-004", "Traceability work item mismatch", errors)
    req(trace.get("owner") == "John Brandon Turner", "Traceability owner mismatch", errors)
    req({item.get("criterionId") for item in trace.get("acceptanceTraceability", [])} == set(criteria), "Traceability criterion coverage mismatch", errors)
    req(len(trace.get("implementationSlices", [])) == 10, "Traceability must contain ten implementation slices", errors)

    metrics = completion.get("metrics", {})
    req(completion.get("status") == "complete-design-implementation-ready", "Completion status mismatch", errors)
    req(completion.get("nextWorkItemId") == "IA-D03-005", "Completion next item mismatch", errors)
    req(metrics.get("sourceBackedFixtures") == 36, "Completion source count mismatch", errors)
    req(metrics.get("syntheticFixtures") == 119, "Completion synthetic count mismatch", errors)
    req(metrics.get("totalFixtures") == 155, "Completion total count mismatch", errors)
    req(metrics.get("acceptanceCriteria") == 20 and metrics.get("blockingFindings") == 0, "Completion acceptance metrics mismatch", errors)

    for name, text in [("review", review), ("readiness", readiness)]:
        req("implementation-ready" in text.lower(), f"{name} lacks readiness decision", errors)
        req("IA-D03-005" in text, f"{name} lacks next action", errors)
        req("not the complete game" in text.lower() or "bounded test corpus" in text.lower(), f"{name} lacks bounded corpus boundary", errors)

    req("**Version:** 0.2.0" in baseline, "Fixture baseline version must be 0.2.0", errors)
    req("INTERNAL_ALPHA_FIXTURE_CATALOG.json" in baseline, "Fixture baseline does not link catalog", errors)
    req("36 source-backed" in baseline and "119 synthetic" in baseline, "Fixture baseline metrics missing", errors)

    req("**Version:** 0.11.0" in backlog, "Backlog version must be 0.11.0", errors)
    req("IA-D03-004 — alpha content and fixture specification — complete" in backlog, "Backlog does not mark IA-D03-004 complete", errors)
    req("IA-D03-005 — Character/Campaign integration review — next" in backlog, "Backlog does not advance to IA-D03-005", errors)
    req("**IA-D03-005 — Character/Campaign integration review.**" in backlog, "Backlog current-next statement mismatch", errors)

    req("**Version:** 0.11.0" in program, "Program README version must be 0.11.0", errors)
    req("## IA-D03-004 — Internal Alpha Content and Deterministic Fixtures" in program, "Program README lacks IA-D03-004 result", errors)
    req("**IA-D03-005 — Character/Campaign integration review.**" in program, "Program README next action mismatch", errors)

    roadmap_ids = {item.get("work_item_id") for item in roadmap.get("entries", [])}
    req("IA-D03-004" in roadmap_ids and "IA-D03-005" in roadmap_ids, "Roadmap index missing IA-D03-004 or IA-D03-005", errors)

    if errors:
        print("IA-D03-004 INTERNAL ALPHA CONTENT/FIXTURE VALIDATION: FAIL")
        for error in errors:
            print(f"- {error}")
        return 1

    print("IA-D03-004 INTERNAL ALPHA CONTENT/FIXTURE VALIDATION: PASS")
    print("Source-backed fixtures: 36")
    print("Synthetic fixtures: 119")
    print("Total fixtures: 155")
    print("Fixture packs: 5")
    print("Coverage families: 15")
    print("Acceptance criteria: 20")
    print("Pack lifecycle scenarios: 9")
    print("Accessibility stressors: 11")
    print("Blocking findings: 0")
    return 0


if __name__ == "__main__":
    sys.exit(main())
