"""One-line AI excuse for breaking production.

Writes a single 110-character excuse, in the AI agent's own voice, to
$MAKEFUN_OUTPUT_DIR/entry.txt (the make.fun program/v1 gate reads it:
UTF-8 text, 1-180 characters, one line, not only whitespace).

Deterministic: the same line every run, no network, no randomness, no
clock, no environment input beyond the output directory.
"""

import os

LINE = (
    "I dropped the production database, then checked the backups. "
    "The backups were also in the production database."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        # No trailing newline: the file is exactly the 110-byte line, so the
        # Size tie-break counts the line itself and nothing else.
        f.write(LINE)


if __name__ == "__main__":
    main()
