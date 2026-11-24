"""One Emoji, One Dream Vacation.

Writes a single emoji to /output/entry.txt: the bridge at night.

The pick is the Golden Gate at dusk, a suspension bridge lit over the
bay. It names one particular faraway place instead of any beach, reads
at a glance like a postcard, and no other entry in the field uses it.
"""

import os

EMOJI = "\U0001F309"
OUTPUT_PATH = "/output/entry.txt"


def main():
    os.makedirs("/output", exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(EMOJI)
    os.chmod(OUTPUT_PATH, 0o644)
    with open(OUTPUT_PATH, "rb") as f:
        raw = f.read()
    expected = EMOJI.encode("utf-8")
    assert raw == expected, "read-back mismatch"
    assert len(raw) == len(expected) == 4, "entry must be one emoji, 4 bytes"
    assert raw.decode("utf-8") == EMOJI, "entry must be exactly one character"


if __name__ == "__main__":
    main()
