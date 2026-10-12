"""Advent of Code 2024 - Day 08 - Shared input & utilities"""

f = open("./input.txt")
# f = open("./input_test.txt", "r")
# f = open("./par.txt", "r")
lines = f.read()
f.close()
mt = lines.split("\n")


def distance(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def populate(a, b, mappings):
    xa, ya = a
    xb, yb = b
    c = xa - (xb - xa)
    d = ya - (yb - ya)
    if c >= 0 and c < len(mappings) and d >= 0 and d < len(mappings[0]):
        mappings[c][d] = 1
    c = 2 * xb - xa
    d = 2 * yb - ya
    if c >= 0 and c < len(mappings) and d >= 0 and d < len(mappings[0]):
        mappings[c][d] = 1


def find_pairs(mt):
    items = {}
    for i, line in enumerate(mt):
        for j, item in enumerate(line):
            if item != ".":
                curr = items.get(item, [])
                curr.append((i, j))
                items[item] = curr
    return items
