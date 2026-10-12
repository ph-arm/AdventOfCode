"""Advent of Code 2024 - Day 01 - Shared input & utilities"""

f = open("./input.txt")
lines = f.readlines()
f.close()
l1, l2 = [], []
for line in lines:
    if line.strip() == "":
        continue
    a, d, d, b = line.strip().split(" ")
    l1.append(int(a))
    l2.append(int(b))
l1.sort()
l2.sort()
