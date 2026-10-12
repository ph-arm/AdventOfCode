"""Advent of Code 2022 - Day 17 - Part Two"""

import os

test_case = bool(int(os.getenv("AOC_TEST_CASE", "0")))

ROCKS = [
    [(0, 0), (1, 0), (2, 0), (3, 0)],
    [(1, 0), (0, 1), (1, 1), (2, 1), (1, 2)],
    [(0, 0), (1, 0), (2, 0), (2, 1), (2, 2)],
    [(0, 0), (0, 1), (0, 2), (0, 3)],
    [(0, 0), (1, 0), (0, 1), (1, 1)],
]


def main():
    path = "./test_input.txt" if test_case else "./input.txt"
    with open(path) as file:
        jets = file.read().strip()

    total = 1000000000000
    occupied = set()
    col_top = [-1] * 7
    height = 0
    jet = 0
    seen = {}
    extra = 0
    rock_number = 0

    while rock_number < total:
        shape = ROCKS[rock_number % 5]
        rx, ry = 2, height + 3
        while True:
            dx = -1 if jets[jet % len(jets)] == "<" else 1
            jet += 1
            if all(
                0 <= x + rx + dx < 7 and (x + rx + dx, y + ry) not in occupied
                for x, y in shape
            ):
                rx += dx
            if all(
                y + ry - 1 >= 0 and (x + rx, y + ry - 1) not in occupied
                for x, y in shape
            ):
                ry -= 1
            else:
                for x, y in shape:
                    occupied.add((x + rx, y + ry))
                    if y + ry > col_top[x + rx]:
                        col_top[x + rx] = y + ry
                height = max(col_top) + 1
                break
        rock_number += 1

        if extra == 0:
            key = (
                rock_number % 5,
                jet % len(jets),
                tuple(height - top for top in col_top),
            )
            if key in seen:
                prev_rock, prev_height = seen[key]
                cycle_len = rock_number - prev_rock
                cycle_height = height - prev_height
                cycles = (total - rock_number) // cycle_len
                extra = cycles * cycle_height
                rock_number += cycles * cycle_len
            else:
                seen[key] = (rock_number, height)

    return height + extra


if __name__ == "__main__":
    print(main())
