#!/usr/bin/env python3
from __future__ import annotations

import json
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / "governance/application-planning/parallel-preimplementation"
FILES = {
    "manifest": BASE / "PPIA-15_SOURCE_AND_TEST_CORPUS_MANIFEST_v0.1.0.json",
    "inventory": BASE / "PPIA-15_INHERITED_SCENARIO_INVENTORY_v0.1.0.json",
    "taxonomy": BASE / "PPIA-15_AWKWARD_CASE_TAXONOMY_v0.1.0.json",
    "gaps": BASE / "PPIA-15_COVERAGE_GAP_MATRIX_v0.1.0.json",
    "oracle": BASE / "PPIA-15_ORACLE_AND_FIXTURE_RULES_v0.1.0.json",
    "cases": BASE / "PPIA-15_FOUNDATION_REFERENCE_CASES_v0.1.0.json",
    "package": BASE / "PPIA-15_FOUNDATION_PACKAGE_INDEX_v0.1.0.json",
}
NARRATIVE = BASE / "PPIA-15_FOUNDATION_EXISTING_TEST_CORPUS_AND_COVERAGE_GAP_INVENTORY.md"
BACKLOG = BASE / "PPIA_PROGRAM_BACKLOG.json"
CHECKPOINT = ROOT / "governance/ai/work-state/PPIA-15-attempt-001.json"
POINTER = ROOT / "governance/ai/runtime/CURRENT_WORK_POINTER.json"
STATUS = ROOT / "governance/ai/runtime/CURRENT_IMPLEMENTATION_STATUS.json"
WORKFLOW = ROOT / ".github/workflows/validate-ppia-15-foundation.yml"


def fail(message: str) -> None:
    print(f"::error title=PPIA-15 Foundation Validator::PPIA-15 FOUNDATION: FAIL — {message}")
    raise SystemExit("PPIA-15 FOUNDATION: FAIL — " + message)


def req(condition: bool, message: str) -> None:
    if not condition:
        fail(message)


def load(path: Path):
    req(path.exists(), f"missing {path.relative_to(ROOT)}")
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> None:
    docs = {name: load(path) for name, path in FILES.items()}
    backlog, checkpoint, pointer, status = map(load, (BACKLOG, CHECKPOINT, POINTER, STATUS))
    for path in (NARRATIVE, WORKFLOW):
        req(path.exists(), f"missing {path.relative_to(ROOT)}")
    for name, doc in docs.items():
        req(doc.get("work_item_id") == "PPIA-15", f"{name} work item changed")
        req(doc.get("artifact_version") == "0.1.0", f"{name} artifact version changed")

    manifest = docs["manifest"]
    expected_deps = {
        "PPIA-09": ("7393eac19d88eb5b2c58e44b51c1c3a2f3e2b968", 256, "3996ca97a2e31fa89ce5c9d4101c96affb83ea71", "31558007822"),
        "PPIA-10": ("507c9da21dd74d771f910861323693e2d7193bfa", 261, "b4ac8c080af7055e2d150ab6d37de41e9cc2a68f", "31585946135"),
        "PPIA-11": ("9bf4627f9e8e4a4c21dcc2614dcb74d54d62d724", 267, "f2274707b1337425f0bc9ac8d1dd5ebb08d9f883", "31595927902"),
        "PPIA-14": ("34c4575ad4ec7dad705b5e292b11c94699a648ac", 284, "2bebbfcfeac78081ab942be1a15eab1745d35c3a", "31646879101"),
    }
    deps = {d.get("work_item_id"): d for d in manifest.get("verified_dependencies", [])}
    req(set(deps) == set(expected_deps), "verified dependency set changed")
    for dep, expected in expected_deps.items():
        row = deps[dep]
        actual = (row.get("validated_head"), row.get("pull_request"), row.get("merge"), row.get("completion_run"))
        req(actual == expected, f"immutable {dep} evidence changed")
    req([s.get("id") for s in manifest.get("repository_sources", [])] == [f"P15-SRC-{i:03d}" for i in range(1, 21)], "20 source IDs changed")
    acct = manifest.get("primary_scenario_accounting", {})
    req(acct.get("effective_distinct_case_records_after_exact_alias_collapse") == 300, "manifest inherited count changed")
    req(acct.get("stage_a_reference_kit_additive_scenarios") == 0 and acct.get("tester_package_additive_scenarios") == 0, "packaging aliases became additive")
    req(acct.get("semantic_deduplication_complete") is False, "Foundation improperly claims semantic deduplication complete")
    source_gaps = {g.get("id"): g for g in manifest.get("source_gaps", [])}
    req(set(source_gaps) == {"P15-GAP-001"} and "F024" in source_gaps["P15-GAP-001"].get("subject", ""), "F024 source gap changed")
    req("Do not invent" in source_gaps["P15-GAP-001"].get("rule", ""), "F024 no-invention rule missing")
    fa = manifest.get("fixture_authority", {})
    req(fa.get("ppia15_fixtures_are_synthetic") is True and fa.get("ppia15_fixtures_are_noncanonical") is True, "fixture classification changed")
    req(fa.get("qa_fixture_may_promote_canonical_content") is False and fa.get("runtime_activation") is False and fa.get("tester_access_authorized") is False, "manifest activation boundary changed")

    inventory = docs["inventory"]
    corpora = inventory.get("corpora", [])
    req([c.get("id") for c in corpora] == [f"P15-COR-{i:03d}" for i in range(1, 8)], "seven inherited corpus IDs changed")
    req([c.get("additive_case_records") for c in corpora] == [24, 0, 0, 36, 90, 42, 108], "inherited additive accounting changed")
    ia = inventory.get("accounting", {})
    req((ia.get("raw_packaged_scenario_representations"), ia.get("exact_alias_representations_removed"), ia.get("primary_effective_case_records_after_exact_alias_collapse")) == (348, 48, 300), "exact-alias accounting changed")
    req(ia.get("semantic_overlap_still_requires_review") is True, "semantic overlap review boundary changed")
    req([r.get("id") for r in inventory.get("nonduplication_rules", [])] == [f"P15-ND-{i:03d}" for i in range(1, 9)], "eight nonduplication rules changed")
    req("must not clone" in inventory.get("baseline_coverage_anchors", {}).get("gm_modification", "").lower(), "GM baseline no-clone guard missing")

    taxonomy = docs["taxonomy"]
    req([x.get("id") for x in taxonomy.get("taxonomy_families", [])] == [f"P15-AX-{i:03d}" for i in range(1, 9)], "eight taxonomy IDs changed")
    awkward = taxonomy.get("required_awkward_families", [])
    req([x.get("id") for x in awkward] == [f"P15-AWK-{i:03d}" for i in range(1, 19)], "18 awkward-family IDs changed")
    expected_keys = ["simultaneous-selection","mid-session-reveals","entitlement-loss","gm-modifications","duplicate-name-objects","version-conflict","campaign-local-override","source-only-objects","vehicle-transfer","relationship-secret-reveal","interrupted-crafting","reconnect-during-approval","large-inventories","dense-creatures","unusual-species","mobile-only","keyboard-accessibility","offline-read-only"]
    req([x.get("key") for x in awkward] == expected_keys, "awkward-family vocabulary changed")
    req((len(taxonomy.get("roles", [])), len(taxonomy.get("contexts", [])), len(taxonomy.get("delivery_channels", []))) == (9, 20, 7), "role/context/channel dimensions changed")
    req((len(taxonomy.get("device_profiles", [])), len(taxonomy.get("interaction_modes", [])), len(taxonomy.get("accessibility_modes", [])), len(taxonomy.get("connection_states", []))) == (5, 5, 5, 5), "device/accessibility/connection dimensions changed")
    tax_text = json.dumps(taxonomy, ensure_ascii=False).lower()
    for phrase in ("do not duplicate baseline gm modification", "scale labels are qa dimensions only", "f024 pack lifecycle remains unsupported"):
        req(phrase in tax_text, f"taxonomy rule missing {phrase!r}")

    gapdoc = docs["gaps"]
    rows = gapdoc.get("rows", [])
    req([r.get("awkward_id") for r in rows] == [f"P15-AWK-{i:03d}" for i in range(1, 19)], "gap row IDs changed")
    req(Counter(r.get("status") for r in rows) == Counter({"partial_awkward_variant":10,"gap_direct":7,"baseline_covered_no_clone":1}), "7/10/1 gap split changed")
    gs = gapdoc.get("summary", {})
    req((gs.get("gap_direct"), gs.get("partial_awkward_variant"), gs.get("baseline_covered_no_clone"), gs.get("required_family_count"), gs.get("families_requiring_additive_or_composed_expansion")) == (7,10,1,18,17), "gap summary changed")
    gm = rows[3]
    req(gm.get("awkward_id") == "P15-AWK-004" and gm.get("status") == "baseline_covered_no_clone" and "do not clone" in gm.get("foundation_disposition", "").lower(), "GM baseline protection changed")
    gap_text = json.dumps(gapdoc, ensure_ascii=False).lower()
    for phrase in ("p15-gap-001/f024 remains open", "scale fixtures are deterministic qa inputs", "no ppia-15 case activates application runtime"):
        req(phrase in gap_text, f"gap blocking rule missing {phrase!r}")

    oracle = docs["oracle"]
    required_fields = set(oracle.get("oracle_model", {}).get("required_fields", []))
    for field in ("case_id","awkward_family_ids","nearest_inherited_anchors","material_differential","expected_authoritative_outcome","expected_nonvisual_projection","expected_provenance","forbidden_outcomes"):
        req(field in required_fields, f"oracle field missing {field}")
    oracle_text = json.dumps(oracle, ensure_ascii=False).lower()
    for phrase in ("status-unknown is not failure", "accepted durable event with projection lag", "offline/local state is not authoritative mutation", "silent last-write-wins is forbidden", "no balanced/fair/safe/winnable/optimal/guaranteed oracle"):
        req(phrase in oracle_text, f"oracle invariant missing {phrase!r}")
    access = oracle.get("accessibility_rules", {})
    for key in ("keyboard_complete","touch_complete","screen_reader_complete","mobile_single_focus_supported","high_zoom_reflow_supported","reduced_motion_supported","noncolor_equivalent_required","safe_semantic_parity_visual_nonvisual"):
        req(access.get(key) is True, f"accessibility requirement changed: {key}")
    iso = oracle.get("fixture_isolation", {})
    req(iso.get("classification") == "synthetic_noncanonical_qa_fixture" and iso.get("canonical") is False and iso.get("real_user_data") is False and iso.get("fixture_may_promote_itself") is False and iso.get("fixture_may_invent_missing_pack_lifecycle") is False and iso.get("fixture_may_override_owning_domain") is False, "fixture isolation changed")
    req(all(value is False for value in oracle.get("nonactivation", {}).values()), "oracle activation boundary changed")

    cases = docs["cases"]
    case_rows = cases.get("cases", [])
    req(cases.get("classification") == "synthetic_noncanonical_qa_foundation_fixture" and cases.get("canonical") is False, "Foundation case classification changed")
    req(cases.get("case_count") == 32 and len(case_rows) == 32, "32 Foundation cases changed")
    req([c.get("id") for c in case_rows] == [f"PPIA15-FC-{i:03d}" for i in range(1, 33)], "Foundation case IDs changed")
    allowed = {f"P15-AWK-{i:03d}" for i in range(1, 19)}
    covered = set()
    for case in case_rows:
        ids = set(case.get("awkward_family_ids", []))
        if case.get("id") == "PPIA15-FC-032":
            req(ids == set(), "F024 source-gap meta-case must not invent an awkward-family binding")
            req("F024" in case.get("title", "") and "source-gap" in case.get("expected", ""), "F024 source-gap meta-case changed")
        else:
            req(ids and ids <= allowed, f"invalid awkward-family binding in {case.get('id')}")
            covered |= ids
        for field in ("nearest_anchors", "material_differential", "fixture", "expected", "forbidden"):
            req(case.get(field), f"{case.get('id')} missing {field}")
    req(covered == allowed, "Foundation cases do not cover all 18 awkward families")
    cases_text = json.dumps(cases, ensure_ascii=False).lower()
    for phrase in ("512 synthetic", "128 synthetic", "status lookup", "screen-reader", "phone-portrait", "f024"):
        req(phrase in cases_text, f"Foundation corpus missing {phrase!r}")

    package = docs["package"]
    req([x.get("id") for x in package.get("package_artifacts", [])] == [f"P15-FND-{i:03d}" for i in range(1, 10)], "nine package-index IDs changed")
    locked = package.get("locked_counts", {})
    req((locked.get("primary_inherited_case_records_after_exact_alias_collapse"), locked.get("required_awkward_families"), locked.get("direct_gaps"), locked.get("partial_awkward_variants"), locked.get("baseline_covered_no_clone"), locked.get("foundation_reference_cases")) == (300,18,7,10,1,32), "package locked counts changed")
    accept = package.get("acceptance", {})
    req(accept.get("foundation_only_not_ppia15_completion") is True, "Foundation improperly claims whole PPIA-15 completion")
    for key in ("application_runtime_activation","stage_a_a2_activation","tester_access_activation","release_activation","deployment_activation","paid_service_activation","production_credentials_activation","canonical_promotion"):
        req(accept.get(key) is False, f"package activation boundary changed: {key}")

    narrative = NARRATIVE.read_text(encoding="utf-8").lower()
    for phrase in ("300 primary distinct case records", "7 direct gaps", "10 partial awkward variants", "1 baseline already covered", "32 synthetic noncanonical foundation cases", "p15-gap-001", "not ppia-15 completion"):
        req(phrase in narrative, f"narrative missing {phrase!r}")

    tranches = {x.get("work_item_id"): x for x in backlog.get("tranches", [])}
    for dep in ("PPIA-09","PPIA-10","PPIA-11","PPIA-14"):
        req(tranches.get(dep, {}).get("status") == "completed_verified", f"{dep} dependency not completed_verified")
    req(checkpoint.get("attempt_id") == "PPIA-15-attempt-001" and checkpoint.get("branch") == "governance/ppia-15-internal-alpha-test-content-expansion", "checkpoint identity changed")
    req(checkpoint.get("unresolved_failures") == [] and checkpoint.get("owner_decision_required") is False, "PPIA-15 unresolved blocker exists")
    current_id = backlog.get("current_work_item_id")
    if current_id == "PPIA-15":
        req(tranches.get("PPIA-15", {}).get("status") in {"started","ready_for_review"}, "active PPIA-15 status changed")
        req(checkpoint.get("status") in {"started","ready_for_review"}, "Foundation cannot complete whole PPIA-15")
        req(pointer.get("primary_attempt_id") == "PPIA-15-attempt-001", "pointer does not select PPIA-15")
        req(status.get("primary", {}).get("work_item_id") == "PPIA-15", "compact status does not select PPIA-15")
        continuity_mode = "active_ppia15"
    else:
        order = backlog.get("execution_order", [])
        req(current_id in order and "PPIA-15" in order and order.index(current_id) > order.index("PPIA-15"), "historical validation only allowed after PPIA-15")
        req(tranches.get("PPIA-15", {}).get("status") == "completed_verified", "historical PPIA-15 backlog must be completed_verified")
        req(checkpoint.get("status") == "completed_verified" and checkpoint.get("active_substep") is None and checkpoint.get("completed_at"), "historical checkpoint must be completed_verified")
        continuity_mode = "historical_after_ppia15"
    bounds = backlog.get("boundaries", {})
    for key in ("application_runtime_mutation_authorized","a2_activation_authorized","release_authorized","deployment_authorized","tester_access_authorized","canonical_promotion_without_source_evidence_authorized"):
        req(bounds.get(key) is False, f"program boundary changed: {key}")

    print("PPIA-15 FOUNDATION: PASS")
    print("inherited_case_records=300 awkward_families=18 direct_gaps=7 partial_gaps=10 baseline_no_clone=1")
    print("foundation_reference_cases=32 synthetic_noncanonical=true f024_gap_open=true")
    print("roles=9 contexts=20 channels=7 devices=5 interactions=5 accessibility_modes=5 connection_states=5")
    print(f"continuity_mode={continuity_mode} runtime_activation=false a2_activation=false tester_access=false release=false deployment=false")


if __name__ == "__main__":
    main()
