"""Advent of Code 2024 - Day 10 - Part Two"""

from shared import *


def main():
    def find_starts(mt):
        starts = []
        for i in range(len(mt)):
            for j in range(len(mt[0])):
                if mt[i][j] == 0:
                    starts.append((i, j))
        return starts

    start_points = find_starts(mt)
    moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    queue = []
    found = 0
    mapping = [[0 for i in range(len(mt[0]))] for j in range(len(mt))]

    def process_queue(point, queue, mapping):
        x, y = point
        val = mt[x][y]
        if val == 9:
            nonlocal found
            found += 1
            return 0
        for move in moves:
            new_x = x + move[0]
            new_y = y + move[1]
            if (
                new_x >= 0
                and new_x < len(mt)
                and new_y >= 0
                and new_y < len(mt[0])
                and mt[new_x][new_y] - val == 1
            ):
                queue.append((new_x, new_y))

    total = 0
    for start in start_points:
        found = 0
        queue.append(start)
        # mapping = [[0 for i in range(len(mt[0]))] for j in range(len(mt))]

        while len(queue) > 0:
            process_queue(queue.pop(0), queue, mapping)
        total += found
    return total


if __name__ == "__main__":
    print(main())
