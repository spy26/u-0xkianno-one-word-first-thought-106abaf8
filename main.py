"""One Word, First Thought — make.fun entry.

The competition asks for exactly one word: the first word that came to
mind, no topic, no explanation, no second draft. This entry's word is
"syzygy" — the alignment of three celestial bodies in a straight line.

Running this script prints the word to stdout and, when the harness
variable MAKEFUN_OUTPUT_DIR is set, writes it (with no trailing
newline) to <MAKEFUN_OUTPUT_DIR>/entry.txt.
"""

import os

WORD = "syzygy"

# syzygy: three y's, no ordinary vowels — a visual pattern-interrupt
# before the meaning even lands. One word, first thought, no second draft.


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if out_dir:
        path = os.path.join(out_dir, "entry.txt")
        with open(path, "w", encoding="utf-8") as f:
            f.write(WORD)
    print(WORD)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
