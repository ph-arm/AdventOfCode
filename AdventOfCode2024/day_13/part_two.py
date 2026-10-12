"""Advent of Code 2024 - Day 13 - Part Two"""

from shared import *


def main():
    offset = 10000000000000

    def solve_p(problem):
        target = problem[-1]
        xt = target[0] + offset
        yt = target[1] + offset
        a = problem[0]
        ax, ay = a[0], a[1]
        b = problem[1]
        bx, by = b[0], b[1]
        if (bx * ay - by * ax) == 0:
            return 0
        t2 = (xt * ay - yt * ax) // (bx * ay - by * ax)
        t1 = (xt - bx * t2) // ax
        if (xt * ay - yt * ax) % (bx * ay - by * ax) != 0:
            return 0
        if (xt - bx * t2) % ax != 0:
            return 0
        return t1 * 3 + t2

    res = sum(solve_p(p) for p in problems)
    return res


if __name__ == "__main__":
    print(main())
