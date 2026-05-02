#!/usr/bin/env python3
"""Audit the Home Assistant Codex workspace structure.

This script checks repository hygiene only. It does not connect to Home Assistant,
read credentials, call ha-mcp, or modify files.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

REQUIRED_PATHS = [
    "AGENTS.md",
    "README.md",
    "USER.md",
    "MEMORY.md",
    "SOUL.md",
    "skills-lock.json",
    ".codexignore",
    ".gitignore",
    ".agents/skills/home-assistant-best-practices/SKILL.md",
    ".agents/skills/home-assistant-dashboard-designer/SKILL.md",
    ".agents/skills/ha-mcp-workflow-tools/SKILL.md",
    "home-assistant/AGENTS.md",
    "esphome/AGENTS.md",
]

RECOMMENDED_DIRS = [
    ".codex/prompts",
    ".codex/agents",
    "docs",
    "tools",
    "home-assistant/automations/exports",
    "home-assistant/helpers/exports",
    "home-assistant/scripts/exports",
    "home-assistant/dashboards/plans",
    "home-assistant/packages",
    "esphome/devices",
    "esphome/packages",
    "esphome/common",
]

SENSITIVE_PATTERNS = [
    "secrets.yaml",
    ".storage/",
    "home-assistant_v2.db",
    ".google.token",
    "known_devices.yaml",
]


def rel(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def check_required_paths() -> list[str]:
    findings: list[str] = []
    for item in REQUIRED_PATHS:
        path = ROOT / item
        if not path.exists():
            findings.append(f"MISSING required path: {item}")
    for item in RECOMMENDED_DIRS:
        path = ROOT / item
        if not path.exists():
            findings.append(f"MISSING recommended directory: {item}")
    return findings


def check_skills_lock() -> list[str]:
    findings: list[str] = []
    lock_path = ROOT / "skills-lock.json"
    if not lock_path.exists():
        return ["Cannot validate skills-lock.json because it is missing"]

    try:
        data = json.loads(lock_path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        return [f"skills-lock.json is not valid JSON: {exc}"]

    skills = data.get("skills", {})
    if not isinstance(skills, dict):
        return ["skills-lock.json: 'skills' must be an object"]

    for name, meta in skills.items():
        if not isinstance(meta, dict):
            findings.append(f"Skill {name!r} metadata must be an object")
            continue
        skill_path = meta.get("path")
        enabled = meta.get("enabled")
        if not skill_path:
            findings.append(f"Skill {name!r} is missing path")
            continue
        if enabled is not True:
            findings.append(f"Skill {name!r} is not enabled")
        path = ROOT / skill_path
        if not path.exists():
            findings.append(f"Skill {name!r} path does not exist: {skill_path}")
        elif not (path / "SKILL.md").exists():
            findings.append(f"Skill {name!r} is missing SKILL.md at {skill_path}")
    return findings


def check_ignore_files() -> list[str]:
    findings: list[str] = []
    for ignore_name in [".gitignore", ".codexignore"]:
        path = ROOT / ignore_name
        if not path.exists():
            continue
        text = path.read_text(encoding="utf-8", errors="replace")
        for pattern in SENSITIVE_PATTERNS:
            if pattern not in text:
                findings.append(f"{ignore_name} should ignore {pattern}")
    return findings


def check_sensitive_files_present() -> list[str]:
    findings: list[str] = []
    for path in ROOT.rglob("*"):
        if not path.is_file():
            continue
        relative = rel(path)
        lowered = relative.lower()
        if ".git/" in lowered:
            continue
        for pattern in SENSITIVE_PATTERNS:
            if pattern.lower().strip("/") in lowered:
                findings.append(f"Sensitive/noisy file appears present: {relative}")
    return findings


def main() -> int:
    findings: list[str] = []
    findings.extend(check_required_paths())
    findings.extend(check_skills_lock())
    findings.extend(check_ignore_files())
    findings.extend(check_sensitive_files_present())

    if findings:
        print("Workspace audit findings:")
        for item in findings:
            print(f"- {item}")
        return 1

    print("Workspace audit passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
