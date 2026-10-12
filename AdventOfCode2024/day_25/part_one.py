"""Advent of Code 2024 - Day 25 - Part One"""

from shared import *


def main():
    fits = 0
    for lock in locks:
        for key in keys:
            # A pair fits when no column's pin + tooth exceeds the free space.
            if all(lock_h + key_h <= SPACE for lock_h, key_h in zip(lock, key)):
                fits += 1
    return fits


if __name__ == "__main__":
    print(main())
