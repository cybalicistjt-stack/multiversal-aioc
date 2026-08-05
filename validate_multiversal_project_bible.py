#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import re
from pathlib import Path


def outside_code_lines(markdown: str):
    in_code = False
    for number, line in enumerate(markdown.splitlines(), 1):
        if line.startswith("```"):
            in_code = not in_code
            continue
        if not in_code:
            yield number, line
    if in_code:
        raise AssertionError("Unbalanced fenced code block.")


def validate(path: Path) -> None:
    text = path.read_text(encoding="utf-8")
    outside = list(outside_code_lines(text))

    h1 = [(number, line[2:]) for number, line in outside if line.startswith("# ")]
    titles = [title for _, title in h1]
    if len(titles) != len(set(titles)):
        duplicates = sorted({title for title in titles if titles.count(title) > 1})
        raise AssertionError(f"Duplicate H1 headings: {duplicates}")

    chapters = []
    appendices = []
    volumes = []
    reviews = []
    for number, line in outside:
        if match := re.match(r"^# (\d+)\. (.+)$", line):
            chapters.append((int(match.group(1)), match.group(2), number))
        elif match := re.match(r"^# Appendix ([A-J]) — (.+)$", line):
            appendices.append((match.group(1), match.group(2), number))
        elif line.startswith("# Volume "):
            volumes.append((number, line))
        elif re.match(r"^# Tranche [2-8] Integration Review$", line):
            reviews.append((number, line))

    assert [number for number, _, _ in chapters] == list(range(1, 81))
    assert [letter for letter, _, _ in appendices] == list("ABCDEFGHIJ")
    assert len(volumes) == 8
    assert len(reviews) == 7

    toc_start = text.index("# Master Table of Contents")
    toc_end = text.index("\n# Volume I — Project Foundation", toc_start)
    toc_text = text[toc_start:toc_end]
    toc_chapters = []
    for line in toc_text.splitlines():
        if match := re.match(r"^(\d+)\. (.+)$", line):
            toc_chapters.append((int(match.group(1)), match.group(2)))
    assert toc_chapters == [(number, title) for number, title, _ in chapters]

    for review_number in range(2, 9):
        assert f"*Tranche {review_number} Integration Review*" in toc_text

    lines = text.splitlines()
    issues = []
    for index, (chapter_number, _, start_line) in enumerate(chapters):
        end_line = chapters[index + 1][2] - 1 if index + 1 < len(chapters) else len(lines)
        sections = []
        for line_number in range(start_line + 1, end_line + 1):
            line = lines[line_number - 1]
            if match := re.match(r"^## (\d+)\.(\d+) ", line):
                prefix, section = int(match.group(1)), int(match.group(2))
                if prefix != chapter_number:
                    issues.append(
                        f"Chapter {chapter_number} has prefix {prefix} at line {line_number}."
                    )
                sections.append(section)
        if sections and sections != list(range(sections[0], sections[0] + len(sections))):
            issues.append(f"Chapter {chapter_number} has noncontiguous sections: {sections}")
    assert not issues, issues

    assert text.count("**Next Step:**") == 1
    assert "49. Inventory, Shared Assets, Crafting, and Vehicles" in toc_text
    assert "50. Investigation and Social Workspaces" in toc_text

    digest = hashlib.sha256(path.read_bytes()).hexdigest()
    print("MULTIVERSAL PROJECT BIBLE VALIDATION: PASS")
    print(f"Path: {path}")
    print(f"Chapters: {len(chapters)}")
    print(f"Appendices: {len(appendices)}")
    print(f"Volumes: {len(volumes)}")
    print(f"Integration reviews: {len(reviews)}")
    print(f"SHA-256: {digest}")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("path", type=Path)
    args = parser.parse_args()
    validate(args.path)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
