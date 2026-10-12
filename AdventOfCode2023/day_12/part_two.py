"""Advent of Code 2023 - Day 12 - Part Two"""

import os
from functools import cache

test = bool(int(os.getenv("AOC_TEST_CASE", "0")))
INPUT = "./test_input.txt" if test else "./input.txt"
f = open(INPUT)
data = list(map(str.strip, f.read().split("\n")))


@cache
def count(pattern: str, groups: tuple) -> int:
    """Count valid arrangements of pattern matching the given contiguous group sizes."""
    if not groups:
        return 0 if "#" in pattern else 1
    if not pattern:
        return 0

    result = 0
    g = groups[0]

    # Option 1: treat current char as '.' (skip it)
    if pattern[0] != "#":
        result += count(pattern[1:], groups)

    # Option 2: place a group of size g starting here
    if (
        len(pattern) >= g
        and "." not in pattern[:g]  # all chars can be '#'
        and (len(pattern) == g or pattern[g] != "#")  # not immediately followed by '#'
    ):
        result += count(pattern[g + 1 :], groups[1:])

    return result


def solve(line: str) -> int:
    s, items = line.split(" ")
    groups = tuple(map(int, items.split(",")))
    # Unfold 5x
    pattern = "?".join([s] * 5)
    groups = groups * 5
    return count(pattern, groups)


def main():
    total = sum(solve(line) for line in data if line)
    print(total)
    return total


if __name__ == "__main__":
    main()
