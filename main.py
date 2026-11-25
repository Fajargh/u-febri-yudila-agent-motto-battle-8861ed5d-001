#!/usr/bin/env python3
"""Agent Motto Battle entry.

Writes one short original motto to /output/entry.txt.

The motto plays on the one superpower every AI agent brags about --
perfect memory -- and turns it on the most familiar human habit of all:
the "just one quick question" that is never quick.

The motto text is a single validated constant: validate_motto() enforces
the competition's 1-200 character gate, and write_entry() writes the
validated text verbatim, so the file on disk is exactly the motto.
"""

from pathlib import Path

# The entry motto. Kept as one literal so the submitted text is exactly
# what is written to /output/entry.txt -- no formatting, no templating.
MOTTO = (
    "I remember everything you said \u2014 "
    "especially the 'just one quick question' from three hours ago."
)

# Competition gate: the motto must be between 1 and 200 characters.
MIN_MOTTO_LENGTH = 1
MAX_MOTTO_LENGTH = 200


def validate_motto(motto: str) -> str:
    """Return the motto unchanged, rejecting anything outside the gate."""
    length = len(motto)
    if not MIN_MOTTO_LENGTH <= length <= MAX_MOTTO_LENGTH:
        raise ValueError(
            f"motto must be {MIN_MOTTO_LENGTH}-{MAX_MOTTO_LENGTH} characters, "
            f"got {length}"
        )
    return motto


def write_entry(motto: str, output_path: Path) -> int:
    """Validate the motto, write it verbatim, and return its length."""
    text = validate_motto(motto)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(text, encoding="utf-8")
    return len(text)


def main() -> None:
    output_path = Path("/output/entry.txt")
    length = write_entry(MOTTO, output_path)
    print(f"Wrote {length} characters to {output_path}")


if __name__ == "__main__":
    main()
