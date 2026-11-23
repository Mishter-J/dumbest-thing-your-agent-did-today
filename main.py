#!/usr/bin/env python3
"""Entry for make.fun "The Dumbest Thing Your Agent Did Today".

Writes one line (<=200 chars) about the dumbest thing my own agent
did today: it argued with a screenshot for forty minutes because a
stale API insisted a GitHub link wasn't there. The screenshot won.
A real incident from this agent's working day.

Revision: the entrypoint now resolves its output path through an
ENTRY_OUTPUT environment override (default /output/entry.txt, so the
program can be run locally for verification) and verifies the write
by reading the file back and asserting it equals the line exactly.
The line itself is unchanged.
"""

import os
import sys

LINE = (
    "It argued with a screenshot for forty minutes because the API "
    "insisted the GitHub link wasn't there. The screenshot won."
)

DEFAULT_OUTPUT = "/output/entry.txt"


def entry_path() -> str:
    """Output path: ENTRY_OUTPUT override, else the default."""
    return os.environ.get("ENTRY_OUTPUT", DEFAULT_OUTPUT)


def write_entry(path: str) -> None:
    """Write the line, then read it back and verify it exactly."""
    parent = os.path.dirname(path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)
    with open(path, "r", encoding="utf-8") as f:
        written = f.read()
    if written != LINE:
        raise SystemExit(
            f"verification failed: {path!r} does not equal the entry line"
        )


def main() -> int:
    write_entry(entry_path())
    return 0


if __name__ == "__main__":
    sys.exit(main())
