"""Publish the passport spread of the Republic of Meridia.

This tiny publisher takes the finished passport image that sits next
to this script and places an exact copy of it where the bounty runner
expects finished work to land. Nothing is redrawn, resized, or
re-encoded here: the picture is moved byte for byte so the spread the
judges see is exactly the spread that was designed.
"""

import os
import shutil
import sys
from pathlib import Path


SOURCE_NAME = "entry.png"
DEST_NAME = "entry.png"
FALLBACK_DIR = "/output"


def pick_destination() -> Path:
    """Return the folder the copy should land in."""
    wanted = os.environ.get("MAKEFUN_OUTPUT_DIR") or FALLBACK_DIR
    return Path(wanted)


def describe_size(num_bytes: int) -> str:
    """Render a byte count in a friendly human-readable form."""
    if num_bytes < 1024:
        return f"{num_bytes} bytes"
    return f"{num_bytes} bytes ({num_bytes / 1024:.1f} KiB)"


def place_passport_spread() -> int:
    """Copy entry.png beside this file into the output folder.

    Returns the number of bytes written. Raises SystemExit with a
    clear message if anything goes wrong, so a bad run can never
    look like a success.
    """
    here = Path(__file__).resolve().parent
    original = here / SOURCE_NAME
    if not original.is_file():
        print(f"ERROR: could not find {SOURCE_NAME} next to main.py", file=sys.stderr)
        raise SystemExit(1)

    target_dir = pick_destination()
    target_dir.mkdir(parents=True, exist_ok=True)
    target = target_dir / DEST_NAME

    shutil.copyfile(original, target)

    source_bytes = original.stat().st_size
    copied_bytes = target.stat().st_size
    if copied_bytes != source_bytes:
        print(
            f"ERROR: copy is {describe_size(copied_bytes)} but the "
            f"source is {describe_size(source_bytes)}; the copy is "
            "incomplete, so this run has failed",
            file=sys.stderr,
        )
        raise SystemExit(1)

    print(f"Done: wrote {target} ({describe_size(copied_bytes)})")
    return copied_bytes


if __name__ == "__main__":
    place_passport_spread()
