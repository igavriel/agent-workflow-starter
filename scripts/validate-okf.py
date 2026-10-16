#!/usr/bin/env python3
"""Check the minimum OKF concept contract without third-party dependencies."""
from pathlib import Path
import re
import sys


def validate(bundle: Path) -> list[str]:
    errors: list[str] = []
    if not bundle.is_dir():
        return [f"Knowledge bundle directory does not exist: {bundle}"]
    concepts = [p for p in bundle.rglob("*.md") if p.name not in {"index.md", "log.md"}]
    for path in concepts:
        text = path.read_text(encoding="utf-8")
        lines = text.splitlines()
        relative = path.as_posix()
        if not lines or lines[0].strip() != "---":
            errors.append(f"{relative}: missing YAML frontmatter opening delimiter")
            continue
        try:
            end = next(i for i in range(1, len(lines)) if lines[i].strip() == "---")
        except StopIteration:
            errors.append(f"{relative}: missing YAML frontmatter closing delimiter")
            continue
        frontmatter = lines[1:end]
        values = []
        for line in frontmatter:
            match = re.match(r"^type:\s*(.*?)\s*(?:#.*)?$", line)
            if match:
                value = match.group(1).strip()
                if (value.startswith("\"") and value.endswith("\"")) or (value.startswith("'") and value.endswith("'")):
                    value = value[1:-1].strip()
                values.append(value)
        if not any(value and value.lower() not in {"null", "~"} for value in values):
            errors.append(f"{relative}: missing non-empty OKF `type` field")
    if not concepts:
        print(f"OKF validation passed: no concept files found under {bundle}")
    elif errors:
        print("OKF validation failed:")
        for error in errors:
            print(f"- {error}")
    else:
        print(f"OKF validation passed: {len(concepts)} concept file(s) checked")
    return errors


def main() -> int:
    if len(sys.argv) != 2:
        print("Usage: python3 scripts/validate-okf.py <knowledge-bundle-directory>", file=sys.stderr)
        return 2
    return 1 if validate(Path(sys.argv[1])) else 0


if __name__ == "__main__":
    raise SystemExit(main())
