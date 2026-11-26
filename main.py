"""Roast the Smart Fridge: one line, best laugh wins.

Writes a single roast line (at most 160 characters) to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt).
Python 3.13, standard library only, deterministic, no network.
"""

import os

LINE = (
    "My smart fridge has Wi-Fi, a camera, a touchscreen, yet it can't "
    "tell me what's inside \u2014 a $3,000 snitch reporting my 2 a.m. "
    "snacking to an app I never open."
)


def validate(line: str) -> None:
    """Gate: entry must be UTF-8 text of 1 to 160 characters, not only whitespace."""
    if not isinstance(line, str):
        raise ValueError("entry must be text")
    if not line.strip():
        raise ValueError("entry must not be only whitespace")
    if not 1 <= len(line) <= 160:
        raise ValueError(f"entry must be 1-160 characters, got {len(line)}")
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be a single line")
    line.encode("utf-8")  # must be valid UTF-8


def main() -> None:
    validate(LINE)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
