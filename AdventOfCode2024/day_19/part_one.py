"""Advent of Code 2024 - Day 19 - Part One"""

from shared import *


def main():
    def process(i, candidates):
        if len(i) == 0:
            return 1
        for j in candidates:
            if i.startswith(j.strip()):
                if process(i[len(j) :], candidates):
                    return 1
        return 0

    not_found = 0
    for i in pat:
        res = process(i, tow)
        if res == 0:
            not_found += 1
    return len(pat) - not_found


if __name__ == "__main__":
    print(main())
