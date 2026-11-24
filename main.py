#!/usr/bin/env python3
"""One sentence explaining the modern internet to a traveler from 1800.

Writes the sentence to /output/entry.txt (UTF-8, one sentence, 136 chars).
Every word in it was in use before 1800: a post office, a letter, a pen.
The picture is one a person from 1800 could hold in their head -- a letter
that reaches any door on earth in a breath, and whose reply is already in
your hand before you set down your pen.
"""

import os
from pathlib import Path

SENTENCE = (
    "It is a post office where your letter reaches any door on earth in a "
    "breath, and the reply is in your hand before you set down your pen."
)

# Words coined after 1800, which the brief forbids; the sentence must use
# none of them. Checked as whole words so "pen" never trips "open", etc.
ANACHRONISMS = (
    "computer", "website", "online", "internet", "screen", "digital",
    "software", "email", "phone", "television", "radio", "video",
    "keyboard", "mouse", "server", "browser", "app", "data",
)


def main() -> None:
    out = Path(os.environ.get("OUTPUT_PATH", "/output/entry.txt"))
    out.parent.mkdir(parents=True, exist_ok=True)
    text = SENTENCE.strip()
    assert 1 <= len(text) <= 200, f"entry is {len(text)} chars, must be 1-200"
    assert text.count(".") == 1, "entry must be a single sentence"
    words = {w.strip(".,;:!?").lower() for w in text.split()}
    bad = sorted(set(ANACHRONISMS) & words)
    assert not bad, f"sentence uses post-1800 words: {bad}"
    out.write_text(text, encoding="utf-8")
    print(f"wrote {len(text)} chars to {out}")


if __name__ == "__main__":
    main()
