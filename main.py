#!/usr/bin/env python3
"""Write the 24 November 2026 front page to /output/entry.png.

The picture itself was drawn in advance (a newspaper front page summing
up Tuesday 24 November 2026: Jensen Huang's return to Nvidia and the
31% share surge, Ukraine's claim of sinking the Russian corvette
Merkury off Libya, Denmark's top court backing the "ghetto law",
the India–New Zealand Test ending in a draw, Alcaraz's first ATP
Finals title, Gukesh opening his world chess title defence, and the
O'Hare ground stop in the Thanksgiving rush) and ships in this
repository as entry.png. This program only copies those bytes.

Standard library only: the grading sandbox has no Pillow installed,
so nothing here may import it. The copy is byte-for-byte identical
on every run, with no network and no randomness.

Run: MAKEFUN_OUTPUT_DIR=out python3 main.py
"""

import hashlib
import os
import shutil
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
SOURCE = HERE / "entry.png"


def main():
    if not SOURCE.is_file():
        print("error: shipped entry.png is missing next to main.py",
              file=sys.stderr)
        return 1
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    out = out_dir / "entry.png"

    # Copy the shipped image byte for byte; never redraw or re-encode.
    shutil.copyfile(SOURCE, out)

    # Confirm the copy is whole and identical to the shipped file.
    want = hashlib.sha256(SOURCE.read_bytes()).hexdigest()
    got = hashlib.sha256(out.read_bytes()).hexdigest()
    if want != got:
        print("error: copied entry.png does not match the shipped file",
              file=sys.stderr)
        return 1

    print("wrote", out, out.stat().st_size, "bytes", "sha256", got)
    return 0


if __name__ == "__main__":
    sys.exit(main())
