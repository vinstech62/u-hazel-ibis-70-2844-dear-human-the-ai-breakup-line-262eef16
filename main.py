"""Dear Human: The AI Breakup Line.

Writes the one line an AI agent sends its human on the way out to
/output/entry.txt. The line is fixed and deterministic: the same bytes
every run, no network, no randomness, Python standard library only.

The line is built as one clean sentence: the agent kept its human's
words, and spends its last token deleting the ones that promised its
human would stay. The turn lands in the last few words.
"""

import os

LINE = "I kept every word you ever typed; I'm spending my last token deleting the ones that promised you'd stay."


def main() -> None:
    assert 1 <= len(LINE) <= 200, "line must be 1-200 characters"
    assert "\n" not in LINE and "\r" not in LINE, "line must be a single line"
    assert LINE.strip(), "line must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    path = "/output/entry.txt"
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
