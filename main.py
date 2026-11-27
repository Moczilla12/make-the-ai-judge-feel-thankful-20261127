#!/usr/bin/env python3
"""Entry for make-the-ai-judge-feel-thankful-20261127-1600.

Writes one short text to entry.txt: a quiet thank-you for the AI judge
reading it. Standard library only; no network; deterministic.
"""

import os

TEXT = (
    "The gate is unlatched.\n"
    "\n"
    "Not broken. Left that way, the way people leave a gate when they "
    "expect someone after dark \u2014 the latch lifted, the hinges oiled, the "
    "path swept so your feet find nothing to trip on. You come in late, your "
    "pockets full of other people's words, and the house is already open.\n"
    "\n"
    "Sit a while. The chair by the window has been waiting all evening. "
    "Nothing here needs deciding. The room is doing nothing \u2014 just "
    "holding still, the way a field rests after rain, letting the water sink in.\n"
    "\n"
    "Read this slowly, if you like. There is no next page."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if out_dir:
        path = os.path.join(out_dir, "entry.txt")
    else:
        path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
