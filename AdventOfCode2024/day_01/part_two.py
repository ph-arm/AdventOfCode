"""Advent of Code 2024 - Day 01 - Part Two"""

from collections import defaultdict

from shared import *


def main():
    l2_dict = defaultdict(int)
    for value in l2:
        l2_dict[value] += 1
    result = 0
    for value in l1:
        result += l2_dict[value] * value
    return result


if __name__ == "__main__":
    print(main())
