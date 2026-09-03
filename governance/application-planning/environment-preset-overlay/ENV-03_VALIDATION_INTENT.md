# ENV-03 Validation Intent

The ENV-03 merge candidate must pass the canonical repository-health workflow on its exact rebased head. Required checks include current authority/lifecycle validation and the complete `tests/control_plane/test_*.py` regression suite, including `test_env03_archetype_extraction.py`.

Merge is not authorized if any current software-roadmap authority is lost, if any of the 40 ENV-02 profiles is unmapped, if any crosswalk archetype ID is absent from the ENV-03 library, or if ENV-04 is not the sole selected successor.
