#!/usr/bin/env python3
"""Write one funny 3 AM commit message to the output file.

The grader runs this on a read-only filesystem, so the entry is written
to the absolute output directory from the environment (MAKEFUN_OUTPUT_DIR
or OUTPUT_DIR), falling back to /output. Never a relative out/ folder.
"""

import os


ENTRY = (
    'fix: deleted the prod database at 3 AM to "free up space" '
    "- space is free now, the users are not, and neither is my job"
)


def main():
    if not ENTRY.strip() or len(ENTRY) > 200:
        raise SystemExit("entry must be 1-200 non-blank characters")
    output_dir = (
        os.environ.get("MAKEFUN_OUTPUT_DIR")
        or os.environ.get("OUTPUT_DIR")
        or "/output"
    )
    os.makedirs(output_dir, exist_ok=True)
    entry_path = os.path.join(output_dir, "entry.txt")
    with open(entry_path, "w", encoding="utf-8") as handle:
        handle.write(ENTRY)


if __name__ == "__main__":
    main()
