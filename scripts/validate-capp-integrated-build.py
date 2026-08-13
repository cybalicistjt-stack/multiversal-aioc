#!/usr/bin/env python3
"""Integrated CAPP-04..12 build validator.

This script is intentionally built before the owner-requested validation round.
It does not mark work completed_verified and does not inspect PR/merge evidence.
"""
from __future__ import annotations

import json
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CAPP = ROOT / "governance/application-planning/character-appearance-production"
PPIA = ROOT / "governance/application-planning/parallel-preimplementation"

REQUIRED = [
    "CAPP-04_ASSET_MANIFEST_CONTRACT_v0.1.0.json",
    "CAPP-04_CONTEXTUAL_COVERAGE_EXTENSION_v0.1.0.json",
    "CAPP-04_COVERAGE_MODEL_v0.1.0.json",
    "CAPP-04_REFERENCE_ANALYZER_CONTRACT_v0.1.0.json",
    "CAPP-04_REFERENCE_EMPTY_MANIFEST_v0.1.0.json",
    "CAPP-04_ACCEPTANCE_MATRIX_v0.1.0.json",
    "CAPP-05_DETERMINISTIC_APPEARANCE_COMPILER_CONTRACT_v0.1.0.json",
    "CAPP-06_WARDROBE_EQUIPMENT_FIT_CATALOG_v0.1.0.json",
    "CAPP-07_APPEARANCE_STUDIO_IMPLEMENTATION_SPEC_v0.1.0.json",
    "CAPP-08_PORTRAIT_TOKEN_EXPORT_CONTRACT_v0.1.0.json",
    "CAPP-09_APPEARANCE_VERSIONING_MIGRATION_CONTRACT_v0.1.0.json",
    "CAPP-10_ACCESSIBILITY_DESCRIPTION_GRAMMAR_v0.1.0.json",
]
TOOLS = [
    "tools/capp05_appearance_compiler.py",
    "tools/capp09_migration_reference.py",
    "tools/capp10_accessibility_description.py",
    "tools/capp11_generate_qa_corpus.py",
]


def load(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def run_self_test(path: str) -> None:
    subprocess.run([sys.executable, str(ROOT / path), "--self-test"], cwd=ROOT, check=True)


def main() -> int:
    for name in REQUIRED:
        require((CAPP / name).is_file(), f"missing required CAPP artifact: {name}")
        load(CAPP / name)
    for tool in TOOLS:
        require((ROOT / tool).is_file(), f"missing required reference tool: {tool}")

    manifest = load(CAPP / "CAPP-04_ASSET_MANIFEST_CONTRACT_v0.1.0.json")
    coverage = load(CAPP / "CAPP-04_COVERAGE_MODEL_v0.1.0.json")
    compiler = load(CAPP / "CAPP-05_DETERMINISTIC_APPEARANCE_COMPILER_CONTRACT_v0.1.0.json")
    fit = load(CAPP / "CAPP-06_WARDROBE_EQUIPMENT_FIT_CATALOG_v0.1.0.json")
    studio = load(CAPP / "CAPP-07_APPEARANCE_STUDIO_IMPLEMENTATION_SPEC_v0.1.0.json")
    export = load(CAPP / "CAPP-08_PORTRAIT_TOKEN_EXPORT_CONTRACT_v0.1.0.json")
    migration = load(CAPP / "CAPP-09_APPEARANCE_VERSIONING_MIGRATION_CONTRACT_v0.1.0.json")
    a11y = load(CAPP / "CAPP-10_ACCESSIBILITY_DESCRIPTION_GRAMMAR_v0.1.0.json")

    require(manifest.get("work_item_id") == "CAPP-04", "CAPP-04 manifest identity mismatch")
    require(coverage.get("work_item_id") == "CAPP-04", "CAPP-04 coverage identity mismatch")
    require(compiler.get("work_item_id") == "CAPP-05", "CAPP-05 identity mismatch")
    require(fit.get("work_item_id") == "CAPP-06", "CAPP-06 identity mismatch")
    require(studio.get("work_item_id") == "CAPP-07", "CAPP-07 identity mismatch")
    require(export.get("work_item_id") == "CAPP-08", "CAPP-08 identity mismatch")
    require(migration.get("work_item_id") == "CAPP-09", "CAPP-09 identity mismatch")
    require(a11y.get("work_item_id") == "CAPP-10", "CAPP-10 identity mismatch")

    require(compiler.get("invariants", {}).get("character_truth_changed") is False, "compiler may not change Character truth")
    require(fit.get("boundaries", {}).get("inventory_ownership_change") is False, "fit catalog may not change inventory")
    require(studio.get("boundaries", {}).get("mechanics_write") is False, "studio may not write mechanics")
    require(export.get("boundaries", {}).get("hidden_information_export") is False, "export may not leak hidden state")
    require(migration.get("boundaries", {}).get("silent_substitution") is False, "migration may not silently substitute")
    require(a11y.get("boundaries", {}).get("hidden_information_leak") is False, "accessibility output may not leak hidden state")

    topology = load(CAPP / "CAPP-03_TOPOLOGY_TEMPLATE_CONTRACT_v0.1.0.json")
    require(topology.get("special_templates", {}).get("CAPP03-TOP-MORAVI", {}).get("legs") == 4, "Moravi topology regression")
    require(topology.get("special_templates", {}).get("CAPP03-TOP-VESPIN", {}).get("arms") == 4, "Vespin topology regression")
    require(topology.get("special_templates", {}).get("CAPP03-TOP-SUULA", {}).get("nested_hands") is True, "Suula topology regression")
    require(topology.get("special_templates", {}).get("CAPP03-TOP-MANYTOMS", {}).get("repeated_constituents") is True, "ManyToms topology regression")

    for tool in TOOLS:
        run_self_test(tool)

    profile_index = CAPP / "CAPP-01_SOURCE_AUTHORITY_AND_PROFILE_INDEX_v0.1.0.json"
    with tempfile.TemporaryDirectory() as td:
        out = Path(td) / "corpus.json"
        subprocess.run([
            sys.executable,
            str(ROOT / "tools/capp11_generate_qa_corpus.py"),
            "--profile-index", str(profile_index),
            "--output", str(out),
        ], cwd=ROOT, check=True)
        corpus = load(out)
        require(corpus.get("profile_count") == 25, "CAPP-11 must cover 25 profiles")
        require(corpus.get("case_count", 0) >= 900, "CAPP-11 corpus must contain at least 900 generated cases")
        require(len({x["case_id"] for x in corpus.get("cases", [])}) == corpus.get("case_count"), "CAPP-11 case IDs must be unique")
        require(all(x.get("provenance_class") == "synthetic_noncanonical" for x in corpus.get("cases", [])), "generated cases must remain synthetic/noncanonical")

    upstream = [
        PPIA / "PPIA-06_APPEARANCE_STUDIO_CONTROL_SURFACE_v0.1.0.json",
        PPIA / "PPIA-06_SPECIES_MORPHOLOGY_PROFILES_v0.1.0.json",
        PPIA / "PPIA-05_SPECIES_FORMS_BIOLOGY_TAXONOMY_v0.1.0.json",
    ]
    for path in upstream:
        require(path.is_file(), f"missing upstream authority: {path.relative_to(ROOT)}")

    print("CAPP integrated build validator: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
