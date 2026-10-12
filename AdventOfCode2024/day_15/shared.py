"""Advent of Code 2024 - Day 15 - Shared input & utilities"""

import copy

f = open("./input.txt")
# f = open("./input_test.txt", "r")
# f = open("./par.txt", "r")
lines = f.read()
f.close()
mt = lines.split("\n")

wall = []
line = mt[0]
i = 0
while "#" in line:
    wall.append(list(line))
    i += 1
    line = mt[i]
wall_1 = copy.deepcopy(wall)
moves = []
for line in mt[i:]:
    if "<" in line:
        moves.append(list(line))
dir = {">": (0, 1), "<": (0, -1), "^": (-1, 0), "v": (1, 0)}

moves = ["".join(m) for m in moves]
moves = "".join(moves)


def find_start_pos(wall):
    for i in range(len(wall)):
        for j in range(len(wall[0])):
            if wall[i][j] == "@":
                return i, j
