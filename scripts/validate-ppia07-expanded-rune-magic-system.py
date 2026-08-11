#!/usr/bin/env python3
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / "governance/application-planning/parallel-preimplementation"
SYSTEM = BASE / "PPIA-07_EXPANDED_RUNE_MAGIC_SYSTEM_v0.2.0.json"
AUDIT = BASE / "PPIA-07_SOURCE_SPELL_COVERAGE_AUDIT_v0.2.0.json"
CORPUS = BASE / "PPIA-07_EXPANDED_RUNE_REFERENCE_CORPUS_v0.2.0.json"
NOTE = BASE / "PPIA-07_EXPANDED_RUNE_MAGIC_SYSTEM_CANDIDATE.md"


def load(path):
    return json.loads(path.read_text(encoding="utf-8"))


def require(cond, msg):
    if not cond:
        raise AssertionError(msg)


def main():
    for path in (SYSTEM, AUDIT, CORPUS, NOTE):
        require(path.exists(), f"missing {path.relative_to(ROOT)}")

    system = load(SYSTEM)
    audit = load(AUDIT)
    corpus = load(CORPUS)
    note = NOTE.read_text(encoding="utf-8")

    require(system["work_item_id"] == "PPIA-07", "wrong work item")
    require(system["schema_version"] == "0.2.0", "wrong system version")
    require(system["rune_count"] == 34, "expanded system must contain 34 runes")
    require(system["rune_families"] == {"operation": 16, "essence": 18}, "rune family counts drifted")

    operations = [r["id"] for r in system["operation_runes"]]
    essences = [r["id"] for r in system["essence_runes"]]
    require(len(operations) == len(set(operations)) == 16, "operation rune IDs must be 16 unique IDs")
    require(len(essences) == len(set(essences)) == 18, "essence rune IDs must be 18 unique IDs")
    require(not set(operations) & set(essences), "operation and essence IDs must not collide")

    legacy = {"SOURCE","MOVE","SHAPE","BIND","CHANGE","SENSE","WARD","LINK"}
    additions = {"RESTORE","UNMAKE","VEIL","CALL","BANISH","COMMAND","DRAIN","IMBUE"}
    expected_essences = {"FIRE","COLD","LIGHTNING","AIR","WATER","EARTH","ACID","FORCE","LIGHT","VOID","LIFE","MIND","SPIRIT","NATURE","SPACE","TIME","SOUND","ARCANE"}
    require(legacy <= set(operations), "verified legacy operation runes not preserved")
    require(additions <= set(operations), "expanded operation family incomplete")
    require(set(essences) == expected_essences, "expanded essence family drifted")

    connector_ids = [c["id"] for c in system["connector_grammar_inherited"]]
    require(connector_ids == ["THEN","WITH","WHEN","IF"], "verified connector grammar drifted")
    require(system["payload_rune_rule"]["standalone_essence_node_allowed"] is False, "essence nodes must remain typed payload glyphs")
    require("payload=rune:ESSENCE_ID" == system["payload_rune_rule"]["syntax"], "payload rune syntax drifted")
    require(system["progressive_disclosure"]["hard_unlocks_defined_here"] is False, "expansion must not invent hard unlocks")
    require(system["final_balance_boundary"].startswith("PPIA-11"), "PPIA-11 balance authority must be preserved")

    require(audit["source"]["spell_rows"] == 385, "source spell row count drifted")
    require(sum(audit["primary_school_counts"].values()) == 385, "school counts must sum to 385")
    require(sum(audit["spell_role_counts"].values()) == 385, "role counts must sum to 385")
    expected_schools = {"Creation","Destruction","Void","Perception","Transition","Emotion","Balance","Stasis","Essence","Energy"}
    require(set(audit["primary_school_counts"]) == expected_schools, "ten-school source coverage drifted")
    expected_roles = {"Offense","Control","Support","Reconnaissance","Mobility","Defense","Utility"}
    require(set(audit["spell_role_counts"]) == expected_roles, "seven-role source coverage drifted")
    require(len(audit["normalized_effect_family_counts"]) == 14, "expected 14 normalized effect families")
    require(len(audit["effect_family_to_operation_runes"]) == 14, "all effect families must map")
    require(len(audit["normalized_subtype_counts"]) == 22, "expected 22 normalized subtype families")
    require(len(audit["subtype_to_essence_runes"]) == 22, "all subtype families must map")
    for routes in audit["effect_family_to_operation_runes"].values():
        require(routes and set(routes) <= set(operations), "effect mapping references unknown operation")
    for routes in audit["subtype_to_essence_runes"].values():
        require(routes and set(routes) <= set(essences), "subtype mapping references unknown essence")
    coverage = audit["route_coverage"]
    require(coverage["spell_rows_examined"] == coverage["school_rows_with_supported_school_route"] == coverage["spell_rows_with_supported_gameplay_role"] == 385, "385-row source routing incomplete")
    require(coverage["normalized_effect_tokens_total"] == coverage["normalized_effect_tokens_mapped"] == 14, "effect-token coverage incomplete")
    require(coverage["normalized_subtype_tokens_total"] == coverage["normalized_subtype_tokens_mapped"] == 22, "subtype-token coverage incomplete")
    require(coverage["unmapped_effect_tokens"] == [], "unmapped effect tokens remain")
    require(coverage["unmapped_subtype_tokens"] == [], "unmapped subtype tokens remain")
    require(coverage["unroutable_spell_ids"] == [], "unroutable source spell IDs remain")

    cases = corpus["cases"]
    require(len(cases) == 34, "expanded reference corpus must contain 34 cases")
    require([c["case_id"] for c in cases] == [f"PPIA07-ER-{i:03d}" for i in range(1,35)], "reference case IDs must be contiguous")
    covered_ops = set()
    covered_ess = set()
    for c in cases:
        require(c["expected"], f"case {c['case_id']} missing expected state")
        require(c["acceptance"], f"case {c['case_id']} missing acceptance text")
        covered_ops.update(c["covers_operations"])
        covered_ess.update(c["covers_essences"])
    require(set(operations) <= covered_ops, f"operation coverage gap: {sorted(set(operations)-covered_ops)}")
    require(set(essences) <= covered_ess, f"essence coverage gap: {sorted(set(essences)-covered_ess)}")
    require(corpus["policy"]["examples_define_final_balance"] is False, "corpus may not define final balance")
    require(corpus["policy"]["examples_replace_source_spells"] is False, "corpus may not replace source spells")
    require(corpus["policy"]["standalone_essence_allowed"] is False, "standalone essence execution must stay invalid")
    require(corpus["policy"]["implicit_multi_payload_allowed"] is False, "implicit multi-payload syntax must stay invalid")
    require(corpus["policy"]["permission_leak_allowed"] is False, "permission leak policy drifted")
    require(corpus["policy"]["retry_may_duplicate_write_or_resource_use"] is False, "idempotency guardrail drifted")

    for required in ["34 runes", "16 Operation Runes", "18 Essence Runes", "385 spells", "PPIA-11", "permission", "expected-version"]:
        require(required.lower() in note.lower(), f"candidate note missing {required}")

    print("PPIA-07 EXPANDED RUNE MAGIC SYSTEM: PASS")
    print("runes=34 operation=16 essence=18 connectors=4")
    print("source_spells=385 schools=10 roles=7 effect_families=14 subtype_families=22")
    print("expanded_reference_cases=34")
    print("final_balance_owner=PPIA-11")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
