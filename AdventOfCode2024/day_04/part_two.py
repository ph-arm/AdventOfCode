"""Advent of Code 2024 - Day 04 - Part Two"""

from shared import *


def main():
    def check(mt, i, j):
        res = 0
        if (
            mt[i - 1][j - 1] == "M"
            and mt[i - 1][j + 1] == "M"
            and mt[i + 1][j + 1] == "S"
            and mt[i + 1][j - 1] == "S"
        ):
            res += 1
        if (
            mt[i - 1][j - 1] == "M"
            and mt[i + 1][j - 1] == "M"
            and mt[i + 1][j + 1] == "S"
            and mt[i - 1][j + 1] == "S"
        ):
            res += 1
        if (
            mt[i - 1][j + 1] == "M"
            and mt[i + 1][j + 1] == "M"
            and mt[i - 1][j - 1] == "S"
            and mt[i + 1][j - 1] == "S"
        ):
            res += 1
        if (
            mt[i + 1][j - 1] == "M"
            and mt[i + 1][j + 1] == "M"
            and mt[i - 1][j - 1] == "S"
            and mt[i - 1][j + 1] == "S"
        ):
            res += 1
        return res

    res = 0
    for i in range(1, -1 + len(mt)):
        for j in range(1, -1 + len(mt[0])):
            if mt[i][j] == "A":
                res += check(mt, i, j)
    return res


if __name__ == "__main__":
    print(main())
