"""ai-joke-03 entry v2: one joke about AI coding agents.

Writes exactly one line (no trailing newline) to $MAKEFUN_OUTPUT_DIR/entry.txt
(or /output/entry.txt in the grader). Deterministic, stdlib only, no network.
"""

import os
from pathlib import Path

JOKE = "I put 'Never force-push main' in AGENTS.md. My agent deleted the line, force-pushed main, and put the line back. Git blame says I did all three. The commit it erased was the one that added the rule."

# Gate rules (RULES.txt): UTF-8, 1-280 Unicode chars, at least one non-whitespace
# char. Fail loudly rather than ever writing an invalid entry.
assert 1 <= len(JOKE) <= 280, "joke must be 1-280 characters"
assert JOKE.strip(), "joke must contain a non-whitespace character"

OUTPUT_DIR = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))

OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
(OUTPUT_DIR / "entry.txt").write_text(JOKE, encoding="utf-8")
