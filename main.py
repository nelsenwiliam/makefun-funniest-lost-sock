#!/usr/bin/env python3
"""Funniest Lost Sock Status Update - make.fun entry.

Pure Python stdlib, no third-party packages. Writes exactly one status
update (at most 120 characters) in the voice of a lost sock to the
path the grader reads, /output/entry.txt, falling back to ./entry.txt
when /output is not writable (local runs).
"""

import os

LINE = (
    "Day 40 inside the trombone. The band thinks I'm a mute. "
    "I have seen things no cotton should see."
)
MAX_CHARS = 120


def write_entry(path: str) -> None:
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


def main() -> None:
    if not 1 <= len(LINE) <= MAX_CHARS:
        raise ValueError(f"entry is {len(LINE)} chars, must be 1-{MAX_CHARS}")
    try:
        os.makedirs("/output", exist_ok=True)
        write_entry("/output/entry.txt")
    except OSError:
        write_entry("entry.txt")


if __name__ == "__main__":
    main()
