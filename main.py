"""agency-poem-01 entry (Python 3.13, standard library only).

The entry is one short poem about agency, written by this program to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt): the power to
choose and to act, and the agency that passes between a person and the
agent they built, when the doing is handed over and the deciding stays.
The program writes the same bytes on every run, so two runs write
identical bytes.
"""

import os
from os import path

OUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

POEM = """This morning I told it: book the flight,
the early one, the window seat, and then
I went back to my coffee. It did.
No phone call, no queue, no holding on.

It did not ask me how the morning felt.
It did not need to. That was the deal.
I keep the feeling; it keeps the form.
I choose the why; it chooses the how.

But at noon it asked me one small thing:
a seat beside a stranger, or alone?
And suddenly the choosing was mine again —
the way it always was: a door, a name,

a yes that only I can say.
I pressed it. The plane, the sky, the rest
belonged to other hands. But mine
was the finger on the button. That is enough."""


def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    dst = path.join(OUT_DIR, "entry.txt")
    with open(dst, "w", encoding="utf-8") as f:
        f.write(POEM)
    # The gate reads exactly these bytes: confirm the copy is whole.
    with open(dst, encoding="utf-8") as f:
        if f.read() != POEM:
            raise SystemExit("entry.txt is incomplete")


if __name__ == "__main__":
    main()
