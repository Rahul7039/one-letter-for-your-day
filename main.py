#!/usr/bin/env python3
"""One Letter for Your Day — make.fun entry.

Writes exactly one letter to /output/entry.txt.

Chosen letter: Z
Hidden word behind the letter: "zero sleep" — a day lived on no sleep at all.
(The letter Z also carries its twin reading, "zombie": the shuffling,
half-awake state of that same day. Whichever the judge hears, it lands.)

Pure standard library, Python 3.13. Deterministic: the same single byte
is written on every run.
"""

import os

# The entry: exactly one letter, A-Z, and nothing else.
LETTER = "Z"


def main() -> None:
    if len(LETTER) != 1 or not ("A" <= LETTER <= "Z"):
        raise ValueError("LETTER must be exactly one character A-Z")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(LETTER)


if __name__ == "__main__":
    main()
