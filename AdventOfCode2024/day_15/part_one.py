"""Advent of Code 2024 - Day 15 - Part One"""

from shared import *


def main():
    def find_start_pos(wall):
        for i in range(len(wall)):
            for j in range(len(wall[0])):
                if wall[i][j] == "@":
                    return i, j

    start_pos = find_start_pos(wall)
    pos = start_pos

    def check_move(wall, pos, move, depth=0):
        try:
            i, j = pos
            mi, mj = dir[move]
            if wall[i + mi][j + mj] == "#":
                return 0
            if wall[i + mi][j + mj] == "O":
                if check_move(wall, (i + mi, j + mj), move, depth + 1):
                    wall[i + mi][j + mj] = wall[i][j]
                    wall[i][j] = "."
                    return 1
                return 0
            elif wall[i + mi][j + mj] == ".":
                wall[i + mi][j + mj] = wall[i][j]
                wall[i][j] = "."
                return 1
            print("here")
        except Exception:
            print("ouch", pos, move)

    for move in moves:
        if check_move(wall, pos, move):
            pos = (pos[0] + dir[move][0], pos[1] + dir[move][1])

    def calc(wall):
        res = 0
        for i in range(len(wall)):
            for j in range(len(wall[0])):
                if wall[i][j] == "O":
                    res += i * 100 + j
        return res

    return calc(wall)


if __name__ == "__main__":
    print(main())
