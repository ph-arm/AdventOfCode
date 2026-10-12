"""Advent of Code 2024 - Day 06 - Part Two"""

from shared import *

DIR_INDEX = {"^": 0, ">": 1, "v": 2, "<": 3}
DIRS = [(-1, 0), (0, 1), (1, 0), (0, -1)]  # up, right, down, left


def main():
    grid = [row for row in mt if row]
    rows, cols = len(grid), len(grid[0])
    sr, sc, sd = x, y, DIR_INDEX[current_dir]

    def patrol(obstacle):
        """Walk from the start; return visited cells, or None if it loops."""
        r, c, d = sr, sc, sd
        seen = set()
        while True:
            state = (r, c, d)
            if state in seen:
                return None
            seen.add(state)
            dr, dc = DIRS[d]
            nr, nc = r + dr, c + dc
            if not (0 <= nr < rows and 0 <= nc < cols):
                return {(vr, vc) for vr, vc, _ in seen}
            if grid[nr][nc] == "#" or (nr, nc) == obstacle:
                d = (d + 1) % 4
            else:
                r, c = nr, nc

    # Only cells on the original patrol path can change the outcome.
    path = patrol(None)
    return sum(patrol(cell) is None for cell in path - {(sr, sc)})


if __name__ == "__main__":
    print(main())
