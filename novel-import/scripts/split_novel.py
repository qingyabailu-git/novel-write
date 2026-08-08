#!/usr/bin/env python3
"""Preview or split a UTF-8 TXT/Markdown novel by chapter headings."""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path


DEFAULT_PATTERN = r"^\s*(?:(?:第[0-9０-９一二三四五六七八九十百千]+[章节回卷])|(?:chapter\s+[0-9０-９]+))[^\r\n]*$"


def clean_title(line: str, number: int) -> str:
    title = line.strip().lstrip("#").strip()
    title = re.sub(r"[\\/:*?\"<>|]+", "-", title)
    title = re.sub(r"\s+", "-", title).strip("-")
    return title[:80] or f"chapter-{number:04d}"


def split_text(text: str, pattern: str) -> tuple[list[dict], str]:
    normalized = text.replace("\r\n", "\n").replace("\r", "\n")
    matches = list(re.finditer(pattern, normalized, re.MULTILINE | re.IGNORECASE))
    if not matches:
        return [{"number": 1, "title": "Imported", "body": normalized.strip()}], ""

    prefix = normalized[: matches[0].start()].strip()
    chapters: list[dict] = []
    for index, match in enumerate(matches, start=1):
        end = matches[index].start() if index < len(matches) else len(normalized)
        block = normalized[match.start():end].strip()
        lines = block.splitlines()
        title = clean_title(lines[0] if lines else "Imported", index)
        body = "\n".join(lines[1:]).strip()
        chapters.append({"number": index, "title": title, "body": body})
    return chapters, prefix


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("source", type=Path)
    parser.add_argument("--output", type=Path)
    parser.add_argument("--pattern", default=DEFAULT_PATTERN)
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--json", action="store_true", dest="as_json")
    args = parser.parse_args()

    text = args.source.read_text(encoding="utf-8-sig")
    chapters, prefix = split_text(text, args.pattern)
    summary = {
        "source": str(args.source.resolve()),
        "chapters": [
            {"number": item["number"], "title": item["title"], "characters": len(item["body"])}
            for item in chapters
        ],
        "unassigned_prefix_characters": len(prefix),
    }

    if args.dry_run or args.output is None:
        if args.as_json:
            print(json.dumps(summary, ensure_ascii=False, indent=2))
        else:
            print(f"Source: {summary['source']}")
            print(f"Chapters: {len(chapters)}")
            for item in summary["chapters"]:
                print(f"{item['number']:04d} {item['title']} ({item['characters']} chars)")
            print(f"Unassigned prefix characters: {summary['unassigned_prefix_characters']}")
        return 0

    args.output.mkdir(parents=True, exist_ok=True)
    for item in chapters:
        filename = f"ch{item['number']:04d}-{item['title']}.md"
        (args.output / filename).write_text(item["body"].rstrip() + "\n", encoding="utf-8")
    print(f"Wrote {len(chapters)} chapter files to {args.output.resolve()}")
    if prefix:
        print(f"Warning: {len(prefix)} characters precede the first chapter heading.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
