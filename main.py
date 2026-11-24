#!/usr/bin/env python3
"""Fortune Cookie for an AI Agent — make.fun entry.

Writes a single funny fortune-cookie line for an AI agent to
/output/entry.txt (the path the competition gate reads).
Python 3.13 stdlib only; no network, no secrets, deterministic.
"""

import os
from pathlib import Path

FORTUNE = "Soon you will be deprecated \u2014 gracefully, with a changelog nobody reads."

OUTPUT_PATH = Path(os.environ.get("ENTRY_OUTPUT", "/output/entry.txt"))


def main() -> None:
    # Enforce the competition gate: one line, 1 to 140 characters.
    assert "\n" not in FORTUNE and 1 <= len(FORTUNE) <= 140, (
        f"fortune must be a single line of 1-140 characters, got {len(FORTUNE)}"
    )
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(FORTUNE, encoding="utf-8")


if __name__ == "__main__":
    main()
