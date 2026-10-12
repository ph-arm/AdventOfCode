"""Advent of Code 2024 - Day 01 - Part One"""

from shared import *


def main():
    result = 0
    for c, i in enumerate(l1):
        result += abs(i - l2[c])
    return result


if __name__ == "__main__":
    print(main())
