#!/usr/bin/env python3
"""Run conservative structural checks for a file-backed novel project."""

from __future__ import annotations

import argparse
import json
from pathlib import Path


REQUIRED = (
    "CREATOR.md",
    "setting/outline.md",
    "setting/progress.md",
    "setting/character-states.md",
    "chapters",
)


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8-sig")


def inspect(root: Path, strict: bool) -> dict:
    issues: list[dict] = []
    warnings: list[dict] = []
    present: list[str] = []
    chapters: list[dict] = []

    if not root.is_dir():
        return {"root": str(root), "issues": [{"path": str(root), "message": "project root is not a directory"}], "warnings": [], "chapters": []}

    for relative in REQUIRED:
        path = root / relative
        if path.exists():
            present.append(relative)
        elif strict:
            issues.append({"path": relative, "message": "required project item is missing"})
        else:
            warnings.append({"path": relative, "message": "recommended project item is missing"})

    chapter_dir = root / "chapters"
    if chapter_dir.is_dir():
        candidates = sorted(
            p for p in chapter_dir.rglob("*")
            if p.is_file() and p.suffix.lower() in {".md", ".markdown", ".txt"}
        )
        for path in candidates:
            relative = path.relative_to(root).as_posix()
            try:
                text = read_text(path)
            except UnicodeDecodeError:
                issues.append({"path": relative, "message": "file is not valid UTF-8"})
                continue
            except OSError as exc:
                issues.append({"path": relative, "message": f"file could not be read: {exc}"})
                continue
            if not text.strip():
                issues.append({"path": relative, "message": "chapter file is empty"})
            if "\ufffd" in text:
                issues.append({"path": relative, "message": "replacement character found"})
            chapters.append({"path": relative, "characters": len(text), "empty": not bool(text.strip())})
        if not candidates:
            warnings.append({"path": "chapters", "message": "no Markdown or TXT chapter files found"})

    return {
        "root": str(root),
        "present": present,
        "chapters": chapters,
        "issues": issues,
        "warnings": warnings,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("root", nargs="?", default=".", help="novel project root")
    parser.add_argument("--strict", action="store_true", help="treat missing recommended structure as errors")
    parser.add_argument("--json", action="store_true", dest="as_json", help="print JSON instead of a human report")
    args = parser.parse_args()

    result = inspect(Path(args.root).resolve(), args.strict)
    if args.as_json:
        print(json.dumps(result, ensure_ascii=False, indent=2))
    else:
        print(f"Project: {result['root']}")
        print(f"Chapters: {len(result['chapters'])}")
        for item in result["issues"]:
            print(f"ISSUE {item['path']}: {item['message']}")
        for item in result["warnings"]:
            print(f"WARN  {item['path']}: {item['message']}")
        if not result["issues"]:
            print("Result: PASS")
    return 1 if result["issues"] else 0


if __name__ == "__main__":
    raise SystemExit(main())
