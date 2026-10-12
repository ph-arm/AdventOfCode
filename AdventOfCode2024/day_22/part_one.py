"""Advent of Code 2024 - Day 22 - Part One"""

from shared import *


def main():
    res = 0
    for i in mt:
        res += n2000(int(i))
    return res


if __name__ == "__main__":
    print(main())
