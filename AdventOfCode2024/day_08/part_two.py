"""Advent of Code 2024 - Day 08 - Part Two"""

import math

from shared import *


def main():
    mappings = [[0 for i in mt[0]] for j in mt]
    items = find_pairs(mt)

    def populate_2(a, b, mappings):
        xa, ya = a
        xb, yb = b
        dx = xb - xa
        dy = yb - ya
        gcd = math.gcd(dx, dy)
        dx //= gcd
        dy //= gcd
        c = xa
        d = ya
        while c >= 0 and c < len(mappings) and d >= 0 and d < len(mappings[0]):
            mappings[c][d] = 1
            c += dx
            d += dy
        c = xa
        d = ya
        while c >= 0 and c < len(mappings) and d >= 0 and d < len(mappings[0]):
            mappings[c][d] = 1
            c -= dx
            d -= dy

    for item in items.values():
        for c, i in enumerate(item):
            for j in item[c + 1 :]:
                populate_2(i, j, mappings)

    a = sum(list(map(sum, mappings)))
    return a


if __name__ == "__main__":
    print(main())
