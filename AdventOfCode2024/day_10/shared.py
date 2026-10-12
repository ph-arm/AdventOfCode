"""Advent of Code 2024 - Day 10 - Shared input & utilities"""

f = open("./input.txt")
# f = open("./input_test.txt", "r")
# f = open("./par.txt", "r")
lines = f.read()
f.close()
mt = lines.split("\n")
mt = [list(x) for x in mt]
mt = [list(map(int, x)) for x in mt]
