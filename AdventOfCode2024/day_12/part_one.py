"""Advent of Code 2024 - Day 12 - Part One"""

from shared import *


def main():
    mappings = [[0 for i in mt[0]] for j in mt]
    moves = [(1, 0), (0, 1), (-1, 0), (0, -1)]

    def find_region(i, j):
        if mappings[i][j] > 0:
            return 0, 0, ""
        r = mt[i][j]
        mappings[i][j] = 1
        queue = [(i, j)]
        cells = [(i, j)]
        while queue:
            x, y = queue.pop(0)
            for move in moves:
                nx, ny = x + move[0], y + move[1]
                if 0 <= nx < len(mt) and 0 <= ny < len(mt[0]):
                    if mappings[nx][ny] == 0 and mt[nx][ny] == r:
                        mappings[nx][ny] = 1
                        queue.append((nx, ny))
                        cells.append((nx, ny))
        a = len(cells)
        p = 0
        for x, y in cells:
            for move in moves:
                nx, ny = x + move[0], y + move[1]
                if not (0 <= nx < len(mt) and 0 <= ny < len(mt[0])) or mt[nx][ny] != r:
                    p += 1
        return p, a, r

    a = 0
    r = 0
    for i in range(len(mt)):
        for j in range(len(mt[0])):
            pl, al, reg = find_region(i, j)
            r += pl * al
            a += al
    return r


if __name__ == "__main__":
    print(main())
