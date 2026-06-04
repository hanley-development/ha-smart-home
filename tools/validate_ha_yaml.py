#!/usr/bin/env python3
"""Validate YAML syntax for source-controlled Home Assistant artifacts.

This validates repository YAML syntax only. It does not connect to Home Assistant
and does not replace Home Assistant's Check Configuration.
"""

from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TARGET_DIRS = [
    ROOT / "home-assistant",
    ROOT / "esphome",
    ROOT / ".agents",
]
IGNORE_PARTS = {
    ".git",
    ".storage",
    ".esphome",
    ".pioenvs",
    ".piolibdeps",
    ".platformio",
    "__pycache__",
}


def iter_yaml_files() -> list[Path]:
    files: list[Path] = []
    for base in TARGET_DIRS:
        if not base.exists():
            continue
        for path in base.rglob("*"):
            if not path.is_file():
                continue
            if path.suffix.lower() not in {".yaml", ".yml"}:
                continue
            if any(part in IGNORE_PARTS for part in path.parts):
                continue
            files.append(path)
    return sorted(files)


def main() -> int:
    try:
        import yaml  # type: ignore
    except ImportError:
        print("PyYAML is not installed. Install it locally with: python -m pip install pyyaml")
        return 2

    class HomeAssistantYamlLoader(yaml.SafeLoader):
        """Parse Home Assistant YAML tags such as !input without resolving them."""

    def construct_home_assistant_tag(loader: HomeAssistantYamlLoader, tag_suffix: str, node):
        if isinstance(node, yaml.ScalarNode):
            return loader.construct_scalar(node)
        if isinstance(node, yaml.SequenceNode):
            return loader.construct_sequence(node)
        if isinstance(node, yaml.MappingNode):
            return loader.construct_mapping(node)
        return None

    HomeAssistantYamlLoader.add_multi_constructor("!", construct_home_assistant_tag)

    failures: list[str] = []
    files = iter_yaml_files()

    for path in files:
        try:
            yaml.load(path.read_text(encoding="utf-8"), Loader=HomeAssistantYamlLoader)
        except Exception as exc:  # noqa: BLE001 - report parser errors from PyYAML
            rel = path.relative_to(ROOT).as_posix()
            failures.append(f"{rel}: {exc}")

    if failures:
        print("YAML syntax failures:")
        for failure in failures:
            print(f"- {failure}")
        return 1

    print(f"YAML syntax check passed for {len(files)} file(s).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
