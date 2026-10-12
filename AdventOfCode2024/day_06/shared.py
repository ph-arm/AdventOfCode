"""Advent of Code 2024 - Day 06 - Shared input & utilities"""

f = open("./input.txt")
# f = open("./input_test.txt", "r")
# f = open("./par.txt", "r")
lines = f.read()
f.close()
mt = lines.split("\n")

directions = ["^", ">", "v", "<"]


def find_start(mt):
    for i in range(len(mt)):
        for j in range(len(mt[0])):
            if mt[i][j] in directions:
                return i, j, mt[i][j]
    return -1, -1


x, y, current_dir = find_start(mt)

x_start, y_start, dir_start = x, y, current_dir
