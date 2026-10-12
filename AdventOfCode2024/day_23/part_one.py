"""Advent of Code 2024 - Day 23 - Part One"""

from shared import *


def main():
    conn = {}
    for i in mt:
        a, b = i.split("-")
        a_c = conn.get(a, set())
        a_c.add(b)
        b_c = conn.get(b, set())
        b_c.add(a)
        conn[a] = a_c
        conn[b] = b_c

    res = set()
    for i in conn.keys():
        for connec in conn[i]:
            for j in conn[connec]:
                if i in conn[j]:
                    f = [i, j, connec]
                    f.sort()
                    res.add(tuple(f))
    tot = 0
    for i in res:
        for j in i:
            if j[0] == "t":
                tot += 1
                break
    return tot


if __name__ == "__main__":
    print(main())
