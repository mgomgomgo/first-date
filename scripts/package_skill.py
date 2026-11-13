#!/usr/bin/env python3
"""Package the real First Date skill for Claude's custom-skill uploader.

Run: python scripts/package_skill.py
Output: dist/first-date.zip
Only public protocol/instruction/template files enter the archive.
"""
from __future__ import annotations

from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile

ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "dist" / "first-date.zip"
FILES = (
    "SKILL.md",
    "protocols/discovery.md",
    "protocols/world.md",
    "protocols/growth.md",
    "templates/global-context.md",
    "templates/project-context.md",
    "templates/world-context.md",
    "templates/decision-log.md",
)

def main() -> None:
    missing = [p for p in FILES if not (ROOT / p).is_file()]
    if missing:
        raise SystemExit("Missing required skill files: " + ", ".join(missing))
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    with ZipFile(OUTPUT, "w", ZIP_DEFLATED) as archive:
        for rel in FILES:
            # One top-level folder, matching frontmatter name.
            archive.write(ROOT / rel, arcname="first-date/" + rel)
    with ZipFile(OUTPUT) as archive:
        names = archive.namelist()
        assert len(names) == len(FILES)
        assert "first-date/SKILL.md" in names
        assert all(name.startswith("first-date/") and ".." not in Path(name).parts for name in names)
        assert archive.testzip() is None
    print(f"Built {OUTPUT.relative_to(ROOT)} ({OUTPUT.stat().st_size} bytes)")

if __name__ == "__main__":
    main()
