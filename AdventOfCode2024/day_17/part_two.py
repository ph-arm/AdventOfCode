"""Advent of Code 2024 - Day 17 - Part Two"""

import shared
from shared import *


def main():
    shared.prog[:] = [2, 4, 1, 1, 7, 5, 1, 5, 4, 0, 0, 3, 5, 5, 3, 0]

    def solve_local(res, ind):
        if ind == len(shared.prog):
            return res
        for i in range(8):
            cur = i ^ 1 ^ 5
            cur = (cur ^ ((i + (res * 8)) // (2 ** (i ^ 1)))) % 8
            to_find = shared.prog[-ind - 1]
            if to_find == cur:
                shared.register[:] = [res * 8 + i, 0, 0]
                run()
                if shared.output == shared.prog[-ind - 1 :]:
                    k = solve_local(res * 8 + i, ind + 1)
                    if k > 0:
                        return k
        return -1

    s = solve_local(0, 0)
    return s


if __name__ == "__main__":
    print(main())
