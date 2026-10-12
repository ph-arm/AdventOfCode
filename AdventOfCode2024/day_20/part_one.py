"""Advent of Code 2024 - Day 20 - Part One"""

from shared import *


def main():
    res = 0
    for i in range(len(mt)):
        for j in range(len(mt[0])):
            res += process_diff(i, j)
    return res


if __name__ == "__main__":
    print(main())
