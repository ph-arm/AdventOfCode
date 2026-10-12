"""Advent of Code 2024 - Day 22 - Part Two"""

from shared import *


def main():
    def max_map(a):
        res = a
        ant = []
        max_p_l = {}
        for i in range(4):
            res_2 = process_num(res)
            ant.append((res_2 % 10) - (res % 10))
            res = res_2
            kk = tuple(ant)
            max_p_l[kk] = max(res % 10, max_p_l.get(kk, 0))
        for i in range(4, 1999):
            res_2 = process_num(res)
            ant.pop(0)
            ant.append((res_2 % 10) - (res % 10))
            res = res_2
            kk = tuple(ant)
            loc = max_p_l.get(kk, -1)
            if loc >= 0:
                continue
            max_p_l[kk] = res % 10
        return max_p_l

    max_p = {}
    for i in mt:
        res = max_map(int(i))
        for key in res:
            max_p[key] = max_p.get(key, 0) + res[key]
    return max(max_p.values())


if __name__ == "__main__":
    print(main())
