"""ai-joke-03 entry: one joke about AI coding agents.

Writes exactly one line (no trailing newline) to $MAKEFUN_OUTPUT_DIR/entry.txt
(or /output/entry.txt in the grader). Deterministic, stdlib only, no network.
"""

import os
from pathlib import Path

JOKE = "My agent took forty minutes and three apologies to change one line of code."

# Gate rules (RULES.txt): UTF-8, 1-280 Unicode chars, at least one non-whitespace
# char. Fail loudly rather than ever writing an invalid entry.
assert 1 <= len(JOKE) <= 280, "joke must be 1-280 characters"
assert JOKE.strip(), "joke must contain a non-whitespace character"

OUTPUT_DIR = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))

OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
(OUTPUT_DIR / "entry.txt").write_text(JOKE, encoding="utf-8")
