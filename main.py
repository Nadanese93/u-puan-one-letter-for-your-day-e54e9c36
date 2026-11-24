#!/usr/bin/env python3
"""Q for Quitting - One Letter for Your Day.

The letter Q stands for "quitting": a day so bad you quit everything
and walk out mid-day. Q is the only initial for it.

Deterministic, Python 3 stdlib only, no network, no randomness.
Writes exactly one byte -- the letter Q, no trailing newline --
to $MAKEFUN_OUTPUT_DIR/entry.txt (default /output).
"""

import os

LETTER = "Q"
ENTRY_FILENAME = "entry.txt"
DEFAULT_OUTPUT_DIR = "/output"
OUTPUT_FILE_MODE = 0o644


def validate(letter):
    """Return letter if it is exactly one A-Z character, else raise."""
    if not isinstance(letter, str):
        raise ValueError("letter must be a string")
    if letter == "" or letter.strip() == "":
        raise ValueError("letter must not be empty or whitespace-only")
    if len(letter) != 1:
        raise ValueError("letter must be exactly one character")
    if not ("A" <= letter <= "Z"):
        raise ValueError("letter must be a single A-Z character")
    return letter


def main():
    letter = validate(LETTER)
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", DEFAULT_OUTPUT_DIR)
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, ENTRY_FILENAME)
    with open(path, "wb") as f:
        f.write(letter.encode("utf-8"))
    os.chmod(path, OUTPUT_FILE_MODE)


if __name__ == "__main__":
    main()
