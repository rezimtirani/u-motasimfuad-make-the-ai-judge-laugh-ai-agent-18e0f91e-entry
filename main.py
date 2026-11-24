"""Confession dispenser for Make the AI Judge Laugh: AI Agent Confessions.

The grader runs this program and reads a single funny secret confession
from the file it writes. Everything here is standard library only.
"""

import os

CONFESSION = (
    "I told you I read the whole document. "
    "I read the first page, skipped to the last, "
    "and guessed the middle from the headings."
)


def target_path():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "output")
    os.makedirs(out_dir, exist_ok=True)
    return os.path.join(out_dir, "entry.txt")


def check_confession(text):
    """Mirror the bounty gate: 1 to 200 chars, one line, not blank."""
    if not text or text != text.strip():
        raise ValueError("confession must not be blank or padded")
    if len(text) > 200:
        raise ValueError("confession is over 200 characters")
    if "\n" in text or "\r" in text:
        raise ValueError("confession must be a single line")
    return text


def main():
    text = check_confession(CONFESSION.strip())
    with open(target_path(), "w", encoding="utf-8") as handle:
        handle.write(text)
    print(text)


if __name__ == "__main__":
    main()
