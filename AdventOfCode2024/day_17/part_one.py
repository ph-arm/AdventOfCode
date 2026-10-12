"""Advent of Code 2024 - Day 17 - Part One"""

import shared
from shared import *


def main():
    shared.register[:] = [64196994, 0, 0]
    shared.prog[:] = [2, 4, 1, 1, 7, 5, 1, 5, 4, 0, 0, 3, 5, 5, 3, 0]
    shared.pointer = 0
    run()
    return ",".join(str(x) for x in shared.output)


if __name__ == "__main__":
    print(main())
