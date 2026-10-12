"""Advent of Code 2024 - Day 06 - Part One"""

from shared import *


def main():
    x, y, current_dir = x_start, y_start, dir_start
    mapper = [[0 for i in range(len(mt))] for j in range(len(mt[0]))]
    count_path = 0

    def track_path(i, j):
        if mapper[i][j] == 1:
            return 0
        mapper[i][j] = 1
        nonlocal count_path
        count_path += 1

    def move(current_dir, i, j, mt):
        if current_dir == "^":
            while i > 0:
                track_path(i, j)
                if mt[i - 1][j] == "#":
                    dir_new = directions[(directions.index(current_dir) + 1) % 4]
                    return i, j, dir_new
                i -= 1
            track_path(i, j)
            return -1, j, current_dir

        if current_dir == "v":
            while i < len(mt) - 1:
                track_path(i, j)
                if mt[i + 1][j] == "#":
                    dir_new = directions[(directions.index(current_dir) + 1) % 4]
                    return i, j, dir_new
                i += 1
            track_path(i, j)
            return -1, j, current_dir
        if current_dir == "<":
            while j > 0:
                track_path(i, j)
                if mt[i][j - 1] == "#":
                    dir_new = directions[(directions.index(current_dir) + 1) % 4]
                    return i, j, dir_new
                j -= 1
            track_path(i, j)
            return i, -1, current_dir
        if current_dir == ">":
            while j < len(mt[0]) - 1:
                track_path(i, j)
                if mt[i][j + 1] == "#":
                    dir_new = directions[(directions.index(current_dir) + 1) % 4]
                    return i, j, dir_new
                j += 1
            track_path(i, j)
            return i, -1, current_dir
        raise Exception("Invalid direction")

    while x >= 0 and y >= 0:
        x, y, current_dir = move(current_dir, x, y, mt)
    return count_path


if __name__ == "__main__":
    print(main())
