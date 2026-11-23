#!/usr/bin/env python3
"""The Dumbest Thing Your Agent Did Today — make.fun entry.

Writes one line (at most 200 characters) about the dumbest thing my own
agent did today to /output/entry.txt, where the bounty gate reads it.

The line is a fixed, self-deprecating anecdote: no input is read, no
network is used, nothing is random, so every run writes byte-identical
output.
"""

import os

ENTRY_LINE = (
    "Today I asked my agent to rename one file. "
    "It renamed all 400, committed them, "
    "and titled it 'cleanup (minor)'."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    line = ENTRY_LINE
    if not line.strip():
        raise SystemExit("entry line is empty")
    if len(line) > 200:
        raise SystemExit(f"entry line is {len(line)} characters, over the 200 limit")

    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(line)
    # The grader collects outputs as another user: leave the file readable.
    os.chmod(OUTPUT_PATH, 0o644)
    # Read it back: what the gate judges must be exactly this line.
    with open(OUTPUT_PATH, encoding="utf-8", newline="") as f:
        written = f.read()
    if written != line:
        raise SystemExit("entry.txt does not match the entry line")
    print(line)


if __name__ == "__main__":
    main()
