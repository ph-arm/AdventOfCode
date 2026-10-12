"""Advent of Code 2024 - Day 19 - Shared input & utilities"""

test = 1
f = open("./input.txt")
# f = open("./input_test.txt", "r")

content = f.read()
f_read = content.split("\n")
tow = f_read[0].split(",")
tow = list(map(lambda x: x.strip(), tow))
pat = list(map(lambda x: x.strip(), f_read[2:]))
