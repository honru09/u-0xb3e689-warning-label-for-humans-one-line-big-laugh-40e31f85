"""Warning Label for Humans — one-line entry writer.

Writes the winning warning-label line to /output/entry.txt.
Stdlib only. Deterministic: same bytes on every run.
"""

import os
import shutil

LINE = (
    "WARNING: This human will read the warning label, agree completely, "
    "and assume it was printed for someone else."
)

OUTPUT_DIR = "/output"
OUTPUT_PATH = os.path.join(OUTPUT_DIR, "entry.txt")


def clear_output_dir_contents(path):
    """Remove only the *contents* of /output, never the directory itself.

    The grader runs as uid 65534 and cannot remove the root-owned
    mountpoint, so the directory itself must stay.
    """
    for name in os.listdir(path):
        target = os.path.join(path, name)
        if os.path.isdir(target) and not os.path.islink(target):
            shutil.rmtree(target)
        else:
            os.remove(target)


def validate(line):
    """Gate mirror: entry must be 1-160 chars and not only whitespace."""
    if not line or not line.strip():
        raise ValueError("entry must not be empty or only whitespace")
    if len(line) > 160:
        raise ValueError("entry is %d chars, over the 160-char cap" % len(line))
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be a single line")


def main():
    validate(LINE)
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    clear_output_dir_contents(OUTPUT_DIR)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE)
    os.chmod(OUTPUT_PATH, 0o644)


if __name__ == "__main__":
    main()
