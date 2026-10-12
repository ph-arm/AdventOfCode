"""Advent of Code 2024 - Day 19 - Part Two"""

from shared import *


def main():
    from functools import cache

    @cache
    def process_2(i):
        if len(i) == 0:
            return 1
        k = 0
        for j in tow:
            if i.startswith(j.strip()):
                k += process_2(i[len(j) :])
        return k

    def process_c(i, comp):
        if len(i) == 0:
            return 1
        for j in comp:
            if i.startswith(j[0]):
                return j[1] * process_c(i[len(j[0]) :], comp)
        return 0

    # compression step:
    comp = []
    for i in range(len(tow)):
        k = process_2(tow[i])
        comp.append([tow[i], k])
    comp.sort(key=lambda x: len(x[0]), reverse=True)

    res = 0
    for i in pat:
        res += process_2(i)
    return res


if __name__ == "__main__":
    print(main())
