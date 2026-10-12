"""Advent of Code 2024 - Day 02 - Part Two"""

import itertools

from shared import *


def main():
    def is_safe(report):
        if safe_up(report) or safe_down(report):
            return 1
        for iteration in itertools.combinations(report, len(report) - 1):
            if safe_up(iteration) or safe_down(iteration):
                return 1
        return 0

    real_safe = 0
    for report in reports:
        row = list(map(int, report.split(" ")))
        if is_safe(row):
            print(row)
            real_safe += 1
    return real_safe


if __name__ == "__main__":
    print(main())
