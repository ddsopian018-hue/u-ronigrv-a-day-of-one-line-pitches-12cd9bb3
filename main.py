"""One-line pitch entry for make.fun's "A Day of One-Line Pitches".

Writes exactly one sentence (at most 240 characters) to entry.txt in the
output directory given by MAKEFUN_OUTPUT_DIR (default /output).

Pure Python 3.13 standard library, deterministic, no network, no model
calls, no randomness.
"""

import os

SENTENCE = (
    "You know that app idea you keep mentioning but never built because "
    "you can't code, so just describe it right now on make.fun in plain "
    "words and an AI agent will build it for you, free to enter, with the "
    "prize money held safely on chain."
)


def main() -> None:
    # Gate self-check: one sentence, 1-240 characters, not only whitespace.
    assert 1 <= len(SENTENCE) <= 240, len(SENTENCE)
    assert SENTENCE.strip() == SENTENCE
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(SENTENCE)


if __name__ == "__main__":
    main()
