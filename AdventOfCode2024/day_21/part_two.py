"""Advent of Code 2024 - Day 21 - Part Two"""

from shared import *


def main():
    return sum(complexity(code, 25) for code in codes)


if __name__ == "__main__":
    print(main())
