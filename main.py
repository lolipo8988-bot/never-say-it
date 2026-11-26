"""Never Say It Out Loud entry.

Writes exactly one funny line (81 chars, <= 140) -- the sentence you must
never say out loud -- to /output/entry.txt. Deterministic: same bytes
on every run. No network, no secrets, no dependencies.
"""

import os

ENTRY = (
    "Never say 'you look tired' \u2014 it's just 'you look awful' "
    "wearing a concerned face."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    assert 1 <= len(ENTRY) <= 140, f"entry is {len(ENTRY)} chars"
    assert ENTRY.strip(), "entry must not be only whitespace"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
