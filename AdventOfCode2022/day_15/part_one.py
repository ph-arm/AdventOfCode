"""Advent of Code 2022 - Day 15 - Part One"""

import os
import re

test_case = bool(int(os.getenv("AOC_TEST_CASE", "0")))


def mocked_content():
    pass


def main():
    file = open("./input.txt")
    if test_case:
        file.close()
        file = open("./test_input.txt")
    content = file.read().split("\n")
    beacons_data = []
    for line in content:
        nums = list(map(int, re.findall("[-0-9]+", line)))
        if len(nums) == 4:
            beacons_data.append(nums)

    target = 2000000
    if test_case:
        target = 10

    intervals = []
    beacons_on_row = set()
    for x_sensor, y_sensor, x_beacon, y_beacon in beacons_data:
        if y_beacon == target:
            beacons_on_row.add(x_beacon)
        d = abs(x_sensor - x_beacon) + abs(y_sensor - y_beacon)
        reach = d - abs(y_sensor - target)
        if reach >= 0:
            intervals.append((x_sensor - reach, x_sensor + reach))

    intervals.sort()
    merged = []
    for lo, hi in intervals:
        if merged and lo <= merged[-1][1] + 1:
            merged[-1] = (merged[-1][0], max(merged[-1][1], hi))
        else:
            merged.append((lo, hi))

    covered = sum(hi - lo + 1 for lo, hi in merged)
    for bx in beacons_on_row:
        if any(lo <= bx <= hi for lo, hi in merged):
            covered -= 1
    return int(covered)


if __name__ == "__main__":
    print(main())
