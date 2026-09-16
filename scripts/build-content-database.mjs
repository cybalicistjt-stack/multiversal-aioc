// Compatibility entrypoint. The certified 3.0 canonical pipeline is authoritative.
// Keep this filename working for historical/deployment callers without maintaining
// a second content-database algorithm.
await import('./materialize-content-source.mjs');
await import('./build-canonical-content-database.mjs');
