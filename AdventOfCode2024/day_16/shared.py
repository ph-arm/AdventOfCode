"""Advent of Code 2024 - Day 16 - Shared input & utilities"""

f = open("./input.txt")
# f = open("./input_test.txt", "r")
# f = open("./par.txt", "r")
lines = f.read()
f.close()
mt = lines.split("\n")
mt = [list(i) for i in mt]


def find_re(mt, X):
    for i, c in enumerate(mt):
        for j, d in enumerate(c):
            if d == X:
                return i, j


moves = {"U": (-1, 0), "R": (0, 1), "D": (1, 0), "L": (0, -1)}
move_k = list(moves.keys())
