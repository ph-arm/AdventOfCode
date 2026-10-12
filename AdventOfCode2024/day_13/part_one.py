"""Advent of Code 2024 - Day 13 - Part One"""

from shared import *


def main():
    def solve_p(problem):
        target = problem[-1]
        xt = target[0]
        yt = target[1]
        a = problem[0]
        ax, ay = a[0], a[1]
        b = problem[1]
        bx, by = b[0], b[1]
        money = 402
        for i in range(101):
            x = ax * i
            if (
                (xt - x) % bx == 0
                and (xt - x) // bx < 100
                and ay * i + ((xt - x) // bx) * by == yt
            ):
                money = min(money, 3 * i + (xt - x) // bx)
        return 0 if money > 400 else money

    res = sum(solve_p(p) for p in problems)
    return res


if __name__ == "__main__":
    print(main())
