"""Advent of Code 2024 - Day 02 - Part One"""

from shared import *


def main():
    safe = 0
    for report in reports:
        row = list(map(int, report.split(" ")))
        if safe_up(row) or safe_down(row):
            print(row)
            safe += 1
    return safe


if __name__ == "__main__":
    print(main())
