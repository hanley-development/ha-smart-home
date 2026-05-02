#!/usr/bin/env python3
"""Build a Markdown index of Home Assistant exports and dashboard plans.

This script scans repository export folders only. It does not connect to Home Assistant.
"""

from __future__ import annotations

from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "home-assistant" / "EXPORT_INDEX.md"
SECTIONS = [
    ("Automation exports", ROOT / "home-assistant" / "automations" / "exports"),
    ("Helper exports", ROOT / "home-assistant" / "helpers" / "exports"),
    ("Script exports", ROOT / "home-assistant" / "scripts" / "exports"),
    ("Dashboard plans", ROOT / "home-assistant" / "dashboards" / "plans"),
    ("Packages", ROOT / "home-assistant" / "packages"),
]


def describe_file(path: Path) -> str:
    stat = path.stat()
    size = stat.st_size
    modified = datetime.fromtimestamp(stat.st_mtime, timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    rel = path.relative_to(ROOT).as_posix()
    return f"- `{rel}` — {size} bytes — modified {modified}"


def main() -> int:
    lines: list[str] = [
        "# Home Assistant Export Index",
        "",
        "Generated from repository files only. This is not live Home Assistant state.",
        "",
    ]

    for title, directory in SECTIONS:
        lines.extend([f"## {title}", ""])
        if not directory.exists():
            lines.extend(["Directory missing.", ""])
            continue
        files = sorted(path for path in directory.rglob("*") if path.is_file())
        if not files:
            lines.extend(["No files yet.", ""])
            continue
        lines.extend(describe_file(path) for path in files)
        lines.append("")

    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text("\n".join(lines), encoding="utf-8", newline="\n")
    print(f"Wrote {OUTPUT.relative_to(ROOT).as_posix()}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
