"""Advent of Code 2024 - Day 20 - Part Two"""

from shared import *


def main():
    def process_diff_2(i, j):
        c = mapping[i][j]
        if c == -1:
            return 0, []
        res = 0
        shortcut = []
        for im in range(-20, 21):
            for jm in range(-(20 - abs(im)), 21 - abs(im)):
                r = (im, jm)
                if (
                    i + r[0] >= 0
                    and i + r[0] < len(mt)
                    and j + r[1] >= 0
                    and j + r[1] < len(mt[0])
                ):
                    if mt[i + r[0]][j + r[1]] == "#" or mapping[i + r[0]][
                        j + r[1]
                    ] < c + 100 + abs(im) + abs(jm):
                        continue
                    res += 1
                    shortcut.append(mapping[i + r[0]][j + r[1]] - c - (im + jm))

        return res, shortcut

    res = 0
    short = []
    for i in range(1, len(mt)):
        for j in range(1, len(mt[0])):
            ans = process_diff_2(i, j)
            res += ans[0]
            short += ans[1]
    print(res)

    maze = mt
    total = 0
    for y in range(1, len(maze) - 1):
        for x in range(1, len(maze[0]) - 1):
            if maze[y][x] != "#":
                for x1 in range(x - 20, x + 21):
                    for y1 in range(y - 20 + abs(x - x1), y + 21 - abs(x - x1)):
                        if (
                            0 < y1 < len(maze) - 1
                            and 0 < x1 < len(maze[0]) - 1
                            and maze[y1][x1] != "#"
                            and mapping[y1][x1]
                            - mapping[y][x]
                            - abs(x1 - x)
                            - abs(y1 - y)
                            >= 100
                        ):
                            total += 1
    return total


if __name__ == "__main__":
    print(main())
