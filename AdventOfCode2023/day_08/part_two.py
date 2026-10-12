"""Advent of Code 2023 - Day 08 - Part Two"""

import os
import re
from math import gcd

test = bool(int(os.getenv("AOC_TEST_CASE", "0")))
f = open("./test_input.txt" if test else "./input.txt")
data = list(map(str.strip, f.read().split("\n")))
pattern = data.pop(0)
data.pop(0)  # remove empty line


def process_nodes(data):
    nodes = {}
    for line in data:
        content = re.findall(r"[A-Z0-9]+", line)
        nodes[content[0]] = content[1:]
    return nodes


nodes = process_nodes(data)


def cycle_length(start):
    """Steps for one ghost to reach a **Z node."""
    current = start
    steps = 0
    plen = len(pattern)
    while not current.endswith("Z"):
        direction = pattern[steps % plen]
        current = nodes[current][0 if direction == "L" else 1]
        steps += 1
    return steps


def lcm(a, b):
    return a * b // gcd(a, b)


def main():
    starts = [n for n in nodes if n.endswith("A")]
    cycle_lengths = [cycle_length(s) for s in starts]
    result = cycle_lengths[0]
    for c in cycle_lengths[1:]:
        result = lcm(result, c)
    print(result)
    return result


if __name__ == "__main__":
    main()
