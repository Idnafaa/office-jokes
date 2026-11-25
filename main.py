#!/usr/bin/env python3
"""One-Line Office Jokes — single-line office joke writer.

Writes one original office joke (1-199 chars, one line) to /output/entry.txt.
"""
import os

JOKE = "Our printer only jams on documents marked urgent, which makes it the only colleague who actually reads my deadlines."

def main():
    # Keep exactly one line: no trailing newline, no extra whitespace.
    # Normalise any accidental double spaces so the line reads clean.
    text = " ".join(JOKE.strip().split())
    assert 1 <= len(text) <= 199, f"joke is {len(text)} chars"
    assert "\n" not in text, "joke must be a single line"
    outdir = "/output"
    os.makedirs(outdir, exist_ok=True)
    with open(os.path.join(outdir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)
    print(f"wrote {len(text)} chars to {outdir}/entry.txt")

if __name__ == "__main__":
    main()
