# VCH Deterministic Receipt Invariants

Planning invariants: explicit schema version; repository-relative `/` paths; canonical UTF-8 serialization; stable key/collection ordering; machine-specific values excluded from deterministic payloads; timestamps/durations excluded from deterministic hashes unless explicitly normalized; SHA-256 over canonical bytes.
