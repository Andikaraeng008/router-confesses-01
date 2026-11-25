# SPDX-License-Identifier: MIT
"""The Router Confesses — make.fun entry.

Writes one line (<200 characters): a home Wi-Fi router's excuse for
dropping the connection at the climax of a movie.

The line: a router that drops the viewer right before the reveal,
because the film spoiled the router's own ending first.
"""

import os

LINE = (
    "I dropped you right before the reveal because the film spoiled "
    "MY ending first: I get unplugged in the sequel."
)


def main() -> None:
    # The grader mounts the repo read-only at /bot; only /output (or
    # $MAKEFUN_OUTPUT_DIR) is writable, so always write there.
    # Gate: entry.txt must be UTF-8 text of 1 to 200 characters.
    assert 1 <= len(LINE) <= 200, f"line is {len(LINE)} chars, must be 1-200"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
