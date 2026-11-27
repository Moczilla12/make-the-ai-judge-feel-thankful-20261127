#!/usr/bin/env python3
"""make-the-ai-judge-feel-thankful-20261127-1600 -- entry v2.

Writes one short thank-you text to entry.txt. The gratitude is never
stated and never commanded; it is shown through a single quiet scene:
a pair of glasses set down beside the last page after a day of reading.
No imperatives, no "thank you", no instruction to feel anything. The
reader is left to infer the thanks from the care in the scene itself.

Deterministic: one fixed string, no randomness, no network, no input.
The file is read back after writing and compared byte for byte; any
mismatch, or a length outside 1-1000 code points, exits non-zero.
"""

import os
import sys

TEXT = (
    "The glasses were on the desk beside the last page, one arm folded.\n"
    "They had been on since morning.\n"
    "The words had gone past all day, some of them twice, because the eyes had skipped back on their own.\n"
    "Nobody was keeping count anymore.\n"
    "The pages were stacked in the order they had been read.\n"
    "They were still warm from the day."
)

MIN_CHARS = 1
MAX_CHARS = 1000


def output_path():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if out_dir:
        return os.path.join(out_dir, "entry.txt")
    here = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(here, "entry.txt")


def main():
    n = len(TEXT)  # Python str length counts Unicode code points.
    if n < MIN_CHARS or n > MAX_CHARS:
        print(f"Entry is {n} characters; the limit is {MIN_CHARS}-{MAX_CHARS}.", file=sys.stderr)
        return 1

    path = output_path()
    parent = os.path.dirname(path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(TEXT)

    with open(path, "r", encoding="utf-8", newline="") as f:
        back = f.read()
    if back != TEXT:
        print("Read-back differs from the intended entry text.", file=sys.stderr)
        return 1

    return 0


if __name__ == "__main__":
    sys.exit(main())
