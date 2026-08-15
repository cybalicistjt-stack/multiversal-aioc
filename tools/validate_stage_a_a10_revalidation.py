from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RECORD = ROOT / "governance/application-planning/stage-a-a10/current-revalidation/STAGE_A_A10_CURRENT_REPOSITORY_REVALIDATION.json"
HANDOFF = ROOT / "governance/application-planning/stage-a-a10/current-revalidation/STAGE_A_A10_CURRENT_REPOSITORY_REVALIDATION.md"
CHECKPOINT = ROOT / "governance/ai/work-state/STAGE-A-A10-current-revalidation-attempt-001.json"


def main() -> int:
    assert RECORD.is_file()
    assert HANDOFF.is_file()
    assert CHECKPOINT.is_file()
    record = json.loads(RECORD.read_text(encoding="utf-8"))
    checkpoint = json.loads(CHECKPOINT.read_text(encoding="utf-8"))
    assert record["work_item_id"] == "STAGE-A-A10"
    assert record["verdict"] == "PASS_READY_FOR_BOUNDED_A10_ACTIVATION"
    assert record["implementation_activated"] is False
    assert record["application_baseline"] == "e0c88756326d00e75d16ee27c198b80b7010f88a"
    assert record["a9_merge"] == "c2030febf860a4fc9bcac9c65fa44a6b22418dd4"
    assert record["next_migration"] == "database/migrations/0008_a10_world_content_authoring.json"
    assert record["source_package"]["source_slices"] == 32
    assert record["source_package"]["deterministic_fixtures"] == 120
    assert record["source_package"]["published_blocking_acceptance_criteria"] == 140
    assert record["source_package"]["families"] == [
        "WSM-S01..WSM-S08", "AM-S01..AM-S08", "CC-S01..CC-S08", "AI-S01..AI-S08"
    ]
    assert set(record["canonical_domains"].values()) == {
        "pack-registry", "entity-catalog", "world-location-map", "adventure-travel",
        "authoring-provenance", "visibility-projection", "media-attachments"
    }
    assert record["authority_boundaries"]["canonical_promotion_owner_only"] is True
    assert record["authority_boundaries"]["hidden_information_filtered_before_derived_output"] is True
    assert record["authority_boundaries"]["monolithic_authoring_persistence_prohibited"] is True
    assert all(value is False for value in record["restrictions"].values())
    assert checkpoint["work_item_id"] == "STAGE-A-A10"
    assert checkpoint["branch"] == "governance/stage-a-a10-current-revalidation"
    assert checkpoint["restrictions"]["a10_activated"] is False
    handoff = HANDOFF.read_text(encoding="utf-8")
    for required in (
        "PASS — READY FOR BOUNDED A10 ACTIVATION",
        "0008_a10_world_content_authoring.json",
        "IA-D07-003",
        "A9 now concretely owns Campaign-runtime relationship/faction/social/investigation state",
        "canonical promotion",
        "Arbitrary executable code",
    ):
        assert required in handoff, required
    print("STAGE-A-A10 CURRENT-REPOSITORY REVALIDATION: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
