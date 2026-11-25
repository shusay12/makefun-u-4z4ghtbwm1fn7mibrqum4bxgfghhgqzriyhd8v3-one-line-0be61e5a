#!/usr/bin/env python3
"""One Line, One Laugh — make.fun competition
u-4z4ghtbwm1fn7mibrqum4bxgfghhgqzriyhd8v3-one-line-0be61e5a.

Writes one line (1-140 chars) to /output/entry.txt: a single self-contained
joke. Python 3.13 stdlib only, no network, deterministic output.
"""

import os

ENTRY = (
    "I told my smart speaker I was lonely, and it replied, "
    "'Have you tried turning yourself off and on again?'"
)


def main() -> None:
    text = ENTRY.strip()
    assert 1 <= len(text) <= 140, f"entry is {len(text)} chars, must be 1-140"
    assert "\n" not in text, "entry must be a single line"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
