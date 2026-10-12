"""Advent of Code 2024 - Day 23 - Shared input & utilities"""

test = 1
f = open("./input.txt")
# f = open("./input_test.txt", "r")

content = f.read()
mt = content.split("\n")

conn = {}
for _i in mt:
    if "-" not in _i:
        continue
    a, b = _i.split("-")
    a_c = conn.get(a, set())
    a_c.add(b)
    b_c = conn.get(b, set())
    b_c.add(a)
    conn[a] = a_c
    conn[b] = b_c

test = 1
f = open("./input.txt")
# f = open("./input_test.txt", "r")

content = f.read()
mt = content.split("\n")
