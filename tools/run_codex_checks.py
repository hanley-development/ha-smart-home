#!/usr/bin/env python3
"""Run local Codex workspace checks for this Home Assistant repo.

This script is repo-local only. It does not connect to Home Assistant, call
ha-mcp, read credentials, manage add-ons, reload Home Assistant, or control
devices.
"""

from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PYTHON = sys.executable


def run_step(name: str, command: list[str], *, required: bool = True) -> int:
    print(f"\n==> {name}")
    print("$ " + " ".join(command))
    completed = subprocess.run(command, cwd=ROOT, check=False)
    if completed.returncode != 0:
        level = "FAILED" if required else "SKIPPED/FAILED"
        print(f"{level}: {name} returned {completed.returncode}")
    return completed.returncode


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Run safe local Codex/Home Assistant workspace checks."
    )
    parser.add_argument(
        "--skip-yaml",
        action="store_true",
        help="Skip repository YAML syntax validation.",
    )
    parser.add_argument(
        "--skip-index",
        action="store_true",
        help="Skip rebuilding home-assistant/EXPORT_INDEX.md.",
    )
    args = parser.parse_args()

    failures: list[str] = []

    audit_code = run_step(
        "Workspace structure audit",
        [PYTHON, "tools/ha_workspace_audit.py"],
    )
    if audit_code != 0:
        failures.append("Workspace structure audit")

    if not args.skip_yaml:
        yaml_code = run_step(
            "YAML syntax validation",
            [PYTHON, "tools/validate_ha_yaml.py"],
        )
        if yaml_code != 0:
            failures.append("YAML syntax validation")

    if not args.skip_index:
        index_code = run_step(
            "Build Home Assistant export index",
            [PYTHON, "tools/build_export_index.py"],
        )
        if index_code != 0:
            failures.append("Build Home Assistant export index")

    if failures:
        print("\nCodex workspace checks completed with failures:")
        for failure in failures:
            print(f"- {failure}")
        return 1

    print("\nCodex workspace checks passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
