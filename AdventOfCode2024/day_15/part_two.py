"""Advent of Code 2024 - Day 15 - Part Two"""

from shared import *


def main():
    wall_2 = []
    for i in wall_1:
        c = []
        for j in i:
            if j == "@":
                c.append("@")
                c.append(".")
            if j == "O":
                c.append("[")
                c.append("]")
            if j == "#":
                c.append("#")
                c.append("#")
            if j == ".":
                c.append(".")
                c.append(".")
        wall_2.append(c)

    pos = find_start_pos(wall_2)

    def check_move_2(wall, pos, move, depth=0):
        # only check this time
        try:
            i, j = pos
            mi, mj = dir[move]
            if wall[i + mi][j + mj] == "#":
                return 0
            if wall[i + mi][j + mj] == ".":
                return 1

            if move in "><":
                return check_move_2(wall, (i + mi, j + mj), move, depth + 1)
            if wall[i + mi][j + mj] == "[":
                return check_move_2(
                    wall, (i + mi, j + 1 + mj), move, depth + 1
                ) and check_move_2(wall, (i + mi, j + mj), move, depth + 1)

            if wall[i + mi][j + mj] == "]":
                return check_move_2(
                    wall, (i + mi, j + mj - 1), move, depth + 1
                ) and check_move_2(wall, (i + mi, j + mj), move, depth + 1)
            return check_move_2(wall, (i + mi, j + mj), move, depth + 1)
        except Exception:
            print("ouch:", pos, move)
            raise Exception from None

    def move_2(wall_2, pos, move, lateral=0):
        try:
            i, j = pos
            mi, mj = dir[move]
            curr = wall_2[i][j]
            if move in "<>":
                if curr in "[]@":
                    move_2(wall_2, (i + mi, j + mj), move)
                    wall_2[i][j] = "."
                    wall_2[i + mi][j + mj] = curr
                return 0
            if curr == "[" and wall_2[i - mi][j - mj] != "[" and not lateral:
                move_2(wall_2, (i + mi, j + mj), move)
                move_2(wall_2, (i, j + 1), move, 1)
                wall_2[i][j] = "."
                wall_2[i + mi][j + mj] = curr
                return
            if curr == "]" and wall_2[i - mi][j - mj] != "]" and not lateral:
                move_2(wall_2, (i + mi, j + mj), move)
                move_2(wall_2, (i, j - 1), move, 1)
                wall_2[i][j] = "."
                wall_2[i + mi][j + mj] = curr
                return
            if curr == ".":
                return
            if curr == "#":
                print("here hit wall -- chcek error")

            move_2(wall_2, (i + mi, j + mj), move)
            wall_2[i][j] = "."
            wall_2[i + mi][j + mj] = curr
        except Exception as e:
            print("move ouch:", pos, move)
            print(e)
            raise Exception from e

    for move in moves:
        if check_move_2(wall_2, pos, move):
            move_2(wall_2, pos, move)
            pos = (pos[0] + dir[move][0], pos[1] + dir[move][1])
            if wall_2[pos[0]][pos[1]] != "@":
                print("here")

    def calc_2(wall):
        res = 0
        for i in range(len(wall)):
            for j in range(len(wall[0])):
                if wall[i][j] == "[":
                    res += i * 100 + j
        return res

    return calc_2(wall_2)


if __name__ == "__main__":
    print(main())
