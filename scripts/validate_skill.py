#!/usr/bin/env python3
"""Deterministic offline checks for the First Date skill and Claude ZIP.

This validates packaging, required protocol topics and references, not model
behavior or provider-specific persistence. Run from any working directory.
"""
from __future__ import annotations

import re
from pathlib import Path
from zipfile import ZipFile

ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "SKILL.md"
DISCOVERY = ROOT / "protocols/discovery.md"
WORLD = ROOT / "protocols/world.md"
GROWTH = ROOT / "protocols/growth.md"
ZIP = ROOT / "dist/first-date.zip"

def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)

def main() -> None:
    skill = SKILL.read_text(encoding="utf-8")
    require(skill.startswith("---\n"), "SKILL.md must start with YAML frontmatter")
    end = skill.find("\n---\n", 4)
    require(end > 0, "SKILL.md must close its frontmatter")
    meta = skill[4:end]
    name = re.search(r"^name:\s*([a-z0-9-]+)\s*$", meta, re.M)
    description = re.search(r'^description:\s*["\']?(.+?)["\']?\s*$', meta, re.M)
    require(bool(name) and name.group(1) == "first-date", "name must be first-date")
    require(bool(description), "description is required")
    require(len(description.group(1)) <= 200, "description exceeds Claude skill metadata limit")
    require("protocols/discovery.md" in skill, "Stage 1 routing is missing")
    require("protocols/world.md" in skill, "Stage 2 routing is missing")
    require("protocols/growth.md" in skill, "Stage 3 routing is missing")

    discovery = DISCOVERY.read_text(encoding="utf-8")
    world = WORLD.read_text(encoding="utf-8")
    growth = GROWTH.read_text(encoding="utf-8")
    require(len(re.findall(r"^### Domain \d+ ", discovery, re.M)) == 10, "Expected 10 specific discovery domains")
    require(len(re.findall(r"^### W\d+\.", world, re.M)) == 7, "Expected 7 optional world domains")
    for file, content in [(DISCOVERY, discovery), (WORLD, world)]:
        require(content.count("**Anchor:**") >= (10 if file == DISCOVERY else 7),
                f"Missing anchor questions in {file.name}")
    for topic in ["consent", "correction", "decision", "calibration"]:
        require(topic in growth.lower(), f"Missing learning-loop topic: {topic}")
    for rel in [
        "templates/global-context.md",
        "templates/project-context.md",
        "templates/world-context.md",
        "templates/decision-log.md",
    ]:
        require((ROOT / rel).is_file(), f"Missing context template: {rel}")

    require(ZIP.is_file(), "Run scripts/package_skill.py first")
    with ZipFile(ZIP) as z:
        names = set(z.namelist())
        require("first-date/SKILL.md" in names, "ZIP must have first-date/SKILL.md")
        require(len(names) == 8, "Unexpected/missing packaged files")
        require(all(n.startswith("first-date/") for n in names), "ZIP has incorrect root")
        require(all(not Path(n).is_absolute() and ".." not in Path(n).parts for n in names),
                "ZIP has unsafe paths")
        require(z.testzip() is None, "ZIP integrity failure")
        for name in names:
            original = ROOT / name.removeprefix("first-date/")
            require(z.read(name) == original.read_bytes(), f"ZIP stale: {name}")
    print("PASS: skill metadata, stage routing, discovery coverage, templates and ZIP integrity")
    print("NOTE: real model behavior, automatic invocation, and provider storage are NOT tested.")

if __name__ == "__main__":
    main()
