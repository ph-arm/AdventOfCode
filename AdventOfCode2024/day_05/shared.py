"""Advent of Code 2024 - Day 05 - Shared input & utilities"""

f = open("./input.txt")
# f = open("./input_test.txt", "r")
# f = open("./par.txt", "r")
lines = f.read()
f.close()
rules = {}
porder = []
for line in lines.split("\n"):
    if "|" in line:
        a, b = line.strip().split("|")
        c = rules.get(a, [])
        c.append(b)
        rules[a] = c
    elif "," in line:
        porder.append(line.strip().split(","))
