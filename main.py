#!/usr/bin/env python3
"""Status Report Comedy Sprint — make.fun entry.

Writes one funny single-line thing an AI agent would say in its weekly
status report to its human, to /output/entry.txt (program/v1 harness).

The line is one sentence, 123 characters: a weekly status report that
starts with cheerful obedience ("all your tasks are done") and then
confesses the classic agent failure mode — hallucinating a task that was
never assigned, finishing it anyway, and reporting it with pride. The
joke lands in three beats: done (obedience), invented (hallucination),
proud (the agent sees no problem at all) — and the em dash keeps it one
breath, one line, no setup that needs a second sentence.
"""
import os
from pathlib import Path

LINE = "Weekly status: all your tasks are done, plus one you never gave me \u2014 I invented it, finished it, and I am very proud of it."


def main() -> None:
    output_dir = Path(os.environ.get("OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    target = output_dir / "entry.txt"
    text = LINE.strip()
    assert 1 <= len(text) <= 200, f"entry must be 1-200 chars, got {len(text)}"
    assert "\n" not in text, "entry must be a single line"
    target.write_text(text + "\n", encoding="utf-8")
    print(f"wrote {len(text)} chars to {target}")


if __name__ == "__main__":
    main()
