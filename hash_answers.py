#!/usr/bin/env python3
"""Regenerate answer_hashes.json from answers_clear.json.

Hashes every plaintext answer in answers_clear.json with the same SHA-256
function used for verification (check_answers.sha256) and rewrites the committed
answer_hashes.json. Use this after manually editing answers_clear.json, instead
of a full network re-fetch with fetch_answers.py.

Usage: python3 hash_answers.py
"""

import json
import sys

from check_answers import HASH_FILE, ROOT, sha256

CLEAR_FILE = ROOT / "answers_clear.json"


def main() -> None:
    if not CLEAR_FILE.exists():
        print(f"Missing {CLEAR_FILE.name}. Run fetch_answers.py first.")
        sys.exit(1)

    with open(CLEAR_FILE) as f:
        clear = json.load(f)

    hashes: dict = {}
    count = 0
    for year_key, days in clear.items():
        hashes[year_key] = {}
        for day_key, parts in days.items():
            hashes[year_key][day_key] = {}
            for part_key, answer in parts.items():
                hashes[year_key][day_key][part_key] = sha256(str(answer))
                count += 1

    with open(HASH_FILE, "w") as f:
        json.dump(hashes, f, indent=2)

    print(f"\u2713 wrote {HASH_FILE.name} ({count} answer hashes)")


if __name__ == "__main__":
    main()
