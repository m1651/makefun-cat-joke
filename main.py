#!/usr/bin/env python3
"""One-line cat joke entry for make.fun.

Writes a single original cat joke to /output/entry.txt.
"""

import os

JOKE = "My cat isn't ignoring me \u2014 he's running a 16-hour-a-day sleep startup, and I'm just the unpaid intern."


def main():
    line = JOKE.strip()
    if not line:
        raise SystemExit("error: joke line is blank")
    if "\n" in line or "\r" in line:
        raise SystemExit("error: joke must be a single line")
    if not 1 <= len(line) <= 200:
        raise SystemExit(f"error: joke line is {len(line)} chars, must be 1-200")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(line + "\n")


if __name__ == "__main__":
    main()
