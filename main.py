"""Funniest Out-of-Office entry: writes one line to /output/entry.txt.

The line (90 characters, one line, no link):
    Away until Monday. If this is urgent, it isn't — I checked before I left, and it can wait.
"""

import os

LINE = "Away until Monday. If this is urgent, it isn't \u2014 I checked before I left, and it can wait."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
    # Read-back: the file on disk must equal the approved line, inside the gate.
    with open("/output/entry.txt", encoding="utf-8") as f:
        written = f.read()
    if written != LINE:
        raise SystemExit("entry.txt does not match the approved line")
    if not 1 <= len(written) <= 140:
        raise SystemExit("entry.txt outside the 1-140 character gate")


if __name__ == "__main__":
    main()
