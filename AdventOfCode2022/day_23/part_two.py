"""Advent of Code 2022 - Day 23 - Part Two"""

import os

test_case = bool(int(os.getenv("AOC_TEST_CASE", "0")))

DIRECTIONS = [
    ((-1, -1), (0, -1), (1, -1), (0, -1)),  # north
    ((-1, 1), (0, 1), (1, 1), (0, 1)),  # south
    ((-1, -1), (-1, 0), (-1, 1), (-1, 0)),  # west
    ((1, -1), (1, 0), (1, 1), (1, 0)),  # east
]
NEIGHBOURS = [
    (-1, -1),
    (0, -1),
    (1, -1),
    (-1, 0),
    (1, 0),
    (-1, 1),
    (0, 1),
    (1, 1),
]


def main():
    path = "./test_input.txt" if test_case else "./input.txt"
    with open(path) as file:
        content = file.read().split("\n")
    elves = set()
    for y, line in enumerate(content):
        for x, item in enumerate(line):
            if item == "#":
                elves.add((x, y))

    offset = 0
    rounds = 0
    while True:
        rounds += 1
        proposals = {}
        counts = {}
        for x, y in elves:
            if not any((x + dx, y + dy) in elves for dx, dy in NEIGHBOURS):
                continue
            for i in range(4):
                c1, c2, c3, mv = DIRECTIONS[(offset + i) % 4]
                if (
                    (x + c1[0], y + c1[1]) not in elves
                    and (x + c2[0], y + c2[1]) not in elves
                    and (x + c3[0], y + c3[1]) not in elves
                ):
                    target = (x + mv[0], y + mv[1])
                    proposals[(x, y)] = target
                    counts[target] = counts.get(target, 0) + 1
                    break

        moved = False
        new_elves = set()
        for elf in elves:
            target = proposals.get(elf)
            if target is not None and counts[target] == 1:
                new_elves.add(target)
                moved = True
            else:
                new_elves.add(elf)
        elves = new_elves
        offset = (offset + 1) % 4
        if not moved:
            return rounds


if __name__ == "__main__":
    print(main())
