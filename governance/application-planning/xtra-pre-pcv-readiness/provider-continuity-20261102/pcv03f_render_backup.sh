#!/usr/bin/env bash
# XTRA-02 operator-only PostgreSQL 17 logical export.
# Run on a trusted Linux host with encrypted private backup storage, NEVER in GitHub Actions.
# This file contains NO credentials or data; it does not open network access or change source data.
set -euo pipefail
umask 077
fail(){ printf 'ERROR: %s\n' "$*" >&2; exit 1; }
for bin in pg_dump pg_restore sha256sum date stat; do command -v "$bin" >/dev/null 2>&1 || fail "Missing $bin"; done
for var in PGHOST PGPORT PGDATABASE PGUSER PGPASSFILE MV_BACKUP_DIR; do
  [[ -n "${!var:-}" ]] || fail "Set $var privately; MV_BACKUP_DIR must be on an encrypted private volume."
done
[[ "${MV_BACKUP_ENCRYPTED_CONFIRMED:-}" == YES ]] || fail "Confirm your backup path uses encrypted storage: set MV_BACKUP_ENCRYPTED_CONFIRMED=YES."
[[ -f "$PGPASSFILE" && -r "$PGPASSFILE" && ! -L "$PGPASSFILE" ]] || fail "Private readable regular non-symlink PGPASSFILE required."
perm=$(stat -c '%a' "$PGPASSFILE")
(( (8#$perm & 8#077) == 0 )) || fail "PGPASSFILE must be inaccessible to group/others (chmod 600)."
[[ "$(pg_dump --version)" == *" 17."* ]] || fail "Use PostgreSQL 17 pg_dump for source PG17."
export PGSSLMODE=require
mkdir -p -- "$MV_BACKUP_DIR"
[[ -d "$MV_BACKUP_DIR" && ! -L "$MV_BACKUP_DIR" ]] || fail "Backup directory must not be a symlink."
chmod 700 "$MV_BACKUP_DIR"
stamp=$(date -u +%Y%m%dT%H%M%SZ)
name="pcv03f-cert-$stamp"
target="$MV_BACKUP_DIR/$name.dump"
partial="$MV_BACKUP_DIR/.$name.partial"
[[ ! -e "$target" && ! -e "$partial" ]] || fail "Refusing to overwrite previous export."
trap 'rm -f -- "$partial"' EXIT
pg_dump --format=custom --no-owner --no-acl --file="$partial"
[[ -s "$partial" ]] || fail "Dump was empty or missing."
pg_restore --list "$partial" > /dev/null || fail "Dump index validation failed."
mv -- "$partial" "$target"
trap - EXIT
(
  cd -- "$MV_BACKUP_DIR"
  sha256sum "$name.dump" > "$name.dump.sha256"
  sha256sum --check --status "$name.dump.sha256" || fail "Checksum verification failed."
)
printf 'EXPORT STRUCTURE CHECK PASSED; INDEPENDENT RESTORE STILL REQUIRED\nFile: %s\nBytes: %s\nChecksum: %s\n' "$target" "$(stat -c '%s' "$target")" "$target.sha256"
printf 'Keep encrypted dump and credentials OUT of all git repositories. Remove temporary single-host allowlist promptly.\n'
