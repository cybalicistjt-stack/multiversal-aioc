#!/usr/bin/env python3
"""Extract and inventory the Multiversal legacy ZIP corpus.

This tool expands every configured archive into a deterministic working tree,
indexes every PDF and CSV member, and preserves archive/member provenance for
later forensic extraction. It is intentionally separate from canonical review.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import shutil
import zipfile
from pathlib import Path
from typing import Any


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def safe_member_path(name: str) -> Path:
    normalized = Path(name.replace('\\', '/'))
    if normalized.is_absolute() or '..' in normalized.parts:
        raise ValueError(f'Unsafe ZIP member path: {name}')
    return normalized


def load_manifest(path: Path) -> dict[str, Any]:
    payload = json.loads(path.read_text(encoding='utf-8'))
    if payload.get('format') != 'multiversal-forensic-archive-corpus':
        raise ValueError('Unrecognized archive corpus manifest')
    return payload


def extract_archive(repo_root: Path, archive_info: dict[str, Any], out_root: Path) -> dict[str, Any]:
    archive_path = repo_root / archive_info['path']
    group = archive_info['group']
    result: dict[str, Any] = {
        'archive': archive_info['path'],
        'group': group,
        'required': bool(archive_info.get('required')),
        'present': archive_path.exists(),
        'members': [],
        'errors': [],
    }
    if not archive_path.exists():
        return result

    group_root = out_root / group
    if group_root.exists():
        shutil.rmtree(group_root)
    group_root.mkdir(parents=True, exist_ok=True)

    with zipfile.ZipFile(archive_path) as zf:
        for info in sorted(zf.infolist(), key=lambda item: item.filename.lower()):
            if info.is_dir():
                continue
            try:
                relative = safe_member_path(info.filename)
            except ValueError as exc:
                result['errors'].append(str(exc))
                continue
            suffix = relative.suffix.lower()
            if suffix not in {'.pdf', '.csv'}:
                continue
            data = zf.read(info)
            destination = group_root / relative
            destination.parent.mkdir(parents=True, exist_ok=True)
            destination.write_bytes(data)
            result['members'].append({
                'archive': archive_info['path'],
                'group': group,
                'member': info.filename,
                'extractedPath': str(destination.relative_to(repo_root)),
                'type': suffix[1:],
                'bytes': len(data),
                'sha256': sha256_bytes(data),
                'compressedBytes': info.compress_size,
            })
    result['memberCount'] = len(result['members'])
    result['pdfCount'] = sum(1 for item in result['members'] if item['type'] == 'pdf')
    result['csvCount'] = sum(1 for item in result['members'] if item['type'] == 'csv')
    return result


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument('--repo-root', type=Path, default=Path('.'))
    parser.add_argument('--manifest', type=Path, default=Path('audit/archive-corpus-manifest.json'))
    parser.add_argument('--out', type=Path, default=Path('audit-work/corpus'))
    parser.add_argument('--inventory', type=Path, default=Path('audit-output/archive-inventory.json'))
    args = parser.parse_args()

    repo_root = args.repo_root.resolve()
    manifest_path = args.manifest if args.manifest.is_absolute() else repo_root / args.manifest
    out_root = args.out if args.out.is_absolute() else repo_root / args.out
    inventory_path = args.inventory if args.inventory.is_absolute() else repo_root / args.inventory
    out_root.mkdir(parents=True, exist_ok=True)
    inventory_path.parent.mkdir(parents=True, exist_ok=True)

    manifest = load_manifest(manifest_path)
    archive_results = [extract_archive(repo_root, item, out_root) for item in manifest['archives']]
    missing_required = [item['archive'] for item in archive_results if item['required'] and not item['present']]
    members = [member for archive in archive_results for member in archive['members']]
    duplicate_hashes: dict[str, list[dict[str, Any]]] = {}
    for member in members:
        duplicate_hashes.setdefault(member['sha256'], []).append(member)
    duplicate_groups = [group for group in duplicate_hashes.values() if len(group) > 1]

    inventory = {
        'format': 'multiversal-forensic-archive-inventory',
        'version': '1.0.0',
        'manifest': str(manifest_path.relative_to(repo_root)),
        'archiveCount': len(archive_results),
        'presentArchiveCount': sum(1 for item in archive_results if item['present']),
        'missingRequiredArchives': missing_required,
        'memberCount': len(members),
        'pdfCount': sum(1 for item in members if item['type'] == 'pdf'),
        'csvCount': sum(1 for item in members if item['type'] == 'csv'),
        'duplicateMemberGroups': duplicate_groups,
        'archives': archive_results,
        'members': members,
        'readyForCompleteAudit': not missing_required,
    }
    inventory_path.write_text(json.dumps(inventory, indent=2, ensure_ascii=False) + '\n', encoding='utf-8')
    print(json.dumps({
        'presentArchives': inventory['presentArchiveCount'],
        'missingRequiredArchives': missing_required,
        'pdfCount': inventory['pdfCount'],
        'csvCount': inventory['csvCount'],
        'duplicateGroups': len(duplicate_groups),
        'inventory': str(inventory_path),
    }, indent=2))


if __name__ == '__main__':
    main()
