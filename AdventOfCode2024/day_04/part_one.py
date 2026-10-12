"""Advent of Code 2024 - Day 04 - Part One"""

from shared import *


def main():
    res = 0
    for line in mt:
        res += line.count("XMAS")  # hori
        res += line[::-1].count("XMAS")  # reverse Hori

    # create up  to down line
    for i in range(len(mt[0])):
        line = ""
        for j in range(len(mt)):
            line += mt[j][i]
        res += line.count("XMAS")  # vert
        res += line[::-1].count("XMAS")  # reverse vert

    # create diagonal line
    for i in range(len(mt)):
        line = ""
        for j in range(len(mt[0])):
            if i + j < len(mt):
                line += mt[i + j][j]
        res += line.count("XMAS")  # diag
        res += line[::-1].count("XMAS")  # reverse diag
        if i == 0:
            continue

        line = ""
        for j in range(len(mt[0])):
            if j - i >= 0:
                line += mt[j - i][j]
        res += line.count("XMAS")  # reverse diag
        res += line[::-1].count("XMAS")  # reverse reverse diag

    # create reverse diagonal line
    for i in range(2 * len(mt)):
        line = ""
        for j in range(len(mt[0])):
            if i - j >= 0 and i - j < len(mt):
                line += mt[i - j][j]
        res += line.count("XMAS")  # reverse diag
        res += line[::-1].count("XMAS")  # reverse reverse diag
    return res


if __name__ == "__main__":
    print(main())
