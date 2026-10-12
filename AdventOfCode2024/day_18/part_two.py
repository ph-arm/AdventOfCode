"""Advent of Code 2024 - Day 18 - Part Two"""

import shared
from shared import *


def main():
    for i in range(71):
        shared.mt[i] = [0] * 71

    timing = -1
    while True:
        timing += 1
        cand = mem_cor[timing]
        cx, cy = int(cand[0]), int(cand[1])
        shared.mt[cy][cx] = 1  # corrupt in shared's grid

        # Re-run BFS
        shared.mapping = [[-1] * 71 for _ in range(71)]
        x, y = 0, 0
        queue = [[0, 0, 0]]
        found = False

        while queue:
            x, y, v = queue.pop(0)
            if x == 70 and y == 70:
                found = True
                break
            queue += process(x, y, v)
            queue.sort(key=lambda q: q[2])

        if not found:
            return f"{cx},{cy}"


if __name__ == "__main__":
    print(main())
