"""Dad Joke Showdown entry.

Writes this entry's single dad joke to ``entry.txt`` in the output
directory (``$MAKEFUN_OUTPUT_DIR`` when set, else ``/output``). The joke
is the whole entry: the sealed scorer checks it is UTF-8 text of 1 to
200 characters, and the judge compares it two at a time against the
other jokes.

The joke was picked from a drafted pool of twenty by scoring each one
head-to-head against the judge's published brief, in its own order:
a dad joke a father would tell at the table; the pun landing cleanly
on the first read; fresh rather than told a thousand times, while
staying inside the dad joke tradition; tight, with the punchline
arriving at the end; and a rhythm that reads naturally aloud.

The winner's turn is the last word. "Boring" is what a person calls a
dull partner and what a drill does for a living, so the break-up line
reads straight first and turns only on the final word -- no explaining,
nothing wasted, and it is not one of the thousand-times classics (the
calendar, the scarecrow, the atoms) that the field is full of.
"""

import os

JOKE = "Why did the drill break up with the hammer? It found him boring."


def main() -> None:
    # Hold the entry to the sealed gate before writing anything: UTF-8
    # text of 1 to 200 characters, not only white space.
    if not 1 <= len(JOKE) <= 200 or not JOKE.strip():
        raise ValueError("joke falls outside the 1-200 character gate")
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(JOKE)


if __name__ == "__main__":
    main()
