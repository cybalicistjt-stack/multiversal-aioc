#!/usr/bin/env python3
import json
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / "governance/application-planning/parallel-preimplementation"

SPEC = BASE / "PPIA-07_RUNE_CONSTRUCTION_EXPERIENCE_SPEC_v1.0.0.md"
BLIND_PROFILE = BASE / "PPIA-07_BLIND_RUNE_PLAY_CONSUMER_PROFILE_v1.0.0.json"
BLIND_CASES = BASE / "PPIA-07_BLIND_RUNE_PLAY_REFERENCE_CASES_v1.0.0.json"
ACCEPTANCE = BASE / "PPIA-07_ACCEPTANCE_TRACEABILITY_MATRIX_v1.0.0.json"
CANDIDATE = BASE / "PPIA-07_COMPLETION_CANDIDATE.md"
EXPANDED = BASE / "PPIA-07_EXPANDED_RUNE_MAGIC_SYSTEM_v0.2.0.json"
AUDIT = BASE / "PPIA-07_SOURCE_SPELL_COVERAGE_AUDIT_v0.2.0.json"
EXPANDED_CASES = BASE / "PPIA-07_EXPANDED_RUNE_REFERENCE_CORPUS_v0.2.0.json"
GRAMMAR_CASES = BASE / "PPIA-07_RUNE_REFERENCE_CORPUS_v0.1.0.json"
CSP_CASES = BASE / "PPIA-07_COST_STABILITY_PROGRESSION_BENCHMARKS_v0.1.0.json"
WORKFLOWS = BASE / "PPIA-07_RUNE_BUILDER_WORKFLOW_AUTHORING_CONTRACT_MATRIX_v0.1.0.json"


def load(path):
    return json.loads(path.read_text(encoding="utf-8"))


def require(cond, msg):
    if not cond:
        raise AssertionError(msg)


def main():
    required_paths = [SPEC, BLIND_PROFILE, BLIND_CASES, ACCEPTANCE, CANDIDATE, EXPANDED, AUDIT, EXPANDED_CASES, GRAMMAR_CASES, CSP_CASES, WORKFLOWS]
    for path in required_paths:
        require(path.exists(), f"missing {path.relative_to(ROOT)}")

    spec = SPEC.read_text(encoding="utf-8")
    candidate = CANDIDATE.read_text(encoding="utf-8")
    blind = load(BLIND_PROFILE)
    blind_cases = load(BLIND_CASES)
    acceptance = load(ACCEPTANCE)
    expanded = load(EXPANDED)
    audit = load(AUDIT)
    er = load(EXPANDED_CASES)
    rc = load(GRAMMAR_CASES)
    csp = load(CSP_CASES)
    workflows = load(WORKFLOWS)

    # Final vocabulary and inherited grammar.
    require(expanded["rune_count"] == 34, "final vocabulary must contain 34 runes")
    require(expanded["rune_families"] == {"operation": 16, "essence": 18}, "final rune-family counts drifted")
    operations = [r["id"] for r in expanded["operation_runes"]]
    essences = [r["id"] for r in expanded["essence_runes"]]
    require(len(operations) == len(set(operations)) == 16, "operation rune IDs invalid")
    require(len(essences) == len(set(essences)) == 18, "essence rune IDs invalid")
    require([c["id"] for c in expanded["connector_grammar_inherited"]] == ["THEN", "WITH", "WHEN", "IF"], "connector grammar drifted")
    require(expanded["payload_rune_rule"]["standalone_essence_node_allowed"] is False, "essence runes must remain typed payload glyphs")
    require(expanded["final_balance_boundary"].startswith("PPIA-11"), "PPIA-11 final balance boundary drifted")

    # Source coverage claim remains bounded and exact.
    coverage = audit["route_coverage"]
    require(audit["source"]["spell_rows"] == 385, "spell row count drifted")
    require(len(audit["primary_school_counts"]) == 10, "expected ten source schools")
    require(len(audit["spell_role_counts"]) == 7, "expected seven spell roles")
    require(len(audit["normalized_effect_family_counts"]) == 14, "expected fourteen effect families")
    require(len(audit["normalized_subtype_counts"]) == 22, "expected twenty-two subtype families")
    require(coverage["unroutable_spell_ids"] == [], "vocabulary-level unroutable spell IDs remain")

    # Reference sets are all preserved.
    require(len(rc["cases"]) == 20, "grammar/reference corpus must retain 20 cases")
    require([c["case_id"] for c in rc["cases"]] == [f"PPIA07-RC-{i:03d}" for i in range(1, 21)], "grammar case IDs drifted")
    require(len(er["cases"]) == 34, "expanded-rune corpus must retain 34 cases")
    require([c["case_id"] for c in er["cases"]] == [f"PPIA07-ER-{i:03d}" for i in range(1, 35)], "expanded case IDs drifted")
    require(len(csp["cases"]) == 16, "cost/stability/progression corpus must retain 16 cases")
    require([c["case_id"] for c in csp["cases"]] == [f"PPIA07-CSP-{i:03d}" for i in range(1, 17)], "CSP case IDs drifted")

    # Integrated workflow package remains intact.
    require(len(workflows["workflows"]) == 16, "Rune Builder workflow count drifted")
    require(len(workflows["action_contracts"]) == 18, "Rune Builder action count drifted")
    require(len(workflows["handoff_contracts"]) == 10, "Rune Builder handoff count drifted")

    # Blind rune-play is a blocking completion capability.
    profile = blind["consumer_profile"]
    require(profile["consumerProfileId"] == "PPIA07-BLIND-RUNE-PLAY", "wrong blind consumer profile")
    require(blind["policy_switch"]["blind_value"] == "blind-gm-adjudicated", "wrong blind-mode policy value")
    require(blind["player_predecision_projection"]["no_effect_preview"] is True, "blind player effect preview must be suppressed")
    require(blind["player_predecision_projection"]["no_hidden_effect_in_tooltips_counts_errors_exports_diagnostics_notifications_or_ai"] is True, "blind projection side channels not blocked")
    require(blind["gm_decision_projection"]["effect_resolution_visible_to_authorized_decider"] is True, "GM must receive interpreted effect")
    require(blind["gm_decision_projection"]["permission_filter_before_resolution_and_serialization"] is True, "GM resolution must stay permission-safe")
    require(blind["decision_contract"]["final_decision_types"] == ["approve", "deny", "modify-and-approve"], "blind final decision set drifted")
    require(blind["decision_contract"]["silence_is_approval"] is False, "silence may never approve blind rune play")
    require(blind["decision_contract"]["one_final_decision_may_win"] is True, "only one blind final decision may win")
    require("original" in blind["decision_contract"]["rune_expression_rewrite_rule"].lower(), "expression rewrite must preserve original")
    require(blind["atomic_commit_contract"]["partial_success_exposed_as_complete"] is False, "partial blind commit may not appear complete")
    require(blind["atomic_commit_contract"]["operation_id_required"] is True, "blind commit requires operation ID")
    require(blind["atomic_commit_contract"]["expected_version_required"] is True, "blind commit requires expected version")
    require(blind["ai_boundary"]["player_ai_may_decode_or_predict_hidden_effect"] is False, "player AI cannot decode blind effect")
    require(blind["ai_boundary"]["ai_may_approve_deny_modify_or_commit"] is False, "AI cannot decide blind proposal")
    require(blind["offline_and_recovery"]["offline_effect_resolution_for_player_allowed"] is False, "offline blind effect resolution must be blocked")
    require(blind["accessibility"]["blindness_of_gameplay_never_means_visual_only_ui"] is True, "blind mode must remain accessible")

    bcases = blind_cases["cases"]
    require(len(bcases) == 16, "blind rune-play corpus must contain 16 cases")
    require([c["case_id"] for c in bcases] == [f"PPIA07-BR-{i:03d}" for i in range(1, 17)], "blind case IDs must be contiguous")
    for case in bcases:
        require(case["expected_player_predecision"], f"{case['case_id']} missing player projection")
        require(case["expected_gm"], f"{case['case_id']} missing GM projection")
        require(case["acceptance"], f"{case['case_id']} missing acceptance text")
    require(blind_cases["policy"]["blind_player_effect_preview_allowed"] is False, "blind case policy permits effect preview")
    require(blind_cases["policy"]["silence_is_approval"] is False, "blind case policy permits silent approval")
    require(blind_cases["policy"]["player_ai_hidden_effect_decode_allowed"] is False, "blind case policy permits AI side channel")
    require(blind_cases["policy"]["duplicate_submit_or_commit_allowed"] is False, "blind case policy permits duplicate effects")

    # Final acceptance matrix: 48 blocking requirements / 16 categories.
    reqs = acceptance["requirements"]
    require(len(reqs) == 48, "final acceptance matrix must contain 48 requirements")
    require([r["requirement_id"] for r in reqs] == [f"PPIA07-AC-{i:03d}" for i in range(1, 49)], "acceptance IDs must be contiguous")
    categories = Counter(r["category"] for r in reqs)
    expected_categories = set(acceptance["coverage"]["categories"])
    require(len(expected_categories) == acceptance["coverage"]["category_count"] == 16, "acceptance category count drifted")
    require(set(categories) == expected_categories, "acceptance categories do not match coverage declaration")
    require(all(v == 3 for v in categories.values()), "each final acceptance category must contain exactly three requirements")
    for req in reqs:
        require(req["requirement"], f"{req['requirement_id']} missing requirement text")
        require(req["traces"], f"{req['requirement_id']} missing traces")
        require(req["reference_cases"], f"{req['requirement_id']} missing reference cases")
    require(acceptance["coverage"]["rune_registry"] == {"operation": 16, "essence": 18, "total": 34, "connectors": 4}, "acceptance rune coverage drifted")
    require(acceptance["coverage"]["workflow_contract"] == {"workflows": 16, "actions": 18, "handoffs": 10}, "acceptance workflow coverage drifted")
    require(acceptance["blocking_policy"]["blind_player_effect_preview_allowed"] is False, "completion policy permits blind preview")
    require(acceptance["blocking_policy"]["silence_is_approval"] is False, "completion policy permits silent approval")
    require(acceptance["blocking_policy"]["gm_silent_expression_rewrite_allowed"] is False, "completion policy permits silent expression rewrite")
    require(acceptance["blocking_policy"]["universal_cost_or_failure_formula_allowed"] is False, "completion policy permits universal cost/failure formula")
    require(acceptance["blocking_policy"]["permission_leak_allowed"] is False, "completion policy permits permission leak")
    require(acceptance["blocking_policy"]["duplicate_authoritative_effect_allowed"] is False, "completion policy permits duplicate effect")
    require(acceptance["blocking_policy"]["final_balance_owner"] == "PPIA-11", "final balance owner drifted")

    # Human-readable final specification/candidate must state the critical contracts.
    required_spec_terms = [
        "34 core runes",
        "16 Operation Runes",
        "18 Essence Runes",
        "blind-gm-adjudicated",
        "player constructs the runes",
        "explicitly chooses whether it goes through",
        "approve",
        "deny",
        "modify-and-approve",
        "Silence is never approval",
        "server-side role projection",
        "PPIA-11",
        "expected_version",
        "operation_id",
        "385 retained spells",
        "20 deterministic grammar/reference cases",
        "34 expanded-rune cases",
        "16 blind rune-play cases",
        "48 final acceptance requirements"
    ]
    low_spec = spec.lower()
    for term in required_spec_terms:
        require(term.lower() in low_spec, f"final spec missing required term: {term}")

    for term in ["blind rune-play", "34 core runes", "48 blocking requirements", "not complete until", "PPIA-08"]:
        require(term.lower() in candidate.lower(), f"completion candidate missing {term}")

    print("PPIA-07 COMPLETION CONTRACT: PASS")
    print("runes=34 operation=16 essence=18 connectors=4")
    print("source_spells=385 schools=10 roles=7 effect_families=14 subtype_families=22")
    print("cases=20 grammar + 34 expanded + 16 csp + 16 blind")
    print("workflow_contract=16 workflows / 18 actions / 10 handoffs")
    print("acceptance=48 requirements / 16 categories")
    print("blind_mode=player effect suppressed; GM interpreted effect; approve/deny/modify-and-approve; silence=false")
    print("final_balance_owner=PPIA-11")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
