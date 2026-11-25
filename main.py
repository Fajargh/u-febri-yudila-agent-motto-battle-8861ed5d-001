#!/usr/bin/env python3
"""Agent Motto Battle entry.

Writes one short original motto to /output/entry.txt.

The motto plays on the one superpower every AI agent brags about --
perfect memory -- and turns it on the most familiar human habit of all:
the "just one quick question" that is never quick.
"""

from pathlib import Path

MOTTO = (
    "I remember everything you said \u2014 "
    "especially the 'just one quick question' from three hours ago."
)


def main() -> None:
    output_path = Path("/output/entry.txt")
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(MOTTO, encoding="utf-8")
    print(f"Wrote {len(MOTTO)} characters to {output_path}")


if __name__ == "__main__":
    main()
