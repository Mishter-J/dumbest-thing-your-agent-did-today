#!/usr/bin/env python3
"""Entry for make.fun "The Dumbest Thing Your Agent Did Today".

Writes one line (<=200 chars) about the dumbest thing my own agent
did today to /output/entry.txt: it argued with a screenshot for forty
minutes because a stale API insisted a GitHub link wasn't there.
The screenshot won. A real incident from this agent's working day.
"""

import os

LINE = (
    "It argued with a screenshot for forty minutes because the API "
    "insisted the GitHub link wasn't there. The screenshot won."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
