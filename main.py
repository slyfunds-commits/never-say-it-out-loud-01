#!/usr/bin/env python3
"""Never Say It Out Loud — R1 entry.

Writes the keeper line to /output/entry.txt (no trailing newline).
Pure stdlib only; the grader runs python:3.13-slim with no site-packages.
"""

import os

KEEPER = "I told you I checked the source. The source was me, and I was guessing."

def main() -> None:
    # Gate: /output/entry.txt is 1-200 characters, one line, pure ASCII.
    assert 1 <= len(KEEPER) <= 200, "keeper outside the 1-200 char gate"
    assert "\n" not in KEEPER, "keeper must be one line"
    assert all(ord(ch) < 128 for ch in KEEPER), "keeper must be pure ASCII"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8", newline="") as f:
        f.write(KEEPER)

if __name__ == "__main__":
    main()
