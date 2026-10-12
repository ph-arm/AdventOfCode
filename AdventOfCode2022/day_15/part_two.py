"""Advent of Code 2022 - Day 15 - Part Two"""

import os
import re

test_case = bool(int(os.getenv("AOC_TEST_CASE", "0")))


def mocked_content():
    pass


def main():
    file = open("./test_input.txt" if test_case else "./input.txt")
    content = file.read().split("\n")
    file.close()
    sensors = []
    for line in content:
        nums = list(map(int, re.findall("[-0-9]+", line)))
        if len(nums) == 4:
            x_sensor, y_sensor, x_beacon, y_beacon = nums
            reach = abs(x_sensor - x_beacon) + abs(y_sensor - y_beacon)
            sensors.append((x_sensor, y_sensor, reach))

    limit = 20 if test_case else 4000000

    # The single uncovered cell sits just outside the perimeter of the sensors,
    # at an intersection of boundary lines of slope +1 (y - x) and -1 (y + x).
    down_diagonals = set()
    up_diagonals = set()
    for x_sensor, y_sensor, reach in sensors:
        down_diagonals.add(y_sensor - x_sensor + reach + 1)
        down_diagonals.add(y_sensor - x_sensor - reach - 1)
        up_diagonals.add(y_sensor + x_sensor + reach + 1)
        up_diagonals.add(y_sensor + x_sensor - reach - 1)

    for a in down_diagonals:
        for b in up_diagonals:
            if (a + b) % 2 != 0:
                continue
            x = (b - a) // 2
            y = (a + b) // 2
            if not (0 <= x <= limit and 0 <= y <= limit):
                continue
            if all(abs(sx - x) + abs(sy - y) > r for sx, sy, r in sensors):
                return x * 4000000 + y
    return None


if __name__ == "__main__":
    print(main())
