#!/usr/bin/env python3
"""One Line, One Laugh: Roast Your Fridge — entrypoint.

Writes a single roast line to $MAKEFUN_OUTPUT_DIR/entry.txt.
Pure standard library; deterministic output.
"""

import os
from pathlib import Path

ENTRY = "My fridge's ice maker produces one cube a day, like it's rationing water for a drought it invented."
# 99 characters, within the 1-200 gate; single line, no trailing newline.


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(ENTRY, encoding="utf-8")


if __name__ == "__main__":
    main()
